---
title: "getEntity (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the getEntity method.
ms.date: 04/21/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 1672c213-d315-48fb-b49c-47cc19d23c28
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
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