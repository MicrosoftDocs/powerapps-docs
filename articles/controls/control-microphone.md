<properties
    pageTitle="Microphone control: reference | Microsoft PowerApps"
    description="Information, including properties and examples, about the Microphone control"
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

**Mic** – On a device that has more than one microphone, the numeric ID of the microphone that the app uses.

**OnStop** – How the app responds when the user stops recording with a microphone control.

## Additional properties ##

**[BorderColor](../properties/properties-color-border.md)** – The color of a control's border.

**[BorderStyle](../properties/properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](../properties/properties-color-border.md)** – The thickness of a control's border.

**[Color](../properties/properties-color-border.md)** – The color of text in a control.

**[Disabled](../properties/properties-core.md)** – Whether the user can interact with the control.

**[DisabledBorderColor](../properties/properties-color-border.md)** – The color of a control's border if the control's **Disabled** property is set to **true**.

**[DisabledColor](../properties/properties-color-border.md)** – The color of text in a control if its **Disabled** property is set to **true**.

**[DisabledFill](../properties/properties-color-border.md)** – The background color of a control if its **Disabled** property is set to **true**.

**[Fill](../properties/properties-color-border.md)** – The background color of a control.

**[Height](../properties/properties-size-location.md)** – The distance between a control's top and bottom edges.

**[HoverBorderColor](../properties/properties-color-border.md)** – The color of a control's border when the user keeps the mouse pointer on that control.

**[HoverColor](../properties/properties-color-border.md)** – The color of the text in a control when the user keeps the mouse pointer on it.

**[HoverFill](../properties/properties-color-border.md)** – The background color of a control when the user keeps the mouse pointer on it.

**[Image](../properties/properties-visual.md)** – The name of the image that appears in an image, audio, or microphone control.

**[ImagePosition](../properties/properties-visual.md)** – The position (**Fill**, **Fit**, **Stretch**, **Tile**, or **Center**) of an image in a screen or a control if it isn't the same size as the image.

**[OnSelect](../properties/properties-core.md)** – How the app responds when the user taps or clicks a control.

**OnStart** – How the app responds when the user starts to record with a microphone control.

**[PressedBorderColor](../properties/properties-color-border.md)** – The color of a control's border when the user taps or clicks that control.

**[PressedColor](../properties/properties-color-border.md)** – The color of text in a control when the user taps or clicks that control.

**[PressedFill](../properties/properties-color-border.md)** – The background color of a control when the user taps or clicks that control.

**[Reset](../properties/properties-core.md)** – Whether a control reverts to its default value.

**[Tooltip](../properties/properties-core.md)** – Explanatory text that appears when the user hovers over a control.

**[Visible](../properties/properties-core.md)** – Whether a control appears or is hidden.

**[Width](../properties/properties-size-location.md)** – The distance between a control's left and right edges.

**[X](../properties/properties-size-location.md)** – The distance between the left edge of a control and the left edge of the screen.

**[Y](../properties/properties-size-location.md)** – The distance between the top edge of a control and the top edge of the screen.

## Related functions ##

[**Patch**( *DataSource*, *BaseRecord*, *ChangeRecord* )](function-patch.md)

## Example ##
### Add sounds to a Custom gallery control ###
1. Add a **Microphone**, name it **MyMic**, and set its **OnStop** property to this formula:<br>
**Collect(MySounds, MyMic.Audio)**

	Don't know how to [add, name, and configure a control](add-configure-controls.md)?

	Want more information about the [**Collect** function](function-clear-collect-clearcollect.md) or [other functions](formula-reference.md)?

1. Add a **Custom gallery** control, move it below **MyMic**, and set the **Items** property for the **Custom gallery** control to **MySounds**.

1. In the template for the **Custom gallery** control, add an **Audio** control, and set its **Media** property to **ThisItem.Url**.

1. Press F5, click or tap **MyMic** to start recording, and then click or tap it again to stop recording.

1. In the **Custom gallery** control, click or tap the play button in the **Audio** control to play back your recording.

1. Add as many recordings as you want, and then return to the default workspace by pressing Esc.

1. (optional) In the template for the **Custom gallery** control, add a **Button** control, set its **OnSelect** property to **Remove(MySounds, ThisItem)**, press F5, and then remove a recording by clicking or tapping the corresponding **Button** control.

Use the [**SaveData** function](function-savedata-loaddata.md) to save the recordings locally or the [**Patch** function](function-patch.md) to update a data source.
