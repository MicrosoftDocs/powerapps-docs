---
title: "removeActionHandler (Client API reference) in model-driven apps (preview)"
description: Includes description and supported parameters for the removeActionHandler method.
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

# removeActionHandler (Client API reference) (preview)

[!INCLUDE [preview-note-pp](~/../shared-content/shared/preview-includes/preview-note-pp.md)]

[!INCLUDE[./includes/removeactionhandler-description.md](./includes/removeactionhandler-description.md)]

## Syntax

`Xrm.Copilot.removeActionHandler(actionId, actionHandler).then(successCallback, errorCallback);`

## Parameters

| Parameter Name| Type| Required | Description|
| --- | --- | --- | --- |
| `actionId` | string | Yes | The unique identifier of the action.|
| `actionHandler` | Function | Yes | The handler to remove. Must be the same function reference passed to [addActionHandler](addactionhandler.md).|
| `successCallback` | Function | Yes | A function to call when the operation succeeds.|
| `errorCallback`   | Function | Yes | A function to call when the operation fails.|

## Return Value

Type: `Promise<void>`

## Remarks

Only the specific function reference passed is removed. Other handlers for the same `actionId` are unaffected. Does nothing if Microsoft 365 Copilot is not enabled.

## Example

```javascript
const handler = async (data) => { /* ... */ };

await Xrm.Copilot.addActionHandler("MS.PA.CopilotChat.OpenRecord", handler);

// Later, when no longer needed:
await Xrm.Copilot.removeActionHandler("MS.PA.CopilotChat.OpenRecord", handler);
```

### Related articles

[addActionHandler](addactionhandler.md)  
[Xrm.Copilot (Client API reference)](../xrm-copilot.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
