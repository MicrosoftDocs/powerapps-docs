<properties
	pageTitle="PowerApps: Text function"
	description="Reference information for the Text function in PowerApps, including syntax and examples"
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

# Text function in PowerApps #

Formats a number or date/time value for display as a string.

## Description ##

The **Text** function formats a number or date/time value based on either:

- A predefined date/time format, using the **DateTimeFormat** enumeration.  For dates and times, these are preferred as they automatically adjust to each user's language and locale.
- A custom format string, made up of placeholders that describe how to format the number or date/time value.  Placeholders include how many digits to show, if thousands separators should be used, and how to display the name of a month.  Placeholders supported are a subset of those available in Microsoft Excel.

See [working with dates and times](../show-text-dates-times.md) for more information. 

### Predefined date/time formats ###

| Predefined Format | Description |
|-------------------|-------------|
| **DateTimeFormat!LongDate** | Full year, month, day of the month, and day of the week.  No abbreviations are used for the month and day of the week names.  |
| **DateTimeFormat!LongDateTime** | Full year, month, day of the month, and day of the week, plus hour (12 hour clock), minutes, seconds, and AM/PM designation.  No abbreviations are used for the month and day of the week names.  |
| **DateTimeFormat!LongDateTime24** | Full year, month, day of the month, and day of the week, plus hour (24 hour clock), minutes, and seconds.  No abbreviations are used for the month and day of the week names.  |
| **DateTimeFormat!LongTime** | Hour (12 hour clock), minutes, seconds, and AM/PM designation.  Same as ShortTime. |
| **DateTimeFormat!LongTime24** | Hour (24 hour clock), minutes, seconds. Same as ShortTime24. |
| **DateTimeFormat!ShortDate** | Four digit year with two digit month and day of the month. |
| **DateTimeFormat!ShortDateTime** | Four digit year with two digit month and day of the month, plus hour (12 hour clock), minutes, seconds, and AM/PM designation. |
| **DateTimeFormat!ShortDateTime24** | Four digit year with two digit month and day of the month, plus hour (24 hour clock), minutes, and seconds. |
| **DateTimeFormat!ShortTime** | Hour (12 hour clock), minutes, seconds, and AM/PM designation.  Same as LongTime. |
| **DateTimeFormat!ShortTime24** | Hour (24 hour clock), minutes, seconds.  Same as LongTime24. |
| **DateTimeFormat!UTC**| The date/time value is converted to UTC based on the current user's time zone and formatted according to the ISO 8601 standard. |

### Number placeholders ###

| Placeholder | Description |
|-------------|-------------|
| **0** (*zero*) | Displays insignificant zeros if a number has fewer digits than there are zeros in the format. For example, if you the number to format is 8.9, and you want it to be displayed as "8.90", use the format "#.00". |
| **#** | Follows the same rules as the 0 (zero). However, **Text** does not return extra zeros when the number has fewer digits on either side of the decimal than there are # symbols in the format. For example, if the custom format is "#.##", and the number to format is 8.9, the number "8.9" is displayed. |
| **.** (*period*) | Displays the decimal point in a number. |
| **,** (*comma*) | Displays the thousands separator in a number. **Text** separates thousands by commas if the format contains a comma that is enclosed by number signs (#) or by zeros. 

If a number has more digits to the right of the decimal point than there are placeholders in the format, the number rounds to as many decimal places as there are placeholders. If there are more digits to the left of the decimal point than there are placeholders, the extra digits are displayed. If the format contains only number signs (#) to the left of the decimal point, numbers less than 1 begin with a decimal point; for example, .47.

### Date and time placeholders ###

| Placeholder | Description |
|-------------|-------------|
| **m**| Displays the month as a number without a leading zero. |
| **mm** | Displays the month as a number with a leading zero when appropriate. |
| **mmm** | Displays the month as an abbreviation ("Jan" to "Dec"). |
| **mmmm** | Displays the month as a full name ("January" to "December"). |
| **d** | Displays the day as a number without a leading zero. |
| **dd** | Displays the day as a number with a leading zero when appropriate. |
| **ddd** | Displays the day as an abbreviation ("Sun" to "Sat"). |
| **dddd** | Displays the day as a full name ("Sunday" to "Saturday"). |
| **yy** | Displays the year as a two-digit number. |
| **yyyy** | Displays the year as a four-digit number. |
| **h** | Displays the hour as a number without a leading zero. |
| **hh** | Displays the hour as a number with a leading zero when appropriate. If the format contains AM or PM, the hour is shown based on the 12-hour clock. Otherwise, the hour is shown based on the 24-hour clock. | 
| **m** | Displays the minute as a number without a leading zero.  Note: The m or the mm code must appear immediately after the h or hh code or immediately before the ss code; otherwise, **Text** returns the month instead of minutes. |
| **mm** | Displays the minute as a number with a leading zero when appropriate. Note: The m or the mm code must appear immediately after the h or hh code or immediately before the ss code; otherwise, Excel displays the month instead of minutes. |
| **s** | Displays the second as a number without a leading zero. |
| **ss** | Displays the second as a number with a leading zero when appropriate.  |
| **f** | Displays the fractions of seconds. |
| **AM/PM**, **am/pm**, **A/P**, **a/p** | Displays the hour based on a 12-hour clock. **Text** returns "AM", "am", "A", or "a" for times from midnight until noon and "PM", "pm", "P", or "p" for times from noon until midnight |

### Literal placeholders ###

You can include any of these characters in your format string.  They will appear in the result of **Text** as is.  Additional characters are reserved for future placeholders and should not be used.

| Character | Description |
|-----------|-------------|
| Any currency symbol | Dollar sign, Cents sign, Euro sign, etc. |
| **+** | Plus sign |
| **(** | Left parenthesis |
| **:** | Colon |
| **^** | Circumflex accent (caret) |
| **'** | Apostrophe |
| **{** | Left curly bracket | 
| **<** | Less-than sign |
| **=** | Equal sign |
| **-** | Minus sign |
| **/** | Slash mark |
| **)** | Right parenthesis |
| **&** | Ampersand |
| **~** | Tilde |
| **}** | Right curly bracket |
| **>** | Greater-than sign |
| &nbsp; | Space character |

## Syntax ##

**Text**( *Number*, *DateTimeFormatEnum* )

- *Number* - Required. The number or date/time value to format.
- *DateTimeFormat* - Required.  A member of the **DateTimeFormat** enumeration.

**Text**( *Number*, *FormatString* )

- *Number* - Required. The number or date/time value to format.
- *FormatString* - Required.  A member of the **DateTimeFormat** enumeration.


## Examples ##

### Number ###

| Formula |  Description | Result |
|-------------|-------------|-------------|
| **Text( 1234.59, "####.#" )** | Formats the number with one decimal place. | "1234.6" |
| **Text( 8.9, "#.000" )** | Pads the decimal portion of the number with trailing zeros, if needed.  | "8.900" |
| **Text( 0.631, "0.#" )** | Pads the whole portion of the number with leading zeros, if needed. | "0.6" | 
| **Text( 12, "#.0#" )**<br>**Text(&nbsp;1234.568,&nbsp;"#.0#"&nbsp;)** | Pads the decimal portion of the number with zeros for one decimal place, and includes a second decimal place if supplied. | "12.0"<br>"1234.57"  |
| **Text( 12000, "$ #,###" )**<br>**Text(&nbsp;1200000,&nbsp;"$&nbsp;#,###"&nbsp;)** | Places a thousands separator every three digits, and includes a currency symbol.  | "$&nbsp;12,000"<br>"$&nbsp;1,200,000" |

### Date/Time ###

- At 2:37:47 PM on Monday, November 23, 2015
- United States Pacific Time Zone (UTC+8)
- English US Locale

| Formula |  Description | Result |
|-------------|-------------|-------------|
| **Text( Now(), DateTimeFormat!LongDate )** | Formats as a long date string, in the language and locale of the current user. | "Monday, November 23, 2015" |
| **Text( Now(), DateTimeFormat!LongDateTime )** | Formats as a long date and time string, in the language and locale of the current user, using a 12 hour clock.  | "Monday, November 23, 2015 2:37:47 PM" |
| **Text( Now(), DateTimeFormat!LongTime24 )** |  Formats as a long time string, using a 24 hour clock. | "14:37:47" | 
| **Text( Now(), DateTimeFormat!ShortDate )** | Formats as a short date string, in the language and locale of the current user. | "11/23/2015" |
| **Text( Now(), "d-mmm-yy" )** | Formats using placeholder characters: <ul><li>"d" for a single or double digit day of the month<li>"-" as a literal character copied to the result<li>"mmm" for a three letter month abbreviation<li>-" as another literal character copied to the result<li>"yy" for a two digit year abbreviation</ul> | "23-Nov-15" |



