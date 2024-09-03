---
title: Add and navigate screens in Power Apps canvas apps
description: Learn how to add screens to your canvas app, use arrows to navigate between them, reorder the screens, and set the start screen.
author: emcoope-msft
ms.author: emcoope
ms.date: 06/06/2024
ms.topic: conceptual
ms.subservice: canvas-maker
search.audienceType: 
  - maker
contributors:
  - mduelae
ai-usage: ai-assisted
ms.custom:
  - canvas
  - ai-gen-diyeditor
---

# Add and navigate screens in Power Apps canvas apps

Create modern, responsive apps by adding prebuilt screens for common app scenarios. The screens feature responsive containers and modern controls that adapt to different screen sizes. You can also add custom screens with different layouts and controls.

:::image type="content" source="./media/add-screen-context-variables/add-a-screen.png" alt-text="Screenshot of the New screen menu in Power Apps Studio showing available layouts.":::

The following new prebuilt screens are available:

- [Welcome screen](add-screen-context-variables.md#welcome-screen)
- [Header and gallery](add-screen-context-variables.md#header-and-gallery-screen)
- [Approval request](add-screen-context-variables.md#approval-request-screen)
- [Header and form](add-screen-context-variables.md#header-and-form)
- [Header and table](add-screen-context-variables.md#header-and-table)

## Add a new screen

1. Sign in to [Power Apps](https://make.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).

1. Create a canvas app or open one for editing.

1. On the command bar, select **New screen**, and then select a screen layout.

1. Preview the app to determine how it looks on different devices. Learn more in [Preview an app](preview-app.md).

To make the app adapt to the size of the device display it's being run on, turn off the **[Scale to fit](create-responsive-layout.md#disable-scale-to-fit)** option.

## Welcome screen

The **Welcome screen** is ideal for the first screen of an app. It has tiles that you can customize with an image, a title, and a description. Change the number of tiles by adding or removing them in the body container. Use the tiles to navigate users to other parts of the app.  

The **Welcome screen** has the following controls:

- Header container
  - Header
- Body container
  - Container
    - Image container
      - Image (classic)
    - Title container
      - Feature item button
      - Text

### Add and customize the Welcome screen

1. Select **New Screen** > **Welcome screen**.

1. To change the image, select it and then select **Edit**.

1. Select the **Feature Item** button control and add your own text.

1. Select the **Short description or engaging message** text and add your own.

1. Add and remove tiles as needed.

    - To add tiles, in the tree view, copy and paste a **Container** item.

    - To remove a tile, in the tree view, right-click a **Container**, and then select **Delete**.  

## Header and gallery screen

Use the **Header and gallery** screen to show a range of product or service information, like a product catalog. When you connect a gallery control to a data source, a catalog is automatically created with little customization required.

The [gallery control](controls/control-gallery.md) in the **Header and gallery** screen is a classic control. When the modern gallery control is released, the **Header and gallery** screen will use it. Learn more in [Overview of modern controls and themes in canvas apps](controls/modern-controls/overview-modern-controls.md).

The **Header and gallery** screen has the following controls:

- Header container
  - Header
- Main container
  - Gallery (classic)
    - Image container
      - Image (classic)
  - Title container
    - Title text
    - Description text
  - Button container
    - Button

### Add and customize the Header and gallery screen

1. Select **New Screen** > **Header and gallery**.

1. In the tree view, select **Gallery** and connect it to a data source such as Dataverse.

1. Select specific controls inside the gallery, such as the image, title text, and text description. In the control's properties, use the *ThisItem* syntax to set the desired image, title text, and description.

## Approval request screen

The **Approval request** screen has a header, a form with a submit button, and a gallery with predefined stages. The **Approval request** screen is useful for scenarios where actions are triggered by form submissions, such as submitting an approval request or displaying a workflow process for a business.

The **Approval request** screen has the following controls:

- Header container
  - Header
- Main container
  - Form container
    - Form title text
    - Approval form
    - Submit button
  - Sidebar container
    - Text
    - Gallery (classic)

### Add and customize the Approval request screen

1. Select **New Screen** > **Approval request**.

1. In the tree view, select **Approval form** and connect it to a data source such as Dataverse.

1. To view the details of the approval stages, in the tree view, select **ReviewersGallery**. Then in the properties pane, select the **Advanced** tab and go to **Items**.

    The approval stages have the following details:
   - **Name**: Name of the stage or approver
   - **Title**: Subtitle of the stage or approver
   - **Status**: Stage status
   - **Current**: Whether this is the current stage of the approval request

You can add a Power Automate approval workflow in the button to notify the approver. Learn more in [Create and test an approval workflow with Power Automate](/power-automate/modern-approvals).

## Header and form

The **Header and form** screen has a header, a form, and two buttons to submit the form and cancel form submission. This screen is great for using a full-screen form.  

The **Header and form** screen has the following controls:

- Header container
  - Header
- Main container
  - Form container
    - Form  
  - Button container
    - Cancel button
    - Submit button

### Add and customize the Header and form screen

1. Select **New Screen** > **Header and form**.

1. In the tree view, select **Form** and connect it to a data source.

1. Optionally, to ensure the best screen responsiveness, select each data card on the form and set its **Width Fit** property to **On** in the **Properties** pane.

## Header and table

The **Header and table** screen has two controls, a header control and a table control. This template is great for showing a detailed data table on a screen.

The **Header and table** screen has the following controls:

- Header container
  - Header
- Main container
  - Table

### Add and customize the Header and table screen

1. Select **New Screen** > **Header and table**.

1. In the tree view, select **Table** and connect it to a data source.

## Reorder screens

When you have more than one screen in your app, you can put them in a different order.

In the left pane, point to a screen that you want to reorder, and then select **Move up** or **Move down**.

Use the **[StartScreen](/power-platform/power-fx/reference/object-app#startscreen-property)** property to set the screen to be displayed first.

## Add navigation

When you have more than one screen in your app, you can add navigation so that your users can move between them.

1. With the screen selected, select **Insert**. In the search box, type **Next arrow** and then select it.

1. Move the arrow to where you want it to appear on the screen.

1. With the arrow selected, set the **[OnSelect](controls/properties-core.md)** property to the **Navigate** function; for example, **Navigate(*Target*, Fade)**.

    Replace *Target* with the name of the screen you're navigating to.

    :::image type="content" source="./media/add-screen-context-variables/onselect-default.png" alt-text="Screenshot of the OnSelect property set to the Navigate function.":::

    In this example, when a user selects the arrow, the *Target* screen fades in.

1. On the *Target* screen, add a **Back arrow** icon the same way. Set its **[OnSelect](controls/properties-core.md)** property; for example, **Navigate(*Target*, ScreenTransition.Fade)**.

    Replace *Target* with the name of the screen you're navigating to.

## Related information

- [Screen-control reference](controls/control-screen.md)
