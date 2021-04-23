---
title: "moveNext (Client API reference) in model-driven apps| MicrosoftDocs"
description: Progresses to the next stage.
ms.date: 04/15/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 97640c6a-816b-4d18-9b0b-e79411787c1a
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# moveNext (Client API reference)



[!INCLUDE[./includes/moveNext-description.md](./includes/moveNext-description.md)]

Moving to next stage is not supported for different table.

## Syntax

`formContext.data.process.moveNext(callbackFunction);`

[!INCLUDE[cc-terminology](../../../../../data-platform/includes/cc-terminology.md)]

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
<td>The next stage is for a different table.</td>
</tr>
<tr>
<td>end</td>
<td>The active stage is the last stage of the active path.</td>
</tr>
<tr>
<td>invalid</td>
<td>The operation failed because the selected stage isn’t the same as the active stage.</td>
</tr>
<tr>
<td>dirtyForm</td>
<td>This value will be returned if the data in the page is not saved.</td>
</tr>
<tr>
<td>stageGate</td>
<td>One or more required column on the current stage is empty.</td>
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

[movePrevious](movePrevious.md)

[formContext.data.process](../../formContext-data-process.md)
 




[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]