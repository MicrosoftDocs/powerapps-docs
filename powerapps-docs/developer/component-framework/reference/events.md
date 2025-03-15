---
title: Events (Power Apps component framework API reference) | Microsoft Docs
description: Provides methods to call events defined in a PCF. For canvas apps, these events will be configured by the maker as Power Fx. For model-driven apps, events are described using JavaScript.
author: OliverDumrique
ms.author: olidum
ms.reviewer: jdaly
ms.date: 11/20/2023
ms.topic: reference
ms.subservice: pcf
---

# Events

[!INCLUDE [events-description](includes/events-description.md)]

## Available for

Canvas apps and model-driven apps

## Syntax

`context.events`

## Methods

[event](../manifest-schema-reference/event.md) nodes in the manifest file are built as callable methods in the `context.events` object.

[Define Events](../events.md)

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
