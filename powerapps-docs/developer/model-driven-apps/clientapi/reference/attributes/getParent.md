---
title: "getParent (Client API reference)| MicrosoftDocs"
description: Returns the formContext.data.entity object that is the parent to all the columns.
ms.date: 04/15/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 6d77db1b-18b4-410f-b91b-d2b65b369946
author: "Nkrb"
ms.subservice: mda-developer
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# getParent (Client API reference)

Returns the `formContext.data.entity` object that is the parent to all the columns. 

## Column types supported

All

## Syntax

`formContext.getAttribute(arg).getParent()`

[!INCLUDE[cc-terminology](../../../../data-platform/includes/cc-terminology.md)]

## Return Value

**Type**: `formContext.data.entity` object. 

**Description**: The parent object.



[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]