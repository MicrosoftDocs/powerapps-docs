---
title: Header modern control in Power Apps
description: Learn about the details, properties, and examples of the header modern control in Power Apps.
author: yogeshgupta698

ms.topic: reference
ms.component: canvas
ms.date: 10/02/2023
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
# Header modern control in Power Apps 

A control that creates a modern app header.

## Description

The **Header** control is a fundamental control that lets you design a user interface for a common app with ease. With minimal configuration, this control responds to themes that use modern theming and dynamic responsiveness, adjusting to the size of the parent container or app. The **Header** control supports a logo, a page title, and displays the user picture, while providing various unique style options. The key properties for this control are **Logo**, **OnSelectLogo**, and **Title**.


## General

**Title** – The title label displayed in the header. Default value is the current screen name. 

**IsTitleVisible** – Whether the title is displayed in the header.

**Logo** – The image displayed in the header. 

**IsLogoVisible** – Whether the logo image is displayed. 

**IsProfilePictureVisible** – Whether the user picture is displayed in the header. By default, a picture of the current user using the app is shown. 

**Visible** - Whether a control appears or is hidden. 

## Size and position

**X** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container). 

**Y** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container). 

**Width** - The distance between a control's left and right edges.  

**Height** - The distance between a control's top and bottom edges.

## Style and theme

**BasePaletteColor** - The color palette applied to a control. This impacts all surfaces of the control that render a theme color. This property has no effect if the **ThemeStyle** property is set to **Neutral**.    

**Style** – Header color variant, based on theme colors. 

**Font** - The name of the family of fonts in which text appears. 

**TitleFontSize** - The font size of the title that appears on a control. If the value is null or zero, then the font size is driven by selected Fluent theme. 

**FontColor** - The color of text in a control.

## Additional properties 

**DisplayMode** – Whether the control allows user input (Edit), only displays data (View), or is disabled (Disabled).  

**LogoMaxHeight** – The maximum height the logo can be placed within the control. 

**LogoToolTip** - Tooltip for the logo.  

**OnSelectLogo** - Actions to perform when the user selects the logo. 


## Unsupported capabilities

The following features aren't supported:

- Customization of colors 
- App navigation

> [!NOTE]
> This list will change over time as we're working to support these capabilities.

The header doesn't automatically replicate across app screens, so it needs to be manually added to each screen.

