---
title: DateTimeFieldBehavior in Microsoft Dataverse| Microsoft Docs
description: The behavior of the datetime object to be formatted.
keywords:
ms.author: jdaly
author: noazarur-microsoft
manager: kvivek
ms.date: 03/12/2022
ms.reviewer: jdaly

ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
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

### Related topics

[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
