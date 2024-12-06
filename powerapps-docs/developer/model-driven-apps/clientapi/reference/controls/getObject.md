---
title: "getObject (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the getObject method.
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
# getObject (Client API reference)

Returns the object in the form that represents an IFRAME or web resource. 

## Control types supported

iframe, webresource

## Syntax

`formContext.getControl(arg).getObject();`

> [!NOTE]
> This method should be used after the [onreadystatecomplete](../events/onreadystatecomplete.md) event is triggered. If this is used before, then there is chance that the call to `getObject()` will fail.
 
## Return Value

**Type**: Object

**Description**: Object depends on the type of control:

- An IFRAME and HTML web resource returns the [IFrame](https://developer.mozilla.org/docs/Web/HTML/Element/iframe) element from the Document Object Model (DOM).


[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
