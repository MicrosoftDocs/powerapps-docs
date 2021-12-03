---
title: "getPrecision (Client API reference)| MicrosoftDocs"
description: Includes description and supported parameters for the getPrecision method.
ms.date: 04/19/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 610b9b53-9c29-4228-8ef3-0c05aae14a2b
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
# getPrecision (Client API reference)



Returns the number of digits allowed to the right of the decimal point. 

## Column types supported

Money, decimal, double, and integer

## Syntax

`formContext.getAttribute(arg).getPrecision()`

## Return Value

**Type**: Number. 

**Description**: The number of digits allowed to the right of the decimal point.

### Related topics

[setPrecision](setPrecision.md)



[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]