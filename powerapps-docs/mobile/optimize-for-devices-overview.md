---
title: Optimize for devices overview (preview)
description: Learn how to make your canvas app screens optimized for devices. 
author: anuitz
ms.topic: how-to
ms.custom: canvas
ms.reviewer: smurkute
ms.date: 05/01/2024
ms.subservice: canvas-maker
ms.author: anuitz
search.audienceType: 
  - maker
contributors:
  - smurkute
  - anuitz
  - gachasta
---

# Optimize for devices overview (preview)

[This article is prerelease documentation and is subject to change.]

**Optimize for devices** is a feature that changes the way canvas app screens are loaded and displayed on Android and iOS devices. This feature lets makers build stunning, native apps for mobile users with device-optimized screens that use native UI elements, instead of rendering inside of web view. Device-optimizes screens provide the following benefits:

- Modern mobile user experiences and interaction patterns
- Improved performance and reliability
- Integrated device capabilities with maker-defined UI

There's no need to rebuild apps as makers can use all the familiar app-building elements to create device-optimized experiences, though there are some [limitations](./optimize-for-devices-controls.md). Apps that are optimized for devices work with other mobile features such as [offline](./canvas-mobile-offline-overview.md), [push notifications](./power-apps-mobile-notification.md), and [wrap](../maker/common/wrap/overview.md).

> [!Important]
> - This is a preview feature.
> - Preview features aren't meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.


## Allow screens to be device-optimized

1. Select **Settings** > **Upcoming features** > **Preview** > **Optimize for devices**.
2. Only use supported controls on the screen.

After this feature is turned on, you can find which controls are supported in the **Insert** pane by selecting the **Device optimized (preview)** filter. Learn more about [which controls are supported natively today](./optimize-for-devices-controls.md).

Screens made solely with device-optimized controls automatically render natively on Android and iOS devices. An app can have screens which are optimized, while some others aren't. This only depends on the controls chosen by the maker to create that screen.

## How screens are optimized for devices

For a canvas app running on Power Apps mobile, there are UI elements, their current state, and the related business logic that determines how screens are optimized. For example, on a screen you might have a button at position 0, with a width and height of 200 and 40 respectively, and with fill color blue. The business logic, with Power Fx, lets you navigate the user to a different screen.

If the **Optimize for devices** option is off for that screen, the screen loads and displays in a web view, running similarly to how it would in a desktop's web browser. When **Optimize for devices** is on, each element's current state is passed over to the device where it renders that same element, but using native UI. So now we have a natively rendered, long blue button in the upper-left corner. Business logic modifies state or takes actions, which runs the same way it did before. When the natively rendered button is selected, the device runs Power Fx and the user is navigated to the specified screen.

Each [control needs a device-optimized](./optimize-for-devices-controls.md), native equivalent that supports the same properties so it can render the way a maker expects. During preview, there are some [limitations](optimize-for-devices-controls.md#known-limitations) to which controls and properties are supported. Whether a control is classic or modern, it filters the list of controls for device-optimized ones.

### Related information

[Supported platforms for running apps using the Power Apps mobile app](/power-apps/limits-and-config#supported-platforms-for-running-apps-using-the-power-apps-mobile-app)   

[!INCLUDE[footer-include](../includes/footer-banner.md)]
