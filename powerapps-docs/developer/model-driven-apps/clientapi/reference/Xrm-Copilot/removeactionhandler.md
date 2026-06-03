---
title: "removeActionHandler (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the removeActionHandler method.
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

# removeActionHandler (Client API reference)

[!INCLUDE[removeactionhandler-description](includes/removeactionhandler-description.md)]

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

The method removes only the specific function reference you pass. It doesn't affect other handlers for the same `actionId`. If Microsoft 365 Copilot isn't enabled, the method does nothing.

## Example

```javascript
const handler = async (data) => { /* ... */ };

await Xrm.Copilot.addActionHandler("My.Namespace.MyActionMessage", handler);

// Later, when no longer needed:
await Xrm.Copilot.removeActionHandler("My.Namespace.MyActionMessage", handler);
```

### Related articles

[addActionHandler](addactionhandler.md)   
[Xrm.Copilot (Client API reference)](../xrm-copilot.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
