<properties
    pageTitle="Microphone control: reference | Microsoft PowerApps"
    description="Information, including properties and examples, about the microphone control"
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
   ms.date="03/10/2016"
   ms.author="anneta"/>

# Microphone control in PowerApps #
[AZURE.INCLUDE [control-summary-microphone](../../includes/control-summary-microphone.md)]

## Description ##
If you add this control, the user can update a data source with one or more sounds from wherever the app is running.

## Key properties ##

[AZURE.INCLUDE [short-mic](../../includes/short-mic.md)]

[AZURE.INCLUDE [short-onstop](../../includes/short-onstop.md)]

## All properties ##

[AZURE.INCLUDE [short-bordercolor](../../includes/short-bordercolor.md)]

[AZURE.INCLUDE [short-borderstyle](../../includes/short-borderstyle.md)]

[AZURE.INCLUDE [short-borderthickness](../../includes/short-borderthickness.md)]

[AZURE.INCLUDE [short-color](../../includes/short-color.md)]

[AZURE.INCLUDE [short-disabled](../../includes/short-disabled.md)]

[AZURE.INCLUDE [short-disabledbordercolor](../../includes/short-disabledbordercolor.md)]

[AZURE.INCLUDE [short-disabledcolor](../../includes/short-disabledcolor.md)]

[AZURE.INCLUDE [short-disabledfill](../../includes/short-disabledfill.md)]

[AZURE.INCLUDE [short-fill](../../includes/short-fill.md)]

[AZURE.INCLUDE [short-height](../../includes/short-height.md)]

[AZURE.INCLUDE [short-hoverbordercolor](../../includes/short-hoverbordercolor.md)]

[AZURE.INCLUDE [short-hovercolor](../../includes/short-hovercolor.md)]

[AZURE.INCLUDE [short-hoverfill](../../includes/short-hoverfill.md)]

[AZURE.INCLUDE [short-image](../../includes/short-image.md)]

[AZURE.INCLUDE [short-imageposition](../../includes/short-imageposition.md)]

[AZURE.INCLUDE [short-mic](../../includes/short-mic.md)]

[AZURE.INCLUDE [short-onselect](../../includes/short-onselect.md)]

[AZURE.INCLUDE [short-onstart](../../includes/short-onstart.md)]

[AZURE.INCLUDE [short-onstop](../../includes/short-onstop.md)]

[AZURE.INCLUDE [short-pressedbordercolor](../../includes/short-pressedbordercolor.md)]

[AZURE.INCLUDE [short-pressedcolor](../../includes/short-pressedcolor.md)]

[AZURE.INCLUDE [short-pressedfill](../../includes/short-pressedfill.md)]

[AZURE.INCLUDE [short-reset](../../includes/short-reset.md)]

[AZURE.INCLUDE [short-tooltip](../../includes/short-tooltip.md)]

[AZURE.INCLUDE [short-visible](../../includes/short-visible.md)]

[AZURE.INCLUDE [short-width](../../includes/short-width.md)]

[AZURE.INCLUDE [short-x](../../includes/short-x.md)]

[AZURE.INCLUDE [short-y](../../includes/short-y.md)]

## Related functions ##

[**Patch**( *DataSource*, *BaseRecord*, *ChangeRecord* )](function-patch.md)

## Example ##
### Add sounds to a gallery ###
1. Add a microphone, name it **MyMic**, and set its **OnStop** property to this formula:<br>
**Collect(MySounds, MyMic.Audio)**

	Don't know how to [add, name, and configure a control](add-configure-controls.md)?

	Want more information about the [**Collect** function](function-clear-collect-clearcollect.md) or [other functions](formula-reference.md)?.

1. Add a custom gallery, move it below **MyMic**, and set the gallery's **Items** property to **MySounds**.

1. In the gallery template, add an audio control, and set its **Media** property to **ThisItem.Url**.

1. Press F5, select **MyMic** to start recording, and then select it again to stop recording.

1. In the gallery, select the play button in the audio control to play back your recording.

1. Add as many recordings as you want, and then return to the default workspace by pressing Esc.

1. (optional) In the gallery template, add a button, set its **OnSelect** property to **Remove(MySounds, ThisItem)**, press F5, and then remove a recording by selecting its button.

Use the [**SaveData** function](function-savedata-loaddata.md) to save the data set locally or the [**Patch** function](function-patch.md) to update a data source.
