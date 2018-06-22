---
title: "getObject (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 10/31/2017
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: ad68d177-3715-468e-b4af-8cf9b3c77799
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# getObject (Client API reference)



Returns the object in the form that represents an IFRAME or web resource. 

## Control types supported

iframe, webresource

## Syntax

`formContext.getControl(arg).getObject();`

## Return Value

**Type**: Object

**Description**: Object depends on the type of control:
- An IFRAME returns the [IFrame](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe) element from the Document Object Model (DOM).
- A Silverlight web resource will return the [Object](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/object) element from the DOM that represents the embedded Silverlight plug-in.



