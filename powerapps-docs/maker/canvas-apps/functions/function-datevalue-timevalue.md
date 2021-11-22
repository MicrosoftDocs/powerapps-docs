---
title: DateValue, TimeValue, and DateTimeValue functions in Power Apps
description: Reference information including syntax and examples for the DateValue, TimeValue, and DateTimeValue functions in Power Apps.
author: gregli-msft
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 04/08/2020
ms.subservice: canvas-maker
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - gregli-msft
  - nkrb
---
# DateValue, TimeValue, and DateTimeValue functions in Power Apps

Converts date, time, or both in a *string* to a *date/time* value.

## Description

- **DateValue** function converts a *date string* (for example, "10/01/2014") to a *date/time* value.

- **TimeValue** function converts a *time string* (for example, "12:15 PM") to a *date/time* value.

- **DateTimeValue** function converts a *date and time string* (for example, "January 10, 2013 12:13 AM") to a *date/time* value.

**DateValue** function ignores any time information in the date string, and the **TimeValue** function ignores any date information in the time string.

> [!NOTE]
> The DateValue, TimeValue, and DateTimeValue functions by default use the language from the current user's settings. You can override it to ensure that strings are interpreted properly. For example, "10/1/1920" is interpreted as *October 1<sup>st</sup>* in "*en*" and as *January 10<sup>th</sup>* in "*fr*".

Dates must be in one of these formats:

- MM/DD/YYYY or MM-DD-YYYY
- DD/MM/YYYY or DD-MM-YYYY
- YYYY/MM/DD or YYYY-MM-DD
- MM/DD/YY or MM-DD-YY
- DD/MM/YY or DD-MM-YY
- DD Mon YYYY
- Month DD, YYYY

To convert from numeric date, month and year components, read [Date](function-date-time.md). <br>
To convert from numeric hour, minute and second components, read [Time](function-date-time.md).

For more information, read:

- [Working with date and time](../show-text-dates-times.md).
- [Date/time and data types](data-types.md#date-time-and-datetime).

## Syntax

**DateValue**( *String* [, *Language* ])<br>
**DateTimeValue**( *String* [, *Language* ])<br>
**TimeValue**( *String* [, *Language* ])

* *String* - Required. A text string that contains a date, time, or combination date and time value.
* *Language* - Optional. A language string, such as would be returned by the first two characters from the [Language](function-language.md) function.  If not provided, the language of the current user's settings is used.  

## Examples

### DateValue

If you type **10/11/2014** into a text-input control named **Startdate**, and then set the [Text](../controls/properties-core.md) property of a label to these formulas:

- Convert a date from a string in the user's locale and show the result as a long date.

    ```powerapps-dot
    Text( DateValue( Startdate.Text ), DateTimeFormat.LongDate )
    ```

    Device set to **en** locale shows the label as **Saturday, October 11, 2014**.
  
    > [!NOTE]
    > You can use several options with the **DateTimeFormat** enum. To display a list of options, type the parameter followed by a dot or period (**.**) in the formula bar or check [**Text** function reference](function-text.md).

- Convert date from a string in the French locale and show the result as a long date. In this example, the months and day of the month are interpreted differently from English.

    ```powerapps-dot
    Text( DateValue( Startdate.Text, "fr" ), DateTimeFormat.LongDate )
    ```
  
    Device set to **en** locale shows the label as **Monday, November 10, 2014**.

If you typed **October 20, 2014** instead:

- Convert a date from a string in the user's locale and calculate the difference between two days, in days

    ```powerapps-dot
    DateDiff( DateValue( Startdate.Text ), Today() )
    ```
  
    Device set to **en** locale shows the label as **9**, indicating the number of days between October 11 and October 20. The [DateDiff](function-dateadd-datediff.md) function can also show the difference in months, quarters, or years.

### DateTimeValue

If you typed **10/11/2014 1:50:24.765 PM** into a text-input control named **Start**, and then set the [Text](../controls/properties-core.md) property of a label to the following formula:

- Convert both a date and time string in the current locale.
 
    ```powerapps-dot
    Text( DateTimeValue( Start.Text ), DateTimeFormat.LongDateTime )
    ```    
    
    Device set to **en** locale shows the label as **Saturday, October 11, 2014 1:50:24 PM**.
  
  > [!NOTE]
  > You can use several options with the **DateTimeFormat** enum. To display a list of options, type the parameter followed by a dot or period (**.**) in the formula bar or check [**Text** function reference](function-text.md).

- Convert both a date and time string in the French locale. Month and day of the month are interpreted differently.

    ```powerapps-dot
    Text( DateTimeValue( Start.Text, "fr"), DateTimeFormat.LongDateTime )
    ```
  
    Device set to **en** locale shows the label as **Monday, November 10, 2014 1:50:24 PM**.

- Convert both a date and time string in the user's locale, and display the result with a fractional second.

    ```powerapps-dot
    Text( DateTimeValue( Start.Text ), "dddd, mmmm dd, yyyy hh:mm:ss.fff AM/PM" )
    ```
  
    Device set to **en** locale shows the label as **Saturday, October 11, 2014 01:50:24.765 PM**.
  
    As an alternative, you can specify **hh:mm:ss.f** or **hh:mm:ss.ff** to round the time to the nearest 10<sup>th</sup> or 100<sup>th</sup> of a second.

### TimeValue

Name a text-input control **FinishedAt**, and set the [Text](../controls/properties-core.md) property of a label to this formula:

```powerapps-dot
If( TimeValue( FinishedAt.Text ) < TimeValue( "5:00:00.000 PM" ), 
    "You made it!", 
    "Too late!"
)
```

- If you type **4:59:59.999 PM** in the **FinishedAt** control, the label shows "*You made it!*"
- If you type **5:00:00.000 PM** in the **FinishedAt** control, the label shows "*Too late!*"


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]