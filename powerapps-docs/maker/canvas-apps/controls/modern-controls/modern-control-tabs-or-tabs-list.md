---
title: Tabs or tab list modern control in Power Apps
description: Learn about the details, properties and examples of the tabs or tab list modern control in Power Apps.
author: yogeshgupta698

ms.topic: reference
ms.component: canvas
ms.date: 3/23/2023
ms.subservice: canvas-maker
ms.author: yogupt


ms.reviewer: mkaur
search.audienceType: 
  - maker
contributors:
  - mduelae
  - yogeshgupta698
  - noazarur-microsoft
  
---
# Tabs or tab list modern control in Power Apps

Select a tab to move between screens or take action on app.

## Description
A **Tab** is a navigation control, which can help users switch between different context within the app. You can add list of items to tabs or select a data table field for the list in tabs to appear. The key properties for this control are **Items**, **OnChange**, and **OnSelect**.

## General

**Items** – List of items to be shown in tabs. This can be array (select value in field) or this can be a data column from a table.

**AccessibleLabel** – Label for screen readers.

**Visible** - Whether a control appears or is hidden.

## Behavior

**DisplayMode** – Whether the control allows user input (Edit), only displays data (View), or is disabled (Disabled).

## Size and position

**Size** – Choose tabs to be shown as small, medium, or large

**Alignment** – Option for tabs to be displayed as vertical or horizontal

**[X](../properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](../properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

**Width** - The distance between a control's left and right edges. 

**Height** - The distance between a control's top and bottom edges. 

## Style and theme

**BasePaletteColor** - The color palette applied to a control. This impacts all surfaces of the control that render a theme color. If the value is null or zero, then the color is driven by selected Fluent theme.

**Font** - The name of the family of fonts in which text appears. 

**FontSize** - The font size of the text that appears on a control. If the value is null or zero, then the font size is driven by selected Fluent theme.

**FontColor** - The color of text in a control. 

**FontWeight** - The weight of the text in a control: **Bold**, **Lighter**, **Normal**, or **Semibold**. 

**FontItalic** - Whether the text in a control is italic. 

**FontUnderline** - Whether a line appears under the text that appears on a control. 

**FontStrikethrough** - Whether a line appears through the text that appears on a control. 

## Additional properties

**DefaultSelectedItems** - The default value of a control before the user specifies a different value. This value should be specified as a table with the first value as the applicable value.

**[OnChange](../properties-core.md)** – Actions to perform when the user changes the value of a control.

**[OnSelect](../properties-core.md)** – Actions to perform when the user selects a control.







