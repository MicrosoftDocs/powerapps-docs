---
title: "removeOnProcessStatusChange (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the removeOnProcessStatusChange method.
ms.date: 04/19/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 5e41f59e-ddb3-4d47-b45b-454aa9e04439
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# removeOnProcessStatusChange (Client API reference)



[!INCLUDE[./includes/removeOnProcessStatusChange-description.md](./includes/removeOnProcessStatusChange-description.md)]

## Syntax

`formContext.data.process.removeOnProcessStatusChange(myFunction);`

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|myFunction|Function reference|Yes|The function to be removed from the [OnProcessStatusChange](../../events/onprocessstatuschange.md) event.|

### Related topics

[addOnProcessStatusChange](addOnProcessStatusChange.md)
 
[formContext.data.process](../../formContext-data-process.md)
 




[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]