---
title: "isDefaultPrevented (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 10/31/2018
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 9a8802ad-80aa-4386-a192-573280587546
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# isDefaultPrevented (Client API reference)



[!INCLUDE[./includes/isDefaultPrevented-description.md](./includes/isDefaultPrevented-description.md)]

## Syntax

`executionContext.getEventArgs().isDefaultPrevented();`

## Return Value

**Type**: Boolean

**Description**: **true** if the save event has been canceled because the preventDefault method was used; **false** otherwise.


### Related topics

[getSaveMode](getSaveMode.md)

[preventDefault](preventDefault.md)

