---
title: Optimize for devices controls
description: Learn which controls and properties are supported for device-optimized screens.
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

# Optimize for devices controls

For a screen to be optimized for devices, it must use controls that are supported natively. You can filter the control **Insert** pane to only show device-optimized controls. 

:::image type="content" source="media/optimized-for-devices-control-filter.png" alt-text="The Insert pane is filtered to only show controls that are device-optimized.":::


## Device-optimized controls
The following controls are available for screens that are optimized for devices. All other controls are currently unsupported.

[**Modern controls**](../maker/canvas-apps/controls/modern-controls/modern-controls-reference.md)
 - Button
 - Checkbox
 - Date picker
 - Form
 - Text
 - Text input
 - Toggle

 [**Controls**](../maker/canvas-apps/reference-properties.md)
 - Add picture
 - Barcode reader
 - Button
 - Camera
 - Check box
 - Circle
 - Container (horizontal and vertical included)
 - Form (edit and display)
 - Gallery (vertical, horizontal, flexible height)
 - Icon (all icons supported)
 - Image
 - Radio
 - Rectangle
 - Text input
 - Text label
 - Timer

## Unsupported controls

If a screen is set to be optimized for devices, but has an unsupported control, an error message in a box is displayed. 

:::image type="content" source="media/optimized-for-devices-control-error.png" alt-text="The error that shows when an unsupported control is on a screen set to optimize for devices.":::

## Device-optimized properties

For device capabilities to be brought inline requires specific configuration. 

For the [barcode reader](../maker/canvas-apps/controls/control-barcodereader.md) control, the maker can select **Scan Inline** for the **Scanning mode** property. In Studio, when this mode is selected, the control will show as an warning box indicating the control will only work on mobile devices. On device, in a screen optimized for devices, the control will show a camera feed and enable barcode scanning.

## Known limitations

As optimize for devices is in preview, there are the limitations listed below.

 - Only the **Segoe UI** font is supported. If a control is using another font, it will instead show with the Segoe UI font. Due to the differences in fonts, this can result in the control taking up more or less space than expected, so it is recommended to use only the Segoe UI font for device-optimized screens.
 - **Image** control when showing an SVG only supports the fit and stretch image position options. It will default to fit if another option is selected. All other image types work as expected for all image positions. 
 - In the **modern Text** control, the Semi-bold and Medium font weights are not supported on Android devices. It will display a regular font weight.
 - In the **modern Text input** control, the **Value** property when set to a Power Fx variable will not display at first navigation. It will instead show the placeholder value until the user navigates away and back to the screen with the modern Text input control.
 - In the **modern Text input** control, the **OnChange** property is called twice when the control is exited and then blurred.
 - In the **modern Text input** control, the **Validate state** property does not display a red border around the control. 
 - In the **Image** control, the **Image rotation** property is not supported. Instead, the image will not be rotated.
 - In the **Dropdown** and **Radio** control, the **Items** property does not support references to other controls. Items will not be shown if they are complex values like references. 
 - In the **modern Date picker** control, tapping on the control opens a modal with a calendar instead of allowing users to type into the control directly. 
 - In the **modern Date picker** control, the **Base pallete color** and modern theme are not applied on Android devices. Instead, it will show as the device's theme color.
 - In the **Button**, **Image**, **Label**, and **Icon** controls, the **SetFocus** Power Fx function does not support keyboard focus, only accessibility focus (e.g. screen reader).
 - In **Horizontal and vertical containers**, the **Drop shadow** property is not supported. Instead, containers will display without drop shadow. 
 - In **Horizontal and vertical containers**, the **Scroll** option only works for a single direction, depending on the **Wrap** property. If **Wrap** is off, the container is scrollable in the primary direction, otherwise it is scrollable in the secondary direction. 
 - Multiple **Barcode reader** controls on a single screen is not supported.
 - Multiple **Camera** controls on a single screen is not supported. 
 - In the **Camera** control, the **Display mode** property of the parent control is not supported. For example, if the camera control is part of a form that is set to view mode, the camera will still be in edit mode. 
 - On **Screen**, the **Background image** property is not supported.
