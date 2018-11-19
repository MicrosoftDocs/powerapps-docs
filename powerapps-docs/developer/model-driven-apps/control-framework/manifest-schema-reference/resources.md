---
title: Resources Element | Microsoft Docs
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
ms.assetid: 66599c2f-6651-4b27-92da-a38897acdfb5
---

# resources element

[!INCLUDE [resources-description](includes/resources-description.md)]

## Parent Elements

|Element|Description|
|--|--|
|[control](control.md)|[!INCLUDE [control-description](includes/control-description.md)]|

## Child Elements

|Element|Description|Occurrences|
|--|--|--|
|[library](library.md)|[!INCLUDE [library-description](includes/library-description.md)]|0 or more|
|[code](code.md)|[!INCLUDE [code-description](includes/code-description.md)]|1 or more|
|[css](css.md)|[!INCLUDE [css-description](includes/css-description.md)]|0 or more|
|[img](img.md)|[!INCLUDE [img-description](includes/img-description.md)]|0 or more|
|[html](html.md)|[!INCLUDE [html-description](includes/html-description.md)]|0 or more|
|[resx](resx.md)|[!INCLUDE [resx-description](includes/resx-description.md)]|0 or more|

## Example

```xml
<resources>
			<code path="JS_HelloWorldControl.js" order="1" />
			<css path="css/JS_HelloWorldControl.css" order="1" />
		</resources>
```

### Related topics

[PowerApps Control Framework Manifest Schema Reference](index.md)<br />
[PowerApps Control Framework API Reference](../reference/index.md)<br />
[PowerApps Control Framework Overview](../powerapps-control-framework-overview.md)
