---
title: Check box control in Power Apps
description: Learn about the details, properties and examples of the check box control in Power Apps.
author: chmoncay
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.date: 10/25/2016
ms.author: chmoncay
ms.reviewer: tapanm
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Check box control in Power Apps
A control that the user can select or clear to set its value to **true** or **false**.

## Description
The user can specify a Boolean value by using this familiar control, which has been used in GUIs for decades.

## Key properties
**[Default](properties-core.md)** – The initial value of a control before it is changed by the user.

**[Text](properties-core.md)** – Text that appears on a control or that the user types into a control.

**[Value](properties-core.md)** – The value of an input control.

## Additional properties
**[BorderColor](properties-color-border.md)** – The color of a control's border.

**[BorderStyle](properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](properties-color-border.md)** – The thickness of a control's border.

**CheckboxBackgroundFill** – The background color of the box that surrounds the checkmark in a checkbox control.

**CheckboxBorderColor** – The color of the border that surrounds the checkmark in a checkbox control.

**CheckboxSize** – The width and height of the box that surrounds the checkmark in a checkbox control.

**CheckmarkFill** – The color of the checkmark in a checkbox control.

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

**OnCheck** – How an app responds when the value of a checkbox or a toggle changes to **true**.

**[OnSelect](properties-core.md)** – How the app responds when the user taps or clicks a control.

**OnUncheck** – How an app responds when the value of a checkbox or a toggle changes to **false**.

**[PaddingBottom](properties-size-location.md)** – The distance between text in a control and the bottom edge of that control.

**[PaddingLeft](properties-size-location.md)** – The distance between text in a control and the left edge of that control.

**[PaddingRight](properties-size-location.md)** – The distance between text in a control and the right edge of that control.

**[PaddingTop](properties-size-location.md)** – The distance between text in a control and the top edge of that control.

**[PressedBorderColor](properties-color-border.md)** – The color of a control's border when the user taps or clicks that control.

**[PressedColor](properties-color-border.md)** – The color of text in a control when the user taps or clicks that control.

**[PressedFill](properties-color-border.md)** – The background color of a control when the user taps or clicks that control.

**[Reset](properties-core.md)** – Whether a control reverts to its default value.

**[Size](properties-text.md)** – The font size of the text that appears on a control.

**[Strikethrough](properties-text.md)** – Whether a line appears through the text that appears on a control.

**[TabIndex](properties-accessibility.md)** – Keyboard navigation order in relation to other controls.

**[Tooltip](properties-core.md)** – Explanatory text that appears when the user hovers over a control.

**[Underline](properties-text.md)** – Whether a line appears under the text that appears on a control.

**[VerticalAlign](properties-text.md)** – The location of text on a control in relation to the vertical center of that control.

**[Visible](properties-core.md)** – Whether a control appears or is hidden.

**[Width](properties-size-location.md)** – The distance between a control's left and right edges.

**[X](properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

## Related functions
[**If**( *Condition*, *Result* )](../functions/function-if.md)

## Example
1. Add a **Check box** control, name it **chkReserve**, and set its **[Text](properties-core.md)** property to show **Reserve now**.
   
    Don't know how to [add, name, and configure a control](../add-configure-controls.md)?
2. Add a **[Date picker](control-date-picker.md)** control, and set its **[Visible](properties-core.md)** property to this formula:
   <br>**If(chkReserve.Value = true, true)**
   
    Want more information about the **[If](../functions/function-if.md)** function or [other functions](../formula-reference.md)?
3. Press F5, click or tap **chkReserve** to set its **[Value](properties-core.md)** property to **true**, and then click or tap **chkReserve** again to set its **[Value](properties-core.md)** property to **false**.
   
    The **[Date Picker](control-date-picker.md)** control appears when the **[Value](properties-core.md)** property of **chkReserve** is **true** but not when it's **false**.
4. To return to the default workspace, press Esc.


## Accessibility guidelines
### Color contrast
There must be adequate color contrast between:
* **CheckmarkFill** and **CheckboxBackgroundFill**
* **CheckboxBackgroundFill** and **[Fill](properties-color-border.md)**
* **CheckboxBackgroundFill** and **[PressedFill](properties-color-border.md)**
* **CheckboxBackgroundFill** and **[HoverFill](properties-color-border.md)**

This is in addition to the [standard color contrast requirements](../accessible-apps-color.md).

### Screen reader support
* **[Text](properties-core.md)** must be present.

### Keyboard support
* **[TabIndex](properties-accessibility.md)** must be zero or greater so that keyboard users can navigate to it.
* Focus indicators must be clearly visible. Use **[FocusedBorderColor](properties-color-border.md)** and **[FocusedBorderThickness](properties-color-border.md)** to achieve this.
 


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]