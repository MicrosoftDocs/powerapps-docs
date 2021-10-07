---
title: Column in Microsoft Dataverse| Microsoft Docs
description: Learn how to use different methods and properties available for column in Power Apps component framework.
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 14/19/2021
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: db4be085-c31e-4045-8834-b0f45c569964
---

# Column

[!INCLUDE [column-description](includes/column-description.md)]

## Available for

Model-driven and canvas apps

## Properties

### alias

The alias of the column.

**Type**: `string`

### attributes

**Type**: `[AttributeMetadata](./attributemetadata.md)`

### dataType

The data type of the column's values.

**Type**: `string`

### disableSorting

Model-driven Only
Prevents the UI from making the column sortable.

**Type**: `boolean`<br />

### displayName

Localized display name for the column

**Type**: `string`

### isHidden

Model-driven Only
The column visibility state.

**Type**: `boolean`<br />

### isPrimary

Model-driven Only
Is specific column the primary column of the view's table.

**Type**: `boolean`<br />

### name

Name of the column, unique in the dataset.

**Type**: `string`

### order

The column order for the layout.

**Type**: `number`

### visualSizeFactor

Model-driven Only
Customized column width ratios.

**Type**: `number`

### Related topics

[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
