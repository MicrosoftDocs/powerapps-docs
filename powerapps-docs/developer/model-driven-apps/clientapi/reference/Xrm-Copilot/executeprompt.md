---
title: "executePrompt (Client API reference) in model-driven apps (preview)"
description: Includes description and supported parameters for the executePrompt method.
author: adrianorth
ms.author: aorth
ms.date: 06/16/2025
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType:
  - developer
contributors:
  - JimDaly
---

# executePrompt (Client API reference) (preview)

[!INCLUDE [preview-note-pp](~/../shared-content/shared/preview-includes/preview-note-pp.md)]

[!INCLUDE[./includes/executeprompt-description.md](./includes/executeprompt-description.md)]

## Syntax

`Xrm.Copilot.executePrompt(promptText).then(successCallback, errorCallback);`

## Parameters

| Parameter Name| Type| Required | Description|
| --- | --- | --- | --- |
| `promptText` | string | Yes | The text that is registered as a trigger query in the MCS topic.  |
| `successCallback` | Function | Yes | A function to call when the operation succeeds.|
| `errorCallback`   | Function | Yes | A function to call when the operation fails.|

## Return Value

An array of [MCSResponse](mcsresponse.md)

## Example

In Microsoft Copilot Studio, a topic is triggered by queries like "hello" or "hi." When `executePrompt` runs with matching promptText, it activates the topic and returns a Message activity with the response text.

```javascript
const response = await Xrm.Copilot.executePrompt("hello"); 
```

### Response

This is an example of the response that may be returned.

```json
[
    {
        "type": "message",
        "timestamp": "2025-02-05T16:46:07.7799759+00:00",
        "replyToId": "aaaaaaaa-0000-1111-2222-bbbbbbbbbbbb",
        "attachments": [],
        "textFormat": "markdown",
        "text": "Hello, how can I help you today?",
        "speak": "Hello, <break strength=\"medium\" /> how can I help?"
    }
]
```

### Related articles

[Xrm.Copilot (Client API reference)](../xrm-copilot.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
