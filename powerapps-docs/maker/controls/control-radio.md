---
title: 'Radio control: reference | Microsoft Docs'
description: Information, including properties and examples, about the Radio control
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
# Radio control in PowerApps
A list that shows all options but the user can select only one at a time.

## Description
A **Radio** control, with which users have decades of experience, is best used with only a few options that are mutually exclusive.

## Key properties
**[Default](properties-core.md)** – The initial value of a control before it is changed by the user.

**[Items](properties-core.md)** – The source of data that appears in a control such as a gallery, a list, or a chart.

[!INCLUDE [long-items](../../includes/long-items.md)]

**[Value](properties-core.md)** – The value of an input control.

## All properties
**[Align](../../controls/properties-text.md)** – The location of text in relation to the horizontal center of its control.

**[BorderColor](properties-color-border.md)** – The color of a control's border.

**[BorderStyle](properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](properties-color-border.md)** – The thickness of a control's border.

**[FocusedBorderThickness](properties-color-border.md)** – The thickness of the control's border when it has keyboard focus.

**[Color](properties-color-border.md)** – The color of text in a control.

**[DisplayMode](properties-core.md)** – Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**).

**[DisabledBorderColor](properties-color-border.md)** – The color of a control's border if the control's **[DisplayMode](properties-core.md)** property is set to **Disabled**.

**[DisabledColor](properties-color-border.md)** – The color of text in a control if its **[DisplayMode](properties-core.md)** property is set to **Disabled**.

**[DisabledFill](properties-color-border.md)** – The background color of a control if its **[DisplayMode](properties-core.md)** property is set to **Disabled**.

**[Fill](properties-color-border.md)** – The background color of a control.

**[Font](../../controls/properties-text.md)** – The name of the family of fonts in which text appears.

**[FontWeight](../../controls/properties-text.md)** – The weight of the text in a control: **Bold**, **Semibold**, **Normal**, or **Lighter**.

**[Height](../../controls/properties-size-location.md)** – The distance between a control's top and bottom edges.

**[HoverColor](properties-color-border.md)** – The color of the text in a control when the user keeps the mouse pointer on it.

**[HoverFill](properties-color-border.md)** – The background color of a control when the user keeps the mouse pointer on it.

**[Italic](../../controls/properties-text.md)** – Whether the text in a control is italic.

**[LineHeight](../../controls/properties-text.md)** – The distance between, for example, lines of text or items in a list.

**[OnChange](properties-core.md)** – How the app responds when the user changes the value of a control (for example, by adjusting a slider).

**[OnSelect](properties-core.md)** – How the app responds when the user taps or clicks a control.

**[PaddingBottom](../../controls/properties-size-location.md)** – The distance between text in a control and the bottom edge of that control.

**[PaddingLeft](../../controls/properties-size-location.md)** – The distance between text in a control and the left edge of that control.

**[PaddingRight](../../controls/properties-size-location.md)** – The distance between text in a control and the right edge of that control.

**[PaddingTop](../../controls/properties-size-location.md)** – The distance between text in a control and the top edge of that control.

**[PressedColor](properties-color-border.md)** – The color of text in a control when the user taps or clicks that control.

**[PressedFill](properties-color-border.md)** – The background color of a control when the user taps or clicks that control.

**RadioBackgroundFill** – The background color of the circles in a radio-button control.

**RadioBorderColor** – The color of the circle for each option in a radio-button control.

**RadioSelectionFill** – The color that appears inside the circle of the selected option in a radio-button control.

**RadioSize** – The diameter of the circles in a radio-button control.

**[Reset](properties-core.md)** – Whether a control reverts to its default value.

**[Size](../../controls/properties-text.md)** – The font size of the text that appears on a control.

**[Strikethrough](../../controls/properties-text.md)** – Whether a line appears through the text that appears on a control.

**[TabIndex](properties-accessibility.md)** – Customizes the tab order of controls at runtime when set to a non-zero value.

**[Tooltip](properties-core.md)** – Explanatory text that appears when the user hovers over a control.

**[Underline](../../controls/properties-text.md)** – Whether a line appears under the text that appears on a control.

**[Visible](properties-core.md)** – Whether a control appears or is hidden.

**[Width](../../controls/properties-size-location.md)** – The distance between a control's left and right edges.

**[X](../../controls/properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](../../controls/properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

## Related functions
[**Distinct**( *DataSource*, *ColumnName* )](../../functions/function-distinct.md)

## Example
1. Add a **Radio** control, name it **Pricing**, and set its **[Items](properties-core.md)** property to this formula:
   <br>**["Standard", "Premium"]**
   
    Don't know how to [add, name, and configure a control](../add-configure-controls.md)?
2. Add a **[Label](control-text-box.md)** control, move it below the **Radio** control, and set the **[Text](properties-core.md)** property of the **[Label](control-text-box.md)** control to this formula:
   <br>**If("Premium" in Pricing.Selected.Value, "$200 per day", "$150 per day")**
   
    Want more information about the **[If](../../functions/function-if.md)** function or [other functions](../formula-reference.md)?
3. Press F5, and then choose either option in the **Radio** control.
   
    The **[Label](control-text-box.md)** control shows the appropriate text for your choice.
4. (optional) In the **Radio** control, choose the other option to confirm that the appropriate text appears.
5. To return to the default workspace, press Esc.

