---
title: "removeOnProcessStatusChange (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the removeOnProcessStatusChange method.
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
# removeOnProcessStatusChange (Client API reference)

[!INCLUDE[./includes/removeOnProcessStatusChange-description.md](./includes/removeOnProcessStatusChange-description.md)]

## Syntax

`formContext.data.process.removeOnProcessStatusChange(myFunction);`

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|`myFunction`|Function reference|Yes|The function to be removed from the [OnProcessStatusChange](../../events/onprocessstatuschange.md) event.|

### Related articles

[addOnProcessStatusChange](addOnProcessStatusChange.md)   
[formContext.data.process](../../formContext-data-process.md)
 
[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]
