---
title: 'List Box control: reference | Microsoft Docs'
description: Information, including properties and examples, about the List Box control
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
# List Box control in PowerApps
A list in which the user can select one or multiple items.

## Description
A **List Box** control always shows all available choices (unlike a **[Drop down](control-drop-down.md)** control) and in which the user can choose more than one item at a time (unlike a **[Radio](../../controls/control-radio.md)** control).

## Key properties
**[Default](../../controls/properties-core.md)** – The initial value of a control before it is changed by the user.

**[Items](../../controls/properties-core.md)** – The source of data that appears in a control such as a gallery, a list, or a chart.

[!INCLUDE [long-items](../../includes/long-items.md)]

## Additional properties
**[BorderColor](../../controls/properties-color-border.md)** – The color of a control's border.

**[BorderStyle](../../controls/properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](../../controls/properties-color-border.md)** – The thickness of a control's border.

**[FocusedBorderThickness](../../controls/properties-color-border.md)** – The thickness of the control's border when it has keyboard focus.

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

**ItemPaddingLeft** – The distance between text in a listbox and its left edge.

**[LineHeight](../../controls/properties-text.md)** – The distance between, for example, lines of text or items in a list.

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

**SelectMultiple** – Whether a user can select more than one item in a listbox.

**[Size](../../controls/properties-text.md)** – The font size of the text that appears on a control.

**[Strikethrough](../../controls/properties-text.md)** – Whether a line appears through the text that appears on a control.

**[TabIndex](../../controls/properties-accessibility.md)** – Customizes the tab order of controls at runtime when set to a non-zero value.

**[Tooltip](../../controls/properties-core.md)** – Explanatory text that appears when the user hovers over a control.

**[Underline](../../controls/properties-text.md)** – Whether a line appears under the text that appears on a control.

**[Visible](../../controls/properties-core.md)** – Whether a control appears or is hidden.

**[Width](../../controls/properties-size-location.md)** – The distance between a control's left and right edges.

**[X](../../controls/properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](../../controls/properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

## Related functions
[**Distinct**( *DataSource*, *ColumnName* )](../../functions/function-distinct.md)

## Example
1. Add a **List box** control, name it **CategoryList**, and set its **[Items](../../controls/properties-core.md)** property to this formula:<br>
   **["Carpet","Hardwood","Tile"]**
   
    Don't know how to [add, name, and configure a control](../add-configure-controls.md)?
   
    ![Flooring categories in listbox](./media/control-list-box/category-listbox.png)
2. Add three **[Drop down](control-drop-down.md)** controls, move them under **CategoryList**, and name them **CarpetList**, **HardwoodList**, and **TileList**.
3. Set the **[Items](../../controls/properties-core.md)** property of each **[Drop down](control-drop-down.md)** control to one of these values:
   
   * CarpetList: **["Caserta Stone Beige","Ageless Beauty Clay", "Lush II Tundra"]**
   * HardwoodList: **["Golden Teak","Natural Hickory", "Victoria Mahogany"]**
   * TileList: **["Honey Onyx Marble","Indian Autumn Slate", "Panaria Vitality Ceramic"]**
     
     ![Flooring names in dropdown lists](./media/control-list-box/flooring-names.png)
4. Set the **[Visible](../../controls/properties-core.md)** property of each **[Drop down](control-drop-down.md)** control to one of these values:
   
   * CarpetList: **If("Carpet" in CategoryList.SelectedItems.Value, true)**
   * HardwoodList: **If("Hardwood" in CategoryList.SelectedItems.Value, true)**
   * TileList: **If("Tile" in CategoryList.SelectedItems.Value, true)**
     
     Want more information about the **[If](../../functions/function-if.md)** function or [other functions](../formula-reference.md)?
5. Press F5, and then choose one or more items in **CategoryList**.
   
    The appropriate **[Drop down](control-drop-down.md)** control or controls appear based on your choice or choices.
   
    ![Flooring names in dropdown lists](./media/control-list-box/selected-lists.png)
6. (optional) Press Esc to return to the default workspace.

