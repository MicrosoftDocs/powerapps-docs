---
title: "getIsPartyList (Client API reference)| MicrosoftDocs"
ms.date: 10/31/2018
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 487d0923-9675-4308-b88e-fdbf91853a98
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# getIsPartyList (Client API reference)



Returns a Boolean value indicating whether the lookup represents a partylist lookup. Partylist lookups allow for multiple records to be set, such as the **To:** field for an email entity record.

## Attribute types supported

Lookup

## Syntax

`formContext.getAttribute(arg).getIsPartyList()`

## Return Value

**Type**: Boolean. 

**Description**: True if the lookup attribute is a partylist, otherwise false.

