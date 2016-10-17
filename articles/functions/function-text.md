<properties
	pageTitle="Text function | Microsoft PowerApps"
	description="Reference information, including syntax and examples, for the Text function in PowerApps"
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
   ms.date="10/15/2016"
   ms.author="gregli"/>

# Text function in PowerApps #

Formats a number or a date/time value for display as a string of text.

## Description ##

The **Text** function formats a number or a date/time value based on one of these types of arguments:

- A predefined date/time format, which you specify by using the **DateTimeFormat** enumeration.  For dates and times, this approach is preferred as it automatically adjusts to each user's language and locale.
- A custom format string, which comprises placeholders that describe how to format the number or the date/time value. Placeholders define how many digits to show, whether thousands separators should be used, and how to display the name of a month. PowerApps supports a subset of the placeholders that Microsoft Excel does.

See [working with dates and times](../show-text-dates-times.md) for more information.

### Predefined date/time formats ###

| Predefined Format | Description |
|-------------------|-------------|
| **DateTimeFormat.LongDate** | Full year, month, day of the month, and day of the week. The names of the month and the day of the week aren't abbreviated.  |
| **DateTimeFormat.LongDateTime** | Full year, month, day of the month, and day of the week, plus hour (12-hour clock), minutes, seconds, and AM/PM designation. The names of the month and the day of the week aren't abbreviated.  |
| **DateTimeFormat.LongDateTime24** | Full year, month, day of the month, and day of the week, plus hour (24-hour clock), minutes, and seconds. The names of the month and the day of the week aren't abbreviated.  |
| **DateTimeFormat.LongTime** | Hour (12-hour clock), minutes, seconds, and AM/PM designation. Same as ShortTime. |
| **DateTimeFormat.LongTime24** | Hour (24-hour clock), minutes, seconds. Same as ShortTime24. |
| **DateTimeFormat.ShortDate** | Four-digit year with two-digit month and day of the month. |
| **DateTimeFormat.ShortDateTime** | Four-digit year with two-digit month and day of the month, plus hour (12-hour clock), minutes, seconds, and AM/PM designation. |
| **DateTimeFormat.ShortDateTime24** | Four-digit year with two-digit month and day of the month, plus hour (24-hour clock), minutes, and seconds. |
| **DateTimeFormat.ShortTime** | Hour (12-hour clock), minutes, seconds, and AM/PM designation.  Same as LongTime. |
| **DateTimeFormat.ShortTime24** | Hour (24-hour clock), minutes, and seconds.  Same as LongTime24. |
| **DateTimeFormat.UTC**| The date/time value is converted to UTC based on the current user's time zone and formatted according to the ISO 8601 standard. |

### Number placeholders ###

| Placeholder | Description |
|-------------|-------------|
| **0** (*zero*) | Displays insignificant zeros if a number has fewer digits than there are zeros in the format. For example, use the format **#.00** if you want to display **8.9** as **8.90**. |
| **#** | Follows the same rules as the **0** (zero). However, **Text** doesn't return extra zeros when the number has fewer digits on either side of the decimal than there are # symbols in the format. For example, **8.9** is displayed if the custom format is **#.##** and the number to format is **8.9**. |
| **.** (*period*) | Displays the decimal point in a number.  Depends on the locale, see [format string locale](#format-string-locale) for more details. |
| **,** (*comma*) | Displays the thousands separator in a number. **Text** separates thousands by commas if the format contains a comma that's enclosed by number signs (**#**) or by zeros.  Depends on the locale, see [format string locale](#format-string-locale) for more details. |

If a number has more digits to the right of the decimal point than there are placeholders in the format, the number rounds to as many decimal places as there are placeholders. If there are more digits to the left of the decimal point than there are placeholders, the extra digits are displayed. If the format contains only number signs (#) to the left of the decimal point, numbers less than 1 start with a decimal point (for example, **.47**).

### Date and time placeholders ###

| Placeholder | Description |
|-------------|-------------|
| **m**| Displays the month as a number without a leading zero. |
| **mm** | Displays the month as a number with a leading zero when appropriate. |
| **mmm** | Displays the month as an abbreviation (**Jan** to **Dec**). |
| **mmmm** | Displays the month as a full name (**January** to **December**). |
| **d** | Displays the day as a number without a leading zero. |
| **dd** | Displays the day as a number with a leading zero when appropriate. |
| **ddd** | Displays the day as an abbreviation (**Sun** to **Sat**). |
| **dddd** | Displays the day as a full name (**Sunday** to **Saturday**). |
| **yy** | Displays the year as a two-digit number. |
| **yyyy** | Displays the year as a four-digit number. |
| **h** | Displays the hour as a number without a leading zero. |
| **hh** | Displays the hour as a number with a leading zero when appropriate. If the format contains **AM** or **PM**, the hour is shown based on the 12-hour clock. Otherwise, the hour is shown based on the 24-hour clock. |
| **m** | Displays the minute as a number without a leading zero.  Note: The **m** or the **mm** code must appear immediately after the **h** or **hh** code or immediately before the **ss** code; otherwise, **Text** returns the month instead of minutes. |
| **mm** | Displays the minute as a number with a leading zero when appropriate. Note: The **m** or the **mm** placeholder must appear immediately after the **h** or **hh** placeholder or immediately before the **ss** placeholder. Otherwise, **Text** returns the month  instead of minutes. |
| **s** | Displays the second as a number without a leading zero. |
| **ss** | Displays the second as a number with a leading zero when appropriate.  |
| **f** | Displays the fractions of seconds. |
| **AM/PM**, **am/pm**, **A/P**, **a/p** | Displays the hour based on a 12-hour clock. **Text** returns "AM", "am", "A", or "a" for times from midnight until noon and "PM", "pm", "P", or "p" for times from noon until midnight |

### Literal placeholders ###

You can include any of these characters in your format string.  They will appear in the result of **Text** as is. Additional characters are reserved for future placeholders, so you shouldn't use them.

| Character | Description |
|-----------|-------------|
| Any currency symbol | Dollar sign, cents sign, euro sign, etc. |
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

### Format string locale ###

How the custom format string itself is interpreted can be dependent on the locale.  Did you intend for "." to be interpreted as a decimal separator or a thousands separator?  

To specify the locale of the custom format string, use:

| Format string locale | Description |
|----------------------|-------------|
| **[$-*xx*]** | The language is specified by the two characters ***xx***.  For example, ***xx*** is **en** for English resulting in **"[$-en]"**, **sp** for Spanish resulting in **"[$$-sp]"**, etc. |
| **[$-*xx*-*YY*]** | The language is specified by the two characters ***xx***, and the region is also specified with the two characters ***YY***.  For example, ***xx*** is "en" for English and ***YY*** is "GB" for Great Britain, resulting in **[$-en-GB]**. |

To see the list of supported locales, type **Text( 1234, "", ** in the formula bar or advanced view and scroll through the list of locales suggested for the third argument.     

The locale specifier can appear anywhere in the string, but may only appear once.

If not provided, the authoring tool may insert this specifier for you automatically.  If your app will be used in the same locale as where it was authored, this specifier will be correct.  This only needs to be adjusted if your app will be used across different locales.  **[$-en-US]** is assumed if this specifier is not present when your app is run. 

### Output locale ###

Independent of how the format string is interpreted, there is the question of which locale should be used for the output of **Text**.  Should month names be returned in Spanish or German?

By default, **Text** uses the locale of the user running the app.  You can determine which locale is being used with the **Language** function.  You can override this default by supplying a locale designation for the optional third argument to **Text**.

## Syntax ##

**Text**( *Number*, *DateTimeFormatEnum* [, *OutputLocale* ] )

- *Number* - Required. The number or the date/time value to format.
- *DateTimeFormat* - Required.  A member of the **DateTimeFormat** enumeration.
- *OutputLocale* - Optional.  The locale to use for the output text.  By default, this is the locale of the user.

**Text**( *Number*, *FormatString* [, *OutputLocale* ] )

- *Number* - Required. The number or the date/time value to format.
- *FormatString* - Required. One or more placeholders enclosed in double quotation marks.
- *OutputLocale* - Optional.  The locale to use for the output text.  By default, this is the locale of the user.

## Examples ##

The user running these formulas is located in the United States, with **Language** returning **"en-US"**.

### Number ###

- English US Locale ("en-US")

| Formula |  Description | Result |
|-------------|-------------|-------------|
| **Text( 1234.59, "####.#" )** | Formats the number with one decimal place. | "1234.6" |
| **Text( 8.9, "#.000" )** | Pads the decimal portion of the number with trailing zeros, if needed.  | "8.900" |
| **Text( 0.631, "0.#" )** | Pads the whole portion of the number with leading zeros, if needed. | "0.6" |
| **Text( 12, "#.0#" )**<br>**Text(&nbsp;1234.568,&nbsp;"#.0#"&nbsp;)** | Pads the decimal portion of the number with zeros for one decimal place, and includes a second decimal place if supplied. | "12.0"<br>"1234.57"  |
| **Text( 12000, "$ #,###" )**<br>**Text(&nbsp;1200000,&nbsp;"$&nbsp;#,###"&nbsp;)** | Places a thousands separator every three digits, and includes a currency symbol.  | "$&nbsp;12,000"<br>"$&nbsp;1,200,000" |


### Date/Time ###

- At **2:37:47 PM** on **Monday, November 23, 2015**
- United States Pacific Time Zone (UTC+8)
- English US Locale ("en-US")

| Formula |  Description | Result |
|-------------|-------------|-------------|
| **Text( Now(), DateTimeFormat.LongDate )** | Formats as a long date string, in the language and locale of the current user. | "Monday, November 23, 2015" |
| **Text( Now(), DateTimeFormat.LongDateTime )** | Formats as a long date and time string, in the language and locale of the current user, using a 12-hour clock.  | "Monday, November 23, 2015 2:37:47 PM" |
| **Text( Now(), DateTimeFormat.LongTime24 )** |  Formats as a long time string, using a 24-hour clock. | "14:37:47" |
| **Text( Now(), DateTimeFormat.ShortDate )** | Formats as a short date string, in the language and locale of the current user. | "11/23/2015" |
| **Text( Now(), "d-mmm-yy" )** | Formats using placeholder characters: <ul><li>**d** for a single-digit or double-digit day of the month<li>**-** as a literal character copied to the result<li>**mmm** for a three-letter abbreviation of the month<li>**-** as another literal character copied to the result<li>**yy** for a two-digit abbreviation of the year</ul> | "23-Nov-15" |

### International ###

| Formula |  Description | Result |
|-------------|-------------|-------------|
| **Text( 1234567.89, "[$-en-US]#,###" )** | Interprets **,** as a grouping separator, placed every three characters. As no decimals are to be displayed, the value is rounded up to the next higher whole number. | "1,234,568" |
| **Text( 1234567.89, "[$-fr-FR]#,###" )** | Interprets **,** as a decimal separator.  Since the **[$-fr-FR]** only determines how the format string is interpreted, the output locale remains "en-US" and a **.** (period) is used as the output decimal separator. | "1234567.89" |
| **Text( 1234567.89, "[$-fr-FR]#,###", "fr-FR" )** | Interprets **,** as a decimal separator.  The output locale has been set to "fr-FR", which will result in **,** (comma) being used as the decimal separator.  | "1234567,89" |
