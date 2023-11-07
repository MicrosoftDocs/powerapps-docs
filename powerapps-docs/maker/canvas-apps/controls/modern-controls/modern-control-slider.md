---
title: Slider modern control in Power Apps
description: Learn about the details, properties, and examples of the slider modern control in Power Apps.
author: yogeshgupta698
ms.topic: reference
ms.component: canvas
ms.date: 11/6/2023
ms.subservice: canvas-maker
ms.author: yogupt
ms.reviewer: mkaur
search.audienceType: 
  - maker
contributors:
  - mduelae
  - yogeshgupta698
  
---
# Slider modern control in Power Apps

A control with which the user can specify a value by dragging a handle.

## Description
The user can indicate a value, between a minimum and a maximum value that you specify, by dragging the handle of a slider left-right or up-down, depending on the direction that you choose.

## Key properties

**[OnChange](../properties-core.md)** – Actions to perform when the user changes the value of a control such as by adjusting a slider.

**Value** – The default and current value of slider control. Many modern controls use single property to manage default and the output updated by users.

**Min** - The minimum value to which the user can set a slider.

**Max** - The maximum value to which the user can set a slider or a rating.

**Layout** - Whether the user scrolls through a gallery or adjusts a slider top to bottom (Vertical) or left to right (Horizontal).

**BasePaletteColor** - The color palette applied to a control. This impacts all surfaces of the control that render a theme color. If the value is null or zero, then the color is driven by selected Fluent theme.

## Additional properties
**AccessibleLabel** – Label for screen readers.

**DisplayMode** – Whether the control allows user input (Edit), only displays data (View), or is disabled (Disabled).

**Visible** - Whether a control appears or is hidden.

**[X](../properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](../properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

**[Size](../properties-text.md)** – The size of the control on the canvas












