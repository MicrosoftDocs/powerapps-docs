---
title: "setDisplayState (Client API reference) in Dynamics 365 Customer Engagement| MicrosoftDocs"
ms.date: 10/31/2017
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 21368fac-d4bc-4f75-8a9c-cce098fa0b45
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# setDisplayState (Client API reference)

[!INCLUDE[](../../../../includes/cc_applies_to_update_9_0_0.md)]

[!INCLUDE[./includes/setDisplayState-description.md](./includes/setDisplayState-description.md)]

## Syntax

`formContext.ui.process.setDisplayState(state);`

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|state|String|Yes|Specify "expanded", "collapsed", or "floating". The value "floating" is not supported on the web client.|

### Related topics

[getDisplayState](getDisplayState.md)

[formContext.ui.process](../formContext-ui-process.md)



