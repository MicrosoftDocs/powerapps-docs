---
title: "removeDefaultActionHandlers (Client API reference) in model-driven apps (preview)"
description: Includes description and supported parameters for the removeDefaultActionHandlers method.
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

# removeDefaultActionHandlers (Client API reference)

[!INCLUDE[./includes/removedefaultactionhandlers-description.md](./includes/removedefaultactionhandlers-description.md)]

## Syntax

`Xrm.Copilot.removeDefaultActionHandlers(actionId).then(successCallback, errorCallback);`

## Parameters

| Parameter Name| Type| Required | Description|
| --- | --- | --- | --- |
| `actionId` | string | Yes | The action ID whose defaults should be removed. Must be one of the built-in action IDs defined in [addActionHandler](addactionhandler.md).|
| `successCallback` | Function | Yes | A function to call when the operation succeeds.|
| `errorCallback`   | Function | Yes | A function to call when the operation fails.|

## Return Value

Type: `Promise<void>`

## Remarks

Custom handlers registered via [addActionHandler](addactionhandler.md) are not affected. Use [addDefaultActionHandlers](adddefaultactionhandlers.md) to restore the defaults. Does nothing if Microsoft 365 Copilot is not enabled.

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
