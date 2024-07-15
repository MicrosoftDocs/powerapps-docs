---
title: Link modern control in Power Apps
description: Learn about the details, properties, and examples of the link modern control in Power Apps.
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
# Link modern control in Power Apps

Open hyperlinks in new tab.

## Description
Use **Link** control to provide links that can be defined with accessibility compliance. The link opens in a new tab on your device. The key properties for this control are **Text** and **URL**. 

## General

**Text** – The text to be displayed on the app with link enabled.

**URL** - URL for the users to navigate through the link.

**AccessibleLabel** – Label for screen readers.

**Visible** - Whether a control appears or is hidden.

## Behavior 

**Wrap** - Whether the text should ever wrap to multiple lines.

**DisplayMode** – Whether the control allows user input (Edit), only displays data (View), or is disabled (Disabled).

## Size and position 

**Align** - The location of text in relation to the horizontal center of its control. The options are updated to **Start**, **End**, **Center**, and **Justify** to better accommodate left to right languages.

**VerticalAlign** - – The location of text on a control in relation to the vertical center of that control.

**AutoHeight** - Whether a label automatically increases its Height property if its Text property contains more characters than the control can show at one time.

**[X](../properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](../properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

**Width** - The distance between a control's left and right edges. 

**Height** - The distance between a control's top and bottom edges. 

## Style and theme

**BasePaletteColor** - The color palette applied to a control. This impacts all surfaces of the control that render a theme color. If the value is null or zero, then the color is driven by selected Fluent theme.

**Font** - The name of the family of fonts in which text appears. 

**FontSize** - The font size of the text that appears on a control. If the value is null or zero, then the font size is driven by selected Fluent theme.

**FontWeight** - The weight of the text in a control: Bold, Lighter, Normal, or Semibold. 

**FontItalic** - Whether the text in a control is italic. 

**FontStrikethrough** - Whether a line appears through the text that appears on a control. 

**FontUnderline** - Whether a line appears under the text that appears on a control. 

## Additional properties

**[AcceptsFocus](../properties-accessibility.md)** - Determines whether the control can receive focus when the user navigates through the app using the keyboard. 



