---
title: "getMin (Client API reference)| MicrosoftDocs"
description: Includes description and supported parameters for the getMin method.
ms.date: 04/19/2021
ms.service: powerapps
ms.topic: "reference"
ms.assetid: 9a04b52a-2bc7-4572-bd3e-8b9622602092
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# getMin (Client API reference)



Returns a number indicating the minimum allowed value for a column. 

## Column types supported

Decimal, integer, double, money

## Syntax

`formContext.getAttribute(arg).getMin()`

## Return Value

**Type**: Number. 

**Description**: The minimum allowed value for the column.



[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]