---
title: Column in Microsoft Dataverse (Power Apps component framework API reference) | Microsoft Docs
description: Learn how to use different methods and properties available for column in Power Apps component framework.
ms.author: noazarur
author: noazarur-microsoft
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
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

Only available for canvas apps.

**Type**: [AttributeMetadata](attributemetadata.md)

### cellType

Cell type. Only available for canvas apps.

**Type**: `string`

### dataType

The data type of the column's values.

**Type**: `string`

### disableSorting

Prevents the UI from making the column sortable. Only available for canvas apps.

**Type**: `boolean`<br />

### displayName

Localized display name for the column.

**Type**: `string`

### isHidden

The column visibility state. Only available for canvas apps.

**Type**: `boolean`<br />

### isPrimary

Is specific column the primary column of the view's table. Only available for model-driven apps.

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

### Related articles

[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
