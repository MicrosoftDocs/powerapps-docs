---
title: Mode (Power Apps component framework API reference) | Microsoft Docs
description: Provides access to methods to get the information about the current state of the code component.
ms.author: noazarur
author: noazarur-microsoft
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
contributors:
 - JimDaly
---

# Mode

[!INCLUDE [mode-description](includes/mode-description.md)]

## Available for 

Model-driven apps, canvas apps, & portals.

## Properties

### allocatedHeight

Height in pixels allocated to the component. 

**Type**: `number`

### allocatedWidth

Width in pixels allocated to the component.

**Type**: `number`

### isControlDisabled

Whether the component is disabled.

**Type**: `string`

### isVisible

Whether the component is visible on the page.

**Type**: `boolean`

### label

The defined component label.

**Type**: `string`

## Methods

|Method | Description | 
| ------------- |-------------|
|[setControlState](mode/setcontrolstate.md)|[!INCLUDE [setcontrolstate-description](mode/includes/setcontrolstate-description.md)]|
|[setFullScreen](mode/setfullscreen.md)|[!INCLUDE [setfullscreen-description](mode/includes/setfullscreen-description.md)]|
|[trackContainerResize](mode/trackcontainerresize.md)|[!INCLUDE [trackcontainerresize-description](mode/includes/trackcontainerresize-description.md)]|


### Related articles

[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
