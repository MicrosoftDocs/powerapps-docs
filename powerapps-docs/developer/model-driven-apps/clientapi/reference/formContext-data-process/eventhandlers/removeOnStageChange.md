---
title: "removeOnStageChange (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the removeOnStageChange method.
ms.date: 04/19/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 649fe7b0-016d-409f-ba3c-b14e0f1953e0
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# removeOnStageChange (Client API reference)

[!INCLUDE[./includes/removeOnStageChange-description.md](./includes/removeOnStageChange-description.md)]

## Syntax

`formContext.data.process.removeOnStageChange(myFunction);`

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|myFunction|Function reference|Yes|The function to be removed from the [OnStageChange](../../events/onstagechange.md) event.|

### Related topics

[addOnStageChange](addOnStageChange.md)
 
[formContext.data.process](../../formContext-data-process.md)
 




[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]