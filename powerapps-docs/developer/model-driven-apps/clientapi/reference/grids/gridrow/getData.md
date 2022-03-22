---
title: "getData (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the getData method.
ms.author: jdaly
author: adrianorth
manager: kvivek
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
  - JimDaly
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