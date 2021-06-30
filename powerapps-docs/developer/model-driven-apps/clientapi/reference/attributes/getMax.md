---
title: "getMax (Client API reference)| MicrosoftDocs"
description: Includes description and supported parameters for the getMax method.
ms.date: 04/19/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 6bcd4b47-b3b6-4a9c-899f-a5dce4cbab51
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# getMax (Client API reference)



Returns a number indicating the maximum allowed value for a column. 

## Column types supported

decimal, integer, double, money

## Syntax

`formContext.getAttribute(arg).getMax()`

## Return Value

**Type**: Number. 

**Description**: The maximum allowed value for the column.



[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]