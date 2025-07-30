---
title: "getOption (Client API reference)"
description: Includes description and supported parameters for the getOption method.
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
# getOption (Client API reference)

Returns an option object with the value matching the argument (label or enumeration value) passed to the method. 

## Column types supported

Choice, Choices

## Syntax

`formContext.getAttribute(arg).getOption(value)`

## Parameters

**String** (label of the option) or **Number** (enumeration value of the option).

## Return Value

**Type**: Option object. 

**Description**: The logical name of the column.

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
