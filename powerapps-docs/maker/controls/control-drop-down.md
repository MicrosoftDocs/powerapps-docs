---
title: 'Drop down control: reference | Microsoft Docs'
description: Information, including properties and examples, about the Drop down control
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
# Drop down control in PowerApps
A list that shows only the first item unless the user opens it.

## Description
A **Drop down** control conserves screen real estate, especially when the list contains a large number of choices. The control takes up only one line unless the user selects the chevron to reveal more choices.

## Key properties
**[Default](../../controls/properties-core.md)** – The initial value of a control before it is changed by the user.

**[Items](../../controls/properties-core.md)** – The source of data that appears in a control such as a gallery, a list, or a chart.

[!INCLUDE [long-items](../../includes/long-items.md)]

**Selected** – The selected item.

## Additional properties
**[BorderColor](../../controls/properties-color-border.md)** – The color of a control's border.

**[BorderStyle](../../controls/properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](../../controls/properties-color-border.md)** – The thickness of a control's border.

**[FocusedBorderThickness](../../controls/properties-color-border.md)** – The thickness of the control's border when it has keyboard focus.

**ChevronBackground** – The color behind the down arrow in a dropdown list.

**ChevronFill** – The color of the down arrow in a dropdown list.

**[Color](../../controls/properties-color-border.md)** – The color of text in a control.

**[DisplayMode](../../controls/properties-core.md)** – Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**).

**[DisabledBorderColor](../../controls/properties-color-border.md)** – The color of a control's border if the control's **[DisplayMode](../../controls/properties-core.md)** property is set to **Disabled**.

**[DisabledColor](../../controls/properties-color-border.md)** – The color of text in a control if its **[DisplayMode](../../controls/properties-core.md)** property is set to **Disabled**.

**[DisabledFill](../../controls/properties-color-border.md)** – The background color of a control if its **[DisplayMode](../../controls/properties-core.md)** property is set to **Disabled**.

**[Fill](../../controls/properties-color-border.md)** – The background color of a control.

**[Font](../../controls/properties-text.md)** – The name of the family of fonts in which text appears.

**[FontWeight](../../controls/properties-text.md)** – The weight of the text in a control: **Bold**, **Semibold**, **Normal**, or **Lighter**.

**[Height](../../controls/properties-size-location.md)** – The distance between a control's top and bottom edges.

**[HoverBorderColor](../../controls/properties-color-border.md)** – The color of a control's border when the user keeps the mouse pointer on that control.

**[HoverColor](../../controls/properties-color-border.md)** – The color of the text in a control when the user keeps the mouse pointer on it.

**[HoverFill](../../controls/properties-color-border.md)** – The background color of a control when the user keeps the mouse pointer on it.

**[Italic](../../controls/properties-text.md)** – Whether the text in a control is italic.

**[OnChange](../../controls/properties-core.md)** – How the app responds when the user changes the value of a control (for example, by adjusting a slider).

**[OnSelect](../../controls/properties-core.md)** – How the app responds when the user taps or clicks a control.

**[PaddingBottom](../../controls/properties-size-location.md)** – The distance between text in a control and the bottom edge of that control.

**[PaddingLeft](../../controls/properties-size-location.md)** – The distance between text in a control and the left edge of that control.

**[PaddingRight](../../controls/properties-size-location.md)** – The distance between text in a control and the right edge of that control.

**[PaddingTop](../../controls/properties-size-location.md)** – The distance between text in a control and the top edge of that control.

**[PressedBorderColor](../../controls/properties-color-border.md)** – The color of a control's border when the user taps or clicks that control.

**[PressedColor](../../controls/properties-color-border.md)** – The color of text in a control when the user taps or clicks that control.

**[PressedFill](../../controls/properties-color-border.md)** – The background color of a control when the user taps or clicks that control.

**[Reset](../../controls/properties-core.md)** – Whether a control reverts to its default value.

**[SelectionColor](../../controls/properties-color-border.md)** – The text color of a selected item or items in a list or the color of the selection tool in a pen control.

**[SelectionFill](../../controls/properties-color-border.md)** – The background color of a selected item or items in a list or a selected area of a pen control.

**[Size](../../controls/properties-text.md)** – The font size of the text that appears on a control.

**[Strikethrough](../../controls/properties-text.md)** – Whether a line appears through the text that appears on a control.

**[TabIndex](../../controls/properties-accessibility.md)** – Customizes the tab order of controls at runtime when set to a non-zero value.

**[Tooltip](../../controls/properties-core.md)** – Explanatory text that appears when the user hovers over a control.

**[Underline](../../controls/properties-text.md)** – Whether a line appears under the text that appears on a control.

**[Visible](../../controls/properties-core.md)** – Whether a control appears or is hidden.

**[Width](../../controls/properties-size-location.md)** – The distance between a control's left and right edges.

**[X](../../controls/properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](../../controls/properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

## Example
1. Add a **[Button](control-button.md)** control, and set its **[Text](../../controls/properties-core.md)** property to show **Collect**.
   
    Don't know how to [add, name, and configure a control](../add-configure-controls.md)?
2. Set the **[OnSelect](../../controls/properties-core.md)** property of the **[Button](control-button.md)** control to this formula:
   <br>**ClearCollect(CityPopulations, {City:"London", Country:"United Kingdom", Population:8615000}, {City:"Berlin", Country:"Germany", Population:3562000}, {City:"Madrid", Country:"Spain", Population:3165000}, {City:"Rome", Country:"Italy", Population:2874000}, {City:"Paris", Country:"France", Population:2273000}, {City:"Hamburg", Country:"Germany", Population:1760000}, {City:"Barcelona", Country:"Spain", Population:1602000}, {City:"Munich", Country:"Germany", Population:1494000}, {City:"Milan", Country:"Italy", Population:1344000})**
   
    Want more information about the **[ClearCollect](../../functions/function-clear-collect-clearcollect.md)** function or [other functions](../formula-reference.md)?
3. Press F5, click or tap the **[Button](control-button.md)** control, and then press Esc.
4. Add a **Drop down** control, name it **Countries**, and set its **[Items](../../controls/properties-core.md)** property to this formula:
   <br>**Distinct(CityPopulations, Country)**
5. Add a **Text gallery** control in vertical/portrait orientation, and set its **[Items](../../controls/properties-core.md)** property to this formula:
   <br>**Filter(CityPopulations, Countries.Selected.Value in Country)**
6. In the first item of the **Text gallery** control, set the **[Text](../../controls/properties-core.md)** property of the upper **[Label](../../controls/control-text-box.md)** control to **ThisItem.City**, and delete the bottom **[Label](../../controls/control-text-box.md)** control.
7. Set the **[TemplateSize](control-gallery.md)** property of the **Text gallery** control to **80**.
8. Press F5, click or tap the chevron in the **Countries** list, and then choose an option in that list.
   
    The **Text gallery** control shows only those cities in the country that you chose.

