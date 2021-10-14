---
title: "setActiveStage (Client API reference) in model-driven apps| MicrosoftDocs"
description: Sets a completed stage as the active stage.
ms.date: 09/10/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 9c40a770-f4cb-4230-8893-0527f8472825
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# setActiveStage (Client API reference)

[!INCLUDE[./includes/setActiveStage-description.md](./includes/setActiveStage-description.md)]

## Syntax

`formContext.data.process.setActiveStage(stageId, callbackFunction);`

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
<td>stageId</td>
<td>String</td>
<td>Yes</td>
<td>The ID of the completed stage for the table to make the active stage. </td>
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
<td>invalid</td>
<td>There are three reasons why this value may be returned:
<ul>
<li>The *stageId* parameter is a non-existent stage ID value.</li>
<li>The active stage isn’t the selected stage.</li>
<li>The record hasn’t been saved yet.</li>
</ul>
</td>
</tr>
<tr>
<td>unreachable</td>
<td>The stage exists on a different path.</td>
</tr>
<tr>
<td>dirtyForm</td>
<td>This value will be returned if the data in the page is not saved.</td>
</tr>
<tr>
<td>preventDefault</td>
<td>This value will be returned if an `OnPreStageChange` event handler invokes preventDefault.</td>
</tr>
</table>
</td>
</tr>
</table>

>[!IMPORTANT]
>This method can only be used when the selected stage and the active stage are the same. When your code is initiated from the [OnStageChange](../../events/onstagechange.md) event, the current stage will be selected. When your code is initiated from the [OnStageSelected](../../events/onstageselected.md) event, you should use the [getActiveStage](getActiveStage.md) method to verify that the selected stage is also the active stage. For any other form event, it isn’t possible to determine which stage is currently selected. For best results, this method should only be used in code that is called in functions initiated by the [OnStageChange](../../events/onstagechange.md) and [OnStageSelected](../../events/onstageselected.md) events.

### Related topics

[getActiveStage](getActiveStage.md)

[formContext.data.process](../../formContext-data-process.md)
 




[!INCLUDE[footer-include](../../../../../../includes/footer-banner.md)]
