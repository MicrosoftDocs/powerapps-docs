---
title: Rating control in Power Apps
description: Learn about the details, properties and examples of the Rating control in Power Apps.
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
---
# Rating control in Power Apps
A control with which users can indicate a value between 1 and a maximum number that you specify.

## Description
In this control, the user can indicate, for example, how much they liked something by selecting a certain number of stars.

## Key properties
**[Default](properties-core.md)** – The initial value of a control before it is changed by the user.

**Max** – The maximum value to which the user can set a slider or a rating.

## Additional properties
**[AccessibleLabel](properties-accessibility.md)** – Label for screen readers.

**[BorderColor](properties-color-border.md)** – The color of a control's border.

**[BorderStyle](properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](properties-color-border.md)** – The thickness of a control's border.

**[DisplayMode](properties-core.md)** – Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**).

**[Fill](properties-color-border.md)** – The background color of a control.

**[FocusedBorderColor](properties-color-border.md)** – The color of a control's border when the control is focused.

**[FocusedBorderThickness](properties-color-border.md)** – The thickness of a control's border when the control is focused.

**[Height](properties-size-location.md)** – The distance between a control's top and bottom edges.

**[OnChange](properties-core.md)** – Actions to perform when the user changes the value of a control (for example, by adjusting a slider).

**[OnSelect](properties-core.md)** – Actions to perform when the user taps or clicks a control.

**RatingFill** – The color of the stars in a rating control.

**ReadOnly** – Whether a user can change the value of a slider or rating control.

**[Reset](properties-core.md)** – Whether a control reverts to its default value.

**ShowValue** – Whether a slider's or rating's value appears as the user changes that value or hovers over the control.

**[TabIndex](properties-accessibility.md)** – Keyboard navigation order in relation to other controls.

**[Tooltip](properties-core.md)** – Explanatory text that appears when the user hovers over a control.

**[Visible](properties-core.md)** – Whether a control appears or is hidden.

**[Width](properties-size-location.md)** – The distance between a control's left and right edges.

**[X](properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

## Related functions
[**Average**( *Value1*, *Value2,* ... )](../functions/function-aggregates.md)

## Example
1. Add a **Rating** control, and name it **Quantitative**.
   
    Don't know how to [add, name, and configure a control](../add-configure-controls.md)?
2. Add a **[Text input](control-text-input.md)** control, name it **Qualitative**, and move it below the **Rating** control.
3. Set the **[Default](properties-core.md)** property of the **[Text input](control-text-input.md)** control to **""**, and set its **HintText** to this formula:
   <br>**If(Quantitative.Value > 3, "What did you especially like?", "How might we do better?")**
   
    Want more information about the **[If](../functions/function-if.md)** function or [other functions](../formula-reference.md)?
4. Press F5, and then click or tap either four or five stars in the **Rating** control.
   
    The hint text in the **[Text input](control-text-input.md)** control changes to reflect the high rating.
5. Click or tap fewer than four stars in **Quantitative**.
   
    The hint text in the **[Text input](control-text-input.md)** control changes to reflect the low rating.
6. To return to the default workspace, press Esc.


## Accessibility guidelines
### Color contrast
There must be adequate color contrast between:
* **RatingFill** and **[Fill](properties-color-border.md)**

This is in addition to the [standard color contrast requirements](../accessible-apps-color.md).

### Screen reader support
* **[AccessibleLabel](properties-accessibility.md)** must be present.

    > [!NOTE]
  > Screen readers treat the **Rating** control as radio buttons.

### Keyboard support
* **[TabIndex](properties-accessibility.md)** must be zero or greater so that keyboard users can navigate to it.
* Focus indicators must be clearly visible. Use **[FocusedBorderColor](properties-color-border.md)** and **[FocusedBorderThickness](properties-color-border.md)** to achieve this.
* Consider using a different control if there are too many stars. It can be tedious to navigate with a keyboard and difficult to select accurately with a touch screen.

    > [!NOTE]
  > The same keyboard interactions for radio buttons can be used on **Rating**.


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]