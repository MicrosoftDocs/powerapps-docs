---
title: "getUserPrivilege (Client API reference)"
description: Includes description and supported parameters for the getUserPrivilege method.
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
# getUserPrivilege (Client API reference)

Returns an object with three boolean properties corresponding to privileges indicating if the user can create, read or update data values for a column. This function is intended for use when Field Level Security modifies a user's privileges for a particular column. 

## Column types supported

All

## Syntax

`formContext.getAttribute(arg).getUserPrivilege()`

## Return Value

**Type**: Object. 

**Description**: The object has three boolean properties:

- canRead
- canUpdate
- canCreate

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
