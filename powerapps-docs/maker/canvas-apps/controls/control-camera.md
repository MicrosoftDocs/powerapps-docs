---
title: 'Camera control: reference | Microsoft Docs'
description: Information, including properties and examples, about the Camera control
author: fikaradz
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.date: 10/25/2016
ms.author: fikaradz
ms.reviewer: anneta
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Camera control in PowerApps
A control with which the user can take photos by using the camera on the device.

## Description
If you add this control, the user can update a data source with one or more photos from wherever the app is running.

## Key properties
**Camera** – On a device that has more than one camera, the numeric ID of the camera that the app uses.

## Additional properties
**[AccessibleLabel](properties-accessibility.md)** – Label for screen readers. Should describe the purpose of taking a picture.

**[BorderColor](properties-color-border.md)** – The color of a control's border.

**[BorderStyle](properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](properties-color-border.md)** – The thickness of a control's border.

**Brightness** – How much light the user is likely to perceive in an image.

**Contrast** – How easily the user can distinguish between similar colors in an image.

**[DisplayMode](properties-core.md)** – Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**).

**[FocusedBorderColor](properties-color-border.md)** – The color of a control's border when the control is focused.

**[FocusedBorderThickness](properties-color-border.md)** – The thickness of a control's border when the control is focused.

**[Height](properties-size-location.md)** – The distance between a control's top and bottom edges.

**[OnSelect](properties-core.md)** – How the app responds when the user taps or clicks a control.

**OnStream** – How the app responds when the **Stream** property is updated.

**Photo** – The image captured  when the user takes a picture.

**Stream** – Automatically updated image based on the **StreamRate** property.

**StreamRate** – How often to update the image on the **Stream** property, in milliseconds.  This value can range from 100 (1/10th of a second) to 3,600,000 (1 hour).

**[TabIndex](properties-accessibility.md)** – Keyboard navigation order in relation to other controls.

**[Tooltip](properties-core.md)** – Explanatory text that appears when the user hovers over a control.

**[Visible](properties-core.md)** – Whether a control appears or is hidden.

**[Width](properties-size-location.md)** – The distance between a control's left and right edges.

**[X](properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

## Related functions
[**Patch**( *DataSource*, *BaseRecord*, *ChangeRecord* )](../functions/function-patch.md)

## Example
### Add photos to an Image gallery control
1. Add a **Camera** control, name it **MyCamera**, and set its **[OnSelect](properties-core.md)** property to this formula:<br>
   **Collect(MyPix, MyCamera.Photo)**

    Don't know how to [add, name, and configure a control](../add-configure-controls.md)?

    Want more information about the **[Collect](../functions/function-clear-collect-clearcollect.md)** function or [other functions](../formula-reference.md)?
2. Press F5, and then take a photo by clicking or tapping **MyCamera**.
3. Add an **[Vertical gallery](control-gallery.md)** control, and then resize its **[Image](control-image.md)** control, its template, and the **Image gallery** control itself to fit in the screen.
4. Set the **[Items](properties-core.md)** property of the **Image gallery** control to:<br>**MyPix**.
5. Set the **[Image](properties-visual.md)** property of the **Image** control in the gallery to this expression:<br>
   **ThisItem.Url**

    The photo that you took appears in the **Image gallery** control.
6. Take as many photos as you want, and then return to the default workspace by pressing Esc.
7. (optional) Set the **OnSelect** property of the **Image** control in the **Image gallery** control to **Remove(MyPix, ThisItem)**, press F5, and then click or tap a photo to remove it.

Use the **[SaveData](../functions/function-savedata-loaddata.md)** function to save the photos locally or the **[Patch](../functions/function-patch.md)** function to update a data source.


## Accessibility guidelines
In addition to showing the camera feed, the entire camera control also functions as a button that takes a picture. Thus, there are similar accessibility considerations as with buttons.

### Video alternatives
* Consider adding an alternative form of input for users with visual disabilities. For example, **[Add picture](control-add-picture.md)** to allow users to upload an image from their device.

### Color contrast
There must be adequate color contrast between:
* **[FocusedBorderColor](properties-color-border.md)** and the outside color

### Screen reader support
* **[AccessibleLabel](properties-accessibility.md)** must be present.

### Keyboard support
* **[TabIndex](properties-accessibility.md)** must be zero or greater so that keyboard users can navigate to it.
* Focus indicators must be clearly visible. Use **[FocusedBorderColor](properties-color-border.md)** and **[FocusedBorderThickness](properties-color-border.md)** to achieve this.
