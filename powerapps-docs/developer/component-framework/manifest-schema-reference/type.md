---
title: Type | Microsoft Docs
description: The type in the type-group node defines the data type in Microsoft Dataverse.
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 10/01/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: d9fb178c-6cc6-48cc-99c0-9972e37dec3e
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

### Related topics

[Power Apps component framework manifest schema reference](index.md)<br/>
[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]