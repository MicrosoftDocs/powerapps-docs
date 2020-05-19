---
title: "getEventSource (Client API reference) in model-driven apps| MicrosoftDocs"
description: "Learn about the getEventSource method that returns a reference to the object that the event occurred on." 
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
# getEventSource (Client API reference)



Returns a reference to the object that the event occurred on.

## Syntax

`ExecutionContextObj.getEventSource()`

## Return value

**Type**: Object

**Description**: Returns the object from the **Xrm** object model that is the source of the event, not an HTML DOM object. For example, in an [OnChange](../events/attribute-onchange.md) event, this method returns the **formContext.data.entity** attribute object that represents the changed attribute.

|Events|Return Object|
|-------|------------|
|[OnDataLoad](../events/form-data-onload.md)|[formContext.data.entity](../formcontext-data-entity.md)|
|[OnGridDataLoad](../events/subgrid-onload.md)|[formContext.ui.SubGridControl](../controls.md#subgrid-control-type)|
|[OnPostSearch](../events/postsearch.md)|[formContext.ui.kbSearchControl](../controls.md#kbsearch-knowledge-base-search-control-type)|
|[OnResultOpened](../events/onresultopened.md)|[formContext.ui.kbSearchControl](../controls.md#kbsearch-knowledge-base-search-control-type)|
|[OnSelection](../events/onselection.md)|None|
|[OnChange](../events/attribute-onchange.md)|[attribute](../attributes.md)|
|[OnLoad](../events/form-onload.md)|[formContext.ui](../formcontext-ui.md)|
|[OnLookupTagClick](../events/onlookuptagclick.md)|[formContext.ui.LookupControl](../controls.md#lookup-control-type)|
|[OnProcessStatusChange](../events/onprocessstatuschange.md)|[formContext.data.process](../formcontext-data-process.md)|
|[OnReadyStateComplete](../events/onreadystatecomplete.md)|[formContext.ui.IFrameControl](../controls.md#iframe-control-type)|
|[OnProcessStatusChange](../events/onprocessstatuschange.md)|[formContext.data.process](../formcontext-data-process.md)|
|[OnRecordSelect](../events/grid-onrecordselect.md)|[formContext.data.entity](../formcontext-data-entity.md)|
|[OnSave](../events/form-onsave.md)|[formContext.data.entity](../formcontext-data-entity.md)|
|[OnStageChange](../events/onstagechange.md)|[formContext.data.process](../formcontext-data-process.md)|
|[OnStageSelected](../events/onstageselected.md)|[formContext.data.process](../formcontext-data-process.md)|
|[OnTabStateChange](../events/tabstatechange.md)|[formContext.ui.tab](../formcontext-ui-tabs.md)|
|[PreSearch](../events/presearch.md)|[formContext.ui.LookupControl](../controls.md#lookup-control-type)|


### Related topics

[Execution context](../execution-context.md)
