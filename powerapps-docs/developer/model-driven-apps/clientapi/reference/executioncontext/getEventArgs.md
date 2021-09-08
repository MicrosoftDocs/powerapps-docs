---
title: "getEventArgs (Client API reference) in model-driven apps| MicrosoftDocs"
description: "Learn about the getEventArgs method that returns an object with methods to manage the **Save** event." 
ms.date: 10/31/2018
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 9f3b2fed-fde5-46e4-8c59-43aa51aa82df
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# getEventArgs (Client API reference)

Returns an object with methods to manage the events.

## Syntax

`ExecutionContextObj.getEventArgs()`

## Return value

**Type**: Object

**Description**: See the below table for the object type information:

|Events|Return Object|
|-------|------------|
|[OnChange](../events/attribute-onchange.md)|None|
|[OnDataLoad](../events/form-data-onload.md)|When the form `OnDataLoad` event occurs, you can use the `getEventArgs` method of the execution context object to retrieve an object that contains the following method: <br/> **getDataLoadState**: Gets the state of the data load. It returns an enum with the following values:<br/> - *InitialLoad =1*<br/>- *Save = 2*<br/>- *Refresh = 3*|
|[OnGridDataLoad](../events/subgrid-onload.md)|None|
|[OnLoad](../events/form-onload.md)|When the form `OnLoad` event occurs, you can use the `getEventArgs` method of the execution context object to retrieve an object that contains the following method: <br/>**getDataLoadState**: Gets the state of the data load. It returns an enum with the following values:<br/> - *InitialLoad =1*<br/>- *Save = 2*<br/>- *Refresh = 3*|
|[OnLookupTagClick](../events/onlookuptagclick.md)| When the form `OnLookupTagClick` event occurs, you can use the `getEventArgs` method of the execution context object to retrieve an object that contains the following methods: <br/>- **getTagValue**: Gets the selected tag value. The value returned for  the `getTagValue` method is a [LookupValue](../attributes/getvalue.md).<br/>- [preventDefault](../save-event-arguments/preventdefault.md)<br/> - [isDefaultPrevented](../save-event-arguments/isdefaultprevented.md)|
|[OnPostSearch](../events/postsearch.md)|None|
|[OnProcessStatusChange](../events/onprocessstatuschange.md)|When the form `OnProcessStatusChange` event occurs, you can use the `getEventArgs` method of the execution context object to retrieve an object that contains the following methods: <br/> - **getStage**: Gets the stage object corresponding to the event triggered. Returns the selected stage in for the `OnStageSelected` event and next or previous stage objects for the `OnStageChange` event depending on direction moved. More information: [Stage methods](../formcontext-data-process.md#stage-methods).<br/>- **getDirection**: Gets the direction of the stage advance action. It returns a string value `Next` or `Previous`.|
|[OnReadyStateComplete](../events/onreadystatecomplete.md)|None|
|[OnRecordSelect](../events/grid-onrecordselect.md)|None|
|[OnResultOpened](../events/onresultopened.md)|None|
|[OnSave](../events/form-onsave.md)|When the form `OnSave` event occurs, you can use the `getEventArgs` method of the execution context object to retrieve an object that contains the following methods: <br/>- [getSaveMode](../save-event-arguments/getsavemode.md)<br/>- [preventDefault](../save-event-arguments/preventdefault.md)<br/> - [isDefaultPrevented](../save-event-arguments/isdefaultprevented.md)|
|[OnSelection](../events/onselection.md)|None|
|[OnStageChange](../events/onstagechange.md)|When the form `OnStageChange` event occurs, you can use the `getEventArgs` method of the execution context object to retrieve an object that contains the following methods: <br/>- **getStage**: Gets the stage object corresponding to the event triggered. Returns the selected stage in for the `OnStageSelected` event and next or previous stage objects for the `OnStageChange` event depending on direction moved.More information: [Stage methods](../formcontext-data-process.md#stage-methods).<br/>- **getDirection**: Gets the direction of the stage advance action. It returns a string value `Next` or `Previous`.|
|[OnStageSelected](../events/onstageselected.md)|When the form `OnStageSelected` event occurs, you can use the `getEventArgs` method of the execution context object to retrieve an object that contains the following methods: <br/>- **getStage**: Gets the stage object corresponding to the event triggered. Returns the selected stage in for the `OnStageSelected` event and next or previous stage objects for the `OnStageChange` event depending on direction moved. More information: [Stage methods](../formcontext-data-process.md#stage-methods).<br/>- **getDirection**: Gets the direction of the stage advance action. It returns a string value `Next` or `Previous`.|
|[OnTabStateChange](../events/tabstatechange.md)|None|
|[PreSearch](../events/presearch.md)|None|
|||
### Related topics

[Execution context](../execution-context.md)







[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]