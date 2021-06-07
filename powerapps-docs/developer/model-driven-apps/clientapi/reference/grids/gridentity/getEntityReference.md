---
title: "getEntityReference (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the getEntityReference method.
ms.date: 04/21/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: b8e23eee-f20f-4db9-9cc6-7fa5dd7ce2bb
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# getEntityReference (Client API reference)



[!INCLUDE[./includes/getEntityReference-description.md](./includes/getEntityReference-description.md)]

## Grid types supported

Read-only and editable grids

## Syntax

`gridEntity.getEntityReference();`

## Return Value

**Type**: Lookup

**Description**: Lookup object that references the record in the row. The object has the following values:

- **entityType**: String. The logical name for the record in the row. The same data returned by the **GridEntity**.[getEntityName](getEntityName.md) method.
- **id**: String. The Id for the record in the row. The same data returned by the **GridEntity**.[getId](getId.md) method.
- **name**: String. The primary column value for the record in the row. The same data returned by the **GridEntity**.[getPrimaryAttributeValue](getPrimaryAttributeValue.md) method.

## Remarks

To get the `gridEntity` object, see [GridEntity](../gridentity.md). 



[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]