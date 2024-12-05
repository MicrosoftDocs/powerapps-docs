---
title: "movePrevious (Client API reference) in model-driven apps"
description: Moves to the previous stage.
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
# movePrevious (Client API reference)

[!INCLUDE[./includes/movePrevious-description.md](./includes/movePrevious-description.md)]

You can also move to a previous stage in a different table.

## Syntax

`formContext.data.process.movePrevious(callbackFunction);`

[!INCLUDE[cc-terminology](../../../../../data-platform/includes/cc-terminology.md)]


## Parameters

|Name|Type|Required|Description|
|---|---|---|---|
|`callbackFunction`|Function|No| A function to call when the operation is complete. See [callbackFunction](#callbackfunction) |

### callbackFunction

This callback function is passed one of the following string values to indicate the status of the operation:

|Value|Reason|
|---|---|
|`success`|The operation succeeded.|
|`crossEntity`|The next stage is for a different table.|
|`beginning`|The active stage is the first stage of the active path.|
|`invalid`|The operation failed because the selected stage isn't the same as the active stage.|
|`dirtyForm`|This value is returned if the data in the page isn't saved.|
|`stageGate`|One or more required columns on the current stage are empty.|
|`preventDefault`|This value is returned if an `OnPreStageChange` event handler invokes preventDefault.|

>[!IMPORTANT]
>This method can only be used when the selected stage and the active stage are the same. When your code is initiated from the [OnStageChange](../../events/onstagechange.md) event, the current stage will be selected. When your code is initiated from the [OnStageSelected](../../events/onstageselected.md) event, you should use the [getActiveStage](../activestage/getActiveStage.md) method to verify that the selected stage is also the active stage. For any other form event, it isn't possible to determine which stage is currently selected. For best results, this method should only be used in code that is called in functions initiated by the [OnStageChange](../../events/onstagechange.md) and [OnStageSelected](../../events/onstageselected.md) events.

## Remarks

This method causes the [OnStageChange](../../events/onstagechange.md) event to occur.

### Related articles

[moveNext](moveNext.md)   
[formContext.data.process](../../formContext-data-process.md)
 
[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]
