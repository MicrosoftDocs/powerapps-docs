---
title: "getDisplayState (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the getDisplayState method.
ms.author: jdaly
author: adrianorth
manager: kvivek
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# getDisplayState (Client API reference)



[!INCLUDE[./includes/getDisplayState-description.md](./includes/getDisplayState-description.md)]

## Syntax

`formContext.ui.process.getDisplayState();`

## Return Value

**Type**: String.

**Description**: Returns "expanded" or "collapsed" on the legacy web client; returns "expanded", "collapsed", or "floating" on Unified Interface.

### Related topics

[setDisplayState](setDisplayState.md)

[formContext.ui.process](../formContext-ui-process.md)





[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]