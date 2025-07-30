---
title: "getRelationship (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the getRelationship method.
author: clromano
ms.author: clromano
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# getRelationship (Client API reference)

[!INCLUDE[./includes/getRelationship-description.md](./includes/getRelationship-description.md)]

## Grid types supported

Read-only and editable grids

## Syntax

`gridContext.getRelationship();`

## Return Value

**Type**: Object.

**Description**: A relationship object with the following:

- **attributeName**: String. Name of the column.
- **name**: String. Name of the relationship. 
- **navigationPropertyName**: String. Name of the navigation property for this relationship.
- **relationshipType**: Number. Returns one of the following values to indicate the relationship type:
    - 0: OneToMany
    - 1: ManyToMany
- **roleType**: Number. Returns one of the following values to indicate the role type of relationship:
    - 1: Referencing
    - 2: AssociationEntity

## Remarks

To get the `gridContext`, see [Getting the grid context](../../grids.md#bkmk_gridcontext).

### Related articles

[openRelatedGrid](openRelatedGrid.md)

[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]
