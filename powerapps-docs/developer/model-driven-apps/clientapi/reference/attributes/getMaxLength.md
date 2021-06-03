---
title: "getMaxLength (Client API reference)| MicrosoftDocs"
description: Includes description and supported parameters for the getMaxLength method.
ms.date: 04/19/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 67a96fc4-4d65-4858-90da-f41eeba0365a
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# getMaxLength (Client API reference)



Returns a number indicating the maximum length of a string or memo column. 

## Column types supported

string, memo

## Syntax

`formContext.getAttribute(arg).getMaxLength()`

## Return Value

**Type**: Number. 

**Description**: The maximum allowed length of a string for this column.

> [!NOTE]
> The email form description column is a memo column, but it does not have a `getMaxLength` method.

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]