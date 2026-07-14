---
title: resources Element | Microsoft Docs
description: The resources node in the component manifest refers to the resource files that component requires to implement it's visualization.
author: anuitz
ms.author: anuitz
ms.date: 03/24/2025
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
---

# resources element

[!INCLUDE [resources-description](includes/resources-description.md)]

## Available for

Model-driven and canvas apps

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
|[resx](resx.md)|[!INCLUDE [resx-description](includes/resx-description.md)]|0 or more|
|[platform-library](platform-library.md)|[!INCLUDE [platform-library-description](includes/platform-library-description.md)]|0 or more|
|[dependency](dependency.md)|[!INCLUDE [dependency-description](includes/dependency-description.md)]|0 or more|


## Example

```xml
<resources>
  <code path="JS_HelloWorldControl.js" order="1" />
    <css path="css/JS_HelloWorldControl.css" order="1" />
</resources>
```

### Related articles

[Power Apps component framework manifest schema reference](index.md)   
[Power Apps component framework API reference](../reference/index.md)   
[Power Apps component framework overview](../overview.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
