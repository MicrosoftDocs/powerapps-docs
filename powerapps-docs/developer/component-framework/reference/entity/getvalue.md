---
title: getValue | Microsoft Docs
description: Returns the value of the specified column name.
ms.author: noazarur
author: noazarur-microsoft
manager: lwelicki
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
---

# getValue

[!INCLUDE [cc_applies_to_update_9_0_0](../../../../includes/cc_applies_to_update_9_0_0.md)]
[!INCLUDE [getvalue-description](includes/getvalue-description.md)]

## Syntax

`getValue(columnName)`

## Parameters

| Parameter Name|Type|Required|Description|
| ------------- |----|--------|-----------|
|`columnName`|`String`|Yes|Logical name of the table column.|

## Return Value

Type: `string | Date | number | boolean |` [Entityreference](../entityreference.md)[]

### Related topics

### Related topics

[Entity](../entity.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]