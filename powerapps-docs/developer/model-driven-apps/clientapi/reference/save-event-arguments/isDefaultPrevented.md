---
title: "isDefaultPrevented (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the isDefaultPrevented method.
ms.date: 04/21/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 9a8802ad-80aa-4386-a192-573280587546
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
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



[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]