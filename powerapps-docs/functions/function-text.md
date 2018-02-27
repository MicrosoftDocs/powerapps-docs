---
title: Text function | Microsoft Docs
description: Reference information, including syntax and examples, for the Text function in PowerApps
services: ''
suite: powerapps
documentationcenter: na
author: gregli-msft
manager: anneta
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 10/25/2016
ms.author: gregli

---
# Text function in PowerApps
Formats a number or a date/time value for display as a string of text.

## Description
The **Text** function formats a number or a date/time value based on one of these types of arguments:

* A predefined date/time format, which you specify by using the **DateTimeFormat** enumeration.  For dates and times, this approach is preferred as it automatically adjusts to each user's language and location.
* A custom format, a string of text that comprises placeholders that describe how to format the number or the date/time value. Placeholders define how many digits to show, whether grouping separators should be used, and how to display the name of a month. PowerApps supports a subset of the placeholders that Microsoft Excel does.

See [working with dates and times](../maker/show-text-dates-times.md) for more information.

### <a name="predefined-datetime-formats"></a> Predefined date/time formats
| Predefined Format | Description |
| --- | --- |
| **DateTimeFormat.LongDate** |Full year, month, day of the month, and day of the week. The names of the month and the day of the week aren't abbreviated. |
| **DateTimeFormat.LongDateTime** |Full year, month, day of the month, and day of the week, plus hour (12-hour clock), minutes, seconds, and AM/PM designation. The names of the month and the day of the week aren't abbreviated. |
| **DateTimeFormat.LongDateTime24** |Full year, month, day of the month, and day of the week, plus hour (24-hour clock), minutes, and seconds. The names of the month and the day of the week aren't abbreviated. |
| **DateTimeFormat.LongTime** |Hour (12-hour clock), minutes, seconds, and AM/PM designation. Same as ShortTime. |
| **DateTimeFormat.LongTime24** |Hour (24-hour clock), minutes, seconds. Same as ShortTime24. |
| **DateTimeFormat.ShortDate** |Four-digit year with two-digit month and day of the month. |
| **DateTimeFormat.ShortDateTime** |Four-digit year with two-digit month and day of the month, plus hour (12-hour clock), minutes, seconds, and AM/PM designation. |
| **DateTimeFormat.ShortDateTime24** |Four-digit year with two-digit month and day of the month, plus hour (24-hour clock), minutes, and seconds. |
| **DateTimeFormat.ShortTime** |Hour (12-hour clock), minutes, seconds, and AM/PM designation.  Same as LongTime. |
| **DateTimeFormat.ShortTime24** |Hour (24-hour clock), minutes, and seconds.  Same as LongTime24. |
| **DateTimeFormat.UTC** |The date/time value is converted to UTC based on the current user's time zone and formatted according to the ISO 8601 standard. |

### Number placeholders
| Placeholder | Description |
| --- | --- |
| **0** (*zero*) |Displays insignificant zeros if a number has fewer digits than there are zeros in the format. For example, use the format **#.00** if you want to display **8.9** as **8.90**. |
| **#** |Follows the same rules as the **0** (zero). However, **Text** doesn't return extra zeros when the number has fewer digits on either side of the decimal than there are # symbols in the format. For example, **8.9** is displayed if the custom format is **#.##** and the number to format is **8.9**. |
| **.** (*period*) |Displays the decimal point in a number.  Depends on the language of the custom format, see [global apps](#global-apps) for more details. |
| **,** (*comma*) |Displays the grouping separator in a number, often used for thousands. **Text** separates groups by commas if the format contains a comma that's enclosed by number signs (**#**) or by zeros.  Depends on the language of the custom format, see [global apps](#global-apps) for more details. |

If a number has more digits to the right of the decimal point than there are placeholders in the format, the number rounds to as many decimal places as there are placeholders. If there are more digits to the left of the decimal point than there are placeholders, the extra digits are displayed. If the format contains only number signs (#) to the left of the decimal point, numbers less than 1 start with a decimal point (for example, **.47**).

### Date and time placeholders
| Placeholder | Description |
| --- | --- |
| **m** |Displays the month as a number without a leading zero. |
| **mm** |Displays the month as a number with a leading zero when appropriate. |
| **mmm** |Displays the month as an abbreviation (**Jan** to **Dec**). |
| **mmmm** |Displays the month as a full name (**January** to **December**). |
| **d** |Displays the day as a number without a leading zero. |
| **dd** |Displays the day as a number with a leading zero when appropriate. |
| **ddd** |Displays the day as an abbreviation (**Sun** to **Sat**). |
| **dddd** |Displays the day as a full name (**Sunday** to **Saturday**). |
| **yy** |Displays the year as a two-digit number. |
| **yyyy** |Displays the year as a four-digit number. |
| **h** |Displays the hour as a number without a leading zero. |
| **hh** |Displays the hour as a number with a leading zero when appropriate. If the format contains **AM** or **PM**, the hour is shown based on the 12-hour clock. Otherwise, the hour is shown based on the 24-hour clock. |
| **m** |Displays the minute as a number without a leading zero.  > [!NOTE]
> The **m** or the **mm** code must appear immediately after the **h** or **hh** code or immediately before the **ss** code; otherwise, **Text** returns the month instead of minutes. |
| **mm** |Displays the minute as a number with a leading zero when appropriate. > [!NOTE]
> The **m** or the **mm** placeholder must appear immediately after the **h** or **hh** placeholder or immediately before the **ss** placeholder. Otherwise, **Text** returns the month  instead of minutes. |
| **s** |Displays the second as a number without a leading zero. |
| **ss** |Displays the second as a number with a leading zero when appropriate. |
| **f** |Displays the fractions of seconds. |
| **AM/PM**, **am/pm**, **A/P**, **a/p** |Displays the hour based on a 12-hour clock. **Text** returns "AM", "am", "A", or "a" for times from midnight until noon and "PM", "pm", "P", or "p" for times from noon until midnight |

### Literal placeholders
You can include any of these characters in your format string.  They will appear in the result of **Text** as is. Additional characters are reserved for future placeholders, so you shouldn't use them.

| Character | Description |
| --- | --- |
| Any currency symbol |Dollar sign, cents sign, euro sign, etc. |
| **+** |Plus sign |
| **(** |Left parenthesis |
| **:** |Colon |
| **^** |Circumflex accent (caret) |
| **'** |Apostrophe |
| **{** |Left curly bracket |
| **<** |Less-than sign |
| **=** |Equal sign |
| **-** |Minus sign |
| **/** |Slash mark |
| **)** |Right parenthesis |
| **&** |Ampersand |
| **~** |Tilde |
| **}** |Right curly bracket |
| **>** |Greater-than sign |
| &nbsp; |Space character |

## Global apps
The **Text** function is globally aware.  For a wide array of languages, it knows how to properly write out dates, times, currencies, and numbers.  To do its job, it needs two pieces of information:

* **The language of the custom format:** For authors, how should a custom format be interpreted?  The separator characters (**.** and **,**) have different meanings in different languages.  This is handled with a special placeholder containing a language tag.  Even easier, the [predefined date/time formats](#predefined-datetime-formats) are language agnostic.
* **The language of the result:** For users, what language should be used in the result of the function?  Names for months and weekdays need to be in the appropriate language for the user of the app.  This is handled with a third optional argument to the **Text** function. 

For both, the language is provided with a [language tag](../maker/functions/function-language.md#language-tags).  To see the list of supported languages type **Text( 1234, "", )** in the formula bar or advanced view and scroll through the list of locales suggested for the third argument.

#### Custom format language placeholder
To specify the language of the custom format, use:

| Placeholder | Description |
| --- | --- |
| **[$-*LanguageTag*]** |*LanguageTag* is a language tag as returned from the **Language** function.  It can be in the form of just the language such as **[$-en]** for English, or it can also include the region such as **[$-en-GB]** to further specify Great Britain. |

The language placeholder can appear anywhere in the custom format but only once.

While writing a formula, if you do not provide a language placeholder and the format string is ambiguous from a global standpoint, the authoring tool will automatically insert the language tag for your current language.  

**[$-en-US]** is assumed if this placeholder is not present when your app is run. 

> [!NOTE]
> In a future version, the syntax of this placeholder may change to avoid confusion with a similar, but different, placeholder supported by Excel.

#### Result language tag
Appearing in the result of **Text** are translated strings for month, weekday, and AM/PM designations, as well as the appropriate group and decimal separators.

By default, **Text** uses the language of the user running the app.  The **Language** function returns the language tag for the current user.  You can override this default by supplying a language tag for the optional third argument to **Text**.

## Syntax
**Text**( *Number*, *DateTimeFormatEnum* [, *ResultLanguageTag* ] )

* *Number* - Required. The number or the date/time value to format.
* *DateTimeFormat* - Required.  A member of the **DateTimeFormat** enumeration.
* *ResultLanguageTag* - Optional.  The language tag to use for the result text.  By default, the language of the current user is used.

**Text**( *Number*, *CustomFormat* [, *ResultLanguageTag* ] )

* *Number* - Required. The number or the date/time value to format.
* *CustomFormat* - Required. One or more placeholders enclosed in double quotation marks.
* *ResultLanguageTag* - Optional.  The language tag to use for the result text.  By default, the language of the current user is used.

## Examples
The user running these formulas is located in the United States and has selected English as their language.  The **Language** function is returning "en-US".

### Number
| Formula | Description | Result |
| --- | --- | --- |
| **Text(&nbsp;1234.59,&nbsp;"####.#"&nbsp;)** |Formats the number with one decimal place. |"1234.6" |
| **Text(&nbsp;8.9,&nbsp;"#.000"&nbsp;)** |Pads the decimal portion of the number with trailing zeros, if needed. |"8.900" |
| **Text(&nbsp;0.631,&nbsp;"0.#"&nbsp;)** |Pads the whole portion of the number with leading zeros, if needed. |"0.6" |
| **Text(&nbsp;12,&nbsp;"#.0#"&nbsp;)**<br>**Text(&nbsp;1234.568,&nbsp;"#.0#"&nbsp;)** |Pads the decimal portion of the number with zeros for one decimal place, and includes a second decimal place if supplied. |"12.0"<br>"1234.57" |
| **Text(&nbsp;12000,&nbsp;"$ #,###"&nbsp;)**<br>**Text(&nbsp;1200000,&nbsp;"$&nbsp;#,###"&nbsp;)** |Places a thousands separator every three digits, and includes a currency symbol. |"$&nbsp;12,000"<br>"$&nbsp;1,200,000" |

### Date/Time
* At **2:37:47 PM** on **Monday, November 23, 2015**
* United States Pacific Time Zone (UTC-8)

| Formula | Description | Result |
| --- | --- | --- |
| **Text( Now(), DateTimeFormat.LongDate )** |Formats as a long date string, in the language and locale of the current user. |"Monday, November 23, 2015" |
| **Text( Now(), DateTimeFormat.LongDateTime )** |Formats as a long date and time string, in the language and locale of the current user, using a 12-hour clock. |"Monday, November 23, 2015 2:37:47 PM" |
| **Text( Now(), DateTimeFormat.LongTime24 )** |Formats as a long time string, using a 24-hour clock. |"14:37:47" |
| **Text( Now(), DateTimeFormat.ShortDate )** |Formats as a short date string, in the language and locale of the current user. |"11/23/2015" |
| **Text( Now(), "d-mmm-yy" )** |Formats using placeholder characters: <ul><li>**d** for a single-digit or double-digit day of the month<li>**-** as a literal character copied to the result<li>**mmm** for a three-letter abbreviation of the month<li>**-** as another literal character copied to the result<li>**yy** for a two-digit abbreviation of the year</ul> |"23-Nov-15" |

### Global apps
| Formula | Description | Result |
| --- | --- | --- |
| **Text( 1234567.89, "[$-en-US]$ #,###" )** |Interprets **,** as a grouping separator placed every three characters and **$** as the currency symbol. As no decimals are to be displayed, the value is rounded up to the next higher whole number. The **[$-en-US]** is optional in this case, as this is the default. |"$ 1,234,568" |
| **Text( 1234567.89, "[$-es-ES]&euro; #,###" )** |Interprets **,** as a decimal separator and **&euro;** as the currency symbol.  Because the **[$-fr-FR]** only determines how the format string is interpreted, the result will use the characters from the default "en-US" lanugage tag: **.** (period) for decimal separator and **$** for currency symbol. |"$ 1234567.89" |
| **Text( 1234567.89, "[$-es-ES]&euro; #,###", "es-ES" )** |Interprets **,** as a decimal separator.  The result language tag has been set to "fr-FR" which will result in **,** (comma) being used as the decimal separator and **&euro;** as the currency symbol. |"&euro; 1234567,89" |
| **Text( Date(2016,1,31), "dddd mmmm d" )** |Returns the weekday, month, and day of the month in the language of the current user. Because none of the placeholders are language dependent, there is no need for a format text language tag. |"Saturday January 31" |
| **Text( Date(2016,1,31), "dddd mmmm d", "es-ES" )** |Returns the weekday, month, and day of the month in the "es-ES" language. |"domingo enero 31" |

