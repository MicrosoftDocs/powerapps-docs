---
title: hasEntityPrivilege | Microsoft Docs
description: 
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 04/23/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
ms.assetid: f22723f0-c606-465c-abba-0a8c46a10e32
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
|entityTypeName|`string`|yes|Entity type name|
|privilegeType|`enum`|no|Entity privilege types. It has the following attributes:<br/>- `None =1`<br/>- `Create =1` <br/>- `Read =2`<br/>- `Write =3`<br/>- `Delete =4`<br/>- `Assign =5`<br/>- `Share =6`<br/>- `Append =7`<br/>- `AppendTo =8`|
|privilegeDepth|`enum`|no|Entity privilege depth. It has the following attribute: <br/>- `None =-1`<br/>- `Basic =0`<br/>- `Local =1`<br/>- `Deep =2`<br/>- `Global =3`|

## Return Value

**Type**: `boolean`

### Related topics

[Utility](../utility.md)<br/>
[PowerApps component framework API Reference](../../reference/index.md)<br/>
[PowerApps component framework Overview](../../overview.md)