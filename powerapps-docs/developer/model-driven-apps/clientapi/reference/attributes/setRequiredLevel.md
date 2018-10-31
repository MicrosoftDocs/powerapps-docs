---
title: "setRequiredLevel (Client API reference)| MicrosoftDocs"
ms.date: 10/31/2018
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 67a96fc4-4d65-4858-90da-f41eeba0365a
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# setRequiredLevel (Client API reference)



Sets whether data is required or recommended for the attribute before the record can be saved.

> [!IMPORTANT]
> Reducing the required level of an attribute can cause an error when the page is saved. If the attribute is required by the server, an error will occur if there is no value for the attribute. 

## Attribute types supported

All

## Syntax

`formContext.getAttribute(arg).setRequiredLevel(requirementLevel)`

## Parameters

**Type**: String. 

**Description**: Set the level to one of the following values:
- none
- required
- recommended

### Related topic
[getRequiredLevel (Client API reference)](getRequiredLevel.md)


