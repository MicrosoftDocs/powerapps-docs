---
title: Round, RoundDown, and RoundUp functions in Power Apps
description: Reference information including syntax and examples for the Round, RoundDown, and RoundUp functions in Power Apps.
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: nabuthuk
ms.date: 11/07/2015
ms.subservice: canvas-maker
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - gregli-msft
  - nkrb
---
# Round, RoundDown, and RoundUp functions in Power Apps
Rounds a number.

## Description
The **Round**, **RoundDown**, and **RoundUp** functions round a number to the specified number of decimal places:

* **Round** rounds up if the next digit is a 5 or higher. Otherwise, this function rounds down.
* **RoundDown** always rounds down to the previous lower number.
* **RoundUp** always rounds up to the next higher number.

If you pass a single number, the return value is the rounded version of that number.  If you pass a single-column [table](../working-with-tables.md) that contains numbers, the return value is a single-column table of rounded numbers. If you have a multi-column table, you can shape it into a single-column table, as [working with tables](../working-with-tables.md) describes.

## Syntax
**Round**( *Number*, *DecimalPlaces* )<br>**RoundDown**( *Number*, *DecimalPlaces* )<br>**RoundUp**( *Number*, *DecimalPlaces* )

* *Number* - Required. The number to round.
* *DecimalPlaces* - Required.  The number of places to the right of the decimal point to round to.  Use 0 to round to a whole number.  



[!INCLUDE[footer-include](../../../includes/footer-banner.md)]