---
title: "getSrc (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the getSrc method.
ms.date: 04/19/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: e003d21f-393a-4681-a6fc-256949167fcc
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# getSrc (Client API reference)



Returns the current URL being displayed in an IFRAME or web resource. 

## Control types supported

iframe, webresource

## Syntax

`formContext.getControl(arg).getSrc();`

## Return Value

**Type**: String

**Description**: A URL representing the **src** property of the IFRAME or web resource.

### Related topics

[setSrc](setSrc.md)



[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]