---
title: Text function in Power Apps
description: Reference information including syntax and examples for the Text function in Power Apps.
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: nabuthuk
ms.date: 11/14/2018
ms.subservice: canvas-maker
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Text function in Power Apps
Converts any value and formats a number or date/time value to a string of text.

## Description
The **Text** function formats a number or a date/time value based on one of these types of arguments:

* A predefined date/time format, which you specify by using the **DateTimeFormat** enumeration. For dates and times, this approach is preferred as it automatically adjusts to each user's language and region.
* A custom format, which comprises a string of placeholders that define, for example, whether numbers show a decimal separator and dates show the full name of the month, the month as an abbreviation, or the month as a number. Power Apps supports a subset of the placeholders that Microsoft Excel does. In this string, the language placeholder specifies the language in which to interpret the other placeholders. If the custom format includes a period, for example, the language-format placeholder specifies whether the period is a decimal separator (ja-JP) or a thousands separator (es-ES).

See [working with dates and times](../show-text-dates-times.md) for more information.

The **Text** function can also convert any data type to a text representation using a default format. Use this to pass non-text values to text-based functions such as [**Len**](function-len.md), [**Right**](function-left-mid-right.md), and [**IsMatch**](function-ismatch.md).

### <a name="predefined-datetime-formats"></a> Predefined date/time formats

For these examples, date and time used is Tuesday, April 7, 2020 8:26:59.180 PM, in the time zone UTC-7 hours.
 
| DateTimeFormat enum | Description | Examples (using **en-US**) |
| --- | --- | --- |
| **LongDate** |Four-digit year, month name, day of the month, and day of the week. The names of the month and day of the week aren't abbreviated. | "Tuesday, April 7, 2020" |
| **LongDateTime** |Four-digit year, month name, day of the month, and day of the week, plus hour (12-hour clock), minutes, seconds, and AM/PM designation. The names of the month and day of the week aren't abbreviated. | "Tuesday, April 7, 2020 8:26:59 PM" |
| **LongDateTime24** |Four-digit year, month, day of the month, and day of the week, plus hour (24-hour clock), minutes, and seconds. The names of the month and day of the week aren't abbreviated. | "Tuesday, April 7, 2020 20:26:59" |
| **LongTime** |Hour (12-hour clock), minutes, seconds, and AM/PM designation.  | "8:26:59 PM" |
| **LongTime24** |Hour (24-hour clock), minutes, seconds.  | "20:26:59" | 
| **ShortDate** |Four-digit year with numerical month and day of the month. | "4/7/2020" | 
| **ShortDateTime** |Four-digit year with numerical month and day of the month, plus hour (12-hour clock), minutes, and AM/PM designation. | "4/7/2020 8:26 PM" |
| **ShortDateTime24** |Four-digit year with numerical month and day of the month, plus hour (24-hour clock) and minutes. | "4/7/2020 20:26" |
| **ShortTime** |Hour (12-hour clock), minutes, and AM/PM designation.   | "8:26 PM" |
| **ShortTime24** |Hour (24-hour clock) and minutes.   | "20:26" |
| **UTC** |The date/time value is converted to UTC based on the current user's time zone and formatted according to the ISO 8601 standard. | "2020-04-08T03:26:59.180Z" |

### Number placeholders

| Placeholder | Description |
| --- | --- |
| **0** (*zero*) |Displays insignificant zeros if a number has fewer digits than there are zeros in the format. For example, use the format **#.00** if you want to display **8.9** as **8.90**. |
| **#** |Follows the same rules as the **0** (zero). However, **Text** doesn't return extra zeros when the number has fewer digits on either side of the decimal than there are # symbols in the format. For example, **8.9** is displayed if the custom format is **#.##** and the number to format is **8.9**. |
| **.** (*period*) |Displays the decimal point in a number. Depends on the language of the custom format; see [global apps](#global-apps) for more details. |
| **,** (*comma*) |Displays the grouping separator in a number, often used for thousands. **Text** separates groups by commas if the format contains a comma that's enclosed by number signs (**#**) or by zeros. Depends on the language of the custom format; see [global apps](#global-apps) for more details. |

If a number has more digits to the right of the decimal point than there are placeholders in the format, the number rounds to as many decimal places as there are placeholders. If there are more digits to the left of the decimal point than there are placeholders, the extra digits are displayed. If the format contains only number signs (#) to the left of the decimal point, numbers less than 1 start with a decimal point (for example, **.47**).

### Date and time placeholders

|   Placeholder    |   Description                                                  |
|------------------|----------------------------------------------------------------|
|  **m**   |   Displays the month as a number without a leading zero.               |
|  **mm**  |   Displays the month as a number with a leading zero when appropriate. |
|  **mmm** |   Displays the month as an abbreviation (**Jan** to **Dec**).          |
|                                                                                                   **mmmm**                                                                                                   |                                                                          Displays the month as a full name (**January** to **December**).                                                                           |
|                                                                                                    **d**                                                                                                     |                                                                                Displays the day as a number without a leading zero.                                                                                 |
|                                                                                                    **dd**                                                                                                    |                                                                         Displays the day as a number with a leading zero when appropriate.                                                                          |
|                                                                                                   **ddd**                                                                                                    |                                                                              Displays the day as an abbreviation (**Sun** to **Sat**).                                                                              |
|                                                                                                   **dddd**                                                                                                   |                                                                            Displays the day as a full name (**Sunday** to **Saturday**).                                                                            |
|                                                                                                    **yy**                                                                                                    |                                                                                      Displays the year as a two-digit number.                                                                                       |
|                                                                                                   **yyyy**                                                                                                   |                                                                                      Displays the year as a four-digit number.                                                                                      |
|                                                                                                    **h**                                                                                                     |                                                                                Displays the hour as a number without a leading zero.                                                                                |
|   **hh** | Displays the hour as a number with a leading zero when appropriate. If the format contains **AM** or **PM**, the hour is shown based on the 12-hour clock. Otherwise, the hour is shown based on the 24-hour clock. | 
|  **m**   |   Displays the minute as a number without a leading zero.<br><br>This placeholder must appear immediately after the **h** or **hh** code or immediately before the **ss** code; otherwise, **Text** returns the month instead of minutes.  |    
| **mm**   | Displays the minute as a number with a leading zero when appropriate.<br><br>This placeholder must appear immediately after the **h** or **hh** placeholder or immediately before the **ss** placeholder. Otherwise, **Text** returns the month instead of minutes. |                                                                                                                   
| **s**   |  Displays the second as a number without a leading zero.  |
| **ss**  | Displays the second as a number with a leading zero when appropriate.                                                                        |
|                                                                                                    **f**                                                                                                     |                                                                                         Displays the fractions of seconds.                                                                                          |
|                                                                                    **AM/PM**, **a/p**                                                                                    |               Displays the hour based on a 12-hour clock. **Text** returns "AM" or "a" for times from midnight until noon and "PM" or "p" for times from noon until midnight                |

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
The **Text** function is globally aware. For a wide array of languages, it knows how to properly write out dates, times, currencies, and numbers. To do its job, it needs two pieces of information:

* **The language of the custom format:** For makers, how should a custom format be interpreted? The separator characters (**.** and **,**) have different meanings in different languages. If you specify a custom format, you can include a language placeholder or take the default value, which reflects the language to which your device is set. Even easier, you can use one of the [predefined date/time formats](#predefined-datetime-formats), which are language agnostic.
* **The language of the result:** For users, in what language should the function result appear? Names of months and weekdays must be in the appropriate language for the user of the app, which you can specify by adding a third, optional argument to the **Text** function. 

For both, you specify the language by using a [language tag](function-language.md#language-tags). To see the list of supported languages, type **Text( 1234, "", )** in the formula bar or the **Advanced** tab of the right-hand pane, and then scroll through the list of locales suggested for the third argument.

### Language placeholder
To specify the language of the custom format, use:

| Placeholder | Description |
| --- | --- |
| **[$-*LanguageTag*]** |*LanguageTag* is a language tag as returned from the **Language** function. It can specify just the language (such as **[$-en]** for English), or it can also specify the region (such as **[$-en-GB]** to further specify Great Britain). |

The language placeholder can appear anywhere in the custom format but only once.

If you specify a custom format without a language placeholder and the format is ambiguous from a global standpoint, the language tag for your current language is inserted automatically.  

**[$-en-US]** is assumed if this placeholder isn't present when your app is run. 

> [!NOTE]
> In a future version, the syntax of this placeholder may change to avoid confusion with a similar, but different, placeholder that Excel supports.

### Result language tag
The result of **Text** includes translated strings for months, weekdays, and AM/PM designations, as well as the appropriate group and decimal separators.

By default, **Text** uses the language of the user running the app. The **Language** function returns the language tag for the current user. You can override this default value by supplying a language tag for the third argument to **Text**.

## Syntax
**Text**( *NumberOrDateTime*, *DateTimeFormatEnum* [, *ResultLanguageTag* ] )

* *NumberOrDateTime* - Required. The number or the date/time value to format.
* *DateTimeFormat* - Required.  A member of the **DateTimeFormat** enumeration.
* *ResultLanguageTag* - Optional. The language tag to use for the result text. By default, the language of the current user is used.

**Text**( *NumberOrDateTime*, *CustomFormat* [, *ResultLanguageTag* ] )

* *Number* - Required. The number or the date/time value to format.
* *CustomFormat* - Required. One or more placeholders enclosed in double quotation marks.
* *ResultLanguageTag* - Optional. The language tag to use for the result text. By default, the language of the current user is used.

**Text**( *AnyValue* )

* *AnyValue* - Required. Value to convert to a text representation. A default format is used.

## Examples
Unless otherwise specified, the user running these formulas is located in the United States and has selected English as their language.  The **Language** function is returning "en-US".

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
| **Text(1448318857*1000, "mmm. dd, yyyy (hh:mm:ss AM/PM)")** | Shows a Unix date-time value in human-readable format if you multiply the source value by 1,000. | "Nov. 23, 2015 (02:47:37 PM)" |

### Global apps

| Formula | Description | Result |
| --- | --- | --- |
| **Text(1234567.89, "[$-fr-FR]# ###,## &euro;", "fr-FR")** | Shows a space as a grouping separator, the comma as a decimal separator, and **&euro;** as the currency symbol. |"1&nbsp;234&nbsp;567,89 &euro;" |
| **Text(1234567,89; "[$-fr-FR]# ###,## &euro;")** | If the source data follows the French custom of using a comma as the decimal separator, you must change your locale to French and separate the arguments with a semi-colon instead of a comma to get the same result as above. |"1&nbsp;234&nbsp;567,89 &euro;" |
| **Text( Date(2016,1,31), "dddd mmmm d" )** |Returns the weekday, month, and day of the month in the language of the current user. Because none of the placeholders are language dependent, there is no need for a format text language tag. |"Saturday&nbsp;January&nbsp;31" |
| **Text( Date(2016,1,31), "dddd mmmm d", "es-ES" )** |Returns the weekday, month, and day of the month in the "es-ES" language. |"domingo&nbsp;enero&nbsp;31" |

### Converting values to text

| Formula | Description | Result |
| --- | --- | --- |
| **Text(&nbsp;1234567.89&nbsp;)** | Converts a number to a string. There are no thousands separators or control over the number of digits before or after the decimal separator; for more control, supply number placeholders as the second argument. | "1234567.89" |
| **Text(&nbsp;DateTimeValue(&nbsp;"01/04/2003"&nbsp;)&nbsp;)** | Converts a date/time value to a string of text. To control the conversion, provide either a member of the DateTimeFormat enumeration or a custom-format string. | "1/4/2003 12:00 AM" |
| **Text(&nbsp;true&nbsp;)** | Converts a Boolean value to a string. | "true" |
| **Text(&nbsp;GUID()&nbsp;)** | Converts a generated GUID value to a string.  | "f8b10550-0f12-4f08-9aa3-bb10958bc3ff" |
| **Left(&nbsp;Text(&nbsp;GUID()&nbsp;),&nbsp;4&nbsp;)** | Returns the first four characters of a generated GUID. | "2d9c" | 


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]