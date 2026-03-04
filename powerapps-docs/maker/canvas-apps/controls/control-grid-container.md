---
title: Grid container control in Power Apps
description: Learn about the details, properties and examples of the grid container control in Power Apps.
author: shivanichander
ms.topic: reference
ms.custom: canvas
ms.reviewer: mkaur
ms.date: 12/16/2025
ms.subservice: canvas-maker
ms.author: shivchan
search.audienceType: 
  - maker
contributors:
  - mduelae
  - shivchan

---
# Grid container control in Power Apps (preview)

[This article is a pre-release document and is subject to change.]

The **Grid container** control gives you a way to **layout child components in a grid pattern**. You get precise control over where each component goes in terms of rows and columns.

This container works like CSS-style grids. You define the **rows and columns** and set the exact position for each child component using its properties.

> [!IMPORTANT]
>
> - This feature is in preview.  
> - Preview features aren't meant for production use and might have restricted functionality These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?linkid=2189520), and are available before an official release so that customers can get early access and provide feedback.
> - This feature is in the process of rolling out and might not be available in your region yet.


## Description

The **Grid container** control offers a flexible layout system for canvas apps. It enables you to:

- Place child components in a **grid pattern**
- Specify the **row and column start and end** for each child
- Make responsive adjustments when the container or screen size changes
- Control alignment, spacing, and overflow within the grid

By using this approach, you don't need to manually position each component. Your apps become **more maintainable and responsive**.


## Display properties

- **Gap** – The spacing in pixels between child components inside the grid.
- **Columns** – The number of columns in the grid layout.
- **Rows** – The number of rows in the grid layout.

## Size and position

- **X** – The horizontal distance from the left edge of the parent container (or screen if no parent).
- **Y** – The vertical distance from the top edge of the parent container (or screen if no parent).
- **Width** – The distance between a control's left and right edges.
- **Height** – The distance between a control's top and bottom edges.
- **Padding** - The spacing between the container edges and its child components.

## Color and border

- **Color** – Foreground color of the container, used for borders and text if applicable.
- **Border**
  - **Style** – Type of border: Solid, Dashed, Dotted, or None.
  - **Thickness** – Width of the border in pixels.
  - **Color** – Color of the border.
- **Border radius** – The degree to which the corners of the container are rounded. You can apply this setting to all corners uniformly or split it into individual corners in advanced settings.
- **Drop shadow** – Shadow effect applied to the container. Options: None, Light, Medium, or Heavy.

## Visibility

- **Visible** – Whether the grid container is displayed. Toggle **On** or **Off**.

## Grid layout properties (child-specific)

- **Column Start / Column End** – Defines the starting and ending columns for a child component.
- **Row Start / Row End** – Defines the starting and ending rows for a child component.

## Example

1. [Create a blank canvas app from scratch](../create-blank-app.md) with a **Responsive** layout.
1. Create a new screen.
1. From the **Insert** pane under **Layout**, select **Grid container**.
1. Set container properties to occupy the full screen:  
   - X = 0  
   - Y = 0  
   - Width = Parent.Width  
   - Height = Parent.Height

1. Add several child components, such as buttons, text inputs, icons, and media. For each child, set grid placement properties:  
   - Column Start / End  
   - Row Start / End  
   - Align in Cell

1. Press **F5** to preview. Resize the screen and observe how child components **remain in their grid positions** and adjust responsively.



