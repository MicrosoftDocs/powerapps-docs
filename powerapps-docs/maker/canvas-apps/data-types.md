---
title: Operators | Microsoft Docs
description: Data types in canvas apps
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: anneta
ms.date: 05/04/2019
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Data types in canvas apps

| Data type | Description | Examples |
|-----------|-------------|---------|
| Boolean | A *true* or *false* value.  Can be used directly in **If**, **Filter** and other functions without a comparison.  | *true* |
| Hyperlink |
| Currency |
| Image |
| Color | A color including an alpha channel.  | Color.Red<br>ColorValue( "#102030" )<br>RGBA( 255, 128, 0, 0.5 ) | 
| Date | A date only. |
| DateTime | A date with time. |
| Number | Floating point number. | 123<br>-4.567<br>8.903e121 |
| Time | A time only. | 
| Text | 
| GUID | A [Globally Unique Identifier](https://en.wikipedia.org/wiki/Universally_unique_identifier). | GUID()<br>GUID( "123e4567-e89b-12d3-a456-426655440000" ) |
| Polymorphic |
| Media |
| Option set | An option from a set of options, backed by a number. It combines both a numeric value that is storead and used for comparisons with a text label for display to app users. | 
| Two option | An option from a set of two options, backed by a boolean.  It combines both a boolean value that is stored and used for comparisons with a text label for display to app users.  The boolean value can be used directly in **If**, **Filter** and other boolean contexts. |

All data types can be *blank*.


| Data type | Range |
|-----------|-------|
| Color | 0–255 for each component.  Alpha channel is converted to a 0–255 value. |
| Number | –1.7976931348623157e+308 to 1.7976931348623157e+308<br>Safe integer: –9,007,199,254,740,991 (–(2<sup>53</sup>–1)) to 9,007,199,254,740,991 (2<sup>53</sup>–1)<br>Smallest value: 5e–324
| Text |
