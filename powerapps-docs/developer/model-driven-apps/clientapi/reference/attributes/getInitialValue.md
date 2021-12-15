---
title: "getInitialValue (Client API reference)| MicrosoftDocs"
description: Includes description and supported parameters for the getInitialValue method.
ms.date: 04/19/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 56fb62e6-d357-4096-bf4c-f4c1b543d633
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
# getInitialValue (Client API reference)



Returns a value that represents the value set for a **Yes/No**, **Choice** or **Choices** column when the form is opened.

## Column types supported

Tes/No, Choice, Choices 

## Syntax

`formContext.getAttribute(arg).getInitialValue()`

## Return Value

**Type**: Number

**Description**: The initial value for the column.




[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]