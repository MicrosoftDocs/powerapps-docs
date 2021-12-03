---
title: Toggle control in Power Apps
description: Learn about the details, properties and examples of the Toggle control in Power Apps.
author: chmoncay
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
# Toggle control in Power Apps
A control that the user can turn on or off by moving its handle.

## Description
A toggle is designed for recent GUIs but behaves the same way as a check box.

## Key properties
**[Default](properties-core.md)** – The initial value of a control before it is changed by the user.

**[Value](properties-core.md)** – The value of an input control.

## Additional properties
**[AccessibleLabel](properties-accessibility.md)** – Label for screen readers.

**[BorderColor](properties-color-border.md)** – The color of a control's border.

**[BorderStyle](properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](properties-color-border.md)** – The thickness of a control's border.

**[DisplayMode](properties-core.md)** – Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**).

**[DisabledBorderColor](properties-color-border.md)** – The color of a control's border if the control's **[DisplayMode](properties-core.md)** property is set to **Disabled**.

**FalseFill** – The toggle fill color when the toggle is off.

**FalseHoverFill** – The toggle hover fill color when toggle is off.

**FalseText** – The text shown when the toggle is off.

**[Fill](properties-color-border.md)** – The background color of a control.

**[FocusedBorderColor](properties-color-border.md)** – The color of a control's border when the control is focused.

**[FocusedBorderThickness](properties-color-border.md)** – The thickness of a control's border when the control is focused.

**HandleFill** – The fill color of the toggle handle.

**[Height](properties-size-location.md)** – The distance between a control's top and bottom edges.

**[HoverBorderColor](properties-color-border.md)** – The color of a control's border when the user keeps the mouse pointer on that control.

**[OnChange](properties-core.md)** – Actions to perform when the user changes the value of a control (for example, by adjusting a slider).

**OnCheck** – Actions to perform when the value of a checkbox or a toggle changes to **true**.

**[OnSelect](properties-core.md)** – Actions to perform when the user taps or clicks a control.

**OnUncheck** – Actions to perform when the value of a checkbox or a toggle changes to **false**.

**[PressedBorderColor](properties-color-border.md)** – The color of a control's border when the user taps or clicks that control.

**RailFill** – The background color of the rectangle in a toggle control when its value is **false** or the color of the line to the right of the handle in a slider control.

**RailHoverFill** – When you hover on a toggle control or a slider, the background color of the rectangle in a toggle control when its value is **false** or the color of the line to the right of the handle in a slider control.

**[Reset](properties-core.md)** – Whether a control reverts to its default value.

**ShowLabel** – Whether a text label is shown beside the toggle control.

**[TabIndex](properties-accessibility.md)** – Keyboard navigation order in relation to other controls.

**TextPosition** – Whether the label is to the left or the right of the toggle control.

**[Tooltip](properties-core.md)** – Explanatory text that appears when the user hovers over a control.

**TrueFill** – Toggle fill color when the toggle is on.

**TrueHoverFill** – Toggle hover fill color when the toggle is on.

**TrueText** – Text shown when the toggle is on.

**ValueFill** – The background color of the rectangle in a toggle control when its value is **true** or the color of the line to the left of the handle in a slider control.

**ValueHoverFill** – When you keep the mouse pointer on a toggle control or a slider, the background color of the rectangle in a toggle control when its value is **true** or the color of the line to the left of the handle in a slider control.

**[Visible](properties-core.md)** – Whether a control appears or is hidden.

**[Width](properties-size-location.md)** – The distance between a control's left and right edges.

**[X](properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

## Related functions
[**If**( *Condition*, *Result* )](../functions/function-if.md)

## Example
1. Add a toggle, and name it **MemberDiscount**.

    Don't know how to [add, name, and configure a control](../add-configure-controls.md)?
2. Add a label, and set its **[Text](properties-core.md)** property to this formula:
   <br>**If(MemberDiscount.Value = true, "Price: $75", "Price: $100")**

    Want more information about the **[If](../functions/function-if.md)** function or [other functions](../formula-reference.md)?
3. Press F5, and change the value of **MemberDiscount**.

    The label shows a different price, depending on whether **MemberDiscount** is on or off.
4. To return to the default workspace, press Esc.


## Accessibility guidelines
### Color contrast
There must be adequate color contrast between:
* **HandleFill** and **FalseFill**
* **HandleFill** and **FalseHoverFill**
* **HandleFill** and **TrueFill**
* **HandleFill** and **TrueHoverFill**
* **FalseFill** and color outside the control
* **FalseHoverFill** and color outside the control
* **TrueFill** and color outside the control
* **TrueHoverFill** and color outside the control

This is in addition to the [standard color contrast requirements](../accessible-apps-color.md).

### Screen reader support
* **[AccessibleLabel](properties-accessibility.md)** must be present.
* **FalseText** must be present.
* **TrueText** must be present.

### Low vision support
* Consider setting **ShowLabel** to **true** so that users can quickly determine the toggle value.

### Keyboard support
* **[TabIndex](properties-accessibility.md)** must be zero or greater so that keyboard users can navigate to it.
* Focus indicators must be clearly visible. Use **[FocusedBorderColor](properties-color-border.md)** and **[FocusedBorderThickness](properties-color-border.md)** to achieve this.


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]