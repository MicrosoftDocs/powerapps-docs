---
title: "movePrevious (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 10/31/2017
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 649fe7b0-016d-409f-ba3c-b14e0f1953e0
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# movePrevious (Client API reference)



[!INCLUDE[./includes/movePrevious-description.md](./includes/movePrevious-description.md)]

You can also move to a previous stage in a different entity.

## Syntax

`formContext.data.process.movePrevious(callbackFunction);`

## Parameters

<table style="width:100%">
<tr>
<th>Name</th>
<th>Type</th>
<th>Required</th>
<th>Description</th>
</tr>
<tr>
<td>callbackFunction</td>
<td>Function</td>
<td>No</td>
<td>A function to call when the operation is complete. This callback function is passed one of the following string values to indicate the status of the operation:
<table>
<tr>
<th>Value</th>
<th>Reason</th>
</tr>
<tr>
<td>success</td>
<td>The operation succeeded.</td>
</tr>
<tr>
<td>crossEntity</td>
<td>The previous stage is for a different entity.</td>
</tr>
<tr>
<td>beginning</td>
<td>The active stage is the first stage of the active path.</td>
</tr>
<tr>
<td>invalid</td>
<td>The operation failed because the selected stage isn’t the same as the active stage.</td>
</tr>
<tr>
<td>dirtyForm</td>
<td>This value will be returned if the data in the page is not saved.</td>
</tr>
</table>
</td>
</tr>
</table>

>[!IMPORTANT]
>This method can only be used when the selected stage and the active stage are the same. When your code is initiated from the [OnStageChange](../../events/onstagechange.md) event, the current stage will be selected. When your code is initiated from the [OnStageSelected](../../events/onstageselected.md) event, you should use the [getActiveStage](../activestage/getActiveStage.md) method to verify that the selected stage is also the active stage. For any other form event, it isn’t possible to determine which stage is currently selected. For best results, this method should only be used in code that is called in functions initiated by the [OnStageChange](../../events/onstagechange.md) and [OnStageSelected](../../events/onstageselected.md) events.

## Remarks

This methods will cause the [OnStageChange](../../events/onstagechange.md) event to occur.

### Related topics

[moveNext](moveNext.md)

[formContext.data.process](../../formContext-data-process.md)
 


