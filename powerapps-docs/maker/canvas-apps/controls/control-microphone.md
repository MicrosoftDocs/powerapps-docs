---
title: 'Microphone control: reference | Microsoft Docs'
description: Information, including properties and examples, about the Microphone control
author: fikaradz
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: anneta
ms.date: 10/25/2016
ms.author: fikaradz
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Microphone control in PowerApps
A control that allows app users to record sounds from their device.

## Description
App users can make audio recordings if the device where the app is running has a microphone.

Audio is stored in 3gp format in Android, AAC format in iOS, and OGG format in web browsers.

## Key properties
**Mic** – On a device that has more than one microphone, the numeric ID of the microphone that the app uses.

**OnStop** – How the app responds when the user stops recording with a microphone control.

## Additional properties
**[AccessibleLabel](properties-accessibility.md)** – Label for screen readers. Should describe the purpose of the microphone.

**[BorderColor](properties-color-border.md)** – The color of a control's border.

**[BorderStyle](properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](properties-color-border.md)** – The thickness of a control's border.

**[Color](properties-color-border.md)** – The color of text in a control.

**[DisplayMode](properties-core.md)** – Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**).

**[DisabledBorderColor](properties-color-border.md)** – The color of a control's border if the control's **[DisplayMode](properties-core.md)** property is set to **Disabled**.

**[DisabledColor](properties-color-border.md)** – The color of text in a control if its **[DisplayMode](properties-core.md)** property is set to **Disabled**.

**[DisabledFill](properties-color-border.md)** – The background color of a control if its **[DisplayMode](properties-core.md)** property is set to **Disabled**.

**[Fill](properties-color-border.md)** – The background color of a control.

**[FocusedBorderColor](properties-color-border.md)** – The color of a control's border when the control is focused.

**[FocusedBorderThickness](properties-color-border.md)** – The thickness of a control's border when the control is focused.

**[Height](properties-size-location.md)** – The distance between a control's top and bottom edges.

**[HoverBorderColor](properties-color-border.md)** – The color of a control's border when the user keeps the mouse pointer on that control.

**[HoverColor](properties-color-border.md)** – The color of the text in a control when the user keeps the mouse pointer on it.

**[HoverFill](properties-color-border.md)** – The background color of a control when the user keeps the mouse pointer on it.

**[Image](properties-visual.md)** – The name of the image that appears in an image, audio, or microphone control.

**[ImagePosition](properties-visual.md)** – The position (**Fill**, **Fit**, **Stretch**, **Tile**, or **Center**) of an image in a screen or a control if it isn't the same size as the image.

**[OnSelect](properties-core.md)** – How the app responds when the user taps or clicks a control.

**OnStart** – How the app responds when the user starts to record with a microphone control.

**[PressedBorderColor](properties-color-border.md)** – The color of a control's border when the user taps or clicks that control.

**[PressedColor](properties-color-border.md)** – The color of text in a control when the user taps or clicks that control.

**[PressedFill](properties-color-border.md)** – The background color of a control when the user taps or clicks that control.

**[Reset](properties-core.md)** – Whether a control reverts to its default value.

**[TabIndex](properties-accessibility.md)** – Keyboard navigation order in relation to other controls.

**[Tooltip](properties-core.md)** – Explanatory text that appears when the user hovers over a control.

**[Visible](properties-core.md)** – Whether a control appears or is hidden.

**[Width](properties-size-location.md)** – The distance between a control's left and right edges.

**[X](properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

## Related functions
[**Patch**( *DataSource*, *BaseRecord*, *ChangeRecord* )](../functions/function-patch.md)

## Example
### Add sounds to a Custom gallery control
1. Add a **Microphone**, name it **MyMic**, and set its **OnStop** property to this formula:<br>
   **Collect(MySounds, MyMic.Audio)**

    Don't know how to [add, name, and configure a control](../add-configure-controls.md)?

    Want more information about the **[Collect](../functions/function-clear-collect-clearcollect.md)** function or [other functions](../formula-reference.md)?
2. Add a **Custom gallery** control, move it below **MyMic**, and set the **[Items](properties-core.md)** property for the **Custom gallery** control to **MySounds**.
3. In the template for the **Custom gallery** control, add an **[Audio](control-audio-video.md)** control, and set its **Media** property to **ThisItem.Url**.
4. Press F5, click or tap **MyMic** to start recording, and then click or tap it again to stop recording.
5. In the **Custom gallery** control, click or tap the play button in the **[Audio](control-audio-video.md)** control to play back your recording.
6. Add as many recordings as you want, and then return to the default workspace by pressing Esc.
7. (optional) In the template for the **Custom gallery** control, add a **[Button](control-button.md)** control, set its **[OnSelect](properties-core.md)** property to **Remove(MySounds, ThisItem)**, press F5, and then remove a recording by clicking or tapping the corresponding **Button** control.

Use the **[SaveData](../functions/function-savedata-loaddata.md)** function to save the recordings locally or the **[Patch](../functions/function-patch.md)** function to update a data source.


## Accessibility guidelines
The same guidelines for **[Button](control-button.md)**  apply because **Microphone** is just a specialized button. In addition, consider the following:

### Audio alternatives
* Consider adding an alternative form of input for users with speech disabilities or without a microphone. For example, **[Text input](control-text-input.md)** to allow users to enter text.

### Color contrast
There must be adequate color contrast between:
* **[Image](properties-visual.md)** and the button text and icon (if applicable)

This is in addition to the [standard color contrast requirements](../accessible-apps-color.md).

### Screen reader support
* **[AccessibleLabel](properties-accessibility.md)** must be present.
