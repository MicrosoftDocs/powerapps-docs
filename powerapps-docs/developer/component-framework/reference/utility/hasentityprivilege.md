---
title: hasEntityPrivilege (Power Apps component framework API reference) | Microsoft Docs
description: Returns if the user has privilege for specific table.
ms.author: noazarur
author: noazarur-microsoft
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
---

# hasEntityPrivilege

[!INCLUDE [hasentityprivilege-description](includes/hasentityprivilege-description.md)]

## Available for 

Model-driven apps

## Syntax

`context.utils.hasEntityPrivilege(entityTypeName, privilegeType, privilegeDepth)`

## Parameters

| Parameter Name|Type|Required|Description|
| ------------- |----|--------|-----------|
|entityTypeName|`string`|Yes|Table type name|
|privilegeType|`enum`|No|Table privilege types. It has the following elements:<br/>- `None = 0`<br/>- `Create = 1` <br/>- `Read = 2`<br/>- `Write = 3`<br/>- `Delete = 4`<br/>- `Assign =5`<br/>- `Share =6`<br/>- `Append =7`<br/>- `AppendTo =8`|
|privilegeDepth|`enum`|No|Table privilege depth. It has the following elements: <br/>- `None = -1`<br/>- `Basic = 0`<br/>- `Local = 1`<br/>- `Deep = 2`<br/>- `Global = 3`|

## Return Value

**Type**: `boolean`

### Related articles

[Utility](../utility.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
