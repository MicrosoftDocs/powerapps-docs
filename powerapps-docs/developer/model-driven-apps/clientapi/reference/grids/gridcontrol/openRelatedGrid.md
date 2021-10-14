---
title: "openRelatedGrid (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the openRelatedGrid method.
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
# openRelatedGrid (Client API reference)



[!INCLUDE[./includes/openRelatedGrid-description.md](./includes/openRelatedGrid-description.md)]

This method does nothing if the grid is not filtered based on a relationship.

## Grid types supported

Read-only and editable grids

## Syntax

`gridContext.openRelatedGrid();`

## Remarks

To get the `gridContext`, see [Getting the grid context](../../grids.md#bkmk_gridcontext).

### Related topics

[getRelationship](getRelationship.md)

<!-- TODO: 
[Customize entity relationship metadata](../../../../customize-entity-relationship-metadata.md)  -->






[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]