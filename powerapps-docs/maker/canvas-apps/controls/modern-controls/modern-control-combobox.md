---
title: Combobox modern control in Power Apps
description: Learn about the details, properties, and examples of the combobox modern control in Power Apps.
author: clromano
ms.topic: reference
ms.component: canvas
ms.date: 1/15/2025
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

A control that lets users select from provided choices, supports search, and multiple selections. 

## Description

A **Combobox** control lets you present collections of items for users to select. Configure single or multi-select mode via the SelectMultiple property. Key properties for this control are Items, DefaultSelectedItems, SelectedItems, SelectMultiple, and IsSearchable.

## General

**Items** – The source of data that contains the items that appear in the control.

Use the control's SearchText property within a PowerFX function to dynamically filter large datasets. For example: `Items = Filter(<dataset>, StartsWith(<column name>, Combobox.SearchText))`

You can configure which column to show as combobox options. In the **Properties** pane, select **Fields** > Edit. The first field in the **Fields** pane is used as options in the combobox's drop down menu.

> [!NOTE]
> If you change **Items**, remember to go to the **Fields** pane and change the field used for options' text. Otherwise, the drop down menu might be empty or show unexpected data.

**AccessibleLabel** – Label for screen readers.

**Visible** - Whether a control appears or is hidden.

## Behavior

**SelectMultiple** - Lets the user select a single item or multiple items. 

**IsSearchable** - Lets the user search for items before selecting. 

**DisplayMode** – Specifies if the control allows user input (Edit), only displays data (View), or is disabled (Disabled). 

## Size and position 

**[X](../properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](../properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

**Width** - The distance between a control's left and right edges. 

**Height** - The distance between a control's top and bottom edges. 

## Style and theme

**BasePaletteColor** - The color palette applied to a control. This impacts all surfaces of the control that render a theme color. 

**Font** - The name of the family of fonts in which text appears. 

**FontSize** - The font size of the text that appears on a control. If the value is null or zero, then the font size is driven by selected Fluent theme. 

**FontColor** - The color of text in a control. 

**FontWeight** - The weight of the text in a control: Bold, Lighter, Normal, or Semibold. 

**FontItalic** - Whether the text in a control is italic. 

**FontUnderline** - Whether a line appears under the text that appears on a control. 

**FontStrikethrough** - Whether a line appears through the text that appears on a control. 

## Additional properties

**OnChange** – Actions performed when the user changes the value of a control.  

**TextInputPlaceholder** - Instructional text shown to users when no items are selected. 

**MultiValueDelimiter** -  If a user selects multiple items, you can select what delimiter is added in-between items such as a comma.

**ValidationState** - The control has two states: **Error** and **None**. When the error state is selected, the control’s border is highlighted in red.

**DefaultSelectedItems** - The initial value of a control before the user selects a different value. 

