---
title: "Background operations (Preview) (Microsoft Dataverse) | Microsoft Docs"
description: "Learn how to invoke custom apis asynchronously." 
ms.custom: intro-internal
ms.date: 04/29/2023
ms.reviewer: jdaly
ms.topic: article
author: Anweshi
ms.subservice: dataverse-developer
ms.author: anweshid
search.audienceType: 
  - developer
contributors:
  - cwithfourplus
  - JimDaly
---

# Background operations (Preview)

[!INCLUDE [preview-include](../../cards/includes/preview-include.md)]

Use background operations to send requests that Dataverse processes asynchronously. Send a request this way when you don't want to maintain a connection awaiting potentially long running operations.

Dataverse immediately responds that the request is accepted and there are several ways to monitor whether the request ultimately succeeds. When the operation succeeds, you can retrieve the result. Send a request this way when you don't want to maintain a connection awaiting potentially long running operations.

Background operations requires that the operation performed is defined as a custom API. More information:

- [Create and use custom APIs](custom-api.md)
- [Retrieve data about custom APIs](custom-api-tables.md#retrieve-data-about-custom-apis)


## Required Privileges

To perform a background operation, the initiating user must have read and write access to the `backgroundoperation` table. Assign the `prvReadbackgroundoperation` and `prvWritebackgroundoperation` privileges to grant this access. More information:

- [Edit a security role](/power-platform/admin/create-edit-security-role#edit-a-security-role)
- <xref:Microsoft.Crm.Sdk.Messages.AddPrivilegesRoleRequest>
- [AddPrivilegesRole Action](xref:Microsoft.Dynamics.CRM.AddPrivilegesRole)

<!-- TODO We need a generic topic to describe adding privileges to security roles programmatically: workitem 3342875 -->


## Request asynchronous processing

You can request asynchronous processing of a request using both the SDK for .NET and Dataverse Web API.

### [SDK for .NET](#tab/sdk)

Use the `ExecuteBackgroundOperation` message.

> [!NOTE]
> The SDK does not currently have `ExecuteBackgroundOperation` request and response classes. Until these classes are added, you will will need to use the base [OrganizationRequest](xref:Microsoft.Xrm.Sdk.OrganizationRequest) and [OrganizationResponse](xref:Microsoft.Xrm.Sdk.OrganizationResponse) classes as described in [Use messages with the Organization service](org-service/use-messages.md)

The `ExecuteBackgroundOperation` message has the following input parameters:

|Name  |Type|Description  |
|---------|---------|---------|
|`Request`|[OrganizationRequest](xref:Microsoft.Xrm.Sdk.OrganizationRequest)|(Required) The request you want to have processed asynchronously. The Dataverse message for this request must be implemented as a custom API.|
|`CallbackUri`|string| (Optional) Dataverse sends a POST HTTP request to this Url when the operation is completed. More information: [Request a callback](#request-a-callback)|

The `ExecuteBackgroundOperation` message has the following output parameters:

|Name|Type|Description |
|---------|---------|---------|
|`BackgroundOperationId`|Guid| The ID of the background operation table row you can use to monitor the processing of your request or cancel it. |
|`Location`|string| The status monitor resource URL to use to retrieve the status of your request or cancel it.|

The following static method uses `ExecuteBackgroundOperation` with a custom API named `sample_ExportDataUsingFetchXmlToAnnotation`. This custom API is described in [Sample: ExportDataUsingFetchXmlToAnnotation custom API](org-service/samples/export-data-fetchxml-annotation-custom-api-sample.md).

```csharp
static void SendRequestAsynchronously(IOrganizationService service)
{
    //Create a request for message defined as a custom API to run in the background
    var asyncRequest = new OrganizationRequest("sample_ExportDataUsingFetchXmlToAnnotation");

    //Setting input parameters for the message
    asyncRequest.Parameters["FetchXml"] =  @"<fetch version='1.0' output-format='xml-platform' mapping='logical'>
                                                <entity name='account'>
                                                      <attribute name='accountid'/>
                                                      <attribute name='name'/>  
                                                </entity>
                                             </fetch>"; 

    //Create a request to execute the message in the background
    var request = new OrganizationRequest("ExecuteBackgroundOperation")
    {
        Parameters = 
        {
            {"Request", asyncRequest }
        }
    };

    //Execute the background operation request
    var response = service.Execute(request);

    Console.WriteLine($"BackgroundOperationId: {response["BackgroundOperationId"]}");
    Console.WriteLine($"Location: {response["Location"]}");
}
```

**Output:**

```
BackgroundOperationId: f86f8700-6e21-4a39-aa6a-db3bb306b884
Location: [Organization URI]/api/backgroundoperation/f86f8700-6e21-4a39-aa6a-db3bb306b884
```

More information:

- [IOrganizationService Interface](xref:Microsoft.Xrm.Sdk.IOrganizationService)
- [Use messages with the Organization service](org-service/use-messages.md)



### [Web API](#tab/webapi)

Send your request with the `Prefer: respond-async` header. More information: [Prefer Headers](webapi/compose-http-requests-handle-errors.md#prefer-headers)

The following example uses the `sample_ExportDataUsingFetchXmlToAnnotation` custom api described in [Sample: ExportDataUsingFetchXmlToAnnotation custom API](org-service/samples/export-data-fetchxml-annotation-custom-api-sample.md)

**Request**

```http
POST [Organization URI]/api/data/v9.2/sample_ExportDataUsingFetchXmlToAnnotation HTTP/1.1
Content-Type: application/json
Accept: application/json
OData-MaxVersion: 4.0
OData-Version: 4.0
Prefer: respond-async

{
    "FetchXml": "<fetch version='1.0' output-format='xml-platform' mapping='logical'>
                    <entity name='account'>
                        <attribute name='accountid'/>
                        <attribute name='name'/>  
                    </entity>
                </fetch>"
}
```

**Response**

```http
HTTP/1.1 202 Accepted
Location: [Organization URI]/api/backgroundoperation/110eaa68-db17-4115-ad74-d185823fc088
x-ms-dyn-backgroundoperationid: 110eaa68-db17-4115-ad74-d185823fc088
Preference-Applied: respond-async

```

- The `x-ms-dyn-backgroundoperationid` response header value is the ID for the background operation row for the request.
- The response [Location](https://developer.mozilla.org/docs/Web/HTTP/Headers/Location) header contains a URL that represents the *status monitor resource*


You can use either URL to manage background operations, but the methods and responses are different.

---

## Manage background operations

When you send a request to be processed in the background, the response will include two values that represent different methods you can use to manage background operations.

- The ID for a row in the `backgroundoperations` table.

   Use this value with either the SDK or Web API to retrieve or update data from the `backgroundoperations` table. More information:

   - [Background Operations table](#background-operations-table)
   - [Poll the background operation table](#poll-the-background-operation-table)
   - [Cancel background operation by updating backgroundoperations](#cancel-background-operation-by-updating-backgroundoperations)


- A `Location` URL that represents the *status monitor resource*.

   > [!IMPORTANT]
   > The status monitor resource is not the Web API `backgroundoperation` EntityType resource.
   > 
   > |URL |Example|
   > |---------|---------|
   > |Status Monitor Resource|`[Organization URI]/api/backgroundoperation/110eaa68-db17-4115-ad74-d185823fc088`|
   > |`backgroundoperation` EntityType|`[Organization URI]/api/data/v9.0/backgroundoperations(110eaa68-db17-4115-ad74-d185823fc088)`|   

   The status monitor resource is not part of the Dataverse Web API. Notice that the URL does not contain `/data/v9.2/`. This resource supports only `GET` and `DELETE` operations. You can use this value to poll and cancel background operations. More information:

   - [Poll the status monitor resource](#poll-the-status-monitor-resource)
   - [Send a DELETE request to the status monitor resource](#send-a-delete-request-to-the-status-monitor-resource)
  

### Background Operations table

The Background Operation table contains information about requests to process asynchronously. It is identified by the entity name `backgroundoperation` and the entity set name `backgroundoperations`.

<!-- TODO: add link to Background Operation Entity table reference when regenerated -->

Background operation has the following columns you can use to manage the status of background operations.


|Display Name<br />`SchemaName`<br />`LogicalName`|Type |Description|
|---------|---------|---------|
|**Background Operation**<br />`BackgroundOperationId`<br />`backgroundoperationid`|Uniqueidentifier|The primary key|
|**Status** <br />`StateCode`<br />`backgroundoperationstatecode`|Picklist|State of the background operation.<br />**Options:**<br />Value: `0`, Label: **Ready**<br />Value: `2`, Label: **Locked**<br />Value: `3`, Label: **Completed**|
|**Status Reason** <br />`StatusCode`<br />`backgroundoperationstatuscode`|Picklist|Status of the background operation.<br />**Options:**<br />Value: `0`, Label: **Waiting For Resources** (State:Ready)<br />Value: `20`, Label: **In Progress** (State:Locked)<br />Value: `22`, Label: **Canceling**  (State:Locked)<br />Value: `30`, Label: **Succeeded**  (State:Completed)<br />Value: `31`, Label: **Failed** (State:Completed)<br />Value: `32`, Label: **Canceled** (State:Completed)|
|**Name**<br />`Name`<br />`name`|String|The name of the background operation.|
|**DisplayName**<br />`DisplayName`<br />`displayname`|String|The display name of background operation.|
|**Input Parameters**<br />`InputParameters`<br />`inputparameters`|Memo|The input parameters that were supplied to start background operation.<br />This is a JSON serialized array of `Key` and `Value`.|
|**Output Parameters**<br />`OutputParameters`<br />`outputparameters`|Memo|The response of background operation<br />This is a JSON serialized array of `Key` and `Value`.|
|**Start Time**<br />`StartTime`<br />`starttime`|DateTime|When the background operation started execution|
|**End Time**<br />`EndTime`<br />`endtime`|DateTime|When the background operation finished execution|
|**Retry Count**<br />`RetryCount`<br />`retrycount`|Integer|The number of times background operation was retried.
|**Error Code**<br />`ErrorCode`<br />`errorcode`|Integer|The error code when the background operation fails|
|**Error Message**<br />`ErrorMessage`<br />`errormessage`|Memo|The error message when the background operation fails|
|**Run As**<br />`RunAs`<br />`runas`|String|The `systemuserid` of the `systemuser` used to execute the background operation|
|**Created On**<br />`CreatedOn`<br />`createdon`|DateTime|When the record was created|
|**Time to live**<br />`TTLInSeconds`<br />`ttlinseconds`|Integer|Time to live in seconds after which the record is automatically deleted. Default value is 90 days|


### Poll the background operation table

After initiating a background operation, you may want to check its status. This process is commonly known as *status polling*. We recommend that you avoid excessive polling because it can negatively impact performance. If needed, we suggest polling at an interval of one minute or more.

This request returns the status of the background operation, and if the operation is complete, it provides the output of the Custom API.If there was an error during execution, you receive an error message and code.

How you do this depends on whether you are using the SDK or Web API.

#### [SDK for .NET](#tab/sdk)

With the SDK, you can query the background operation table to retrieve these column values: `backgroundoperationstatecode`,`backgroundoperationstatuscode`,`outputparameters`,`errorcode`,`errormessage`

```csharp
static void PollBackgroundOperationRequest(IOrganizationService service, Guid backgroundOperationId)
{
    // List of columns that will help to get status, output and error details if any
    var columnSet = new ColumnSet(
        "backgroundoperationstatecode",
        "backgroundoperationstatuscode",
        "outputparameters",
        "errorcode",
        "errormessage");

    try
    {
        // Get the entity with all the required columns
        var backgroundOperation = service.Retrieve("backgroundoperation", backgroundOperationId, columnSet);

        Console.WriteLine($"State Code: {backgroundOperation.FormattedValues["backgroundoperationstatecode"]}");
        Console.WriteLine($"Status Code: {backgroundOperation.FormattedValues["backgroundoperationstatuscode"]}");
        Console.WriteLine($"Output Parameters:");

        // Deserialize the Output Parameters into KeyValuePair<string, string>
        List<KeyValuePair<string, string>>? output = 
            System.Text.Json.JsonSerializer
            .Deserialize<List<KeyValuePair<string, string>>>((string)backgroundOperation["outputparameters"]);

        output.ForEach(x => {
            Console.WriteLine($"\t{x.Key}: {x.Value}");
        });

        Console.WriteLine($"Error Code: {backgroundOperation.GetAttributeValue<string>("errorcode")}");
        Console.WriteLine($"Error Message: {backgroundOperation.GetAttributeValue<string>("errormessage")}");
    }
    // Catch platform errors
    catch (FaultException<OrganizationServiceFault> ex)
    {
        Console.WriteLine($"ErrorCode:{ex.Detail.ErrorCode}");
        Console.WriteLine($"Message:{ex.Message}");
    }
    // Catch other errors
    catch (Exception error)
    {
        Console.WriteLine($"Some other error occurred: '{error.Message}'");
    }
}
```

**Waiting Output**

```console
State Code: Locked
Status Code:  In Progress
Output Parameters:  
Error Code:  
Error Message:  
```

**Complete Output**

```console
State Code: Completed
Status Code:  Succeeded
Output Parameters:
        outputParam1: {value},
        outputParam2: {value},
        outputParam3: {value}
Error Code:  
Error Message:  
```

**Error Output**

```console
State Code: Completed
Status Code:  Failed
Output Parameters: 
Error Code:  500
Error Message:  This is a sample error message 
```

**Id not found**

```console
ErrorCode:-2147185406
Message:The HTTP status code of the response was not expected (404).

Status: 404
Response:
{"error":{"message":"Could not find item '110eaa68-db17-4115-ad74-d185823fc089'.","details":[{"message":"\r\nErrors : [\r\n  \"Resource Not Found. Learn more: https://aka.ms/cosmosdb-tsg-not-found\"\r\n]\r\n"}]}}
```

If the error is produced by the platform, it will have an integer value that corresponds to one of the codes listed in the [Web service error codes](reference/web-service-error-codes.md). However, if the error is not caused by the platform, its value will be set to zero.

<!-- I don't really understand what this means. How do I get the error?
Even a 404 error returns -2147185406, IsvAbortedNotFound error. -->

#### [Web API](#tab/webapi)

With the Web API, you can also query the backgroundoperation EntityType resource.

**Request**

```http
GET [Organization URI]/api/data/v9.2/backgroundoperations(<backgroundoperationid value>)?$select=backgroundoperationstatecode,backgroundoperationstatuscode,outputparameters,errorcode,errormessage
Content-Type: application/json
Accept: application/json
OData-MaxVersion: 4.0
OData-Version: 4.0
Prefer: odata.include-annotations="OData.Community.Display.V1.FormattedValue"
```

**Response**

```http
HTTP/1.1 200 OK
Content-Type: application/json; odata.metadata=minimal
OData-Version: 4.0
Preference-Applied: odata.include-annotations="OData.Community.Display.V1.FormattedValue"

{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#backgroundoperations(backgroundoperationstatecode,backgroundoperationstatuscode,outputparameters,errorcode,errormessage)/$entity",
    "@odata.etag": "W/\"92030eaa-0000-0200-0000-644d7c300000\"",
    "backgroundoperationstatecode@OData.Community.Display.V1.FormattedValue": "Completed",
    "backgroundoperationstatecode": 3,
    "backgroundoperationstatuscode@OData.Community.Display.V1.FormattedValue": "Succeeded",
    "backgroundoperationstatuscode": 30,
    "outputparameters": "[{\"Key\":\"AnnotationId\",\"Value\":\"bb26025c-cbe6-ed11-a7c6-000d3a9933c9\"}]",
    "errorcode": null,
    "errormessage": null,
    "backgroundoperationid": "<backgroundoperationid value>",
    "versionnumber": 638183964640916096
}
```

---

### Poll the status monitor resource

You can poll the status monitor resource.



If the error is produced by the platform, it will have an integer value that corresponds to one of the codes listed in the [Web service error codes](reference/web-service-error-codes.md). However, if the error is not caused by the platform, its value will be set to zero.

<!-- I don't really understand what this means. How do I get the error?
Even a 404 error returns -2147185406, IsvAbortedNotFound error. -->



Send a request to the status monitor URL that was returned with the `Location` response header of the original request.

**Request**

```http
GET [Organization URI]/api/backgroundoperation/{backgroundoperationid}
Content-Type: application/json  
```

**Response**

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  backgroundOperationErrorCode: {INT},
  backgroundOperationErrorMessage: {string},
  backgroundOperationStateCode: {INT},
  backgroundOperationStatusCode: {INT},
  outputParam1: {value},
  outputParam2: {value},
  outputParam3: {value},
}
```

`backgroundOperationErrorCode` and `backgroundOperationErrorMessage` values are only included when an error occurs. Output parameters are only included when the operation completes successfully.

---


### Request a callback

You can specify a URL in your request to receive a callback when the operation is completed. Dataverse uses this URL to send a `POST` request with the following payload:

```json
{
   backgroundOperationId: {GUID},
   backgroundOperationStateCode: {INT},
   backgroundOperationStatusCode: {INT},
   backgroundOperationErrorCode: {INT},
   backgroundOperationErrorMessage: {string},
   location: {locationURL}
}
```

`backgroundOperationErrorCode` and `backgroundOperationErrorMessage` are only included when an error occurs. The callback payload does not include any output parameters. The site that receives the callback can use the location url to retrieve any results.

> [!NOTE]
>
> - If the URL requires authentication, the URL must be a self-sufficient shared access signature (SAS) URL. It isn't possible to include any additional headers to include API keys or tokens for authentication. More information: [Grant limited access to Azure Storage resources using shared access signatures (SAS)](/azure/storage/common/storage-sas-overview)
> - You may want to use a site like [webhook.site](https://webhook.site/) to test the callback URL.

How you do request a callback depends on whether you are using the SDK or Web API.

The following examples show sending a request using a webhook to [webhook.site](https://webhook.site/) for testing:

#### [SDK for .NET](#tab/sdk)

With the SDK, set the `ExecuteBackgroundOperation.CallbackUri` parameter to the URL to send the request.

```csharp
static void SendRequestAsynchronouslyWithCallback(IOrganizationService service)
{
    //Create a request for main workload i.e. Custom API that need to run in background
    var asyncRequest = new new OrganizationRequest("sample_ExportDataUsingFetchXmlToAnnotation");

    //Setting parameters of main workload
    createAccountRequest.Parameters["FetchXml"] =  @"<fetch version='1.0' output-format='xml-platform' mapping='logical'>
                                                            <entity name='account'>
                                                                <attribute name='accountid'/>
                                                                <attribute name='name'/>  
                                                            </entity>
                                                        </fetch>";

    //Create a request to execute main workload in background
    var request = new OrganizationRequest("ExecuteBackgroundOperation")
    {
        Parameters = 
        {
            {"Request", asyncRequest },
            {"CallbackUri", "https://webhook.site/<id>" }
        }
    };

    //Issue a background operation request
    var response = service.Execute(request);

    Console.WriteLine($"BackgroundOperationId: {response["BackgroundOperationId"]}");
    Console.WriteLine($"Location: {response["Location"]}");
}
```

#### [Web API](#tab/webapi)

With the Web API, set the `Prefer` request header with this value:

`Prefer: respond-async, callback; url="<url>"`

<!-- 
Spec 8.2.8.2 Preference odata.callback says this should be 'odata.callback' rather than just 'callback'.. 
http://docs.oasis-open.org/odata/odata/v4.0/errata03/os/complete/part1-protocol/odata-v4.0-errata03-os-part1-protocol-complete.html#_Toc445374558
-->

**Request**

```http
POST [Organization URI]/api/data/v9.2/sample_ExportDataUsingFetchXmlToAnnotation 
Content-Type: application/json
Accept: application/json
Prefer: respond-async, callback; url="https://webhook.site/<id>"

{
    "FetchXml": "<fetch version='1.0' output-format='xml-platform' mapping='logical'>
                    <entity name='account'>
                        <attribute name='accountid'/>
                        <attribute name='name'/>  
                    </entity>
                </fetch>"
}
```

**Response**

```http
HTTP/1.1 202 Accepted
Preference-Applied: callback
x-ms-dyn-backgroundoperationid: f86f8700-6e21-4a39-aa6a-db3bb306b884
location: [Organization URI]/api/backgroundoperation/f86f8700-6e21-4a39-aa6a-db3bb306b884

{
   backgroundOperationId: f86f8700-6e21-4a39-aa6a-db3bb306b884,
   location: [Organization URI]/api/backgroundoperation/f86f8700-6e21-4a39-aa6a-db3bb306b884
}
```

---

## Cancel background operations

If you initiate a background operation, you may sometimes need to cancel its execution.

- If the operation hasn't begun execution yet, the platform won't execute it.
- If the execution has already started, the platform won't abort the operation.
- If an error occurs during the execution, the platform won't retry it if a cancellation request was made.

There are two ways to cancel a background operation:

- [Cancel background operation by updating backgroundoperations](#cancel-background-operation-by-updating-backgroundoperations)
- [Send a DELETE request to the status monitor resource](#send-a-delete-request-to-the-status-monitor-resource)

### Cancel background operation by updating backgroundoperations

Update the row in the `backgroundoperations` table to set the the `backgroundoperationstatecode` to 2 (**Locked**) and `backgroundoperationstatuscode` to 22 (**Cancelling**)

### [SDK for .NET](#tab/sdk)

```csharp
static void CancelBackgroundOperationRequest(IOrganizationService service, Guid backgroundOperationId)
{
    var backgroundOperation = new Entity("backgroundoperation");
                    
    backgroundOperation.Id = backgroundOperationId;

    //Set state as Locked
    backgroundOperation["backgroundoperationstatecode"] = new OptionSetValue(2); 

    //Set status as Cancelling
    backgroundOperation["backgroundoperationstatuscode"] = new OptionSetValue(22);

    service.Update(backgroundOperation);
}
```

### [Web API](#tab/webapi)

**Request**

```http
PATCH [Organization URI]/api/data/v9.2/backgroundoperations(110eaa68-db17-4115-ad74-d185823fc088) HTTP/1.1
Accept: application/json
OData-MaxVersion: 4.0
OData-Version: 4.0
If-Match: *
Content-Type: application/json

{
    "backgroundoperationstatecode": 2,
    "backgroundoperationstatuscode": 22
}
```

**Response**

```http
HTTP/1.1 204 No Content
OData-Version: 4.0
```

---


### Send a DELETE request to the status monitor resource

**Request**

```http
DELETE [Organization URI]/api/backgroundoperation/{backgroundoperationid}
```

**Response**

```http
HTTP/1.1 200 Ok

{
    backgroundOperationStateCode: 2,
    backgroundOperationStatusCode: 22
}
```


## Receive notification of result

Background operations can be performed with the option of receiving notification through a callback URL upon completion, or by subscribing to the SDK Message called **OnBackgroundOperationComplete**, which is triggered each time a background operation finishes. 

To configure this message, refer to the [Register a plug-in](register-plug-in.md) instructions, and ensure that you set the message name as **OnBackgroundOperationComplete** in asynchronous mode. Additionally, set the 'Auto Delete' to 'true' so that the [System Job (AsyncOperation)](reference/entities/asyncoperation.md) record is automatically removed, and set the stage to **Post Operation** or higher.


## Retries

If an error occurs during execution of the request, it is retried up to three times. These retries use a [exponential backoff strategy](https://wikipedia.org/wiki/Exponential_backoff).