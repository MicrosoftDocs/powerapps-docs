---
title: "getEntityName (Client API reference) in Dynamics 365 Customer Engagement| MicrosoftDocs"
ms.date: 11/10/2017
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 1ead9dc0-7511-4b41-bd7d-23b8bb3b4e43
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# getEntityName (Client API reference)

[!INCLUDE[](../../../../../includes/cc_applies_to_update_9_0_0.md)]

[!INCLUDE[./includes/getEntityName-description.md](./includes/getEntityName-description.md)]

## Grid types supported

Read-only and editable grids

## Syntax

`gridContext.getEntityName();`

## Return Value

**Type**: String

**Description**: The logical name of the entity data displayed in the grid.

## Remarks

To get the `gridContext`, see [Getting the grid context](../../grids.md#bkmk_gridcontext). 


