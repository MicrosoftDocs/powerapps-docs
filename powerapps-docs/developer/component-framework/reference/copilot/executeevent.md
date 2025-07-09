---
title: executeEvent (Power Apps component framework API reference) (preview)
description: Executes a Microsoft Copilot Studio topic based on the registered Event Name. 
author: adrianorth
ms.author: aorth
ms.date: 07/07/2025
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
---

# executeEvent (preview)

[!INCLUDE [preview-note-pp](~/../shared-content/shared/preview-includes/preview-note-pp.md)]

[!INCLUDE[./includes/executeevent-description.md](./includes/executeevent-description.md)]

## Available for

Model-driven apps

## Syntax

`context.copilot.executeEvent(eventName, eventParameters).then(successCallback, errorCallback);`

## Parameters

| Parameter Name| Type| Required | Description|
| --- | --- | --- | --- |
| `eventName` | string | Yes | Event Name registered in the Copilot Studio topic  |
| `eventParameters` | Unknown  | Yes | Parameters needed for the event execution. These depend on what the topic does.|
| `successCallback` | Function | Yes | A function to call when the operation succeeds.|
| `errorCallback`   | Function | Yes | A function to call when the operation fails.|

## Return Value

Type: `Promise<`[MCSResponse](mcsresponse.md)`>`

See [Promise](https://developer.mozilla.org/docs/Web/JavaScript/reference/Global_Objects/Promise) and [MCSResponse](mcsresponse.md)

## Accessing app context

When an Agent API is called, context for the app is passed to the Copilot Studio topic through a set of variables. The following are context variables available as [Copilot Studio global variables](/microsoft-copilot-studio/authoring-variables-bot).

[!INCLUDE [app-context-table](../../../model-driven-apps/clientapi/includes/app-context-table.md)]

For example, using `Global.PA__Copilot_Model_PageContext.pageContext.id.guid` and `Global.PA__Copilot_Model_PageContext.pageContext.entityTypeName`, the form's record can be retrieved from Dataverse.

[!INCLUDE [accessing-event-parameters](../../../model-driven-apps/clientapi/includes/accessing-event-parameters.md)]


### Related articles

[Copilot](../copilot.md)  
[executePrompt](executeprompt.md)  
[Power Apps component framework API reference](../../reference/index.md)  
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
