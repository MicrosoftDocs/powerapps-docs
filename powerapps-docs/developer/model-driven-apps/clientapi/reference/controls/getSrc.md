---
title: "getSrc (Client API reference) in Dynamics 365 Customer Engagement| MicrosoftDocs"
ms.date: 10/31/2017
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: e003d21f-393a-4681-a6fc-256949167fcc
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# getSrc (Client API reference)

[!INCLUDE[](../../../../includes/cc_applies_to_update_9_0_0.md)]

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

