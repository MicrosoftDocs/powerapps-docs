---
title: Events (Power Apps component framework API reference) | Microsoft Docs
description: Provides methods to calling maker-defined PFX events that are configured in Power Apps Studio.
ms.author: olidum
author: OliverDumrique
ms.date: 11/20/2023
ms.reviewer: olidum
ms.topic: reference
ms.subservice: pcf
contributors:
 - OliverDumrique
---

# Events

[!INCLUDE [events-description](includes/events-description.md)]

## Available for

Canvas apps only

## Syntax

`context.events`

## Methods

[event](../manifest-schema-reference/event.md) nodes in the manifest file are built as callable methods in the `context.events` object.

## Example

```JSX
return (
  <Button
    onClick={() => {
      context.events.OnCustomEvent();
    }}
  />
);
```

### Related articles
[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
