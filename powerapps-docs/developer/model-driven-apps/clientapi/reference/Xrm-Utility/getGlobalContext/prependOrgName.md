---
title: "prependOrgName (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the prependOrgName method.
ms.author: jdaly
author: adrianorth
manager: kvivek
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
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