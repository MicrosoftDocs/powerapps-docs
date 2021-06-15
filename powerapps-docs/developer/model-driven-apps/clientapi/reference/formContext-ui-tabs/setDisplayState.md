---
title: "setDisplayState (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the setDisplayState method.
ms.date: 04/21/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 13731ab8-e850-49d4-94c0-eae6135745c7
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

> [!IMPORTANT]
> The setDisplayState method will be deprecated with the 2021 release wave 1 (April 2021). Use the [setFocus](setfocus.md) method in Unified Interface to ensure the correct tab is opened on a form.

[!INCLUDE[./includes/setDisplayState-description.md](./includes/setDisplayState-description.md)]

## Syntax

`tabObj.setDisplayState(state);`

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|state|String|Yes|Specify "expanded" or "collapsed".|

### Related topics

[getDisplayState](getDisplayState.md)





[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]