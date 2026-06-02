---
title: SendPromptToM365CopilotOptions Interface (Client API reference)
description: The interface that describes the optional parameters for the Xrm.Copilot.sendPromptToM365Copilot method.
author: devkeydet
ms.author: marcsc
ms.date: 06/02/2026
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
  - JimDaly
---

# SendPromptToM365CopilotOptions interface (Client API reference)

[!INCLUDE [sendprompttom365copilotoptions-description](includes/sendprompttom365copilotoptions-description.md)]

## Properties

| Name| Type| Description|
|---|---|---|
| `gptId`| `string`| ID of a specific M365 Copilot agent to target. If omitted, the prompt is sent to the default Copilot experience.|
| `autoSubmit`| `boolean`| When `false`, the prompt text is placed in the Copilot input box but not submitted, so the user can review or edit it first. Defaults to `true`.|

### Related articles

[sendPromptToM365Copilot method](sendprompttom365copilot.md)   
[Xrm.Copilot (Client API reference)](../xrm-copilot.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
