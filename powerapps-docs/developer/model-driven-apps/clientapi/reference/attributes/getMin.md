---
title: "getMin (Client API reference)"
description: Includes description and supported parameters for the getMin method.
author: clromano
ms.author: clromano
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: mda-developer
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# getMin (Client API reference)

Returns a number indicating the minimum allowed value for a column. 

## Column types supported

Decimal, integer, double, money

## Syntax

`formContext.getAttribute(arg).getMin()`

## Return Value

**Type**: Number. 

**Description**: The minimum allowed value for the column.

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
