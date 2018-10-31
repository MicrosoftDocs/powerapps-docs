---
title: "isOnPremise (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 10/31/2018
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 855767c5-c48f-47a2-8f99-52423221d974
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# isOnPremise (Client API reference)



Returns a boolean value indicating if the model-driven apps instance is hosted on-premises or online. 

## Syntax

```JavaScript
var globalContext = Xrm.Utility.getGlobalContext();
globalContext.isOnPremises();
```

## Return Value

**Type**: Boolean

**Description**: **true** if the model-driven apps instance is on-premises; **false** otherwise.

### Related topics

[Xrm.Utility.getGlobalContext](../getGlobalContext.md)



