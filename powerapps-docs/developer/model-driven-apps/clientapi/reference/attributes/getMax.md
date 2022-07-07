---
title: "getMax (Client API reference)| MicrosoftDocs"
description: Includes description and supported parameters for the getMax method.
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
# getMax (Client API reference)



Returns a number indicating the maximum allowed value for a column. 

## Column types supported

decimal, integer, double, money

## Syntax

`formContext.getAttribute(arg).getMax()`

## Return Value

**Type**: Number. 

**Description**: The maximum allowed value for the column.



[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]