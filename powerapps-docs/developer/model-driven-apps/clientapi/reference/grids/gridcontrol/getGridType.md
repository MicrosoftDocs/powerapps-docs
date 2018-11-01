---
title: "getGridType (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 10/31/2018
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: a441c08c-df32-433e-b666-4253f2cf878c
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
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


