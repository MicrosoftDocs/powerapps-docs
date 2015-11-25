<properties
	pageTitle="PowerApps: Day, Month, Year, Hour, Minute, and Second functions"
	description="Reference information for the Day, Month, Year, Hour, Minute, and Second functions in PowerApps, including syntax and examples"
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

# Day, Month, Year, Hour, Minute, and Second functions #

Returns individual components of a Date/Time value.

## Description ##

The **Day** function returns the day component of a Date/Time value, ranging from 1 to 31.

The **Month** function returns the month component of a Date/Time value, ranging from 1 to 12.

The **Year** function returns the year component of a Date/Time value, starting with 1900.

The **Hour** function returns the hour component of a Date/Time value, ranging from 0 (12:00 AM) to 23 (11:00 PM).

The **Minute** function returns the minute component of a Date/Time value, ranging from 0 to 59.

The **Second** function returns the second component of a Date/Time value, ranging from 0 to 59.

All functions return a number.

See [working with dates and times](../show-text-dates-times.md) for more information. 

<!-- TOOD: should we have a millisecond? -->

## Syntax ##

**Day**( *DateTime* )<br>**Month**( *DateTime* )<br>**Year**( *DateTime* )<br>**Hour**( *DateTime* )<br>**Minute**( *DateTime* )<br>**Second**( *DateTime* )

- *DateTime* - Required.  Date/Time value to operate on.  

<!-- TODO: examples -->

