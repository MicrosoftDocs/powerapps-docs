---
title: "getSubmitMode (Client API reference)"
description: Includes description and supported parameters for the getSubmitMode method.
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
# getSubmitMode (Client API reference)

Returns a string indicating when data from the column will be submitted when the record is saved. 

## Column types supported

All

## Syntax

`formContext.getAttribute(arg).getSubmitMode()`

## Return Value

**Type**: String. 

**Description**: Returns one of the following values:

- always
- never
- dirty

### Related article

[setSubmitMode (Client API reference)](setSubmitMode.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
