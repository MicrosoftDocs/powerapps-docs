---
title: MoneyPrecisionSource in Microsoft Dataverse| Microsoft Docs
description: Enumeration for money precision source.
keywords:
ms.author: nabuthuk
manager: kvivek
author: nkrb
ms.date: 11/04/2021
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: ad8659f7-f566-43db-bed1-c8484c114a59
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
