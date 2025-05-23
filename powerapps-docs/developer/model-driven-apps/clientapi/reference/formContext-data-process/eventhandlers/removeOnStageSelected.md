---
title: "removeOnStageSelected (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the removeOnStageSelected method.
author: matthidinger
ms.author: mahiding
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# removeOnStageSelected (Client API reference)

[!INCLUDE[./includes/removeOnStageSelected-description.md](./includes/removeOnStageSelected-description.md)]

## Syntax

`formContext.data.process.removeOnStageSelected(myFunction);`

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|`myFunction`|Function reference|Yes|The function to be removed from the [OnStageSelected](../../events/onstageselected.md) event.|

### Related articles

[addOnStageSelected](addOnStageSelected.md)   
[formContext.data.process](../../formContext-data-process.md)
 
[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]
