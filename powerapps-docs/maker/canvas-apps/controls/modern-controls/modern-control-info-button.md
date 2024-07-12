---
title: Information button modern control in Power Apps
description: Learn about the details, properties, and examples of the information button modern control in Power Apps.
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
# Info button modern control in Power Apps (preview)

[This article is pre-release document and is subject to change.]

Use **Info button** control to provide additional information to users.

## Description
**Info button** control enables developers to provide help and guidance to app users in an accessible way. The key properties for this control are **Content**, **Icon Siz**e, and **OnSelec**.

## General 

**Content** – Content to be displayed when users interact with the control.

**AccessibleLabel** – Label for screen readers.

**Visible** - Whether a control appears or is hidden. 

## Size and position

**IconSize** - Whether the information icon is small, medium, or large.

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

**DisplayMode** – Whether the control allows user input (Edit), only displays data (View), or is disabled (Disabled).

**[AcceptsFocus](../properties-accessibility.md)** - Determines whether the control can receive focus when the user navigates through the app using the keyboard. 

**OnSelect** - Actions to perform when the user selects a control.  




