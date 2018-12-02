---
title: IsMatch, Match, and MatchAll functions | Microsoft Docs
description: Reference information, including syntax, for the IsMatch, Match, and MatchAll functions in PowerApps
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: anneta
ms.date: 02/05/2017
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# IsMatch, Match, and MatchAll functions in PowerApps
Tests for a match or extracts portions of a text string based on a pattern.

## Description
The **IsMatch** function tests whether a text string matches a pattern that can comprise ordinary characters, predefined patterns, or a [regular expression](#regular-expressions).  The **Match** and **MatchAll** functions return what was matched including sub-matches.  

Use **IsMatch** to validate what a user has typed in a **[Text input](../controls/control-text-input.md)** control. For example, you can confirm whether the user has entered a valid email address before the result is saved to your data source. If the entry doesn't match your criteria, add other controls that prompt the user to correct the entry.

Use **Match** to extract the portion of a text string that matches a pattern; **MatchAll** to extract all portions that match.  Sub-matches can also be extracted to parse complex strings into a set of result values with one function call.   

**Match** returns a record of information for the first match found while **MatchAll** returns a table of records for every match found.  This record contains predefined columns and named sub-matches.  The predefined columns are:

| Column | Type | Description |
|----|----|----|
| **FullMatch** | Text | The text that was matched. |
| **StartMatch** | Number | The starting position of the match within the input string.  The first character of the string returns 1. | 
| **SubMatches** | Single column table of Text (column **Value**) | The table of named and unnamed sub-matches in the order they appear in the regular expression. Use the [**ForAll**](function-forall.md) function or **[Last](function-first-last.md)( [FirstN](function-first-last.md)( **...** ) )** functions to work with an individual sub-match. |

Named sub-matches are created with **(?&lt;*name*&gt;**...**)** in the regular expression.  For each named sub-match, the column **name** will be provided in the result of **Match** and **MatchAll**.  If a named sub-match has the same name as a predefined column then the sub-match will take precedence and a warning will be generated.  Rename the sub-match to a different name to remove this warning. 

By default, these functions perform a case-sensitive match.  By default, **IsMatch** will match the entire text string while **Match** and **MatchAll** will search for a match anywhere in the text string. You can modify this behavior by specifying one or more [**MatchOptions**](#match-options).

**IsMatch** returns *true* if the text string matches the pattern or *false* if it doesn't.  **Match** returns *blank* if no match is found that can be tested with the **IsBlank** function.  **MatchAll** returns an empty table if no match is found that can be tests with the **IsEmpty** function.

## Patterns
The key to using these functions is in describing the pattern to match. You describe the pattern in a text string as a combination of:

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
| **Email** |Matches an email address that contains an "at" symbol ("\@") and a domain name that contains a dot (".") |**.+\@.+\\.[^\\.]{2,}** |
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

Regular expressions have different dialects, and PowerApps uses a variant of the JavaScript dialect. For more information, see [regular expression syntax](http://msdn.microsoft.com/library/1400241x.aspx).  One key addition are named sub-matches expressed with **(?&lt;*name*&gt;** ... **)**. 

In the **Match** enum table above, each enum expands into a regular expression, and the text string in the "Regular Expression" column defines that expression.

## Match options
You can modify the behavior of **IsMatch** by specifying one or more options, which you can combine by using the string concatenation operator (**&amp;**).  

By default, **IsMatch** tests for a complete match of the entire text string while **Match** and **MatchAll** look for a match anywhere in the text string.

| MatchOptions Enum | Description | Impact on regular expression |
| --- | --- | --- |
| **BeginsWith** |The pattern must match from the beginning of the text. |Adds a **^** to the start of the regular expression. |
| **Complete** |Default for **IsMatch**.  The pattern must match the entire text, from beginning to end. |Adds a **^** to the start and **$** to the end of the regular expression. |
| **Contains** |Default for **Match** and **IsMatch**.  The pattern must appear somewhere in the text but doesn't need to begin or end it. |Doesn't modify the regular expression. |
| **EndsWith** |The pattern must match the end of the text. |Adds a **$** to the end of the regular expression. |
| **IgnoreCase** |Treats the matching of letters in a case-insensitive manner. By default, matching is case sensitive. |Doesn't modify the regular expression. |
| **Multiline** |Matches across multiple lines. |Doesn't modify the regular expression. |

## Syntax
**IsMatch**( *Text*, *Pattern* [, *Options* ] )

* *Text* – Required.  The text string to test.
* *Pattern* – Required.  The pattern to test, as a text string.  Concatenate predefined patterns that the **Match** enum defines or provide a regular expression.
* *Options* – Optional.  A text string combination of **MatchOptions** enum values.  By default, **MatchOptions.Complete** is used.

**Match**( *Text*, *Pattern* [, *Options* ] )

* *Text* – Required.  The text string to test.
* *Pattern* – Required.  The pattern to test, as a text string.  Concatenate predefined patterns that the **Match** enum defines or provide a regular expression.
* *Options* – Optional.  A text string combination of **MatchOptions** enum values.  By default, **MatchOptions.Contains** is used.

**MatchAll**( *Text*, *Pattern* [, *Options* ] )

* *Text* – Required.  The text string to test.
* *Pattern* – Required.  The pattern to test, as a text string.  Concatenate predefined patterns that the **Match** enum defines or provide a regular expression.
* *Options* – Optional.  A text string combination of **MatchOptions** enum values.  By default, **MatchOptions.Contains** is used.

## IsMatch Examples
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

|                                                            Formula                                                            |                                                                Description                                                                |  Result   |
|-------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| **IsMatch( "123-45-7890", Digit & Digit & Digit & Hyphen & Digit & Digit & Hyphen & Digit & Digit & Digit & Digit & Digit )** |                                              Matches a United States Social Security Number                                               | **true**  |
|                                           **IsMatch( "joan@contoso.com", Email )**                                            |                                                         Matches an email address                                                          | **true**  |
|                              **IsMatch( "123.456", MultipleDigits & Period & OptionalDigits )**                               |                                   Matches a sequence of digits, a period, and then zero or more digits.                                   | **true**  |
|                                **IsMatch( "123", MultipleDigits & Period & OptionalDigits )**                                 | Matches a sequence of digits, a period, and then zero or more digits. A period doesn't appear in the text, so this pattern isn't matched. | **false** |

### Regular expressions

|                                                                              Formula                                                                              |                                                                                                                                  Description                                                                                                                                   |  Result   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
|                                                                    **IsMatch( "986", "\d+" )**                                                                    |                                                                                                                    Matches a an integer greater than zero.                                                                                                                     | **true**  |
|                                                               **IsMatch( "1.02", "\d+(\.\d\d)?" )**                                                               |                                        Matches a positive currency amount. If the input contains a decimal point, the input must also contain 2 numeric characters after the decimal point. For example, 3.00 is valid, but 3.1 isn't.                                         | **true**  |
|                                                            **IsMatch( "-4.95", "(-)?\d+(\.\d\d)?" )**                                                             |                                                        Matches a positive or negative currency amount. If the input contains a decimal point, the input must also contain 2 numeric characters after the decimal point.                                                        | **true**  |
|                                                         **IsMatch( "111-11-1111", "\d{3}-\d{2}-\d{4}" )**                                                         | Matches a United States Social Security number.  Validates the format, type, and length of the supplied input field. The string to match must consist of 3 numeric characters followed by a dash, then 2 numeric characters followed by a dash, and then 4 numeric characters. | **true**  |
|                                                         **IsMatch( "111-111-111", "\d{3}-\d{2}-\d{4}" )**                                                         |                                                                                               Same as the previous example, but one of the hyphens is out of place in the input.                                                                                               | **false** |
|                                         **IsMatch( "weakpassword", "(?!^[0-9]\*$)(?!^[a-zA-Z]\*$)([a-zA-Z0-9]{8,10})" )**                                         |                                        Validates a strong password, which must contain 8, 9, or 10 characters, in addition to at least one digit and at least one alphabetic character. The string must not contain special characters.                                        | **false** |
| **IsMatch( "<http://microsoft.com>", "(ht&#124;f)tp(s?)\:\/\/\[0-9a-zA-Z\]([-.\w]\*[0-9a-zA-Z])\*(:(0-9)\*)\*(\/?)([a-zA-Z0-9\-\.\?\,\'\/\\\+&amp;%\$#_]\*)?" )** |                                                                                                                     Validates an http, https, or ftp URL.                                                                                                                      | **true**  |

## Match and MatchAll Examples

| Formula | Description | Result |
|--------|------------|-----------|
| **Match( "Bob Jones &lt;bob.jones@contoso.com&gt;", "&lt;(?&lt;email&gt;" & Match.Email & ")&gt;"** | Extracts only the email portion of the contact information.  | {<br>email: "bob.jones@contoso.com",<br>FullMatch: "&lt;bob.jones@contoso.com&gt;",<br>SubMatches: [ "bob.jones@contoso.com" ],<br>StartMatch: 11<br>}  
| **Match( "Bob Jones &lt;InvalidEmailAddress&gt;", "&lt;(?&lt;email&gt;" & Match.Email & ")&gt;"** | Extracts only the email portion of the contact information.  As no legal address is found (there is no @ sign) the function returns *blank* | *blank* |  
| **Match( "PT2H1M39S", "PT(?&lt;hours&gt;\d+H)?<br>(?&lt;minutes&gt;\d+M)?<br>(?&lt;seconds&gt;\d+S)?" )** | Extracts the hours, minutes, and seconds from an ISO 8601 duration value. Note that although we have extracted numbers they are still in a text string, use the [**Value**](function-value.md) function to convert to a number before performing mathematical operations.  | {<br> hours: "2",<br>minutes: "1",<br>seconds: "39",<br>FullMatch: "PT2H1M39S",<br>SubMatches:&nbsp;[&nbsp;"2",&nbsp;"1",&nbsp;"39"&nbsp;],<br>StartMatch: 1<br>} |

For the following examples, insert a button control on the screen with **OnSelect** property equal to **Set( pangram, "The quick brown fox jumps over the lazy dog." )** and press the button.

| Formula | Description | Result |
|---------|-------------|--------|
| **Match( pangram, "THE", IgnoreCase )** | Find all matches of "THE" in the text string **pangram**.  There are two possible matches, but only the first will be returned as we are using **Match** and not **MatchAll**. The SubMatches column is empty since there were no sub-matches defined.  | {<br>FullMatch: "The",<br>SubMatches: [],<br>StartMatch: 32<br>} |
| **MatchAll( pangram, "the" )** | Find all matches of "the" in the text string **pangram**.  As the test is case sensitive, only the second instance of "the" is found. The SubMatches column is empty since there were no sub-matches defined.  | [ { FullMatch: "the", SubMatches: [], StartMatch: 32 } ] |
| **MatchAll( pangram, "the", IgnoreCase )** | Find all matches of "the" in the text string **pangram**.  In this case the test is case insensitive resulting in both instances of the word being found. The SubMatches column is empty since there were no sub-matches defined.  | [ { Match: "The", SubMatches: [], StartMatch: 1 },<br>{ FullMatch: "the", SubMatches: [], StartMatch: 32 } ] |
| **MatchAll( pangram, "\b\wo\w\b" )** | Finds all three letter words with an "o" in the middle. Note that "brown" is excluded because it fails to match "\b" (word boundary) as it is not a three letter word.  | [ { Match: "fox", SubMatches: [], StartMatch: 17 },<br>{ Match: "dog", SubMatches: [], StartMatch: 41 } ] |
| **Match( pangram, "\b\wo\w\b\s\*(?<between>\w.+\w)\s\*\b\wo\w\b" )** | Matches all the characters between "fox" and "dog". | {<br>between: "jumps over the lazy",<br>FullMatch: "fox jumps over the lazy dog",<br>SubMatches: [ "jumps over the lazy" ],<br>StartMatch: 17<br> } |
