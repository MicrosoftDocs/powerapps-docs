---
title: Date Picker control in Power Apps
description: Learn about the details, properties and examples of the Date Picker control in Power Apps.
author: chmoncay
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 07/06/2021
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

# Date Picker control in Power Apps

A control that the user can select to specify a date.

## Description
If you add a **Date Picker** control instead of a **[Text input](control-text-input.md)** control, you help ensure that the user specifies a date in the correct format.

## Key properties
**DefaultDate** – The initial value of a date control unless the user changes it.

**SelectedDate** – The date currently selected in a date control.  This date is represented in local time.

**Format** – The text format in which the control shows the date and the user specifies the date. You can set this property to **ShortDate** (default) or **LongDate** to format dates based on the **Language** property of this control. You can also set this property to an expression, such as **yyyy/mm/dd** if you want the same format regardless of language. For example:

* The control shows **12/31/2017** if the user clicks or taps the last day of 2017, the **Format** property is set to **ShortDate**, and the **Language** property is set to **en-us**.
* The control shows **dimanche 31 decembre 2017** if the user clicks or taps the last day of 2017, the **Format** property is set to **LongDate**, and the **Language** property is set to **fr-fr**.

**Language** – Determines the language that's used to format dates, including names of months. If this property isn't specified, the user's device setting determines the language. Supported values include "EN-us" and "FR".

## Additional properties
**[AccessibleLabel](properties-accessibility.md)** – Label for screen readers.

**[BorderColor](properties-color-border.md)** – The color of a control's border.

**[BorderStyle](properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](properties-color-border.md)** – The thickness of a control's border.

**[Color](properties-color-border.md)** – The color of text in a control.

**DateTimeZone** – Whether to display the date in **UTC** or the user's **Local** time.

**[DisplayMode](properties-core.md)** – Whether the control allows user input (Edit), only displays data (View), or is disabled (Disabled).

**[DisabledBorderColor](properties-color-border.md)** – The color of a control's border if the control's **[DisplayMode](properties-core.md)** property is set to **Disabled**.

**[DisabledColor](properties-color-border.md)** – The color of text in a control if its **[DisplayMode](properties-core.md)** property is set to **Disabled**.

**[DisabledFill](properties-color-border.md)** – The background color of a control if its **[DisplayMode](properties-core.md)** property is set to **Disabled**.

**EndYear** – The latest year to which the user can set value of a date-picker control.

**[Fill](properties-color-border.md)** – The background color of a control.

**[FocusedBorderColor](properties-color-border.md)** – The color of a control's border when the control is focused.

**[FocusedBorderThickness](properties-color-border.md)** – The thickness of a control's border when the control is focused.

**[Font](properties-text.md)** – The name of the family of fonts in which text appears.

**[FontWeight](properties-text.md)** – The weight of the text in a control: **Bold**, **Semibold**, **Normal**, or **Lighter**.

**[Height](properties-size-location.md)** – The distance between a control's top and bottom edges.

**IconFill** – The foreground color of a the date picker icon.

**IconBackground** – The background color of a the date picker icon.

**InputTextPlaceholder** – Instructional text that appears if no dates are entered.

**IsEditable** – Whether the Date Picker text can be edited. If false, the date can only be changed by using the calendar.

**[Italic](properties-text.md)** – Whether the text in a control is italic.

**[OnSelect](properties-core.md)** – Actions to perform when the user taps or clicks a control.

**[OnChange](properties-core.md)** –  Actions to perform when the user changes the value of a control. 

Difference between **OnChange** and **OnSelect**: OnSelect and OnChange trigger on the same user action if the user's *click* causes the change. In this case, OnSelect triggers **before** OnChange.

**[PaddingBottom](properties-size-location.md)** – The distance between text in a control and the bottom edge of that control.

**[PaddingLeft](properties-size-location.md)** – The distance between text in a control and the left edge of that control.

**[PaddingRight](properties-size-location.md)** – The distance between text in a control and the right edge of that control.

**[PaddingTop](properties-size-location.md)** – The distance between text in a control and the top edge of that control.

**Reset** - Whether the Date Picker control should be reset to the **DefaultDate** value.

**[Size](properties-text.md)** – The font size of the text that appears on a control.

**StartOfWeek** – The day of the week to display in the first day column of the date-picker control.

**StartYear** – The earliest year to which the user can set the value of a date-picker control.

**[TabIndex](properties-accessibility.md)** – Keyboard navigation order in relation to other controls.

**[Visible](properties-core.md)** – Whether a control appears or is hidden.

**[Width](properties-size-location.md)** – The distance between a control's left and right edges.

**[X](properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

## Related functions

**[Year](../functions/function-datetime-parts.md)**( *DateTimeValue* )

## Examples

### Basic date picker

1. Add a **Date Picker** control, and name it "Deadline".

    Don't know how to [add, name, and configure a control](../add-configure-controls.md)?

2. Add a **[Label](control-text-box.md)** control, and set its **[Text](properties-core.md)** property to the following formula:

   ```powerapps-dot
    DateDiff(Today(), Deadline.SelectedDate) & " days to go!"
    ```

    Want more information about the **[DateDiff](../functions/function-dateadd-datediff.md)** function or [other functions](../formula-reference.md)?

3. Press **F5**, choose a date in **Deadline**, and then select **OK**.

    The **[Label](control-text-box.md)** control shows the number of days between today and the date that you chose.

4. To return to the default workspace, press Esc.

##  Reset date picker to default date

1. Add a **Date Picker** control, and name it "DateTimeReset".

    Don't know how to [add, name, and configure a control](../add-configure-controls.md)?

1. Add a **[Button](control-button.md)** control, and set its **[OnChange](properties-core.md)** property to the following formula:
    ```powerapps-dot
    Reset(DateTimeReset)
    ```

1. Press **F5**, choose a new date in **DateTimeReset**, and then select **OK**.

1. Press the button. The date will reset back to the **DefaultDate** (Today).

1. To return to the default workspace, press Esc.

## Accessibility guidelines
### Color contrast
* [Standard color contrast requirements](../accessible-apps-color.md) apply.

### Screen reader support
* **[AccessibleLabel](properties-accessibility.md)** must be present.

### Keyboard support
* **[TabIndex](properties-accessibility.md)** must be zero or greater so that keyboard users can navigate to it.
* Focus indicators must be clearly visible. Use **[FocusedBorderColor](properties-color-border.md)** and **[FocusedBorderThickness](properties-color-border.md)** to achieve this.

> [!TIP]
> When the calendar is open, press **Page up** and **Page down** to navigate between months and **Shift+Page up** and **Shift+Page down** to navigate between years.


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
