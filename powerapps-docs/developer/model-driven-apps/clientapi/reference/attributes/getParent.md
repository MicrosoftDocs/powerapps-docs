---
title: "getParent (Client API reference)| MicrosoftDocs"
description: Returns the formContext.data.entity object that is the parent to all the columns.
ms.author: jdaly
author: adrianorth
manager: kvivek
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.subservice: mda-developer
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
  - JimDaly
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