---
title: "removeDefaultActionHandlers (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the removeDefaultActionHandlers method.
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

# removeDefaultActionHandlers (Client API reference)

[!INCLUDE[removedefaultactionhandlers-description](includes/removedefaultactionhandlers-description.md)]

## Syntax

`Xrm.Copilot.removeDefaultActionHandlers(actionId).then(successCallback, errorCallback);`

## Parameters

| Parameter Name| Type| Required | Description|
| --- | --- | --- | --- |
| `actionId` | string | Yes | The action ID whose defaults you want to remove. Must be one of the built-in action IDs defined in [addActionHandler](addactionhandler.md).|
| `successCallback` | Function | Yes | A function to call when the operation succeeds.|
| `errorCallback`   | Function | Yes | A function to call when the operation fails.|

## Return Value

Type: `Promise<void>`

## Remarks

This method doesn't affect custom handlers registered through [addActionHandler](addactionhandler.md). To restore the default handlers, use [addDefaultActionHandlers](adddefaultactionhandlers.md). If Microsoft 365 Copilot isn't enabled, this method does nothing.

## Example

```javascript
// Replace default record navigation with custom behavior
await Xrm.Copilot.removeDefaultActionHandlers("MS.PA.CopilotChat.OpenRecord");

await Xrm.Copilot.addActionHandler("MS.PA.CopilotChat.OpenRecord", async ({ entity, recordId }) => {
    // custom implementation
});
```

### Related articles

[addDefaultActionHandlers](adddefaultactionhandlers.md)   
[Xrm.Copilot (Client API reference)](../xrm-copilot.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
