---
title: setFilter (Power Apps component framework API reference) | Microsoft Docs
description: Sets the top-most filter associated with the dataset.
ms.author: noazarur
author: noazarur-microsoft
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
---

# setFilter

[!INCLUDE [setfilter-description](includes/setfilter-description.md)]

## Syntax

`context.filtering.setFilter()`

## Available for 

Model-driven and canvas apps

## Parameters

| Parameter Name|Type|Required|Description|
| ------------- |----|--------|-----------|
|expression|[FilterExpression](../filterexpression.md)|Yes|The `FilterExpression` to set.|


### Related articles

[Filtering](../filtering.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
