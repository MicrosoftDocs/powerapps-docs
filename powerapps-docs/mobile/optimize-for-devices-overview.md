---
title: Optimize for devices overview (preview)
description: Learn how to make your canvas app screens optimized for devices. 
author: anuitz
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: sericks
ms.date: 11/14/2023
ms.subservice: canvas-maker
ms.author: anuitz
search.audienceType: 
  - maker
contributors:
  - sericks
  - anuitz
---

# Optimize for devices overview (preview)

[This article is prerelease documentation and is subject to change.]

_Optimize for devices_ is a feature that changes the way canvas app screens are loaded and displayed for Android and iOS devices to use native UI. This lets makers build stunning native apps for mobile users with device-optimized screens that use native UI elements instead of rendering inside of web view. This feature provides the following benefits:

- Brings modern mobile user experiences and interaction patterns
- Improves performance and reliability
- Integrates device capabilities with maker-defined UI

There's no need to rebuild apps as makers can use all the familiar app building elements to create device-optimized experiences, though there are some limitations around which [controls are supported natively today](./optimize-for-devices-controls.md). Apps that are optimized for devices work with other mobile features like [offline](./canvas-mobile-offline-overview.md), [push notifications](./power-apps-mobile-notification.md), and [wrap](../maker/common/wrap/overview.md).

> [!Important]
> - This is a preview feature.
> - Preview features aren't meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.

## How screens are optimized for devices

For a canvas app running on Power Apps mobile, there are UI elements, their current state, and the related business logic. For example, on a screen you might have a button that is currently at position 0, with a width and height of 200 and 40 respectively, and is fill color blue on top of having business logic defined on select with Power Fx that navigates the user to a different screen.

If optimize for devices is off for that screen, the screen loads and displays in a web view, running similarly to how it would in a desktop's web browser. When optimized for devices is on, each element's current state is passed over to the device where it renders that same element, but using native UI. So now we have a natively rendered, long blue button in the upper-left corner. Business logic modifies state or takes actions, which run the same way it did before, meaning that when the now natively rendered button is selected, the device runs Power Fx and the user is navigated to the specified screen.

What this means is that each [control needs a device-optimized](./optimize-for-devices-controls.md), native equivalent that supports the same properties so it can render the way a maker expects. During preview, there are some [limitations](optimize-for-devices-controls.md#known-limitations) to which controls and properties are supported. This is independent of whether a control is classic or modern, but rather a filter on the list of controls to ones that are device-optimized. 

## Enable screens to be device-optimized

There are two steps to enabling a screen to be optimized for devices.

1. The **Optimize for devices** experimental app setting must be turned on.

    The setting can be found in the **Settings** > **Upcoming features** > **Experimental** tab. Turning on the **Optimize for devices** app setting shows the **Optimize for devices** property on screens.

    :::image type="content" source="media/optimized-for-devices-app-setting.png" alt-text="Shows the app setting that enables Optimize for devices.":::

2. On each screen, the **Optimize for devices** property must be set to **On**.

    A maker can open the tree view in the left pane and select a screen where the **Optimize for devices** property will be. By setting this property to **On**, the screen will be rendered natively when running on Power Apps mobile in iOS and Android devices. 

    :::image type="content" source="media/optimized-for-devices-screen-setting.png" alt-text="Shows the screen setting that sets the screen to display natively.":::
