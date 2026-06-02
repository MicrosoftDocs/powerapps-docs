---
title: "openM365CopilotPanel (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the openM365CopilotPanel method.
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

# openM365CopilotPanel (Client API reference)

[!INCLUDE[openm365copilotpanel-description](includes/openm365copilotpanel-description.md)]

## Syntax

`Xrm.Copilot.openM365CopilotPanel().then(successCallback, errorCallback);`

## Parameters

| Parameter Name| Type| Required | Description|
| --- | --- | --- | --- |
| `successCallback` | Function | Yes | A function to call when the operation succeeds.|
| `errorCallback`   | Function | Yes | A function to call when the operation fails.|

## Return Value

Type: `Promise<void>`

## Remarks

If the panel is already open, this method ensures it is initialized. Does nothing if Microsoft 365 Copilot is not enabled.

## Example

```javascript
await Xrm.Copilot.openM365CopilotPanel();
```

### Related articles

[Xrm.Copilot (Client API reference)](../xrm-copilot.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
