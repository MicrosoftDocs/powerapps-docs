---
title: "getIsPartyList (Client API reference)| MicrosoftDocs"
description: Returns a boolean value indicating whether the lookup represents a partylist lookup.
ms.date: 04/15/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 487d0923-9675-4308-b88e-fdbf91853a98
author: "Nkrb"
ms.subservice: mda-developer
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
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