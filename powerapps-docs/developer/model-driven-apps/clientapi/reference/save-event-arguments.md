---
title: "Save event arguments (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 10/31/2018
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: dff20ae0-c9ec-4413-9cd1-0ff77639ad91
author: "Nkrb"
ms.subservice: mda-developer
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Save event arguments (Client API reference)



When the form [OnSave](events/form-onsave.md) event occurs, you can use the [getEventArgs](executioncontext/getEventArgs.md) method of the execution context object to retrieve an object that contains methods you can use to manage the save event.

|Method|Description|
|--|--|
|[getSaveMode](save-event-arguments/getSaveMode.md)|[!INCLUDE[save-event-arguments/includes/getSaveMode-description.md](save-event-arguments/includes/getSaveMode-description.md)]|
|[isDefaultPrevented](save-event-arguments/isDefaultPrevented.md)|[!INCLUDE[save-event-arguments/includes/isDefaultPrevented-description.md](save-event-arguments/includes/isDefaultPrevented-description.md)]|
|[preventDefault](save-event-arguments/preventDefault.md)|[!INCLUDE[save-event-arguments/includes/preventDefault-description.md](save-event-arguments/includes/preventDefault-description.md)]|


## Related topics

[Client API execution context](../clientapi-execution-context.md)

[Execution context methods](execution-context.md)



[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]