---
title: Drop down modern control in Power Apps
description: Learn about the details, properties, and examples of the dropdown modern control in Power Apps.
author: yogeshgupta698

ms.topic: reference
ms.component: canvas
ms.date: 09/15/2025
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

[This article is a pre-release document and is subject to change.]

Select a value from a list of items.

## Description
A **Drop down** control saves screen space, especially when the list has many choices. The control uses only one line unless the user selects the chevron to show more choices. The key properties for this control are **Items**, **ValidationState**, and **OnChange**.

## General

**[Items](../properties-core.md)** – The source of data that contains the items that appear in the control.

Set which column shows as drop down options. In the **Properties** pane, select **Fields** > Edit. The first field in the **Fields** pane is used as options in the drop down's menu.

> [!NOTE]
> If you change **Items**, go to the **Fields** pane and check the field used for options' text. Otherwise, the drop down menu can be empty or show unexpected data.

**AccessibleLabel** – Label for screen readers

**Visible** – Whether a control appears or is hidden 

## Behavior

**Required** – Specifies if the field must be filled in.

**DisplayMode** – Specifies whether the control lets the user enter data (Edit), only shows data (View), or is disabled (Disabled).

## Size and position

**[X](../properties-size-location.md)** – The distance from the left edge of a control to the left edge of its parent container (or the screen if there's no parent container).

**[Y](../properties-size-location.md)** – The distance from the top edge of a control to the top edge of its parent container (or the screen if there's no parent container).

**Width** – The distance between a control's left and right edges.

**Height** – The distance between a control's top and bottom edges. 

## Style and theme

**BasePaletteColor** - The color palette applied to a control. It affects all surfaces of the control that show a theme color.

**FontSize** - The font size of the text that appears on a control. If the value is null or zero, the font size comes from the selected Fluent theme. 


## Additional properties

**OnChange** – Actions that run when the user changes the value of a control.

**ValidationState** - The control has two states: **Error** and **None**. When the error state is selected, the control’s border is highlighted in red.

**DefaultSelectedItems** - The initial value of a control before the user selects a different value. 
