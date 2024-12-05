---
title: "getAttributeType (Client API reference)"
description: Includes description and supported parameters for the getAttributeType method.
author: clromano
ms.author: clromano
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: mda-developer
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# getAttributeType (Client API reference)

Returns a string value that represents the type of column. 

## Column types supported

All

## Syntax

`formContext.getAttribute(arg).getAttributeType()`

## Return Value

This method will return one of the following **string** values:

- boolean
- datetime
- decimal
- double
- file
- image
- integer
- lookup
- memo
- money
- multiselectoptionset (choices)
- optionset (choice)
- string


[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
