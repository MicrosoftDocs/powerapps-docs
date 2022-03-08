---
title: Mode | Microsoft Docs
description: Provides access to methods to get the information about the current state of the code component.
keywords:
author: adrianorth
ms.date: 03/07/2022
ms.author: jdaly
ms.reviewer: jdaly
manager: kvivek

ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 8b51654c-ee67-40f8-ae5b-be684dad3520
---

# Mode


[!INCLUDE [mode-description](includes/mode-description.md)]

## Available for 

Model-driven and canvas apps.

## Properties

### allocatedHeight

Height in pixels allocated to the component. 

**Type**: `number`

### allocatedWidth

Width in pixels allocated to the component. This property is supported in both model-driven and canvas apps.

**Type**: `number`

### isControlDisabled

Whether the component is disabled. This property is supported in both model-driven and canvas apps.

**Type**: `string`

### isVisible

Whether the component is visible on the page. This property is supported in both model-driven and canvas apps.

**Type**: `boolean`

### label

The defined component label. This property is supported in both model-driven and canvas apps.

**Type**: `string`

## Methods

|Method | Description | 
| ------------- |-------------|
|[setControlState](mode/setcontrolstate.md)|[!INCLUDE [setcontrolstate-description](mode/includes/setcontrolstate-description.md)]|
|[setFullScreen](mode/setfullscreen.md)|[!INCLUDE [setfullscreen-description](mode/includes/setfullscreen-description.md)]|
|[trackContainerResize](mode/trackcontainerresize.md)|[!INCLUDE [trackcontainerresize-description](mode/includes/trackcontainerresize-description.md)]|


### Related topics

[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]