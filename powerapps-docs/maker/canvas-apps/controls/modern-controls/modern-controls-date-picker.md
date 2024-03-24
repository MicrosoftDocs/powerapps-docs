---
title: Date picker control in Power Apps
description: Learn about the details, properties, and examples of the date picker modern control in Power Apps.
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
# Date picker control in Power Apps (preview)

[This article is pre-release document and is subject to change.]

A control that the user can select to specify a date.

## Description
If you add a Date Picker control instead of a Text input control, you help ensure that the user specifies a date in the correct format. The key properties for this control are **Format**, **ValidationState**, and **OnChange**.

## General

**PlaceHolder** - Instructional text that appears if no dates are entered. 

**Format** – The text format in which the control shows the date the user specified. The format of the date can be short, LongAbbreviated, or YearMonth. For example: 

-  Short - 2/1/2024 

-  LongAbbreviated - Thurs, Feb 1, 2024 

-  YearMonth - February 2024 

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

**Font** - The name of the family of fonts in which text appears. 

**FontSize** - The font size of the text that appears on a control. If the value is null or zero, then the font size is driven by selected Fluent theme. 

**FontColor** - The color of text in a control. 

**FontWeight** - The weight of the text in a control: **Bold**, **Lighter**, **Normal**, or **Semibold**

**FontItalic** - Whether the text in a control is italic. 

**FontUnderline** - Whether a line appears under the text that appears on a control. 

**FontStrikethrough** - Whether a line appears through the text that appears on a control. 

## Additional properties

**Required** – You can mandate the date picker as required field in a context.

**EndDate** - The latest date to which the user can set value of a date-picker control. 

**IsEditable** - Whether the Date Picker text can be edited. If false, the date can only be changed by using the calendar. 

**OnChange** – Actions to perform when the user changes the value of a control. 

**SelectedDate** - The date currently selected in a date control. This date is represented in local time. 

**StartDate** - The earliest date to which the user can set the value of a date-picker control. 

**StartOfWeek** - The day of the week to display in the first day column of the date-picker control. 

**ValidationState** - The control has two states, which are **Error** and **None**. When the error state is selected the date picker border is highlighted in red. 



