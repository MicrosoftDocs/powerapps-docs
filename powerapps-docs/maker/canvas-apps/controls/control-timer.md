---
title: Timer control in Power Apps
description: Learn about the details, properties and examples of the Timer control in Power Apps.
author: chmoncay
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 10/25/2016
ms.subservice: canvas-maker
ms.author: chmoncay
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - tapanm-msft
  - chmoncay
---
# Timer control in Power Apps
A control that can determine how your app responds after a certain amount of time passes.

## Description
Timers can, for example, determine how long a control appears or change other properties of a control after a certain amount of time has passed.

> [!NOTE]
> In Power Apps Studio, timers run only in Preview mode.


## Key properties
**Duration** – How long a timer runs in milliseconds. The maximum is 24 hours expressed in milliseconds. Default is 60 seconds.

**OnTimerEnd** – Actions to perform when a timer finishes running.

**Repeat** – Whether a timer automatically restarts when it finishes running.

## Additional properties
**[Align](properties-text.md)** – The location of text in relation to the horizontal center of its control.

**AutoPause** – Whether the timer control automatically pauses if the user navigates to a different screen.

**AutoStart** – Whether the timer control automatically starts to play when the user navigates to the screen that contains that control.

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

**[Font](properties-text.md)** – The name of the family of fonts in which text appears.

**[FontWeight](properties-text.md)** – The weight of the text in a control: **Bold**, **Semibold**, **Normal**, or **Lighter**.

**[Height](properties-size-location.md)** – The distance between a control's top and bottom edges.

**[HoverBorderColor](properties-color-border.md)** – The color of a control's border when the user keeps the mouse pointer on that control.

**[HoverColor](properties-color-border.md)** – The color of the text in a control when the user keeps the mouse pointer on it.

**[HoverFill](properties-color-border.md)** – The background color of a control when the user keeps the mouse pointer on it.

**[Italic](properties-text.md)** – Whether the text in a control is italic.

**[OnSelect](properties-core.md)** – Actions to perform when the user taps or clicks a control.

**OnTimerStart** – Actions to perform when a timer starts to run.

**[PressedBorderColor](properties-color-border.md)** – The color of a control's border when the user taps or clicks that control.

**[PressedColor](properties-color-border.md)** – The color of text in a control when the user taps or clicks that control.

**[PressedFill](properties-color-border.md)** – The background color of a control when the user taps or clicks that control.

**[Reset](properties-core.md)** – Whether a control reverts to its default value.

**[Size](properties-text.md)** – The font size of the text that appears on a control.

**Start** – Whether the timer starts.

**[Strikethrough](properties-text.md)** – Whether a line appears through the text that appears on a control.

**[TabIndex](properties-accessibility.md)** – Keyboard navigation order in relation to other controls.

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

    Want more information about the **[RoundUp](../functions/function-round.md)** function or [other functions](../formula-reference.md)?

    The label shows how many seconds remain before the timer restarts.

### Animate a control
1. Add a timer, and name it **FadeIn**.

    Don't know how to [add, name, and configure a control](../add-configure-controls.md)?
2. Set the timer's **Duration** property to **5000**, its **Repeat** property to **true**, and its **[Text](properties-core.md)** property to **Toggle animation**.
3. (optional) Make the timer easier to read by setting its **[Height](properties-size-location.md)** property to **160**, its **[Width](properties-size-location.md)** property to **600**, and its **[Size](properties-text.md)** property to **60**.
4. Add a label, set its **[Text](properties-core.md)** property to show **Welcome!** and set its **[Color](properties-color-border.md)** property to this formula:
   <br>**ColorFade(Color.BlueViolet, FadeIn.Value/5000)**

    Want more information about the **[ColorFade](../functions/function-colors.md)** function or [other functions](../formula-reference.md)?

5. Select the timer button to start or stop the animation. The text in the label fades to white, returns to full intensity, and repeats the process.

## Accessibility guidelines
The same guidelines for the **[Button](control-button.md)** control apply to the **Timer** control if users can interact with it.

### Background timers
Background timers run automatically and are hidden. Use them in a supporting role where the elapsed time is of little interest to the user. For example, you can refresh data every minute or show a notification message only for a certain amount of time.

Background timers should have their **[Visible](properties-core.md)** property set to false so that they are hidden from all users.

### Timing considerations
If a **Timer** runs automatically, consider whether users have enough time to read and use content. Keyboard and screen-reader users may need more time to react to a timed event.

Any of these strategies is sufficient:
* Allow users to cancel the timed event.
* Allow users to adjust the time limit before it begins.
* Warn 20 seconds before the time limit expires and provide an easy way to extend the limit.

Some scenarios are exempt from these requirements. Learn more in the [WCAG 2.0 guideline for time limits](https://www.w3.org/TR/WCAG20/#time-limits).

### Screen reader support
* If a timer triggers changes on the current screen, use a [live region](../accessible-apps-live-regions.md) to tell screen-reader users what changed.

    > [!NOTE]
    > If the timer is visible and running, screen readers will announce the elapsed time every five seconds.

* Don't use the **[Text](properties-core.md)** property of a control for time-sensitive and important information. Screen readers won't announce changes to **[Text](properties-core.md)**.
* For interactive timers:
    * **[Text](properties-core.md)** must be present.
    * Consider adding a **[Label](control-text-box.md)** control to show the elapsed time. Use the timer's **[Text](properties-core.md)** property to instruct the user to start or stop the timer.


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]