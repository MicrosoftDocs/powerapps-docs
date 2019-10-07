---
title: TrackContainerResize | Microsoft Docs
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
ms.assetid: c5f482c2-dde2-460b-89a7-39e0efcc5704
---

# trackContainerResize

[!INCLUDE [trackcontainerresize-description](includes/trackcontainerresize-description.md)].

If the parent context hosting the component provides a limit on the height in model-driven apps, the same is properly applied to the child component. However, in most scenarios,the parent context does not constrain the height of the component, and so it receives "-1" to indicate that it may grow further.

In canvas apps, the parent context always provides the height and width to the component by nature of the drag-and-drop editor.

## Available for 

Model-driven apps

## Syntax

`context.mode.trackContainerResize(value)`

## Parameters

| Parameter Name|Type|Required|Description|
| ------------- |----|--------|-----------|
|value|`Boolean`|Yes|`True` if controls needs to track container size, component will get allocatedWidth or allocatedHeight.|


### Related topics

[Mode](../mode.md)<br/>
[PowerApps component framework API Reference](../../reference/index.md)<br/>
[PowerApps component framework Overview](../../overview.md)
