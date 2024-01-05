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
  
---
# Tabs or tab list modern control in Power Apps

Select a tab to move between screens or take action on app.

## Description
A **Tab** is a navigation control which can help users switch between different context within the app. You can add list of items to tabs or select a data table field for the list in tabs to appear.

## Key properties

**Items** – List of items to be shown in tabs. This can be array (select value in field) or this can be a data column from a table.

**DefaultSelectedItems** - The default value of a control before the user specifies a different value. This value should be specified as a table with first value as applicable value.

**[OnChange](../properties-core.md)** – Actions to perform when the user changes the value of a control.

**[OnSelect](../properties-core.md)** – Actions to perform when the user taps or clicks a control.

**BasePaletteColor** - The color palette applied to a control. This impacts all surfaces of the control that render a theme color. If the value is null or zero, then the color is driven by selected Fluent theme.

**FontSize** - The font size of the text that appears on a control. If the value is null or zero, then the font size is driven by selected Fluent theme.

**Size** – Choose tabs to be shown as small, medium or large

**Alignment** – Option for tabs to be displayed as vertical or horizontal

## Additional properties
**Accessible label** – Label for screen readers.

**DisplayMode** – Whether the control allows user input (Edit), only displays data (View), or is disabled (Disabled).

**Visible** - Whether a control appears or is hidden.

**[X](../properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](../properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).






