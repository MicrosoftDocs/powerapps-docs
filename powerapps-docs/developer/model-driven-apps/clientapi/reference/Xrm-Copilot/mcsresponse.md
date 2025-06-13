---
title: MCSResponse Interface (Client API reference) (preview)
description: The interface that describes the properties of contains data returned by the Xrm.Copilot.executeEvent and Xrm.Copilot.executePrompt methods.
author: adrianorth
ms.author: aorth
ms.date: 06/16/2025
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
  - JimDaly
---

# MCSResponse Interface (Client API reference) (preview)

[!INCLUDE [preview-note-pp](~/../shared-content/shared/preview-includes/preview-note-pp.md)]

An interface that describes the data returned by the [executeEvent](executeevent.md) and [executePrompt](executeprompt.md) methods.

<!-- The information below may be identical to the MCSResponse used in Xrm Client API
Try to re-use this content with an include if possible -->

## Properties

The following table describes the `MCSResponse` properties. Only the `type` property will always be present.


| Name| Type| Description|
|---|---|---|
| `type`| `string`| **Required.** The type of the response.|
| `id`| `string`|  Unique identifier for the response.|
| `locale`| `string`|  Locale information (e.g., language or region).|
| `replyToId`| `string`|  ID of the message this is replying to.|
| `timestamp`| `string`|  Timestamp of the response.|
| `speak`| `string`|  Text to be spoken by a speech synthesizer.|
| `text`| `string`|  Text content of the response.|
| `textFormat`| `plain` \| `markdown` \| `xml`  |  Format of the text content.|
| `suggestedActions` | `{ actions: any[]; to?: string[] }`  |  Suggested actions for the user to take.|
| `value`| `unknown`|  Custom payload or data.|
| `valueType`| `string`|  Type of the value payload.|
| `name`| `string`|  Name of the response or action.|
| `attachmentLayout` | `list` \| `carousel`|  Layout style for displaying attachments.|
| `attachments`| [Attachment](#attachment-interface)[]|  Array of attachments included in the response.|

### Attachment Interface

| Name| Type| Description|
|---|---|---|
| `content`| `unknown` |  **Required.** The content of the attachment. |
| `contentType`| `string` |  Describes the type of content. |