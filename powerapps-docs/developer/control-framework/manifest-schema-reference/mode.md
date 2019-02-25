---
title: Mode | Microsoft Docs
description: 
keywords:
ms.author: nabuthuk
manager: kvivek
ms.date: 03/01/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
---

# Manifest element

[!INCLUDE [mode-description](includes/mode-description.md)]

## Child Elements

|Element|Description|Occurrences|
|--|--|--|
|[read](read.md)|[!INCLUDE [read-description](includes/read-description.md)]|1 or more|
|[edit](edit.md)|[!INCLUDE [edit-description](includes/edit-description.md)]|0 or more|
|[container](container.md)|[!INCLUDE [property-description](includes/property-description.md)]|0 or more|
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

[Control](control.md)<br />
[PowerApps Control Framework Manifest Schema Reference](index.md)<br />
[PowerApps Control Framework API Reference](../reference/index.md)<br />
[PowerApps Control Framework Overview](../overview.md)