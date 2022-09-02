---
title: "Card Designer overview"
description: "Learn about the designer in Power Cards to confidently create cards"
keywords: "Card Designer, Power Apps, Cards"
ms.date: 09/20/2022
ms.topic: article
author: iaanw
ms.author: iawilt
manager: shellyha
ms.reviewer: 
ms.custom: 
ms.collection: 
---

# Card Designer overview

The Cards Designer is where makers can build out cards to suit their own needs, enabling them to optimize and automate business user tasks and to create actionable scenarios in interactive and easy-to-make cards. The Designer builds off of the designer for Adaptive Cards, introducing a few new concepts:

- Power Fx: specify an action to trigger when an element is selected
- Connectors: bring data into cards (for now, only Dataverse)
- Variables: store, bind, and reuse data across a card
- Dataverse: stores each card you create and allows you to retrieve the card at send time

## Find the Designer

To get to the Card Designer, follow the instructions below:

1. Navigate to [https://make.powerapps.com](https://make.powerapps.com).

1. Go to the left side pane to access all of the Card-related views.

   1. Create a new card: select **Cards** > **Create**
   1. See all current cards: select **Cards** > **Cards**

      :::image type="content" source="../media/designer-overview/create-new-card.png" alt-text="Screenshot showing card creation screen." border="false":::

1. From **Cards** > **Create**, select **Create a card** to start building your own card.

## What's in the Designer

The Designer is made up of the following elements:

- Navigation
- Tool pane
- Card canvas
- Property pane
- Formula bar
- Play button

:::image type="content" source="../media/designer-overview/designer-elements.png" alt-text="Screenshot of Power Apps Cards Designer with elements highlighted." border="false":::

### Navigation

The navigation bar allows you to swap between the different tools available in the Designer. In order, these are:

- Expand toolbar: allows you to see the full name for each option in the navigation bar
- Structure: see the card as a hierarchical outline and view the relationships of the card elements; add multiple steps to a card
- Elements (default view): main UI for editing the card
- Data connections: add connectors to your card to use data from external sources
- Variables: store, bind, and reuse data across a card.

### Tool pane

When you start making your card, you'll use items from the Elements pane. There are three categories of items to choose from, as shown in the tables below:

### Card canvas

The card canvas is where the magic happens – this is where you'll build the user interface for your card, using connectors, variables, and elements from the Tool pane.

You can't resize a card in the card canvas view because cards automatically fit themselves to the location they're placed into.

### Property pane

The property pane is used to change up specific properties for an element. Each type of element has its own property pane, including the card itself. For most of the drag-and-drop elements, you'll be able to specify things like:

- **Name**: the variable name of that element, referenceable in a PowerFX formula
- **Label**/**Text**: any text the user will see when they load in the card
- **Default value**: the initial value of a field
- **Initially visible**: choose if the element will be visible on load

Each property pane also contains Advanced features, which allow you to specify things like:

- **Repeat for every**: provide a trigger for if/when an element should be repeated
- **Show when**: provide a trigger to show the element
- **Requires**: make the element dependent on certain features, corresponding with a minimum version

You can also input PowerFX expressions into the properties, utilizing low-code solutions to make your card more powerful.

### Power Fx editor

The formula bar sits at the top of the card designer and allows you to write Power Fx expressions with intellisense. When you select an element on the card, the formula bar lets you select a property of that element from the dropdown that supports a code input and then assists you in writing an expression. Intellisense will also pull in any variables you've defined, and specific functions based on the data connections you've made. To get started with Power Fx, see [Intro to Power FX](../make-a-card/power-fx/intro-to-pfx.md). For more information on the specific functions you can use, see the Microsoft documentation for [Formula reference for Power Apps](/powerapps/maker/canvas-apps/formula-reference).

Note that some expressions supported in Power Apps will not be available for cards during preview.

### Play button

Once you've set up your card to your liking, you can preview the card with the Play button. This will open your card in a new tab and allow you to test out the card's functionalities. This is also where, if needed, you'll be able to debug and troubleshoot your card. For more information on debugging, see [Debugging cards](../make-a-card/testing/debugging-cards.md).

## Next steps

Now that you've got an overview of the Power Cards Designer, [Get started making your first card](../tutorials/hello-world-card.md).
