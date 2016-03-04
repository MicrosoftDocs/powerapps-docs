<properties
    pageTitle="Audio and video: reference | Microsoft PowerApps"
    description="Information, including properties and examples, about the audio and video controls"
    services=""
    suite="powerapps"
    documentationCenter="na"
    authors="aftowen"
    manager="erikre"
    editor=""
    tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="02/29/2016"
   ms.author="anneta"/>

# Audio and video controls in PowerApps #
[AZURE.INCLUDE [control-text-box](../../includes/control-text-box.md)]

## Description ##
An audio control plays a sound clip from a file or a microphone control or the audio track from a video file. A video control plays a video clip from a file or from YouTube if you specify a URL.

## Key properties ##

[AZURE.INCLUDE [long-media](../../includes/long-media.md)]

[AZURE.INCLUDE [long-showcontrols](../../includes/long-showcontrols.md)]

[AZURE.INCLUDE [long-loop](../../includes/long-loop.md)]

## All properties ##

[AZURE.INCLUDE [short-autopause](../../includes/short-autopause.md)]

[AZURE.INCLUDE [short-autostart](../../includes/short-autostart.md)]

[AZURE.INCLUDE [short-bordercolor](../../includes/short-bordercolor.md)]

[AZURE.INCLUDE [short-borderstyle](../../includes/short-borderstyle.md)]

[AZURE.INCLUDE [short-borderthickness](../../includes/short-borderthickness.md)]

[AZURE.INCLUDE [short-disabled](../../includes/short-disabled.md)]

[AZURE.INCLUDE [short-fill](../../includes/short-fill.md)]

[AZURE.INCLUDE [short-height](../../includes/short-height.md)]

[AZURE.INCLUDE [short-image](../../includes/short-image.md)]

[AZURE.INCLUDE [short-imageposition](../../includes/short-imageposition.md)]

**Note:** The **ImagePosition** property is available for the audio control but not the video control.

[AZURE.INCLUDE [short-loop](../../includes/short-loop.md)]

[AZURE.INCLUDE [short-media](../../includes/short-media.md)]

[AZURE.INCLUDE [short-onend](../../includes/short-onend.md)]

[AZURE.INCLUDE [short-onpause](../../includes/short-onpause.md)]

[AZURE.INCLUDE [short-onstart](../../includes/short-onstart.md)]

[AZURE.INCLUDE [short-reset](../../includes/short-reset.md)]

[AZURE.INCLUDE [short-showcontrols](../../includes/short-showcontrols.md)]

[AZURE.INCLUDE [short-start](../../includes/short-start.md)]

[AZURE.INCLUDE [short-starttime](../../includes/short-starttime.md)]

[AZURE.INCLUDE [short-tooltip](../../includes/short-tooltip.md)]

[[AZURE.INCLUDE [short-visible](../../includes/short-visible.md)]

[AZURE.INCLUDE [short-width](../../includes/short-width.md)]

[AZURE.INCLUDE [short-x](../../includes/short-x.md)]

[AZURE.INCLUDE [short-y](../../includes/short-y.md)]

## Related functions ##

[**First**( *TableName*)](function-first-last.md)

## Examples ##
### Play an audio or video file ###
1. On the **File** menu, click or tap **Media**, click or tap **Videos** or **Audio**, and then click or tap **Browse**.

1. Browse to the file you want to use, click or tap it, and then click or tap **Open**.

1. Press Esc to return to the default workspace, add an audio or video control, and set its **Media** property to the file that you added.

	Don't know how to [add and configure a control](add-configure-controls.md)?

1. Press F5, and then play the clip by clicking or tapping the play button of the control that you added.

	**Tip:** The play button of the video control appears when you hover over the control.

1. Press Esc to return to the default workspace.

### Play a YouTube video ###
1. Add a video control, and set its **Media** property to the URL, enclosed in double quotation marks, of a YouTube video.

1. Press F5, and then play the video by clicking or tapping the play button of the video control.

1. Press Esc to return to the default workspace.
