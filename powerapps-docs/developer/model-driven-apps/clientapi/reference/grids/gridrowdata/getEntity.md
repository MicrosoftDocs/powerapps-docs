---
title: "getEntity (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the getEntity method.
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
# getEntity (Client API reference)

[!INCLUDE[./includes/getEntity-description.md](./includes/getEntity-description.md)]

As this is deprecated, you should use **GridRowData.entity**.

## Grid types supported

Read-only and editable grids

## Syntax

`gridRowData.getEntity();`

## Return Value

**Type**: [GridEntity](../gridentity.md)

## Remarks

To get the `gridRowData` object, see [GridRowData](../gridrowdata.md). 

[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]
