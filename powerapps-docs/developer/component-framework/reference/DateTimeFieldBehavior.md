---
title: DateTimeFieldBehavior (Power Apps component framework API reference)| Microsoft Docs
description: The behavior of the datetime object to be formatted.
ms.author: noazarur
author: noazarur-microsoft
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
---

# DateTimeFieldBehavior

[!INCLUDE [DateTimeFieldBehavior-description](includes/datetimefieldbehavior-description.md)]

## Available for

Model-driven apps

## Values

| Value | Description                                                             |
| ----- | ----------------------------------------------------------------------- |
| `0`   | Unknown: DateTime behavior..                                             |
| `1`   | UserLocal: Respect user local time. Dates stored as UTC.                 |
| `2`   | DateOnly: Dates with time stored as midnight without conversion to UTC. |
| `3`   | TimeZoneIndependent: Dates and time stored without conversion to UTC.    |

### Related articles

[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
