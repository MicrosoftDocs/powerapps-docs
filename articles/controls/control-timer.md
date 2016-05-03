<properties
    pageTitle="Timer control: reference | Microsoft PowerApps"
    description="Information, including properties and examples, about the timer control"
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
   ms.date="03/09/2016"
   ms.author="anneta"/>

# Timer control in PowerApps #
[AZURE.INCLUDE [control-summary-timer](../../includes/control-summary-timer.md)]

## Description ##
Timers can, for example, determine how long a control appears or change other properties of a control after a certain amount of time has passed.

## Key properties ##

**Duration** – How long a timer runs.

**OnTimerEnd** – How an app responds when a timer finishes running.

**Repeat** – Whether a timer automatically restarts when it finishes running.

## Additional properties ##

**[Align](../properties/properties-text.md)** – The location of text in relation to the horizontal center of its control.

**AutoPause** – Whether an audio or video clip automatically pauses if the user navigates to a different screen.

**AutoStart** – Whether an audio or video control automatically starts to play a clip when the user navigates to the screen that contains that control.

**[BorderColor](../properties/properties-color-border.md)** – The color of a control's border.

**[BorderStyle](../properties/properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](../properties/properties-color-border.md)** – The thickness of a control's border.

**[Color](../properties/properties-color-border.md)** – The color of text in a control.

**[Disabled](../properties/properties-core.md)** – Whether the user can interact with the control.

**[DisabledBorderColor](../properties/properties-color-border.md)** – The color of a control's border if the control's **Disabled** property is set to **true**.

**[DisabledColor](../properties/properties-color-border.md)** – The color of text in a control if its **Disabled** property is set to **true**.

**[DisabledFill](../properties/properties-color-border.md)** – The background color of a control if its **Disabled** property is set to **true**.

**[Fill](../properties/properties-color-border.md)** – The background color of a control.

**[Font](../properties/properties-text.md)** – The name of the family of fonts in which text appears.

**[FontWeight](../properties/properties-text.md)** – The weight of the text in a control: **Bold**, **Semibold**, **Normal**, or **Lighter**.

**[Height](../properties/properties-size-location.md)** – The distance between a control's top and bottom edges.

**[HoverBorderColor](../properties/properties-color-border.md)** – The color of a control's border when the user keeps the mouse pointer on that control.

**[HoverColor](../properties/properties-color-border.md)** – The color of the text in a control when the user keeps the mouse pointer on it.

**[HoverFill](../properties/properties-color-border.md)** – The background color of a control when the user keeps the mouse pointer on it.

**[Italic](../properties/properties-text.md)** – Whether the text in a control is italic.

**[OnSelect](../properties/properties-core.md)** – How the app responds when the user taps or clicks a control.

**OnTimerStart** – How an app responds when a timer starts to run.

**[PressedBorderColor](../properties/properties-color-border.md)** – The color of a control's border when the user taps or clicks that control.

**[PressedColor](../properties/properties-color-border.md)** – The color of text in a control when the user taps or clicks that control.

**[PressedFill](../properties/properties-color-border.md)** – The background color of a control when the user taps or clicks that control.

**[Reset](../properties/properties-core.md)** – Whether a control reverts to its default value.

**[Size](../properties/properties-text.md)** – The font size of the text that appears on a control.

**Start** – Whether an audio or video clip plays.

**[Strikethrough](../properties/properties-text.md)** – Whether a line appears through the text that appears on a control.

**[Text](../properties/properties-core.md)** – Text that appears on a control or that the user types into a control.

**[Tooltip](../properties/properties-core.md)** – Explanatory text that appears when the user hovers over a control.

**[Underline](../properties/properties-text.md)** – Whether a line appears under the text that appears on a control.

**[Visible](../properties/properties-core.md)** – Whether a control appears or is hidden.

**[Width](../properties/properties-size-location.md)** – The distance between a control's left and right edges.

**[X](../properties/properties-size-location.md)** – The distance between the left edge of a control and the left edge of the screen.

**[Y](../properties/properties-size-location.md)** – The distance between the top edge of a control and the top edge of the screen.

## Related functions ##

[**Refresh**( *DataSource* )](function-refresh.md)

## Examples ##
### Show a countdown ###
1. Add a timer, and name it **Countdown**.

	Don't know how to [add, name, and configure a control](add-configure-controls.md)?

1. Set the timer's **Duration** property to **10000** and its **Repeat** and **Autostart** properties to **true**.

1. (optional) Make the timer easier to read by setting its **Height** property to **160**, its **Width** property to **600**, and its **Size** property to **60**.

1. Add a text box, and set its **Text** property to this formula:
<br>**"Number of seconds remaining: " & RoundUp(10-Countdown.Value/1000, 0)**

	Want more information about the [**RoundUp** function](function-round.md) or [other functions](formula-reference.md)?

	The text box shows how many seconds remain before the timer restarts.

1. (optional) Set the timer's **Visible** property to **false**.

### Animate a control ###
1. Add a timer, and name it **FadeIn**.

	Don't know how to [add, name, and configure a control](add-configure-controls.md)?

1. Set the timer's **Duration** property to **5000** and its **Repeat** and **Autostart** properties to **true**.

1. (optional) Make the timer easier to read by setting its **Height** property to **160**, its **Width** property to **600**, and its **Size** property to **60**.

1. Add a text box, set its **Text** property to show **Welcome!** and set its **Color** property to this formula:
<br>**ColorFade(Color.BlueViolet, FadeIn.Value/5000)**

	Want more information about the [**ColorFade** function](function-colors.md) or [other functions](formula-reference.md)?

	The text in the text box fades to white, returns to full intensity, and repeats the process.

1. (optional) Set the timer's **Visible** property to **false**.
