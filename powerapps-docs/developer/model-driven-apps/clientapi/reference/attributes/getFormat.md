---
title: "getFormat (Client API reference)| MicrosoftDocs"
ms.date: 10/31/2017
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: e5f97552-4a48-4bf9-b460-6105442e2e6b
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# getFormat (Client API reference)



Returns a string value that represents formatting options for the attribute. 

## Attribute types supported

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
> This format information generally represents the format options of the application field. Format options for Boolean fields are not provided.

The following table lists the format string values to expect for each type of attribute schema type and format option.

| Application Field Type | Format Option | Attribute Type | Format Value|
|----------------------------|-------------------|--------------------|------------------|
| Date and Time              | Date Only         | datetime           | date             |
| Date and Time              | Date and Time     | datetime           | datetime         |
| Whole Number               | Duration          | integer            | duration         |
| Single Line of Text        | E-mail            | string             | email            |
| Whole Number               | Language          | optionset          | language         |
| Whole Number               | None              | integer            | none             |
| Single Line of Text        | Text Area         | string             | textarea         |
| Single Line of Text        | Text              | string             | text             |
| Single Line of Text        | Ticker Symbol     | string             | tickersymbol     |
| Single Line of Text        | Phone             | string             | phone            |
| Whole Number               | Time Zone         | optionset          | timezone         |
| Single Line of Text        | Url               | string             | url 
