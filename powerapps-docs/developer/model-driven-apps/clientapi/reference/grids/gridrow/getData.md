---
title: "getData (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the getData method.
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
# getData (Client API reference)



[!INCLUDE[./includes/getData-description.md](./includes/getData-description.md)]

As this is deprecated, you should use **GridRow.data**.

## Grid types supported

Read-only and editable grids

## Syntax

`gridRow.getData();`

## Return Value

**Type**: [GridRowData](../gridrowdata.md)

## Remarks

To get the `gridRow` object, see [GridRow](../gridrow.md). 



[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]