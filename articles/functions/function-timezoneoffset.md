<properties
	pageTitle="TimeZoneOffset function in PowerApps | Microsoft PowerApps"
	description="Reference information, including syntax and examples, for the TimeZoneOffset function in PowerApps"
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

# TimeZoneOffset functions in PowerApps #

Returns the difference between UTC and the user's time zone in minutes.

## Description ##

The **TimeZoneOffset** function returns the number of minutes between the user's time zone and UTC (Coordinated Universal Time).   

This value can be used with the [**DateAdd**](function-dateadd-datediff.md) function to convert to and from UTC. Adding **TimeZoneOffset** will convert a local time to UTC, subtracting (adding the negative) will convert from UTC to local time.

Also see [working with dates and times](../show-text-dates-times.md) for more information.

## Syntax ##

**TimeZoneOffset**( [ *DateTime* ] )

- *DateTime* - Optional.  Date/time value to return the offset for.  By default, the current date/time is used.

## Examples ##

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