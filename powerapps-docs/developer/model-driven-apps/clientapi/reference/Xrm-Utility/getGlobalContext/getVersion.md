---
title: "getVersion (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the getVersion method.
ms.date: 04/21/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 2fd5c43e-5a01-431d-ac2c-abefdb8d06ac
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# getVersion (Client API reference)



Returns the version number of the model-driven apps instance.

## Syntax

```JavaScript
var globalContext = Xrm.Utility.getGlobalContext();
globalContext.getVersion();
``` 
## Return Value

**Type**: String

**Description**: Version of the model-driven apps instance. For example:

`"9.0.0.1103"`

### Related topics

[Xrm.Utility.getGlobalContext](../getGlobalContext.md)


[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]