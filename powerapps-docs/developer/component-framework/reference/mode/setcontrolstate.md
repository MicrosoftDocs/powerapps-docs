---
title: setControlState | Microsoft Docs
description: 
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 10/01/2019
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
ms.assetid: 1052db82-7002-44ca-ad1f-9d3d4c311817
---

# setControlState

[!INCLUDE [setcontrolstate-description](includes/setcontrolstate-description.md)]

## Syntax

`context.mode.setControlState(state);`

## Available for 

Model-driven apps and canvas apps (public preview) 

## Parameters

| Parameter Name|Type|Required|Description|
| ------------- |----|--------|-----------|
|state|`Dictionary`|Yes|Data that persists in one session for a single user.|

## Return Value

Type: `boolean`


### Related topics

[Mode](../mode.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]