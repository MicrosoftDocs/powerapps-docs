---
title: "sendPromptToM365Copilot (Client API reference) in model-driven apps (preview)"
description: Includes description and supported parameters for the sendPromptToM365Copilot method.
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

# sendPromptToM365Copilot (Client API reference) (preview)

[!INCLUDE [preview-note-pp](~/../shared-content/shared/preview-includes/preview-note-pp.md)]

[!INCLUDE[./includes/sendprompttom365copilot-description.md](./includes/sendprompttom365copilot-description.md)]

## Syntax

`Xrm.Copilot.sendPromptToM365Copilot(promptText, options).then(successCallback, errorCallback);`

## Parameters

| Parameter Name| Type| Required | Description|
| --- | --- | --- | --- |
| `promptText` | string | Yes | The prompt text to send to the Microsoft 365 Copilot side panel.|
| `options` | [SendPromptToM365CopilotOptions](sendprompttom365copilotoptions.md) | No | Additional options, such as a target GPT ID or auto-submit behavior.|
| `successCallback` | Function | Yes | A function to call when the operation succeeds.|
| `errorCallback`   | Function | Yes | A function to call when the operation fails.|

## Return Value

Type: `Promise<void>`

## Remarks

Does nothing if Microsoft 365 Copilot is not enabled.

## Example

```javascript
await Xrm.Copilot.sendPromptToM365Copilot(
    "Summarize the recent activity for this account.",
    { gptId: "dddddddd-3333-4444-5555-eeeeeeeeeeee" }
);
```

### Related articles

[SendPromptToM365CopilotOptions](sendprompttom365copilotoptions.md)  
[Xrm.Copilot (Client API reference)](../xrm-copilot.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
