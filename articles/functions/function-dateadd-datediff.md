<properties
	pageTitle="DateAdd and DateDiff functions | Microsoft PowerApps"
	description="Reference information, including syntax and examples, for the DateAdd and DateDiff functions in PowerApps"
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
   ms.date="05/23/2017"
   ms.author="gregli"/>

# DateAdd and DateDiff functions in PowerApps #

Adds to or finds the difference in date/time values.

## Description ##

The **DateAdd** function adds a number of units to a date/time value.  The result is a new date/time value.  Negative values can be used to subtract a number of units.

The **DateDiff** function returns the difference between two date/time values.  The result is a number of units.

For both functions, units can be in **Milliseconds**, **Seconds**, **Minutes**, **Hours**, **Days**, **Months**, **Quarters**, or **Years**.  By default, both functions use **Days** as units.

Also see [working with dates and times](../show-text-dates-times.md) for more information.

## Syntax ##

**DateAdd**( *DateTime*, *Addition* [, *Units* ] )

- *DateTime* - Required.  Date/time value to operate on.
- *Addition* - Required.  Number to add to the *DateTime*, in *Units*.
- *Units* - Optional. **Milliseconds**, **Seconds**, **Minutes**, **Hours**, **Days**, **Months**, **Quarters**, or **Years**.  If not specified, **Days** are used.

**DateDiff**( *StartDateTime*, *EndDateTime* [, *Units* ] )

- *StartDateTime* - Required.  Starting date/time value.
- *EndDateTime* - Required.  Ending date/time value.
- *Units* - Optional. **Milliseconds**, **Seconds**, **Minutes**, **Hours**, **Days**, **Months**, **Quarters**, or **Years**.  If not specified, **Days** are used.

## Examples ##

### Simple DateAdd ###

The current date and time is **July 15, 2013, 1:02 PM**.

| Formula | Description | Result |
|---------|-------------|--------|
| **Text( DateAdd( Now(), 3 ),<br>"dd-mm-yyyy hh:mm" )** | Adds three days (default units) to the current date and time. | "18-07-2013 13:02" |
| **Text( DateAdd( Now(), 4, Hours ),<br>"dd-mm-yyyy hh:mm" )** | Add three hours to the current date and time. | "15-07-2013 17:02" |  
| **Text( DateAdd( Today(), 1, Months ),<br>"dd-mm-yyyy hh:mm" )** | Adds one month to the current date, without time as **Today** does not return a time component. | "18-08-2013 00:00" |
| **Text( DateAdd( Now(), &#8209;30, Minutes ),<br>"dd-mm-yyyy hh:mm" )** | Subtracts 30 minutes from the current date and time. | "15-07-2013 12:32" |

### Simple DateDiff ###

The current date and time is **July 15, 2013, 1:02 PM**.

| Formula | Description | Result |
|---------|-------------|--------|
| **DateDiff( Now(), DateValue("1/1/2014") )** | Returns the difference between the two units in the default units of **Days** | 170 |
| **DateDiff( Now(), DateValue("1/1/2014"), Months )** | Returns the difference between the two values in **Months** | 6 | 
| **DateDiff( Now(), Today(), Minutes )** | Returns the difference between the current date/time and the current date only (no time) in minutes.  Since the **Now** is later than **Today** the result will be negative.  | -782 |

### Converting to UTC ###

To convert to UTC (Coordinated Universal Time), add the **TimeZoneOffset** for the given time.  

For example, imagine the current date and time is **July 15, 2013, 1:02 PM** in Pacific Daylight Time (PDT, UTC-7).  To determine the current time in UTC, use:

- **DateAdd( Now(), TimeZoneOffset(), Minutes )**

Since **TimeZoneOffset** defaults to the current time, we do not need to pass it an argument.

To see the result, use the **Text** function with format "dd-mm-yyyy hh:mm" which will return "15-07-2013 20:02".

### Converting from UTC ###

To convert from UTC, subtract (by adding the negative) **TimeZoneOffset** for the given time.

For example, imagine the UTC date and time **July 15, 2013, 8:02 PM** is stored in a variable named **StartTime**.  To adjust the time for the user's time zone, use:

- **DateAdd( StartTime, -TimeZoneOffset( StartTime ), Minutes )**

Note the negative sign before TimeZoneOffset to subtract the offset rather than add it.

To see the result, use the **Text** function with format "dd-mm-yyyy hh:mm" which will result in "15-07-2013 13:02".