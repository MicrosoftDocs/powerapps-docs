---
title: Header modern control in Power Apps
description: Learn about the details, properties and examples of the header modern control in Power Apps.
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
# Header modern control in Power Apps (preview)

[This article is pre-release document and is subject to change.]

A control that creates a modern app header.

## Description

The **Header** control is a fundamental control that lets you create a common app user interface design with minimal configuration. This control lets you to generate themes that incorporate contemporary theming and dynamic responsiveness, adapting to the size of the parent container or app. The Header control supports a logo, a page title, and displays the user's current picture, while providing a range of distinct style options.


## Key properties

**ThemeStyle** – Header color variant, based on theme colors.

**Logo** – The image displayed in the header. 

**IsLogoVisible** – Whether the logo image is displayed. 

**Title** – The title label displayed in the header. Default value is the current screen name. 

**IsTitleVisible** – Whether the title is displayed in the header.

**IsProfilePictureVisible** – Whether the user picture is displayed in the header. By default, picture of the current user using the app is shown. 


## Unsupported capabilities

Support for the following features is expected in the future: 

- Customization of colors 
- App navigation 

Currently the header does not automatically replicate across app screens, and needs to be manually added to each screen.

