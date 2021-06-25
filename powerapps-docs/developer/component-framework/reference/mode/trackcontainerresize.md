---
title: TrackContainerResize | Microsoft Docs
description: Determines the container sizing if the component needs to react.
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 06/23/2021
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

When you call the `trackContainerResize(true)` method, the `context.mode.allocatedWidth` and `context.mode.allocatedHeight` will be provided inside the `updateView` method of the code component. The values of these properties are different depending on where the code component is hosted. A value of `-1` indicates that the code component can set CSS Style rules to fill the available space as required. 

The following table shows the values of `allocatedWidth` and `allocatedHeight` in the different combinations of host and code component lifecycle methods.

| Host                            | Lifecycle Method | `allocatedWidth`                                             | `allocatedHeight`                                            |
| ------------------------------- | ---------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Model-driven and canvas apps | `init`           | -1                                                           | -1                                                           |
| Model-driven apps               | `updateView`     | **-1** if `trackContainerResize(false)` or <br />**width in pixels** if `trackContainerResize(true)`<br />The width will change as the browser window is resized and the form adjusts to the space available. | -1                                                           |
| Canvas apps                     | `updateView`     | Set by the app maker.<br />Can change dynamically if the width is set to a Power FX formula. | Set by the app maker.<br/> Can change dynamically if the width is set to a Power FX formula. |

> [!NOTE] 
> In the test harness (started using `npm start`), the `allocatedHeight` and `allocatedWidth` will be returned as strings rather than numbers. When no value is provided, they will return an empty string rather than -1 or undefined. Additionally, once the width or height is set, you cannot undo the changes without refreshing the browser, instead a blank value will be interpreted as a size of 1.

In general, model-driven apps do not constrain the height and width of a component, so tracking the container size is not necessary. Instead, the code components can grow to use either 100% of the space for grid components, or to a specific height required by the contents when rendering a `field` component. In canvas apps, however, the parent context always provides the height and width to the component by nature of the drag-and-drop editor.

The following table shows the strategies that you can use to control the height and width of your controls HTML contents:

| Host              | Code Component Type                    | CSS Height Size Strategy                                     | CSS Width Size Strategy  |
| ----------------- | -------------------------------------- | ------------------------------------------------------------ | ------------------------ |
| Model-driven apps | `dataset`                              | `height: "100%"`                                             | `width: "100%"`          |
| Model-driven apps | `field`                                | Grow up to a maximum height<br />(The hosting form will also grow to accommodate). | `width: "100%"`          |
| Model-driven apps | `field` (full screen mode)             | `height: "100%"`                                             | `width: "100%"`          |
| Canvas apps       | `dataset` & `field`                    | `height: allocatedWidth`                                     | `width: allocatedHeight` |
| Canvas apps       | `dataset` & `field` (full screen mode) | `height: "100%"`                                             | `width: "100%"`          |

If the  of `allocatedWidth` and `allocatedHeight` change after the first `updateView` is called, then a subsequent `updateView` is called with "layout" added to the `context.updatedProperties`. More information: [UpdatedProperties](..\updatedproperties.md).

## Available for 

Model-driven and canvas apps

## Syntax

`context.mode.trackContainerResize(value)`

## Parameters

| Parameter Name|Type|Required|Description|
| ------------- |----|--------|-----------|
|value|`Boolean`|Yes|`True` if controls need to track container size, component will get allocatedWidth or allocatedHeight.|


### Related articles

[Mode](../mode.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]