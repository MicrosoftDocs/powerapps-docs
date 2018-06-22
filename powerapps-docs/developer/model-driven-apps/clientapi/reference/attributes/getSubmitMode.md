---
title: "getSubmitMode (Client API reference)| MicrosoftDocs"
ms.date: 10/31/2017
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: a3231438-3821-4dce-b118-d63e6ce85e01
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# getSubmitMode (Client API reference)

[!INCLUDE[](../../../../includes/cc_applies_to_update_9_0_0.md)]

Returns a string indicating when data from the attribute will be submitted when the record is saved. 

## Attribute types supported

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

