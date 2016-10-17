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

The **Value** function converts a string that contains number characters to a number value. Use this function to perform calculations on strings that the user enters and that contain numbers.

The string is parsed in the locale of the current user, which includes how to interpret grouping and decimal separators such as **,** and **.**.  You can specify the locale to use by providing a language tag as an optional argument.

## Syntax ##

**Value**( *String* [, *LanguageTag*] )

- *String* - Required. String to convert to a numeric value.
- *LanguageTag* - Optional.  The language to use in parsing the string.  If not specified, the language of the current user, as returned by the **Language** function, is used.
