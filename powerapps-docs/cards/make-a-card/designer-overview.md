---
title: Card Designer overview (Preview)
description: Learn about the designer and how to create cards using it.
ms.date: 09/20/2022
ms.topic: article
author: iaanw
ms.author: iawilt
manager: shellyha
ms.reviewer: 
ms.custom: 
ms.collection: 
---

# Card Designer overview (Preview)

[!INCLUDE[cards_preview_notice](../includes/preview-include.md)]

The Card Designer is where makers and developers can build cards to suit their needs. The designer lets you optimize and automate business user tasks and create actionable scenarios in interactive and easy-to-make cards. The designer builds off of the designer for Adaptive Cards, introducing a few new concepts:

- Power Fx: specify an action to trigger when an element is selected
- Connectors: bring data into cards (currently only from Dataverse)
- Variables: store, bind, and reuse data across a card
- Dataverse: stores each card you create and allows you to retrieve the card at send time

## Find the designer

To get to the designer, take the following steps:

1. Go to [Power Apps](https://make.powerapps.com) and make sure you're in the correct environment.

1. Go to the pane on the left to access all of the card-related views.

   1. To create a new card, select **Cards** then **Create**.
   1. To see all current cards, select **Cards** then **Cards**

      :::image type="content" source="../media/designer-overview/create-new-card.png" alt-text="Screenshot showing card creation screen." border="false":::

1. Select the **+ Create a card** to start building your own card.

## What's in the designer?

The designer is made up of the following elements:

:::image type="content" source="../media/designer-overview/designer-elements.png" alt-text="Screenshot of Card Designer with elements highlighted." border="false":::

1. Main menu
1. Tool pane
1. Card canvas
1. Property pane
1. Formula bar
1. Play button

The sections below describe each of the designer elements.

### Main menu

The main menu lets you switch between the different tools available in the designer. In order, these are:

- Tree View: see the card as a hierarchical outline and view the relationships of the card elements.
- Insert: main UI for editing and adding card elements.
- Data: add connectors to your card to use data from external sources.
- Variables: store, bind, and reuse data across a card.

### Tool pane

When you start making your card, you'll use items from the Tool pane. There are three categories of items in the pane:

- Display: Add text and media to cards.
- Input: Add different types of input boxes to collect information from users.
- Layout: Add formatting and customize your card's structure.

### Card canvas

The card canvas is where where you build the user interface for your card, using connectors, variables, and elements from the Tool pane.

You can't resize a card in the card canvas view because cards automatically fit themselves to the location they're placed into.

### Property pane

The property pane is used to change up specific properties for an element. Each type of element has its own property pane, including the card itself. For most of the drag-and-drop elements, you'll be able to specify things like:

- **Name**: the variable name associated with that element, which you can reference in a Power Fx formula
- **Label**/**Text**: any text the user will see when they load in the card
- **Default value**: the initial value of a field
- **Initially visible**: choose if the element will be visible on load

Certain elements have visual aspects that you can modify. For text labels and input controls, for example, you can customize font, color, spacing, and more.

Each property pane also contains advanced features, which allow you to specify things like:

- **Repeat for every**: provide a trigger for if/when an element should be repeated
- **Show when**: provide a trigger to show the element
- **Requires**: make the element dependent on certain features, corresponding with a minimum version

You can also input Power Fx expressions into the properties, utilizing low-code solutions to make your card more powerful.

### Power Fx editor

The formula bar at the top of the card designer and allows you to write Power Fx expressions. When you select an element on the card, the formula bar lets you select a property of that element from the dropdown that supports a code input and then assists you in writing an expression. Intellisense will also pull in any variables you've defined, and specific functions based on the data connections you've made.

To get started with Power Fx, see [Introduction to Power FX](../make-a-card/power-fx/intro-to-pfx.md). For more information on the specific functions you can use, see the Microsoft documentation for [Formula reference for Power Apps](/powerapps/maker/canvas-apps/formula-reference).

> [!NOTE]
> Some expressions supported in Power Apps aren't available for cards during preview.

### Play button

Once you've set up your card to your liking, select **Play** to preview your card. This will open your card in a new tab and allow you to test out the card's functionalities. This is also where, if needed, you'll be able to debug and troubleshoot your card. For more information on debugging, see [Debugging cards](../make-a-card/testing/debugging-cards.md).

## Next steps

Now that you've got an overview of designer, [make your first card](../tutorials/hello-world-card.md).
