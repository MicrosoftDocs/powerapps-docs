---
title: "removeOnPreStageChange (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the removeOnPreStageChange method.
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
# removeOnPreStageChange (Client API reference)

[!INCLUDE[./includes/removeOnPreStageChange-description.md](./includes/removeOnPreStageChange-description.md)]

## Syntax

`formContext.data.process.removeOnPreStageChange(myFunction);`

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|myFunction|Function reference|Yes|The function to be removed from the [OnPreStageChange](../../events/onprestagechange.md) event.|

### Related topics

[addOnPreStageChange](addOnPreStageChange.md)
 
[formContext.data.process](../../formContext-data-process.md)
 




[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]