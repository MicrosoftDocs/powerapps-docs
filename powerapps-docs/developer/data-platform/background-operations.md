---
title: "Background operations (Preview) (Microsoft Dataverse) | Microsoft Docs"
description: "Learn how to invoke custom apis asynchronously." 
ms.custom: intro-internal
ms.date: 03/22/2022
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

Use background operations to send requests that Dataverse will process asynchronously. Dataverse will immediately respond that the request was accepted and provide you with several ways to monitor whether the request ultimately succeeds and to retrieve the result, if any.

<!-- Need some information about whether these are actually limited to custom api and why that may be. Many of our system messages are now implemented as custom api. Usually, the caller doesn't need to know how they are defined. -->

Send a request this way when you don't want to maintain a connection awaiting a potentially long running operations.

> [!NOTE]
> This pattern doesn't allow for operations defined by custom apis to exceed the 2 minute time limit for plug-ins.

## Request asynchronous processing

You can request asynchronous processing of a request using both the SDK for .NET and Dataverse Web API.

### [SDK for .NET](#tab/sdk)

Use the `ExecuteBackgroundOperation` message.

> [!NOTE]
> The SDK does not currently have `ExecuteBackgroundOperation` request and response classes. Until these classes are added, you will will need to use the base [OrganizationRequest](xref:Microsoft.Xrm.Sdk.OrganizationRequest) and [OrganizationResponse](xref:Microsoft.Xrm.Sdk.OrganizationResponse) classes as described in [Use messages with the Organization service](org-service/use-messages.md)

The `ExecuteBackgroundOperation` message has the following request parameters:

|Name  |Type|Description  |
|---------|---------|---------|
|`Request`|[OrganizationRequest](xref:Microsoft.Xrm.Sdk.OrganizationRequest)|(Required) The request you want to have processed asynchronously.|
|`CallbackUri`|string| (Optional) Dataverse will send a POST HTTP request to this Url when the operation is completed. More information: [Request a callback](#request-a-callback)|

The `ExecuteBackgroundOperation` message has the following response properties:

|Name|Type|Description |
|---------|---------|---------|
|`BackgroundOperationId`|Guid| The id of the background operation table row you can use to monitor the processing of your request. |
|`Location`|string| The URL to use to retrieve the status of your request|

The following static method sends a <xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> using `ExecuteBackgroundOperation`.

<!-- I'm using a CreateRequest b/c it is simpler in explaining the use of this message w/o introducing some random Custom API. Most People know what a CreateRequest does. 

Does it have to be a Custom API?
-->

```csharp
static void SendRequestAsynchronously(IOrganizationService service)
{

    CreateRequest createRequest = new CreateRequest
    {
            Target = new Entity("account")
            {
                Attributes = {
                    {"name","Test Account" }
                }
            }
    };

    OrganizationRequest request = new OrganizationRequest("ExecuteBackgroundOperation")
    {
        Parameters = {
            {"Request", createRequest }
        }
    };

    var response = service.Execute(request);

    Console.WriteLine($"BackgroundOperationId: {response["BackgroundOperationId"]}");
    Console.WriteLine($"Location: {response["Location"]}");

}
```

**Output:**

```
BackgroundOperationId: f86f8700-6e21-4a39-aa6a-db3bb306b884
Location: [Organization URI]/api/data/v9.2/backgroundoperations(f86f8700-6e21-4a39-aa6a-db3bb306b884)
```


### [Web API](#tab/webapi)

Send your request with the `Prefer: respond-async` header. More information: [Prefer Headers](webapi/compose-http-requests-handle-errors.md#prefer-headers)

The following example uses the `sample_IsSystemAdmin` custom api described in [Sample: IsSystemAdmin Custom API](org-service/samples/issystemadmin-customapi-sample-plugin.md). This custom API is function bound to the [systemuser EntityType](xref:Microsoft.Dynamics.CRM.systemuser)

**Request**

```http
GET [Organization URI]/api/data/v9.2/systemusers(4026be43-6b69-e111-8f65-78e7d1620f5e)/Microsoft.Dynamics.CRM.sample_IsSystemAdmin
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
Prefer: respond-async
```

The response indicates that the request was accepted and has the state of **Ready** and status reason of **Waiting for Resources**.

**Response**

```http
HTTP/1.1 202 Accepted
Content-Type: application/json; odata.metadata=minimal
Preference-Applied: respond-async
OData-Version: 4.0

{
   backgroundOperationId: f86f8700-6e21-4a39-aa6a-db3bb306b884,
   backgroundOperationStateCode@OData.Community.Display.V1.FormattedValue": "Ready",
   backgroundOperationStateCode: 0,
   backgroundOperationStatusCode@OData.Community.Display.V1.FormattedValue": "Waiting For Resources",
   backgroundOperationStatusCode: 0,
   location: [Organization URI]/api/data/v9.2/backgroundoperations(f86f8700-6e21-4a39-aa6a-db3bb306b884)
}
```

---

## Monitor background operations

The Background Operation table contains information about requests that are sent to be processed asynchronously.

<!-- TODO: add link to Entity table reference when regenerated -->

Background operation has the following columns you can use to check the status of background operations.


|Display Name<br />`SchemaName`<br />`LogicalName`|Type |Description|
|---------|---------|---------|
|**Background Operation**<br />`BackgroundOperationId`<br />`backgroundoperationid`|Uniqueidentifier|The primary key.|
|**Status** <br />`StateCode`<br />`backgroundoperationstatecode`|Picklist|State of the background operation.<br />**Options:**<br />Value: `0`, Label: **Ready**<br />Value: `2`, Label: **Locked**<br />Value: `3`, Label: **Completed**|
|**Status Reason** <br />`StatusCode`<br />`backgroundoperationstatuscode`|Picklist|Status of the background operation.<br />**Options:**<br />Value: `0`, Label: **Waiting For Resources** (State:Ready)<br />Value: `20`, Label: **In Progress** (State:Locked)<br />Value: `22`, Label: **Canceling**  (State:Locked)<br />Value: `30`, Label: **Succeeded**  (State:Completed)<br />Value: `31`, Label: **Failed** (State:Completed)<br />Value: `32`, Label: **Canceled** (State:Completed)|
|**Name**<br />`Name`<br />`name`|String|The name of the background operation.|
|**DisplayName**<br />`DisplayName`<br />`displayname`|String|The display name of background operation.|
|**Input Parameters**<br />`InputParameters`<br />`inputparameters`|Memo|The input parameters that were supplied to start background operation.|
|**Output Parameters**<br />`OutputParameters`<br />`outputparameters`|Memo|The response of background operation.|
|**Start Time**<br />`StartTime`<br />`starttime`|DateTime|When the background operation started execution.|
|**End Time**<br />`EndTime`<br />`endtime`|DateTime|When the background operation finished execution.|
|**Retry Count**<br />`RetryCount`<br />`retrycount`|Integer|The number of times background operation was retried.
|**Error Code**<br />`ErrorCode`<br />`errorcode`|Integer|The error code of error for background operation in case of failure.|
|**Error Message**<br />`ErrorMessage`<br />`errormessage`|Memo|The error message of error for background operation in case of failure. |
|**Run As**<br />`RunAs`<br />`runas`|String|The system user identity of user (systemuser entity - systemuserid attribute) which was used to execute background operation.|
|**Created On**<br />`CreatedOn`<br />`createdon`|DateTime|When the record was created.|
|**Time to live**<br />`TTLInSeconds`<br />`ttlinseconds`|Integer|Time to live in seconds after which the record will be automatically deleted. Default value is 90 days.|


### Poll the background operation table

After initiating a background operation, you may want to check its status. To do this, you can use an Web API call with an HTTP GET verb on the location URL. This will give you the status of the background operation, and if the operation is complete, it will also provide the output of the Custom API. If there was an error during execution, you will receive an error message and code. This process is commonly known as status polling. We recommend that you avoid excessive polling, as it can have a negative impact on performance. If needed, we suggest polling at an interval of one minute or more.

#### [SDK for .NET](#tab/sdk)

```csharp
static Entity PollBackgroundOperationRequest(IOrganizationService service, Guid backgroundOperationId)
{
    // List of columns that will help to get status, output and error details if any
    var columnSet = new ColumnSet("backgroundoperationstatecode", "backgroundoperationstatuscode", "outputparameters", "errorcode", "errormessage");

    // Get the entity with all the required columns
    var backgroundOperation = serviceClient.Retrieve("backgroundoperation", backgroundOperationId, columnSet);

    return backgroundOperation;
}
```

#### [Web API](#tab/webapi)

**Request**

```http
GET [Organization URI]/api/backgroundOperation/{backgroundoperationid}
Content-Type: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0
```

**Response**

```http
HTTP/1.1 200 OK
Content-Type: application/json; odata.metadata=minimal
OData-Version: 4.0

{
  backgroundOperationErrorCode: {INT},
  backgroundOperationErrorMessage: {string},
  backgroundOperationStateCode: {INT},
  backgroundOperationSatusCode: {INT},
  outputParam1: {value},
  outputParam2: {value},
  outputParam3: {value},
}
```
`backgroundOperationErrorCode` and `backgroundOperationErrorMessage` will only be included when an error occurs. `outputParams` will be included when the operation is successfully complete.

---

### Request a callback

You can specify a URL in your request to recieve a callback when the operation is completed. Dataverse will use this URL to sent a POST request with the following payload:

```json
{
   backgroundOperationId: {GUID},
   backgroundOperationStateCode: {INT},
   backgroundOperationStatusCode: {INT},
   backgroundOperationErrorCode: {INT},
   backgroundOperationErrorMessage: {string},
   location:{locationURL}
}
```

`backgroundOperationErrorCode` and `backgroundOperationErrorMessage` will only be included when an error occurs.

> [!NOTE]
> - If the URL requires authentication, the URL must be a self-sufficient shared access signature (SAS)  URL. It isn't possible to include any additional headers to include API keys or tokens for authentication. More information: [Grant limited access to Azure Storage resources using shared access signatures (SAS)](/azure/storage/common/storage-sas-overview)
> - You may want to use a site like [webhook.site](https://webhook.site/) to test the callback URL.

The following examples show sending a request using a webhook to [webhook.site](https://webhook.site/) for testing:



#### [SDK for .NET](#tab/sdk)

Set the `ExecuteBackgroundOperation.CallbackUri` parameter to the URL to send the request.

```csharp
static void SendRequestAsynchronouslyWithCallback(IOrganizationService service)
{

    CreateRequest createRequest = new CreateRequest
    {
            Target = new Entity("account")
            {
                Attributes = {
                    {"name","Test Account" }
                }
            }
    };

    OrganizationRequest request = new OrganizationRequest("ExecuteBackgroundOperation")
    {
        Parameters = {
            {"Request", createRequest },
            {"CallbackUri", "https://webhook.site/<id>" }
        }
    };

    var response = service.Execute(request);

    Console.WriteLine($"BackgroundOperationId: {response["BackgroundOperationId"]}");
    Console.WriteLine($"Location: {response["Location"]}");

}
```

#### [Web API](#tab/webapi)

**Request**
```http
GET [Organization URI]/api/data/v9.2/systemusers(4026be43-6b69-e111-8f65-78e7d1620f5e)/Microsoft.Dynamics.CRM.sample_IsSystemAdmin
Content-Type: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
Prefer: respond-async, callback; url="https://webhook.site/<id>"
```
**Response**

```http
HTTP/1.1 202 Accepted
Content-Type: application/json; odata.metadata=minimal
Preference-Applied: callback
OData-Version: 4.0

{
   backgroundOperationId: f86f8700-6e21-4a39-aa6a-db3bb306b884,
   backgroundOperationStateCode@OData.Community.Display.V1.FormattedValue": "Ready",
   backgroundOperationStateCode: 0,
   backgroundOperationStatusCode@OData.Community.Display.V1.FormattedValue": "Waiting For Resources",
   backgroundOperationStatusCode: 0,
   location: [Organization URI]/api/data/v9.2/backgroundoperations(f86f8700-6e21-4a39-aa6a-db3bb306b884)
}
```
---

## Cancel background operations

If you initiate a background operation, you may sometimes need to cancel its execution. To do so, you can make use of an Web API call with an HTTP Delete verb on the location URL. If the operation hasn't begun execution yet, the platform won't execute it. However, if the execution has already started, the platform won't abort the operation. Additionally, if an error occurs during the execution, the platform won't retry it if a cancellation request was made.

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

```http
DELETE [Organization URI]/api/backgroundOperation/{backgroundoperationid}
Content-Type: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0
```

---

## Receive notification of result

Background operations can be executed with an optional callback URL to get notified for a specific execution. Alternatively, you can subscribe to the Business Event **OnBackgroundOperationComplete**, which is triggered whenever a background operation is complete.

Follow steps mentioned in [Register a webhook](https://learn.microsoft.com/en-us/dynamics365/customerengagement/on-premises/developer/use-webhooks?view=op-9-1#register-a-webhook) for message name OnBackgroundOperationComplete in asynchronous mode. 

---

## Retries

If an error occurs during execution of the request it will be retried up to three times. These retries will use a [exponential backoff strategy](https://wikipedia.org/wiki/Exponential_backoff).