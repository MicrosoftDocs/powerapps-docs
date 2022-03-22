---
title: "Save event arguments (Client API reference) in model-driven apps| MicrosoftDocs"
ms.author: jdaly
author: adrianorth
manager: kvivek
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.subservice: mda-developer
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
  - JimDaly
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