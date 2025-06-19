---
title: "setRequiredLevel (Client API reference)"
description: Includes description and supported parameters for the setRequiredLevel method.
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
# setRequiredLevel (Client API reference)

Sets whether data is required or recommended for the column before the record can be saved.

> [!IMPORTANT]
> Reducing the required level of a column can cause an error when the page is saved. If the column is required by the server, an error will occur if there is no value for the column. 

## Column types supported

All

## Syntax

`formContext.getAttribute(arg).setRequiredLevel(requirementLevel)`

## Parameters

**Type**: String.

**Description**: Set the level to one of the following values:

- `none`
- `required`
- `recommended`

### Related article

[getRequiredLevel (Client API reference)](getRequiredLevel.md)


[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
