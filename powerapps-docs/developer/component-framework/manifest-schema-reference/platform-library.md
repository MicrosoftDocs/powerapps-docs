---
title: platform-library Element | Microsoft Docs
description: "Platform library resources used in the component."
ms.author: hemantg
author: HemantGaur
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
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
   <platform-library name="React" version="16.8.6" />
   <platform-library name="Fluent" version="8.29.0" />
</resources>
```

### Related topics

[React controls & platform libraries (Preview) ](../react-controls-platform-libraries.md)<br />
[Power Apps component framework manifest schema reference](index.md)<br/>
[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
