---
title: Toggle modern control in Power Apps
description: Learn about the details, properties, and examples of the toggle modern control in Power Apps.
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
# Toggle modern control in Power Apps

A control that the user can turn on or off by moving the handle.

## Description

A toggle is a user interface element that has been created for modern graphical user interfaces (GUIs), but it functions in the same manner as a checkbox. The key properties for this control are **Checked**, **Label**, **OnCheck**, **OnSelect**, and **OnUncheck**.
 
## General

**Label** – The text shown next to the toggle. 

**AccessibleLabel** – Label for screen readers. 

**Visible** - Whether a control appears or is hidden. 

## Behavior

**Checked** - The initial value of a control before it's changed by the user. 

**DisplayMode** – Whether the control allows user input (Edit), only displays data (View), or is disabled (Disabled). 

## Size and position 

**LabelPostion** – The text shown next to the toggle can be placed before, after, or above the toggle. 

**[X](../properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](../properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

**Width** - The distance between a control's left and right edges. 

**Height** - The distance between a control's top and bottom edges. 

## Style and theme

**BasePaletteColor** - The color palette applied to a control. This impacts all surfaces of the control that render a theme color. 

**Font** - The name of the family of fonts in which text appears. 

**FontSize** - The font size of the text that appears on a control. If the value is null or zero, then the font size is driven by selected Fluent theme. 

**FontColor** - The color of text in a control. 

**FontWeight** - The weight of the text in a control: **Bold**, **Lighter**, **Normal**, or **Semibold**. 

**FontItalic** - Whether the text in a control is italic. 

**FontUnderline** - Whether a line appears under the text that appears on a control. 

**FontStrikethrough** - Whether a line appears through the text that appears on a control. 

## Additional properties

**OnCheck** – Actions to perform when the value of the toggle changes to **true**. 

**OnSelect** – Actions to perform when the user selects a control. 

**OnUncheck** – Actions to perform when the value of the toggle changes to **false**. 
