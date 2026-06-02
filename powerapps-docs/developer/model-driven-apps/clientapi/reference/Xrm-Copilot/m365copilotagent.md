---
title: M365CopilotAgent Interface (Client API reference)
description: The interface that describes the response for the Xrm.Copilot.getCurrentAgent method.
author: devkeydet
ms.author: marcsc
ms.date: 04/23/2026
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
  - JimDaly
---

# M365CopilotAgent Interface (Client API reference)

[!INCLUDE [m365copilotagent-description](includes/m365copilotagent-description.md)]

## Properties

| Name| Type| Description|
|---|---|---|
| `agentId` | `string \| null` | The unique identifier of the active agent, or `null` if the user is on mainline Microsoft 365 Copilot. |
| `mode` | [M365CopilotAgentMode](m365copilotagentmode.md) `\| null` | How the agent is being referenced, or `null` when no agent is active. |

## Remarks

`agentId` and `mode` are paired:
- `agentId` = string, `mode` = `"agentPage"` or `"mentioned"`: an agent is active.
- `agentId` = `null`, `mode` = `null`: the user is explicitly on mainline Microsoft 365 Copilot.