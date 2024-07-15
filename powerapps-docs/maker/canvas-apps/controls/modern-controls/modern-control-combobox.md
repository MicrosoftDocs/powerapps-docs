---
title: Combobox modern control in Power Apps
description: Learn about the details, properties, and examples of the combobox modern control in Power Apps.
author: noazarur-microsoft

ms.topic: reference
ms.component: canvas
ms.date: 3/15/2024
ms.subservice: canvas-maker
ms.author: noazarur


ms.reviewer: mkaur
search.audienceType: 
  - maker
contributors:
  - mduelae
  - noazarur-microsoft
  
---
# Combobox modern control in Power Apps (preview)

[This article is pre-release document and is subject to change.]

A control that allows users to make selections from provided choices and supports search and multiple selections. 

## Description

A **Combobox** control allows you to search for items that you select. Single or multi-select mode is configured via the SelectMultiple property. Key properties for this control are Items, DefaultSelectedItems, SelectedItems, SelectMultiple, and IsSearchable.

## General

**Items** – The source of data that contains the items that appear in the control. If the source has multiple columns, set the control's **Value** property to the column of data that you want to show. 

**AccessibleLabel** – Label for screen readers.

**Visible** - Whether a control appears or is hidden.

## Behavior

**SelectMultiple** - Whether the user can select a single item or multiple items. 

**IsSearchable** - Whether the user can search for items before selecting. 

**DisplayMode** – Whether the control allows user input (Edit), only displays data (View), or is disabled (Disabled). 

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

**OnChange** – Actions to perform when the user changes the value of a control.  

**TextInputPlaceholder** - Instructional text shown to end users when no items are selected. 

**MultiValueDelimiter** -  If a user selects multiple items, you can select what delimiter is added in-between items such as a comma.

**ValidationState** - The control has two states, which are **Error** and **None**. When the error state is selected the control’s border is highlighted in red.

**DefaultSelectedItems** - The initial value of a control before the user specifies a different value. 


