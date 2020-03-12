---
title: "setDisplayState (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 10/31/2018
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 21368fac-d4bc-4f75-8a9c-cce098fa0b45
author: "KumarVivek"
ms.author: "kvivek"
manager: "annbe"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# setDisplayState (Client API reference)



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



