---
title: Spinner modern control in Power Apps
description: Learn about the details, properties, and examples of the spinner modern control in Power Apps.
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
# Spinner modern control in Power Apps

Displays state in motion such as loading a page or table.

## Description
**Spinner** control can be used to display loading scenarios where an action is in progress. This powerful control provides multiple display options suited for many scenarios. The key properties for this control are **Label**, **Appearance**, and **SpinnerSize**.

## General

**Label** – The label to the spinner. The label slot receives the styling related to the text associated with the Spinner.

**AccessibleLabel** – Label for screen readers.

**Visible** - Whether a control appears or is hidden.

## Size and position

**LabelPosition** – Where the label is positioned relative to the spinner.

**SpinnerSize** – The size of the spinner.

**[X](../properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](../properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

**Width** - The distance between a control's left and right edges. 

**Height** - The distance between a control's top and bottom edges. 

## Style and theme

**Appearance** – The appearance of the Spinner. Primary or Inverted. 

**BasePaletteColor** - The color palette applied to a control. This impacts all surfaces of the control that render a theme color.  

**Font** - The name of the family of fonts in which text appears. 

**FontSize** - The font size of the text that appears on a control. If the value is null or zero, then the font size is driven by selected Fluent theme. 

**FontColor** - The color of text in a control. 

**FontWeight** - The weight of the text in a control: Bold, Lighter, Normal, or Semibold. 

**FontItalic** - Whether the text in a control is italic. 

**FontUnderline** - Whether a line appears under the text that appears on a control. 

**FontStrikethrough** - Whether a line appears through the text that appears on a control. 

## Additional properties

**DisplayMode** – Whether the control allows user input (Edit), only displays data (View), or is disabled (Disabled).

**OnChange** - Actions to perform when the user changes the value of a control.  




