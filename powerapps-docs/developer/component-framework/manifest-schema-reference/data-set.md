---
title: DataSet Element | Microsoft Docs
description: The data-set node in the component manifest represents a specific, configurable representation of a set of table records.
keywords:
ms.subservice: pcf
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 10/01/2019
ms.service: "powerapps"
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

You can define multiple datasets in the manifest. The first dataset in the manifest is as the primary dataset. When configuring the multi dataset component, the primary dataset property always has name `Items`. All non-primary dataset properties will have a `_Items` suffix after the dataset name. 

Certain features in the authoring panel will only apply to the primary dataset properties, such as data source selector, field selector, and view selector. To configure a non-primary dataset property, the maker needs to first import the data source to the app, then set the property value to that secondary data source. Property-set should be used for accessing columns in a non-primary dataset property. 

## Parameters

|Name|Description|Type|Required|Available for|
|--|--|--|--|-------|
|`description-key`|Defines the description of the property.|`string`|Optional|Model-driven and canvas apps|
|`display-name-key`|Defines the name of the property.|`string`|Yes|Model-driven and canvas apps|
|`name`|Name of the grid|`string`|Yes|Model-driven and canvas apps|
|`cds-data-set-options`|Displays the Commandbar, ViewSelector, QuickFind if set to true |`string`|Yes|Model-driven apps|

## Parent Elements

|Element|Description|
|--|--|
|[control](control.md)|[!INCLUDE [control-description](includes/control-description.md)]|


## Example

```xml
 <data-set name="dataSetGrid" display-name-key="DataSetGridProperty" cds-data-set-options="displayCommandBar:true;displayViewSelector:true;displayQuickFind:true">
 </data-set>
```

### Related topics

[Power Apps component framework manifest schema reference](index.md)<br/>
[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]