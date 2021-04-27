---
title: "getDisplayState (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the getDisplayState method.
ms.date: 04/19/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 21368fac-d4bc-4f75-8a9c-cce098fa0b45
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
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