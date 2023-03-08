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

---

More information: [Dependency tracking for solution components](/power-platform/alm/dependency-tracking-solution-components)

## Suppress duplicate detection

### [SDK for .NET](#tab/sdk)

Content for SDK...

### [Web API](#tab/webapi)

Content for Web API...

---

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

