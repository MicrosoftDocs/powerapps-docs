---
title: "getSrc (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 10/31/2018
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: e003d21f-393a-4681-a6fc-256949167fcc
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
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

