---
title: "getGridType (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the getGridType method.
ms.date: 04/21/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: a441c08c-df32-433e-b666-4253f2cf878c
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# getGridType (Client API reference)



[!INCLUDE[./includes/getGridType-description.md](./includes/getGridType-description.md)]

## Grid types supported

Read-only and editable grids

## Syntax

`var gridType = gridContext.getGridType();`

## Return Value

**Type**: Number

**Description**: Returns one of the following values:

|Value |Description |
|--|--|
|1|HomePageGrid|
|2|Subgrid|

## Remarks

To get the `gridContext`, see [Getting the grid context](../../grids.md#bkmk_gridcontext). 




[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]