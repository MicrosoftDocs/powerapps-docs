---
title: "getCurrentView (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the getCurrentView method.
author: sriharibs-msft
ms.author: srihas
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
  - JimDaly
---
# getCurrentView (Client API reference)



[!INCLUDE[./includes/getCurrentView-description.md](./includes/getCurrentView-description.md)]

## Grid types supported

Read-only grid

## Syntax

`viewSelector.getCurrentView();`

## Return Value

**Type**: Lookup object

**Description**: The Lookup object has the following values:

- **entityType**: Number. The object type code for the SavedQuery (1039) or UserQuery (4230) that represents the view the user can select.
- **id**: String. The Id for the view the user can select.
- **name**: String. The name of the view the user can select.

## Remarks

If the subgrid control is not configured to display the view selector, calling this method on the `viewSelector` object will throw an error.

To get the `viewSelector` object, see [ViewSelector](../viewselector.md).





[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]