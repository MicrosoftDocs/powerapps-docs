---
title: platform-action Element | Microsoft Docs
description: "Used to specify that control dependencies load on demand instead of when the control is loaded."
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

# platform-action element

[!INCLUDE [platform-action-description](includes/platform-action-description.md)]

## Available for

Model-driven apps

## Parameters

|Name|Description|Type|Required|Available for|
|--|--|--|--|--------|
|`action-type`| Set to `afterPageLoad` | string | No | Model-driven apps|

## Parent Elements

|Element|Description|
|--|--|
|[control](control.md)|[!INCLUDE [control-description](includes/control-description.md)]|

### Example

```XML
<platform-action action-type="afterPageLoad" />
```

### Related articles

[Dependent Libraries (preview)](../dependent-libraries.md)   
[Power Apps component framework manifest schema reference](index.md)   
[Power Apps component framework API reference](../reference/index.md)   
[Power Apps component framework overview](../overview.md)

[!INCLUDE [footer-banner](../../../includes/footer-banner.md)]
