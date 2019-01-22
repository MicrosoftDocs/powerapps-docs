---
title: Control Element | Microsoft Docs
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
ms.assetid: 4dacd337-c9df-458e-86f3-bfb3ab543ea7
---

# control element

[!INCLUDE [control-description](includes/control-description.md)]

## Attributes

|Name|Description|Type|Required|
|--|--|--|--|
|`namespace`|Defines the object prototype of the control|[!INCLUDE [alphanumerictype-description](includes/alphanumerictype-description.md)]|yes|
|`constructor`|A method for initializing the object|[!INCLUDE [alphanumerictype-description](includes/alphanumerictype-description.md)]|yes|
|`control-type`|Standard|[!INCLUDE [controltype-description](includes/controltype-description.md)]|no|
|`description-key`|Used in the customization screens as localized strings that describes the description of the property.|`string`|no|
|`display-name-key`|Used in the customization screens as localized strings that describes the name of the property.|`string`|yes|
|`preview-image`|Image that will be used on the customization screens to show a preview of the control to the customizer|`string`|no|
|`version`|Defines the version of the control|`string`|yes|
|`hidden`|Defines whether the control should be hidden or not|[!INCLUDE [booleantype-description](includes/booleantype-description.md)]| no|

## Parent Elements

|Element|Description|
|--|--|
|[manifest](manifest.md)|[!INCLUDE [manifest-description](includes/manifest-description.md)]|

## Child Elements

|Element|Description|Occurrences|
|--|--|--|
|[data-set](data-set.md)|[!INCLUDE [data-set-description](includes/data-set-description.md)]|0 or more|
|[property](property.md)|[!INCLUDE [property-description](includes/property-description.md)]|0 or more|
|[resources](resources.md)|[!INCLUDE [resources-description](includes/resources-description.md)]|1|
|[type-group](type-group.md)|[!INCLUDE [type-group-description](includes/type-group-description.md)]|0 or more|

## Example

```xml
<control namespace="MyNameSpace" constructor="JSHelloWorldControl" version="1.0.0" display-name-key="JS_HelloWorldControl_Display_Key" description-key="JS_HelloWorldControl_Desc_Key" control-type="standard" preview-image="img/preview.png">
  ```

### Related topics

[PowerApps Control Framework Manifest Schema Reference](index.md)<br />
[PowerApps Control Framework API Reference](../reference/index.md)<br />
[PowerApps Control Framework Overview](../powerapps-control-framework-overview.md)
