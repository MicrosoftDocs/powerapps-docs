---
title: "getOption (Client API reference)| MicrosoftDocs"
description: Includes description and supported parameters for the getOption method.
ms.date: 04/19/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: e334d2d9-91c0-4953-956d-444a84dc9da2
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# getOption (Client API reference)



Returns an option object with the value matching the argument (label or enumeration value) passed to the method. 

## Column types supported

Choice, Choices

## Syntax

`formContext.getAttribute(arg).getOption(value)`

## Parameters

**String** (label of the option) or **Number** (enumeration value of the option).

## Return Value

**Type**: Option object. 

**Description**: The logical name of the column.



[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]