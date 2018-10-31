---
title: "getEntityReference (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 10/31/2018
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: b8e23eee-f20f-4db9-9cc6-7fa5dd7ce2bb
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# getEntityReference (Client API reference)



[!INCLUDE[./includes/getEntityReference-description.md](./includes/getEntityReference-description.md)]

## Grid types supported

Read-only and editable grids

## Syntax

`gridEntity.getEntityReference();`

## Return Value

**Type**: Lookup

**Description**: Lookup object that references the record in the row. The object has the following attributes:
- **entityType**: String. The logical name for the record in the row. The same data returned by the **GridEntity**.[getEntityName](getEntityName.md) method.
- **id**: String. The Id for the record in the row. The same data returned by the **GridEntity**.[getId](getId.md) method.
- **name**: String. The primary attribute value for the record in the row. The same data returned by the **GridEntity**.[getPrimaryAttributeValue](getPrimaryAttributeValue.md) method.

## Remarks

To get the `gridEntity` object, see [GridEntity](../gridentity.md). 

