---
title: 'Microphone control: reference | Microsoft Docs'
description: Information, including properties and examples, about the Microphone control
author: chmoncay
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 03/11/2020
ms.author: chmoncay
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Microphone control in Power Apps

A control that allows app users to record sounds from their device.

## Description

App users can record audio using the microphone on a device running the app. Recorded audio can be:

- Played back with the [Audio](control-audio-video.md) control.
- Temporarily put in a variable or a collection.
- Stored in a database.

Format of the recorded audio:

- *3gp* format for *Android*.
- *AAC* format for *iOS*.
- *OGG* format for the *web browsers.

## Key properties

**Mic** – Numeric ID of the microphone on a device that has more than one microphone.

**OnStop** – How the app responds when the user stops recording with a microphone control.

**Audio** – The audio clip captured when the user records with the device's microphone. Captured media is referenced by a URI. For more information, see the [data type documentation](../functions/data-types.md#uris-for-images-and-other-media)

## Additional properties

[AccessibleLabel](properties-accessibility.md) – Label for screen readers. Should describe the purpose of the microphone.

[BorderColor](properties-color-border.md) – The color of a control's border.

[BorderStyle](properties-color-border.md) – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

[BorderThickness](properties-color-border.md) – The thickness of a control's border.

[Color](properties-color-border.md) – The color of text in a control.

[DisplayMode](properties-core.md) – Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**).

[DisabledBorderColor](properties-color-border.md) – The color of a control's border if the control's [DisplayMode](properties-core.md) property is set to **Disabled**.

[DisabledColor](properties-color-border.md) – The color of text in a control if its [DisplayMode](properties-core.md) property is set to **Disabled**.

[DisabledFill](properties-color-border.md) – The background color of a control if its [DisplayMode](properties-core.md) property is set to **Disabled**.

[Fill](properties-color-border.md) – The background color of a control.

[FocusedBorderColor](properties-color-border.md) – The color of a control's border when the control is focused.

[FocusedBorderThickness](properties-color-border.md) – The thickness of a control's border when the control is focused.

[Height](properties-size-location.md) – The distance between a control's top and bottom edges.

[HoverBorderColor](properties-color-border.md) – The color of a control's border when the user keeps the mouse pointer on that control.

[HoverColor](properties-color-border.md) – The color of the text in a control when the user keeps the mouse pointer on it.

[HoverFill](properties-color-border.md) – The background color of a control when the user keeps the mouse pointer on it.

[Image](properties-visual.md) – The name of the image that appears in an image, audio, or microphone control.

[ImagePosition](properties-visual.md) – The position (**Fill**, **Fit**, **Stretch**, **Tile**, or **Center**) of an image in a screen or a control if it isn't the same size as the image.

[OnSelect](properties-core.md) – How the app responds when the user selects a control.

**OnStart** – How the app responds when the user starts to record with a microphone control.

[PressedBorderColor](properties-color-border.md) – The color of a control's border when the user selects that control.

[PressedColor](properties-color-border.md) – The color of text in a control when the user selects that control.

[PressedFill](properties-color-border.md) – The background color of a control when the user selects that control.

[Reset](properties-core.md) – Whether a control reverts to its default value.

[TabIndex](properties-accessibility.md) – Keyboard navigation order compared to other controls.

[Tooltip](properties-core.md) – Explanatory text that appears when the user hovers over a control.

[Visible](properties-core.md) – Whether a control appears or is hidden.

[Width](properties-size-location.md) – The distance between a control's left and right edges.

[X](properties-size-location.md) – The distance between the left edge of a control and the left edge of its parent container or screen.

[Y](properties-size-location.md) – The distance between the top edge of a control and the top edge of the parent container or screen.

## Related functions

[*Patch( DataSource, BaseRecord, ChangeRecord*)](../functions/function-patch.md)

## Example

### Simple direct playback

In this example, we'll directly connect a **Microphone** control with an **Audio** control for immediate playback:

1. [Add](../add-configure-controls.md) a **Microphone** control to your app.
1. Add an **Audio** control to your app.
1. Set the **Audio** control's **Media** property to the formula:

    ```
    Microphone1.Audio
    ```

1. Preview the app.
1. Select the **Microphone** control to begin recording.
1. Speak to record audio.
1. Select the **Microphone** control again to end the recording.
1. Select the **Audio** control to hear the recording.  

### Add sounds to a Gallery control

In this example, we'll create a gallery of audio clips stored in a collection that can be individually selected for playback:

1. [Add](../add-configure-controls.md) a **Microphone** control.

1. Set its **OnStop** property to this formula using the [Collect](../functions/function-clear-collect-clearcollect.md) function:

    ```
    Collect( MySounds, MyMic.Audio )
    ```

1. Add a **Gallery** control, move it below **MyMic**.

1. Set the [Items](properties-core.md) property for the gallery to this formula:

    ```
    MySounds
    ```

1. In the template for the **Custom gallery** control, add an [Audio](control-audio-video.md) control.

1. Set the audio control's **Media** property to this formula:

    ```
    ThisItem.Url
    ```

1. Press F5 to preview the app.

1. Select **MyMic** to start recording, and then select it again to stop recording.

1. In the **Gallery** control, select the play button in the **Audio** control to play back your recording.

1. Add as many recordings as you want, and then return to the default workspace by pressing the Esc key.

1. (optional) In the template for the **Gallery** control, add a [Button](control-button.md) control.

1. Set its [OnSelect](properties-core.md) property to the formula:

    ```
    Remove( MySounds, ThisItem )
    ```

1. Press F5, and then remove a recording by selecting the corresponding **Button** control.

Use the [SaveData](../functions/function-savedata-loaddata.md) function to save the recordings locally or the [Patch](../functions/function-patch.md) function to update a data source.

## Accessibility guidelines

The same guidelines for [Button](control-button.md)  apply because **Microphone** is just a specialized button. Also, consider:

### Audio alternatives

Consider adding an alternative form of input for users with speech disabilities or without a microphone. For example, [Text input](control-text-input.md) to allow users to enter text.

### Color contrast

- Read the [standard color contrast requirements](../accessible-apps-color.md)
- Ensure adequate color contrast between [Image](properties-visual.md) and the button text and icon (if applicable).

### Screen reader support

- [AccessibleLabel](properties-accessibility.md) must be present.
