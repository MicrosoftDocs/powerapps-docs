---
title: 'Microphone control: reference | Microsoft Docs'
description: Information, including properties and examples, about the Microphone control
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
# Microphone control in PowerApps
A control with which the user can record sounds.

## Description
If you add this control, the user can update a data source with one or more sounds from wherever the app is running.

## Key properties
**Mic** – On a device that has more than one microphone, the numeric ID of the microphone that the app uses.

**OnStop** – How the app responds when the user stops recording with a microphone control.

## Additional properties
**[BorderColor](properties-color-border.md)** – The color of a control's border.

**[BorderStyle](properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](properties-color-border.md)** – The thickness of a control's border.

**[Color](properties-color-border.md)** – The color of text in a control.

**[DisplayMode](properties-core.md)** – Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**).

**[DisabledBorderColor](properties-color-border.md)** – The color of a control's border if the control's **[DisplayMode](properties-core.md)** property is set to **Disabled**.

**[DisabledColor](properties-color-border.md)** – The color of text in a control if its **[DisplayMode](properties-core.md)** property is set to **Disabled**.

**[DisabledFill](properties-color-border.md)** – The background color of a control if its **[DisplayMode](properties-core.md)** property is set to **Disabled**.

**[Fill](properties-color-border.md)** – The background color of a control.

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
   
    Don't know how to [add, name, and configure a control](../maker/add-configure-controls.md)?
   
    Want more information about the **[Collect](../functions/function-clear-collect-clearcollect.md)** function or [other functions](../formula-reference.md)?
2. Add a **Custom gallery** control, move it below **MyMic**, and set the **[Items](properties-core.md)** property for the **Custom gallery** control to **MySounds**.
3. In the template for the **Custom gallery** control, add an **[Audio](control-audio-video.md)** control, and set its **Media** property to **ThisItem.Url**.
4. Press F5, click or tap **MyMic** to start recording, and then click or tap it again to stop recording.
5. In the **Custom gallery** control, click or tap the play button in the **[Audio](control-audio-video.md)** control to play back your recording.
6. Add as many recordings as you want, and then return to the default workspace by pressing Esc.
7. (optional) In the template for the **Custom gallery** control, add a **[Button](control-button.md)** control, set its **[OnSelect](properties-core.md)** property to **Remove(MySounds, ThisItem)**, press F5, and then remove a recording by clicking or tapping the corresponding **Button** control.

Use the **[SaveData](../functions/function-savedata-loaddata.md)** function to save the recordings locally or the **[Patch](../functions/function-patch.md)** function to update a data source.

