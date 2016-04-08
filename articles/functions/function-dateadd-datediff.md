<properties
	pageTitle="DateAdd and DateDiff functions | Microsoft PowerApps"
	description="Reference information, including syntax and examples, for the DateAdd and DateDiff functions in PowerApps"
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

# DateAdd and DateDiff functions in PowerApps #

Adds to or finds the difference in date/time values.

## Description ##

The **DateAdd** function adds **Days**, **Months**, **Quarters**, or **Years** to a date/time value.  The result is a new date/time value.

The **DateDiff** function returns the difference between two date/time values, in **Days**, **Months**, **Quarters**, or **Years**.  The result is a number.

By default, both functions use **Days** as units.

Also see [working with dates and times](../show-text-dates-times.md) for more information.

## Syntax ##

**DateAdd**( *DateTime*, *Addition* [, *Units* ] )

- *DateTime* - Required.  Date/time value to operate on.
- *Addition* - Required.  Number to add to the *DateTime*, in *Units*.
- *Units* - Optional. **Days**, **Months**, **Quarters**, or **Years**.  If not specified, **Days** are used.

**DateDiff**( *StartDateTime*, *EndDateTime* [, *Units* ] )

- *StartDateTime* - Required.  Starting date/time value.
- *EndDateTime* - Required.  Ending date/time value.
- *Units* - Optional. **Days**, **Months**, **Quarters**, or **Years**.  If not specified, **Days** are used.

## Examples ##

If today were **July 15, 2013**:

- **DateAdd(Now(), 3)** would return 7/18/2013.
- **DateAdd(Today(), 1, Days)** and **DateAdd(Today(), 1)** would both return 7/16/2013.
- **DateAdd(Today(), 1, Months)** would return 8/15/2013.
- **DateDiff(Now(), DateValue("1/1/2014"))** and **DateDiff(Now(), DateValue("1/1/2014"), Days)** would both return 170 days.
- **DateDiff(Now(), DateValue("1/1/2014"), Months)** would return 6 months.
