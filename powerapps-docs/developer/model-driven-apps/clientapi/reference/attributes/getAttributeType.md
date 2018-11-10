---
title: "getAttribute (Client API reference)| MicrosoftDocs"
ms.date: 10/31/2018
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 9ef1c886-a0b8-4ba9-bb9f-e6ecfa9d6dff
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# getAttribute (Client API reference)



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