---
title: "getEventArgs (Client API reference) in model-driven apps"
description: "Learn about the getEventArgs method that returns an object with methods to manage the **Save** event." 
author: sriharibs-msft
ms.author: srihas
ms.date: 11/02/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# getEventArgs (Client API reference)

Returns an object with methods to manage the events.

## Syntax

`ExecutionContextObj.getEventArgs()`

## Return value

**Type**: Object

**Description**: When a specified event occurs, you can use the `getEventArgs` method of the execution context object to retrieve an object that may contain additional methods you can use. The table below describes the methods:

|Events|Return Object Methods|
|-------|------------|
|[OnChange](../events/attribute-onchange.md)|None|
|[OnDataLoad](../events/form-data-onload.md)|**`getDataLoadState`**: Gets the state of the data load. It returns an enum with the following values:<br/> - *InitialLoad =1*<br/>- *Save = 2*<br/>- *Refresh = 3*|
|[OnGridDataLoad](../events/subgrid-onload.md)|None|
|[OnLoad](../events/form-onload.md)|**`getDataLoadState`**: Gets the state of the data load. It returns an enum with the following values:<br/> - *InitialLoad =1*<br/>- *Save = 2*<br/>- *Refresh = 3*|
|[OnLookupTagClick](../events/onlookuptagclick.md)| - **`getTagValue`**: Gets the selected tag value. The value returned for  the `getTagValue` method is a [LookupValue](../attributes/getvalue.md).<br/>- [preventDefault](../save-event-arguments/preventdefault.md): [!INCLUDE [preventDefault-description](../save-event-arguments/includes/preventDefault-description.md)]<br/> - [isDefaultPrevented](../save-event-arguments/isdefaultprevented.md): [!INCLUDE [isDefaultPrevented-description](../save-event-arguments/includes/isDefaultPrevented-description.md)]|
|[OnPostSearch](../events/postsearch.md)|None|
|[OnPostSave Event](../events/postsave.md)|- [getEntityReference](../save-event-arguments/getEntityReference.md): [!INCLUDE [getEntityReference-description](../formContext-data-entity/includes/getEntityReference-description.md)]<br /> - [getIsSaveSuccess](../save-event-arguments/getIsSaveSuccess.md): Returns data about whether the save operation succeeded.<br /> -  [getSaveErrorInfo](../save-event-arguments/getSaveErrorInfo.md): If the save operation failed, returns data about why it failed.|
|[OnProcessStatusChange](../events/onprocessstatuschange.md)|- **`getStatus`**: Returns the Business Process Flow status: `Active`, `Finished`, or `Aborted`.|
|[OnPreProcessStatusChange](../events/onpreprocessstatuschange.md)|- **`getStatus`**: Returns the Business Process Flow status: `Active`, `Finished`, or `Aborted`.|
|[OnPreStageChange event](../events/onprestagechange.md)|- **`getStage`**: Gets the stage object corresponding to the event triggered. Returns the selected stage in for the `OnStageSelected` event and next or previous stage objects for the `OnStageChange` event depending on direction moved. More information: [Stage methods](../formcontext-data-process.md#stage-methods).|
|[OnReadyStateComplete](../events/onreadystatecomplete.md)|None|
|[OnRecordSelect](../events/grid-onrecordselect.md)|None|
|[OnResultOpened](../events/onresultopened.md)|None|
|[OnSave](../events/form-onsave.md)|- [getSaveMode](../save-event-arguments/getsavemode.md): [!INCLUDE [getSaveMode-description](../save-event-arguments/includes/getSaveMode-description.md)]<br/>- [preventDefault](../save-event-arguments/preventdefault.md): [!INCLUDE [preventDefault-description](../save-event-arguments/includes/preventDefault-description.md)]<br/> - [isDefaultPrevented](../save-event-arguments/isdefaultprevented.md): [!INCLUDE [isDefaultPrevented-description](../save-event-arguments/includes/isDefaultPrevented-description.md)] <br/> If the event is async and async handlers are enabled, the following are also available: <br/> - [preventDefaultOnError](../save-event-arguments/preventDefaultOnError.md): Cancels the save operation if the event handler has a script error.<br/> - [disableAsyncTimeout](../events/form-onsave.md#async-onsave-timeouts): Disables the default async handler timeout.|
|[OnSelection](../events/onselection.md)|None|
|[OnStageChange](../events/onstagechange.md)|- **`getStage`**: Gets the stage object corresponding to the event triggered. Returns the selected stage in for the `OnStageSelected` event and next or previous stage objects for the `OnStageChange` event depending on direction moved. More information: [Stage methods](../formcontext-data-process.md#stage-methods).<br/>- **`getDirection`**: Gets the direction of the stage advance action. It returns a string value `Next` or `Previous`.|
|[OnStageSelected](../events/onstageselected.md)|- **`getStage`**: Gets the stage object corresponding to the event triggered. Returns the selected stage in for the `OnStageSelected` event and next or previous stage objects for the `OnStageChange` event depending on direction moved. More information: [Stage methods](../formcontext-data-process.md#stage-methods).<br/>- **`getDirection`**: Gets the direction of the stage advance action. It returns a string value `Next` or `Previous`.|
|[OnTabStateChange](../events/tabstatechange.md)|None|
|[PreSearch](../events/presearch.md)|None|


### Related articles

[Execution context](../execution-context.md)







[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
