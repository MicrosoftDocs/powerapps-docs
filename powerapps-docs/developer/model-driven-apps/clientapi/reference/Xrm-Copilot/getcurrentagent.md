---
title: "getCurrentAgent (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the getCurrentAgent method.
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

# getCurrentAgent (Client API reference)

[!INCLUDE[./includes/getcurrentagent-description.md](./includes/getcurrentagent-description.md)]

## Syntax

`Xrm.Copilot.getCurrentAgent().then(successCallback, errorCallback);`

## Parameters

| Parameter Name| Type| Required | Description|
| --- | --- | --- | --- |
| `successCallback` | Function | Yes | A function to call when the operation succeeds.|
| `errorCallback`   | Function | Yes | A function to call when the operation fails.|

## Return Value

Type: `Promise<M365CopilotAgent | undefined>` — Resolves to an [M365CopilotAgent](m365copilotagent.md) object describing the active agent, or `undefined` if the agent state has not been determined yet.

## Remarks

Does nothing if Microsoft 365 Copilot is not enabled.

The returned object's `agentId` and `mode` properties are paired:
- `agentId` is a non-null string and `mode` is `"agentPage"` or `"mentioned"`: an agent is active.
- `agentId` is `null` and `mode` is `null`: the user is on mainline Microsoft 365 Copilot (no agent active).

## Example

```javascript
const agent = await Xrm.Copilot.getCurrentAgent();
if (agent && agent.agentId) {
    console.log(`Active agent: ${agent.agentId}, mode: ${agent.mode}`);
} else if (agent) {
    console.log("User is on mainline M365 Copilot (no agent).");
} else {
    console.log("Agent state not yet determined.");
}
```

### Related articles

[Xrm.Copilot (Client API reference)](../xrm-copilot.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
