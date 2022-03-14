---
title: MoneyPrecisionSource in Microsoft Dataverse| Microsoft Docs
description: Enumeration for money precision source.
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

# MoneyPrecisionSource

[!INCLUDE [MoneyPrecisionSource-description](includes/moneyprecisionsource-description.md)]

## Available for

Model-driven and canvas apps

## Values

| Value | Description  |
| ----- | ------------ |
| `0`   | None: Precision comes from "accuracy" attribute of properties XML. |
| `1`   | Organization: Precision comes from the PricingDecimalPrecision column in the organization table. |
| `2`   | Currency: Precision comes from the currency. |

### Related topics

[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
