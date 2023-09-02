---
title: condition operator values
description: Use these values in a condition element operator attribute to specify how to evaluate the condition.
author: pnghub
ms.author: gned
ms.reviewer: jdaly
ms.date: 08/31/2023
ms.topic: reference
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
contributors:
 - JimDaly
---
# condition operator values

To learn how to use these values, see [Filter rows using FetchXml](../filter-rows.md).

|Operator|Description|Data Types|
|---|---|---|
|[above](#above)|[!INCLUDE [operator-above-description](includes/operator-above-description.md)]|[Hierarchical](#hierarchical-data)|
|[begins-with](#begins-with)|[!INCLUDE [operator-begins-with-description](includes/operator-begins-with-description.md)]|TBD|
|[between](#between)|[!INCLUDE [operator-between-description](includes/operator-between-description.md)]|TBD|
|[contain-values](#contain-values)|[!INCLUDE [operator-contain-values-description](includes/operator-contain-values-description.md)]|TBD|
|[ends-with](#ends-with)|[!INCLUDE [operator-ends-with-description](includes/operator-ends-with-description.md)]|TBD|
|[eq](#eq)|[!INCLUDE [operator-eq-description](includes/operator-eq-description.md)]|TBD|
|[eq-businessid](#eq-businessid)|[!INCLUDE [operator-eq-businessid-description](includes/operator-eq-businessid-description.md)]|TBD|
|[eq-or-above](#eq-or-above)|[!INCLUDE [operator-eq-or-above-description](includes/operator-eq-or-above-description.md)]|[Hierarchical](#hierarchical-data)|
|[eq-or-under](#eq-or-under)|[!INCLUDE [operator-eq-or-under-description](includes/operator-eq-or-under-description.md)]|[Hierarchical](#hierarchical-data)|
|[eq-userid](#eq-userid)|[!INCLUDE [operator-eq-userid-description](includes/operator-eq-userid-description.md)]|TBD|
|[eq-userlanguage](#eq-userlanguage)|[!INCLUDE [operator-eq-userlanguage-description](includes/operator-eq-userlanguage-description.md)]|TBD|
|[eq-useroruserhierarchy](#eq-useroruserhierarchy)|[!INCLUDE [operator-eq-useroruserhierarchy-description](includes/operator-eq-useroruserhierarchy-description.md)]|[Hierarchical](#hierarchical-data)|
|[eq-useroruserhierarchyandteams](#eq-useroruserhierarchyandteams)|[!INCLUDE [operator-eq-useroruserhierarchyandteams-description](includes/operator-eq-useroruserhierarchyandteams-description.md)]|[Hierarchical](#hierarchical-data)|
|[eq-useroruserteams](#eq-useroruserteams)|[!INCLUDE [operator-eq-useroruserteams-description](includes/operator-eq-useroruserteams-description.md)]|TBD|
|[eq-userteams](#eq-userteams)|[!INCLUDE [operator-eq-userteams-description](includes/operator-eq-userteams-description.md)]|TBD|
|[ge](#ge)|[!INCLUDE [operator-ge-description](includes/operator-ge-description.md)]|TBD|
|[gt](#gt)|[!INCLUDE [operator-gt-description](includes/operator-gt-description.md)]|TBD|
|[in](#in)|[!INCLUDE [operator-in-description](includes/operator-in-description.md)]|TBD|
|[in-fiscal-period](#in-fiscal-period)|[!INCLUDE [operator-in-fiscal-period-description](includes/operator-in-fiscal-period-description.md)]|TBD|
|[in-fiscal-period-and-year](#in-fiscal-period-and-year)|[!INCLUDE [operator-in-fiscal-period-and-year-description](includes/operator-in-fiscal-period-and-year-description.md)]|TBD|
|[in-fiscal-year](#in-fiscal-year)|[!INCLUDE [operator-in-fiscal-year-description](includes/operator-in-fiscal-year-description.md)]|TBD|
|[in-or-after-fiscal-period-and-year](#in-or-after-fiscal-period-and-year)|[!INCLUDE [operator-in-or-after-fiscal-period-and-year-description](includes/operator-in-or-after-fiscal-period-and-year-description.md)]|TBD|
|[in-or-before-fiscal-period-and-year](#in-or-before-fiscal-period-and-year)|[!INCLUDE [operator-in-or-before-fiscal-period-and-year-description](includes/operator-in-or-before-fiscal-period-and-year-description.md)]|TBD|
|[last-fiscal-period](#last-fiscal-period)|[!INCLUDE [operator-last-fiscal-period-description](includes/operator-last-fiscal-period-description.md)]|TBD|
|[last-fiscal-year](#last-fiscal-year)|[!INCLUDE [operator-last-fiscal-year-description](includes/operator-last-fiscal-year-description.md)]|TBD|
|[last-month](#last-month)|[!INCLUDE [operator-last-month-description](includes/operator-last-month-description.md)]|TBD|
|[last-seven-days](#last-seven-days)|[!INCLUDE [operator-last-seven-days-description](includes/operator-last-seven-days-description.md)]|TBD|
|[last-week](#last-week)|[!INCLUDE [operator-last-week-description](includes/operator-last-week-description.md)]|TBD|
|[last-x-days](#last-x-days)|[!INCLUDE [operator-last-x-days-description](includes/operator-last-x-days-description.md)]|TBD|
|[last-x-fiscal-periods](#last-x-fiscal-periods)|[!INCLUDE [operator-last-x-fiscal-periods-description](includes/operator-last-x-fiscal-periods-description.md)]|TBD|
|[last-x-fiscal-years](#last-x-fiscal-years)|[!INCLUDE [operator-last-x-fiscal-years-description](includes/operator-last-x-fiscal-years-description.md)]|TBD|
|[last-x-hours](#last-x-hours)|[!INCLUDE [operator-last-x-hours-description](includes/operator-last-x-hours-description.md)]|TBD|
|[last-x-months](#last-x-months)|[!INCLUDE [operator-last-x-months-description](includes/operator-last-x-months-description.md)]|TBD|
|[last-x-weeks](#last-x-weeks)|[!INCLUDE [operator-last-x-weeks-description](includes/operator-last-x-weeks-description.md)]|TBD|
|[last-x-years](#last-x-years)|[!INCLUDE [operator-last-x-years-description](includes/operator-last-x-years-description.md)]|TBD|
|[last-year](#last-year)|[!INCLUDE [operator-last-year-description](includes/operator-last-year-description.md)]|TBD|
|[le](#le)|[!INCLUDE [operator-le-description](includes/operator-le-description.md)]|TBD|
|[like](#like)|[!INCLUDE [operator-like-description](includes/operator-like-description.md)]|TBD|
|[lt](#lt)|[!INCLUDE [operator-lt-description](includes/operator-lt-description.md)]|TBD|
|[ne](#ne)|[!INCLUDE [operator-ne-description](includes/operator-ne-description.md)]|TBD|
|[ne-businessid](#ne-businessid)|[!INCLUDE [operator-ne-businessid-description](includes/operator-ne-businessid-description.md)]|TBD|
|[ne-userid](#ne-userid)|[!INCLUDE [operator-ne-userid-description](includes/operator-ne-userid-description.md)]|TBD|
|[neq](#neq)|[!INCLUDE [operator-neq-description](includes/operator-neq-description.md)]|TBD|
|[next-fiscal-period](#next-fiscal-period)|[!INCLUDE [operator-next-fiscal-period-description](includes/operator-next-fiscal-period-description.md)]|TBD|
|[next-fiscal-year](#next-fiscal-year)|[!INCLUDE [operator-next-fiscal-year-description](includes/operator-next-fiscal-year-description.md)]|TBD|
|[next-month](#next-month)|[!INCLUDE [operator-next-month-description](includes/operator-next-month-description.md)]|TBD|
|[next-seven-days](#next-seven-days)|[!INCLUDE [operator-next-seven-days-description](includes/operator-next-seven-days-description.md)]|TBD|
|[next-week](#next-week)|[!INCLUDE [operator-next-week-description](includes/operator-next-week-description.md)]|TBD|
|[next-x-days](#next-x-days)|[!INCLUDE [operator-next-x-days-description](includes/operator-next-x-days-description.md)]|TBD|
|[next-x-fiscal-periods](#next-x-fiscal-periods)|[!INCLUDE [operator-next-x-fiscal-periods-description](includes/operator-next-x-fiscal-periods-description.md)]|TBD|
|[next-x-fiscal-years](#next-x-fiscal-years)|[!INCLUDE [operator-next-x-fiscal-years-description](includes/operator-next-x-fiscal-years-description.md)]|TBD|
|[next-x-hours](#next-x-hours)|[!INCLUDE [operator-next-x-hours-description](includes/operator-next-x-hours-description.md)]|TBD|
|[next-x-months](#next-x-months)|[!INCLUDE [operator-next-x-months-description](includes/operator-next-x-months-description.md)]|TBD|
|[next-x-weeks](#next-x-weeks)|[!INCLUDE [operator-next-x-weeks-description](includes/operator-next-x-weeks-description.md)]|TBD|
|[next-x-years](#next-x-years)|[!INCLUDE [operator-next-x-years-description](includes/operator-next-x-years-description.md)]|TBD|
|[next-year](#next-year)|[!INCLUDE [operator-next-year-description](includes/operator-next-year-description.md)]|TBD|
|[not-begin-with](#not-begin-with)|[!INCLUDE [operator-not-begin-with-description](includes/operator-not-begin-with-description.md)]|TBD|
|[not-between](#not-between)|[!INCLUDE [operator-not-between-description](includes/operator-not-between-description.md)]|TBD|
|[not-contain-values](#not-contain-values)|[!INCLUDE [operator-not-contain-values-description](includes/operator-not-contain-values-description.md)]|TBD|
|[not-end-with](#not-end-with)|[!INCLUDE [operator-not-end-with-description](includes/operator-not-end-with-description.md)]|TBD|
|[not-in](#not-in)|[!INCLUDE [operator-not-in-description](includes/operator-not-in-description.md)]|TBD|
|[not-like](#not-like)|[!INCLUDE [operator-not-like-description](includes/operator-not-like-description.md)]|TBD|
|[not-null](#not-null)|[!INCLUDE [operator-not-null-description](includes/operator-not-null-description.md)]|TBD|
|[not-under](#not-under)|[!INCLUDE [operator-not-under-description](includes/operator-not-under-description.md)]|[Hierarchical](#hierarchical-data)|
|[null](#null)|[!INCLUDE [operator-null-description](includes/operator-null-description.md)]|TBD|
|[olderthan-x-days](#olderthan-x-days)|[!INCLUDE [operator-olderthan-x-days-description](includes/operator-olderthan-x-days-description.md)]|TBD|
|[olderthan-x-hours](#olderthan-x-hours)|[!INCLUDE [operator-olderthan-x-hours-description](includes/operator-olderthan-x-hours-description.md)]|TBD|
|[olderthan-x-minutes](#olderthan-x-minutes)|[!INCLUDE [operator-olderthan-x-minutes-description](includes/operator-olderthan-x-minutes-description.md)]|TBD|
|[olderthan-x-months](#olderthan-x-months)|[!INCLUDE [operator-olderthan-x-months-description](includes/operator-olderthan-x-months-description.md)]|TBD|
|[olderthan-x-weeks](#olderthan-x-weeks)|[!INCLUDE [operator-olderthan-x-weeks-description](includes/operator-olderthan-x-weeks-description.md)]|TBD|
|[olderthan-x-years](#olderthan-x-years)|[!INCLUDE [operator-olderthan-x-years-description](includes/operator-olderthan-x-years-description.md)]|TBD|
|[on](#on)|[!INCLUDE [operator-on-description](includes/operator-on-description.md)]|TBD|
|[on-or-after](#on-or-after)|[!INCLUDE [operator-on-or-after-description](includes/operator-on-or-after-description.md)]|TBD|
|[on-or-before](#on-or-before)|[!INCLUDE [operator-on-or-before-description](includes/operator-on-or-before-description.md)]|TBD|
|[this-fiscal-period](#this-fiscal-period)|[!INCLUDE [operator-this-fiscal-period-description](includes/operator-this-fiscal-period-description.md)]|TBD|
|[this-fiscal-year](#this-fiscal-year)|[!INCLUDE [operator-this-fiscal-year-description](includes/operator-this-fiscal-year-description.md)]|TBD|
|[this-month](#this-month)|[!INCLUDE [operator-this-month-description](includes/operator-this-month-description.md)]|TBD|
|[this-week](#this-week)|[!INCLUDE [operator-this-week-description](includes/operator-this-week-description.md)]|TBD|
|[this-year](#this-year)|[!INCLUDE [operator-this-year-description](includes/operator-this-year-description.md)]|TBD|
|[today](#today)|[!INCLUDE [operator-today-description](includes/operator-today-description.md)]|TBD|
|[tomorrow](#tomorrow)|[!INCLUDE [operator-tomorrow-description](includes/operator-tomorrow-description.md)]|TBD|
|[under](#under)|[!INCLUDE [operator-under-description](includes/operator-under-description.md)]|[Hierarchical](#hierarchical-data)|
|[yesterday](#yesterday)|[!INCLUDE [operator-yesterday-description](includes/operator-yesterday-description.md)]|TBD|

## Details

This section includes details about each of the FetchXml condition operators.

### above
 
[!INCLUDE [operator-above-description](includes/operator-above-description.md)]

 Data Types: [Hierarchical](#hierarchical-data)

### begins-with
 
[!INCLUDE [operator-begins-with-description](includes/operator-begins-with-description.md)]

 Data Types: TBD

### between
 
[!INCLUDE [operator-between-description](includes/operator-between-description.md)]

 Data Types: TBD

### contain-values
 
[!INCLUDE [operator-contain-values-description](includes/operator-contain-values-description.md)]

 Data Types: TBD

### ends-with
 
[!INCLUDE [operator-ends-with-description](includes/operator-ends-with-description.md)]

 Data Types: TBD

### eq
 
[!INCLUDE [operator-eq-description](includes/operator-eq-description.md)]

 Data Types: TBD

### eq-businessid

[!INCLUDE [operator-eq-businessid-description](includes/operator-eq-businessid-description.md)]

 Data Types: TBD

### eq-or-above
 
[!INCLUDE [operator-eq-or-above-description](includes/operator-eq-or-above-description.md)]

 Data Types: TBD

### eq-or-under
 
[!INCLUDE [operator-eq-or-under-description](includes/operator-eq-or-under-description.md)]

 Data Types: TBD

### eq-userid
 
[!INCLUDE [operator-eq-userid-description](includes/operator-eq-userid-description.md)]

 Data Types: TBD

### eq-userlanguage
 
[!INCLUDE [operator-eq-userlanguage-description](includes/operator-eq-userlanguage-description.md)]

 Data Types: TBD

### eq-useroruserhierarchy
 
[!INCLUDE [operator-eq-useroruserhierarchy-description](includes/operator-eq-useroruserhierarchy-description.md)]

 Data Types: TBD

### eq-useroruserhierarchyandteams
 
[!INCLUDE [operator-eq-useroruserhierarchyandteams-description](includes/operator-eq-useroruserhierarchyandteams-description.md)]

 Data Types: TBD

### eq-useroruserteams
 
[!INCLUDE [operator-eq-useroruserteams-description](includes/operator-eq-useroruserteams-description.md)]

 Data Types: TBD

### eq-userteams
 
[!INCLUDE [operator-eq-userteams-description](includes/operator-eq-userteams-description.md)]

 Data Types: TBD

### ge
 
[!INCLUDE [operator-ge-description](includes/operator-ge-description.md)]

 Data Types: TBD

### gt
 
[!INCLUDE [operator-gt-description](includes/operator-gt-description.md)]

 Data Types: TBD

### in
 
[!INCLUDE [operator-in-description](includes/operator-in-description.md)]

 Data Types: TBD

### in-fiscal-period
 
[!INCLUDE [operator-in-fiscal-period-description](includes/operator-in-fiscal-period-description.md)]

 Data Types: TBD

### in-fiscal-period-and-year
 
[!INCLUDE [operator-in-fiscal-period-and-year-description](includes/operator-in-fiscal-period-and-year-description.md)]

 Data Types: TBD

### in-fiscal-year
 
[!INCLUDE [operator-in-fiscal-year-description](includes/operator-in-fiscal-year-description.md)]

 Data Types: TBD

### in-or-after-fiscal-period-and-year
 
[!INCLUDE [operator-in-or-after-fiscal-period-and-year-description](includes/operator-in-or-after-fiscal-period-and-year-description.md)]

 Data Types: TBD

### in-or-before-fiscal-period-and-year
 
[!INCLUDE [operator-in-or-before-fiscal-period-and-year-description](includes/operator-in-or-before-fiscal-period-and-year-description.md)]

 Data Types: TBD

### last-fiscal-period
 
[!INCLUDE [operator-last-fiscal-period-description](includes/operator-last-fiscal-period-description.md)]

 Data Types: TBD

### last-fiscal-year
 
[!INCLUDE [operator-last-fiscal-year-description](includes/operator-last-fiscal-year-description.md)]

 Data Types: TBD

### last-month
 
[!INCLUDE [operator-last-month-description](includes/operator-last-month-description.md)]

 Data Types: TBD

### last-seven-days
 
[!INCLUDE [operator-last-seven-days-description](includes/operator-last-seven-days-description.md)]

 Data Types: TBD

### last-week
 
[!INCLUDE [operator-last-week-description](includes/operator-last-week-description.md)]

 Data Types: TBD

### last-x-days
 
[!INCLUDE [operator-last-x-days-description](includes/operator-last-x-days-description.md)]

 Data Types: TBD

### last-x-fiscal-periods
 
[!INCLUDE [operator-last-x-fiscal-periods-description](includes/operator-last-x-fiscal-periods-description.md)]

 Data Types: TBD

### last-x-fiscal-years
 
[!INCLUDE [operator-last-x-fiscal-years-description](includes/operator-last-x-fiscal-years-description.md)]

 Data Types: TBD

### last-x-hours
 
[!INCLUDE [operator-last-x-hours-description](includes/operator-last-x-hours-description.md)]

 Data Types: TBD

### last-x-months
 
[!INCLUDE [operator-last-x-months-description](includes/operator-last-x-months-description.md)]

 Data Types: TBD

### last-x-weeks
 
[!INCLUDE [operator-last-x-weeks-description](includes/operator-last-x-weeks-description.md)]

 Data Types: TBD

### last-x-years
 
[!INCLUDE [operator-last-x-years-description](includes/operator-last-x-years-description.md)]

 Data Types: TBD

### last-year
 
[!INCLUDE [operator-last-year-description](includes/operator-last-year-description.md)]

 Data Types: TBD

### le
 
[!INCLUDE [operator-le-description](includes/operator-le-description.md)]

 Data Types: TBD

### like
 
[!INCLUDE [operator-like-description](includes/operator-like-description.md)]

 Data Types: TBD

### lt
 
[!INCLUDE [operator-lt-description](includes/operator-lt-description.md)]

 Data Types: TBD

### ne
 
[!INCLUDE [operator-ne-description](includes/operator-ne-description.md)]

 Data Types: TBD

### ne-businessid
 
[!INCLUDE [operator-ne-businessid-description](includes/operator-ne-businessid-description.md)]

 Data Types: TBD

### ne-userid
 
[!INCLUDE [operator-ne-userid-description](includes/operator-ne-userid-description.md)]

 Data Types: TBD

### neq
 
[!INCLUDE [operator-neq-description](includes/operator-neq-description.md)]

 Data Types: TBD

### next-fiscal-period
 
[!INCLUDE [operator-next-fiscal-period-description](includes/operator-next-fiscal-period-description.md)]

 Data Types: TBD

### next-fiscal-year
 
[!INCLUDE [operator-next-fiscal-year-description](includes/operator-next-fiscal-year-description.md)]

 Data Types: TBD

### next-month
 
[!INCLUDE [operator-next-month-description](includes/operator-next-month-description.md)]

 Data Types: TBD

### next-seven-days
 
[!INCLUDE [operator-next-seven-days-description](includes/operator-next-seven-days-description.md)]

 Data Types: TBD

### next-week
 
[!INCLUDE [operator-next-week-description](includes/operator-next-week-description.md)]

 Data Types: TBD

### next-x-days
 
[!INCLUDE [operator-next-x-days-description](includes/operator-next-x-days-description.md)]

 Data Types: TBD

### next-x-fiscal-periods
 
[!INCLUDE [operator-next-x-fiscal-periods-description](includes/operator-next-x-fiscal-periods-description.md)]

 Data Types: TBD

### next-x-fiscal-years
 
[!INCLUDE [operator-next-x-fiscal-years-description](includes/operator-next-x-fiscal-years-description.md)]

 Data Types: TBD

### next-x-hours
 
[!INCLUDE [operator-next-x-hours-description](includes/operator-next-x-hours-description.md)]

 Data Types: TBD

### next-x-months
 
[!INCLUDE [operator-next-x-months-description](includes/operator-next-x-months-description.md)]

 Data Types: TBD

### next-x-weeks
 
[!INCLUDE [operator-next-x-weeks-description](includes/operator-next-x-weeks-description.md)]

 Data Types: TBD

### next-x-years
 
[!INCLUDE [operator-next-x-years-description](includes/operator-next-x-years-description.md)]

 Data Types: TBD

### next-year
 
[!INCLUDE [operator-next-year-description](includes/operator-next-year-description.md)]

 Data Types: TBD

### not-begin-with
 
[!INCLUDE [operator-not-begin-with-description](includes/operator-not-begin-with-description.md)]

 Data Types: TBD

### not-between
 
[!INCLUDE [operator-not-between-description](includes/operator-not-between-description.md)]

 Data Types: TBD

### not-contain-values
 
[!INCLUDE [operator-not-contain-values-description](includes/operator-not-contain-values-description.md)]

 Data Types: TBD

### not-end-with
 
[!INCLUDE [operator-not-end-with-description](includes/operator-not-end-with-description.md)]

 Data Types: TBD

### not-in
 
[!INCLUDE [operator-not-in-description](includes/operator-not-in-description.md)]

 Data Types: TBD

### not-like
 
[!INCLUDE [operator-not-like-description](includes/operator-not-like-description.md)]

 Data Types: TBD

### not-null
 
[!INCLUDE [operator-not-null-description](includes/operator-not-null-description.md)]

 Data Types: TBD

### not-under
 
[!INCLUDE [operator-not-under-description](includes/operator-not-under-description.md)]

 Data Types: [Hierarchical](#hierarchical-data)

### null
 
[!INCLUDE [operator-null-description](includes/operator-null-description.md)]

 Data Types: TBD

### olderthan-x-days
 
[!INCLUDE [operator-olderthan-x-days-description](includes/operator-olderthan-x-days-description.md)]

 Data Types: TBD

### olderthan-x-hours
 
[!INCLUDE [operator-olderthan-x-hours-description](includes/operator-olderthan-x-hours-description.md)]

 Data Types: TBD

### olderthan-x-minutes
 
[!INCLUDE [operator-olderthan-x-minutes-description](includes/operator-olderthan-x-minutes-description.md)]

 Data Types: TBD

### olderthan-x-months
 
[!INCLUDE [operator-olderthan-x-months-description](includes/operator-olderthan-x-months-description.md)]

 Data Types: TBD

### olderthan-x-weeks
 
[!INCLUDE [operator-olderthan-x-weeks-description](includes/operator-olderthan-x-weeks-description.md)]

 Data Types: TBD

### olderthan-x-years
 
[!INCLUDE [operator-olderthan-x-years-description](includes/operator-olderthan-x-years-description.md)]

 Data Types: TBD

### on
 
[!INCLUDE [operator-on-description](includes/operator-on-description.md)]

 Data Types: TBD

### on-or-after
 
[!INCLUDE [operator-on-or-after-description](includes/operator-on-or-after-description.md)]

 Data Types: TBD

### on-or-before
 
[!INCLUDE [operator-on-or-before-description](includes/operator-on-or-before-description.md)]

 Data Types: TBD

### this-fiscal-period
 
[!INCLUDE [operator-this-fiscal-period-description](includes/operator-this-fiscal-period-description.md)]

 Data Types: TBD

### this-fiscal-year
 
[!INCLUDE [operator-this-fiscal-year-description](includes/operator-this-fiscal-year-description.md)]

 Data Types: TBD

### this-month
 
[!INCLUDE [operator-this-month-description](includes/operator-this-month-description.md)]

 Data Types: TBD

### this-week
 
[!INCLUDE [operator-this-week-description](includes/operator-this-week-description.md)]

 Data Types: TBD

### this-year
 
[!INCLUDE [operator-this-year-description](includes/operator-this-year-description.md)]

 Data Types: TBD

### today
 
[!INCLUDE [operator-today-description](includes/operator-today-description.md)]

 Data Types: TBD

### tomorrow
 
[!INCLUDE [operator-tomorrow-description](includes/operator-tomorrow-description.md)]

 Data Types: TBD

### under
 
[!INCLUDE [operator-under-description](includes/operator-under-description.md)]

 Data Types: TBD

### yesterday
 
[!INCLUDE [operator-yesterday-description](includes/operator-yesterday-description.md)]

 Data Types: TBD


## By Data type

This section groups operators by the type of data they can be used with.

 [Choice data](#choice-data)
 [Datetime data](#datetime-data)
 [Hierarchical data](#hierarchical-data)
 [Number data](#number-data)
 [Owner data](#owner-data)
 [String data](#string-data)
 [Unique Identifier data](#unique-identifier-data)

### Choice data

Use the following operators in [conditions](condition.md) using choice values.

|Operator|Description|
|---|---|
|[contain-values](#contain-values)|[!INCLUDE [operator-contain-values-description](includes/operator-contain-values-description.md)]|
|[eq](#eq)|[!INCLUDE [operator-eq-description](includes/operator-eq-description.md)]|
|[ne](#ne)|[!INCLUDE [operator-ne-description](includes/operator-ne-description.md)]|
|[not-contain-values](#not-contain-values)|[!INCLUDE [operator-not-contain-values-description](includes/operator-not-contain-values-description.md)]|
|[not-null](#not-null)|[!INCLUDE [operator-not-null-description](includes/operator-not-null-description.md)]|
|[null](#null)|[!INCLUDE [operator-null-description](includes/operator-null-description.md)]|


### Datetime data

 Use the following operators in [conditions](condition.md) using date and time values.

 |Operator|Description|
 |---|---|
 |[eq](#eq)|[!INCLUDE [operator-eq-description](includes/operator-eq-description.md)]|
 |[in-fiscal-period-and-year](#in-fiscal-period-and-year)|[!INCLUDE [operator-in-fiscal-period-and-year-description](includes/operator-in-fiscal-period-and-year-description.md)]|
 |[in-fiscal-period](#in-fiscal-period)|[!INCLUDE [operator-in-fiscal-period-description](includes/operator-in-fiscal-period-description.md)]|
 |[in-fiscal-year](#in-fiscal-year)|[!INCLUDE [operator-in-fiscal-year-description](includes/operator-in-fiscal-year-description.md)]|
 |[in-or-after-fiscal-period-and-year](#in-or-after-fiscal-period-and-year)|[!INCLUDE [operator-in-or-after-fiscal-period-and-year-description](includes/operator-in-or-after-fiscal-period-and-year-description.md)]|
 |[in-or-before-fiscal-period-and-year](#in-or-before-fiscal-period-and-year)|[!INCLUDE [operator-in-or-before-fiscal-period-and-year-description](includes/operator-in-or-before-fiscal-period-and-year-description.md)]|
 |[last-fiscal-period](#last-fiscal-period)|[!INCLUDE [operator-last-fiscal-period-description](includes/operator-last-fiscal-period-description.md)]|
 |[last-fiscal-year](#last-fiscal-year)|[!INCLUDE [operator-last-fiscal-year-description](includes/operator-last-fiscal-year-description.md)]|
 |[last-month](#last-month)|[!INCLUDE [operator-last-month-description](includes/operator-last-month-description.md)]|
 |[last-seven-days](#last-seven-days)|[!INCLUDE [operator-last-seven-days-description](includes/operator-last-seven-days-description.md)]|
 |[last-week](#last-week)|[!INCLUDE [operator-last-week-description](includes/operator-last-week-description.md)]|
 |[last-x-days](#last-x-days)|[!INCLUDE [operator-last-x-days-description](includes/operator-last-x-days-description.md)]|
 |[last-x-fiscal-periods](#last-x-fiscal-periods)|[!INCLUDE [operator-last-x-fiscal-periods-description](includes/operator-last-x-fiscal-periods-description.md)]|
 |[last-x-fiscal-periods](#last-x-fiscal-periods)|[!INCLUDE [operator-last-x-fiscal-periods-description](includes/operator-last-x-fiscal-periods-description.md)]|
 |[last-x-hours](#last-x-hours)|[!INCLUDE [operator-last-x-hours-description](includes/operator-last-x-hours-description.md)]|
 |[last-x-hours](#last-x-hours)|[!INCLUDE [operator-last-x-hours-description](includes/operator-last-x-hours-description.md)]|
 |[last-x-weeks](#last-x-weeks)|[!INCLUDE [operator-last-x-weeks-description](includes/operator-last-x-weeks-description.md)]|
 |[last-x-years](#last-x-years)|[!INCLUDE [operator-last-x-years-description](includes/operator-last-x-years-description.md)]|
 |[last-year](#last-year)|[!INCLUDE [operator-last-year-description](includes/operator-last-year-description.md)]|
 |[le](#le)|[!INCLUDE [operator-le-description](includes/operator-le-description.md)]|
 |[next-fiscal-period](#next-fiscal-period)|[!INCLUDE [operator-next-fiscal-period-description](includes/operator-next-fiscal-period-description.md)]|
 |[next-fiscal-year](#next-fiscal-year)|[!INCLUDE [operator-next-fiscal-year-description](includes/operator-next-fiscal-year-description.md)]|
 |[next-month](#next-month)|[!INCLUDE [operator-next-month-description](includes/operator-next-month-description.md)]|
 |[next-seven-days](#next-seven-days)|[!INCLUDE [operator-next-seven-days-description](includes/operator-next-seven-days-description.md)]|
 |[next-week](#next-week)|[!INCLUDE [operator-next-week-description](includes/operator-next-week-description.md)]|
 |[next-x-days](#next-x-days)|[!INCLUDE [operator-next-x-days-description](includes/operator-next-x-days-description.md)]|
 |[next-x-fiscal-periods](#next-x-fiscal-periods)|[!INCLUDE [operator-next-x-fiscal-periods-description](includes/operator-next-x-fiscal-periods-description.md)]|
 |[next-x-fiscal-years](#next-x-fiscal-years)|[!INCLUDE [operator-next-x-fiscal-years-description](includes/operator-next-x-fiscal-years-description.md)]|
 |[next-x-hours](#next-x-hours)|[!INCLUDE [operator-next-x-hours-description](includes/operator-next-x-hours-description.md)]|
 |[next-x-months](#next-x-months)|[!INCLUDE [operator-next-x-months-description](includes/operator-next-x-months-description.md)]|
 |[next-x-weeks](#next-x-weeks)|[!INCLUDE [operator-next-x-weeks-description](includes/operator-next-x-weeks-description.md)]|
 |[next-x-years](#next-x-years)|[!INCLUDE [operator-next-x-years-description](includes/operator-next-x-years-description.md)]|
 |[next-year](#next-year)|[!INCLUDE [operator-next-year-description](includes/operator-next-year-description.md)]|
 |[not-null](#not-null)|[!INCLUDE [operator-not-null-description](includes/operator-not-null-description.md)]|
 |[null](#null)|[!INCLUDE [operator-null-description](includes/operator-null-description.md)]|
 |[olderthan-x-days](#olderthan-x-days)|[!INCLUDE [operator-olderthan-x-days-description](includes/operator-olderthan-x-days-description.md)]|
 |[olderthan-x-hours](#olderthan-x-hours)|[!INCLUDE [operator-olderthan-x-hours-description](includes/operator-olderthan-x-hours-description.md)]|
 |[olderthan-x-minutes](#olderthan-x-minutes)|[!INCLUDE [operator-olderthan-x-minutes-description](includes/operator-olderthan-x-minutes-description.md)]|
 |[olderthan-x-months](#olderthan-x-months)|[!INCLUDE [operator-olderthan-x-months-description](includes/operator-olderthan-x-months-description.md)]|
 |[olderthan-x-months](#olderthan-x-months)|[!INCLUDE [operator-olderthan-x-months-description](includes/operator-olderthan-x-months-description.md)]|
 |[olderthan-x-years](#olderthan-x-years)|[!INCLUDE [operator-olderthan-x-years-description](includes/operator-olderthan-x-years-description.md)]|
 |[on-or-after](#on-or-after)|[!INCLUDE [operator-on-or-after-description](includes/operator-on-or-after-description.md)]|
 |[on-or-before](#on-or-before)|[!INCLUDE [operator-on-or-before-description](includes/operator-on-or-before-description.md)]|
 |[on](#on)|[!INCLUDE [operator-on-description](includes/operator-on-description.md)]|
 |[this-fiscal-period](#this-fiscal-period)|[!INCLUDE [operator-this-fiscal-period-description](includes/operator-this-fiscal-period-description.md)]|
 |[this-fiscal-year](#this-fiscal-year)|[!INCLUDE [operator-this-fiscal-year-description](includes/operator-this-fiscal-year-description.md)]|
 |[this-month](#this-month)|[!INCLUDE [operator-this-month-description](includes/operator-this-month-description.md)]|
 |[this-week](#this-week)|[!INCLUDE [operator-this-week-description](includes/operator-this-week-description.md)]|
 |[this-year](#this-year)|[!INCLUDE [operator-this-year-description](includes/operator-this-year-description.md)]|
 |[today](#today)|[!INCLUDE [operator-today-description](includes/operator-today-description.md)]|
 |[tomorrow](#tomorrow)|[!INCLUDE [operator-tomorrow-description](includes/operator-tomorrow-description.md)]|
 |[yesterday](#yesterday)|[!INCLUDE [operator-yesterday-description](includes/operator-yesterday-description.md)]|


### Hierarchical data

Use the following operators in [conditions](condition.md) using hierarchical data. [Learn more about querying hierarchical data](../../query-hierarchical-data.md).

|Operator|Description|
|---|---|
|[above](#above)|[!INCLUDE [operator-above-description](includes/operator-above-description.md)]|
|[eq-or-above](#eq-or-above)|[!INCLUDE [operator-eq-or-above-description](includes/operator-eq-or-above-description.md)]|
|[eq-or-under](#eq-or-under)|[!INCLUDE [operator-eq-or-under-description](includes/operator-eq-or-under-description.md)]|
|[eq-useroruserhierarchy](#eq-useroruserhierarchy)|[!INCLUDE [operator-eq-useroruserhierarchy-description](includes/operator-eq-useroruserhierarchy-description.md)]|
|[eq-useroruserhierarchyandteams](#eq-useroruserhierarchyandteams)|[!INCLUDE [operator-eq-useroruserhierarchyandteams-description](includes/operator-eq-useroruserhierarchyandteams-description.md)]|
|[not-under](#not-under)|[!INCLUDE [operator-not-under-description](includes/operator-not-under-description.md)]|
|[under](#under)|[!INCLUDE [operator-under-description](includes/operator-under-description.md)]|

### Number data

Use the following operators in [conditions](condition.md) using numeric values.

|Operator|Description|
|---|---|
|[between](#between)|[!INCLUDE [operator-between-description](includes/operator-between-description.md)]|
|[eq-userlanguage](#eq-userlanguage)|[!INCLUDE [operator-eq-userlanguage-description](includes/operator-eq-userlanguage-description.md)]|
|[eq](#eq)|[!INCLUDE [operator-eq-description](includes/operator-eq-description.md)]|
|[ge](#ge)|[!INCLUDE [operator-ge-description](includes/operator-ge-description.md)]|
|[gt](#gt)|[!INCLUDE [operator-gt-description](includes/operator-gt-description.md)]|
|[in](#in)|[!INCLUDE [operator-in-description](includes/operator-in-description.md)]|
|[le](#le)|[!INCLUDE [operator-le-description](includes/operator-le-description.md)]|
|[lt](#lt)|[!INCLUDE [operator-lt-description](includes/operator-lt-description.md)]|
|[ne](#ne)|[!INCLUDE [operator-ne-description](includes/operator-ne-description.md)]|
|[not-between](#not-between)|[!INCLUDE [operator-not-between-description](includes/operator-not-between-description.md)]|
|[not-in](#not-in)|[!INCLUDE [operator-not-in-description](includes/operator-not-in-description.md)]|
|[not-null](#not-null)|[!INCLUDE [operator-not-null-description](includes/operator-not-null-description.md)]|
|[null](#null)|[!INCLUDE [operator-null-description](includes/operator-null-description.md)]|

### Owner data

Use the following operators in [conditions](condition.md) using owner values.

|Operator|Description|
|---|---|
|[eq-useroruserteams](#eq-useroruserteams)|[!INCLUDE [operator-eq-useroruserteams-description](includes/operator-eq-useroruserteams-description.md)]|
|[eq-userteams](#00)|[!INCLUDE [operator-eq-userteams-description](includes/operator-eq-userteams-description.md)]|
|[eq](#eq)|[!INCLUDE [operator-eq-description](includes/operator-eq-description.md)]|
|[ne](#ne)|[!INCLUDE [operator-ne-description](includes/operator-ne-description.md)]|

### String data

Use the following operators in [conditions](condition.md) using string values.

|Operator|Description|
|---|---|
|[begins-with](#begins-with)|[!INCLUDE [operator-begins-with-description](includes/operator-begins-with-description.md)]|
|[ends-with](#ends-with)|[!INCLUDE [operator-ends-with-description](includes/operator-ends-with-description.md)]|
|[eq](#eq)|[!INCLUDE [operator-eq-description](includes/operator-eq-description.md)]|
|[like](#like)|[!INCLUDE [operator-like-description](includes/operator-like-description.md)]|
|[ne](#ne)|[!INCLUDE [operator-ne-description](includes/operator-ne-description.md)]|
|[not-begin-with](#not-begin-with)|[!INCLUDE [operator-not-begin-with-description](includes/operator-not-begin-with-description.md)]|
|[not-end-with](#not-end-with)|[!INCLUDE [operator-not-end-with-description](includes/operator-not-end-with-description.md)]|
|[not-like](#not-like)|[!INCLUDE [operator-not-like-description](includes/operator-not-like-description.md)]|
|[not-null](#not-null)|[!INCLUDE [operator-not-null-description](includes/operator-not-null-description.md)]|
|[null](#null)|[!INCLUDE [operator-null-description](includes/operator-null-description.md)]|


### Unique Identifier data

Use the following operators in [conditions](condition.md) using unique identifier (GUID) values.

|Operator|Description|
|---|---|
|[eq-businessid](#eq-businessid)|[!INCLUDE [operator-eq-businessid-description](includes/operator-eq-businessid-description.md)]|
|[eq-userid](#eq-userid)|[!INCLUDE [operator-eq-userid-description](includes/operator-eq-userid-description.md)]|
|[eq](#eq)|[!INCLUDE [operator-eq-description](includes/operator-eq-description.md)]|
|[ne-businessid](#ne-businessid)|[!INCLUDE [operator-ne-businessid-description](includes/operator-ne-businessid-description.md)]|
|[ne-userid](#ne-userid)|[!INCLUDE [operator-ne-userid-description](includes/operator-ne-userid-description.md)]|
|[ne](#ne)|[!INCLUDE [operator-ne-description](includes/operator-ne-description.md)]|
|[not-null](#not-null)|[!INCLUDE [operator-not-null-description](includes/operator-not-null-description.md)]|
|[null](#null)|[!INCLUDE [operator-null-description](includes/operator-null-description.md)]|



[!INCLUDE [footer-banner](../../../../includes/footer-banner.md)]
