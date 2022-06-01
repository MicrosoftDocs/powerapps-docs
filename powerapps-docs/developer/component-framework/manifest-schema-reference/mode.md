---
title: Mode element| Microsoft Docs
description: Provides information on methods available for mode element.
ms.author: noazarur
author: noazarur-microsoft
manager: lwelicki
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly"
---

# Mode element

[!INCLUDE [mode-description](includes/mode-description.md)]

## Child Elements

|Element|Description|Occurrences|
|--|--|--|
|[data-set](data-set.md)|[!INCLUDE [data-set-description](includes/data-set-description.md)]|0 or more|
|[resource](resources.md)|[!INCLUDE [resource-description](includes/resources-description.md)]|1 or more|

## Example

```xml
<?xml version="1.0" encoding="utf-8" ?>
<manifest>
   <control namespace="MyNameSpace" constructor="JSHelloWorldControl" version="1.0.0" display-name-key="JS_HelloWorldControl_Display_Key" description-key="JS_HelloWorldControl_Desc_Key" control-type="standard">
      <property name="myFirstProperty" display-name-key="myFirstProperty_Display_Key" description-key="myFirstProperty_Desc_Key" of-type="SingleLine.Text" usage="bound" required="true" />
      <resources>
         <code path="JS_HelloWorldControl.js" order="1" />
         <css path="css/JS_HelloWorldControl.css" order="1" />
      </resources>
   </control>
</manifest>
```

### Related topics

[Power Apps component framework manifest schema reference](index.md)<br/>
[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]