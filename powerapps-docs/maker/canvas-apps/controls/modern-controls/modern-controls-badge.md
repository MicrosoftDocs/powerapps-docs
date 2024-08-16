---
title: Badge control in Power Apps
description: Learn about the details, properties, and examples of the Badge control in Power Apps.
author: yogeshgupta698

ms.topic: reference
ms.component: canvas
ms.date: 4/4/2023
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
# Badge control in Power Apps

A badge is a visual decoration for UI elements.

## Description
Badge can be used to display content in a visually better way. The key properties for this control are **Content**, **Shape**, and **Appearance**. 

## General

**Content** – The content to be displayed inside Badge control

**Visible** - Whether a control appears or is hidden. 

## Size and position

**[X](../properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](../properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

**Width** - The distance between a control's left and right edges. 

**Height** - The distance between a control's top and bottom edges. 

## Style and theme

**Appearance** – A Badge can be filled, outline, ghost, inverted.

**Shape** – The shape of the badge can be circular, square, or rounded. 

**ThemeColor** – The style of the badge has different visual representations based on the selected scenarios: brand, danger, important, informative, severe, subtle, success, or warning. 

**BasePaletteColor** - The color palette applied to a control. This impacts all surfaces of the control that render a theme color. This property is on in effect if the **Color** property has a value of **Brand**.  

**Font** - The name of the family of fonts in which text appears. 

**FontSize** - The font size of the text that appears on a control. If the value is null or zero, then the font size is driven by selected Fluent theme. 

**FontColor** - The color of text in a control. 

**FontWeight** - The weight of the text in a control: **Bold**, **Lighter**, **Normal**, or **Semibold**. 

**FontItalic** - Whether the text in a control is italic. 

**FontUnderline** - Whether a line appears under the text that appears on a control. 

**FontStrikethrough** - Whether a line appears through the text that appears on a control. 


## Additional properties

**AccessibleLabel** – Label for screen readers. 

**DisplayMode** – Whether the control allows user input (Edit), only displays data (View), or is disabled (Disabled). 





