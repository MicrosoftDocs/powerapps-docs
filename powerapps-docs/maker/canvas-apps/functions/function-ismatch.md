---
title: IsMatch function | Microsoft Docs
description: Reference information, including syntax, for the IsMatch function in PowerApps
documentationcenter: na
author: gregli-msft
manager: kfile
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: reference
ms.component: canvas
ms.date: 02/05/2017
ms.author: gregli

---
# IsMatch function in PowerApps
Tests whether a text string matches a pattern.

## Description
The **IsMatch** function tests whether a text string matches a pattern that can comprise ordinary characters, predefined patterns, or a [regular expression](#regular-expressions).  

Use **IsMatch** to validate what a user has typed in a **[Text input](../controls/control-text-input.md)** control. For example, you can confirm whether the user has entered a valid email address before the result is saved to your data source. If the entry doesn't match your criteria, add other controls that prompt the user to correct the entry.

By default, **IsMatch** performs a case-sensitive match for the entire text string. You can modify this behavior by specifying one or more [**MatchOptions**](#match-options).

**IsMatch** returns *true* if the text string matches the pattern or *false* if it doesn't.

## Patterns
The key to using **IsMatch** is in describing the pattern to match. You describe the pattern in a text string as a combination of:

* Ordinary characters, such as  **"abc"** or **"123"**.
* Predefined patterns, such as **Letter**, **MultipleDigits**, or **Email**. (The **Match** enum defines these patterns.)
* Regular expressions codes, such as **"\d+\s+\d+"** or **"[a-z]+"**.

Combine these elements by using the [string concatenation operator **&**](operators.md). For example, **"abc" & Digit & "\s+"** is a valid pattern that matches the characters "a", "b", and "c", followed by a digit from 0 to 9, followed by at least one whitespace character.

### Ordinary characters
The simplest pattern is a sequence of ordinary characters to be matched exactly.

For example, the string "Hello" matches the pattern **"Hello"** exactly. No more and no less. The string "hello!" doesn't match the pattern because of the exclamation point on the end and the case is wrong for the letter "h". (See [MatchOptions](#match-options) for ways to modify this behavior.)

In the pattern language, certain characters are reserved for special purposes. To use these characters, either prefix the character with a **\\** (backslash) to indicate that the character should be taken literally or use one of the predefined patterns. This table lists the special characters:

| Special character | Description |
| --- | --- |
| **.** |dot or period |
| **?** |question mark |
| **&#42;** |asterisk |
| **\+** |plus |
| **( )** |parenthesis |
| **[ ]** |square brackets |
| **{ }** |curly braces |
| **^** |caret |
| **$** |dollar sign |
| **&#124;** |vertical bar or pipe |
| **\\** |backslash |

For example, you can match "Hello?" by using the pattern **"Hello\\?"** with a backslash before the question mark.

### Predefined patterns
Predefined patterns provide a simple way to match one of a set of characters, or a sequence of multiple characters. Use the [string concatenation operator **&**](operators.md) to combine your own text strings with members of the **Match** enum:

| Match Enum | Description | Regular Expression |
| --- | --- | --- |
| **Any** |Matches any character. |**.** |
| **Comma** |Matches a comma. |**,** |
| **Digit** |Matches a single digit ("0" through "9"). |**\\d** |
| **Email** |Matches an email address that contains an "at" symbol ("@") and a domain name that contains a dot (".") |**.+@.+\\.[^\\.]{2,}** |
| **Hyphen** |Matches a hyphen. |**\\-** |
| **LeftParen** |Matches a left parenthesis "(". |**\\(** |
| **Letter** |Matches a letter. |**\\p{L}** |
| **MultipleDigits** |Matches one or more digitis. |**\\d+** |
| **MultipleLetters** |Matches one or more letters. |**\\p{L}+** |
| **MultipleNonSpaces** |Matches one or more characters that don't add whitespace (space, tab, newline). |**\\S+** |
| **MultipleSpaces** |Matches one or more characters that add whitespace (space, tab, newline). |**\\s+** |
| **NonSpace** |Matches a single character that doesn't add whitespace. |**\\S** |
| **OptionalDigits** |Matches zero, one, or more digits. |**\\d** |
| **OptionalLetters** |Matches zero, one, or more letters. |**\\p{L}** |
| **OptionalNonSpaces** |Matches zero, one, or more characters that don't add whitespace. |**\\S** |
| **OptionalSpaces** |Matches zero, one, or more characters that add whitespace. |**\\s** |
| **Period** |Matches a period or dot ("."). |**\\.** |
| **RightParen** |Matches a right parenthesis ")". |**\\)** |
| **Space** |Matches a character that adds whitespace. |**\\s** |

For example, the pattern **"A" & MultipleDigits** will match the letter "A" followed by one or more digits.  

### Regular expressions
The pattern used by **IsMatch** is a *regular expression*. The ordinary characters and predefined patterns that are described above help build regular expressions.  

Regular expressions are very powerful, available in many programming languages, and used for a wide variety of purposes. This article can't describe all aspects of regular expressions, but a wealth of information and tutorials are published on the web to aid you.  

Regular expressions have different dialects, and PowerApps uses a variant of the JavaScript dialect. For more information, see [regular expression syntax](http://msdn.microsoft.com/library/1400241x.aspx).

In the **Match** enum table above, each enum expands into a regular expression, and the text string in the "Regular Expression" column defines that expression.

## Match options
You can modify the behavior of **IsMatch** by specifying one or more options, which you can combine by using the string concatenation operator (**&amp;**).  

By default, **IsMatch** tests for a complete match of the entire text string.

| MatchOptions Enum | Description | Impact on regular expression |
| --- | --- | --- |
| **BeginsWith** |The pattern must match from the beginning of the text. |Adds a **^** to the start of the regular expression. |
| **Complete** |Default.  The pattern must match the entire text, from beginning to end. |Adds a **^** to the start and **$** to the end of the regular expression. |
| **Contains** |The pattern must appear somewhere in the text but doesn't need to begin or end it. |Doesn't modify the regular expression. |
| **EndsWith** |The pattern must match the end of the text. |Adds a **$** to the end of the regular expression. |
| **IgnoreCase** |Treats the matching of letters in a case-insensitive manner. By default, matching is case sensitive. |Doesn't modify the regular expression. |
| **Multiline** |Matches across multiple lines. |Doesn't modify the regular expression. |

## Syntax
**IsMatch**( *Text*, *Pattern* [, *Options* ] )

* *Text* – Required.  The text string to test.
* *Pattern* – Required.  The pattern to test, as a text string.  Concatenate predefined patterns that the **Match** enum defines or provide a regular expression.
* *Options* – Optional.  A text string combination of **MatchOptions** enum values.  By default, **MatchOptions.Complete** is used.

## Examples
### Ordinary characters
Imagine that your app contains a **Text input** control named **TextInput1**.  The user enters values into this control to be stored in a database.   

The user types **Hello world** into **TextInput1**.

| Formula | Description | Result |
| --- | --- | --- |
| **IsMatch( TextInput1.Text, "Hello world" )** |Tests whether the user's input matches, exactly, the string "Hello world" |**true** |
| **IsMatch( TextInput1.Text, "Good bye" )** |Tests whether the user's input matches, exactly, the string "Good bye" |**false** |
| **IsMatch( TextInput1.Text, "hello", Contains )** |Tests whether the user's input contains  the word "hello" (case sensitive). |**false** |
| **IsMatch( TextInput1.Text, "hello", Contains & IgnoreCase )** |Tests whether the user's input contains the word "hello" (case insensitive). |**true** |

### Predefined patterns
| Formula | Description | Result |
| --- | --- | --- |
| **IsMatch( "123-45-7890", Digit & Digit & Digit & Hyphen & Digit & Digit & Hyphen & Digit & Digit & Digit & Digit & Digit )** |Matches a United States Social Security Number |**true** |
| **IsMatch( "joan@contoso.com", Email )** |Matches an email address |**true** |
| **IsMatch( "123.456", MultipleDigits & Period & OptionalDigits )** |Matches a sequence of digits, a period, and then zero or more digits. |**true** |
| **IsMatch( "123", MultipleDigits & Period & OptionalDigits )** |Matches a sequence of digits, a period, and then zero or more digits. A period doesn't appear in the text, so this pattern isn't matched. |**false** |

### Regular expressions
| Formula | Description | Result |
| --- | --- | --- |
| **IsMatch( "986", "\d+" )** |Matches a an integer greater than zero. |**true** |
| **IsMatch( "1.02", "\d+(\.\d\d)?" )** |Matches a positive currency amount. If the input contains a decimal point, the input must also contain 2 numeric characters after the decimal point. For example, 3.00 is valid, but 3.1 isn't. |**true** |
| **IsMatch( "-4.95", "(-)?\d+(\.\d\d)?" )** |Matches a positive or negative currency amount. If the input contains a decimal point, the input must also contain 2 numeric characters after the decimal point. |**true** |
| **IsMatch( "111-11-1111", "\d{3}-\d{2}-\d{4}" )** |Matches a United States Social Security number.  Validates the format, type, and length of the supplied input field. The string to match must consist of 3 numeric characters followed by a dash, then 2 numeric characters followed by a dash, and then 4 numeric characters. |**true** |
| **IsMatch( "111-111-111", "\d{3}-\d{2}-\d{4}" )** |Same as the previous example, but one of the hyphens is out of place in the input. |**false** |
| **IsMatch( "weakpassword", "(?!^[0-9]\*$)(?!^[a-zA-Z]\*$)([a-zA-Z0-9]{8,10})" )** |Validates a strong password, which must contain 8, 9, or 10 characters, in addition to at least one digit and at least one alphabetic character. The string must not contain special characters. |**false** |
| **IsMatch( "http://microsoft.com", "(ht&#124;f)tp(s?)\:\/\/\[0-9a-zA-Z\]([-.\w]\*[0-9a-zA-Z])\*(:(0-9)\*)\*(\/?)([a-zA-Z0-9\-\.\?\,\'\/\\\+&amp;%\$#_]\*)?" )** |Validates an http, https, or ftp URL. |**true** |

