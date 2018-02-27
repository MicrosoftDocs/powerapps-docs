---
title: 'Image control: reference | Microsoft Docs'
description: Information, including properties and examples, about the Image control
services: ''
suite: powerapps
documentationcenter: na
author: fikaradz
manager: anneta
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 10/25/2016
ms.author: fikaradz

---
# Image control in PowerApps
A control that shows an image from, for example, a local file or a data source.

## Description
If you add one or more **Image** controls to your app, you can show individual images that aren't part of a data set, or you can incorporate images from records in data sources.

## Key properties
**[Image](../../controls/properties-visual.md)** – The name of the image that appears in an image, audio, or microphone control.

## Additional properties
**ApplyEXIFOrientation** – Whether to automatically apply the orientation specified in the EXIF data embedded with the image.

**AutoDisableOnSelect** – Automatically disables the control while the OnSelect behavior is executing.

**[BorderColor](properties-color-border.md)** – The color of a control's border.

**[BorderStyle](properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](properties-color-border.md)** – The thickness of a control's border.

**[FocusedBorderThickness](properties-color-border.md)** – The thickness of the control's border when it has keyboard focus.

**CalculateOriginalDimensions** – Enables the **OriginalHeight** and **OriginalWidth** properties.

**[DisplayMode](properties-core.md)** – Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**).

**[DisabledBorderColor](properties-color-border.md)** – The color of a control's border if the control's **[DisplayMode](properties-core.md)** property is set to **Disabled**.

**[DisabledFill](properties-color-border.md)** – The background color of a control if its **[DisplayMode](properties-core.md)** property is set to **Disabled**.

**[Fill](properties-color-border.md)** – The background color of a control.

**FlipHorizontal** – Whether to flip the image horizontally before displaying it.

**FlipVertical** – Whether to flip the image vertically before displaying it.

**[Height](../../controls/properties-size-location.md)** – The distance between a control's top and bottom edges.

**[HoverBorderColor](properties-color-border.md)** – The color of a control's border when the user keeps the mouse pointer on that control.

**[HoverFill](properties-color-border.md)** – The background color of a control when the user keeps the mouse pointer on it.

**[ImagePosition](../../controls/properties-visual.md)** – The position (**Fill**, **Fit**, **Stretch**, **Tile**, or **Center**) of an image in a screen or a control if it isn't the same size as the image.

**ImageRotation** – How to rotate the image before displaying it.  Values can be none, clockwise (CW) 90 degrees, counter-clockwise (CCW) 90 degrees and clockwise 180 degrees.

**[OnSelect](properties-core.md)** – How the app responds when the user taps or clicks a control.

**OriginalHeight** – Original height of an image, enabled with the **CalculateOriginalDimensions** property.

**OriginalWidth** – Original width of an image, enabled with the **CalculateOriginalDimensions** property.

**[PaddingBottom](../../controls/properties-size-location.md)** – The distance between text in a control and the bottom edge of that control.

**[PaddingLeft](../../controls/properties-size-location.md)** – The distance between text in a control and the left edge of that control.

**[PaddingRight](../../controls/properties-size-location.md)** – The distance between text in a control and the right edge of that control.

**[PaddingTop](../../controls/properties-size-location.md)** – The distance between text in a control and the top edge of that control.

**[PressedBorderColor](properties-color-border.md)** – The color of a control's border when the user taps or clicks that control.

**[PressedFill](properties-color-border.md)** – The background color of a control when the user taps or clicks that control.

**[RadiusBottomLeft](../../controls/properties-size-location.md)** – The degree to which the bottom-left corner of a control is rounded.

**[RadiusBottomRight](../../controls/properties-size-location.md)** – The degree to which the bottom-right corner of a control is rounded.

**[RadiusTopLeft](../../controls/properties-size-location.md)** – The degree to which the top-left corner of a control is rounded.

**[RadiusTopRight](../../controls/properties-size-location.md)** – The degree to which the top-right corner of a control is rounded.

**[Tooltip](properties-core.md)** – Explanatory text that appears when the user hovers over a control.

**Transparency** – The degree to which controls behind an image remain visible.

**[Visible](properties-core.md)** – Whether a control appears or is hidden.

**[Width](../../controls/properties-size-location.md)** – The distance between a control's left and right edges.

**[X](../../controls/properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](../../controls/properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

## Related functions
[**Remove**( *DataSource*, ThisItem )](../../functions/function-remove-removeif.md)

## Examples
### Show an image from a local file
1. On the **Content** tab, click or tap **Media**, and then click or tap **Browse**.
2. Click or tap the image file that you want to add, click or tap **Open**, and then press Esc to return to the default workspace.
3. Add an **Image** control, and set its **[Items](properties-core.md)** property to the name of the file that you added.

    Don't know how to [add and configure a control](../add-configure-controls.md)?

    The **Image** control shows the image that you specified.

### Show a set of images from a data source
1. Download this [Excel file](https://pwrappssamples.blob.core.windows.net/samples/FlooringEstimates.xlsx), and save it on your local device.
2. In PowerApps Studio, create or open an app, and then click or tap **Add data source** in the right-hand pane.

    If **Add data source** doesn't appear in the right-hand pane, click or tap a screen in the left navigation bar.
3. Click or tap **Add static data to your app**, click or tap the Excel file that you downloaded, and then click or tap **Open**.
4. Select the **Flooring Estimates** check box, and then click or tap **Connect**.
5. Add a **Gallery** control with images, and set its **[Items](properties-core.md)** property to **FlooringEstimates**.

    Don't know how to [add and configure a control](../add-configure-controls.md)?

    The **Gallery** control shows images of carpet, hardwood, and tile products based on links in the Excel file that you downloaded.
