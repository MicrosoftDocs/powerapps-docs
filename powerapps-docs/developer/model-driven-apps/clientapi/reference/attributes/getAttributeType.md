---
title: "getAttribute (Client API reference)| MicrosoftDocs"
ms.date: 10/31/2017
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 9ef1c886-a0b8-4ba9-bb9f-e6ecfa9d6dff
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# getAttribute (Client API reference)

[!INCLUDE[](../../../../includes/cc_applies_to_update_9_0_0.md)]

Returns a string value that represents the type of attribute. 

## Attribute types supported

All

## Syntax

`formContext.getAttribute(arg).getAttributeType()`

## Return Value

This method will return one of the following **string** values:

- boolean
- datetime
- decimal
- double
- integer
- lookup
- memo
- money
- multioptionset
- optionset
- string