---
title: "executeEvent (Client API reference) in model-driven apps (preview)"
description: Includes description and supported parameters for the executeEvent method.
author: adrianorth
ms.author: aorth
ms.date: 06/02/2026
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType:
  - developer
contributors:
  - JimDaly
---

# executeEvent (Client API reference) (preview)

[!INCLUDE [preview-note-pp](~/../shared-content/shared/preview-includes/preview-note-pp.md)]

[!INCLUDE[executeevent-description](includes/executeevent-description.md)]

## Syntax

`Xrm.Copilot.executeEvent(eventName, eventParameters).then(successCallback, errorCallback); `

## Parameters

| Parameter Name| Type| Required | Description|
| --- | --- | --- | --- |
| `eventName` | string | Yes | Event name registered in the Microsoft Copilot Studio topic  |
| `eventParameters` | Unknown  | Yes | Parameters needed for the event execution. These depend on what the topic does.|
| `successCallback` | Function | Yes | A function to call when the operation succeeds.|
| `errorCallback`   | Function | Yes | A function to call when the operation fails.|

## Return Value

An array of [MCSResponse](mcsresponse.md).

## Accessing app context

When you call an Agent API, the Copilot Studio topic receives the app context through a set of variables. The following context variables are available as [Copilot Studio global variables](/microsoft-copilot-studio/authoring-variables-bot).

[!INCLUDE [app-context-table](../../includes/app-context-table.md)]

For example, by using `Global.PA__Copilot_Model_PageContext.pageContext.id.guid` and `Global.PA__Copilot_Model_PageContext.pageContext.entityTypeName`, you can retrieve the form's record from Dataverse.

[!INCLUDE [accessing-event-parameters](../../includes/accessing-event-parameters.md)]

### Example

In Microsoft Copilot Studio, register a topic that accepts an ID (entity record ID) as an input parameter. Based on the input, the topic retrieves the related activities of that entity record and returns the results as a Copilot Studio event activity.

```javascript
const response = await Xrm.Copilot.executeEvent( 
    "Microsoft.PowerApps.Copilot.RelatedActivities", 
    { id:"aaaaaaaa-0000-1111-2222-bbbbbbbbbbbb"}); 
```

[!INCLUDE [accessing-event-parameters-response](../../includes/accessing-event-parameters-response.md)]


### Related articles

[Xrm.Copilot (Client API reference)](../xrm-copilot.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
