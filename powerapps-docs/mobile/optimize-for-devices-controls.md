---
title: Optimize for devices (preview)
description: Learn which controls and properties are supported for device-optimized screens.
author: anuitz
ms.topic: article
ms.custom: canvas
ms.reviewer: smurkute
ms.date: 05/01/2024
ms.subservice: canvas-maker
ms.author: anuitz
search.audienceType: 
  - maker
contributors:
- gachasta 
- smurkute
ms.contributors:
- devangpandya
---

# Optimize for devices (preview)

For a screen to be optimized for devices, it must use controls that are supported natively. You can filter the control Insert pane to only show device-optimized controls.
:::image type="content" source="media/optimized-for-devices-control-filter.png" alt-text="The Insert pane is filtered to only show controls that are device-optimized.":::

> [!Important]
> - This is a preview feature. Documentation is subject to change.
> - Preview features aren't meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.

## Device-optimized controls

The following controls are optimized for iOS and Android devices. All other controls are currently unsupported. A screen that has one or more unsupported controls automatically renders in a web view instead of native UI. Learn more: [Optimize for devices overview](optimize-for-devices-overview.md).

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
- Form
- Gallery (vertical, horizontal, flexible height)
- Icon (all icons supported)
- Image
- Radio
- Rectangle
- Text input
- Text label
- Timer

### [Modern controls](../maker/canvas-apps/controls/modern-controls/modern-controls-reference.md)

- Button
- Check box
- Date picker
- Text
- Text input
- Toggle

Learn more: [Overview of modern controls and themes in canvas apps](../maker/canvas-apps/controls/modern-controls/overview-modern-controls.md)

## Unsupported controls

If a screen has an unsupported control, the screen automatically reverts to render with a web view.

## Device-optimized properties

Some properties must be configured so they're optimized for devices. For example, consider the [barcode reader](../maker/canvas-apps/controls/control-barcodereader.md) control. The maker can select **Scan Inline** for the **Scanning mode** property. In Power Apps Studio, when this mode is selected, the control displays as a warning box indicating that the control only works on mobile devices. On a device, in a screen optimized for devices, the control displays a camera feed to allow barcode scanning.

## Known limitations

Note the following limitations with the 'optimize for devices' feature.

- The **Image** control, when showing an SVG file, only supports the fit, fill, and stretch image position options. Its default behavior is to fit, if another option is selected. All other image types work as expected for all image positions.
- In the **modern Text input** control, the **Value** property, when set to a Power Fx variable, isn't displayed at first navigation. Instead, it shows the placeholder value until the user navigates away and back to the screen with the **modern Text input** control.
- In the **modern Text input** control, the **OnChange** property is called each time the user interacts with the control, instead of when navigating away from the control.
- In the **modern Text input** control, the **Validate state** property doesn't display a red border around the control.
- In the **Image** control, the **Image rotation** property isn't supported. The image isn't rotated.
- In the **Dropdown** and **Radio** control, the **Items** property doesn't support references to other controls. Items aren't shown if they're complex values, like references.
- In the **modern Date picker** control, tapping on the control opens a modal with a calendar instead of allowing users to type into the control directly.
- In the **modern Date picker** control, the **Base palette color** and modern theme aren't applied on Android devices. Instead, it displays as the device's theme color.
- In the **Button**, **Image**, **Label**, and **Icon** controls, the **SetFocus** Power Fx function doesn't support keyboard focus, only accessibility focus (for example, screen reader).
- In **Horizontal and vertical containers**, the **Scroll** option only works for a single direction, depending on the **Wrap** property. If **Wrap** is off, the container is scrollable in the primary direction, otherwise it's scrollable in the secondary direction.
- Multiple **Barcode reader** controls on a single screen aren't supported.
- Multiple **Camera** controls on a single screen aren't supported.
- In the **Camera** control, the **Display mode** property of the parent control isn't supported. For example, if the camera control is part of a form that is set to view mode, the camera might still be in edit mode.
