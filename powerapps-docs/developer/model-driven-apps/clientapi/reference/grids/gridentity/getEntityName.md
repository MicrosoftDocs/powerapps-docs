---
title: "getEntityName (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the getEntityName method.
ms.date: 04/21/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 20f9127f-c90a-4ea9-aab3-6ef1f0347a48
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# getEntityName (Client API reference)



[!INCLUDE[./includes/getEntityName-description.md](./includes/getEntityName-description.md)]

## Grid types supported

Read-only and editable grids

## Syntax

`gridEntity.getEntityName();`

## Return Value

**Type**: String

**Description**: The logical name for the record in the row.

## Remarks

To get the `gridEntity` object, see [GridEntity](../gridentity.md). 



[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]