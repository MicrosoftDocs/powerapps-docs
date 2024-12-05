---
title: "removeOnStageChange (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the removeOnStageChange method.
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
# removeOnStageChange (Client API reference)

[!INCLUDE[./includes/removeOnStageChange-description.md](./includes/removeOnStageChange-description.md)]

## Syntax

`formContext.data.process.removeOnStageChange(myFunction);`

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|`myFunction`|Function reference|Yes|The function to be removed from the [OnStageChange](../../events/onstagechange.md) event.|

### Related articles

[addOnStageChange](addOnStageChange.md)   
[formContext.data.process](../../formContext-data-process.md)
 
[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]
