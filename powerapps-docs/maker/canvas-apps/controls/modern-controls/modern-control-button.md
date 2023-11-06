---
title: Button modern control in Power Apps
description: Learn about the details, properties and examples of the button modern control in Power Apps.
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
# Button modern control in Power Apps

A control that the user can select to interact with the app.

## Description
With the modern button you can set a button to be primary or secondary. Configure the **[OnSelect](../properties-core.md)** property of a **Button** control to run one or more formulas when the user selects the control. As a design pattern, we recommend always placing the primary button on the left, the secondary button to the right of it.

## Key properties
**[OnSelect](../properties-core.md)** – Actions to perform when the user taps or clicks a control.

**[Text](../properties-core.md)** – Text that appears on a component.

**BasePaletteColor** - The color palette applied to a control. This impacts all surfaces of the control that render a theme color. If the value is null or zero, then the color is driven by selected Fluent theme.

**Appearance** – A button can have its content and borders styled for greater emphasis or to be subtle. Below are the options available:
* Primary: Emphasizes the button as a primary action.
* Secondary: Gives emphasis to the button in such a way that it indicates a secondary action.
* Outline: Removes background styling.
* Subtle: Minimizes emphasis to blend into the background until hovered or focused.
* Transparent: Removes background and border styling.

**FontSize** - The font size of the text that appears on a control. If the value is null or zero, then the font size is driven by selected Fluent theme.

## Additional properties
**AccessibleLabel** – Label for screen readers.

**DisplayMode** – Whether the control allows user input (Edit), only displays data (View), or is disabled (Disabled).

**Visible** - Whether a control appears or is hidden.

**[X](../properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](../properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

**[Size](../properties-text.md)** – The size of the control on the canvas













