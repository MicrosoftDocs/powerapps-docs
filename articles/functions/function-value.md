<properties
	pageTitle="Value function | Microsoft PowerApps"
	description="Reference information, including syntax, for the Value function in PowerApps"
	services=""
	suite="powerapps"
	documentationCenter="na"
	authors="gregli-msft"
	manager="dwrede"
	editor=""
	tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="11/07/2015"
   ms.author="gregli"/>

# Value function in PowerApps #

Converts a string of text to a number.

## Description ##

The **Value** function converts a string of text that contains number characters to a number value. Use this function to perform calculations on text that the user enters and that contain numbers.

Different languages interpret **,** and **.** differently.  By default, the text is interpreted in the language of the current user.  You can specify the language to use with a language tag, using the same language tags that are returned by the **[Language](function-language.md)** function.

## Syntax ##

**Value**( *String* [, *LanguageTag* ] )

- *String* - Required. String to convert to a numeric value.
- *LanguageTag* - Optional.  The language tag in which to parse the string.  If not specified, the language of the current user is used.

## Examples ##

The user running these formulas is located in the United States and has selected English as their language.  The **Language** function is returning "en-US".

| Formula | Description | Result |
|---------|-------------|--------|
| **Value( "123.456" )** | The default language of "en-US" will be used, which uses a period as the decimal separator.  | 123.456 |
| **Value( "123.456", "es-ES" )** | "es-ES" is the language tag for Spanish in Spain.  In Spain, a period is a thousands separator.  | 123456 |
| **Value( "123,456" )** | The default language of "en-US" will be used, which uses a comma as a thousands separator.  | 123456 |
| **Value( "123,456", "es-ES" )** | "es-ES" is the language tag for Spanish in Spain.  In Spain, a comma is the decimal separator.  | 123.456 |
