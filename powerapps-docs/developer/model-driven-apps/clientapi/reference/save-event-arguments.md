---
title: "Save event arguments (Client API reference) in model-driven apps"
description: "When the form OnSave event occurs, you can use the getEventArgs method of the execution context object to retrieve an object that contains methods you can use to manage the save event."
author: MitiJ
ms.author: mijosh
ms.date: 01/16/2024
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
ms.subservice: mda-developer
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# Save event arguments (Client API reference)

When the form [OnSave](events/form-onsave.md) event occurs, you can use the [getEventArgs](executioncontext/getEventArgs.md) method of the execution context object to retrieve an object that contains methods you can use to manage the save event.

|Method|Description|
|----|----|
|[getSaveMode](save-event-arguments/getSaveMode.md)|[!INCLUDE[save-event-arguments/includes/getSaveMode-description.md](save-event-arguments/includes/getSaveMode-description.md)]|
|[isDefaultPrevented](save-event-arguments/isDefaultPrevented.md)|[!INCLUDE[save-event-arguments/includes/isDefaultPrevented-description.md](save-event-arguments/includes/isDefaultPrevented-description.md)]|
|[preventDefault](save-event-arguments/preventDefault.md)|[!INCLUDE[save-event-arguments/includes/preventDefault-description.md](save-event-arguments/includes/preventDefault-description.md)]|
|[preventDefaultOnError](save-event-arguments/preventDefaultOnError.md)|[!INCLUDE [preventDefaultOnError-description](save-event-arguments/includes/preventDefaultOnError-description.md)]|
|[disableAsyncTimeout](save-event-arguments/disableasynctimeout.md)|[!INCLUDE [disableAsyncTimeout-description](save-event-arguments/includes/disableAsyncTimeout-description.md)]|

## PostSave event arguments

When the form [OnPostSave](events/postsave.md) event occurs, you can use the [getEventArgs](executioncontext/getEventArgs.md) method of the execution context object to retrieve an object that contains methods you can use to manage the postsave event.

|Method|Description|
|----|----|
|[getEntityReference](save-event-arguments/getEntityReference.md)|Use this method to know information about a table being saved. It returns the table logical name, record ID, and table name if save was successful.|
|[getIsSaveSuccess](save-event-arguments/getIsSaveSuccess.md)|Use this method to know whether the save operation was successful or failed.|
|[getSaveErrorInfo](save-event-arguments/getSaveErrorInfo.md)|Use this method to know the error details on why save failed.|

## Related articles

[Client API execution context](../clientapi-execution-context.md)   
[Execution context methods](execution-context.md)


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
