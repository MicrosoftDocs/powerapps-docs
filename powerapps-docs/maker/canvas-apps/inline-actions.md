---
title: Use inline actions when you're buiding a canvas app
description: Learn how to use inline actions while you’re building a canvas app in Power Apps Studio.
author: tashaev
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: mkaur
ms.date: 03/08/2024
ms.subservice: canvas-maker
ms.author: tashas
search.audienceType: 
  - maker
contributors:
  - mduelae
  - tashas
  
---

# Use inline action bar in Power Apps Stuido

The inline action bar is a feature that lets you to update layouts, work with data, collaborate with your colleagues, and use Copilot directly on the canvas for specific controls. This means you can make changes and interact without leaving the context of your current view while editing a canvas app in Power Apps Studio.


## Use Copilot in the formula bar

 Use Copilot in the inline actions to help you write Power Fx formulas. USe Copilot to apply conditional formatting, sort and filter your data, and more with the help of Power Apps Ideas. The Copilot button appears where applicable, offering suggestions for supported controls such as **Gallery**, **Data table**, **Text input**, **Drop down**, **Combo box**, and **Text label**. For more information, see [Power Apps Ideas here](power-apps-ideas.md).

:::image type="content" source="media/inline-actions/inline-actions-power-fx.png" alt-text="Inline actions for Power Fx formulas":::

## Choose a layout

Use the inline actions to select layout options for certtain controls to create the look you want.

### Blank screen template

Use the inline actions to apply a layout to blank screens. 

Add a blank, select **Templates** and then select a new layout. 

> [!NOTE]
> When a screen has content the **Templates** button isn't available anymore.

:::image type="content" source="media/inline-actions/inline-actions-screen-template.png" alt-text="Use inline actions to select a screen template":::

### Gallery control (classic) layouts

Add a gallery control and then use the the **Layout** button to change the layout for the control. Different layout options appear depending on whether you add a **Vertical gallery** or **Horizonal gallery**. When you add or remove controls after applying a layout, changing the layout will remove your customizations.  

:::image type="content" source="media/inline-actions/inline-actions-gallery-layout.png" alt-text=""Use inline actions to select a layout":::

### Form control (modern or classic) layouts

When you add a **Form** control (modern or classic) the **Layout** button appears in the inline actions once you add data source. Use the layout option to choose whether labels and inputs are arranged together vertically or horizontal.

- Select the **Vertical** layout to place the label above the corresponding input control.
- Select the **Horizontal** layout to place the label to the left of the input control.

## Add Data and Fields 

Maintain your workflow using the inline actions to bind data to a control and add fields.

:::image type="content" source="media/inline-actions/inline-actions-data-fields.png" alt-text="Add Data and Fields using the inline actions":::

### Gallery, Table, and Form

 When you add a gallery, **Table**, or  **Form** control, the **Data** button is automatically selected. This allows you to choose and add a data source to the control. Once the data source is added, the contorl displays the data.

 Use the **Fields** button to select which fields are shown on the control from the seleted data source. 

 In a **Table** control, you can drag and drop the fields to change the order they appear in the table.

In a **Form** control, if you choose a new data source, you’ll be prompted to replace the data cards. When you confirm this option it will remove any customizations and generate a new form with fields corresponding to the new data source.  

The **Data** and **Fields** buttons is always available in the inline actions to update the data used in the gallery or **Table** control.

## Comments 

Comments allow you to tag peers in your app to ask questions, leave instructions, and propose next steps. You can add and read 
comments on a screen and any control from the inline actions.  


The sceenshot shows how the comment button will look when there is no comment or when a comment is added.

- Comment button when there's no comment: :::image type="content" source="media/inline-actions/no-comment.png" alt-text="No comment has been added":::
- Comment buttton when a commemnt is added: :::image type="content" source="media/inline-actions/comment-added.png" alt-text="Comment button when there's a comment":::

 When you select **Comments** it opne the **Comments** pane so you can add and view comments.