---
title: Value function in Power Apps
description: Reference information including syntax and examples for the Value function in Power Apps.
author: gregli-msft
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 02/06/2020
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
# Value function in Power Apps
Converts a string of text to a number.

## Description
The **Value** function converts a string of text that contains number characters to a number value. Use this function when you need to perform calculations on numbers that were entered as text by a user.

Different languages interpret **,** and **.** differently.  By default, the text is interpreted in the language of the current user.  You can specify the language to use with a language tag, using the same language tags that are returned by the **[Language](function-language.md)** function.

Notes on the format of the string:

* The string may be prefixed with the currency symbol for the current language.  The currency symbol is ignored.  Currency symbols for other languages are not ignored.
* The string may be include a percent sign (**%**) at the end, indicating that it is a percentage.  The number will be divided by 100 before being returned.  Percentages and currency symbols cannot be mixed.
* The string may be in scientific notation, with 12 x 10<sup>3</sup> expressed as "12e3".

If the number is not in a proper format, **Value** will return *blank*.

To convert date and time values, use the [**DateValue**](function-datevalue-timevalue.md), [**TimeValue**](function-datevalue-timevalue.md), or [**DateTimeValue**](function-datevalue-timevalue.md) functions.

## Syntax
**Value**( *String* [, *LanguageTag* ] )

* *String* - Required. String to convert to a numeric value.
* *LanguageTag* - Optional.  The language tag in which to parse the string.  If not specified, the language of the current user is used.

## Examples
The user running these formulas is located in the United States and has selected English as their language.  The **Language** function is returning "en-US".

| Formula | Description | Result |
| --- | --- | --- |
| **Value( "123.456" )** |The default language of "en-US" will be used, which uses a period as the decimal separator. |123.456 |
| **Value( "123.456", "es-ES" )** |"es-ES" is the language tag for Spanish in Spain.  In Spain, a period is a thousands separator. |123456 |
| **Value( "123,456" )** |The default language of "en-US" will be used, which uses a comma as a thousands separator. |123456 |
| **Value( "123,456", "es-ES" )** |"es-ES" is the language tag for Spanish in Spain.  In Spain, a comma is the decimal separator. |123.456 |
| **Value( "12.34%" )** |The percentage sign at the end of the string indicates that this is a percentage. |0.1234 |
| **Value( "$ 12.34" )** |The currency symbol for the current language is ignored. |12.34 |
| **Value( "24e3" )** |Scientific notation for 24 x 10<sup>3</sup>. |24000 |



[!INCLUDE[footer-include](../../../includes/footer-banner.md)]