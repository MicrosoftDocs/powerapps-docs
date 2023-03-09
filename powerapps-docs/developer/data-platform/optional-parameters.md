---
title: "Use optional parameters (Microsoft Dataverse) | Microsoft Docs" 
description: "Use optional parameters to control operation behaviors" 
ms.date: 03/08/2023
ms.reviewer: jdaly
ms.topic: article
author: divkamath
ms.subservice: dataverse-developer
ms.author: dikamath
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
  - PHecke
  - JimDaly
  - LearningEveryday1
  - NHelgren
---
# Use optional parameters

Dataverse provides a set of optional parameters or request header values a developer of a client application can use to modify the behavior of individual requests. This article describes the parameter values and request headers that you can use to get the behaviors you need.

## How to use

How you use these optional parameters depends on whether you are using the Dataverse SDK for .NET or Web API.

### [SDK for .NET](#tab/sdk)

Add the parameter to the [OrganizationRequest.Parameters Collection](xref:Microsoft.Xrm.Sdk.OrganizationRequest.Parameters) of the named request class.

> [!NOTE]
> You cannot specify these parameters using the 7 shortcut methods exposed with the <xref:Microsoft.Xrm.Sdk.IOrganizationService>. You must use the named request class with the [IOrganizationService.Execute method](xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute%2A). 

More information:

- [Use messages with the Organization service](org-service/use-messages.md)
- See the examples below

### [Web API](#tab/webapi)

Add the parameter as a request header with the `MSCRM.` namespace.

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

The following examples will create a web resource solution component and add it to the solution with the unique name of `ExampleSolution`.
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

**Request**

```http
POST [Organization URI]/api/data/v9.2/webresourceset HTTP/1.1
MSCRM.SolutionUniqueName: ExampleSolution
Content-Type: application/json

{
  "displayname": "Simple HTML web resource",
  "content": "PCFET0NUWVBFIGh0bWw+CjxodG1sPgogIDxib2R5PgogICAgPGgxPkhlbGxvIFdvcmxkPC9oMT4KICA8L2JvZHk+CjwvaHRtbD4=",
  "webresourcetype": 1,
  "name": "sample_SimpleHTMLWebResource.htm",
  "description": "An example HTML web resource"
}
```

**Response**

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

If you want to have the platform throw an error when a new row you create is determined to be a duplicate row, or you update an existing row so that duplicate detection rules will be evaluated, you must use the create or update the row using the `SuppressDuplicateDetection` parameter with a value of false.

The following examples will return an error when the following are true:

- Duplicate Detection is enabled for the environment when a row is created or updated.
- The `account` table has duplicate detection enabled
- A Duplicate Detection Rule is published that checks whether the account `name` value is an exact match for an existing row
- There is an existing account with the name` Sample Account`.

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

**Request**

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

**Response**

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

### [SDK for .NET](#tab/sdk)

Content for SDK...

### [Web API](#tab/webapi)

Content for Web API...

---

## Perform a data operation with specified partition

### [SDK for .NET](#tab/sdk)

Content for SDK...

### [Web API](#tab/webapi)

Content for Web API...

---

## Bypass custom synchronous logic

### [SDK for .NET](#tab/sdk)

Content for SDK...

### [Web API](#tab/webapi)

Content for Web API...

---

## Bypass flow triggers

### [SDK for .NET](#tab/sdk)

Content for SDK...

### [Web API](#tab/webapi)

Content for Web API...

---

### See also


[!INCLUDE[footer-include](../../includes/footer-banner.md)]

