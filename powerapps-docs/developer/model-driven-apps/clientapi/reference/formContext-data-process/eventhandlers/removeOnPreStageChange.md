---
title: "removeOnPreStageChange (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 08/05/2019
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
author: "MsftMan"
ms.author: "DeonHe"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
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