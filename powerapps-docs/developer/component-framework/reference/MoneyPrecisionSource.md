---
title: MoneyPrecisionSource (Power Apps component framework API reference)| Microsoft Docs
description: Enumeration for money precision source.
ms.author: noazarur
author: noazarur-microsoft
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
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

### Related articles

[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
