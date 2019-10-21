---
title: Resources Element | Microsoft Docs
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
ms.assetid: 66599c2f-6651-4b27-92da-a38897acdfb5
---

# resources element

[!INCLUDE [resources-description](includes/resources-description.md)]

## Available for

Model-driven apps and canvas apps (experimental preview)

## Parent Elements

|Element|Description|
|--|--|
|[control](control.md)|[!INCLUDE [control-description](includes/control-description.md)]|

## Child Elements

|Element|Description|Occurrences|
|--|--|--|
|[code](code.md)|[!INCLUDE [code-description](includes/code-description.md)]|1|
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

[PowerApps component framework manifest schema reference](index.md)<br/>
[PowerApps component framework API reference](../reference/index.md)<br/>
[PowerApps component framework overview](../overview.md)