---
title: WeekNum and ISOWeekNum functions in Power Apps
description: Reference information including syntax and examples for the WeekNum and ISOWeekNum functions in Power Apps.
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: nabuthuk
ms.date: 06/23/2021
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# WeekNum and ISOWeekNum functions in Power Apps

Returns the week number of a specific date. 

## Description

Use the **WeekNum** and **ISOWeekNum** functions to determine the week number of a date.

These functions differ in how they determine the first week of the year (week 1):
- **WeekNum** - The week containing January 1 is the first week of the year.  The result ranges from 1 to 54.
- **ISOWeekNum** - The week containing the first Thursday of the year is the first week of the year. This follows the [ISO 8601 date and time standard definition](https://en.wikipedia.org/wiki/ISO_week_date) for week numbering.  The result ranges from 1 to 53.  It is possible that 52 or 53 may be returned for the first days of January, indicating that the date belongs to the last week of the previous year.

The **WeekNum** function supports weeks that start with different days.  

| Excel code | StartOfWeek enumeration | Description |
| --- | --- | --- |
| **1**, **17** |**StartOfWeek.Sunday** |Week begins on Sunday.  Default. |
| **2**, **11** |**StartOfWeek.Monday** |Week begins on Monday. |
| **12** |**StartOfWeek.Tuesday** |Week begins on Tuesday. |
| **13** |**StartOfWeek.Wednesday** |Week begins on Wednesday. |
| **14** |**StartOfWeek.Thursday** |Week begins on Thursday. |
| **15** |**StartOfWeek.Friday** |Week begins on Friday. |
| **16** |**StartOfWeek.Saturday** |Week begins on Saturday. |

**ISOWeekNum** always uses Monday.  Excel supports an addition code **21** that is the equivalent of using **ISOWeekNum**.

If you pass a single number to these functions, the return value is a single result.  If you pass a single-column [table](../working-with-tables.md) that contains numbers, the return value is a single-column table of results, one result for each record in the argument's table. If you have a multi-column table, you can shape it into a single-column table, as [working with tables](../working-with-tables.md) describes.  

## Syntax
**WeekNum**( *DateTime* [, *StartOfWeek* ] )

* *DateTime* - Required.  Date/Time value to operate on.  
* *StartOfWeek* - Optional.  Excel code or StartOfWeek enumartion that determines which day the week begins.

**ISOWeekNum**( *DateTime* )

* *DateTime* - Required.  Date/Time value to operate on.  The week always begins on Monday.

## Examples

First and last calendar weeks of 2021

| Date | WeekNum( Date ) | ISOWeekNum( Date ) | WeekNum( Date, StartOfWeek.Wednesday ) |  
|------|:---------------:|:-------------------:|:-------------------------------------:|
| Friday, January 1, 2021 | 1 | 53 | 1 |
| Saturday, January 2, 2021 | 1 | 53 | 1 |
| Sunday, Jaunary 3, 2021 | 2 | 53 | 1 |
| Monday, January 4, 2021 | 2 | 1 | 1 |
| Tuesday, January 5, 2021 | 2 | 1 | 1 |
| Wednesday, January 6, 2021 | 2 | 1 | 2 |
| Thursday, January 7, 2021 | 2 | 1 | 2 |
| Saturday, December 25, 2021 | 52 | 51 | 52 |
| Sunday, December 26, 2021 | 53 | 51 | 52 |
| Monday, December 27, 2021 | 53 | 52 | 52 |
| Tuesday, December 28, 2021 | 53 | 52 | 52 |
| Wednesday, December 29, 2021 | 53 | 52 | 53 |
| Thursday, December 30, 2021 | 53 | 52 | 53 |
| Friday, December 31, 2021 | 53 | 52 | 53 |

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]