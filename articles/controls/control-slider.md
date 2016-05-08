<properties
    pageTitle="Slider control: reference | Microsoft PowerApps"
    description="Information, including properties and examples, about the slider control"
    services=""
    suite="powerapps"
    documentationCenter="na"
    authors="aftowen"
    manager="erikre"
    editor=""
    tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="03/09/2016"
   ms.author="anneta"/>

# Slider control in PowerApps #
A control with which the user can specify a value by dragging a handle.

## Description ##
The user can indicate a value, between a minimum and a maximum value that you specify, by dragging the handle of a slider left-right or up-down, depending on the direction that you choose.

## Key properties ##

**[Default](../properties/properties-core.md)** – The initial value of a control before it is changed by the user.

**Max** – The maximum value to which the user can set a slider or a rating.

**Min** – The minimum value to which the user can set a slider.

**[Value](../properties/properties-core.md)** – The value of an input control.

## Additional properties ##

**[BorderColor](../properties/properties-color-border.md)** – The color of a control's border.

**[BorderStyle](../properties/properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](../properties/properties-color-border.md)** – The thickness of a control's border.

**[Disabled](../properties/properties-core.md)** – Whether the user can interact with the control.

**[DisabledBorderColor](../properties/properties-color-border.md)** – The color of a control's border if the control's **Disabled** property is set to **true**.

**HandleActiveFill** – The color of the handle for a slider as the user changes its value.

**HandleFill** – The color of the handle (the element that changes position) in a toggle or slider control.

**HandleHoverFill** – The color of the handle in a slider when the user keeps the mouse pointer on it.

**[Height](../properties/properties-size-location.md)** – The distance between a control's top and bottom edges.

**[HoverBorderColor](../properties/properties-color-border.md)** – The color of a control's border when the user keeps the mouse pointer on that control.

**Layout** – Whether the user scrolls through a gallery or adjusts a slider top to bottom (**Vertical**) or left to right (**Horizontal**).

**[OnChange](../properties/properties-core.md)** – How the app responds when the user changes the value of a control (for example, by adjusting a slider).

**[OnSelect](../properties/properties-core.md)** – How the app responds when the user taps or clicks a control.

**[PressedBorderColor](../properties/properties-color-border.md)** – The color of a control's border when the user taps or clicks that control.

**RailFill** – The background color of the rectangle in a toggle control when its value is **false** or the color of the line to the right of the handle in a slider control.

**RailHoverFill** – When you hover on a toggle control or a slider, the background color of the rectangle in a toggle control when its value is **false** or the color of the line to the right of the handle in a slider control.

**ReadOnly** – Whether a user can change the value of a slider or rating control.

**[Reset](../properties/properties-core.md)** – Whether a control reverts to its default value.

**ShowValue** – Whether a slider's or rating's value appears as the user changes that value or hovers over the control.

**[Tooltip](../properties/properties-core.md)** – Explanatory text that appears when the user hovers over a control.

**ValueFill** – The background color of the rectangle in a toggle control when its value is **true** or the color of the line to the left of the handle in a slider control.

**ValueHoverFill** – When you keep the mouse pointer on a toggle control or a slider, the background color of the rectangle in a toggle control when its value is **true** or the color of the line to the left of the handle in a slider control.

**[Visible](../properties/properties-core.md)** – Whether a control appears or is hidden.

**[Width](../properties/properties-size-location.md)** – The distance between a control's left and right edges.

**[X](../properties/properties-size-location.md)** – The distance between the left edge of a control and the left edge of the screen.

**[Y](../properties/properties-size-location.md)** – The distance between the top edge of a control and the top edge of the screen.

## Related functions ##

[**Sum**( *Value1*, *Value2* )](function-aggregates.md)

## Example ##
1. Add a button, and set its **OnSelect** property to this formula:
<br>**ClearCollect(CityPopulations, {City:"London", Country:"United Kingdom", Population:8615000}, {City:"Berlin", Country:"Germany", Population:3562000}, {City:"Madrid", Country:"Spain", Population:3165000}, {City:"Rome", Country:"Italy", Population:2874000}, {City:"Paris", Country:"France", Population:2273000}, {City:"Hamburg", Country:"Germany", Population:1760000}, {City:"Barcelona", Country:"Spain", Population:1602000}, {City:"Munich", Country:"Germany", Population:1494000}, {City:"Milan", Country:"Italy", Population:1344000})**

	Don't know how to [add, name, and configure a control](add-configure-controls.md)?

	Want more information about the [**ClearCollect** function](function-clear-collect-clearcollect.md) or [other functions](formula-reference.md)?

1. Press F5, select the button, and then press Esc.

1. Add a slider, move it below the button, and name the slider **MinPopulation**.

1. Set the slider's **Max** property to **5000000** and its **Min** property to **1000000**.

1. Add a text gallery in vertical/portrait orientation, move it below the slider, and set the gallery's **Items** property to this formula:<br>
**Filter(CityPopulations, Population > MinPopulation)**

1. In the first item of the gallery, set the **Text** property of the top text box to **ThisItem.City**, and set the **Text** property of the bottom text box to this formula:<br> **Text(ThisItem.Population, "##,###")**

1. Press F5, and then adjust **MinPopulation** to show only those cities that have a population that's greater than the value that you specify.

1. To return to the default workspace, press Esc.
