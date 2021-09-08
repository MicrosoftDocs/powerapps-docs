---
title: "removeOnPreProcessStatusChange (Client API reference) in model-driven apps in Power Apps| MicrosoftDocs"
description: Includes description and supported parameters for the removeOnProcessStatusChange method.
ms.date: 04/19/2021
ms.service: powerapps
ms.topic: reference
ms.assetid: 
author: MSFTMan
ms.author: Deonhe
manager: KVivek
search.audienceType: 
  - developer
search.app: 
  - D365CE
---
# removeOnPreProcessStatusChange (Client API reference)

[!INCLUDE[](../../../../../../includes/cc_applies_to_update_9_0_0.md)]

[!INCLUDE[./includes/removeOnPreProcessStatusChange-description.md](./includes/removeOnPreProcessStatusChange-description.md)]

## Syntax

`formContext.data.process.removeOnPreProcessStatusChange(myFunction);`

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|myFunction|Function reference|Yes|The function to be removed from the [OnPreProcessStatusChange](../../events/onpreprocessstatuschange.md) event.|

### Related topics

[addOnProcessStatusChange](addOnProcessStatusChange.md)
 
[formContext.data.process](../../formContext-data-process.md)
 




[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]