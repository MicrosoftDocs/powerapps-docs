---
title: "getMaxLength (Client API reference)"
description: Includes description and supported parameters for the getMaxLength method.
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
# getMaxLength (Client API reference)

Returns a number indicating the maximum length of a string or memo column. 

## Column types supported

string, memo

## Syntax

`formContext.getAttribute(arg).getMaxLength()`

## Return Value

**Type**: Number. 

**Description**: The maximum allowed length of a string for this column.

> [!NOTE]
> The email form description column is a memo column, but it does not have a `getMaxLength` method.

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
