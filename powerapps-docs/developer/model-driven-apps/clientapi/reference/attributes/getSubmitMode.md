---
title: "getSubmitMode (Client API reference)| MicrosoftDocs"
description: Includes description and supported parameters for the getSubmitMode method.
ms.date: 04/19/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: a3231438-3821-4dce-b118-d63e6ce85e01
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
# getSubmitMode (Client API reference)



Returns a string indicating when data from the column will be submitted when the record is saved. 

## Column types supported

All

## Syntax

`formContext.getAttribute(arg).getSubmitMode()`

## Return Value

**Type**: String. 

**Description**: Returns one of the following values:
- always
- never
- dirty

### Related topic
[setSubmitMode (Client API reference)](setSubmitMode.md)



[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]