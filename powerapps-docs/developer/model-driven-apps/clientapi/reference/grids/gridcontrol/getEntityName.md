---
title: "getEntityName (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the getEntityName method.
ms.date: 04/21/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 1ead9dc0-7511-4b41-bd7d-23b8bb3b4e43
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# getEntityName (Client API reference)



[!INCLUDE[./includes/getEntityName-description.md](./includes/getEntityName-description.md)]

## Grid types supported

Read-only and editable grids

## Syntax

`gridContext.getEntityName();`

## Return Value

**Type**: String

**Description**: The logical name of the table data displayed in the grid.

## Remarks

To get the `gridContext`, see [Getting the grid context](../../grids.md#bkmk_gridcontext). 




[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]