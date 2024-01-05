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
  
---
# Header modern control in Power Apps 

A control that creates a modern app header.

## Description

The **Header** control is a fundamental control that lets you design a user interface for a common app with ease. With minimal configuration, this control responds to themes that use modern theming and dynamic responsiveness, adjusting to the size of the parent container or app. The **Header** control supports a logo, a page title, and displays the user picture, while providing a variety of unique style options.


## Key properties

**ThemeStyle** – Header color variant, based on theme colors.

**Base palette color** - The color palette applied to a control. This impacts all surfaces of the control that render a theme color. This property has no effect if the **ThemeStyle** property is set to **Neutral**.    

**Logo** – The image displayed in the header. 

**IsLogoVisible** – Whether the logo image is displayed. 

**Title** – The title label displayed in the header. Default value is the current screen name. 

**IsTitleVisible** – Whether the title is displayed in the header.

**IsProfilePictureVisible** – Whether the user picture is displayed in the header. By default, a picture of the current user using the app is shown. 


## Unsupported capabilities

The following features aren't supported:

- Customization of colors 
- App navigation

> [!NOTE]
> This list will change over time as we're working to support these capabilities.

The header doesn't automatically replicate across app screens, so it needs to be manually added to each screen.

