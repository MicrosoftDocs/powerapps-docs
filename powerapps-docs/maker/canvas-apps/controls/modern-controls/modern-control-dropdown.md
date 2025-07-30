---
title: Drop down modern control in Power Apps
description: Learn about the details, properties, and examples of the dropdown modern control in Power Apps.
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
# Drop down modern control in Power Apps (preview)

[This article is pre-release document and is subject to change.]

Select a value from the list of items.

## Description
A **Drop down** control conserves screen real estate, especially when the list contains a large number of choices. The control takes up only one line unless the user selects the chevron to reveal more choices. The key properties for this control are **Items**, **ValidationState**, and **OnChange**.

## General

**[Items](../properties-core.md)** – The source of data that contains the items that appear in the control. If the source has multiple columns, set the control's **Value** property to the column of data that you want to show.

**AccessibleLabel** – Label for screen readers.

**Visible** - Whether a control appears or is hidden. 

## Behavior 

**Required** - Can mandate if one must fill in field.

**DisplayMode** – Whether the control allows user input (Edit), only displays data (View), or is disabled (Disabled).

## Size and position

**[X](../properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](../properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

**Width** - The distance between a control's left and right edges. 

**Height** - The distance between a control's top and bottom edges. 

## Style and theme

**BasePaletteColor** - The color palette applied to a control. This impacts all surfaces of the control that render a theme color.  

**FontSize** - The font size of the text that appears on a control. If the value is null or zero, then the font size is driven by selected Fluent theme. 


## Additional properties

**OnChange** – Actions to perform when the user changes the value of a control.  

**ValidationState** - The control has two states, which are **Error** and **None**. When the error state is selected the control’s border is highlighted in red. 

**DefaultSelectedItems** - The initial value of a control before the user specifies a different value. 
