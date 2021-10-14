---
title: "getRelationship (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the getRelationship method.
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

### Related topics

[openRelatedGrid](openRelatedGrid.md)





[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]