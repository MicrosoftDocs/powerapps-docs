---
title: "getInitialValue (Client API reference)| MicrosoftDocs"
description: Includes description and supported parameters for the getInitialValue method.
ms.author: jdaly
author: adrianorth
manager: kvivek
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.subservice: mda-developer
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
  - JimDaly
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