<properties
	pageTitle="Split function | Microsoft PowerApps"
	description="Reference information, including syntax and examples, for the Split function in PowerApps"
	services=""
	suite="powerapps"
	documentationCenter="na"
	authors="gregli-msft"
	manager="anneta"
	editor=""
	tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="08/28/2017"
   ms.author="gregli"/>

# Split function in PowerApps #

Splits a text string into a table of substrings.

## Description ##

The **Split** function breaks a text string into a table of substrings.  Use **Split** to break up a comma delimited list, a date that use a slash between date parts, and in other situations in which a well defined delimiter is used.  

A separator string is used to break the text string apart.  The separator can be zero, one, or more characters that are matched in the text string. The separator characters that are matched are not returned in the result.

Use the [**Concat**](function-concat.md) function to recombine the string (without the separators).  

## Syntax ##

**Split**( *Text*, *Separator* )

- *Text* - Required.  Text to split.
- *Separator* - Required.  Separator to use in splitting the string.

## Examples ##

| Formula | Description | Result |
|---------|-------------|--------|
| **Split( "08/28/17", "/" )** | Splits the date apart, using a forward slash as the separator. | <style> img { max-width: none; } </style> ![](media/function-split/date.png) |
| **Split( "Hello, World", "," )** | Splits the words apart, using a comma as the separator.  The second result starts with a space since this was the character immediately following the comma. | <style> img { max-width: none; } </style> ![](media/function-split/comma.png) |
| **Split( "Hello, World", "o" )** | Splits the string apart, using the character "o" as the separator.| <style> img { max-width: none; } </style> ![](media/function-split/o.png) |
| **Split( "Hello, World", "l" )** | Splits the string apart, using the single character "l" as the separator. Since there were no characters between the two l's in **Hello**, a *blank* value was returned. | <style> img { max-width: none; } </style> ![](media/function-split/l.png) |
| **Split( "Hello, World", "ll" )** | Splits the string apart, using the double character "ll" as the separator. | <style> img { max-width: none; } </style> ![](media/function-split/ll.png) |
| **Split( "Hello, World", "%" )** | Splits the string apart, using the percent sign as the separator. Since this separator does not appear in the string, the entire string is returned as one result.  | <style> img { max-width: none; } </style> ![](media/function-split/percent.png) |
| **Split( "Hello, World", "" )** | Splits the string apart, using an empty string as the separator (zero characters). This will break the string on each character.  | <style> img { max-width: none; } </style> ![](media/function-split/none.png) |
