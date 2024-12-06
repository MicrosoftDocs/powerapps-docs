---
title: "getEventSource (Client API reference) in model-driven apps"
description: "Learn about the getEventSource method that returns a reference to the object that the event occurred on." 
author: sriharibs-msft
ms.author: srihas
ms.date: 05/15/2024
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# getEventSource (Client API reference)

Returns a reference to the object that the event occurred on.

## Syntax

`ExecutionContextObj.getEventSource()`

## Return value

**Type**: Object

**Description**: Returns the object from the **Xrm** object model that is the source of the event, not an HTML DOM object. For example, in an [OnChange](../events/attribute-onchange.md) event, this method returns an item from the **formContext.data.entity.attributes**  collection that represents the changed column.

[!INCLUDE[cc-terminology](../../../../data-platform/includes/cc-terminology.md)]

|Events|Return Object|
|-------|------------|
|[OnChange](../events/attribute-onchange.md)|[column](../attributes.md)|
|[OnDataLoad](../events/form-data-onload.md)|[formContext.data.entity](../formcontext-data-entity.md)|
|[OnGridDataLoad](../events/subgrid-onload.md)|[SubGrid](../controls.md#subgrid-control-type) control|
|[OnLoad](../events/form-onload.md)|[formContext.ui](../formcontext-ui.md)|
|[OnLookupTagClick](../events/onlookuptagclick.md)|[Lookup](../controls.md#lookup-control-type) control|
|[OnPostSearch](../events/postsearch.md)|[kbSearch](../controls.md#kbsearch-knowledge-base-search-control-type) control|
|[OnProcessStatusChange](../events/onprocessstatuschange.md)|[formContext.data.process](../formcontext-data-process.md)|
|[OnProcessStatusChange](../events/onprocessstatuschange.md)|[formContext.data.process](../formcontext-data-process.md)|
|[OnReadyStateComplete](../events/onreadystatecomplete.md)|[IFrame](../controls.md#iframe-control-type) control|
|[OnRecordSelect](../events/grid-onrecordselect.md)|[formContext.data.entity](../formcontext-data-entity.md)|
|[OnResultOpened](../events/onresultopened.md)|[kbSearch](../controls.md#kbsearch-knowledge-base-search-control-type) control|
|[OnSave](../events/form-onsave.md)|[formContext.data.entity](../formcontext-data-entity.md)|
|[OnPostSave](../events/postsave.md)|None|
|[OnSelection](../events/onselection.md)|None|
|[OnStageChange](../events/onstagechange.md)|[formContext.data.process](../formcontext-data-process.md)|
|[OnStageSelected](../events/onstageselected.md)|[formContext.data.process](../formcontext-data-process.md)|
|[OnTabStateChange](../events/tabstatechange.md)|[tab](../formcontext-ui-tabs.md) object|
|[PreSearch](../events/presearch.md)|[Lookup](../controls.md#lookup-control-type) control|


### Related articles

[Execution context](../execution-context.md)


[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
