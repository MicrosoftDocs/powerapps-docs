---
title: "removeOnPreProcessStatusChange (Client API reference) in Dynamics 365 for Customer Engagement| MicrosoftDocs"
ms.date: 06/20/2019
ms.service: crm-online
ms.topic: reference
applies_to: Dynamics 365 for Customer Engagement (online)
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

[!INCLUDE[](../../../../../includes/cc_applies_to_update_9_0_0.md)]

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