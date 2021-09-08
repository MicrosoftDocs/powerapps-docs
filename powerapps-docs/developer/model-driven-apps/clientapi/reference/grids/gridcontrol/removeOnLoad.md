---
title: "removeOnLoad (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the removeOnLoad method.
ms.date: 04/21/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 4d025f92-db16-440c-9f82-e40d71e09862
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# removeOnLoad (Client API reference)



[!INCLUDE[./includes/removeOnLoad-description.md](./includes/removeOnLoad-description.md)]

## Grid types supported

Read-only grids

## Syntax

`gridContext.removeOnLoad(myFunction);`

## Parameter

|Name|Type|Required|Description|
|--|--|--|--|
|myFunction|function reference|Yes|The function to be removed from the **OnLoad** event.

## Remarks

To get the `gridContext`, see [Getting the grid context](../../grids.md#bkmk_gridcontext).

### Related topics

[addOnLoad](addOnLoad.md) 




[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]