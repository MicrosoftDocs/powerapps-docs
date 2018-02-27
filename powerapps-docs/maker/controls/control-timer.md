---
title: 'Timer control: reference | Microsoft Docs'
description: Information, including properties and examples, about the timer control
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
# Timer control in PowerApps
A control that can determine how your app responds after a certain amount of time passes.

## Description
Timers can, for example, determine how long a control appears or change other properties of a control after a certain amount of time has passed.

Note that you need to preview the app in order for Timer to run in the designer.  This allows user to configure the timer in the designer without any time restrictions.

## Key properties
**Duration** – How long a timer runs in milliseconds.  There is no maximum value.

**OnTimerEnd** – How an app responds when a timer finishes running.

**Repeat** – Whether a timer automatically restarts when it finishes running.

## Additional properties
**[Align](properties-text.md)** – The location of text in relation to the horizontal center of its control.

**AutoPause** – Whether an audio or video clip automatically pauses if the user navigates to a different screen.

**AutoStart** – Whether an audio or video control automatically starts to play a clip when the user navigates to the screen that contains that control.

**[BorderColor](properties-color-border.md)** – The color of a control's border.

**[BorderStyle](properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](properties-color-border.md)** – The thickness of a control's border.

**[Color](properties-color-border.md)** – The color of text in a control.

**[DisplayMode](properties-core.md)** – Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**).

**[DisabledBorderColor](properties-color-border.md)** – The color of a control's border if the control's **[DisplayMode](properties-core.md)** property is set to **Disabled**.

**[DisabledColor](properties-color-border.md)** – The color of text in a control if its **[DisplayMode](properties-core.md)** property is set to **Disabled**.

**[DisabledFill](properties-color-border.md)** – The background color of a control if its **[DisplayMode](properties-core.md)** property is set to **Disabled**.

**[Fill](properties-color-border.md)** – The background color of a control.

**[Font](properties-text.md)** – The name of the family of fonts in which text appears.

**[FontWeight](properties-text.md)** – The weight of the text in a control: **Bold**, **Semibold**, **Normal**, or **Lighter**.

**[Height](properties-size-location.md)** – The distance between a control's top and bottom edges.

**[HoverBorderColor](properties-color-border.md)** – The color of a control's border when the user keeps the mouse pointer on that control.

**[HoverColor](properties-color-border.md)** – The color of the text in a control when the user keeps the mouse pointer on it.

**[HoverFill](properties-color-border.md)** – The background color of a control when the user keeps the mouse pointer on it.

**[Italic](properties-text.md)** – Whether the text in a control is italic.

**[OnSelect](properties-core.md)** – How the app responds when the user taps or clicks a control.

**OnTimerStart** – How an app responds when a timer starts to run.

**[PressedBorderColor](properties-color-border.md)** – The color of a control's border when the user taps or clicks that control.

**[PressedColor](properties-color-border.md)** – The color of text in a control when the user taps or clicks that control.

**[PressedFill](properties-color-border.md)** – The background color of a control when the user taps or clicks that control.

**[Reset](properties-core.md)** – Whether a control reverts to its default value.

**[Size](properties-text.md)** – The font size of the text that appears on a control.

**Start** – Whether an audio or video clip plays.

**[Strikethrough](properties-text.md)** – Whether a line appears through the text that appears on a control.

**[Text](properties-core.md)** – Text that appears on a control or that the user types into a control.

**[Tooltip](properties-core.md)** – Explanatory text that appears when the user hovers over a control.

**[Underline](properties-text.md)** – Whether a line appears under the text that appears on a control.

**[Visible](properties-core.md)** – Whether a control appears or is hidden.

**[Width](properties-size-location.md)** – The distance between a control's left and right edges.

**[X](properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

## Related functions
[**Refresh**( *DataSource* )](../functions/function-refresh.md)

## Examples
### Show a countdown
1. Add a timer, and name it **Countdown**.

    Don't know how to [add, name, and configure a control](../add-configure-controls.md)?
2. Set the timer's **Duration** property to **10000** and its **Repeat** and **Autostart** properties to **true**.
3. (optional) Make the timer easier to read by setting its **[Height](properties-size-location.md)** property to **160**, its **[Width](properties-size-location.md)** property to **600**, and its **[Size](properties-text.md)** property to **60**.
4. Add a label, and set its **[Text](properties-core.md)** property to this formula:
   <br>**"Number of seconds remaining: " & RoundUp(10-Countdown.Value/1000, 0)**

    Want more information about the **[RoundUp](../../functions/function-round.md)** function or [other functions](../formula-reference.md)?

    The label shows how many seconds remain before the timer restarts.
5. (optional) Set the timer's **[Visible](properties-core.md)** property to **false**.

### Animate a control
1. Add a timer, and name it **FadeIn**.

    Don't know how to [add, name, and configure a control](../add-configure-controls.md)?
2. Set the timer's **Duration** property to **5000** and its **Repeat** and **Autostart** properties to **true**.
3. (optional) Make the timer easier to read by setting its **[Height](properties-size-location.md)** property to **160**, its **[Width](properties-size-location.md)** property to **600**, and its **[Size](properties-text.md)** property to **60**.
4. Add a label, set its **[Text](properties-core.md)** property to show **Welcome!** and set its **[Color](properties-color-border.md)** property to this formula:
   <br>**ColorFade(Color.BlueViolet, FadeIn.Value/5000)**

    Want more information about the **[ColorFade](../functions/function-colors.md)** function or [other functions](../formula-reference.md)?

    The text in the label fades to white, returns to full intensity, and repeats the process.
5. (optional) Set the timer's **[Visible](properties-core.md)** property to **false**.
