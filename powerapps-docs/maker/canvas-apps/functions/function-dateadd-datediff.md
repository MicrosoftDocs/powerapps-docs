---
title: DateAdd, DateDiff, and TimeZoneOffset functions in Power Apps
description: Reference information including syntax and examples for the DateAdd, DateDiff, and TimeZoneOffset functions in Power Apps.
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: nabuthuk
ms.date: 05/23/2017
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# DateAdd, DateDiff, and TimeZoneOffset functions in Power Apps
Adds to or finds the difference in date/time values and converts between local time and UTC.

## Description
The **DateAdd** function adds a number of units to a date/time value. The result is a new date/time value. You can also subtract a number of units from a date/time value by specifying a negative value.

The **DateDiff** function returns the difference between two date/time values. The result is a whole number of units.

For both functions, units can be **Milliseconds**, **Seconds**, **Minutes**, **Hours**, **Days**, **Months**, **Quarters**, or **Years**.  By default, both functions use **Days** as units.

The **TimeZoneOffset** function returns the number of minutes between the user's local time and UTC (Coordinated Universal Time).   

You can use **DateAdd** with the **TimeZoneOffset** to convert between the user's local time and UTC (Coordinated Universal Time).  Adding **TimeZoneOffset** will convert a local time to UTC, and subtracting it (adding the negative) will convert from UTC to local time.

Also see [Date, Time, and DateTime data types](../functions/data-types.md#date-time-and-datetime) and [working with dates and times](../show-text-dates-times.md) for more information.

## Syntax
**DateAdd**( *DateTime*, *Addition* [, *Units* ] )

* *DateTime* - Required. Date/time value to operate on.
* *Addition* - Required. Number, in *Units*, to add to the *DateTime*.
* *Units* - Optional. The type of *Units* to add: **Milliseconds**, **Seconds**, **Minutes**, **Hours**, **Days**, **Months**, **Quarters**, or **Years**.  If not specified, **Days** are used.

**DateDiff**( *StartDateTime*, *EndDateTime* [, *Units* ] )

* *StartDateTime* - Required. Starting date/time value.
* *EndDateTime* - Required. Ending date/time value.
* *Units* - Optional. The type of *Units* to subtract: **Milliseconds**, **Seconds**, **Minutes**, **Hours**, **Days**, **Months**, **Quarters**, or **Years**.  If not specified, **Days** are used.

**TimeZoneOffset**( [ *DateTime* ] )

* *DateTime* - Optional.  Date/time value for which to return the offset.  By default, the current date/time is used.

## Examples
In all of these examples, assume that the current date and time is **July 15, 2013, 1:02 PM**.

### Simple DateAdd

| Formula | Description | Result |
| --- | --- | --- |
| **Text( DateAdd( Now(), 3 ),<br>"dd-mm-yyyy hh:mm" )** |Adds three days (default units) to the current date and time. |"18-07-2013 13:02" |
| **Text( DateAdd( Now(), 4, Hours ),<br>"dd-mm-yyyy hh:mm" )** |Add four hours to the current date and time. |"15-07-2013 17:02" |
| **Text( DateAdd( Today(), 1, Months ),<br>"dd-mm-yyyy hh:mm" )** |Adds one month to the current date, without time as **Today** doesn't return a time component. |"15-08-2013 00:00" |
| **Text( DateAdd( Now(), &#8209;30, Minutes ),<br>"dd-mm-yyyy hh:mm" )** |Subtracts 30 minutes from the current date and time. |"15-07-2013 12:32" |

### Simple DateDiff

| Formula | Description | Result |
| --- | --- | --- |
| **DateDiff( Now(), DateValue("1/1/2014") )** |Returns the difference between the two units in the default units of **Days** |170 |
| **DateDiff( Now(), DateValue("1/1/2014"), Months )** |Returns the difference between the two values in **Months** |6 |
| **DateDiff( Now(), Today(), Minutes )** |Returns the difference between the current date/time and the current date only (no time) in minutes.  Since the **Now** is later than **Today** the result will be negative. |-782 |

### Difference of dates with fractional results

The function DateDiff only returns a whole number of the units being subtracted, and the precision is given in the unit specified. To calculate the difference with a higher precision, use a smaller unit, and convert the result appropriately, like in the examples below.

| Formula | Description | Result |
| --- | --- | --- |
| **DateDiff( TimeValue("09:45:00"), TimeValue("10:15:36"), Hours )** | The minutes/seconds are ignored, the difference is based on the time up to the hour. | 1 |
| **DateDiff( TimeValue("09:45:00"), TimeValue("10:15:36"), Minutes )/60** | The minutes are used in the difference, and the result is divided by 60 to have the difference in hours. | 0.5 |
| **DateDiff( TimeValue("09:45:00"), TimeValue("10:15:36"), Seconds )/3600** | The minutes and seconds are used in the difference; the result is divided by 3600 to have the difference in hours. | 0.51 |

### Converting to UTC
To convert to UTC (Coordinated Universal Time), add the **TimeZoneOffset** for the given time.  

For example, imagine the current date and time is **July 15, 2013, 1:02 PM** in Pacific Daylight Time (PDT, UTC-7).  To determine the current time in UTC, use:

* **DateAdd( Now(), TimeZoneOffset(), Minutes )**

**TimeZoneOffset** defaults to the current time, so you don't need to pass it an argument.

To see the result, use the **Text** function with the format *dd-mm-yyyy hh:mm*, which will return **15-07-2013 20:02**.

### Converting from UTC
To convert from UTC, subtract the **TimeZoneOffset** (by adding the negative) for the given time.

For example, imagine the UTC date and time **July 15, 2013, 8:02 PM** is stored in a variable named **StartTime**. To adjust the time for the user's time zone, use:

* **DateAdd( StartTime, &minus;TimeZoneOffset( StartTime ), Minutes )**

Note the negative sign before **TimeZoneOffset** to subtract the offset rather than add it.

To see the result, use the **Text** function with the format *dd-mm-yyyy hh:mm*, which will result in **15-07-2013 13:02** if you're in Pacific Daylight Time.



[!INCLUDE[footer-include](../../../includes/footer-banner.md)]