---
title: "prependOrgName (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the prependOrgName method.
ms.date: 04/21/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 89123cde-7c66-4c7d-94e4-e287285019f8
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
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




[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]