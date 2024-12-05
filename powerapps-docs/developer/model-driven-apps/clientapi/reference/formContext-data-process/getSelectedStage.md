---
title: "getSelectedStage (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the getSelectedStage method.
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
# getSelectedStage (Client API reference)

[!INCLUDE[./includes/getSelectedStage-description.md](./includes/getSelectedStage-description.md)]

## Syntax

`formContext.data.process.getSelectedStage();`

## Return Value

**Type**: Stage. 

**Description**: The currently selected stage. See [Stage methods](../formContext-data-process.md#stage-methods) for the methods to access the properties of the stage returned.

### Related articles

[getActiveStage (Client API reference)](activestage/getActiveStage.md)   
[formContext.data.process](../formContext-data-process.md)
 
[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
