---
title: Type | Microsoft Docs
description: The type in the type-group node defines the data type in Microsoft Dataverse.
author: anuitz
ms.author: anuitz
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
---

# type

[!INCLUDE [type-description](includes/type-description.md)]

## Available for

Model-driven apps

## Parent Elements

|Element|Description|
|--|--|
|[type-group](type-group.md)|[!INCLUDE [type-group-description](includes/type-group-description.md)]|

## Value element

This element contains a `string` with one of the following values:

[!INCLUDE [type-table](includes/type-table.md)]

### Example for Enum type

```XML
<property name="YesNo" display-name-key="YesNo_Display_Key" description-key="YesNo_Desc_Key" of-type="Enum" usage="input" required="false">
      <value name="Yes" display-name-key="Yes">0</value>
      <value name="No" display-name-key="No">1</value>
</property>
```

### Related articles

[Power Apps component framework manifest schema reference](index.md)<br/>
[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
