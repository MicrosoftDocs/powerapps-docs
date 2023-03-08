---
title: "Use Optional parameters (Microsoft Dataverse) | Microsoft Docs" 
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
# Use Optional parameters

Dataverse provides a set of optional parameters or request header values a developer of a client application can use to modify the behavior of individual requests. This article describes the parameter values and request headers that you can use to get the behaviors you need.

## How to use

The way you use these optional parameters depends on whether you are using the Dataverse SDK for .NET or Web API.

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

When you create or update a solution component, you can associate it with a solution by specifying the solution unique name.

You can use this parameter with these messages:

- `AddPrivilegesRole`
- `Create` (`POST`)
- `Delete` (`DELETE`)
- `MakeAvailableToOrganizationTemplate`
- `Update` (`PATCH`)

### [SDK for .NET](#tab/sdk)

Content for SDK...

### [Web API](#tab/webapi)

Content for Web API...

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

