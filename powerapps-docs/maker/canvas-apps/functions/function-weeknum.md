---
title: WeekNum and ISOWeekNum functions in Power Apps
description: Reference information including syntax and examples for the WeekNum and ISOWeekNum functions in Power Apps.
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: nabuthuk
ms.date: 08/05/2021
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

- **WeekNum** uses the week containing January 1 as the first week of the year.  The result from this function can range from 1 to 54.

- **ISOWeekNum** uses the week containing the first Thursday of the year as the first week of the year. This follows the [ISO 8601 date and time standard definition](https://en.wikipedia.org/wiki/ISO_week_date) for week numbering.  The result from this function can range from 1 to 53.  It is possible that 52 or 53 may be returned for the first days of January since the dates could belong to the last week of the previous year.

Use the second parameter to **WeekNum** to specify which day begins a week.  You can provide either an Excel code number or use the StartOfWeek enumeration:

| Excel code | StartOfWeek enumeration | Description |
| --- | --- | --- |
| **1**, **17** |**StartOfWeek.Sunday** |Week begins on Sunday.  Default. |
| **2**, **11** |**StartOfWeek.Monday** |Week begins on Monday. |
| **12** |**StartOfWeek.Tuesday** |Week begins on Tuesday. |
| **13** |**StartOfWeek.Wednesday** |Week begins on Wednesday. |
| **14** |**StartOfWeek.Thursday** |Week begins on Thursday. |
| **15** |**StartOfWeek.Friday** |Week begins on Friday. |
| **16** |**StartOfWeek.Saturday** |Week begins on Saturday. |

**ISOWeekNum** always uses Monday as the start of the week.  In Excel, the **WeekNum** function supports an addition code **21** that is not supported here; use **ISOWeekNum** instead.

If you pass a single number to these functions, the return value is a single result.  If you pass a single-column [table](../working-with-tables.md) that contains numbers, the return value is a single-column table of results, one result for each record in the argument's table. If you have a multi-column table, you can shape it into a single-column table, as [working with tables](../working-with-tables.md) describes.  

## Syntax

**WeekNum**( *DateTime* [, *StartOfWeek* ] )

- *DateTime* - Required.  Date/Time value to operate on.  
- *StartOfWeek* - Optional.  Excel code or StartOfWeek enumeration that determines which day the week begins.

**ISOWeekNum**( *DateTime* )

- *DateTime* - Required.  Date/Time value to operate on.  The week always begins on Monday.

## Examples

First and last calendar weeks of 2021

| Date | WeekNum(&nbsp;Date&nbsp;) | ISOWeekNum(&nbsp;Date&nbsp;) | WeekNum(&nbsp;Date, StartOfWeek.Wednesday&nbsp;) |
|------|:-------:|:-------:|:------:|
| Friday,&nbsp;January&nbsp;1,&nbsp;2021 | 1 | 53 | 1 |
| Saturday,&nbsp;January&nbsp;2,&nbsp;2021 | 1 | 53 | 1 |
| Sunday,&nbsp;January&nbsp;3,&nbsp;2021 | 2 | 53 | 1 |
| Monday,&nbsp;January&nbsp;4,&nbsp;2021 | 2 | 1 | 1 |
| Tuesday,&nbsp;January&nbsp;5,&nbsp;2021 | 2 | 1 | 1 |
| Wednesday,&nbsp;January&nbsp;6,&nbsp;2021 | 2 | 1 | 2 |
| Thursday,&nbsp;January&nbsp;7,&nbsp;2021 | 2 | 1 | 2 |
| Saturday,&nbsp;December&nbsp;25,&nbsp;2021 | 52 | 51 | 52 |
| Sunday,&nbsp;December&nbsp;26,&nbsp;2021 | 53 | 51 | 52 |
| Monday,&nbsp;December&nbsp;27,&nbsp;2021 | 53 | 52 | 52 |
| Tuesday,&nbsp;December&nbsp;28,&nbsp;2021 | 53 | 52 | 52 |
| Wednesday,&nbsp;December&nbsp;29,&nbsp;2021 | 53 | 52 | 53 |
| Thursday,&nbsp;December&nbsp;30,&nbsp;2021 | 53 | 52 | 53 |
| Friday,&nbsp;December&nbsp;31,&nbsp;2021 | 53 | 52 | 53 |

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]