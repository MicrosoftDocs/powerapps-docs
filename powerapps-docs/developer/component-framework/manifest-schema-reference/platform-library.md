---
title: platform-library Element | Microsoft Docs
description: "Platform library resources used in the component."
author: anuitz
ms.author: anuitz
ms.date: 12/04/2024
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
 - miglisic
---

# platform-library element

[!INCLUDE [platform-library-description](includes/platform-library-description.md)]

## Available for

Model-driven and canvas apps

## Attributes

|Name|Description|Type|Required|Available for|
|--|--|--|--|-------|
|`name`|Either `React` or `Fluent`.|`string`|Yes|Model-driven and canvas apps|
|`version`|The current version of the platform library|`string`|Yes|Model-driven and canvas apps|

## Parent Elements

|Element|Description|
|--|--|
|[resources](resources.md)|[!INCLUDE [resources-description](includes/resources-description.md)]|


## Example

```xml
<resources>
   <code path="index.ts" order="1" />
   <platform-library name="React" version="16.14.0" />
   <platform-library name="Fluent" version="9.46.2" />
</resources>
```

### Related articles

[React controls & platform libraries](../react-controls-platform-libraries.md)<br />
[Power Apps component framework manifest schema reference](index.md)<br/>
[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
