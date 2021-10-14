---
title: Control Element | Microsoft Docs
description: Defines the component's namespace, version and display information.
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
ms.assetid: 4dacd337-c9df-458e-86f3-bfb3ab543ea7
---

# control element

[!INCLUDE [control-description](includes/control-description.md)]

## Available for

Model-driven and canvas apps

## Parameters

|Name|Description|Type|Required|Available for|
|--|--|--|--|--------|
|`namespace`|Defines the object prototype of the component|[!INCLUDE [alphanumerictype-description](includes/alphanumerictype-description.md)]|Yes|Model-driven and canvas apps |
|`constructor`|A method for initializing the object|[!INCLUDE [alphanumerictype-description](includes/alphanumerictype-description.md)]|Yes|Model-driven and canvas apps |
|`control-type`|Standard|[!INCLUDE [controltype-description](includes/controltype-description.md)]|No|Model-driven and canvas apps |
|`description-key`|Defines the description of the component that will be seen on the UI.|`string`|No|Model-driven and canvas apps |
|`display-name-key`|Defines the name of the control that is displayed on the UI.|`string`|Yes|Model-driven and canvas apps  |  
|`preview-image`|Image that will be used on the customization screens to show a preview of the component.|`string`|No|Model-driven apps|
|`version`|Defines the version of the component defined in [Semantic Versioning](https://semver.org)|`string`|Yes|Model-driven and canvas apps |
<!--|`hidden`|Defines whether the component should be hidden or not|[!INCLUDE [booleantype-description](includes/booleantype-description.md)]| No|Model-driven apps|-->

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
<control namespace="MyNameSpace" constructor="JSHelloWorldControl" version="1.0.0"
 display-name-key="JS_HelloWorldControl_Display_Key" description-key="JS_HelloWorldControl_Desc_Key"
 control-type="standard" preview-image="img/preview.png">
</control>
  ```

### Related topics

[Power Apps component framework manifest schema reference](index.md)<br/>
[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]