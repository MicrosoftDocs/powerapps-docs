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
|[OnGridDataLoad](../events/subgrid-onload.md)|[formContext.getControl](../grids/gridcontrol/addonload.md)|
|[OnPostSearch](../events/postsearch.md)	|[kbsearch](../controls/addonpostsearch.md)|
|[OnResultOpened](../events/onresultopened.md)|[kbsearch](../controls/addonresultopened.md)|
|[OnSelection](../events/onselection.md)|None|
|[OnChange](../events/attribute-onchange.md)|[formContext.data.entity.attributes](../attributes.md)|
|[OnLoad](../events/form-onload.md)	|[formContext.ui](../formcontext-ui.md)|
|[OnLookupTagClick](../events/onlookuptagclick.md)	|[formContext.getControl](../controls/addonlookuptagclick.md)|
|[OnProcessStatusChange](../events/onprocessstatuschange.md)|[formContext.data.process](../formcontext-data-process/eventhandlers/addonprocessstatuschange.md)|
|[OnReadyStateComplete](../events/onreadystatecomplete.md)	|formContext.Controls.FramedControl|
|[OnRecordSelect](../events/grid-onrecordselect.md)	|formContext.Entity|
|[OnSave](../events/form-onsave.md)	|[formContext.data.entity](../formcontext-data-entity/save.md)|
|[OnStageChange](../events/onstagechange.md)|	[formContext.data.process](../formcontext-data-process/eventhandlers/addonstagechange.md)|
|[OnStageSelected](../events/onstageselected.md)|	[formContext.data.process](../formcontext-data-process/eventhandlers/addonstageselected.md)|
|[OnTabStateChange](../events/tabstatechange.md)|[formContext.ui.tab](../formcontext-ui-tabs/addtabstatechange.md)|
|[PreSearch](../events/presearch.md)|	[formContext.getControl](../controls/addpresearch.md)|


### Related topics

[Execution context](../execution-context.md)





