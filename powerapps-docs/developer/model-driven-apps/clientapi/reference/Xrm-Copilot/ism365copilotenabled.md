---
title: "isM365CopilotEnabled (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the isM365CopilotEnabled method.
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

# isM365CopilotEnabled (Client API reference)

[!INCLUDE[ism365copilotenabled-description](includes/ism365copilotenabled-description.md)]

## Syntax

`Xrm.Copilot.isM365CopilotEnabled().then(successCallback, errorCallback);`

## Parameters

| Parameter Name| Type| Required | Description|
| --- | --- | --- | --- |
| `successCallback` | Function | Yes | A function to call when the operation succeeds.|
| `errorCallback`   | Function | Yes | A function to call when the operation fails.|

## Return Value

Type: `Promise<boolean>`

Returns `true` if Microsoft 365 Copilot is enabled in the current environment; `false` otherwise.

## Remarks

Enablement is determined by a ranked sequence of checks: a feature control kill switch, three parallel eligibility checks (license, environment setting, and Dataverse indexing status), an optional app-level setting override, and a gradual rollout flag. The result is cached for 30 minutes, and concurrent calls are deduplicated.

All other Microsoft 365 Copilot methods check this value before executing and complete without action if it returns `false`.

## Example

```javascript
const isEnabled = await Xrm.Copilot.isM365CopilotEnabled();
if (isEnabled) {
    // Show Copilot-related controls
}
```

### Related articles

[Xrm.Copilot (Client API reference)](../xrm-copilot.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
