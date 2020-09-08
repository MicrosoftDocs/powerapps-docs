---
title: "setDisplayState (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 08/27/2020
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
> The setDisplayState method will be deprecated with the Release Wave One 2021 (April 2021). Use [setFocus](setfocus.md) method in the Unified Interface to ensure the correct tab is opened on a form.

[!INCLUDE[./includes/setDisplayState-description.md](./includes/setDisplayState-description.md)]

## Syntax

`tabObj.setDisplayState(state);`

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|state|String|Yes|Specify "expanded" or "collapsed".|

### Related topics

[getDisplayState](getDisplayState.md)



