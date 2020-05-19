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

**Description**: Returns the object from the **Xrm** object model that is the source of the event, not an HTML DOM object. For example, in an [OnChange](../events/attribute-onchange.md) event, this method returns the **formContext.Attributes.Attribute** attribute object that represents the changed attribute.

|Events|Return Object|
|-------|------------|
|[OnDataLoad](../events/form-data-onload.md)|fromContext.data.Entity|
|[OnGridDataLoad](../events/subgrid-onload.md)	|fromContext.Controls.SubGridControl|
|[OnPostSearch](../events/postsearch.md)	|fromContext.Controls.SearchWidgetControl|
|[OnResultOpened](../events/onresultopened.md)	|fromContext.Controls.SearchWidgetControl|
|[OnSelection](../events/onselection.md)|None|
|[OnChange](../events/attribute-onchange.md)|fromContext.Attributes.Attribute|
|[OnLoad](../events/form-onload.md)	|fromContext.FormUi|
|[OnLookupTagClick](../events/onlookuptagclick)	|fromContext.Controls.LookupControl|
|[OnProcessStatusChange](../events/onprocessstatuschange.md)|fromContext.Process.Process|
|[OnReadyStateComplete](../events/onreadystatecomplete.md)	|fromContext.Controls.FramedControl|
|[OnRecordSelect](../events/grid-onrecordselect.md)	|fromContext.Entity|
|[OnSave](../events/form-onsave.md)	|fromContext.Entity|
|[OnStageChange](../events/onstagechange.md)|	fromContext.Process.Stage|
|[OnStageSelected](../events/onstageselected.md)|	fromContext.Process.Stage|
|[OnTabStateChange](../events/tabstatechange.md)|fromContext.Controls.Tab|
|[PreSearch](../events/presearch.md)|	fromContext.Controls.LookupControl|


### Related topics
[Execution context](../execution-context.md)





