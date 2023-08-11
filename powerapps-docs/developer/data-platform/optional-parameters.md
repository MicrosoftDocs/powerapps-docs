---
title: "Use optional parameters (Microsoft Dataverse) | Microsoft Docs" 
description: "Use optional parameters to control operation behaviors" 
ms.date: 06/28/2023
ms.reviewer: jdaly
ms.topic: article
author: divkamath
ms.subservice: dataverse-developer
ms.author: dikamath
search.audienceType: 
  - developer
contributors:
  - PHecke
  - JimDaly
  - LearningEveryday1
  - NHelgren
---
# Use optional parameters

Dataverse provides a set of optional parameters or request header values a developer of a client application can use to modify the behavior of individual requests. This article describes the parameter values and request headers that you can use to get the behaviors you need.

> [!NOTE]
> This article introduces these parameters but does not explain them in depth. Please follow the links for more information to fully understand the scenarios for using these parameters.

## How to use

How you use these optional parameters depends on whether you're using the Dataverse SDK for .NET or Web API.

### [SDK for .NET](#tab/sdk)

Usually, you will add the parameter to the [OrganizationRequest.Parameters Collection](xref:Microsoft.Xrm.Sdk.OrganizationRequest.Parameters) of the named request class.

> [!NOTE]
> You cannot specify these parameters using the 7 shortcut methods exposed with the <xref:Microsoft.Xrm.Sdk.IOrganizationService>. You must use the named request class with the [IOrganizationService.Execute method](xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute%2A).

One exception is when setting the `partitionid`, this is set as an attribute of the entity instance. More information: [Perform a data operation with specified partition](#perform-a-data-operation-with-specified-partition)

More information:

- [Use messages with the Organization service](org-service/use-messages.md)
- See the examples below

### [Web API](#tab/webapi)

Usually, you'll add the parameter as a request header with the `MSCRM.` namespace.

Two exceptions are the following that are appended to the URL.

- The `tag` parameter. See [Add a shared variable to the plugin execution context](#add-a-shared-variable-to-the-plugin-execution-context)
- The `partitionid` parameter. See [Perform a data operation with specified partition](#perform-a-data-operation-with-specified-partition)

More information:

- [Compose HTTP requests and handle errors : Other headers](webapi/compose-http-requests-handle-errors.md#other-headers)
- See the examples below.

---

## Associate a solution component with a solution

When you perform data operations on a solution component, you can associate it with a solution by specifying the solution unique name with the `SolutionUniqueName` parameter.

You can use this parameter with these messages:

- `AddPrivilegesRole`
- `Create` (POST)
- `Delete` (DELETE)
- `MakeAvailableToOrganizationTemplate`
- `Update` (PATCH)

The following examples create a web resource solution component and add it to the solution with the unique name of `ExampleSolution`.
### [SDK for .NET](#tab/sdk)

```csharp
static void CreateWebResourceInSolution(IOrganizationService service)
{
    Entity webResource = new("webresource");

    webResource["displayname"] = "Simple HTML web resource";
    webResource["content"] = "PCFET0NUWVBFIGh0bWw+CjxodG1sPgogIDxib2R5PgogICAgPGgxPkhlbGxvIFdvcmxkPC9oMT4KICA8L2JvZHk+CjwvaHRtbD4=";
    webResource["webresourcetype"] = new OptionSetValue(1);
    webResource["name"] = "sample_SimpleHTMLWebResource.htm";
    webResource["description"] = "An example HTML web resource";

    CreateRequest request = new();
    request.Target = webResource;
    request["SolutionUniqueName"] = "ExampleSolution";

    service.Execute(request);
}

```

More information:

- [Use messages with the Organization service](org-service/use-messages.md)
- [Create table rows using the Organization Service](org-service/entity-operations-create.md)
- [Import files as web resources](org-service/samples/import-files-as-web-resources.md)

### [Web API](#tab/webapi)

**Request:**

```http
POST [Organization URI]/api/data/v9.2/webresourceset HTTP/1.1
If-None-Match: null
OData-Version: 4.0
OData-MaxVersion: 4.0
Content-Type: application/json
Accept: application/json
MSCRM.SolutionUniqueName: ExampleSolution

{
  "displayname": "Simple HTML web resource",
  "content": "PCFET0NUWVBFIGh0bWw+CjxodG1sPgogIDxib2R5PgogICAgPGgxPkhlbGxvIFdvcmxkPC9oMT4KICA8L2JvZHk+CjwvaHRtbD4=",
  "webresourcetype": 1,
  "name": "sample_SimpleHTMLWebResource.htm",
  "description": "An example HTML web resource"
}
```

**Response:**

```http
HTTP/1.1 204 No Content
OData-Version: 4.0
OData-EntityId: [Organization URI]/api/data/v9.2/webresourceset(833aa051-05be-ed11-83ff-000d3a993550)

```

More information: [Create a table row using the Web API](webapi/create-entity-web-api.md)

---

More information:

- [Create a custom table using code](org-service/create-custom-entity.md)
- [Create and update table definitions using the Web API](webapi/create-update-entity-definitions-using-web-api.md)


## Suppress duplicate detection

If you want to have Dataverse throw an error when a new record you create or a record you update matches the duplicate detection rules for another record, you must create or update the row using the `SuppressDuplicateDetection` parameter with a value of false.

The following examples return an error when the following are true:

- Duplicate Detection is enabled for the environment when a row is created or updated.
- The `account` table has duplicate detection enabled
- A Duplicate Detection Rule is published that checks whether the account `name` value is an exact match for an existing row
- There's an existing account with the name` Sample Account`.

### [SDK for .NET](#tab/sdk)

```csharp
static void DemonstrateSuppressDuplicateDetection(IOrganizationService service)
{
    Entity account = new("account");
    account["name"] = "Sample Account";

    CreateRequest request = new()
    {
        Target = account
    };
    request.Parameters.Add("SuppressDuplicateDetection", false);

    try
    {
        service.Execute(request);
    }
    catch (FaultException<OrganizationServiceFault> ex)
    {
        throw ex.Detail.ErrorCode switch
        {
            -2147220685 => new InvalidOperationException(ex.Detail.Message),
            _ => ex,
        };
    }
}
```

### [Web API](#tab/webapi)

**Request:**

```http
POST [Organization URI]/api/data/v9.2/accounts HTTP/1.1
If-None-Match: null
OData-Version: 4.0
OData-MaxVersion: 4.0
Content-Type: application/json
Accept: application/json
MSCRM.SuppressDuplicateDetection: false

{
    "name":"Sample Account"
}
```

**Response:**

```http
HTTP/1.1 412 Precondition Failed
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0

{
    "error": {
        "code": "0x80040333",
        "message": "A record was not created or updated because a duplicate of the current record already exists."
    }
}
```

---

More information:

- [Detect duplicate data using the Organization service](org-service/detect-duplicate-data.md)
- [Detect duplicate data using the Web API](webapi/manage-duplicate-detection-create-update.md)

## Add a shared variable to the plugin execution context

Use the `tag` parameter to include a shared variable value that is accessible within a plug-in. This extra information allows a plug-in to apply logic that depends on the client application.

> [!NOTE]
> This parameter is intended for client applications to be able to set any value they wish. No Microsoft feature should require that you set a specific value in your client application code to enable different behaviors.

To access the value in a plug-in, use the [IExecutionContext.SharedVariables collection](xref:Microsoft.Xrm.Sdk.IExecutionContext.SharedVariables)

```csharp
if (context.SharedVariables.ContainsKey("tag")){
    string tagValue = context.SharedVariables["tag"];
}
```

The following examples pass this value: `A string value` while creating an account record.

### [SDK for .NET](#tab/sdk)

```csharp
static void DemonstrateTag(IOrganizationService service)
{
    Entity account = new("account");
    account["name"] = "Sample Account";

    CreateRequest request = new()
    {
        Target = account
    };
    request.Parameters.Add("tag", "A string value");
    service.Execute(request);
}
```

### [Web API](#tab/webapi)

**Request:**

```http
POST [Organization URI]/api/data/v9.2/accounts?tag=A%20string%20value HTTP/1.1
If-None-Match: null
OData-Version: 4.0
OData-MaxVersion: 4.0
Content-Type: application/json
Accept: application/json

{
    "name":"Sample Account"
}
```

The response shouldn't be affected by sending the tag unless the plug-in contains logic to change it.

---

More information: [Shared variables](understand-the-data-context.md#shared-variables)

## Perform a data operation with specified partition

When using elastic tables with a partitioning strategy, you can pass a unique string value with the `partitionid` parameter to access non-relational table data within a storage partition.

The following examples use the `partitionid` value of `deviceId` when retrieving a `contoso_sensordata` record.

### [SDK for .NET](#tab/sdk)

```csharp
private static Entity RetrieveRecord(
    IOrganizationService service,
    Guid contosoSensorDataId,
    string deviceId,
    string sessionToken)
{
    EntityReference entityReference = new("contoso_sensordata", contosoSensorDataId);

    RetrieveRequest request = new()
    {
        ColumnSet = new ColumnSet("contoso_value"),
        Target = entityReference,
        ["partitionId"] = deviceId, //To identify the record
        ["SessionToken"] = sessionToken //Pass the session token for strong consistency
    };
    var response = (RetrieveResponse)service.Execute(request);
    return response.Entity;

}
```

### [Web API](#tab/webapi)

**Request:**

```http
GET [Organization Uri]/api/data/v9.2/contoso_sensordatas(da9c32cc-2df8-ed11-8849-000d3a993550)?partitionId=Device-ABC-1234&$select=contoso_value
MSCRM.SessionToken: 207:8#142792105#7=-1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

---

Alternatively, you can use the `partitionid` value using alternate key style.

- [Learn about using the alternate keys with elastic tables](use-elastic-tables.md#using-the-alternate-key)
- [Learn about specify a partitionid](use-elastic-tables.md#specify-partitionid)

## Bypass custom synchronous logic

Synchronous logic must be applied during the transaction and can significantly impact performance of individual operations. When performing bulk operations, the additional time for these individual operations can increase the time required. Use the `BypassCustomPluginExecution` parameter when you want to improve performance while performing bulk data operations.

> [!IMPORTANT]
> The calling user must have the `prvBypassCustomPlugins` privilege.

### [SDK for .NET](#tab/sdk)

There are two ways to use this parameter with the SDK for .NET.
#### Set the value as an optional parameter

The following example sets the optional `BypassCustomPluginExecution` parameter when creating a new account record using the [CreateRequest class](xref:Microsoft.Xrm.Sdk.Messages.CreateRequest).

```csharp
static void DemonstrateBypassCustomPluginExecution(IOrganizationService service)
{
    Entity account = new("account");
    account["name"] = "Sample Account";

    CreateRequest request = new()
    {
        Target = account
    };
    request.Parameters.Add("BypassCustomPluginExecution", true);
    service.Execute(request);
}
```


#### Set the CrmServiceClient.BypassPluginExecution property

The following example sets the [CrmServiceClient.BypassPluginExecution Property](xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient.BypassPluginExecution) when creating a new account record:

```csharp
var service = new CrmServiceClient(connectionString);  

service.BypassPluginExecution = true;

var account = new Entity("account");
account["name"] = "Sample Account";

service.Create(account);
```

Because this setting is applied to the service, it remains set for all requests sent using the service until it's set to `false`.

> [!NOTE]
> This property is not available in the [Dataverse.Client.ServiceClient](xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient), but it is available on the [Dataverse.Client.Extensions.CRUDExtentions methods](xref:Microsoft.PowerPlatform.Dataverse.Client.Extensions.CRUDExtentions).

### [Web API](#tab/webapi)

**Request:**

```http
POST [Organization URI]/api/data/v9.2/accounts HTTP/1.1
If-None-Match: null
OData-Version: 4.0
OData-MaxVersion: 4.0
Content-Type: application/json
Accept: application/json
MSCRM.BypassCustomPluginExecution: true

{
    "name":"Sample Account"
}
```

The response shouldn't be affected by sending the `MSCRM.BypassCustomPluginExecution` request header.

---

More information: [Bypass Synchronous Logic](bypass-custom-business-logic.md#bypass-synchronous-logic)

## Bypass Power Automate Flows

When bulk data operations occur that trigger flows, Dataverse creates system jobs to execute the flows. When the number of system jobs is very large, it may cause performance issues for the system. If this occurs, you can choose to bypass triggering the flows by using the `SuppressCallbackRegistrationExpanderJob` optional parameter.

The [CallbackRegistration table](reference/entities/callbackregistration.md) manages flow triggers, and there's an internal operation called *expander* that calls the registered flow triggers.

> [!NOTE]
> When this option is used, the flow owners will not receive a notification that their flow logic was bypassed.

### [SDK for .NET](#tab/sdk)

```csharp
static void DemonstrateSuppressCallbackRegistrationExpanderJob(IOrganizationService service)
{
    Entity account = new("account");
    account["name"] = "Sample Account";

    CreateRequest request = new()
    {
        Target = account
    };
    request.Parameters.Add("SuppressCallbackRegistrationExpanderJob", true);
    service.Execute(request);
}
```

### [Web API](#tab/webapi)

**Request:**

```http
POST [Organization URI]/api/data/v9.2/accounts HTTP/1.1
If-None-Match: null
OData-Version: 4.0
OData-MaxVersion: 4.0
Content-Type: application/json
Accept: application/json
MSCRM.SuppressCallbackRegistrationExpanderJob: true

{
    "name":"Sample Account"
}
```

---

More information: [Bypass Power Automate Flows](bypass-custom-business-logic.md#bypass-power-automate-flows)

### See also

[Use messages with the Organization service](org-service/use-messages.md)<br />
[Web API: Compose HTTP requests and handle errors : Other headers](webapi/compose-http-requests-handle-errors.md#other-headers)<br />
[Bypass Custom Business Logic](bypass-custom-business-logic.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]

