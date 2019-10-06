---
title: SortStatus | Microsoft Docs
description: 
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 10/01/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 09f6d0a7-a95a-421e-a413-281d1d0d0e19
---

# SortStatus


[!INCLUDE [sort-description](includes/sortstatus-description.md)]

## Available for 

Model-driven apps

## Properties

### name

The name of the column

**Type**: `string`

### sortDirection

<!-- ColumnSortDirection  -->
The current sort direction for the column.

**Type**: `enum`

The `sortDirection` value is an enum with the following possible values

|Value|Member|
|--|--|
|-1|None|
|0|Ascending|
|1|Descending|


### Related topics

[PowerApps component framework API Reference](../reference/index.md)<br/>
[PowerApps component framework Overview](../overview.md)