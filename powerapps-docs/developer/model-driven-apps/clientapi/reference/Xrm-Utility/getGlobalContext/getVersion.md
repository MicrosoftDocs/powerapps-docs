---
title: "getVersion (Client API reference) in Dynamics 365 Customer Engagement| MicrosoftDocs"
ms.date: 10/31/2017
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 2fd5c43e-5a01-431d-ac2c-abefdb8d06ac
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# getVersion (Client API reference)



Returns the version number of the Dynamics 365 Customer Engagement instance.

## Syntax

```JavaScript
var globalContext = Xrm.Utility.getGlobalContext();
globalContext.getVersion();
``` 
## Return Value

**Type**: String

**Description**: Version of the Customer Engagement instance. For example:

`"9.0.0.1103"`

### Related topics

[Xrm.Utility.getGlobalContext](../getGlobalContext.md)
