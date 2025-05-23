---
title: "removeOnPreProcessStatusChange (Client API reference) in model-driven apps in Power Apps"
description: Includes description and supported parameters for the removeOnPreProcessStatusChange method.
author: matthidinger
ms.author: mahiding
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# removeOnPreProcessStatusChange (Client API reference)

[!INCLUDE[](../../../../../../includes/cc_applies_to_update_9_0_0.md)]

[!INCLUDE[./includes/removeOnPreProcessStatusChange-description.md](./includes/removeOnPreProcessStatusChange-description.md)]

## Syntax

`formContext.data.process.removeOnPreProcessStatusChange(myFunction);`

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|`myFunction`|Function reference|Yes|The function to be removed from the [OnPreProcessStatusChange](../../events/onpreprocessstatuschange.md) event.|

### Related articles

[addOnProcessStatusChange](addOnProcessStatusChange.md)   
[formContext.data.process](../../formContext-data-process.md)
 
[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]
