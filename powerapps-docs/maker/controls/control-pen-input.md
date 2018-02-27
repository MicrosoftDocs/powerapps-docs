---
title: 'Pen input control: reference | Microsoft Docs'
description: Information, including properties and examples, about the Pen input control
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
# Pen input control in PowerApps
A control in which the user can draw, erase, and highlight areas of an image.

## Description
The user can use this control like a whiteboard, drawing diagrams and writing words that can be converted to typed text.

## Key properties
**[Color](properties-color-border.md)** – The color of input strokes.

**Mode** – The control is in **Draw** or **Erase** mode.  Select mode has been deprecated.

## Additional properties
**[BorderColor](properties-color-border.md)** – The color of a control's border.

**[BorderStyle](properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](properties-color-border.md)** – The thickness of a control's border.

**[DisplayMode](../../controls/properties-core.md)** – Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**).

**[Fill](properties-color-border.md)** – The background color of a control.

**[Height](../../controls/properties-size-location.md)** – The distance between a control's top and bottom edges.

**Input** – Input.

**[OnSelect](../../controls/properties-core.md)** – How the app responds when the user taps or clicks a control.

**[SelectionColor](properties-color-border.md)** – The text color of a selected item or items in a list or the color of the selection tool in a pen control.

**SelectionThickness** – The thickness of the selection tool for a pen-input control.

**ShowControls** – Whether an audio or video player shows, for example, a play button and a volume slider, and a pen control shows, for example, icons for drawing, erasing, and clearing.

**[Size](../../controls/properties-text.md)** – The font size of the text that appears on a control.

**[Tooltip](../../controls/properties-core.md)** – Explanatory text that appears when the user hovers over a control.

**[Visible](../../controls/properties-core.md)** – Whether a control appears or is hidden.

**[Width](../../controls/properties-size-location.md)** – The distance between a control's left and right edges.

**[X](../../controls/properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](../../controls/properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

## Related functions
[**Collect**( *CollectionName*, *DatatoCollect* )](../../functions/function-clear-collect-clearcollect.md)

## Example
### Create a set of images
1. Add a **Pen input** control, name it **MyDoodles**, and set its **ShowControls** property to **true**.
   
    Don't know how to [add, name, and configure a control](../add-configure-controls.md)?
2. Add a **[Button](control-button.md)** control, move it below **MyDoodles**, and set the **[Text](../../controls/properties-core.md)** property of the **[Button](control-button.md)** control to show **Add**.
3. Set the **[OnSelect](../../controls/properties-core.md)** property of the **[Button](control-button.md)** control to this formula:<br>
   **Collect(Doodles, {Sketch:MyDoodles.Image})**
4. Add an **Image gallery** control, move it below the **[Button](control-button.md)** control, and shrink the width of the **Image gallery** control until it shows three items.
5. Set the **[Items](../../controls/properties-core.md)** property of the **Image gallery** control to **Doodles**, and then  press F5.
6. Draw an image in **MyDoodles**, and then click or tap the **[Button](control-button.md)** control.
   
    The image that you drew appears in the **Image gallery** control.
7. (optional) In the **Pen input** control, click or tap the icon to clear the image that you drew, draw another image, and then click or tap the **[Button](control-button.md)** control.
8. In the **Image gallery** control, set the **[OnSelect](../../controls/properties-core.md)** property of the **[Image](control-image.md)** control to this formula:<br>
   **Remove(Doodles, ThisItem)**
9. Remove a drawing by clicking or tapping it in the **Image gallery** control.

Use the **[SaveData](../../functions/function-savedata-loaddata.md)** function to save your drawings locally or the **[Patch](../../functions/function-patch.md)** function to save them to a data source.

