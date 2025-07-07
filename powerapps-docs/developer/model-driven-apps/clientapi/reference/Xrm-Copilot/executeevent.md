---
title: "executeEvent (Client API reference) in model-driven apps (preview)"
description: Includes description and supported parameters for the executeEvent method.
author: adrianorth
ms.author: aorth
ms.date: 07/07/2025
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType:
  - developer
contributors:
  - JimDaly
---

# executeEvent (Client API reference)  (preview)

[!INCLUDE [preview-note-pp](~/../shared-content/shared/preview-includes/preview-note-pp.md)]

[!INCLUDE[./includes/executeevent-description.md](./includes/executeevent-description.md)]

## Syntax

`Xrm.Copilot.executeEvent(eventName, eventParameters).then(successCallback, errorCallback); `

## Parameters

| Parameter Name| Type| Required | Description|
| --- | --- | --- | --- |
| `eventName` | string | Yes | Event Name registered in the Microsoft Copilot Studio topic  |
| `eventParameters` | Unknown  | Yes | Parameters needed for the event execution. These depend on what the topic does.|
| `successCallback` | Function | Yes | A function to call when the operation succeeds.|
| `errorCallback`   | Function | Yes | A function to call when the operation fails.|

## Return Value

An array of [MCSResponse](mcsresponse.md)

## Accessing app context

When an Agent API is called, context for the app is passed to the Copilot Studio topic through a set of variables. The following are context variables available as [Copilot Studio global variables](/microsoft-copilot-studio/authoring-variables-bot).

[!INCLUDE [app-context-table](../../includes/app-context-table.md)]

For example, using `Global.PA__Copilot_Model_PageContext.pageContext.id.guid` and `Global.PA__Copilot_Model_PageContext.pageContext.entityTypeName`, the form's record can be retrieved from Dataverse.

[!INCLUDE [accessing-event-parameters](../../includes/accessing-event-parameters.md)]


### Related articles

[Xrm.Copilot (Client API reference)](../xrm-copilot.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
