---
title: dependency Element | Microsoft Docs
description: Refers to a library in another component that this component depends on.
author: anuitz
ms.author: anuitz
ms.date: 02/20/2025
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
|`type`|TODO: What are valid values here?|`String`|Yes|Model-driven apps |
|`name`|The schemaName name of the library component|`String`|Yes|Model-driven  apps |
|`order`|The order in which the dependent library should load|`Positive integer`|Yes|Model-driven  apps |
|`load-type`|TODO: What are valid values here? Is `onDemand` the only valid value?|`String`|Yes|Model-driven  apps |

## Parent Elements

|Element|Description|
|--|--|
|[resources](resources.md)|[!INCLUDE [resources-description](includes/resources-description.md)]|

### Example

```XML
<dependency 
   type="control" 
   name="samples_SampleNS.SampleStubLibraryPCF" 
   order="1"/>
```

### Related topics

[Dependent Libraries](../dependent-libraries.md)   
[Power Apps component framework manifest schema reference](index.md)   
[Power Apps component framework API reference](../reference/index.md)   
[Power Apps component framework overview](../overview.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]