---
title: Audio and Video controls in Power Apps
description: Learn about the details, properties and examples of the audio and video controls in Power Apps.
author: chmoncay
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.date: 10/25/2016
ms.subservice: canvas-maker
ms.author: chmoncay
ms.reviewer: tapanm
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Audio and Video controls in Power Apps
A control that plays an audio file, a video file, or a video on YouTube.

## Description
An **Audio** control plays a sound clip from a file, a recording from a **[Microphone](control-microphone.md)** control, or the audio track from a video file.

A **Video** control plays a video clip from a file or from YouTube or Azure Media Services.  Closed captions can optionally be shown when specified.

## Key properties
**Loop** – Whether an audio or video clip automatically starts over as soon as it finishes playing.

**Media** – An identifier for the clip that an audio or video control plays.

**ShowControls** – Whether an audio or video player shows, for example, a play button and a volume slider, and a pen control shows, for example, icons for drawing, erasing, and clearing.

## Additional properties
**[AccessibleLabel](properties-accessibility.md)** – Label for screen readers. Should be the title of the video or audio clip.

**AutoPause** – Whether an audio or video clip automatically pauses if the user navigates to a different screen.

**AutoStart** – Whether an audio or video control automatically starts to play a clip when the user navigates to the screen that contains that control.

**[BorderColor](properties-color-border.md)** – The color of a control's border.

**[BorderStyle](properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](properties-color-border.md)** – The thickness of a control's border.

**ClosedCaptionsUrl** – Video control only.  URL of closed captions file in WebVTT format.  Both video and captions URLs must be HTTPS. Server hosting both video and captions file needs to be CORS enabled.

**[DisplayMode](properties-core.md)** – Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**).

**[Fill](properties-color-border.md)** – The background color of a control.

**[FocusedBorderColor](properties-color-border.md)** – The color of a control's border when the control is focused.

**[FocusedBorderThickness](properties-color-border.md)** – The thickness of a control's border when the control is focused.

**[Height](properties-size-location.md)** – The distance between a control's top and bottom edges.

**[Image](properties-visual.md)** – The name of the image that appears in an image, audio, or microphone control.

**[ImagePosition](properties-visual.md)** – The position (**Fill**, **Fit**, **Stretch**, **Tile**, or **Center**) of an image in a screen or a control if it isn't the same size as the image.

**OnEnd** – Actions to perform when an audio or video clip finishes playing.

**OnPause** – Actions to perform when the user pauses the clip that an audio or video control is playing.

**OnStart** – Actions to perform when the user starts to record with a microphone control.

**Paused** – *True* if a media playback control is currently paused, *false* otherwise.

**[Reset](properties-core.md)** – Whether a control reverts to its default value.

**Start** – Whether an audio or video clip plays.

**StartTime** – The time after the start of an audio or video clip when the clip starts to play.

**Time** – A media control's current position.

**[TabIndex](properties-accessibility.md)** – Keyboard navigation order in relation to other controls.

**[Tooltip](properties-core.md)** – Explanatory text that appears when the user hovers over a control.

**[Visible](properties-core.md)** – Whether a control appears or is hidden.

**[Width](properties-size-location.md)** – The distance between a control's left and right edges.

**[X](properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

## Related functions
[**First**( *TableName* )](../functions/function-first-last.md)

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
1. Add a **Video** control, and set its **Media** property to the URL of the YouTube video, enclosed in double quotation marks.
2. Press F5, and then play the clip by clicking or tapping the play button of the **Video** control.
3. Press Esc to return to the default workspace.

### Play a video from Azure Media Services
1. After the videos are published on AMS, copy the manifest URL. Start the streaming endpoint of your service, if not already.
1. Add a **Video** control, and set its **Media** property to the URL of the AMS video, enclosed in double quotation marks.
2. Press F5, and then play the clip by clicking or tapping the play button of the **Video** control.
3. Press Esc to return to the default workspace.


## Accessibility guidelines
### Audio and video alternatives
* **ShowControls** must be true so that users can listen or watch multimedia at their own pace. This also allows users to toggle closed captions and full-screen mode on video players.
* Closed captions must be provided for videos.
  *  For YouTube videos, use authoring tools provided by YouTube to add captions.
  *  For other videos, create captions in WebVTT format, upload them, and set **ClosedCaptionsUrl** to the url location. There are several limitations. Server(s) hosting video and captions needs to be CORS-enabled and serve them using HTTPS protocol. Captioning does not work on Internet Explorer.
* Consider providing an audio or video transcript using one of these methods:
  1. Put the text in a **[Label](control-text-box.md)** and position it adjacent to the multimedia player. Optionally, create a **[Button](control-button.md)** to toggle the display of the text.
  2. Put the text in a different screen. Create a **[Button](control-button.md)** that navigates to the screen and position the button adjacent to the multimedia player.
  3. If the description is short, it can be put it in the **[AccessibleLabel](properties-accessibility.md)**.

### Color contrast
There must be adequate color contrast between:
* **[FocusedBorderColor](properties-color-border.md)** and the outside color
* **[Image](properties-visual.md)** and the multimedia player controls (if applicable)
* **[Fill](properties-color-border.md)** and the multimedia player controls (if the fill is visible)

Provide closed captions and/or transcript if the video content has color contrast issues.

### Screen reader support
* **[AccessibleLabel](properties-accessibility.md)** must be present.

### Keyboard support
* **[TabIndex](properties-accessibility.md)** must be zero or greater so that keyboard users can navigate to it.
* Focus indicators must be clearly visible. Use **[FocusedBorderColor](properties-color-border.md)** and **[FocusedBorderThickness](properties-color-border.md)** to achieve this.
* **AutoStart** should be false because it can be difficult for keyboard users to stop playback quickly.


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]