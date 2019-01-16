---
title: Split function | Microsoft Docs
description: Reference information, including syntax and examples, for the Split function in PowerApps
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: anneta anneta
ms.date: 08/28/2017
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Split function in PowerApps
Splits a text string into a table of substrings.

## Description
The **Split** function breaks a text string into a table of substrings.  Use **Split** to break up comma delimited lists, dates that use a slash between date parts, and in other situations where a well defined delimiter is used.  

A separator string is used to break the text string apart.  The separator can be zero, one, or more characters that are matched as a whole in the text string.  Using a zero length or *blank* string results in each character being broken out individually.  The matched separator characters are not returned in the result.  If no separator match is found then the entire text string is returned as a single result.

Use the **[Concat](function-concatenate.md)** function to recombine the string (without the separators). Use the **[MatchAll](function-ismatch.md)** function to extract portions of a text string by using a regular expression, which (in some cases) you can use to split a string. 

## Syntax
**Split**( *Text*, *Separator* )

* *Text* - Required.  Text to split.
* *Separator* - Required.  Separator to use in splitting the string.  Can be zero, one, or more characters.

## Examples

| Formula | Description | Result |
| --- | --- | --- |
| **Split( "Apples,&nbsp;Oranges,&nbsp;Bananas", "," )** |Splits the different fruits apart, based on the comma separator.  The split is performed based on only the comma and not the space after it, resulting in a space at the front of "&nbsp;Oranges" and "&nbsp;Bananas". |<style> img { max-width: none; } </style> ![](media/function-split/fruit1.png) |
| **TrimEnds( Split( "Apples,&nbsp;Oranges,&nbsp;Bananas", "," ) )** |Same as the previous example, but in this case the space is removed by the [**TrimEnds** function](function-trim.md), operating on the single column table that is produced by **Split**. We could have also used the separator **",&nbsp;"** which includes the space after the comma, but that would not have worked properly if there is no space or there are two spaces. |<style> img { max-width: none; } </style> ![](media/function-split/fruit2.png) |
| **Split( "08/28/17", "/" )** |Splits the date apart, using a forward slash as the separator. |<style> img { max-width: none; } </style> ![](media/function-split/date.png) |
| **Split( "Hello,&nbsp;World", "," )** |Splits the words apart, using a comma as the separator.  The second result starts with a space since this was the character immediately following the comma. |<style> img { max-width: none; } </style> ![](media/function-split/comma.png) |
| **Split( "Hello,&nbsp;World", "o" )** |Splits the string apart, using the character "o" as the separator. |<style> img { max-width: none; } </style> ![](media/function-split/o.png) |
| **Split( "Hello,&nbsp;World", "l" )** |Splits the string apart, using the single character "l" as the separator. Since there were no characters between the two **l**'s in **Hello**, a *blank* value was returned. |<style> img { max-width: none; } </style> ![](media/function-split/l.png) |
| **Split( "Hello,&nbsp;World", "ll" )** |Splits the string apart, using the double character "ll" as the separator. |<style> img { max-width: none; } </style> ![](media/function-split/ll.png) |
| **Split( "Hello,&nbsp;World", "%" )** |Splits the string apart, using the percent sign as the separator. Since this separator does not appear in the string, the entire string is returned as one result. |<style> img { max-width: none; } </style> ![](media/function-split/percent.png) |
| **Split( "Hello,&nbsp;World", "" )** |Splits the string apart, using an empty string as the separator (zero characters). This will break the string on each character. |<style> img { max-width: none; } </style> ![](media/function-split/none.png) |

