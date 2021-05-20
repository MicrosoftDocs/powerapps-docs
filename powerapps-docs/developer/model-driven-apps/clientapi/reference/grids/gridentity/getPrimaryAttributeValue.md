---
title: "getPrimaryAttributeValue (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the getPrimaryAttributeValue method.
ms.date: 04/21/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 4bd76f0c-5905-4bc2-a423-7d74a267a464
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# getPrimaryAttributeValue (Client API reference)



[!INCLUDE[./includes/getPrimaryAttributeValue-description.md](./includes/getPrimaryAttributeValue-description.md)]

## Grid types supported

Read-only grid

## Syntax

`gridEntity.getPrimaryAttributeValue();`

## Return Value

**Type**: String

**Description**: The primary column value for the record in the row.

## Remarks

To get the `gridEntity` object, see [GridEntity](../gridentity.md). 



[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]