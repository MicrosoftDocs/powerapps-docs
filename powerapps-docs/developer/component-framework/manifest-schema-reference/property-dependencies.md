---
title: property-dependencies Element | Microsoft Docs
description: Defines a group of property-dependencies.
author: anuitz
ms.author: anuitz
ms.date: 11/21/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
---

# property-dependencies element

[!INCLUDE [property-dependencies-description](includes/property-dependencies-description.md)]

## Available for

Canvas apps

## Parent Elements

|Element|Description|
|--|--|
|[control](control.md)|[!INCLUDE [control-description](includes/control-description.md)]|

## Child Elements

|Element|Description|Occurrences|Available for|
|--|--|--|-------|
|[property-dependency](property-dependency.md)|[!INCLUDE [property-dependency-description](includes/property-dependency-description.md)]|1 or more|Canvas apps |

### Example

```XML
<property-dependencies>
   <property-dependency input="Text" output="Photos" required-for="schema" />
</property-dependencies>
```

### Related articles

[Power Apps component framework manifest schema reference](index.md)<br/>
[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]