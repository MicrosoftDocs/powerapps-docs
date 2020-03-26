---
title: "setPrecision (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 10/31/2018
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 580aebec-c1d1-4e4a-8c20-ced859569fb2
author: "KumarVivek"
ms.author: "kvivek"
manager: "annbe"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# setPrecision (Client API reference)



Sets the number of digits allowed to the right of the decimal point. 

## Attribute types supported

Money, decimal, double, and integer

## Syntax

`formContext.getAttribute(arg).setPrecision(value);`

## Parameter

 Parameter Name| Type| Description  |
| --------|-----------| -----|
|value| Number| Number of digits allowed to the right of the decimal point.|

### Related topics

[getPrecision](getPrecision.md)

