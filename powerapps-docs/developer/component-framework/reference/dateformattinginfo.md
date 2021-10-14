---
title: DateFormattingInfo | Microsoft Docs
description: Provides the date formatting information for the current user.
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 10/01/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 4e7d43fb-b6b7-4f1d-89e3-0b8157c9d2d9
---

# DateFormattingInfo

[!INCLUDE [context-description](includes/dateformattinginfo-description.md)]

## Available for 

Model-driven apps

## Properties

### abbreviatedDayNames

{ "Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat" }

**Type**: `string`

### abbreviatedMonthGenitiveNames

{ "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec", "" }

**Type**: `string[]`

### abbreviatedMonthNames

{ "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec", "" }

**Type**: `string[]`

### amDesignator

"AM"

**Type**: `string`

### calendar

**Type**: `object`

The `calendar` object contains the following properties:

|Name|Type|Description|
|--|--|--|
|`algorithmType`|`number`|1|
|`calendarType`|`number`|1|
|`maxSupportedDateTime`|`Date`|"/Date(253402300799999)/"|
|`minSupportedDateTime`|`Date`|"/Date(-62135568000000)/"|
|`twoDigitYearMax`|`number`|2029|

### calendarWeekRule

**Type**: `number`

### dateSeparator

"/"

**Type**: `string`

### dayNames

{ "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday" }

**Type**: `string[]`

### firstDayOfWeek

**Type**: `number`

The `firstDayOfWeek` property can be set to one of the following values:

|Value|Meaning|
|--|--|
|0|Sunday|
|1|Monday|
|2|Tuesday|
|3|Wednesday|
|4|Thursday|
|5|Friday|
|6|Saturday|

### fullDateTimePattern

"dddd, MMMM d, yyyy h:mm:ss tt"

**Type**: `string`

### longDatePattern

dddd, MMMM d, yyyy"

**Type**: `string`

### longTimePattern

"hh:mm:ss tt"

**Type**: `string`

### monthDayPattern

"MMMM dd"

**Type**: `string`

### monthGenitiveNames

{ "January", "February", "March", ...  "December", "" }

**Type**: `string[]`

### monthNames

{ "January", "February", "March", ...  "December", "" }

**Type**: `string[]`

### pmDesignator

"PM"

**Type**: `string`

### shortDatePattern

"M/d/yyyy"

**Type**: `string`

### shortTimePattern

"h:mm tt"

**Type**: `string`

### shortestDayNames

{ "Su", "Mo", "Tu", "We", "Th", "Fr", "Sa" }

**Type**: `string[]`

### sortableDateTimePattern

yyyy'-'MM'-'dd'T'HH':'mm':'ss"

**Type**: `string`

### timeSeparator

":"

**Type**: `string`

### universalSortableDateTimePattern

"yyyy'-'MM'-'dd HH':'mm':'ss'Z'"

**Type**: `string`

### yearMonthPattern

"MMMM yyyy"

**Type**: `string`


### Related topics

[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]