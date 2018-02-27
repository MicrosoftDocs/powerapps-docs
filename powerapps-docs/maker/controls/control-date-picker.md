---
title: 'Date Picker control: reference | Microsoft Docs'
description: Information, including properties and examples, about the Date Picker control
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
# Date Picker control in PowerApps
A control that the user can click or tap to specify a date.

## Description
If you add a **Date Picker** control instead of a **[Text input](control-text-input.md)** control, you help ensure that the user specifies a date in the correct format.

## Key properties
**DefaultDate** – The initial value of a date control unless the user changes it.

**SelectedDate** – The date currently selected in a date control.

**Format** – The text format in which the control shows the date and the user specifies the date. You can set this property to **ShortDate** (default) or **LongDate** to format dates based on the **Language** property of this control. You can also set this property to an expression, such as **yyyy/mm/dd** if you want the same format regardless of language. For example:

* The control shows **12/31/2017** if the user clicks or taps the last day of 2017, the **Format** property is set to **ShortDate**, and the **Language** property is set to **en-us**.
* The control shows **dimanche 31 decembre 2017** if the user clicks or taps the last day of 2017, the **Format** property is set to **LongDate**, and the **Language** property is set to **fr-fr**.

**Language** – Determines the language used to format dates, including names of months. If this property isn't specified, the user's device setting determines the language.

## Additional properties
**[BorderColor](properties-color-border.md)** – The color of a control's border.

**[BorderStyle](properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](properties-color-border.md)** – The thickness of a control's border.

**[FocusedBorderThickness](properties-color-border.md)** – The thickness of the control's border when it has keyboard focus.

**[Color](properties-color-border.md)** – The color of text in a control.

**[DisplayMode](properties-core.md)** – Whether the control allows user input (Edit), only displays data (View), or is disabled (Disabled).

**[DisabledBorderColor](properties-color-border.md)** – The color of a control's border if the control's **[DisplayMode](properties-core.md)** property is set to **Disabled**.

**[DisabledColor](properties-color-border.md)** – The color of text in a control if its **[DisplayMode](properties-core.md)** property is set to **Disabled**.

**[DisabledFill](properties-color-border.md)** – The background color of a control if its **[DisplayMode](properties-core.md)** property is set to **Disabled**.

**EndYear** – The latest year to which the user can set value of a date-picker control.

**[Fill](properties-color-border.md)** – The background color of a control.

**[Font](properties-text.md)** – The name of the family of fonts in which text appears.

**[FontWeight](properties-text.md)** – The weight of the text in a control: **Bold**, **Semibold**, **Normal**, or **Lighter**.

**[Height](properties-size-location.md)** – The distance between a control's top and bottom edges.

**[Italic](properties-text.md)** – Whether the text in a control is italic.

**[OnSelect](properties-core.md)** – How the app responds when the user taps or clicks a control.

**[PaddingBottom](properties-size-location.md)** – The distance between text in a control and the bottom edge of that control.

**[PaddingLeft](properties-size-location.md)** – The distance between text in a control and the left edge of that control.

**[PaddingRight](properties-size-location.md)** – The distance between text in a control and the right edge of that control.

**[PaddingTop](properties-size-location.md)** – The distance between text in a control and the top edge of that control.

**[Size](properties-text.md)** – The font size of the text that appears on a control.

**StartYear** – The earliest year to which the user can set the value of a date-picker control.

**[TabIndex](properties-accessibility.md)** – Customizes the tab order of controls at runtime when set to a non-zero value.

**[Visible](properties-core.md)** – Whether a control appears or is hidden.

**[Width](properties-size-location.md)** – The distance between a control's left and right edges.

**[X](properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

## Related functions
**[Year](../../functions/function-datetime-parts.md)**( *DateTimeValue* )

## Example
1. Add a **Date Picker** control, and name it **Deadline**.
   
    Don't know how to [add, name, and configure a control](../add-configure-controls.md)?
2. Add a **[Label](control-text-box.md)** control, and set its **[Text](properties-core.md)** property to this formula:
   <br>**DateDiff(Today(), Deadline.SelectedDate) & " days to go!"**
   
    Want more information about the **[DateDiff](../../functions/function-dateadd-datediff.md)** function or [other functions](../formula-reference.md)?
3. Press F5, choose a date in **Deadline**, and then click or tap **OK**.
   
    The **[Label](control-text-box.md)** control shows the number of days between today and the date that you chose.
4. To return to the default workspace, press Esc.

