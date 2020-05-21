---
title: "getEventArgs (Client API reference) in model-driven apps| MicrosoftDocs"
description: "Learn about the getEventArgs method that returns an object with methods to manage the **Save** event." 
ms.date: 10/31/2018
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 9f3b2fed-fde5-46e4-8c59-43aa51aa82df
author: "KumarVivek"
ms.author: "kvivek"
manager: "annbe"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# getEventArgs (Client API reference)



Returns an object with methods to manage the **Save** event.

## Syntax

`ExecutionContextObj.getEventArgs()`

## Return value

**Type**: Object

**Description**: See [Save Event Arguments](../save-event-arguments.md).

|Events|Return Object|
|-------|------------|
|[OnChange](../events/attribute-onchange.md)|None|
|[OnDataLoad](../events/form-data-onload.md)|**getDataLoadState**: Gets the state of the data load. It returns the following enums:<br/> - *InitialLoad =1*<br/>- *Save = 2*<br/>- *Refresh = 3*|
|[OnGridDataLoad](../events/subgrid-onload.md)|None|
|[OnLoad](../events/form-onload.md)|**getDataLoadState**: Gets the state of the data load. It returns the following enums:<br/> - *InitialLoad =1*<br/>- *Save = 2*<br/>- *Refresh = 3*|
|[OnLookupTagClick](../events/onlookuptagclick.md)| Returns a [LookupValue](../attributes/getvalue.md#return-value). It returns the following:<br/> - **getTagValue**: Gets the selected tag value.|
|[OnPostSearch](../events/postsearch.md)|None|
|[OnProcessStatusChange](../events/onprocessstatuschange.md)|- **getStage**: Gets the stage object corresponding to the event triggered. Returns the selected stage in for the `OnStageSelected` event and next or previous stage objects for the `OnStageChange` event depending on direction moved.<br/>- **getDirection**: Gets the direction (Next / Previous) of the stage advance action.|
|[OnReadyStateComplete](../events/onreadystatecomplete.md)|None|
|[OnRecordSelect](../events/grid-onrecordselect.md)|None|
|[OnResultOpened](../events/onresultopened.md)|None|
|[OnSave](../events/form-onsave.md)|[getSaveMode](../save-event-arguments/getsavemode.md)|
|[OnSelection](../events/onselection.md)|None|
|[OnStageChange](../events/onstagechange.md)|- **getStage**: Gets the stage object corresponding to the event triggered. Returns the selected stage in for the `OnStageSelected` event and next or previous stage objects for the `OnStageChange` event depending on direction moved.<br/>- **getDirection**: Gets the direction (Next / Previous) of the stage advance action.|
|[OnStageSelected](../events/onstageselected.md)|- **getStage**: Gets the stage object corresponding to the event triggered. Returns the selected stage in for the `OnStageSelected` event and next or previous stage objects for the `OnStageChange` event depending on direction moved.<br/>- **getDirection**: Gets the direction (Next / Previous) of the stage advance action. |
|[OnTabStateChange](../events/tabstatechange.md)|None|
|[PreSearch](../events/presearch.md)|None|


### Related topics

[Execution context](../execution-context.md)





