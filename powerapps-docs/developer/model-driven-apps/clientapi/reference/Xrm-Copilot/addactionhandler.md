---
title: "addActionHandler (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the addActionHandler method.
author: devkeydet
ms.author: marcsc
ms.date: 06/02/2026
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType:
  - developer
contributors:
  - JimDaly
---

# addActionHandler (Client API reference)

[!INCLUDE[addactionhandler-description](includes/addactionhandler-description.md)]

## Syntax

`Xrm.Copilot.addActionHandler(actionId, actionHandler).then(successCallback, errorCallback);`

## Parameters

| Parameter Name| Type| Required | Description|
| --- | --- | --- | --- |
| `actionId` | string | Yes | The unique identifier of the action to handle.|
| `actionHandler` | Function | Yes | The function to invoke when the action is triggered. Receives the action's data payload as an argument.|
| `successCallback` | Function | Yes | A function to call when the operation succeeds.|
| `errorCallback`   | Function | Yes | A function to call when the operation fails.|

## Return Value

Type: `Promise<void>`

## Remarks

You can register multiple handlers for the same `actionId`. They run sequentially. The API silently ignores registering the same function reference twice for the same `actionId`. The API does nothing if Microsoft 365 Copilot isn't enabled.

### Built-in action IDs

The following action IDs have platform-default handlers registered automatically. You can add custom handlers alongside them, or remove the default handlers first by using [removeDefaultActionHandlers](removedefaultactionhandlers.md).

| Action ID | Description | Data properties |
|---|---|---|
| `MS.PA.CopilotChat.OpenRecord` | Opens a record. | `entity` (string) — table logical name; `recordId` (string) — record ID |
| `MS.PA.CopilotChat.NavigateToView` | Navigates to a view. | `entity` (string) — table logical name; `fetchXml` (string) — FetchXML query |

## Example

```javascript
const handler = async ({ entity, recordId }) => {
    // Open the record in a side pane instead of navigating away
    const pane = Xrm.App.sidePanes.createPane({ canClose: true });
    await pane.navigate({ pageType: "entityrecord", entityName: entity, entityId: recordId });
};

await Xrm.Copilot.addActionHandler("My.Namespace.MyActionMessage", handler);
```

### Related articles

[removeActionHandler method](removeactionhandler.md)  
[Xrm.Copilot (Client API reference)](../xrm-copilot.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
