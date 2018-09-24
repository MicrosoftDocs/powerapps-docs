---
title: DateValue, TimeValue, and DateTimeValue functions | Microsoft Docs
description: Reference information, including syntax and examples, for the DateValue, TimeValue, and DateTimeValue functions in PowerApps
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: anneta
ms.date: 11/07/2015
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# DateValue, TimeValue, and DateTimeValue functions in PowerApps
Converts a date, a time, or both in a string to a date/time value.

## Description
The **DateValue** function converts a date string (for example, "10/01/2014") to a date/time value.

The **TimeValue** function converts a time string (for example, "12:15 PM") to a date/time value.

The **DateTimeValue** functions converts a date and time string (for example, "January 10, 2013 12:13 AM") to a date/time value.

The **DateValue** function ignores any time information in the date string, and the **TimeValue** function ignores any date information in the time string.

By default, the language used is that of the current user, but you can override this to ensure that strings are interpreted properly. For example, "10/1/1920" is interpreted as October 1<sup>st</sup> in "en" and as January 10<sup>th</sup> in "fr".

Dates must be in one of these formats:

* MM/DD/YYYY
* DD/MM/YYYY
* DD Mon YYYY
* Month DD, YYYY

See the **[Date](function-date-time.md)** and **[Time](function-date-time.md)** functions to convert from numeric components date, month, and year, and hour, minute, and second.

Also see [working with dates and times](../show-text-dates-times.md) for more information.

To convert numbers, see the **[Value](function-value.md)** function.

## Syntax
**DateValue**( *String* [, *Language* ])<br>**DateTimeValue**( *String* [, *Language* ])<br>**TimeValue**( *String* [, *Language* ])

* *String* - Required.  A text string that contains a date, time, or combination date and time value.
* *Language* - Optional.  A language string, such as would be returned by the first two characters from the **[Language](function-language.md)** function.  If not provided, the language of the current user's client is used.  

## Examples
### DateValue
If you typed **10/11/2014** into a text-input control named **Startdate** and then set the **[Text](../controls/properties-core.md)** property of a label to this function:

* **Text(DateValue(Startdate.Text), DateTimeFormat.LongDate)**
  
    The label would show **Saturday, October 11, 2014**, if your computer were set to the **en** locale.
  
    > [!NOTE]
  > You can use several options, other than **LongDateTime**, with the **DateTimeFormat** parameter. To display a list of those options, type the parameter, followed immediately by an exclamation point, in the function box.
* **Text(DateValue(Startdate.Text, "fr"), DateTimeFormat.LongDate)**
  
    The label would show **Monday, November 10, 2014**.

If you did the same thing on **October 20, 2014**:

* **DateDiff(DateValue(Startdate.Text), Today())**
  
    If your computer were set to the **en** language, the label would show **9**, indicating the number of days between October 11 and October 20. The **[DateDiff](function-dateadd-datediff.md)** function can also show the difference in months, quarters, or years.

### DateTimeValue
If you typed **10/11/2014 1:50:24.765 PM** into a text-input control named **Start** and then set the **[Text](../controls/properties-core.md)** property of a label to this function:

* **Text(DateTimeValue(Start.Text), DateTimeFormat.LongDateTime)**
  
    The label would show **Saturday, October 11, 2014 1:50:24 PM** if your computer were set to the "en" locale.
  
    > [!NOTE]
  > You can use several options, other than **LongDateTime**, with the **DateTimeFormat** parameter. To display a list of those options, type the parameter, followed immediately by an exclamation point, in the function box.
* **Text(DateTimeValue(Start.Text, "fr"), DateTimeFormat.LongDateTime)**
  
    The label would show **Monday, November 10, 2014 1:50:24 PM**.
* **Text(DateTimeValue(Start.Text), "dddd, mmmm dd, yyyy hh:mm:ss.fff AM/PM")**
  
    The label would show **Saturday, October 11, 2014 01:50:24:765 PM** if your computer were set to the **en** locale.
  
    As an alternative, you can specify **hh:mm:ss.f** or **hh:mm:ss.ff** to round the time to the nearest tenth or hundredth of a second.

### TimeValue
Name a text-input control **FinishedAt**, and set the **[Text](../controls/properties-core.md)** property of a label to this function:

**If(TimeValue(FinishedAt.Text)<TimeValue("5:00:00.000 PM"), "You made it!", "Too late!")**

* If you type **4:59:59.999 PM** into the **FinishedAt** control, the label shows "You made it!"
* If you type **5:00:00.000 PM** into the **FinishedAt** control, the label shows "Too late!"

