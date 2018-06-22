---
title: "isOnPremise (Client API reference) in Dynamics 365 Customer Engagement| MicrosoftDocs"
ms.date: 10/31/2017
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 855767c5-c48f-47a2-8f99-52423221d974
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# isOnPremise (Client API reference)

[!INCLUDE[](../../../../../includes/cc_applies_to_update_9_0_0.md)]

Returns a boolean value indicating if the Customer Engagement instance is hosted on-premises or online. 

## Syntax

```JavaScript
var globalContext = Xrm.Utility.getGlobalContext();
globalContext.isOnPremises();
```

## Return Value

**Type**: Boolean

**Description**: **true** if the Customer Engagement instance is on-premises; **false** otherwise.

### Related topics

[Xrm.Utility.getGlobalContext](../getGlobalContext.md)



