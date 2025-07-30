---
title: data-set Element | Microsoft Docs
description: The data-set node in the component manifest represents a specific, configurable representation of a set of table records.
author: anuitz
ms.author: anuitz
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
---

# data-set element

[!INCLUDE [data-set-description](includes/data-set-description.md)]

You can define multiple datasets in the manifest. The first dataset in the manifest is as the primary dataset. When you configure a multi dataset component, the primary dataset property always has name `Items`. All nonprimary dataset properties will have a `_Items` suffix after the dataset name.

Certain features in the authoring panel only apply to the primary dataset properties, such as data source selector, field selector, and view selector. To configure a nonprimary dataset property, the maker needs to first import the data source to the app, then set the property value to that secondary data source. Property-set should be used for accessing columns in a nonprimary dataset property. 

## Parameters

|Name|Description|Type|Required|Available for|
|--|--|--|--|-------|
|`description-key`|Defines the description of the property.|`string`|Optional|Model-driven and canvas apps|
|`display-name-key`|Defines the name of the property.|`string`|Yes|Model-driven and canvas apps|
|`name`|Name of the grid|`string`|Yes|Model-driven and canvas apps|
|`cds-data-set-options`|Displays the `Commandbar`, `ViewSelector`, `QuickFind` if set to true |`string`|Yes|Model-driven apps|

## Parent Elements

|Element|Description|
|--|--|
|[control](control.md)|[!INCLUDE [control-description](includes/control-description.md)]|


## Example

```xml
<data-set name="dataSetGrid"
   display-name-key="DataSetGridProperty"
   cds-data-set-options="displayCommandBar:true;displayViewSelector:true;displayQuickFind:true">
</data-set>
```

### Related articles

[Power Apps component framework manifest schema reference](index.md)   
[Power Apps component framework API reference](../reference/index.md)   
[Power Apps component framework overview](../overview.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
