---
title: Text input modern control in Power Apps
description: Learn about the details, properties, and examples of the text input modern control in Power Apps.
author: yogeshgupta698

ms.topic: reference
ms.component: canvas
ms.date: 1/16/2025
ms.subservice: canvas-maker
ms.author: yogupt


ms.reviewer: mkaur
search.audienceType: 
  - maker
contributors:
  - clromano
  - mduelae
  - yogeshgupta698
  - noazarur-microsoft
  
---
# Text input modern control in Power Apps

A box in which the user can type text, numbers, and other data.

## Description
The user can specify data by typing into a **Text input** control. Depending on how you configure the app, that data might be added to a data source, used to calculate a temporary value, or incorporated in some other way. The key properties for this control are **Value**, **Mode**, and **ValidationState**.

## General

**PlaceHolder** - Instructional text that appears if no dates are entered. 

**AccessibleLabel** – Label for screen readers.

**Visible** - Whether a control appears or is hidden. 

## Behavior

**Mode** – The control is in **SingleLine** or **MultiLine** mode.

**Type** – The type of text that that is entered such as text, password, or search. 

**DisplayMode** – Whether the control allows user input (Edit), only displays data (View), or is disabled (Disabled).

**TriggerOutput** - When the control updates its **Value** and triggers OnChange.

- Delayed - Update the control's value when the user pauses typing.
- FocusOut - Update the control's value when the user selects a different control or clicks outside the control.
- Keypress - Update the control's value immediately on every character input.

## Size and position 

**[X](../properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](../properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

**Width** - The distance between a control's left and right edges. 

**Height** - The distance between a control's top and bottom edges. 

## Style and theme

**BasePaletteColor** - The color palette applied to a control. This impacts all surfaces of the control that render a theme color.  

**Font** - The name of the family of fonts in which text appears. 

**FontSize** - The font size of the text that appears on a control. If the value is null or zero, then the font size is driven by selected Fluent theme. 

**FontColor** - The color of text in a control. 

**FontWeight** - The weight of the text in a control: Bold, Lighter, Normal, or Semibold. 

**FontItalic** - Whether the text in a control is italic. 

**FontUnderline** - Whether a line appears under the text that appears on a control. 

**FontStrikethrough** - Whether a line appears through the text that appears on a control. 

**Align** -The location of text on a control in relation to the vertical center of that control. 

## Additional properties

**Value** – The initial value of a control before it's changed by the user.

**Required** – Must fill in field or not.

**DelayOutput** - When set to true, user input is registered after half a second delay. Useful for delaying expensive operations until user completes inputting text such as for filtering when input is used in other formulas.

**MaxLength** - The number of characters that the user can type into a text-input control. 

**OnChange** - Actions to perform when the user changes the value of a control.  

**ValidationState** - The control has two states, which are **Error** and **None**. When the error state is selected the control’s border is highlighted in red.


