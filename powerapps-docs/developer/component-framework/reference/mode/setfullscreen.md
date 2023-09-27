---
title: setFullScreen (Power Apps component framework API reference) | Microsoft Docs
description: Make the component full screen.
ms.author: noazarur
author: noazarur-microsoft
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
---

# setFullScreen

[!INCLUDE [setfullscreen-description](includes/setfullscreen-description.md)]

## Syntax

`context.mode.setFullScreen(value);`

## Available for 

Model-driven apps, canvas apps, & portals.

## Parameters

| Parameter Name|Type|Required|Description|
| ------------- |----|--------|-----------|
|value|`Boolean`|Yes|`True` if component needs to auto size to full screen. `False` if component needs to auto size to allocated width.|


### Related articles

[Mode](../mode.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
