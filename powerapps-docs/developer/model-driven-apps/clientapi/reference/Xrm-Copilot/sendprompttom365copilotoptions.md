---
title: SendPromptToM365CopilotOptions Interface (Client API reference) (preview)
description: The interface that describes the optional parameters for the Xrm.Copilot.sendPromptToM365Copilot method.
author: devkeydet
ms.author: marcsc
ms.date: 04/23/2026
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
  - JimDaly
---

# SendPromptToM365CopilotOptions Interface (Client API reference) (preview)

[!INCLUDE [preview-note-pp](~/../shared-content/shared/preview-includes/preview-note-pp.md)]

An interface that describes the optional parameters passed to the [sendPromptToM365Copilot](sendprompttom365copilot.md) method.

## Properties

| Name| Type| Description|
|---|---|---|
| `gptId`| `string`| ID of a specific GPT to target. If omitted, the prompt is sent to the default Copilot experience.|
| `autoSubmit`| `boolean`| When `false`, the prompt text is placed in the Copilot input box but not submitted, allowing the user to review or edit it first. Defaults to `true`.|
