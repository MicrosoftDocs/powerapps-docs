---
title: Now, Today, and IsToday functions | Microsoft Docs
description: Reference information, including syntax and examples, for the Now, Today, and IsToday functions in PowerApps
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
ms.date: 11/07/2015
ms.author: gregli

---
# Now, Today, and IsToday functions in PowerApps
Returns the current date and time, and tests whether a date/time value is today.

## Description
The **Now** function returns the current date and time as a date/time value.

The **Today** function returns the current date as a date/time value. The time portion is midnight. **Today** has the same value throughout a day, from midnight today to midnight tomorrow.

The **IsToday** function tests whether a date/time value is between midnight today and midnight tomorrow. This function returns a Boolean **true** or **false** value.

All these functions work with the local time of the current user.

See [working with dates and times](../show-text-dates-times.md) for more information.

## Syntax
**Now**()

**Today**()

**IsToday**( *DateTime* )

* *DateTime* - Required.  The date/time value to test.

## Examples
For the examples in this section, the current time is **3:59 AM** on **February 12, 2015**, and the language is **en-us**.

| Formula | Description | Result |
| --- | --- | --- |
| **Text( Now(), "mm/dd/yyyy hh:mm:ss" )** |Retrieves the current date and time, and displays it as a string. |"02/12/2015 03:59:00" |
| **Text( Today(), "mm/dd/yyyy hh:mm:ss" )** |Retrieves the current date only, leaving the time portion as midnight, and displays it as a string. |"02/12/2015 00:00:00" |
| **IsToday( Now() )** |Tests whether the current date and time is between midnight today and midnight tomorrow. |**true** |
| **IsToday( Today() )** |Tests whether the current date is between midnight today and midnight tomorrow. |**true** |
| **Text( DateAdd( Now(), 12 ), "mm/dd/yyyy hh:mm:ss" )** |Retrieves the current date and time, adds 12 days to the result, and displays it as a string. |"02/24/2015 03:59:00" |
| **Text( DateAdd( Today(), 12 ), "mm/dd/yyyy hh:mm:ss" )** |Retrieves the current date, adds 12 days to the result, and displays it as a string. |"02/24/2015 00:00:00" |
| **IsToday( DateAdd( Now(), 12 ) )** |Tests whether the current date and time, plus 12 days, is between midnight today and midnight tomorrow. |**false** |
| **IsToday( DateAdd( Today(), 12 ) )** |Tests whether the current date, plus 12 days, is between midnight today and midnight tomorrow. |**false** |

