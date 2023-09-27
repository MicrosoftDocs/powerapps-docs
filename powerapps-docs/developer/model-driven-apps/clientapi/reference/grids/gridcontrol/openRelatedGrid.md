---
title: "openRelatedGrid (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the openRelatedGrid method.
author: jasongre
ms.author: jasongre
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
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

### Related articles

[getRelationship](getRelationship.md)

[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]
