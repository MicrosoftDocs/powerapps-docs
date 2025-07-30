---
title: "isDefaultPrevented (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the isDefaultPrevented method.
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
# isDefaultPrevented (Client API reference)

[!INCLUDE[./includes/isDefaultPrevented-description.md](./includes/isDefaultPrevented-description.md)]

## Syntax

`executionContext.getEventArgs().isDefaultPrevented();`

## Return Value

**Type**: Boolean

**Description**: **true** if the save event has been canceled because the preventDefault method was used; **false** otherwise.


### Related articles

[getSaveMode](getSaveMode.md)   
[preventDefault](preventDefault.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
