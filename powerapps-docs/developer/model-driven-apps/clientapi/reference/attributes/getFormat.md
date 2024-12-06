---
title: "getFormat (Client API reference)"
description: Includes description and supported parameters for the getFormat method.
author: clromano
ms.author: clromano
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
ms.subservice: mda-developer
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# getFormat (Client API reference)

Returns a string value that represents formatting options for the column. 

## Column types supported

All

## Syntax

`formContext.getAttribute(arg).getFormat()`

## Return Value

This method will return one of the following **string** values or "null":

- date
- datetime
- duration
- email
- language
- none
- phone
- text
- textarea
- tickersymbol
- timezone
- url

> [!NOTE]
> This format information generally represents the format options of the application column. Format options for Boolean columns are not provided.

The following table lists the format string values to expect for each type of column type and format option.

| Application column Type | Format Option | Column Type | Format Value|
|----------------------------|-------------------|--------------------|------------------|
| Date and Time              | Date Only         | datetime           | date             |
| Date and Time              | Date and Time     | datetime           | datetime         |
| Whole Number               | Duration          | integer            | duration         |
| Single Line of Text        | E-mail            | string             | email            |
| Whole Number               | Language          | choice          | language         |
| Whole Number               | None              | integer            | none             |
| Single Line of Text        | Text Area         | string             | textarea         |
| Single Line of Text        | Text              | string             | text             |
| Single Line of Text        | Ticker Symbol     | string             | tickersymbol     |
| Single Line of Text        | Phone             | string             | phone            |
| Whole Number               | Time Zone         | choice          | timezone         |
| Single Line of Text        | Url               | string             | url 


[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
