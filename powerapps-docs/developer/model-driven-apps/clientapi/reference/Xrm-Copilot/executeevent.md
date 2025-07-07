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
| `eventName` | string | Yes | Event Name registered in the Microsoft Copilot Studio (MCS) topic  |
| `eventParameters` | Unknown  | Yes | Parameters needed for the event execution. These depend on what the topic does.|
| `successCallback` | Function | Yes | A function to call when the operation succeeds.|
| `errorCallback`   | Function | Yes | A function to call when the operation fails.|

## Return Value

An array of [MCSResponse](mcsresponse.md)

[!INCLUDE [accessing-app-context](../../includes/accessing-app-context.md)]

[!INCLUDE [accessing-event-parameters](../../includes/accessing-event-parameters.md)]


### Related articles

[Xrm.Copilot (Client API reference)](../xrm-copilot.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
