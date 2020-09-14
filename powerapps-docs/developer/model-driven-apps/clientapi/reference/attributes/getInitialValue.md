---
title: "getInitialValue (Client API reference)| MicrosoftDocs"
ms.date: 10/31/2018
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 56fb62e6-d357-4096-bf4c-f4c1b543d633
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# getInitialValue (Client API reference)



Returns a value that represents the value set for a **Boolean**, **OptionSet** or **MultiSelectOptionSet** attribute when the form is opened.

## Attribute types supported

Boolean, OptionSet, MultiSelectOptionSet 

## Syntax

`formContext.getAttribute(arg).getInitialValue()`

## Return Value

**Type**: Number

**Description**: The initial value for the attribute.


