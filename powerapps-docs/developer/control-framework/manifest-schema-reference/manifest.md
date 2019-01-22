---
title: Manifest Element | Microsoft Docs
description: 
keywords:
ms.author: nabuthuk
manager: jdaly
ms.date: 06/4/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: a48831c6-133a-4747-99fa-7cc1df4558d0
---

# Manifest element

[!INCLUDE [manifest-description](includes/manifest-description.md)]

## Child Elements

|Element|Description|Occurrences|
|--|--|--|
|[control](control.md)|[!INCLUDE [control-description](includes/control-description.md)]|1 or more|

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
[PowerApps Control Framework Overview](../powerapps-control-framework-overview.md)
