---
title: Add picture control in canvas apps
description: Information, including properties and examples, about the Add picture control.
author: chmoncay
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.date: 04/17/2020
ms.subservice: canvas-maker
ms.author: chmoncay
ms.reviewer: tapanm
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - tapanm-msft
  - chmoncay
---
# Add picture control in canvas apps

Takes a photo or loads images from the local device.

## Description
With this control users can take photos or upload image files from their device and update the data source with this content. On a mobile device the user is presented with the device's choice dialog to choose between taking a photo or selecting one already available.

This control is a grouped control containing two controls: an **Image** and an **Add picture button**. The **Image** control shows the uploaded image or a placeholder if no image has been uploaded. The **Add picture button** prompts for an image to be uploaded.

See the [Image control reference](control-image.md) for **Image** properties.

## Add picture button properties
**[AccessibleLabel](properties-accessibility.md)** – Label for screen readers. Should describe the purpose of adding a picture.

**[Align](properties-text.md)** – The location of text in relation to the horizontal center of its control.

**[BorderColor](properties-color-border.md)** – The color of a control's border.

**[BorderStyle](properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](properties-color-border.md)** – The thickness of a control's border.

**ChangePictureText** – Text that appears on the button when an image has been uploaded.

**[Color](properties-color-border.md)** – The color of text in a control.

**[DisabledBorderColor](properties-color-border.md)** – The color of a control's border if the control's **[DisplayMode](properties-core.md)** property is set to **Disabled**.

**[DisabledColor](properties-color-border.md)** – The color of text in a control if its **[DisplayMode](properties-core.md)** property is set to **Disabled**.

**[DisabledFill](properties-color-border.md)** – The background color of a control if its **[DisplayMode](properties-core.md)** property is set to **Disabled**.

**[DisplayMode](properties-core.md)** – Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**).

**Error** - If there is a problem uploading an image, this property will contain an appropriate error string.

**[Fill](properties-color-border.md)** – The background color of a control.

**[FocusedBorderColor](properties-color-border.md)** – The color of a control's border when the control is focused.

**[FocusedBorderThickness](properties-color-border.md)** – The thickness of a control's border when the control is focused.

**[Font](properties-text.md)** – The name of the family of fonts in which text appears.

**[FontWeight](properties-text.md)** – The weight of the text in a control: **Bold**, **Semibold**, **Normal**, or **Lighter**.

**[Height](properties-size-location.md)** – The distance between a control's top and bottom edges.

**[HoverBorderColor](properties-color-border.md)** – The color of a control's border when the user keeps the mouse pointer on that control.

**[HoverColor](properties-color-border.md)** – The color of the text in a control when the user keeps the mouse pointer on it.

**[HoverFill](properties-color-border.md)** – The background color of a control when the user keeps the mouse pointer on it.

**[Italic](properties-text.md)** – Whether the text in a control is italic.

**Media** – An identifier for the clip that an audio or video control plays.

**[OnChange](properties-core.md)** – Actions to perform when the user changes the value of a control (for example, by adjusting a slider).

**[OnSelect](properties-core.md)** – Actions to perform when the user taps or clicks a control.

**[Padding](properties-size-location.md)** – The distance between the text on an import or export button and the edges of that button.

**[PressedBorderColor](properties-color-border.md)** – The color of a control's border when the user taps or clicks that control.

**[PressedColor](properties-color-border.md)** – The color of text in a control when the user taps or clicks that control.

**[PressedFill](properties-color-border.md)** – The background color of a control when the user taps or clicks that control.

**[Reset](properties-core.md)** – Whether a control reverts to its default value.

**[Size](properties-text.md)** – The font size of the text that appears on a control.

**[Strikethrough](properties-text.md)** – Whether a line appears through the text that appears on a control.

**[TabIndex](properties-accessibility.md)** – Keyboard navigation order in relation to other controls.

**[Text](properties-core.md)** – Text that appears on the button when an image has not been uploaded.

**[Tooltip](properties-core.md)** – Explanatory text that appears when the user hovers over a control.

**[Underline](properties-text.md)** – Whether a line appears under the text that appears on a control.

**UseMobileCamera** – Whether to use a mobile camera directly, when available.

**[VerticalAlign](properties-text.md)** – The location of text on a control in relation to the vertical center of that control.

**[Visible](properties-core.md)** – Whether a control appears or is hidden.

**[Width](properties-size-location.md)** – The distance between a control's left and right edges.

**[X](properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

## Related functions
[**Patch**( *DataSource*, *BaseRecord*, *ChangeRecord* )](../functions/function-patch.md)

## Examples
### Add images to an Image gallery control
1. Add an **Add picture** control, and then triple-click it.
   
    Don't know how to [add, name, and configure a control](../add-configure-controls.md)?
1. In the **Open** dialog box, click or tap an image file, and then click or tap **Open**.
1. Add a **[Button](control-button.md)** control, move it under the **Add picture** control, and set the **[OnSelect](properties-core.md)** property for the **[Button](control-button.md)** control to this formula:<br>
   **Collect(MyPix, AddMediaButton1.Media)**
   
    Want more information about the **[Collect](../functions/function-clear-collect-clearcollect.md)** function or [other functions](../formula-reference.md)?
1. Add a **Vertical gallery** control, and set its **[Items](properties-core.md)** property to **MyPix**.
1. Select the **[Image](control-image.md)** control in the gallery and set it's **Image** property to **ThisItem.Value**.
1. Press F5, and then click or tap the **[Button](control-button.md)** control.
   
    The image from the **Add picture** control appears in the **Vertical Gallery** control. If your image doesn't have the same aspect ratio as the **[Image](control-image.md)** control in the **Vertical gallery** control, set the **[ImagePosition](properties-visual.md)** property of the **[Image](control-image.md)** control to **Fit**.
1. Click or tap the **Add picture** control, click or tap another image file, click or tap **Open**, and then click or tap the **[Button](control-button.md)** control that you added.
   
    The second image appears in the **Image gallery** control.
1. (optional) Repeat the previous step one or more times, and then return to the default workspace by pressing Esc.

Use the **[SaveData](../functions/function-savedata-loaddata.md)** function to save the images locally or the **[Patch](../functions/function-patch.md)** function to update a data source.


## Accessibility guidelines
The same guidelines for **[Button](control-button.md)** and **[Image](control-image.md)** apply. In addition, consider the following:

### Color contrast
* **Add picture button** must have adequate contrast between its text and background. Since the uploaded image may have varying colors, use an opaque **[Fill](properties-color-border.md)** on the **Add picture button** to ensure consistent contrast.

### Screen reader support
* **Add picture button** must have **Text** and **ChangePictureText** that prompts the user to add or change a picture.

### Keyboard support
* **Add picture button** must have **[TabIndex](properties-accessibility.md)** of zero or greater so that keyboard users can navigate to it.
* **Add picture button** must have clearly visible focus indicators. Use **[FocusedBorderColor](properties-color-border.md)** and **[FocusedBorderThickness](properties-color-border.md)** to achieve this.
 


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]