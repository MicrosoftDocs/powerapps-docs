---
title: Optimize for devices controls (preview)
description: Learn which controls and properties are supported for device-optimized screens.
author: anuitz
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: sericks
ms.date: 03/14/2024
ms.subservice: canvas-maker
ms.author: anuitz
search.audienceType: 
  - maker
contributors:
  - sericks
  - anuitz
ms.contributors:
- devangpandya
---

# Optimize for devices controls (preview)

[This article is prerelease documentation and is subject to change.]

For a screen to be optimized for devices, it must use controls that are supported natively. You can filter the control **Insert** pane to only show device-optimized controls. 

:::image type="content" source="media/optimized-for-devices-control-filter.png" alt-text="The Insert pane is filtered to only show controls that are device-optimized.":::

> [!Important]
> - This is a preview feature.
> - Preview features aren't meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.

## Device-optimized controls

The following controls are available for screens that are optimized for devices. All other controls are currently unsupported.

### [Modern controls](../maker/canvas-apps/controls/modern-controls/modern-controls-reference.md)

- Button
- Check box
- Date picker
- Text
- Text input
- Toggle

#### Turn on modern controls

Makers must complete the following steps to turn on modern controls and themes for an app.

1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
1. In the navigation pane, select **Apps**.
1. Select an app.
1. Select **Settings** in the command bar.
1. In the **Settings** window, select **General**.
1. Turn on the **Modern controls and themes** option.

### [Controls](../maker/canvas-apps/reference-properties.md)

- Add picture
- Attachment
- Barcode reader
- Button
- Camera
- Check box
- Circle
- Components
- Container (horizontal and vertical included)
- Gallery (vertical, horizontal, flexible height)
- Icon (all icons supported)
- Image
- Radio
- Rectangle
- Text input
- Text label
- Timer

## Unsupported controls

If a screen is set for optimization for devices, but has an unsupported control, you see an error message in a box.

:::image type="content" source="media/optimized-for-devices-control-error.png" alt-text="The error that shows when an unsupported control is on a screen set to optimize for devices.":::

## Device-optimized properties

Some properties must be configured so they're optimized for devices. For example, consider the [barcode reader](../maker/canvas-apps/controls/control-barcodereader.md) control. The maker can select **Scan Inline** for the **Scanning mode** property. In Power Apps Studio, when this mode is selected, the control displays as a warning box indicating the control only works on mobile devices. On a device, in a screen optimized for devices, the control displays a camera feed to enable barcode scanning.

## Known limitations

Note the following limitations with the 'optimize for devices' feature.

- Only the **Segoe UI** font is supported. If a control is using another font, it displays the Segoe UI font instead. Due to the differences in fonts, the control can take up more or less space than expected. We recommend that you use the Segoe UI font for device-optimized screens.
- The **Image** control, when showing an SVG, only supports the fit and stretch image position options. Its default behavior is to fit, if another option is selected. All other image types work as expected for all image positions.
- In the **modern Text** control, the **Semi-bold** and **Medium** font weights aren't supported on Android devices. It displays a regular font weight instead.
- In the **modern Text input** control, the **Value** property, when set to a Power Fx variable, isn't displayed at first navigation. Instead, it shows the placeholder value until the user navigates away and back to the screen with the **modern Text input** control.
- In the **modern Text input** control, the **OnChange** property is called twice when the control is exited, and then blurred.
- In the **modern Text input** control, the **Validate state** property doesn't display a red border around the control.
- In the **Image** control, the **Image rotation** property isn't supported. The image isn't rotated.
- In the **Dropdown** and **Radio** control, the **Items** property doesn't support references to other controls. Items aren't shown if they're complex values, like references.
- In the **modern Date picker** control, tapping on the control opens a modal with a calendar instead of allowing users to type into the control directly.
- In the **modern Date picker** control, the **Base palette color** and modern theme aren't applied on Android devices. Instead, it displays as the device's theme color.
- In the **Button**, **Image**, **Label**, and **Icon** controls, the **SetFocus** Power Fx function doesn't support keyboard focus, only accessibility focus (for example, screen reader).
- In **Horizontal and vertical containers**, the **Drop shadow** property isn't supported. Instead, containers display without drop shadow.
- In **Horizontal and vertical containers**, the **Scroll** option only works for a single direction, depending on the **Wrap** property. If **Wrap** is off, the container is scrollable in the primary direction, otherwise it's scrollable in the secondary direction.
- Multiple **Barcode reader** controls on a single screen aren't supported.
- Multiple **Camera** controls on a single screen aren't supported.
- In the **Camera** control, the **Display mode** property of the parent control isn't supported. For example, if the camera control is part of a form that is set to view mode, the camera might still be in edit mode.
- On **Screen**, the **Background image** property isn't supported.
