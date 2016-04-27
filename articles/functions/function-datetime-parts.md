<properties
	pageTitle="Day, Month, Year, Hour, Minute, Second, and Weekday functions | Microsoft PowerApps"
	description="Reference information, including syntax and examples, for the Day, Month, Year, Hour, Minute, Second, and Weekday functions in PowerApps"
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

# Day, Month, Year, Hour, Minute, Second, and Weekday functions in PowerApps #

Returns individual components of a Date/Time value.

## Description ##

The **Day** function returns the day component of a Date/Time value, ranging from 1 to 31.

The **Month** function returns the month component of a Date/Time value, ranging from 1 to 12.

The **Year** function returns the year component of a Date/Time value, starting with 1900.

The **Hour** function returns the hour component of a Date/Time value, ranging from 0 (12:00 AM) to 23 (11:00 PM).

The **Minute** function returns the minute component of a Date/Time value, ranging from 0 to 59.

The **Second** function returns the second component of a Date/Time value, ranging from 0 to 59.

The **Weekday** function returns the weekday of a Date/Time value.  By default, the result ranges from 1 (Sunday) to 7 (Saturday).  You can specify a different range with an Microsoft Excel Weekday function code:

| Excel code | Description |
|-----|--------|
|  1, 17 | Numbers 1 (Sunday) through 7 (Saturday).  |
|  2, 11 | Numbers 1 (Monday) through 7 (Sunday). |
|  3 | Numbers 0 (Monday) through 6 (Sunday). |
|  12 | Numbers 1 (Tuesday) through 7 (Monday). |
|  13 | Numbers 1 (Wednesday) through 7 (Tuesday). |
|  14 | Numbers 1 (Thursday) through 7 (Wednesday). |
|  15 | Numbers 1 (Friday) through 7 (Thursday). |
|  16 | Numbers 1 (Saturday) through 7 (Friday). |

All functions return a number.

See [working with dates and times](../show-text-dates-times.md) for more information.

## Syntax ##

**Day**( *DateTime* )<br>**Month**( *DateTime* )<br>**Year**( *DateTime* )<br>**Hour**( *DateTime* )<br>**Minute**( *DateTime* )<br>**Second**( *DateTime* )

- *DateTime* - Required.  Date/Time value to operate on.  

**Weekday**( *DateTime* [, *WeekdayFirst* ] )<br>

- *DateTime* - Required.  Date/Time value to operate on. 
- *WeekdayFirst* - Optional.  Excel code specifying which day starts the week.  If not supplied, 1 (Sunday first) is used.

## Examples ##

For the following example, the current time is **3:59:37 PM** on **Thursday, April 9, 2015**.

| Formula | Description | Result |
|---------|-------------|--------|
| **Year( Now() )** | Returns the year component of the current time and date. | 2015 |
| **Month( Now() )** | Returns the month component of the current time and date. | 4 |
| **Day( Now() )** | Returns the day component of the current time and date. | 9 |
| **Hour( Now() )** | Returns the hour component of the current time and date. | 15 |
| **Minute( Now() )** | Returns the minute component of the current time and date. | 59 |
| **Second( Now() )** | Returns the minute component of the current time and date. | 37 |
| **Weekday( Now() )** | Returns the weekday component of the current time and date, using the default start of the week as Sunday. | 5 |
| **Weekday( Now(), 14 )** | Returns the weekday component of the current time and date, using an Excel code to specify the start of the week as Friday. | 1 |


