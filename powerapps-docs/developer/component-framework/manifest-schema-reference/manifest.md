---
title: Manifest Element | Microsoft Docs
description: Manifest is the metadata file that defines a component.
author: anuitz
ms.author: anuitz
ms.date: 02/06/2023
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
---

# Manifest element

[!INCLUDE [manifest-description](includes/manifest-description.md)]

## Available for

Model-driven and canvas apps

## Child Elements

|Element|Description|Occurrences|Available for|
|--|--|--|-------|
|[control](control.md)|[!INCLUDE [control-description](includes/control-description.md)]|1|Model-driven and canvas apps |

<!-- IDK why these were listed as child elements. -->
<!-- |[type-group](type-group.md)|[!INCLUDE [type-group-description](includes/type-group-description.md)]|0 or more|Model-driven and canvas apps |
|[property](property.md)|[!INCLUDE [property-description](includes/property-description.md)]|0 or more|Model-driven and canvas apps |
|[data-set](data-set.md)|[!INCLUDE [data-set-description](includes/data-set-description.md)]|0 or more|Model-driven apps|
|[resources](resources.md)|[!INCLUDE [resource-description](includes/resources-description.md)]|1 or more|Model-driven and canvas apps |
|[feature-usage](feature-usage.md)|[!INCLUDE [feature-usage-description](includes/feature-usage-description.md)]|0 or more|Model-driven and canvas apps | -->

## Example

```xml
<?xml version="1.0" encoding="utf-8" ?>
<manifest>
   <control namespace="MyNameSpace"
      constructor="JSHelloWorldControl"
      version="1.0.0"
      display-name-key="JS_HelloWorldControl_Display_Key"
      description-key="JS_HelloWorldControl_Desc_Key"
      control-type="standard">
      <property name="myFirstProperty"
         display-name-key="myFirstProperty_Display_Key"
         description-key="myFirstProperty_Desc_Key"
         of-type="SingleLine.Text"
         usage="bound"
         required="true" />
      <resources>
         <code path="JS_HelloWorldControl.js"
            order="1" />
         <css path="css/JS_HelloWorldControl.css"
            order="1" />
      </resources>
   </control>
</manifest>
```

### Related articles

[Power Apps component framework manifest schema reference](index.md)<br/>
[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]