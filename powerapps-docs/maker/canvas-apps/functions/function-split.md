---
title: Split function in Power Apps
description: Reference information including syntax and examples for the Split function in Power Apps.
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: nabuthuk
ms.date: 09/14/2019
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Split function in Power Apps
Splits a text string into a table of substrings.

## Description
The **Split** function breaks a text string into a table of substrings.  Use **Split** to break up comma delimited lists, dates that use a slash between date parts, and in other situations where a well defined delimiter is used.  

A separator string is used to break the text string apart.  The separator can be zero, one, or more characters that are matched as a whole in the text string.  Using a zero length or *blank* string results in each character being broken out individually.  The matched separator characters are not returned in the result.  If no separator match is found then the entire text string is returned as a single result.

Use the **[Concat](function-concatenate.md)** function to recombine the string without the separators. 
 
Use the **[MatchAll](function-ismatch.md)** function to split a string using a regular expression.

The examples show how **Split** can be used with the **[First](function-first-last.md)** and **[Last](function-first-last.md)** functions to extract a single delimited substring.  The **[Match](function-ismatch.md)** function is often a more concise and powerful choice for those familiar with regular expressions.

## Syntax
**Split**( *Text*, *Separator* )

* *Text* - Required.  Text to split.
* *Separator* - Required.  Separator to use in splitting the string.  Can be zero, one, or more characters.

## Examples

### Basic usage

| Formula | Description | Result |
| --- | --- | --- |
| `Split( "Apples, Oranges, Bananas", "," )` |Splits the different fruits apart, based on the comma separator.  The split is performed based on only the comma and not the space after it, resulting in a space at the front of "&nbsp;Oranges" and "&nbsp;Bananas". | ![Split based on comma](media/function-split/fruit1.png) |
| `TrimEnds( Split( "Apples, Oranges, Bananas", "," ) )` |Same as the previous example, but in this case the space is removed by the [**TrimEnds** function](function-trim.md), operating on the single column table that is produced by **Split**. We could have also used the separator **",&nbsp;"** which includes the space after the comma, but that would not have worked properly if there is no space or there are two spaces. | ![Split with space removed](media/function-split/fruit2.png) |
| `Split( "08/28/17", "/" )` |Splits the date apart, using a forward slash as the separator. | ![Using forward slash](media/function-split/date.png) |

### Different delimiters

| Formula | Description | Result |
| --- | --- | --- |
| `Split( "Hello, World", "," )` |Splits the words apart, using a comma as the separator.  The second result starts with a space since this was the character immediately following the comma. | ![Using comma separator](media/function-split/comma.png) |
| `Split( "Hello, World", "o" )` |Splits the string apart, using the character "o" as the separator. | ![Using o separator](media/function-split/o.png) |
| `Split( "Hello, World", "l" )` |Splits the string apart, using the single character "l" as the separator. Since there were no characters between the two **l**'s in **Hello**, a *blank* value was returned. | ![Using l separator](media/function-split/l.png) |
| `Split( "Hello, World", "ll" )` |Splits the string apart, using the double character "ll" as the separator. | ![Using ll separator](media/function-split/ll.png) |
| `Split( "Hello, World", "%" )` |Splits the string apart, using the percent sign as the separator. Since this separator does not appear in the string, the entire string is returned as one result. | ![Using % separator](media/function-split/percent.png) |
| `Split( "Hello, World", "" )` |Splits the string apart, using an empty string as the separator (zero characters). This will break the string on each character. | ![Using empty string separator](media/function-split/none.png) |

### Substring extraction

| Formula | Description | Result |
| --- | --- | --- |
| `First( Split( Last( Split( "Bob Jones <bob.jones@contoso.com>", "<" ) ).Result, ">" ) ).Result` | Splits the string apart based on an opening delimiter (<) and extracts the string to the right of the delimiter with **Last**.  The formula then splits that result based on the closing delimiter (>) and extracts the string the left of the delimiter with **Right**. | "bob.jones@contoso.com" |
| `Match( "Bob Jones <bob.jones@contoso.com>", "<(?<email>.+)>" ).email` | Performs the same delimiter based extraction as the last example but uses the **Match** function and a regular expression instead. | "bob.jones@contoso.com" |



[!INCLUDE[footer-include](../../../includes/footer-banner.md)]