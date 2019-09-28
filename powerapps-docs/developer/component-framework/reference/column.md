---
title: Column | Microsoft Docs
description: 
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 04/23/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: db4be085-c31e-4045-8834-b0f45c569964
---

# Column

[!INCLUDE[cc-beta-prerelease-disclaimer](../../../includes/cc-beta-prerelease-disclaimer.md)]

[!INCLUDE [column-description](includes/column-description.md)]

## Available for 

Model-driven apps

## Properties

### alias

The alias of the column.

**Type**: `string`

### dataType

The data type of the column's values.

**Type**: `string`

### disableSorting

Prevents the UI from making the column sortable.

**Type**: `boolean`<br />

### displayName

Localized display name for the column

**Type**: `string`

### isHidden

The column visibility state.

**Type**: `boolean`<br />

### isPrimary

Is specific column the primary attribute of the view's entity.

**Type**: `boolean`<br />

### name

Name of the column, unique in the dataset.

**Type**: `string`

### order

The column order for the layout.

**Type**: `number`

### visualSizeFactor

Customized column width ratios. 

**Type**: `number`


### Related topics

[PowerApps component framework API Reference](../reference/index.md)<br/>
[PowerApps component framework Overview](../overview.md)