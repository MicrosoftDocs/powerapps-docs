---
title: "process.getDisplayState (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the process.getDisplayState method.
author: matthidinger
ms.author: mahiding
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# process.getDisplayState (Client API reference)

[!INCLUDE[./includes/getDisplayState-description.md](./includes/getDisplayState-description.md)]

## Syntax

`formContext.ui.process.getDisplayState();`

## Return Value

**Type**: String.

**Description**: Returns `expanded` or `collapsed` on the legacy web client; returns `expanded`, `collapsed`, or `floating` on Unified Interface.

### Related articles

[setDisplayState](setDisplayState.md)   
[formContext.ui.process](../formContext-ui-process.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
