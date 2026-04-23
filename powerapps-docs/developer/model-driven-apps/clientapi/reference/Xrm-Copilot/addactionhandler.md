---
title: "addActionHandler (Client API reference) in model-driven apps (preview)"
description: Includes description and supported parameters for the addActionHandler method.
author: devkeydet
ms.author: marcsc
ms.date: 04/23/2026
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType:
  - developer
contributors:
  - JimDaly
---

# addActionHandler (Client API reference) (preview)

[!INCLUDE [preview-note-pp](~/../shared-content/shared/preview-includes/preview-note-pp.md)]

[!INCLUDE[./includes/addactionhandler-description.md](./includes/addactionhandler-description.md)]

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

Multiple handlers can be registered for the same `actionId` and run sequentially. Registering the same function reference twice for the same `actionId` is silently ignored. Does nothing if Microsoft 365 Copilot is not enabled.

### Built-in action IDs

The following action IDs have platform-default handlers registered automatically. Custom handlers can be added alongside them, or the defaults can be removed first using [removeDefaultActionHandlers](removedefaultactionhandlers.md).

| Action ID | Description | Data properties |
|---|---|---|
| `MS.PA.CopilotChat.OpenRecord` | Navigates to a record. | `entity` (string) — table logical name; `recordId` (string) — record ID |
| `MS.PA.CopilotChat.NavigateToView` | Navigates to a view. | `entity` (string) — table logical name; `fetchXml` (string) — FetchXML query |

## Example

```javascript
const handler = async ({ entity, recordId }) => {
    // Open the record in a side pane instead of navigating away
    const pane = Xrm.App.sidePanes.createPane({ canClose: true });
    await pane.navigate({ pageType: "entityrecord", entityName: entity, entityId: recordId });
};

await Xrm.Copilot.addActionHandler("MS.PA.CopilotChat.OpenRecord", handler);
```

### Related articles

[removeActionHandler](removeactionhandler.md)  
[Xrm.Copilot (Client API reference)](../xrm-copilot.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
