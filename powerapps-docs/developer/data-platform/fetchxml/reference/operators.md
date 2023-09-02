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
|[begins-with](#begins-with)|[!INCLUDE [operator-begins-with-description](includes/operator-begins-with-description.md)]|[String](#string-data)|
|[between](#between)|[!INCLUDE [operator-between-description](includes/operator-between-description.md)]|[Number](#number-data)<br />[Datetime](#datetime-data)|
|[contain-values](#contain-values)|[!INCLUDE [operator-contain-values-description](includes/operator-contain-values-description.md)]|[Choice](#choice-data)|
|[ends-with](#ends-with)|[!INCLUDE [operator-ends-with-description](includes/operator-ends-with-description.md)]|[String](#string-data)|
|[eq](#eq)|[!INCLUDE [operator-eq-description](includes/operator-eq-description.md)]|[Choice](#choice-data)<br />[Datetime](#datetime-data)<br />[Hierarchical](#hierarchical-data)<br />[Number](#number-data)<br />[Owner](#owner-data)<br />[String](#string-data)<br />[Unique Identifier](#unique-identifier-data)|
|[eq-businessid](#eq-businessid)|[!INCLUDE [operator-eq-businessid-description](includes/operator-eq-businessid-description.md)]|[Unique Identifier](#unique-identifier-data)|
|[eq-or-above](#eq-or-above)|[!INCLUDE [operator-eq-or-above-description](includes/operator-eq-or-above-description.md)]|[Hierarchical](#hierarchical-data)|
|[eq-or-under](#eq-or-under)|[!INCLUDE [operator-eq-or-under-description](includes/operator-eq-or-under-description.md)]|[Hierarchical](#hierarchical-data)|
|[eq-userid](#eq-userid)|[!INCLUDE [operator-eq-userid-description](includes/operator-eq-userid-description.md)]|[Unique Identifier](#unique-identifier-data)|
|[eq-userlanguage](#eq-userlanguage)|[!INCLUDE [operator-eq-userlanguage-description](includes/operator-eq-userlanguage-description.md)]|[Number](#number-data)|
|[eq-useroruserhierarchy](#eq-useroruserhierarchy)|[!INCLUDE [operator-eq-useroruserhierarchy-description](includes/operator-eq-useroruserhierarchy-description.md)]|[Hierarchical](#hierarchical-data)|
|[eq-useroruserhierarchyandteams](#eq-useroruserhierarchyandteams)|[!INCLUDE [operator-eq-useroruserhierarchyandteams-description](includes/operator-eq-useroruserhierarchyandteams-description.md)]|[Hierarchical](#hierarchical-data)|
|[eq-useroruserteams](#eq-useroruserteams)|[!INCLUDE [operator-eq-useroruserteams-description](includes/operator-eq-useroruserteams-description.md)]|[Owner](#owner-data)|
|[eq-userteams](#eq-userteams)|[!INCLUDE [operator-eq-userteams-description](includes/operator-eq-userteams-description.md)]|[Owner](#owner-data)|
|[ge](#ge)|[!INCLUDE [operator-ge-description](includes/operator-ge-description.md)]|[Number](#number-data)<br />[Datetime](#datetime-data)|
|[gt](#gt)|[!INCLUDE [operator-gt-description](includes/operator-gt-description.md)]|[Number](#number-data)<br />[Datetime](#datetime-data)|
|[in](#in)|[!INCLUDE [operator-in-description](includes/operator-in-description.md)]|[Number](#number-data)|
|[in-fiscal-period](#in-fiscal-period)|[!INCLUDE [operator-in-fiscal-period-description](includes/operator-in-fiscal-period-description.md)]|[Datetime](#datetime-data)|
|[in-fiscal-period-and-year](#in-fiscal-period-and-year)|[!INCLUDE [operator-in-fiscal-period-and-year-description](includes/operator-in-fiscal-period-and-year-description.md)]|[Datetime](#datetime-data)|
|[in-fiscal-year](#in-fiscal-year)|[!INCLUDE [operator-in-fiscal-year-description](includes/operator-in-fiscal-year-description.md)]|[Datetime](#datetime-data)|
|[in-or-after-fiscal-period-and-year](#in-or-after-fiscal-period-and-year)|[!INCLUDE [operator-in-or-after-fiscal-period-and-year-description](includes/operator-in-or-after-fiscal-period-and-year-description.md)]|[Datetime](#datetime-data)|
|[in-or-before-fiscal-period-and-year](#in-or-before-fiscal-period-and-year)|[!INCLUDE [operator-in-or-before-fiscal-period-and-year-description](includes/operator-in-or-before-fiscal-period-and-year-description.md)]|[Datetime](#datetime-data)|
|[last-fiscal-period](#last-fiscal-period)|[!INCLUDE [operator-last-fiscal-period-description](includes/operator-last-fiscal-period-description.md)]|[Datetime](#datetime-data)|
|[last-fiscal-year](#last-fiscal-year)|[!INCLUDE [operator-last-fiscal-year-description](includes/operator-last-fiscal-year-description.md)]|[Datetime](#datetime-data)|
|[last-month](#last-month)|[!INCLUDE [operator-last-month-description](includes/operator-last-month-description.md)]|[Datetime](#datetime-data)|
|[last-seven-days](#last-seven-days)|[!INCLUDE [operator-last-seven-days-description](includes/operator-last-seven-days-description.md)]|[Datetime](#datetime-data)|
|[last-week](#last-week)|[!INCLUDE [operator-last-week-description](includes/operator-last-week-description.md)]|[Datetime](#datetime-data)|
|[last-x-days](#last-x-days)|[!INCLUDE [operator-last-x-days-description](includes/operator-last-x-days-description.md)]|[Datetime](#datetime-data)|
|[last-x-fiscal-periods](#last-x-fiscal-periods)|[!INCLUDE [operator-last-x-fiscal-periods-description](includes/operator-last-x-fiscal-periods-description.md)]|[Datetime](#datetime-data)|
|[last-x-fiscal-years](#last-x-fiscal-years)|[!INCLUDE [operator-last-x-fiscal-years-description](includes/operator-last-x-fiscal-years-description.md)]|[Datetime](#datetime-data)|
|[last-x-hours](#last-x-hours)|[!INCLUDE [operator-last-x-hours-description](includes/operator-last-x-hours-description.md)]|[Datetime](#datetime-data)|
|[last-x-months](#last-x-months)|[!INCLUDE [operator-last-x-months-description](includes/operator-last-x-months-description.md)]|[Datetime](#datetime-data)|
|[last-x-weeks](#last-x-weeks)|[!INCLUDE [operator-last-x-weeks-description](includes/operator-last-x-weeks-description.md)]|[Datetime](#datetime-data)|
|[last-x-years](#last-x-years)|[!INCLUDE [operator-last-x-years-description](includes/operator-last-x-years-description.md)]|[Datetime](#datetime-data)|
|[last-year](#last-year)|[!INCLUDE [operator-last-year-description](includes/operator-last-year-description.md)]|[Datetime](#datetime-data)|
|[le](#le)|[!INCLUDE [operator-le-description](includes/operator-le-description.md)]|[Number](#number-data)<br />[Datetime](#datetime-data)|
|[like](#like)|[!INCLUDE [operator-like-description](includes/operator-like-description.md)]|[String](#string-data)|
|[lt](#lt)|[!INCLUDE [operator-lt-description](includes/operator-lt-description.md)]|[Number](#number-data)<br />[Datetime](#datetime-data)|
|[ne](#ne)|[!INCLUDE [operator-ne-description](includes/operator-ne-description.md)]|[Choice](#choice-data)<br />[Datetime](#datetime-data)<br />[Hierarchical](#hierarchical-data)<br />[Number](#number-data)<br />[Owner](#owner-data)<br />[String](#string-data)<br />[Unique Identifier](#unique-identifier-data)|
|[ne-businessid](#ne-businessid)|[!INCLUDE [operator-ne-businessid-description](includes/operator-ne-businessid-description.md)]|[Unique Identifier](#unique-identifier-data)|
|[ne-userid](#ne-userid)|[!INCLUDE [operator-ne-userid-description](includes/operator-ne-userid-description.md)]|[Unique Identifier](#unique-identifier-data)|
|[neq](#neq)|[!INCLUDE [operator-neq-description](includes/operator-neq-description.md)]|N/A|
|[next-fiscal-period](#next-fiscal-period)|[!INCLUDE [operator-next-fiscal-period-description](includes/operator-next-fiscal-period-description.md)]|[Datetime](#datetime-data)|
|[next-fiscal-year](#next-fiscal-year)|[!INCLUDE [operator-next-fiscal-year-description](includes/operator-next-fiscal-year-description.md)]|[Datetime](#datetime-data)|
|[next-month](#next-month)|[!INCLUDE [operator-next-month-description](includes/operator-next-month-description.md)]|[Datetime](#datetime-data)|
|[next-seven-days](#next-seven-days)|[!INCLUDE [operator-next-seven-days-description](includes/operator-next-seven-days-description.md)]|[Datetime](#datetime-data)|
|[next-week](#next-week)|[!INCLUDE [operator-next-week-description](includes/operator-next-week-description.md)]|[Datetime](#datetime-data)|
|[next-x-days](#next-x-days)|[!INCLUDE [operator-next-x-days-description](includes/operator-next-x-days-description.md)]|[Datetime](#datetime-data)|
|[next-x-fiscal-periods](#next-x-fiscal-periods)|[!INCLUDE [operator-next-x-fiscal-periods-description](includes/operator-next-x-fiscal-periods-description.md)]|[Datetime](#datetime-data)|
|[next-x-fiscal-years](#next-x-fiscal-years)|[!INCLUDE [operator-next-x-fiscal-years-description](includes/operator-next-x-fiscal-years-description.md)]|[Datetime](#datetime-data)|
|[next-x-hours](#next-x-hours)|[!INCLUDE [operator-next-x-hours-description](includes/operator-next-x-hours-description.md)]|[Datetime](#datetime-data)|
|[next-x-months](#next-x-months)|[!INCLUDE [operator-next-x-months-description](includes/operator-next-x-months-description.md)]|[Datetime](#datetime-data)|
|[next-x-weeks](#next-x-weeks)|[!INCLUDE [operator-next-x-weeks-description](includes/operator-next-x-weeks-description.md)]|[Datetime](#datetime-data)|
|[next-x-years](#next-x-years)|[!INCLUDE [operator-next-x-years-description](includes/operator-next-x-years-description.md)]|[Datetime](#datetime-data)|
|[next-year](#next-year)|[!INCLUDE [operator-next-year-description](includes/operator-next-year-description.md)]|[Datetime](#datetime-data)|
|[not-begin-with](#not-begin-with)|[!INCLUDE [operator-not-begin-with-description](includes/operator-not-begin-with-description.md)]|[String](#string-data)|
|[not-between](#not-between)|[!INCLUDE [operator-not-between-description](includes/operator-not-between-description.md)]|[Number](#number-data)<br />[Datetime](#datetime-data)|
|[not-contain-values](#not-contain-values)|[!INCLUDE [operator-not-contain-values-description](includes/operator-not-contain-values-description.md)]|[Choice](#choice-data)|
|[not-end-with](#not-end-with)|[!INCLUDE [operator-not-end-with-description](includes/operator-not-end-with-description.md)]|[String](#string-data)|
|[not-in](#not-in)|[!INCLUDE [operator-not-in-description](includes/operator-not-in-description.md)]|[Number](#number-data)|
|[not-like](#not-like)|[!INCLUDE [operator-not-like-description](includes/operator-not-like-description.md)]|[String](#string-data)|
|[not-null](#not-null)|[!INCLUDE [operator-not-null-description](includes/operator-not-null-description.md)]|[Choice](#choice-data)<br />[Datetime](#datetime-data)<br />[Hierarchical](#hierarchical-data)<br />[Number](#number-data)<br />[Owner](#owner-data)<br />[String](#string-data)<br />[Unique Identifier](#unique-identifier-data)|
|[not-under](#not-under)|[!INCLUDE [operator-not-under-description](includes/operator-not-under-description.md)]|[Hierarchical](#hierarchical-data)|
|[null](#null)|[!INCLUDE [operator-null-description](includes/operator-null-description.md)]|[Choice](#choice-data)<br />[Datetime](#datetime-data)<br />[Hierarchical](#hierarchical-data)<br />[Number](#number-data)<br />[Owner](#owner-data)<br />[String](#string-data)<br />[Unique Identifier](#unique-identifier-data)|
|[olderthan-x-days](#olderthan-x-days)|[!INCLUDE [operator-olderthan-x-days-description](includes/operator-olderthan-x-days-description.md)]|[Datetime](#datetime-data)|
|[olderthan-x-hours](#olderthan-x-hours)|[!INCLUDE [operator-olderthan-x-hours-description](includes/operator-olderthan-x-hours-description.md)]|[Datetime](#datetime-data)|
|[olderthan-x-minutes](#olderthan-x-minutes)|[!INCLUDE [operator-olderthan-x-minutes-description](includes/operator-olderthan-x-minutes-description.md)]|[Datetime](#datetime-data)|
|[olderthan-x-months](#olderthan-x-months)|[!INCLUDE [operator-olderthan-x-months-description](includes/operator-olderthan-x-months-description.md)]|[Datetime](#datetime-data)|
|[olderthan-x-weeks](#olderthan-x-weeks)|[!INCLUDE [operator-olderthan-x-weeks-description](includes/operator-olderthan-x-weeks-description.md)]|[Datetime](#datetime-data)|
|[olderthan-x-years](#olderthan-x-years)|[!INCLUDE [operator-olderthan-x-years-description](includes/operator-olderthan-x-years-description.md)]|[Datetime](#datetime-data)|
|[on](#on)|[!INCLUDE [operator-on-description](includes/operator-on-description.md)]|[Datetime](#datetime-data)|
|[on-or-after](#on-or-after)|[!INCLUDE [operator-on-or-after-description](includes/operator-on-or-after-description.md)]|[Datetime](#datetime-data)|
|[on-or-before](#on-or-before)|[!INCLUDE [operator-on-or-before-description](includes/operator-on-or-before-description.md)]|[Datetime](#datetime-data)|
|[this-fiscal-period](#this-fiscal-period)|[!INCLUDE [operator-this-fiscal-period-description](includes/operator-this-fiscal-period-description.md)]|[Datetime](#datetime-data)|
|[this-fiscal-year](#this-fiscal-year)|[!INCLUDE [operator-this-fiscal-year-description](includes/operator-this-fiscal-year-description.md)]|[Datetime](#datetime-data)|
|[this-month](#this-month)|[!INCLUDE [operator-this-month-description](includes/operator-this-month-description.md)]|[Datetime](#datetime-data)|
|[this-week](#this-week)|[!INCLUDE [operator-this-week-description](includes/operator-this-week-description.md)]|[Datetime](#datetime-data)|
|[this-year](#this-year)|[!INCLUDE [operator-this-year-description](includes/operator-this-year-description.md)]|[Datetime](#datetime-data)|
|[today](#today)|[!INCLUDE [operator-today-description](includes/operator-today-description.md)]|[Datetime](#datetime-data)|
|[tomorrow](#tomorrow)|[!INCLUDE [operator-tomorrow-description](includes/operator-tomorrow-description.md)]|[Datetime](#datetime-data)|
|[under](#under)|[!INCLUDE [operator-under-description](includes/operator-under-description.md)]|[Hierarchical](#hierarchical-data)|
|[yesterday](#yesterday)|[!INCLUDE [operator-yesterday-description](includes/operator-yesterday-description.md)]|[Datetime](#datetime-data)|


## By Data type

This section groups operators by the type of data they can be used with.

- [Choice data](#choice-data)
- [Datetime data](#datetime-data)
- [Hierarchical data](#hierarchical-data)
- [Number data](#number-data)
- [Owner data](#owner-data)
- [String data](#string-data)
- [Unique Identifier data](#unique-identifier-data)

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
 |[between](#eq)|[!INCLUDE [operator-between-description](includes/operator-between-description.md)]|
 |[eq](#eq)|[!INCLUDE [operator-eq-description](includes/operator-eq-description.md)]|
 |[gt](#eq)|[!INCLUDE [operator-gt-description](includes/operator-gt-description.md)]|
 |[ge](#eq)|[!INCLUDE [operator-ge-description](includes/operator-ge-description.md)]|
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
 |[lt](#lt)|[!INCLUDE [operator-lt-description](includes/operator-lt-description.md)]|
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
 |[not-between](#not-between)|[!INCLUDE [operator-not-between-description](includes/operator-not-between-description.md)]|
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
|[eq-userteams](#eq-userteams)|[!INCLUDE [operator-eq-userteams-description](includes/operator-eq-userteams-description.md)]|
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

## Details

This section includes details about each of the FetchXml condition operators.

<!-- We can put examples here as needed. I added a couple... -->

### above
 
[!INCLUDE [operator-above-description](includes/operator-above-description.md)]

Data Type: [Hierarchical](#hierarchical-data)

### begins-with
 
[!INCLUDE [operator-begins-with-description](includes/operator-begins-with-description.md)]

Data Type: [String](#string-data)

### between
 
[!INCLUDE [operator-between-description](includes/operator-between-description.md)]

This operator requires two values.

```xml
<condition attribute="numberofemployees" operator="between">
  <value>6</value>
  <value>20</value>
</condition>
```

Data Types: 

- [Number](#number-data)
- [Datetime](#datetime-data)

### contain-values
 
[!INCLUDE [operator-contain-values-description](includes/operator-contain-values-description.md)]

Data Type: [Choice](#choice-data)

### ends-with
 
[!INCLUDE [operator-ends-with-description](includes/operator-ends-with-description.md)]

Data Type: [String](#string-data)

### eq
 
[!INCLUDE [operator-eq-description](includes/operator-eq-description.md)]

 Data Types:

- [Choice](#choice-data)
- [Datetime](#datetime-data)
- [Hierarchical](#hierarchical-data)
- [Number](#number-data)
- [Owner](#owner-data)
- [String](#string-data)
- [Unique Identifier](#unique-identifier-data)

### eq-businessid

[!INCLUDE [operator-eq-businessid-description](includes/operator-eq-businessid-description.md)]

Data Type: [Unique Identifier](#unique-identifier-data)

### eq-or-above
 
[!INCLUDE [operator-eq-or-above-description](includes/operator-eq-or-above-description.md)]

Data Type: [Hierarchical](#hierarchical-data)

### eq-or-under
 
[!INCLUDE [operator-eq-or-under-description](includes/operator-eq-or-under-description.md)]

Data Type: [Hierarchical](#hierarchical-data)

### eq-userid
 
[!INCLUDE [operator-eq-userid-description](includes/operator-eq-userid-description.md)]

No value is required for this operator.

```xml
<condition attribute='ownerid' operator='eq-userid' />
```

Data Type: [Unique Identifier](#unique-identifier-data)

### eq-userlanguage
 
[!INCLUDE [operator-eq-userlanguage-description](includes/operator-eq-userlanguage-description.md)]

Data Type: [Number](#number-data)

### eq-useroruserhierarchy
 
[!INCLUDE [operator-eq-useroruserhierarchy-description](includes/operator-eq-useroruserhierarchy-description.md)]

Data Type: [Hierarchical](#hierarchical-data)

### eq-useroruserhierarchyandteams
 
[!INCLUDE [operator-eq-useroruserhierarchyandteams-description](includes/operator-eq-useroruserhierarchyandteams-description.md)]

Data Type: [Hierarchical](#hierarchical-data)

### eq-useroruserteams
 
[!INCLUDE [operator-eq-useroruserteams-description](includes/operator-eq-useroruserteams-description.md)]

Data Type: [Owner](#owner-data)

### eq-userteams
 
[!INCLUDE [operator-eq-userteams-description](includes/operator-eq-userteams-description.md)]

Data Type: [Owner](#owner-data)

### ge
 
[!INCLUDE [operator-ge-description](includes/operator-ge-description.md)]

Data Types: 

- [Number](#number-data)
- [Datetime](#datetime-data)

### gt
 
[!INCLUDE [operator-gt-description](includes/operator-gt-description.md)]

Data Types: 

- [Number](#number-data)
- [Datetime](#datetime-data)

### in
 
[!INCLUDE [operator-in-description](includes/operator-in-description.md)]

Data Type: [Number](#number-data)

### in-fiscal-period
 
[!INCLUDE [operator-in-fiscal-period-description](includes/operator-in-fiscal-period-description.md)]

Data Type: [Datetime](#datetime-data)

### in-fiscal-period-and-year
 
[!INCLUDE [operator-in-fiscal-period-and-year-description](includes/operator-in-fiscal-period-and-year-description.md)]

Data Type: [Datetime](#datetime-data)

### in-fiscal-year
 
[!INCLUDE [operator-in-fiscal-year-description](includes/operator-in-fiscal-year-description.md)]

Data Type: [Datetime](#datetime-data)

### in-or-after-fiscal-period-and-year
 
[!INCLUDE [operator-in-or-after-fiscal-period-and-year-description](includes/operator-in-or-after-fiscal-period-and-year-description.md)]

Data Type: [Datetime](#datetime-data)

### in-or-before-fiscal-period-and-year
 
[!INCLUDE [operator-in-or-before-fiscal-period-and-year-description](includes/operator-in-or-before-fiscal-period-and-year-description.md)]

Data Type: [Datetime](#datetime-data)

### last-fiscal-period
 
[!INCLUDE [operator-last-fiscal-period-description](includes/operator-last-fiscal-period-description.md)]

Data Type: [Datetime](#datetime-data)

### last-fiscal-year
 
[!INCLUDE [operator-last-fiscal-year-description](includes/operator-last-fiscal-year-description.md)]

Data Type: [Datetime](#datetime-data)

### last-month
 
[!INCLUDE [operator-last-month-description](includes/operator-last-month-description.md)]

Data Type: [Datetime](#datetime-data)

### last-seven-days
 
[!INCLUDE [operator-last-seven-days-description](includes/operator-last-seven-days-description.md)]

Data Type: [Datetime](#datetime-data)

### last-week
 
[!INCLUDE [operator-last-week-description](includes/operator-last-week-description.md)]

Data Type: [Datetime](#datetime-data)

### last-x-days
 
[!INCLUDE [operator-last-x-days-description](includes/operator-last-x-days-description.md)]

Data Type: [Datetime](#datetime-data)

### last-x-fiscal-periods
 
[!INCLUDE [operator-last-x-fiscal-periods-description](includes/operator-last-x-fiscal-periods-description.md)]

Data Type: [Datetime](#datetime-data)

### last-x-fiscal-years
 
[!INCLUDE [operator-last-x-fiscal-years-description](includes/operator-last-x-fiscal-years-description.md)]

Data Type: [Datetime](#datetime-data)

### last-x-hours
 
[!INCLUDE [operator-last-x-hours-description](includes/operator-last-x-hours-description.md)]

Data Type: [Datetime](#datetime-data)

### last-x-months
 
[!INCLUDE [operator-last-x-months-description](includes/operator-last-x-months-description.md)]

Data Type: [Datetime](#datetime-data)

### last-x-weeks
 
[!INCLUDE [operator-last-x-weeks-description](includes/operator-last-x-weeks-description.md)]

Data Type: [Datetime](#datetime-data)

### last-x-years
 
[!INCLUDE [operator-last-x-years-description](includes/operator-last-x-years-description.md)]

Data Type: [Datetime](#datetime-data)

### last-year
 
[!INCLUDE [operator-last-year-description](includes/operator-last-year-description.md)]

Data Type: [Datetime](#datetime-data)

### le
 
[!INCLUDE [operator-le-description](includes/operator-le-description.md)]

Data Types:

- [Number](#number-data)
- [Datetime](#datetime-data)

### like
 
[!INCLUDE [operator-like-description](includes/operator-like-description.md)]

Data Type: [String](#string-data)

### lt
 
[!INCLUDE [operator-lt-description](includes/operator-lt-description.md)]

Data Types:

- [Number](#number-data)
- [Datetime](#datetime-data)

### ne
 
[!INCLUDE [operator-ne-description](includes/operator-ne-description.md)]

 Data Types:

- [Choice](#choice-data)
- [Datetime](#datetime-data)
- [Hierarchical](#hierarchical-data)
- [Number](#number-data)
- [Owner](#owner-data)
- [String](#string-data)
- [Unique Identifier](#unique-identifier-data)



### ne-businessid
 
[!INCLUDE [operator-ne-businessid-description](includes/operator-ne-businessid-description.md)]

Data Type: [Unique Identifier](#unique-identifier-data)

### ne-userid
 
[!INCLUDE [operator-ne-userid-description](includes/operator-ne-userid-description.md)]

Data Type: [Unique Identifier](#unique-identifier-data)

### neq
 
[!INCLUDE [operator-neq-description](includes/operator-neq-description.md)]

### next-fiscal-period
 
[!INCLUDE [operator-next-fiscal-period-description](includes/operator-next-fiscal-period-description.md)]

Data Type: [Datetime](#datetime-data)

### next-fiscal-year
 
[!INCLUDE [operator-next-fiscal-year-description](includes/operator-next-fiscal-year-description.md)]

Data Type: [Datetime](#datetime-data)

### next-month
 
[!INCLUDE [operator-next-month-description](includes/operator-next-month-description.md)]

Data Type: [Datetime](#datetime-data)

### next-seven-days
 
[!INCLUDE [operator-next-seven-days-description](includes/operator-next-seven-days-description.md)]

Data Type: [Datetime](#datetime-data)

### next-week
 
[!INCLUDE [operator-next-week-description](includes/operator-next-week-description.md)]

Data Type: [Datetime](#datetime-data)

### next-x-days
 
[!INCLUDE [operator-next-x-days-description](includes/operator-next-x-days-description.md)]

Data Type: [Datetime](#datetime-data)

### next-x-fiscal-periods
 
[!INCLUDE [operator-next-x-fiscal-periods-description](includes/operator-next-x-fiscal-periods-description.md)]

Data Type: [Datetime](#datetime-data)

### next-x-fiscal-years
 
[!INCLUDE [operator-next-x-fiscal-years-description](includes/operator-next-x-fiscal-years-description.md)]

Data Type: [Datetime](#datetime-data)

### next-x-hours
 
[!INCLUDE [operator-next-x-hours-description](includes/operator-next-x-hours-description.md)]

Data Type: [Datetime](#datetime-data)

### next-x-months
 
[!INCLUDE [operator-next-x-months-description](includes/operator-next-x-months-description.md)]

Data Type: [Datetime](#datetime-data)

### next-x-weeks
 
[!INCLUDE [operator-next-x-weeks-description](includes/operator-next-x-weeks-description.md)]

Data Type: [Datetime](#datetime-data)

### next-x-years
 
[!INCLUDE [operator-next-x-years-description](includes/operator-next-x-years-description.md)]

Data Type: [Datetime](#datetime-data)

### next-year
 
[!INCLUDE [operator-next-year-description](includes/operator-next-year-description.md)]

Data Type: [Datetime](#datetime-data)

### not-begin-with
 
[!INCLUDE [operator-not-begin-with-description](includes/operator-not-begin-with-description.md)]

Data Type: [String](#string-data)

### not-between
 
[!INCLUDE [operator-not-between-description](includes/operator-not-between-description.md)]

 Data Types: 

- [Number](#number-data)
- [Datetime](#datetime-data)

### not-contain-values
 
[!INCLUDE [operator-not-contain-values-description](includes/operator-not-contain-values-description.md)]

Data Type: [Choice](#choice-data)

### not-end-with
 
[!INCLUDE [operator-not-end-with-description](includes/operator-not-end-with-description.md)]

Data Type: [String](#string-data)

### not-in
 
[!INCLUDE [operator-not-in-description](includes/operator-not-in-description.md)]

Data Type: [Number](#number-data)

### not-like
 
[!INCLUDE [operator-not-like-description](includes/operator-not-like-description.md)]

Data Type: [String](#string-data)

### not-null
 
[!INCLUDE [operator-not-null-description](includes/operator-not-null-description.md)]

 Data Types:

- [Choice](#choice-data)
- [Datetime](#datetime-data)
- [Hierarchical](#hierarchical-data)
- [Number](#number-data)
- [Owner](#owner-data)
- [String](#string-data)
- [Unique Identifier](#unique-identifier-data)

### not-under
 
[!INCLUDE [operator-not-under-description](includes/operator-not-under-description.md)]

Data Type: [Hierarchical](#hierarchical-data)

### null
 
[!INCLUDE [operator-null-description](includes/operator-null-description.md)]

 Data Types:

- [Choice](#choice-data)
- [Datetime](#datetime-data)
- [Hierarchical](#hierarchical-data)
- [Number](#number-data)
- [Owner](#owner-data)
- [String](#string-data)
- [Unique Identifier](#unique-identifier-data)

### olderthan-x-days
 
[!INCLUDE [operator-olderthan-x-days-description](includes/operator-olderthan-x-days-description.md)]

Data Type: [Datetime](#datetime-data)

### olderthan-x-hours
 
[!INCLUDE [operator-olderthan-x-hours-description](includes/operator-olderthan-x-hours-description.md)]

Data Type: [Datetime](#datetime-data)

### olderthan-x-minutes
 
[!INCLUDE [operator-olderthan-x-minutes-description](includes/operator-olderthan-x-minutes-description.md)]

Data Type: [Datetime](#datetime-data)

### olderthan-x-months
 
[!INCLUDE [operator-olderthan-x-months-description](includes/operator-olderthan-x-months-description.md)]

Data Type: [Datetime](#datetime-data)

### olderthan-x-weeks
 
[!INCLUDE [operator-olderthan-x-weeks-description](includes/operator-olderthan-x-weeks-description.md)]

Data Type: [Datetime](#datetime-data)

### olderthan-x-years
 
[!INCLUDE [operator-olderthan-x-years-description](includes/operator-olderthan-x-years-description.md)]

Data Type: [Datetime](#datetime-data)

### on
 
[!INCLUDE [operator-on-description](includes/operator-on-description.md)]

Data Type: [Datetime](#datetime-data)

### on-or-after
 
[!INCLUDE [operator-on-or-after-description](includes/operator-on-or-after-description.md)]

Data Type: [Datetime](#datetime-data)

### on-or-before
 
[!INCLUDE [operator-on-or-before-description](includes/operator-on-or-before-description.md)]

Data Type: [Datetime](#datetime-data)

### this-fiscal-period
 
[!INCLUDE [operator-this-fiscal-period-description](includes/operator-this-fiscal-period-description.md)]

Data Type: [Datetime](#datetime-data)

### this-fiscal-year
 
[!INCLUDE [operator-this-fiscal-year-description](includes/operator-this-fiscal-year-description.md)]

Data Type: [Datetime](#datetime-data)

### this-month
 
[!INCLUDE [operator-this-month-description](includes/operator-this-month-description.md)]

Data Type: [Datetime](#datetime-data)

### this-week
 
[!INCLUDE [operator-this-week-description](includes/operator-this-week-description.md)]

Data Type: [Datetime](#datetime-data)

### this-year
 
[!INCLUDE [operator-this-year-description](includes/operator-this-year-description.md)]

Data Type: [Datetime](#datetime-data)

### today
 
[!INCLUDE [operator-today-description](includes/operator-today-description.md)]

Data Type: [Datetime](#datetime-data)

### tomorrow
 
[!INCLUDE [operator-tomorrow-description](includes/operator-tomorrow-description.md)]

Data Type: [Datetime](#datetime-data)

### under
 
[!INCLUDE [operator-under-description](includes/operator-under-description.md)]

Data Type: [Hierarchical](#hierarchical-data)

### yesterday
 
[!INCLUDE [operator-yesterday-description](includes/operator-yesterday-description.md)]

Data Type: [Datetime](#datetime-data)



[!INCLUDE [footer-banner](../../../../includes/footer-banner.md)]
