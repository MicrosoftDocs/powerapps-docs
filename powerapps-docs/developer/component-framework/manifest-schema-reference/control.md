---
title: Control Element | Microsoft Docs
description: Defines the component's namespace, version and display information.
ms.author: anuitz
author: anuitz
ms.date: 12/04/2023
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
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
|`control-type`|Whether the control is a standard control or a React control. The value of `virtual` indicates a React control using platform React library. Virtual controls are a feature in public preview. More information: [React controls & platform libraries](../react-controls-platform-libraries.md)|[!INCLUDE [controltype-description](includes/controltype-description.md)]|No|Model-driven and canvas apps |
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
|[external-service-usage](external-service-usage.md)|[!INCLUDE [external-service-usage-description](includes/external-service-usage-description.md)]|0 or 1|
|[property](property.md)|[!INCLUDE [property-description](includes/property-description.md)]|0 or more|
|[resources](resources.md)|[!INCLUDE [resources-description](includes/resources-description.md)]|1|
|[type-group](type-group.md)|[!INCLUDE [type-group-description](includes/type-group-description.md)]|0 or more|
|[property-dependencies](property-dependencies.md)|[!INCLUDE [property-dependencies-description](includes/property-dependencies-description.md)]|0 or more|

## Example

```xml
<control namespace="MyNameSpace"
   constructor="JSHelloWorldControl"
   version="1.0.0"
   display-name-key="JS_HelloWorldControl_Display_Key"
   description-key="JS_HelloWorldControl_Desc_Key"
   control-type="standard"
   preview-image="img/preview.png">
</control>
  ```

### Related topics

[Power Apps component framework manifest schema reference](index.md)<br/>
[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
