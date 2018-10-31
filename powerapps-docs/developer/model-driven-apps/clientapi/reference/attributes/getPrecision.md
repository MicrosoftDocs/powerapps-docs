---
title: "getPrecision (Client API reference)| MicrosoftDocs"
ms.date: 10/31/2018
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 610b9b53-9c29-4228-8ef3-0c05aae14a2b
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# getPrecision (Client API reference)



Returns the number of digits allowed to the right of the decimal point. 

## Attribute types supported

Money, decimal, double, and integer

## Syntax

`formContext.getAttribute(arg).getPrecision()`

## Return Value

**Type**: Number. 

**Description**: The number of digits allowed to the right of the decimal point.

### Related topics

[setPrecision](setPrecision.md)

