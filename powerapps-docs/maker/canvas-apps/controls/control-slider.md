---
title: Slider control in Power Apps
description: Learn about the details, properties and examples of the Slider control in Power Apps.
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
# Slider control in Power Apps
A control with which the user can specify a value by dragging a handle.

## Description
The user can indicate a value, between a minimum and a maximum value that you specify, by dragging the handle of a slider left-right or up-down, depending on the direction that you choose.

## Key properties
**[Default](properties-core.md)** – The initial value of a control before it is changed by the user.

**Max** – The maximum value to which the user can set a slider or a rating.

**Min** – The minimum value to which the user can set a slider.

**[Value](properties-core.md)** – The value of an input control.

## Additional properties
**[AccessibleLabel](properties-accessibility.md)** – Label for screen readers.

**[BorderColor](properties-color-border.md)** – The color of a control's border.

**[BorderStyle](properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](properties-color-border.md)** – The thickness of a control's border.

**[DisplayMode](properties-core.md)** – Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**).

**[DisabledBorderColor](properties-color-border.md)** – The color of a control's border if the control's **[DisplayMode](properties-core.md)** property is set to **Disabled**.

**[FocusedBorderColor](properties-color-border.md)** – The color of a control's border when the control is focused.

**[FocusedBorderThickness](properties-color-border.md)** – The thickness of a control's border when the control is focused.

**HandleActiveFill** – The color of the handle for a slider as the user changes its value.

**HandleFill** – The color of the handle (the element that changes position) in a toggle or slider control.

**HandleHoverFill** – The color of the handle in a slider when the user keeps the mouse pointer on it.

**HandleSize** – The diameter of the handle.

**[Height](properties-size-location.md)** – The distance between a control's top and bottom edges.

**[HoverBorderColor](properties-color-border.md)** – The color of a control's border when the user keeps the mouse pointer on that control.

**Layout** – Whether the user scrolls through a gallery or adjusts a slider top to bottom (**Vertical**) or left to right (**Horizontal**).

**[OnChange](properties-core.md)** – Actions to perform when the user changes the value of a control (for example, by adjusting a slider).

**[OnSelect](properties-core.md)** – Actions to perform when the user taps or clicks a control.

**[PressedBorderColor](properties-color-border.md)** – The color of a control's border when the user taps or clicks that control.

**RailFill** – The background color of the rectangle in a toggle control when its value is **false** or the color of the line to the right of the handle in a slider control.

**RailHoverFill** – When you hover on a toggle control or a slider, the background color of the rectangle in a toggle control when its value is **false** or the color of the line to the right of the handle in a slider control.

**ReadOnly** – Whether a user can change the value of a slider or rating control.

**[Reset](properties-core.md)** – Whether a control reverts to its default value.

**ShowValue** – Whether a slider's or rating's value appears as the user changes that value or hovers over the control.

**[TabIndex](properties-accessibility.md)** – Keyboard navigation order in relation to other controls.

**[Tooltip](properties-core.md)** – Explanatory text that appears when the user hovers over a control.

**ValueFill** – The background color of the rectangle in a toggle control when its value is **true** or the color of the line to the left of the handle in a slider control.

**ValueHoverFill** – When you keep the mouse pointer on a toggle control or a slider, the background color of the rectangle in a toggle control when its value is **true** or the color of the line to the left of the handle in a slider control.

**[Visible](properties-core.md)** – Whether a control appears or is hidden.

**[Width](properties-size-location.md)** – The distance between a control's left and right edges.

**[X](properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

## Related functions
[**Sum**( *Value1*, *Value2* )](../functions/function-aggregates.md)

## Example
1. Add a button, and set its **[OnSelect](properties-core.md)** property to this formula:
   <br>**ClearCollect(CityPopulations, {City:"London", Country:"United Kingdom", Population:8615000}, {City:"Berlin", Country:"Germany", Population:3562000}, {City:"Madrid", Country:"Spain", Population:3165000}, {City:"Rome", Country:"Italy", Population:2874000}, {City:"Paris", Country:"France", Population:2273000}, {City:"Hamburg", Country:"Germany", Population:1760000}, {City:"Barcelona", Country:"Spain", Population:1602000}, {City:"Munich", Country:"Germany", Population:1494000}, {City:"Milan", Country:"Italy", Population:1344000})**
   
    Don't know how to [add, name, and configure a control](../add-configure-controls.md)?
   
    Want more information about the **[ClearCollect](../functions/function-clear-collect-clearcollect.md)** function or [other functions](../formula-reference.md)?
2. Press F5, select the button, and then press Esc.
3. Add a slider, move it below the button, and name the slider **MinPopulation**.
4. Set the slider's **Max** property to **5000000** and its **Min** property to **1000000**.
5. Add a text gallery in vertical/portrait orientation, move it below the slider, and set the gallery's **[Items](properties-core.md)** property to this formula:<br>
   **Filter(CityPopulations, Population > MinPopulation)**
6. In the first item of the gallery, set the **[Text](properties-core.md)** property of the top label to **ThisItem.City**, and set the **[Text](properties-core.md)** property of the bottom label to this formula:<br> **Text(ThisItem.Population, "##,###")**
7. Press F5, and then adjust **MinPopulation** to show only those cities that have a population that's greater than the value that you specify.
8. To return to the default workspace, press Esc.


## Accessibility guidelines
### Color contrast
There must be adequate color contrast between:
* **ValueFill** and **RailFill**
* **ValueHoverFill** and **RailHoverFill**
* **[FocusedBorderColor](properties-color-border.md)** and color outside the control
* **ValueFill** and background color
* **RailFill** and background color
* **ValueHoverFill** and background color
* **RailHoverFill** and background color

### Screen reader support
* **[AccessibleLabel](properties-accessibility.md)** must be present.

### Keyboard support
* **[TabIndex](properties-accessibility.md)** must be zero or greater so that keyboard users can navigate to it.
* Focus indicators must be clearly visible. Use **[FocusedBorderColor](properties-color-border.md)** and **[FocusedBorderThickness](properties-color-border.md)** to achieve this.
* Slider value must be shown when interacting with the keyboard. This can be achieved by any one of these methods:
    * Set **ShowValue** to **true**.
    * Add a **[Label](control-text-box.md)** adjacent to the slider. Set the label's **[Text](properties-core.md)** to the slider's **[Value](properties-core.md)**.


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]