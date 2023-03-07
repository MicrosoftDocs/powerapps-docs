---
title: "process.setDisplayState (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the process.setDisplayState method.
author: HemantGaur
ms.author: hemantg
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
  - JimDaly
---
# process.setDisplayState (Client API reference)



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