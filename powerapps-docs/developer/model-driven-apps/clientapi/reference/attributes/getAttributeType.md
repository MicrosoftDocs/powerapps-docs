---
title: "getAttributeType (Client API reference)| MicrosoftDocs"
ms.date: 02/13/2019
ms.service: powerapps
ms.topic: "reference"
ms.assetid: 9ef1c886-a0b8-4ba9-bb9f-e6ecfa9d6dff
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# getAttributeType (Client API reference)



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
- multiselectoptionset
- optionset
- string


[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]