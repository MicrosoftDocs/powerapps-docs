<properties
	pageTitle="IsMatch function | Microsoft PowerApps"
	description="Reference information, including syntax, for the IsMatch function in PowerApps"
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
   ms.date="02/05/2017"
   ms.author="gregli"/>

# IsMatch function in PowerApps #

Tests if a string matches a pattern.

## Description ##

The **IsMatch** function tests a text string for a match with a pattern.  The pattern can be a simple concatenation of predefined common patterns or a more advanced [regular expression](#regular-expressions).  **IsMatch** returns *true* if the text string matches the pattern, *false* if it does not.

Use **IsMatch** to validate what a user has typed in to a [**Text input** control](../controls/control-text-input.md).

### Common patterns ###

The easiest way to use **IsMatch** is to provide a combination of predefined patterns and  letters, numbers, and other characters as a text string.  Use the [string concatenation operator **&**](operators.md) to combine your own text strings with members of the **Match** enum:

| Match Enum | Description | Regular Expression |
|------------|--------------------|-------------|
| **Any** |  Matches any character.  | **.** |
| **Comma** |  Matches a comma. | **,** |
| **Digit** | Matches a single digit ("0" through "9"). | **\\d** | 
| **Email** | Matches an email address that contains an ampersand ("@") and a domain name that contains a dot (".") |  **.+@.+\\.[^\\.]{2,}** |
| **Hyphen** |  Matches a hyphen. | **\\-** |
| **LeftParen** |  Matches a Left Parenthesis "(". | **\\(** |
| **Letter** |  Matches a letter. | **\\p{L}** |
| **MultipleDigits** |  Matches one or more digitis. | **\\d+** |
| **MultipleLetters** |  Matches one or more letters. | **\\p{L}+** |
| **MultipleNonSpaces** |  Matches one or more non-whitespace characters (space, tab, newline). | **\\S+** |
| **MultipleSpaces** |  Matches one or more whitespace characters (space, tab, newline). | **\\s+** |
| **NonSpace** |  Matches a single non-whitespace character. | **\\S** |
| **OptionalDigits** |  Matches zero, one, or more digits. | **\\d** |
| **OptionalLetters** |  Matches zero, one, or more letters. | **\\p{L}** |
| **OptionalNonSpaces** |  Matches zero, one, or more non-whitepace characters. | **\\S** |
| **OptionalSpaces** |  Matches zero, one, or more whitespace characters. | **\\s** |
| **Period** |  Matches a period or dot ("."). | **\\.** |
| **RightParen** |  Matches a right parenthesis (")"). | **\\)** |
| **Space** |  Matches a whitespace character. | **\\s** |

For example, **"A" & Digit & Digit** as a pattern will match the letter "A" followed by exactly two digits.  See the [Examples](#examples) section below.

Not that for some common characters, such as a dot or period, the enum value must be used.  **Digit & "." & Digit** will not match the string "1.2".  Instead, **Digit & Period & Digit** must be used.

### Regular expressions ###

At the heart of **IsMatch** is the ability to match a regular expression.  

The predefined patterns above help build regular expressions.  The third column provides the underlying regular expression that the **Match** enum member provides.  

Regular expressions are very powerful.  They are available in many programming languages and used for a wide variety of purposes.  It is beyond the scope of this article to describe all aspects of regular expressions, but there is a wealth of information and tutorials published on the web to help you.  

There are different dialects of regular expressions.  PowerApps uses a varient of the JavaScript dialect.  For more information, see:
- [Creating a regular expression](https://msdn.microsoft.com/en-us/library/ee236359.aspx)
- [Regular expression syntax](https://msdn.microsoft.com/en-us/library/1400241x.aspx)

### Match options ###

The behavior of **IsMatch** can be modified through the use of one or more options.  Options can be defined with the string concatenation operator.  

By default, **IsMatch** tests for a complete match of the entire text string.

| MatchOptions Enum | Description | Impact on regular expression | 
|------------------|-----------|-------------|
| **BeginsWith** | The pattern must match from the beginning of the text.  | Adds a **^** to the start of the regular expression. |
| **Complete** | Default.  The pattern must match the entire text, from beginning to end.  | Adds a **^** to the start and **$** to the end of the regular expression. |
| **Contains** | The pattern must appear somewhere in the text, but does not need to begin or end it. | Does not modify the regular expression. |
| **EndsWith** | The pattern must match the end of the text.  | Adds a **$** to the end of the regular expression. |
| **IgnoreCase** | Treats the matching of letters in a case insensitive manner.  By default, matching is case sensitive. | Does not modify the regular expression. |
| **Multiline** | Matches across multiple lines.  | Does not modify the regular expression.  |

## Syntax ##

**IsMatch**( *Text*, *Pattern* [, *Options* ] )

- *Text* – Required.  The text string to test.
- *Pattern* – Required.  The pattern to test, as a text string.  Concatenate predefined patterns provided with the **Match** enum or provide a regular expression.
- *Options* – Optional.  A text string combination of **MatchOptions** enum values.  By default, **MatchOptions.Complete** is used.

## Examples ##

### Common Patterns ###

| Formula | Description | Result |
|---------|-------------|--------|
| **IsMatch( "123-45-7890", Digit & Digit & Digit & Hyphen & Digit & Digit & Hyphen & Digit & Digit & Digit & Digit & Digit )** | Matches a United States Social Security Number | **true** |
| **IsMatch( "joan@contoso.com", Email )** | Matches an email address | **true** |


