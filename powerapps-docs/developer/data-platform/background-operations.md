---
title: Background operations (preview)
description: Learn how to use background operations to send Dataverse requests invoked as custom APIs asynchronously.
ms.collection: get-started
ms.date: 06/05/2023
ms.topic: how-to
ms.subservice: dataverse-developer
author: sumadhey
ms.author: sumadhey
ms.reviewer: jdaly
search.audienceType: 
  - developer
contributors:
  - JimDaly
  - cwithfourplus
  - Anweshi
ms.custom: bap-template
---

# Background operations (preview)

[!INCLUDE [preview-banner](~/../shared-content/shared/preview-includes/preview-banner.md)]

Use background operations to send requests that Dataverse processes asynchronously. Background operations are useful when you don't want to maintain a connection while a request runs.

When a background operation completes, you can get notified in either of two ways:

- [Include a callback URL with your request](#request-a-callback).
- [Subscribe to the `OnBackgroundOperationComplete` event](#subscribe-to-the-onbackgroundoperationcomplete-event).

You can retrieve the result of a background operation in either of two ways:

- [Poll the background operations table](#poll-the-background-operations-table).
- [Poll the status monitor resource](#poll-the-status-monitor-resource).

To run a request in the background, the operation must be defined as a custom API. Learn how to [create and use custom APIs](custom-api.md) and [retrieve data about custom APIs](custom-api-tables.md#retrieve-data-about-custom-apis).

Custom APIs use plug-ins to perform data operations. Like all Dataverse plug-ins, these plug-ins have a two-minute execution time-out. Sending the request asynchronously doesn't provide more execution time.

## Required privileges

To perform a background operation, the initiating user must have read and write access to the `backgroundoperations` table. Assign the `prvReadbackgroundoperation` and `prvWritebackgroundoperation` privileges to grant this access.

- SDK: <xref:Microsoft.Crm.Sdk.Messages.AddPrivilegesRoleRequest>
- Web API: [AddPrivilegesRole Action](xref:Microsoft.Dynamics.CRM.AddPrivilegesRole)

 [Learn how to edit a security role](/power-platform/admin/create-edit-security-role#edit-a-security-role).

## Request asynchronous processing

You can run asynchronous requests in the background using either the SDK for .NET or the Dataverse Web API.

Examples in this article use a custom API named `sample_ExportDataUsingFetchXmlToAnnotation`. This custom API is described in [Sample: ExportDataUsingFetchXmlToAnnotation custom API](org-service/samples/export-data-fetchxml-annotation-custom-api-sample.md).

### [SDK for .NET](#tab/sdk)

Use the `ExecuteBackgroundOperation` message.

The SDK doesn't have `ExecuteBackgroundOperation` request and response classes. Until these classes are added, use the base [OrganizationRequest](xref:Microsoft.Xrm.Sdk.OrganizationRequest) and [OrganizationResponse](xref:Microsoft.Xrm.Sdk.OrganizationResponse) classes as described in [Use messages with the organization service](org-service/use-messages.md).

The following table describes the input parameters for the `ExecuteBackgroundOperation` message.

|Name|Type|Description|
|---------|---------|---------|
|`Request`|[OrganizationRequest](xref:Microsoft.Xrm.Sdk.OrganizationRequest)|(Required) Contains the request you want to have processed asynchronously. The Dataverse message for the request must be implemented as a custom API.|
|[`CallbackUri`](#request-a-callback)|string| (Optional) Dataverse sends a POST HTTP request to this URL when the operation is completed.|

The following table describes the output parameters for the `ExecuteBackgroundOperation` message.

|Name|Type|Description|
|---------|---------|---------|
|`BackgroundOperationId`|Guid|Identifies the background operation table row you can use to monitor or cancel the processing of your request.|
|`Location`|string|Identifies the status monitor resource URL you can use to retrieve the status of your request or to cancel it.|

The following static method uses `ExecuteBackgroundOperation` with the `sample_ExportDataUsingFetchXmlToAnnotation` custom API.

```csharp
static void SendRequestAsynchronously(IOrganizationService service)
{
    //Create a request for message defined as a custom API to run in the background
    var asyncRequest = new OrganizationRequest("sample_ExportDataUsingFetchXmlToAnnotation")
    {
        Parameters =
        {
            {"FetchXml",  @"<fetch version='1.0'  
                                    output-format='xml-platform' 
                                    mapping='logical'>
                                <entity name='account'>
                                    <attribute name='accountid'/>
                                    <attribute name='name'/>  
                                </entity>
                            </fetch>" }
        }
    };

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

```text
BackgroundOperationId: <backgroundoperationid value>
Location: [Organization URI]/api/backgroundoperation/<backgroundoperationid value>
```

Learn more about the [IOrganizationService interface](xref:Microsoft.Xrm.Sdk.IOrganizationService) and how to [use messages with the organization service](org-service/use-messages.md).

### [Web API](#tab/webapi)

Send your request with the `Prefer: respond-async` header. [Learn more about `Prefer` headers](webapi/compose-http-requests-handle-errors.md#prefer-headers).

**Request:**

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

**Response:**

```http
HTTP/1.1 202 Accepted
Location: [Organization URI]/api/backgroundoperation/<backgroundoperationid value>
x-ms-dyn-backgroundoperationid: <backgroundoperationid value>
Preference-Applied: respond-async

```

- The `x-ms-dyn-backgroundoperationid` response header value is the ID for the background operation row for the request.
- The response [Location](https://developer.mozilla.org/docs/Web/HTTP/Headers/Location) header contains a URL that represents the status monitor resource.

[Learn how to use Web API actions](webapi/use-web-api-actions.md).

---

## Manage background operations

When you send a request to be processed in the background, the response includes two values that represent different methods you can use to monitor or cancel background operations.

- Use the ID of a row in the [`backgroundoperations` table](#background-operations-table) to retrieve or update data in the table:

  - [Poll the background operations table](#poll-the-background-operations-table)
  - [Cancel a background operation by updating backgroundoperations](#cancel-a-background-operation-by-updating-backgroundoperations)

- Use the `Location` URL, which represents the status monitor resource, to poll and cancel background operations:

  - [Poll the status monitor resource](#poll-the-status-monitor-resource).
  - [Send a DELETE request to the status monitor resource](#send-a-delete-request-to-the-status-monitor-resource).

   > [!IMPORTANT]
   > The status monitor resource is not the Web API `backgroundoperation` EntityType resource.
   >
   > |URL|Example|
   > |---------|---------|
   > |Status Monitor Resource|`[Organization URI]/api/backgroundoperation/<backgroundoperationid value>`|
   > |`backgroundoperation` EntityType resource|`[Organization URI]/api/data/v9.2/backgroundoperations(<backgroundoperationid value>)`|

   The status monitor resource isn't part of the Dataverse Web API. Notice that the URL doesn't contain `/data/v9.2/`. The status monitor resource supports only GET and DELETE operations and doesn't have the same behaviors as the Web API `backgroundoperation` EntityType resource.

Querying the background operations table or status monitor resource to check on requests is commonly known as *status polling*. We recommend that you avoid excessive polling because it can negatively affect performance. If needed, we suggest polling at an interval of one minute or more.

## Background operations table

The background operations table contains information about requests to process asynchronously. This table has the logical name `backgroundoperation` and the entity set name `backgroundoperations`. [Learn about the backgroundoperation EntityType](xref:Microsoft.Dynamics.CRM.backgroundoperation).

The following table describes the columns you can use to manage the status of background operations.

|Display name<br/>Schema name<br/>Logical name|Type|Description|
|---------|---------|---------|
|Background Operation<br/>`BackgroundOperationId`<br/>`backgroundoperationid`|Uniqueidentifier|The primary key|
|Status<br/>`StateCode`<br/>`backgroundoperationstatecode`|Picklist|State of the background operation<br/><br/>Options:<br/>- Value: `0`, Label: **Ready**<br/>- Value: `2`, Label: **Locked**<br/>- Value: `3`, Label: **Completed**|
|Status Reason<br/>`StatusCode`<br/>`backgroundoperationstatuscode`|Picklist|Status of the background operation<br/><br/>Options:<br/>- Value: `0`, Label: **Waiting For Resources** (State:Ready)<br/>- Value: `20`, Label: **In Progress** (State:Locked)<br/>- Value: `22`, Label: **Canceling** (State:Locked)<br/>- Value: `30`, Label: **Succeeded** (State:Completed)<br/>- Value: `31`, Label: **Failed** (State:Completed)<br/>- Value: `32`, Label: **Canceled** (State:Completed)|
|Name<br/>`Name`<br/>`name`|String|The `UniqueName` of the custom API used for the background operation|
|DisplayName<br/>`DisplayName`<br/>`displayname`|String|The `DisplayName` of the custom API used for the background operation|
|Input Parameters<br/>`InputParameters`<br/>`inputparameters`|Memo|The input parameters that were supplied to start the background operation<br/><br/>This string is a JSON serialized array of `Key` and `Value`.|
|Output Parameters<br/>`OutputParameters`<br/>`outputparameters`|Memo|The response of the background operation<br/><br/>This string is a JSON serialized array of `Key` and `Value`.|
|Start Time<br/>`StartTime`<br/>`starttime`|DateTime|When the background operation started execution|
|End Time<br/>`EndTime`<br/>`endtime`|DateTime|When the background operation finished execution|
|Retry Count<br/>`RetryCount`<br/>`retrycount`|Integer|The number of times the background operation was retried|
|Error Code<br/>`ErrorCode`<br/>`errorcode`|Integer|The error code if the background operation fails<br/><br/>If the error comes from Dataverse, it has an integer value that corresponds to one of the codes listed in [Web service error codes](reference/web-service-error-codes.md). If the error didn't come from Dataverse, the value is set to zero.|
|Error Message<br/>`ErrorMessage`<br/>`errormessage`|Memo|The error message if the background operation fails|
|Run As<br/>`RunAs`<br/>`runas`|String|The `systemuserid` of the `systemuser` used to execute the background operation|
|Created On<br/>`CreatedOn`<br/>`createdon`|DateTime|When the record was created|
|Time to live<br/>`TTLInSeconds`<br/>`ttlinseconds`|Integer|Time to live in seconds, after which the record is automatically deleted; the default value is 90 days|

### Poll the background operations table

Make sure to include these columns in your query:

- `name`
- `backgroundoperationstatecode`
- `backgroundoperationstatuscode`
- `outputparameters`
- `errorcode`
- `errormessage`

How you poll the table depends on whether you're using the SDK or the Web API.

#### [SDK for .NET](#tab/sdk)

```csharp
static void PollBackgroundOperationRequest(IOrganizationService service, Guid backgroundOperationId)
{
    // List of columns that will help to get status, output and error details if any
    var columnSet = new ColumnSet(
        "name",
        "backgroundoperationstatecode",
        "backgroundoperationstatuscode",
        "outputparameters",
        "errorcode",
        "errormessage");

    try
    {
        // Get the entity with all the required columns
        var backgroundOperation = service.Retrieve("backgroundoperation", backgroundOperationId, columnSet);

        Console.WriteLine($"Name: {backgroundOperation["name"]}");
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
    // Catch Dataverse errors
    catch (FaultException<OrganizationServiceFault> ex)
    {
        Console.WriteLine($"ErrorCode:{ex.Detail.ErrorCode}");
        Console.WriteLine($"Message:{ex.Detail.Message}");
    }
    // Catch other errors
    catch (Exception error)
    {
        Console.WriteLine($"Some other error occurred: '{error.Message}'");
    }
}
```

**Waiting output:**

```console
Name: sample_ExportDataUsingFetchXmlToAnnotation
State Code: Locked
Status Code:  In Progress
Output Parameters:  
Error Code:  
Error Message:  
```

**Complete output:**

```console
Name: sample_ExportDataUsingFetchXmlToAnnotation
State Code: Completed
Status Code:  Succeeded
Output Parameters:
        AnnotationId: {value}
Error Code:  
Error Message:  
```

**Error output:**

```console
Name: sample_ExportDataUsingFetchXmlToAnnotation
State Code: Completed
Status Code:  Failed
Output Parameters: 
Error Code:  -2147187707
Error Message:  Access is denied.
```

If the platform produces the error, it has an integer value that corresponds to one of the codes listed in the [Web service error codes](reference/web-service-error-codes.md). If the platform doesn't produce the error, its value is set to zero.

**Id not found:**

```console
ErrorCode:-2147185406
Message:The HTTP status code of the response was not expected (404).

Status: 404
Response:
{"error":{"message":"Could not find item '110eaa68-db17-4115-ad74-d185823fc089'.","details":[{"message":"\r\nErrors : [\r\n  \"Resource Not Found. Learn more: https://aka.ms/cosmosdb-tsg-not-found\"\r\n]\r\n"}]}}
```

#### [Web API](#tab/webapi)

**Request:**

```http
GET [Organization URI]/api/data/v9.2/backgroundoperations(<backgroundoperationid value>)?$select=
name,
backgroundoperationstatecode,
backgroundoperationstatuscode,
outputparameters,
errorcode,
errormessage
Content-Type: application/json
Accept: application/json
OData-MaxVersion: 4.0
OData-Version: 4.0
Prefer: odata.include-annotations="OData.Community.Display.V1.FormattedValue"
```

**Response:**

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
    "name":"sample_ExportDataUsingFetchXmlToAnnotation"
    "outputparameters": "[{\"Key\":\"AnnotationId\",\"Value\":\"bb26025c-cbe6-ed11-a7c6-000d3a9933c9\"}]",
    "errorcode": null,
    "errormessage": null,
    "backgroundoperationid": "<backgroundoperationid value>",
    "versionnumber": 638183964640916096
}
```

---

### Poll the status monitor resource

You can poll the status monitor resource with a GET request, which returns the status of the background operation. If the operation is complete, it provides the output of the custom API. If there was an error during execution, you receive an error message and code.

Send a request to the status monitor resource URL that was returned with the `Location` response header of the original request.

**Request:**

```http
GET [Organization URI]/api/backgroundoperation/{backgroundoperationid}
Content-Type: application/json  
```

**Response:**

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

`backgroundOperationErrorCode` and `backgroundOperationErrorMessage` values are included only when an error occurs. Output parameters are included only when the operation completes successfully.

Labels aren't available with the status monitor resource.

## Receive notification of result

To get a notification when a background operation completes, you can either [include a callback URL with your request](#request-a-callback) or [subscribe to the `OnBackgroundOperationComplete` event](#subscribe-to-the-onbackgroundoperationcomplete-event).

### Request a callback

You can specify a URL in your request to receive a callback when the operation is completed. Dataverse uses this URL to send a POST request with the following payload:

```json
{
    "location": "< status monitor resource URL >",
    "backgroundOperationId": "{GUID}",
    "backgroundOperationStateCode": {INT},
    "backgroundOperationStatusCode": {INT},
    "backgroundOperationErrorCode": {INT},
    "backgroundOperationErrorMessage": {string},
}
```

`backgroundOperationErrorCode` and `backgroundOperationErrorMessage` are included only when an error occurs.

The callback payload doesn't include any output parameters. The site that receives the callback must send an authenticated GET request using the status monitor resource URL to get results.

If the URL requires authentication, it must be a self-sufficient [shared access signature (SAS)](/azure/storage/common/storage-sas-overview) URL. It isn't possible to include any more headers to include API keys or tokens for authentication.

You may want to use a site like [webhook.site](https://webhook.site/) to test the callback URL.

How you request a callback depends on whether you're using the SDK or the Web API. The following examples send a request using a webhook to [webhook.site](https://webhook.site/) for testing.

#### [SDK for .NET](#tab/sdk)

With the SDK, set the `ExecuteBackgroundOperation.CallbackUri` parameter to the URL to send the request.

```csharp
static void SendRequestAsynchronouslyWithCallback(IOrganizationService service)
{
    //Create a request for message defined as a custom API to run in the background
    var asyncRequest = new OrganizationRequest("sample_ExportDataUsingFetchXmlToAnnotation")
    {
        Parameters =
        {
            {"FetchXml",  @"<fetch version='1.0'  
                                    output-format='xml-platform' 
                                    mapping='logical'>
                                <entity name='account'>
                                    <attribute name='accountid'/>
                                    <attribute name='name'/>  
                                </entity>
                            </fetch>" }
        }
    };

    //Create a request to execute the message in the background
    var request = new OrganizationRequest("ExecuteBackgroundOperation")
    {
        Parameters =
        {
            {"Request", asyncRequest },
            // Request a callback
            {"CallbackUri", "https://webhook.site/<id>" }
        }
    };

    //Execute the background operation request
    var response = service.Execute(request);

    Console.WriteLine($"BackgroundOperationId: {response["BackgroundOperationId"]}");
    Console.WriteLine($"Location: {response["Location"]}");
}
```

#### [Web API](#tab/webapi)

With the Web API, set the `Prefer` request header with this value: `Prefer: respond-async, odata.callback; url="<url>"`

**Request:**

```http
POST [Organization URI]/api/data/v9.2/sample_ExportDataUsingFetchXmlToAnnotation 
Content-Type: application/json
Accept: application/json
Prefer: respond-async, odata.callback; url="https://webhook.site/<id>"

{
    "FetchXml": "<fetch version='1.0' output-format='xml-platform' mapping='logical'>
                    <entity name='account'>
                        <attribute name='accountid'/>
                        <attribute name='name'/>  
                    </entity>
                </fetch>"
}
```

**Response:**

```http
HTTP/1.1 202 Accepted
Preference-Applied: callback
x-ms-dyn-backgroundoperationid: <backgroundoperationid value>
location: [Organization URI]/api/backgroundoperation/<backgroundoperationid value>

{
   backgroundOperationId: <backgroundoperationid value>,
   location: [Organization URI]/api/backgroundoperation/<backgroundoperationid value>
}
```

---

### Subscribe to the OnBackgroundOperationComplete event

Another way to receive a notification when a background operation completes is to register a step on the `OnBackgroundOperationComplete` message. This message is a custom API that only allows asynchronous step registrations. It's an example of the type of messages created using a custom API to represent [business events](business-events.md).

As the name suggests, the OnBackgroundOperationComplete event occurs each time a background operation completes. When you register an asynchronous step on this event, you can perform any type of logic you want in a plug-in or forward the data to Azure services or a webhook. Learn more:

- [Register a plug-in](register-plug-in.md)
- [Azure integration](azure-integration.md)
- [Work with Microsoft Dataverse event data in your Azure Event Hubs solution](work-event-data-azure-event-hub-solution.md)
- [Use Webhooks to create external handlers for server events](use-webhooks.md)

The following tables describe the input and output parameters for the `OnBackgroundOperationComplete` message.

Input parameters:

|Name|Type|Description|
|---------|---------|---------|
|`PayloadType`|Integer|What type of response is sent to the callback URI when the background operation is complete; always zero for background operations<br/><br/>This field is internal and shouldn't be updated.|
|`LocationUrl`|String|Location URL|
|`BackgroundOperationId`|Guid|The ID of the background operation|

Output parameters:

|Name|Type|Description|
|---------|---------|---------|
|`OperationName`|String|Operation name|
|`BackgroundOperationStateCode`|Integer|Background operation state code|
|`BackgroundOperationStatusCode`|Integer|Background operation status code|

Configure the `OnBackgroundOperationComplete` message as shown in the instructions to [register a plug-in](register-plug-in.md). Make sure you set the message name as `OnBackgroundOperationComplete`. Set **Auto Delete** to `true` so that the [System Job (AsyncOperation)](reference/entities/asyncoperation.md) record is automatically removed.

## Cancel background operations

You can cancel a background operation that you initiated if it hasn't started.

- If the operation hasn't started, Dataverse doesn't execute it.
- If the operation has started, Dataverse doesn't stop it.
- If an error occurs during execution of a background operation you canceled, Dataverse doesn't retry it.
- If the operation has already completed, you get the following error: `Canceling background operation is not allowed after it is in terminal state.`

You can cancel a background operation in either of two ways:

- [Cancel a background operation by updating backgroundoperations](#cancel-a-background-operation-by-updating-backgroundoperations)
- [Send a DELETE request to the status monitor resource](#send-a-delete-request-to-the-status-monitor-resource)

### Cancel a background operation by updating backgroundoperations

Update the row in the `backgroundoperations` table to set the `backgroundoperationstatecode` to `2` (**Locked**) and `backgroundoperationstatuscode` to `22` (**Cancelling**).

How you update the `backgroundoperations` table depends on whether you're using the SDK or the Web API.

### [SDK for .NET](#tab/sdk)

```csharp
static void CancelBackgroundOperationRequest(
    IOrganizationService service, 
    Guid backgroundOperationId)
{
    var backgroundOperation = new Entity(
        entityName: "backgroundoperation", 
        id: backgroundOperationId)
    { 
        Attributes =
        {
            //Set state as Locked
            {"backgroundoperationstatecode", new OptionSetValue(2) },
            //Set status as Cancelling
            {"backgroundoperationstatuscode", new OptionSetValue(22) }
        }            
    }; 

    service.Update(backgroundOperation);
}
```

### [Web API](#tab/webapi)

**Request:**

```http
PATCH [Organization URI]/api/data/v9.2/backgroundoperations(<backgroundoperationid value>) HTTP/1.1
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

**Response:**

```http
HTTP/1.1 204 No Content
OData-Version: 4.0
```

---

### Send a DELETE request to the status monitor resource

You can also cancel a background operation by sending a DELETE request to the status monitor resource.

**Request:**

```http
DELETE [Organization URI]/api/backgroundoperation/{backgroundoperationid}
```

**Response:**

```http
HTTP/1.1 200 Ok

{
    backgroundOperationStateCode: 2,
    backgroundOperationStatusCode: 22
}
```

## Retries

If an error occurs during execution of the request, it's retried up to three times. These retries use an [exponential backoff strategy](https://wikipedia.org/wiki/Exponential_backoff).