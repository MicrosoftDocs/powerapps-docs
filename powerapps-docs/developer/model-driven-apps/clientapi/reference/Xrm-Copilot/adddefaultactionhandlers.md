---
title: "addDefaultActionHandlers (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the addDefaultActionHandlers method.
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

# addDefaultActionHandlers (Client API reference)

[!INCLUDE[adddefaultactionhandlers-description](includes/adddefaultactionhandlers-description.md)]

## Syntax

`Xrm.Copilot.addDefaultActionHandlers(actionId).then(successCallback, errorCallback);`

## Parameters

| Parameter Name| Type| Required | Description|
| --- | --- | --- | --- |
| `actionId` | string | Yes | The action ID to restore defaults for. Must be one of the built-in action IDs defined in [addActionHandler](addactionhandler.md).|
| `successCallback` | Function | Yes | A function to call when the operation succeeds.|
| `errorCallback`   | Function | Yes | A function to call when the operation fails.|

## Return Value

Type: `Promise<void>`

## Remarks

Does nothing if Microsoft 365 Copilot isn't enabled.

## Example

```javascript
await Xrm.Copilot.addDefaultActionHandlers("MS.PA.CopilotChat.OpenRecord");
```

### Related articles

[removeDefaultActionHandlers](removedefaultactionhandlers.md)  
[Xrm.Copilot (Client API reference)](../xrm-copilot.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
