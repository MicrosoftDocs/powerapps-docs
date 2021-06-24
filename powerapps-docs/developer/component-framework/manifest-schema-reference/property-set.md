---
title: Property Set Element | Microsoft Docs
description: Defines an inner configuration within a dataset manifest node to allow you to explicitly configure a column of your dataset against a column of a given type from the table against which the dataset is configured.
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 10/01/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 996f10e5-8057-40ea-9680-555e4cd682ff
---

# property-set element

[!INCLUDE [property-set-description](includes/property-set-description.md)]

## Available for

Model-driven and canvas apps

## Properties

|Name |Description |Type |Required |Available for|
|----- |------ |------ |---------- |-------------|
|name | Name of the column. |string |Yes |Model-driven and canvas apps|
|display-name-key  | Used in customization screens as localized strings that describe the name of the property. |string |Yes |Model-driven and canvas apps|
|description-key |Used in customization screens as localized strings that describe the description of the property. |string |Optional |Model-driven apps|
|of-type |Defines the data type of the property |See [Remarks](#remarks) |Optional |Model-driven apps|
|required|Indicates whether the property is required or not.|boolean |Optional |Model-driven apps|
|of-type-group |Name of the type-group as defined in manifest. |string|Optional |Model-driven apps|
|usage |The usage property identifies if the property is meant to represent a table column that the component can change (bound) or read-only values (input). |bound or input |Yes |Model-driven apps|

## Parent Elements

|Element|Description|
|--|--|
|[dataset](data-set.md)|[!INCLUDE [data-set-description](includes/data-set-description.md)]|

## Child Elements

|Element|Description|Occurrences|
|--|--|--|
|[types](types.md)||0 or more|

### Remarks

The `of-type` attribute value must be one of the following:

[!INCLUDE [type-table](includes/type-table.md)]

### Related topics

[Power Apps component framework manifest schema reference](index.md)<br/>
[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]