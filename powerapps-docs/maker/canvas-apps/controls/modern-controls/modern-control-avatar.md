---
title: Avatar modern control in Power Apps
description: Learn about the details, properties, and examples of the avatar modern control in Power Apps.
author: jasongre

ms.topic: reference
ms.component: canvas
ms.date: 05/20/2023
ms.subservice: canvas-maker
ms.author: jasongre


ms.reviewer: mkaur
search.audienceType: 
  - maker
contributors:
  - jasongre
     
---
# Avatar modern control in Power Apps (preview)

[This article is prerelease documentation and is subject to change.]

A control that shows a graphic representation of a user, team, or entity.  

## Description

Use the avatar control to visually represent a user, team, or entity. This control supports both image and initials formats and allows a small badge to be included to help convey status. The key properties for this control are **Name** and **Image**.  

## General

**Name** - The name of the person or entity. Name is used to determine the initials displayed when there's no image and is also used for accessibility. 

**Image** – The visual representation for the person or entity.

**Badge** – A small visual decoration added to convey status of the person or entity. 

**Visible** - Whether a control appears or is hidden.

## Size and position 

**[X](../properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](../properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

**Width** - The distance between a control's left and right edges. 

**Height** - The distance between a control's top and bottom edges. 

## Style and theme

**Shape** - Whether the avatar appears with a circular or square shape. 

**Appearance** – An avatar can have portions of itself styled for greater emphasis or to be subtle. 

The following options are available:

- **Brand**: Uses the modern theme to style the avatar. The Color palette property can be used to override this color scheme. 
- **Neutral**: Uses a grayscale for the initials background to provide a subtle appearance.
- **Colorful**: Users a color from a predefined set of colors, based on a hash of the provided Name. 

**BasePaletteColor** - The color palette applied to a control. This impacts all surfaces of the control that render a theme color. If the value is null or zero, then the color is driven by the selected Fluent theme.

**Font** - The name of the family of fonts in which text appears.

**FontSize** - The font size of the text that appears on a control. If the value is null or zero, then the font size is driven by selected Fluent theme.

**FontColor** - The color of text in a control. 

**FontWeight** - The weight of the text in a control: **Bold**, **Lighter**, **Normal**, or **Semibold**. 

**FontItalic** - Whether the text in a control is italic. 

**FontUnderline** - Whether a line appears under the text that appears on a control. 

**FontStrikethrough** - Whether a line appears through the text that appears on a control. 

## Additional properties

**Out of office** - Adjusts the Badge icon to show its corresponding "out of office" variant.  










