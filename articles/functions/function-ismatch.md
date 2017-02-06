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

Tests if a text string matches a pattern.

## Description ##

The **IsMatch** function tests a text string for a match with a pattern.  The pattern can be a concatenation of ordinary characters, predefined patterns, or a [regular expression](#regular-expressions).  

Use **IsMatch** to validate what a user has typed in to a [**Text input** control](../controls/control-text-input.md).  For example, you can check if the user has entered a valid email address before saving the result to your data source.  Use other controls to display a warning and have the user correct their entry.

By default, **IsMatch** preforms a case sensitive match for the entire text string.  You can modify this behavior by providing one or more [**MatchOptions**](#match-options).

**IsMatch** returns *true* if the text string matches the pattern, *false* if it does not. 

## Patterns ##

The key to using **IsMatch** is in describing a pattern to match.  Patterns are described in a text string combining:
- Ordinary characters.  **"abc"** or **"123"**.
- Predefined patterns.  **Letter**, **MultipleDigits**, or **Email**.  These are provided by the **Match** enum.
- Regular expressions codes.  **"\d+\s+\d+"** or **"[a-z]+"**.

You can combine these elements with the [string concatenation operator **&**](operators.md).  For example, **"abc" & Digit & "\s+"**.

### Ordinary characters ###

The simplest pattern is a sequence of ordinary characters to be matched exactly. 

For example, the pattern **"Hello"** will match exactly the string "Hello".  No more and no less.  The string "hello!" would not be matched (without some options described later).

Certain characters are reserved in the pattern language for special purposes.  To use these characters, either prefix the character with a **\** (backslash) to indicate that it should be taken literally or use one of the predefined patterns.  These characters are:

| Special character | Description |
|-------------------|-------------|
| **.** | dot or period |
| **?** | question mark |  
| **\*** | asterisk |
| **\+** | plus |
| **( )** | parenthesis |
| **[ ]** | square brackets |
| **{ }** | curly braces |
| **^** | caret |
| **$** | dollar sign |
| **&#124;** | vertical bar or pipe |
| **\** | backslash |

For example, to match "Hello?" use the pattern **"Hello\?"** with a backslash before the question mark.

### Predefined patterns ###

Predefined patterns provide a simple way to match one of a set of characters or a sequence of multiple characters.  Use the [string concatenation operator **&**](operators.md) to combine your own text strings with members of the **Match** enum:

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

For example, the pattern **"A" & MultipleDigits** will match the letter "A" followed by one or more digits.  

### Regular expressions ###

The pattern used by **IsMatch** is a Regular Expression.  The ordinary characters and predefined patterns described above help build regular expressions.  

Regular expressions are very powerful.  They are available in many programming languages and used for a wide variety of purposes.  It is beyond the scope of this article to describe all aspects of regular expressions, but there is a wealth of information and tutorials published on the web to aid you.  

There are different dialects of regular expressions.  PowerApps uses a variant of the JavaScript dialect.  For more information, see [regular expression syntax](http://msdn.microsoft.com/library/1400241x.aspx).

In the **Match** enum table above, the "Regular Expression" column provides the regular expression text string that the enum expands into.

## Match options ##

The behavior of **IsMatch** can be modified through a set of options.  Options can be combined with the string concatenation operator.  

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

### Ordinary characters ###

Imagine that your app contains a **Text input** control named **TextInput1**.  The user enters values into this control to be stored in a database.   

Our user types **Hello world** into **TextInput1**.

| Formula | Description | Result |
|---------|-------------|--------|
| **IsMatch( TextInput1.Text, "Hello world" )** | Tests if the user's input matches, exactly, the string "Hello world" | **true** |
| **Ismatch( TextInput1.Text, "Good bye" )** | Tests if the user's input matches, exactly, the string "Good bye" | **false** |
| **IsMatch( TextInput1.Text, "hello", Contains )** | Tests if the user's input contains  the word "hello" (case sensitive). | **false** |
| **IsMatch( TextInput1.Text, "hello", Contains & IgnoreCase )** | Tests if the user's input contains the word "hello" (case insensitive). | **true** |

### Predefined patterns ###

| Formula | Description | Result |
|---------|-------------|--------|
| **IsMatch( "123-45-7890", Digit & Digit & Digit & Hyphen & Digit & Digit & Hyphen & Digit & Digit & Digit & Digit & Digit )** | Matches a United States Social Security Number | **true** |
| **IsMatch( "joan@contoso.com", Email )** | Matches an email address | **true** |
| **IsMatch( "123.456", MultipleDigits & Period & OptionalDigits )** | Matches a sequence of digits, a period, and then zero or more digits.  | **true** |
| **IsMatch( "123", MultipleDigits & Period & OptionalDigits )** | Matches a sequence of digits, a period, and then zero or more digits.  Sine a period does not appear, in the text, this pattern is not matched. | **false** |







