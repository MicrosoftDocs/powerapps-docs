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

Use **Match** to extract the first text string that matches a pattern and **MatchAll** to extract all text strings that match.  Sub-matches can also be extracted to parse complex strings.   

**Match** returns a record of information for the first match found and **MatchAll** returns a table of records for every match found.  This record contains:

| Column | Type | Description |
|----|----|----|
| *named sub&#8209;match(es)* | Text | Each named sub-match will have its own column. Named sub-matches are created with **(?&lt;*name*&gt;**...**)** in the regular expression.  If a named sub-match has the same name as one of the above columns then the sub-match will take precedence and a warning will be generated; rename the sub-match to avoid this warning. |
| **FullMatch** | Text | All of the text string that was matched. |
| **StartMatch** | Number | The starting position of the match within the input text string.  The first character of the string returns 1. | 
| **SubMatches** | Single column table of Text (column **Value**) | The table of named and unnamed sub-matches in the order they appear in the regular expression. Generally, named sub-matches are easier to work with and are encouraged.  Use the [**ForAll**](function-forall.md) function or **[Last](function-first-last.md)( [FirstN](function-first-last.md)( **...** ) )** functions to work with an individual sub-match.  If there are no sub-matches defined in the regular expression this table will still be present but will be empty. |

These functions support [**MatchOptions**](match-options).  By default: 
- These functions perform a case-sensitive match.  Use **IgnoreCase** to perform case-insensitive matches.    
- **IsMatch** will match the entire text string (**Complete** MatchOption) while **Match** and **MatchAll** will search for a match anywhere in the text string (**Contains** MatchOption). 

**IsMatch** returns *true* if the text string matches the pattern or *false* if it doesn't.  **Match** returns *blank* if no match is found that can be tested with the [**IsBlank**](function-isblank-isempty.md) function.  **MatchAll** returns an empty table if no match is found that can be tested with the [**IsEmpty**](function-isblank-isempty.md) function.

If you are using **MatchAll** to split a text string, consider using the **[Split](function-split.md)** function which is simpler to use and faster.

## Patterns
The key to using these functions is in describing the pattern to match. You describe the pattern in a text string as a combination of:

* Ordinary characters, such as  **"abc"** or **"123"**.
* Predefined patterns, such as **Letter**, **MultipleDigits**, or **Email**. (The **Match** enum defines these patterns.)
* Regular expressions codes, such as **"\d+\s+\d+"** or **"[a-z]+"**.

Combine these elements by using the [string concatenation operator **&**](operators.md). For example, **"abc" & Digit & "\s+"** is a valid pattern that matches the characters "a", "b", and "c", followed by a digit from 0 to 9, followed by at least one whitespace character.

### Ordinary characters
The simplest pattern is a sequence of ordinary characters to be matched exactly.

For example, when used with the **IsMatch** function, the string "Hello" matches the pattern **"Hello"** exactly. No more and no less. The string "hello!" doesn't match the pattern because of the exclamation point on the end and the case is wrong for the letter "h". (See [MatchOptions](#match-options) for ways to modify this behavior.)

In the pattern language, certain characters are reserved for special purposes. To use these characters, either prefix the character with a **\\** (backslash) to indicate that the character should be taken literally or use one of the predefined patterns described below. This table lists the special characters:

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
| **Any** |Matches any character. |<code>.</code> |
| **Comma** |Matches a comma. |<code>,</code> |
| **Digit** |Matches a single digit ("0" through "9"). |<code>\d</code> |
| **Email** |Matches an email address that contains an "at" symbol ("\@") and a domain name that contains a dot (".") |<code>.+\@.+\\.[^\\.]{2,}</code> |
| **Hyphen** |Matches a hyphen. |<code>\-</code> |
| **LeftParen** |Matches a left parenthesis "(". |<code>\(</code> |
| **Letter** |Matches a letter. |<code>\p{L}</code> |
| **MultipleDigits** |Matches one or more digitis. |<code>\d+</code> |
| **MultipleLetters** |Matches one or more letters. |<code>\p{L}+</code> |
| **MultipleNonSpaces** |Matches one or more characters that don't add whitespace (space, tab, newline). |<code>\S+</code> |
| **MultipleSpaces** |Matches one or more characters that add whitespace (space, tab, newline). |<code>\s+</code> |
| **NonSpace** |Matches a single character that doesn't add whitespace. |<code>\S</code> |
| **OptionalDigits** |Matches zero, one, or more digits. |<code>\d*</code> |
| **OptionalLetters** |Matches zero, one, or more letters. |<code>\p{L}*</code> |
| **OptionalNonSpaces** |Matches zero, one, or more characters that don't add whitespace. |<code>\S*</code> |
| **OptionalSpaces** |Matches zero, one, or more characters that add whitespace. |<code>\s*</code> |
| **Period** |Matches a period or dot ("."). |<code>\.</code> |
| **RightParen** |Matches a right parenthesis ")". |<code>\)</code> |
| **Space** |Matches a character that adds whitespace. |<code>\s</code> |

For example, the pattern **"A" & MultipleDigits** will match the letter "A" followed by one or more digits.  

### Regular expressions
The pattern used by these functions is a [*regular expression*](https://en.wikipedia.org/wiki/Regular_expression). The ordinary characters and predefined patterns that are described above help build regular expressions.  

Regular expressions are very powerful, available in many programming languages, and used for a wide variety of purposes. This article can't describe all aspects of regular expressions, but a wealth of information and tutorials are published on the web to aid you.  

Regular expressions come in different dialects and PowerApps uses a variant of the JavaScript dialect. See [regular expression syntax](http://msdn.microsoft.com/library/1400241x.aspx) for an introduction to the syntax.  One key addition is named sub-matches (sometimes called named capture groups) expressed with **(?&lt;*name*&gt;** ... **)**. 

In the **Match** enum table above, each enum expands into a regular expression, and the text string in the "Regular Expression" column defines that expression.

## Match options
You can modify the behavior of these functions by specifying one or more options, which you can combine by using the string concatenation operator (**&amp;**).  

| MatchOptions Enum | Description | Impact on regular expression |
| --- | --- | --- |
| **BeginsWith** |The pattern must match from the beginning of the text. |Adds a **^** to the start of the regular expression. |
| **Complete** |Default for **IsMatch**.  The pattern must match the entire text, from beginning to end. |Adds a **^** to the start and **$** to the end of the regular expression. |
| **Contains** |Default for **Match** and **IsMatch**.  The pattern must appear somewhere in the text but doesn't need to begin or end it. |Doesn't modify the regular expression. |
| **EndsWith** |The pattern must match the end of the text. |Adds a **$** to the end of the regular expression. |
| **IgnoreCase** |Treats the matching of letters in a case-insensitive manner. By default, matching is case sensitive. |Doesn't modify the regular expression. This is the equivalent of the standard regular expression "i" modifier.  |
| **Multiline** |Matches across multiple lines. |Doesn't modify the regular expression. This is the equivalent of the standard regular expression "m" modifier. |

Using **MatchAll** is equivalent to using the standard regular expression "g" modifier.

## Syntax
**IsMatch**( *Text*, *Pattern* [, *Options* ] )

* *Text* – Required.  The text string to test.
* *Pattern* – Required.  The pattern to test, as a text string.  Concatenate predefined patterns that the **Match** enum defines or provide a regular expression.  *Pattern* must be a constant formula without variable, data source, or any other dynamic reference that changes as the app executes.
* *Options* – Optional.  A text string combination of **MatchOptions** enum values.  By default, **MatchOptions.Complete** is used.

**Match**( *Text*, *Pattern* [, *Options* ] )

* *Text* – Required.  The text string to test.
* *Pattern* – Required.  The pattern to test, as a text string.  Concatenate predefined patterns that the **Match** enum defines or provide a regular expression.  *Pattern* must be a constant formula without variable, data source, or any other dynamic reference that changes as the app executes.
* *Options* – Optional.  A text string combination of **MatchOptions** enum values.  By default, **MatchOptions.Contains** is used.

**MatchAll**( *Text*, *Pattern* [, *Options* ] )

* *Text* – Required.  The text string to test.
* *Pattern* – Required.  The pattern to test, as a text string.  Concatenate predefined patterns that the **Match** enum defines or provide a regular expression.  *Pattern* must be a constant formula without variable, data source, or any other dynamic reference that changes as the app executes.
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
|                                                                    <code>IsMatch( "986", "\d+" )</code>                                                                    |                                                                                                                    Matches a an integer greater than zero.                                                                                                                     | **true**  |
|                                                               <code>IsMatch( "1.02", "\d+(\.\d\d)?" )</code>                                                              |                                        Matches a positive currency amount. If the input contains a decimal point, the input must also contain 2 numeric characters after the decimal point. For example, 3.00 is valid, but 3.1 isn't.                                         | **true**  |
|                                                            <code>IsMatch( "-4.95",<br>"(-)?\d+(\.\d\d)?" )</code>                                                             |                                                        Matches a positive or negative currency amount. If the input contains a decimal point, the input must also contain 2 numeric characters after the decimal point.                                                        | **true**  |
|                                                         <code>IsMatch( "111-11-1111",<br>"\d{3}-\d{2}-\d{4}" )</code>                                                        | Matches a United States Social Security number.  Validates the format, type, and length of the supplied input field. The string to match must consist of 3 numeric characters followed by a dash, then 2 numeric characters followed by a dash, and then 4 numeric characters. | **true**  |
|                                                         <code>IsMatch( "111-111-111",<br>"\d{3}-\d{2}-\d{4}" )</code>                                                         |                                                                                               Same as the previous example, but one of the hyphens is out of place in the input.                                                                                               | **false** |
|                                         <code>IsMatch( "aweakpassword",<br>"(?!^[0-9]\*$)(?!^[a-zA-Z]\*$)([a-zA-Z0-9]{8,10})" )</code>                                         |                                        Validates a strong password, which must contain 8, 9, or 10 characters, in addition to at least one digit and at least one alphabetic character. The string must not contain special characters.                                        | **false** |
| <code>IsMatch( "<http://microsoft.com>", "(ht&#124;f)tp(s?)\:\/\/\[0-9a-zA-Z\]([-.\w]\*[0-9a-zA-Z])\*(:(0-9)\*)\*(\/?)([a-zA-Z0-9\-\.\?\,\'\/\\\+&amp;%\$#_]\*)?" )</code> |                                                                                                                     Validates an http, https, or ftp URL.                                                                                                                      | **true**  |

## Match and MatchAll Examples

| Formula | Description | Result |
|--------|------------|-----------|
| <code>Match( "Bob Jones &lt;bob.jones@contoso.com&gt;",<br>"&lt;(?&lt;email&gt;" & Match.Email & ")&gt;"</code> | Extracts only the email portion of the contact information.  | {<br>email:&nbsp;"bob.jones@contoso.com",<br>FullMatch:&nbsp;"&lt;bob.jones@contoso.com&gt;",<br>SubMatches:&nbsp;[&nbsp;"bob.jones@contoso.com"&nbsp;],<br>StartMatch: 11<br>}  
| <code>Match( "Bob Jones &lt;InvalidEmailAddress&gt;",<br>"&lt;(?&lt;email&gt;" & Match.Email & ")&gt;"</code> | Extracts only the email portion of the contact information.  As no legal address is found (there is no @ sign) the function returns *blank* | *blank* |  
| <code>Match( Language(),<br>"(?&lt;language&gt;\w{2})<br>(?:-(?&lt;script&gt;\w{4}))?<br>(?:-(?&lt;region&gt;\w{2}))?" )</code> | Extracts the language, script, and region portions of the language tag returned by the **[Language](function-language.md)** function.  Results shown here are when run in the United States, see the [**Language** function documentation](function-language.md) for more examples.  The **(?:** operator is used to group characters without creating an additional sub-match. | {<br>language: "en",<br>script: "", <br>region: "US",<br>FullMatch: "en-US", <br>SubMatches: [ "en", "", "US" ], <br>StartMatch: 1<br>} 
| <code>Match( "PT2H1M39S",<br>"PT(?:(?&lt;hours&gt;\d+)H)?<br>(?:(?&lt;minutes&gt;\d+)M)?<br>(?:(?&lt;seconds&gt;\d+)S)?" )</code> | Extracts the hours, minutes, and seconds from an ISO 8601 duration value. Note that although we have extracted numbers they are still in a text string, use the [**Value**](function-value.md) function to convert to a number before performing mathematical operations.  | {<br> hours: "2",<br>minutes: "1",<br>seconds: "39",<br>FullMatch: "PT2H1M39S",<br>SubMatches:&nbsp;[&nbsp;"2",&nbsp;"1",&nbsp;"39"&nbsp;],<br>StartMatch: 1<br>} |

Let's drill into that last example.  If we wanted to convert this string to a Date/Time value using the **[Time](function-date-time.md)** function we need to pass in the named sub-matches individually.  To do this we can use the **[ForAll](function-forall.md)** function operating on the first record returned from **MatchAll**:

```
First( 
	ForAll( 
		MatchAll( "PT2H1M39S", "PT(?:(?<hours>\d+)H)?(?:(?<minutes>\d+)M)?(?:(?<seconds>\d+)S)?" ), 
		Time( Value( hours ), Value( minutes ), Value( seconds ) )
	)
).Value
```

For the following examples, insert a [Button](../controls/control-button.md) control on the screen and set the **OnSelect** property to:

- **Set( pangram, "The quick brown fox jumps over the lazy dog." )** 
 
and press the button.

| Formula | Description | Result |
|---------|-------------|--------|
| <code>Match( pangram, "THE", IgnoreCase )</code> | Find all matches of "THE" in the text string **pangram**.  There are two possible matches, but only the first will be returned as we are using **Match** and not **MatchAll**. The SubMatches column is empty since there were no sub-matches defined.  | {<br>FullMatch: "The",<br>SubMatches: [&nbsp;],<br>StartMatch: 32<br>} |
| <code>MatchAll( pangram, "the" )</code> | Find all matches of "the" in the text string **pangram**.  As the test is case sensitive, only the second instance of "the" is found. The SubMatches column is empty since there were no sub-matches defined.  | ![](media/function-ismatch/pangram-the-one.png) |
| <code>MatchAll( pangram, "the", IgnoreCase )</code> | Find all matches of "the" in the text string **pangram**.  In this case the test is case insensitive resulting in both instances of the word being found. The SubMatches column is empty since there were no sub-matches defined.  | ![](media/function-ismatch/pangram-the-two.png) |
| <code>MatchAll( pangram, "\b\wo\w\b" )</code> | Finds all three letter words with an "o" in the middle. Note that "brown" is excluded because it fails to match "\b" (word boundary) as it is not a three letter word.  | ![](media/function-ismatch/pangram-fox-dog.png) |
| <code>Match(&nbsp;pangram,<br>"\b\wo\w\b\s\*<br>(?&lt;between&gt;w.+\w)<br>\s\*\b\wo\w\b" )</code> | Matches all the characters between "fox" and "dog". | {<br>between:&nbsp;"jumps&nbsp;over&nbsp;the&nbsp;lazy",<br>FullMatch:&nbsp;"fox&nbsp;jumps&nbsp;over&nbsp;the&nbsp;lazy&nbsp;dog",<br>SubMatches: [ "jumps over the lazy" ],<br>StartMatch: 17<br> } |

To see the results of **MatchAll** in a gallery:

1. Create a new screen and insert a **[Gallery](../controls/control-gallery.md)** control.

2. Set the Gallery's **Items** property to **MatchAll( pangram, "\w+" )**.  You could also use **MatchAll( pangram, MultipleLetters )**.

	![](media/function-ismatch/pangram-gallery1.png)

	**TODO: image needs update**

3. Insert a Label control.

4. Set the Label control's **Text** property to **ThisItem.FullMatch**.
 
5. Your gallery will be filled with each word in our example text.

	![](media/function-ismatch/pangram-gallery2.png)

	**TODO: image needs update**
