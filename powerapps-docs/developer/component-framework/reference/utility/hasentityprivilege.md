---
title: hasEntityPrivilege | Microsoft Docs
description: Returns if the user has privilege for specific table.
keywords:
ms.author: jdaly
author: noazarur-microsoft
manager: kvivek
ms.date: 03/12/2022
ms.reviewer: jdaly

ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
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

### Related topics

[Utility](../utility.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]