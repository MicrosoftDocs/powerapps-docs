---
title: "updateContext (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the updateContext method.
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

# updateContext (Client API reference)

[!INCLUDE[updatecontext-description](includes/updatecontext-description.md)]

## Syntax

`Xrm.Copilot.updateContext(context).then(successCallback, errorCallback);`

## Parameters

| Parameter Name| Type| Required | Description|
| --- | --- | --- | --- |
| `context` | [PowerAppsContent](powerappscontent.md) | Yes | An object describing the current app context to send to the Microsoft 365 Copilot side panel.|
| `successCallback` | Function | Yes | A function to call when the operation succeeds.|
| `errorCallback`   | Function | Yes | A function to call when the operation fails.|

## Return Value

Type: `Promise<void>`

## Remarks

Base context fields (`appId`, `appType`, `orgId`, `geo`, `schemaVersion`) are merged in automatically. You do not need to provide them. Does nothing if Microsoft 365 Copilot is not enabled.

## Example

```javascript
await Xrm.Copilot.updateContext({
    entity: "account",
    filterXML: "<fetch><entity name='account'><filter><condition attribute='statecode' operator='eq' value='0'/></filter></entity></fetch>"
});
```

### Related articles

[PowerAppsContent](powerappscontent.md)  
[Xrm.Copilot (Client API reference)](../xrm-copilot.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
