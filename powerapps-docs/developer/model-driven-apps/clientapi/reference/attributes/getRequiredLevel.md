---
title: "getRequiredLevel (Client API reference)| MicrosoftDocs"
description: Includes description and supported parameters for the getRequiredLevel method.
author: HemantGaur
ms.author: hemantg
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
# getRequiredLevel (Client API reference)



Returns a string value indicating whether a value for the column is required or recommended. 

## Column types supported

All

## Syntax

`formContext.getAttribute(arg).getRequiredLevel()`

## Return Value

**Type**: String. 

**Description**: Returns one of the following values:
- none
- required
- recommended

### Related article

[setRequiredLevel (Client API reference)](setRequiredLevel.md)


[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
