---
title: "getActiveStage (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the getActiveStage method.
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
# getActiveStage (Client API reference)

[!INCLUDE[./includes/getActiveStage-description.md](./includes/getActiveStage-description.md)]

## Syntax

`formContext.data.process.getActiveStage();`

## Return Value

**Type**: Stage. 

**Description**: The currently active stage. See [Stage methods](../../formContext-data-process.md#stage-methods) for the methods to access the properties of the stage returned.

### Related articles

[setActiveStage](setActiveStage.md)   
[getSelectedStage (Client API reference)](../getSelectedStage.md)   
[formContext.data.process](../../formContext-data-process.md)
 

[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]
