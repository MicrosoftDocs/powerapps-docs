---
title: Date and Time functions in Power Apps
description: Reference information including syntax and examples for the Date and Time functions in Power Apps.
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: nabuthuk
ms.date: 11/07/2015
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Date and Time functions in Power Apps
Converts date and time components to a date/time value.

## Description
The **Date** function converts individual Year, Month, and Day values to a Date/Time value.  The time portion is midnight.

* If Year is between 0 and 1899 (inclusive), the function adds that value to 1900 to calculate the year.  **70** becomes **1970**.
* If Month is less than 1 or more than 12, the result subtracts or adds that many months from the beginning of the specified year.
* If Day is greater than the number of days in the specified month, the function adds that many days to the first day of the month and returns the corresponding date from a subsequent month.  If Day is less than 1, the function subtracts that many days, plus 1, from the first day of the specified month.

The **Time** function converts individual Hour, Minute, and Second values to a Date/Time value.  The result has no date associated with it.

See the **[DateValue](function-datevalue-timevalue.md)**, **[TimeValue](function-datevalue-timevalue.md)**, and **[DateTimeValue](function-datevalue-timevalue.md)** functions for information about how to convert a string to a value.  

Also see [working with dates and times](../show-text-dates-times.md) for more information.

## Syntax
**Date**( *Year*, *Month*, *Day* )

* *Year* - Required.  Numbers greater than 1899 are interpreted as absolute (1980 is interpreted as 1980); numbers that range from 0 to 1899 are interpreted as relative to 1900. (For example, 80 is interpreted as 1980.)
* *Month* - Required.  A number that ranges from 1 to 12.
* *Day* - Required. A number that ranges from 1 to 31.

**Time**( *Hour*, *Minute*, *Second* )

* *Hour* - Required.  A number that ranges from 0 (12:00 AM) to 23 (11:00 PM).
* *Minute* - Required. A number that ranges from 0 to 59.
* *Second* - Required. A number that ranges from 0 to 59.

## Examples
### Date
If a user typed **1979** in a text-input control named **HireYear**, **3** in a text-input control named **HireMonth**, and **17** in a text-input control named **HireDay**, this function would return **3/17/1979**:

**Date(Value(HireYear.Text), Value(HireMonth.Text), Value(HireDay.Text))**

### Time
If a user typed **14** in a text-input control named **BirthHour**, **50** in a text-input control named **BirthMinute**, and **24** in a text-input control named **BirthSecond**, this function would return **02:50:24 p**.

**Text(Time(Value(BirthHour.Text), Value(BirthMinute.Text), Value(BirthSecond.Text)), "hh:mm:ss a/p")**



[!INCLUDE[footer-include](../../../includes/footer-banner.md)]