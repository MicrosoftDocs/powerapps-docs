---
title: Button modern control in Power Apps
description: Learn about the details, properties, and examples of the button modern control in Power Apps.
author: yogeshgupta698

ms.topic: reference
ms.component: canvas
ms.date: 7/10/2024
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
# Button modern control in Power Apps

A control that the user can select to interact with the app.

## Description
Use the modern button to set a button to be primary or secondary. Configure the **[OnSelect](../properties-core.md)** property of a **Button** control to run one or more formulas when the user selects the control. As a design pattern, we recommend always placing the primary button on the left, the secondary button to the right of it. The key properties for this control are **OnSelect** and **Text**.

## General

**[Text](../properties-core.md)** – Text that appears on a component.

**AccessibleLabel** – Label for screen readers.

**Visible** - Whether a control appears or is hidden.

## Add an icon to a button control

The button control now includes subset of Fluent icons. The following properties are available:

**Icon** - The button control now allows you to enhance its visual appeal by including Fluent icons. In the properties pane, select the desired icon from a dropdown menu that displays all available options.

> [!div class="mx-imgBorder"]
> ![List of icons](media/Icons-List.png)

**Layout** - Defines the positioning of the icon in relation to the text on the button or no icon at all.

**Icon Rotation** - Provides the ability to rotate the icon to a desired orientation.

**Icon Style** - Provides option for icon to be rendered in filled or outline state.

## Behavior

**DisplayMode** – Whether the control allows user input (Edit), only displays data (View), or is disabled (Disabled).

## Size and position 

**[X](../properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](../properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

**Width** - The distance between a control's left and right edges. 

**Height** - The distance between a control's top and bottom edges. 

## Style and theme

**Appearance** – A button can have its content and borders styled for greater emphasis or to be subtle. Below are the options available:
* Primary: Emphasizes the button as a primary action.
* Secondary: Gives emphasis to the button in such a way that it indicates a secondary action.
* Outline: Removes background styling.
* Subtle: Minimizes emphasis to blend into the background until hovered or focused.
* Transparent: Removes background and border styling.

**BasePaletteColor** - The color palette applied to a control. This impacts all surfaces of the control that render a theme color. If the value is null or zero, then the color is driven by selected Fluent theme.

**Font** - The name of the family of fonts in which text appears.

**FontSize** - The font size of the text that appears on a control. If the value is null or zero, then the font size is driven by selected Fluent theme.

**FontColor** - The color of text in a control. 

**FontWeight** - The weight of the text in a control: **Bold**, **Lighter**, **Normal**, or **Semibold**. 

**FontItalic** - Whether the text in a control is italic. 

**FontUnderline** - Whether a line appears under the text that appears on a control. 

**FontStrikethrough** - Whether a line appears through the text that appears on a control. 

## Additional properties

**[AcceptsFocus](../properties-accessibility.md)** - Determines whether the control can receive focus when the user navigates through the app using the keyboard. 

**[OnSelect](../properties-core.md)** – Actions to perform when the user selects a control.













