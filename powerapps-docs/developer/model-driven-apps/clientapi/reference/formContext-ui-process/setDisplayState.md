---
title: "setDisplayState (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the setDisplayState method.
ms.date: 04/19/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 21368fac-d4bc-4f75-8a9c-cce098fa0b45
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
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





[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]