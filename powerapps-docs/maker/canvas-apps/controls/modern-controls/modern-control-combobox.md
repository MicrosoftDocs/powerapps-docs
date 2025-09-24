---
title: Combobox modern control in Power Apps
description: Learn about the details, properties, and examples of the combobox modern control in Power Apps.
author: clromano
ms.topic: reference
ms.component: canvas
ms.date: 09/15/2025
ms.subservice: canvas-maker
ms.author: clromano
ms.reviewer: mkaur
search.audienceType: 
  - maker
contributors:
  - clromano
  - mduelae
  - noazarur-microsoft
  
---

# Combobox modern control in Power Apps

This control lets users select from provided choices, search, and make multiple selections. 

## Description

A **Combobox** control lets you show a collection of items for the user to select. Set single or multi-select mode with the `SelectMultiple` property. Key properties are `Items`, `DefaultSelectedItems`, `SelectedItems`, `SelectMultiple`, and `IsSearchable`.

## General

**Items** – The source of data that has the items that appear in the control.

Use the control's `SearchText` property in a PowerFX function to filter large datasets dynamically. For example: `Items = Filter(<dataset>, StartsWith(<column name>, Combobox.SearchText))`

Set which column appears as combobox options. In the **Properties** pane, select **Fields** > Edit. The first field in the **Fields** pane appears as options in the combobox's drop down menu.

> [!NOTE]
> If you change **Items**, go to the **Fields** pane and check the field used for options' text. Otherwise, the drop down menu might be empty or show unexpected data.

**AccessibleLabel** – Label for screen readers.

**Visible** – Whether a control appears or is hidden.

## Behavior

**SelectMultiple** – Lets the user select one or more items.

**IsSearchable** – Lets the user search for items before selecting.

**DisplayMode** – Specifies if the control lets user input (Edit), only shows data (View), or is disabled (Disabled).

## Size and position 

**[X](../properties-size-location.md)** – The distance from the left edge of a control to the left edge of its parent container (or the screen if there's no parent container).

**[Y](../properties-size-location.md)** – The distance from the top edge of a control to the top edge of its parent container (or the screen if there's no parent container).

**Width** – The distance between a control's left and right edges.

**Height** – The distance between a control's top and bottom edges. 

## Style and theme

**BasePaletteColor** - The color palette applied to a control. It affects all surfaces of the control that show a theme color.

**Font** - The font family name for the text.

**FontSize** - The font size of the text on a control. If the value is null or zero, the font size comes from the selected Fluent theme.

**FontColor** - The text color in a control.

**FontWeight** - The text weight in a control: Bold, Lighter, Normal, or Semibold.

**FontItalic** - Whether the text in a control is italic.

**FontUnderline** - Whether a line appears under the text in a control.

**FontStrikethrough** - Whether a line appears through the text in a control. 

## Additional properties

**OnChange** – Actions performed when the user changes the value of a control.  

**TextInputPlaceholder** - Instructional text shown to users when no items are selected. 

**MultiValueDelimiter** -  If a user selects multiple items, you can select what delimiter is added in-between items such as a comma.

**ValidationState** - The control has two states: **Error** and **None**. When the error state is selected, the control’s border is highlighted in red.

**DefaultSelectedItems** - The initial value of a control before the user selects a different value. 

