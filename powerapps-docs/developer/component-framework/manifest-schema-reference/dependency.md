---
title: dependency Element | Microsoft Docs
description: Refers to a library in another component that this component depends on.
author: anuitz
ms.author: anuitz
ms.date: 03/24/2025
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
 - kierantpetrie
---

# dependency element

[!INCLUDE [dependency-description](includes/dependency-description.md)]

## Available for

Model-driven apps

## Parameters

|Name|Description|Type|Required|Available for|
|--|--|--|--|-----|
|`type`|Set to `control`|`String`|Yes|Model-driven apps |
|`name`|The schema name name of the library component|`String`|Yes|Model-driven  apps |
|`order`|The order in which the dependent library should load|`Positive integer`|No|Model-driven  apps |
|`load-type`|Set to `onDemand`|`String`|No|Model-driven  apps |

## Parent Elements

|Element|Description|
|--|--|
|[resources](resources.md)|[!INCLUDE [resources-description](includes/resources-description.md)]|

### Example

```XML
<dependency 
   type="control" 
   name="samples_SampleNS.SampleStubLibraryPCF" 
   load-type="onDemand"/>
```

### Related articles

[Dependent Libraries (preview)](../dependent-libraries.md)   
[Power Apps component framework manifest schema reference](index.md)   
[Power Apps component framework API reference](../reference/index.md)   
[Power Apps component framework overview](../overview.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
