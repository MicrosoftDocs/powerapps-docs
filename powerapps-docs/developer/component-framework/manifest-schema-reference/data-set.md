---
title: DataSet Element | Microsoft Docs
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
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
ms.assetid: 9ffe8930-b290-4252-98d4-a1195b00205f
---

# data-set element

[!INCLUDE [data-set-description](includes/data-set-description.md)]

## Attributes

|Name|Description|Type|Required|Available for|
|--|--|--|--|-------|
|`description-key`|Defines the description of the property.|`string`|Optional|Model-driven apps and canvas apps (public preview)|
|`display-name-key`|Defines the name of the property.|`string`|Yes|Model-driven apps and canvas apps (public preview)|
|`name`|Name of the grid|`string`|Yes|Model-driven apps and canvas apps (public preview)|
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