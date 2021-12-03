---
title: "setPrecision (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the setPrecision method.
ms.date: 04/19/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 580aebec-c1d1-4e4a-8c20-ced859569fb2
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
# setPrecision (Client API reference)



Sets the number of digits allowed to the right of the decimal point. 

## Column types supported

Money, decimal, double, and integer

## Syntax

`formContext.getAttribute(arg).setPrecision(value);`

## Parameter

 Parameter Name| Type| Description  |
| --------|-----------| -----|
|value| Number| Number of digits allowed to the right of the decimal point.|

### Related topics

[getPrecision](getPrecision.md)



[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]