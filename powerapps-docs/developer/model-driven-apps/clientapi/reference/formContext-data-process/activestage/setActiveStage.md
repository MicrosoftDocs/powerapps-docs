---
title: "setActiveStage (Client API reference) in model-driven apps"
description: Sets a completed stage as the active stage.
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
# setActiveStage (Client API reference)

[!INCLUDE[./includes/setActiveStage-description.md](./includes/setActiveStage-description.md)]

## Syntax

`formContext.data.process.setActiveStage(stageId, callbackFunction);`

[!INCLUDE[cc-terminology](../../../../../data-platform/includes/cc-terminology.md)]

## Parameters

|Name|Type|Required|Description|
|---|---|---|---|
|`stageId`|String|Yes|The ID of the completed stage for the table to make the active stage.|
|`callbackFunction`|Function|No|A function to call when the operation is complete. See [callbackFunction parameter](#callbackfunction-parameter)|

### callbackFunction parameter

This callback function is passed one of the following string values to indicate the status of the operation:

|Value|Reason|
|---|---|
|`success`|The operation succeeded.|
|`invalid`|There are three reasons why this value may be returned:<br />- The *stageId* parameter is a non-existent stage ID value.<br />- The active stage isn't the selected stage.<br />- The record hasn't been saved yet.|
|`unreachable`|The stage exists on a different path.|
|`dirtyForm`|This value will be returned if the data in the page is not saved.|
|`preventDefault`|This value will be returned if an `OnPreStageChange` event handler invokes preventDefault.|


>[!IMPORTANT]
>This method can only be used when the selected stage and the active stage are the same. When your code is initiated from the [OnStageChange](../../events/onstagechange.md) event, the current stage will be selected. When your code is initiated from the [OnStageSelected](../../events/onstageselected.md) event, you should use the [getActiveStage](getActiveStage.md) method to verify that the selected stage is also the active stage. For any other form event, it isn't possible to determine which stage is currently selected. For best results, this method should only be used in code that is called in functions initiated by the [OnStageChange](../../events/onstagechange.md) and [OnStageSelected](../../events/onstageselected.md) events.

### Related articles

[getActiveStage](getActiveStage.md)   
[formContext.data.process](../../formContext-data-process.md)
 
[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]
