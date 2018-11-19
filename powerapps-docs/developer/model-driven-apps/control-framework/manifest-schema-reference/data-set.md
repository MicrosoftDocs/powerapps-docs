---
title: DataSet Element | Microsoft Docs
description: 
keywords:
ms.author: nabuthuk
manager: jdaly
ms.date: 06/4/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
ms.assetid: 9ffe8930-b290-4252-98d4-a1195b00205f
---

# data-set element

[!INCLUDE [data-set-description](includes/data-set-description.md)]

## Attributes

|Name|Description|Type|Required|
|--|--|--|--|
|`description-key`|Used in the customization screen as localized strings that describes the description of the property.|`string`|no|
|`display-name-key`|Used in the customization screens as localized strings that describes the name of the property.|`string`|yes|
|`name`|Name of the grid|`string`|yes|

## Parent Elements

|Element|Description|
|--|--|
|[control](control.md)|[!INCLUDE [control-description](includes/control-description.md)]|

## Example

```xml
 <data-set name="dataSetGrid" display-name-key="DataSetGridProperty">
 </data-set>
```

### Related topics

[PowerApps Control Framework Manifest Schema Reference](index.md)<br />
[PowerApps Control Framework API Reference](../reference/index.md)<br />
[PowerApps Control Framework Overview](../powerapps-control-framework-overview.md)
