---
title: Radio control in Power Apps
description: Learn about the details, properties and examples of the Radio control in Power Apps.
author: chmoncay
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 07/06/2018
ms.author: chmoncay
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Radio control in Power Apps

An input control that shows multiple options, of which users can select only one at a time.

## Description

A **Radio** control, a standard HTML input control, is best used with only a few, mutually exclusive options.

The control can have a horizontal or vertical layout.

## Key properties

**[Default](properties-core.md)** – The value of a control before the user changes it.

**[Items](properties-core.md)** – The source of data that appears in a control such as a gallery, a list, or a chart.

**Layout** – Whether the options are laid out vertically or horizontally.

**[Value](properties-core.md)** – The value of an input control.

**Selected** – The data record that represents the selected item.

## All properties

**[Align](properties-text.md)** – The location of text in relation to the horizontal center of its control.

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

**[HoverColor](properties-color-border.md)** – The color of the text in a control when the user keeps the mouse pointer on it.

**[HoverFill](properties-color-border.md)** – The background color of a control when the user keeps the mouse pointer on it.

**[Italic](properties-text.md)** – Whether the text in a control is italic.

**[LineHeight](properties-text.md)** – The distance between, for example, lines of text or items in a list.

**[OnChange](properties-core.md)** – How the app responds when the user changes the value of a control (for example, by adjusting a slider).

**[OnSelect](properties-core.md)** – How the app responds when the user taps or clicks a control.

**[PaddingBottom](properties-size-location.md)** – The distance between text in a control and the bottom edge of that control.

**[PaddingLeft](properties-size-location.md)** – The distance between text in a control and the left edge of that control.

**[PaddingRight](properties-size-location.md)** – The distance between text in a control and the right edge of that control.

**[PaddingTop](properties-size-location.md)** – The distance between text in a control and the top edge of that control.

**[PressedColor](properties-color-border.md)** – The color of text in a control when the user taps or clicks that control.

**[PressedFill](properties-color-border.md)** – The background color of a control when the user taps or clicks that control.

**RadioBackgroundFill** – The background color of the circles in a radio-button control.

**RadioBorderColor** – The color of the circle for each option in a radio-button control.

**RadioSelectionFill** – The color that appears inside the circle of the selected option in a radio-button control.

**RadioSize** – The diameter of the circles in a radio-button control.

**[Reset](properties-core.md)** – Whether a control reverts to its default value.

**SelectedText (Deprecated)** – A string value that represents the selected item.

**[Size](properties-text.md)** – The font size of the text that appears on a control.

**[Strikethrough](properties-text.md)** – Whether a line appears through the text that appears on a control.

**[TabIndex](properties-accessibility.md)** – Keyboard-navigation order in relation to other controls.

**[Tooltip](properties-core.md)** – Explanatory text that appears when the user hovers over a control.

**[Underline](properties-text.md)** – Whether a line appears under the text that appears on a control.

**[Visible](properties-core.md)** – Whether a control appears or is hidden.

**[Width](properties-size-location.md)** – The distance between a control's left and right edges.

**[X](properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

## Related functions

[**Distinct**( *DataSource*, *ColumnName* )](../functions/function-distinct.md)

## Example

1. Add a **Radio** control, name it **Pricing**, and set its **[Items](properties-core.md)** property to this formula:

    **["Standard", "Premium"]**

    Don't know how to [add, name, and configure a control](../add-configure-controls.md)?

2. Add a **[Label](control-text-box.md)** control, move it below the **Radio** control, and set the **[Text](properties-core.md)** property of the **[Label](control-text-box.md)** control to this formula:

    **If("Premium" in Pricing.Selected.Value, "$200 per day", "$150 per day")**

    Want more information about the **[If](../functions/function-if.md)** function or [other functions](../formula-reference.md)?

3. While holding down the Alt key, select either option in the **Radio** control.

    The **[Label](control-text-box.md)** control shows the appropriate text for your choice.

4. (optional) While holding down the Alt key, select the other option to confirm that the appropriate text appears.

## Accessibility guidelines

### Color contrast

In addition to the [standard color contrast requirements](../accessible-apps-color.md), ensure adequate color contrast between:

* **RadioSelectionFill** and **RadioBackgroundFill**
* **RadioBackgroundFill** and **[Fill](properties-color-border.md)**

### Screen-reader support

* Ensure that every option has a **[Value](properties-core.md)**.
* Consider adding a **[Label](control-text-box.md)** immediately before the **Radio** control to serve as the heading.

### Keyboard support

* Set the **[TabIndex](properties-accessibility.md)** property to zero or greater so that keyboard users can navigate to it.
* Set the **[FocusedBorderColor](properties-color-border.md)** and **[FocusedBorderThickness](properties-color-border.md)** properties so that focus indicators are clearly visible.


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]