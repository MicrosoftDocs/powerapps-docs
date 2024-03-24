---
title: Number Input modern control in Power Apps
description: Learn about the details, properties, and examples of the number input modern control in Power Apps.
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
# Number Input modern control in Power Apps (preview)

[This article is pre-release document and is subject to change.]

A number input control the user can modify. 

## Description

Makers can add a number input control that can be used to type in or use the arrows to select a number value. They can also configure decimal precision and step values for this control. This control also provides number type as a default output to build numeric scenarios in Power Apps. A key property for this control is Value.
 
## General

**Value** – The initial value of a control before it's changed by the user. 

**Min** - The minimum number the user can input. 

**Max** – The maximum number the user can input. 

**Precision** – How many decimal points to show for the number. 

**Step** – What value is added or subtracted from the prior number when the up or down arrows are selected. 

**AccessibleLabel** – Label for screen readers. 

**Visible** - Whether a control appears or is hidden. 

## Behavior

**DisplayMode** – Whether the control allows user input (Edit), only displays data (View), or is disabled (Disabled). 

## Size and position 

**[X](../properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](../properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

**Width** - The distance between a control's left and right edges. 

**Height** - The distance between a control's top and bottom edges. 

## Style and theme

**BasePaletteColor** - The color palette applied to a control. This impacts all surfaces of the control that render a theme color. 

**FontSize** - The font size of the text that appears on a control. If the value is null or zero, then the font size is driven by selected Fluent theme. 

**Align** - The location of text in relation to the horizontal center of its control. The options are updated to **Start**, **End**, **Center, and **Justify** to better accommodate left to right languages. 

## Additional properties

**DelayOutput** - When set to true, user input is registered after half a second delay. Useful for delaying expensive operations until user completes inputting text such as when filtering when input is used in other formulas. 

**OnChange** – Actions to perform when the user changes the value of a control. 

**ValidationState** - The control has two states, which are **Error** and **None**. When the error state is selected the date picker border is highlighted in red.  

