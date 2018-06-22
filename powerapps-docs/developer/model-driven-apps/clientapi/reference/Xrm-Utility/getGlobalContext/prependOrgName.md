---
title: "prependOrgName (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 10/31/2017
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 89123cde-7c66-4c7d-94e4-e287285019f8
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# prependOrgName (Client API reference)



Prefixes the current organization's unique name to a string, typically a URL path.

## Syntax

 ```JavaScript
var globalContext = Xrm.Utility.getGlobalContext();
globalContext.prependOrgName(sPath);
```

## Parameters

|Name |Type |Required |Description |
|---|---|---|---|
|sPath |String |Yes |A local path to a resource. |

## Return Value

**Type**: String

**Description**: A path string with the organization name prefixed in the following format:

`"/"+ orgName + sPath`

### Related topics

[Xrm.Utility.getGlobalContext](../getGlobalContext.md)


