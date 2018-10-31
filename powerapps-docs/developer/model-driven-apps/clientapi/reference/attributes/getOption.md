---
title: "getOption (Client API reference)| MicrosoftDocs"
ms.date: 10/31/2018
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: e334d2d9-91c0-4953-956d-444a84dc9da2
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# getOption (Client API reference)



Returns an option object with the value matching the argument (label or enumeration value) passed to the method. 

## Attribute types supported

OptionSet, MultiSelectOptionSet

## Syntax

`formContext.getAttribute(arg).getOption(value)`

## Parameters

**String** (label of the option) or **Number** (enumeration value of the option).

## Return Value

**Type**: Option object. 

**Description**: The logical name of the attribute.

