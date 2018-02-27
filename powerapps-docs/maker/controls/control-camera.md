---
title: 'Camera control: reference | Microsoft Docs'
description: Information, including properties and examples, about the Camera control
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
# Camera control in PowerApps
A control with which the user can take photos by using the camera on the device.

## Description
If you add this control, the user can update a data source with one or more photos from wherever the app is running.

## Key properties
**Camera** – On a device that has more than one camera, the numeric ID of the camera that the app uses.

## Additional properties
**[BorderColor](properties-color-border.md)** – The color of a control's border.

**[BorderStyle](properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](properties-color-border.md)** – The thickness of a control's border.

**Brightness** – How much light the user is likely to perceive in an image.

**Contrast** – How easily the user can distinguish between similar colors in an image.

**[DisplayMode](../../controls/properties-core.md)** – Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**).

**[Height](../../controls/properties-size-location.md)** – The distance between a control's top and bottom edges.

**[OnSelect](../../controls/properties-core.md)** – How the app responds when the user taps or clicks a control.

**OnStream** – How the app responds when the **Stream** property is updated.

**Photo** – The image captured  when the user takes a picture.

**Stream** – Automatically updated image based on the **StreamRate** property.

**StreamRate** – How often to update the image on the **Stream** property, in milliseconds.  This value can range from 100 (1/10th of a second) to 3,600,000 (1 hour).

**[Tooltip](../../controls/properties-core.md)** – Explanatory text that appears when the user hovers over a control.

**[Visible](../../controls/properties-core.md)** – Whether a control appears or is hidden.

**[Width](../../controls/properties-size-location.md)** – The distance between a control's left and right edges.

**[X](../../controls/properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](../../controls/properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

**Zoom** – The percentage by which an image from a camera is magnified or the view of a file in a PDF viewer.

## Related functions
[**Patch**( *DataSource*, *BaseRecord*, *ChangeRecord* )](../../functions/function-patch.md)

## Example
### Add photos to an Image gallery control
1. Add a **Camera** control, name it **MyCamera**, and set its **[OnSelect](../../controls/properties-core.md)** property to this formula:<br>
   **Collect(MyPix, MyCamera.Photo)**
   
    Don't know how to [add, name, and configure a control](../add-configure-controls.md)?
   
    Want more information about the **[Collect](../../functions/function-clear-collect-clearcollect.md)** function or [other functions](../formula-reference.md)?
2. Press F5, and then take a photo by clicking or tapping **MyCamera**.
3. Add an **[Image gallery](control-gallery.md)** control, and then resize its **[Image](control-image.md)** control, its template, and the **Image gallery** control itself to fit in the screen.
4. Set the **[Items](../../controls/properties-core.md)** property of the **Image gallery** control to this expression:<br>**MyPix.Url**.
5. Set the **[Image](../../controls/properties-visual.md)** property of the **Image** control in the gallery to this expression:<br>
   **ThisItem.Url**
   
    The photo that you took appears in the **Image gallery** control.
6. Take as many photos as you want, and then return to the default workspace by pressing Esc.
7. (optional) Set the **OnSelect** property of the **Image** control in the **Image gallery** control to **Remove(MyPix, ThisItem)**, press F5, and then click or tap a photo to remove it.

Use the **[SaveData](../../functions/function-savedata-loaddata.md)** function to save the photos locally or the **[Patch](../../functions/function-patch.md)** function to update a data source.

