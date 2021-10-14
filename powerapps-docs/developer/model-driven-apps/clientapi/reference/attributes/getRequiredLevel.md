---
title: "getRequiredLevel (Client API reference)| MicrosoftDocs"
description: Includes description and supported parameters for the getRequiredLevel method.
ms.date: 04/19/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: c0b6ea26-2a11-4a49-8ecf-fe700e782bf3
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

### Related topic
[setRequiredLevel (Client API reference)](setRequiredLevel.md)


[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]