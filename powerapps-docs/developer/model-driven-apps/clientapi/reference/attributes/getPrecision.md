---
title: "getPrecision (Client API reference)| MicrosoftDocs"
ms.date: 10/31/2017
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 610b9b53-9c29-4228-8ef3-0c05aae14a2b
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# getPrecision (Client API reference)

[!INCLUDE[](../../../../includes/cc_applies_to_update_9_0_0.md)]

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

