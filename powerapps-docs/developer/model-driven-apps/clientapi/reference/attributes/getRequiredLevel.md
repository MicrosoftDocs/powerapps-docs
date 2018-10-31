---
title: "getRequiredLevel (Client API reference)| MicrosoftDocs"
ms.date: 10/31/2018
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: c0b6ea26-2a11-4a49-8ecf-fe700e782bf3
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# getRequiredLevel (Client API reference)



Returns a string value indicating whether a value for the attribute is required or recommended. 

## Attribute types supported

All

## Syntax

`formContext.getAttribute(arg).getRequiredLevel()`

## Return Value

**Type**: String. 

**Description**: Returns one of the following values:
- none
- required
- recommended

### Related topic
[setRequiredLevel (Client API reference)](setRequiredLevel.md)
