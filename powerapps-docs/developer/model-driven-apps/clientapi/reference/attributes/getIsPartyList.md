---
title: "getIsPartyList (Client API reference)"
description: Returns a boolean value indicating whether the lookup represents a partylist lookup.
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
# getIsPartyList (Client API reference)

Returns a Boolean value indicating whether the lookup represents a partylist lookup. Partylist lookups allow for multiple records to be set, such as the **To:** column for an email table record.

## Column types supported

Lookup

## Syntax

`formContext.getAttribute(arg).getIsPartyList()`

[!INCLUDE[cc-terminology](../../../../data-platform/includes/cc-terminology.md)]

## Return Value

**Type**: Boolean. 

**Description**: True if the lookup column is a partylist, otherwise false.



[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
