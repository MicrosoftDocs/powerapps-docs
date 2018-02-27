---
title: 'Audio and Video controls: reference | Microsoft Docs'
description: Information, including properties and examples, about the Audio and Video controls
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
# Audio and Video controls in PowerApps
A control that plays an audio file, a video file, or a video on YouTube.

## Description
An **Audio** control plays a sound clip from a file, a recording from a **[Microphone](control-microphone.md)** control, or the audio track from a video file. A **Video** control plays a video clip from a file or from YouTube if you specify a URL with optional closed captions.

## Key properties
**Loop** – Whether an audio or video clip automatically starts over as soon as it finishes playing.

**Media** – An identifier for the clip that an audio or video control plays.

**ShowControls** – Whether an audio or video player shows, for example, a play button and a volume slider, and a pen control shows, for example, icons for drawing, erasing, and clearing.

## Additional properties
**AutoPause** – Whether an audio or video clip automatically pauses if the user navigates to a different screen.

**AutoStart** – Whether an audio or video control automatically starts to play a clip when the user navigates to the screen that contains that control.

**[BorderColor](properties-color-border.md)** – The color of a control's border.

**[BorderStyle](properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](properties-color-border.md)** – The thickness of a control's border.

**ClosedCaptionsUrl** – Video control only.  URL of closed captions file in WebVTT format.  Both video and captions URLs must be HTTPS. Server hosting both video and captions file needs to be CORS enabled.

**[DisplayMode](properties-core.md)** – Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**).

**[Fill](properties-color-border.md)** – The background color of a control.

**[Height](properties-size-location.md)** – The distance between a control's top and bottom edges.

**[Image](../../controls/properties-visual.md)** – The name of the image that appears in an image, audio, or microphone control.

**[ImagePosition](../../controls/properties-visual.md)** – The position (**Fill**, **Fit**, **Stretch**, **Tile**, or **Center**) of an image in a screen or a control if it isn't the same size as the image.

**OnEnd** – How an app responds when an audio or video clip finishes playing.

**OnPause** – How an app responds when the user pauses the clip that an audio or video control is playing.

**OnStart** – How the app responds when the user starts to record with a microphone control.

**Paused** – *True* if a media playback control is currently paused, *false* otherwise.

**[Reset](properties-core.md)** – Whether a control reverts to its default value.

**Start** – Whether an audio or video clip plays.

**StartTime** – The time after the start of an audio or video clip when the clip starts to play.

**Time** – A media control's current position.

**[Tooltip](properties-core.md)** – Explanatory text that appears when the user hovers over a control.

**[Visible](properties-core.md)** – Whether a control appears or is hidden.

**[Width](properties-size-location.md)** – The distance between a control's left and right edges.

**[X](properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

## Related functions
[**First**( *TableName* )](../../functions/function-first-last.md)

## Examples
### Play an audio or video file
1. On the **File** menu, click or tap **Media**, click or tap **Videos** or **Audio**, and then click or tap **Browse**.
2. Browse to the file you want to use, click or tap it, and then click or tap **Open**.
3. Press Esc to return to the default workspace, add an **Audio** or **Video** control, and set its **Media** property to the file that you added.

    Don't know how to [add and configure a control](../add-configure-controls.md)?
4. Press F5, and then play the clip by clicking or tapping the play button of the control that you added.

    > [!TIP]
> The play button of the **Video** control appears when you hover over the control.
5. Press Esc to return to the default workspace.

### Play a YouTube video
1. Add a **Video** control, and set its **Media** property to the URL, enclosed in double quotation marks, of a YouTube video.
2. Press F5, and then play the clip by clicking or tapping the play button of the **Video** control.
3. Press Esc to return to the default workspace.
