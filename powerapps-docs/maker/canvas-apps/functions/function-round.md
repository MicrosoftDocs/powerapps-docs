---
title: Int, Round, RoundDown, RoundUp, and Trunc functions | Microsoft Docs
description: Reference information, including syntax, for the Int, Round, RoundDown, RoundUp, and Trunc functions in Power Apps
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: nabuthuk
ms.date: 6/15/2021
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Int, Round, RoundDown, RoundUp, and Trunc functions in Power Apps
Rounds a number.

## Description
The **Round**, **RoundDown**, and **RoundUp** functions round a number to the specified number of decimal places:

* **Round** rounds up if the next digit is a 5 or higher. Otherwise, this function rounds down.
* **RoundDown** always rounds down to the previous lower number, towards zero.
* **RoundUp** always rounds up to the next higher number, away from zero.

The number of decimal places can be:

| Decimal places | Description |
|-----|-----|
| Greater than 0 | The number is rounded to the right of the decimal separator.  | 
| 0 |  The number is rounded to the nearest integer. |
| Less than 0 | The number is rounded to the left of the decimal separator.  |

The **Int** and **Trunc** functions round a number to an integer (whole number without a decimal): 

* **Int** rounds down to the nearest integer.  
* **Trunc** truncates the number to just the integer portion by removing any decimal portion.  

The difference between **Int** and **Trunc** is in the handling of negative numbers.  For example, for an argument of `-4.3`, **Int** will return the integer further away from zero, `-5`, while **Trunc** will return the integer closer to zero, `-4`.   **Int** returns values that are unique amongst the five rounding functions, while **Trunc** returns the same values as **RoundDown** with 0 decimal places.

Use **Trunc** to extract the decimal portion of a number by subtracting from the original, for example `X - Trunc(X)`.  

If you pass a single number, the return value is the rounded version of that number.  If you pass a single-column [table](../working-with-tables.md) that contains numbers, the return value is a single-column table of rounded numbers. If you have a multi-column table, you can shape it into a single-column table, as [working with tables](../working-with-tables.md) describes.

## Syntax
**Round**( *Number*, *DecimalPlaces* )<br>**RoundDown**( *Number*, *DecimalPlaces* )<br>**RoundUp**( *Number*, *DecimalPlaces* )

* *Number* - Required. The number to round.
* *DecimalPlaces* - Required.  The number of places to the right of the decimal point to round to.  Use 0 to round to a whole number.  Use a negative number to round to the left of the decimal place.

**Int**( *Number* )<br>**Trunc**( *Number* )

* *Number* - Required. The number to round to an integer.

## Examples

| `X`  | `Round( X, 0 )` | `RoundUp( X, 0 )` | `RoundDown( X, 0 )` | `Int( X )` | `Trunc( X )` |
|:----:|:-----:|:-----:|:------:|:----:|:-----:|
| 7.9  | 8  | 8  | 7  | 7  | 7  |
| -7.9 | -8 | -8 | -7 | -8 | -7 |
| 7.5  | 8  | 8  | 7  | 7  | 7  |
| -7.5 | -8 | -8 | -7 | -8 | -7 |
| 7.1  | 7  | 8  | 7  | 7  | 7  |
| -7.1 | -7 | -8 | -7 | -8 | -7 |

| `X` | `Round( X, 2 )` | `RoundUp( X, 2 )` | `RoundDown( X, 2 )` | 
|:----:|:----:|:------------:|:----------:|
| 430.123 | 430.12 | 430.13 | 430.12 | 
| 450.125 | 450.13 | 450.13 | 450.12 | 
| 479.128 | 479.13 | 479.13 | 479.12 |

| `X` | `Round( X, -2 )` | `RoundUp( X, -2 )` | `RoundDown( X, -2 )` |
|:----:|:----:|:------------:|:----------:|
| 430.123 | 400 | 500 | 400 |
| 449.942 | 400 | 500 | 400 |
| 450.000 | 500 | 500 | 400 |
| 450.124 | 500 | 500 | 400 |
| 479.128 | 500 | 500 | 400 |

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]