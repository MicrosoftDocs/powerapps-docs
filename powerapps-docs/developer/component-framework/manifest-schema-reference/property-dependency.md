---
title: property-dependency Element | Microsoft Docs
description: A property dependency in the property-dependencies node. Defines dependency between two properties.
ms.author: noazarur
author: noazarur-microsoft
ms.date: 11/07/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
---

# property-dependency element

[!INCLUDE [property-dependency-description](includes/property-dependency-description.md)]

## Available for

Canvas apps

## Parameters

|Name|Description|Type|Required|Available for|
|--|--|--|--|-----|
|`input`||string|yes|Canvas apps|
|`output`||string|yes|Canvas apps|
|`required-for`||string|yes|Canvas apps|

## Parent Elements

|Element|Description|
|--|--|
|[property-dependencies element](property-dependencies.md)|[!INCLUDE [property-dependencies-description](includes/property-dependencies-description.md)]|

### Example

```XML
<property-dependencies>
   <property-dependency input="Text" output="Photos" required-for="schema" />
</property-dependencies>
```

### Related topics

[Power Apps component framework manifest schema reference](index.md)<br/>
[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]