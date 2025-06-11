---
title: executePrompt (Power Apps component framework API reference) (preview)
description: Executes a Microsoft Copilot Studio topic based on the trigger queries registered in the topic.
author: adrianorth
ms.author: aorth
ms.date: 05/05/2025
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
---

# executePrompt (preview)

[!INCLUDE [preview-note-pp](~/../shared-content/shared/preview-includes/preview-note-pp.md)]

[!INCLUDE[./includes/executeprompt-description.md](./includes/executeprompt-description.md)]

## Available for

Model-driven apps

## Syntax

`context.copilot.executeEvent(promptText).then(successCallback, errorCallback);`

## Return Value

Type: `Promise<`[MCSResponse](mcsresponse.md)`>`

See [Promise](https://developer.mozilla.org/docs/Web/JavaScript/reference/Global_Objects/Promise) and [MCSResponse](mcsresponse.md)

## Example

In Microsoft Copilot Studio, when a topic is triggered by queries like "hello" or "hi." When `executePrompt` runs with matching `promptText`, it activates the topic and returns a Message activity with the response text.

```typescript
const response = await context.copilot.executePrompt("hello");
```

### Response

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

[Copilot](../copilot.md)  
[executeEvent](executeevent.md)  
[Power Apps component framework API reference](../../reference/index.md)  
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
