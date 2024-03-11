---
title: Use inline actions when you're building  a canvas app
description: Learn how to use inline actions while you’re building a canvas app in Power Apps Studio.
author: tashaev
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: mkaur
ms.date: 03/09/2024
ms.subservice: canvas-maker
ms.author: tashas
search.audienceType: 
  - maker
contributors:
  - mduelae
  - tashas
  
---

# Use inline actions in Power Apps Studio 

Use inline actions to update layouts, work with data, collaborate with your colleagues, and use Copilot directly on the canvas for specific controls. This means you can build and modify your app without navigating away from your current view in Power Apps Studio. This provides a more streamlined and efficient way to work.

## Use Copilot in the formula bar

Use Copilot inline to help you write Power Fx formulas. Use Copilot to apply conditional formatting, sort and filter your data, and more with the help of Power Apps Ideas. The Copilot button appears where applicable, offering suggestions for supported controls such as **Gallery**, **Data table**, **Text input**, **Drop down**, **Combo box**, and **Text label**. For more information, see [Power Apps Ideas](power-apps-ideas.md).

:::image type="content" source="media/inline-actions/inline-actions-power-fx.png" alt-text="Inline actions for Power Fx formulas":::

## Choose a layout

Use inline actions to select layout options for certain controls to create the look you want.

### Blank screen template

Use inline actions to apply a layout to blank screens. 

Add a blank screen, select **Templates** and then select a new layout. 

> [!NOTE]
> Once you add content to a screen, the **Templates** button won't be available.

:::image type="content" source="media/inline-actions/inline-actions-screen-template.png" alt-text="Use inline actions to select a screen template":::

### Gallery control (classic) layouts

Add a gallery control and then use the **Layout** button to change the layout for the control. Different layout options appear when you add  a **Vertical gallery** or **Horizontal gallery**.

When you add or remove controls after applying a layout, changing the layout removes your customizations.

:::image type="content" source="media/inline-actions/inline-actions-gallery-layout.png" alt-text="Use inline actions to select a layout":::

### Form control (modern or classic) layouts

On a **Form** control (modern or classic), you need to connect it to a data source and then the **Layout** button appears in the inline actions. Use the layout option to choose whether labels and inputs are arranged together vertically or horizontal.

- Select the **Vertical** layout to place the label above the corresponding input control.
- Select the **Horizontal** layout to place the label to the left of the input control.

## Add Data and Fields

Maintain your workflow using the inline actions to bind data to a control and then add fields.

:::image type="content" source="media/inline-actions/inline-actions-data-fields.png" alt-text="Add Data and Fields using the inline actions":::

### Gallery, Table, and Form

 When you add a gallery, **Table**, or **Form** control, the **Data** button is automatically selected. You can then add a data source to the control. Once the data source is added, the control displays the data.

 Use the **Fields** button to select which fields are shown on the control from the selected data source.

 In a **Table** control, you can drag and drop the fields to change the order that they appear in the table.

In a **Form** control, if you choose a new data source, you're prompted to replace the data card. When you confirm your selection, it removes any customizations and generates a new form with fields corresponding to the new data source.  

You can always access the **Data** and **Fields** buttons in the inline actions to modify the information used in the gallery or **Table**  control.

## Add comments

Comments allow you to tag peers in your app to ask questions, leave instructions, and propose next steps. You can add and read
comments on a screen and any control from the inline actions.  

The following images show how the comment button looks when there's no comment and when a comment is added.

- Comment button when there's no comment: :::image type="content" source="media/inline-actions/no-comment.png" alt-text="No comment has been added":::
- Comment button when a comment is added: :::image type="content" source="media/inline-actions/comment-added.png" alt-text="Comment button when there's a comment":::

 When you select **Comments** it opens the **Comments** pane so you can add and view comments.
