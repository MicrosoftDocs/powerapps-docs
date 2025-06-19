---
title: "getSrc (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the getSrc method.
author: MitiJ
ms.author: mijosh
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
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

### Related articles

[setSrc](setSrc.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
