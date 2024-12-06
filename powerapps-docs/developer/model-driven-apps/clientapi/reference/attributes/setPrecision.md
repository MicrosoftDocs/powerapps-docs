---
title: "setPrecision (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the setPrecision method.
author: clromano
ms.author: clromano
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
ms.subservice: mda-developer
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# setPrecision (Client API reference)

Sets the number of digits allowed to the right of the decimal point. 

## Column types supported

Money, decimal, double, and integer

## Syntax

`formContext.getAttribute(arg).setPrecision(value);`

## Parameter

 Parameter Name| Type| Description  |
| --------|-----------| -----|
|`value`| Number| Number of digits allowed to the right of the decimal point.|

### Related articles

[getPrecision](getPrecision.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
