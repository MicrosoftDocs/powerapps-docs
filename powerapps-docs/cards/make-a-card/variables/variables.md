---
title: Add variables to a card (Preview)
description: Learn how to add screens to your Microsoft Power Apps cards.
ms.date: 09/20/2022
ms.topic: how-to
author: iaanw
ms.author: iawilt
manager: shellyha
ms.reviewer: 
ms.custom: 
ms.collection: 
---

# Add variables to a card (Preview)

Variables store data for reuse. The data can be of different types, like table, text, or a number. Variables have unique names, which is how you refer to them in [Power Fx formulas](../../make-a-card/power-fx/intro-to-pfx.md). Insert, modify, and remove them in the [card designer](../designer-overview.md).

The value of a variable can be temporary, resetting after every card session, or permanent, shared across all sessions of a specific card instance.

As an example, you've created a card that counts how many times the user presses a button during a session. You would create a temporary number variable to store the number of button presses in the current instance of the card. If you also want to capture the name of the last user to press a button in a card instance, you would store it in a permanent text variable. If you further want to save the data between card instances, you would use a [data connection](../connectors/connector-intro.md).

## Prerequisites

- A [Power Apps](https://powerapps.microsoft.com/) account
- [A card](../../tutorials/hello-world-card.md)

## Create a variable

1. Sign in to [Power Apps](https://powerapps.microsoft.com/). Select **Cards (preview)** > **Cards**, and then select a card.
1. In the left pane of the card designer, select **Variables**
1. Select **+ New variable**.
1. In the **New variable** window, set the following values:

    - **Name**: The name of your variable (Required)
    - **Type**: The type of variable (Required)
    - **Default value**: The default value of the variable
    - **Value Persistence**: Whether the variable is temporary (resets every time the card is opened) or permanent

    You can't change the name or type of a variable. If you need to change them, create a new variable.

    You can also customize sender options and, under **Additional variable information**, the **Title** and **Description** of the variable. This information may be helpful for testing and debugging and using your variable with Power Automate flows and Power Virtual Agents bots.

    :::image type="content" source="../../media/variables/new-variable.png" alt-text="Screenshot of the New variable window in the card designer.":::

1. Select **Save**.

### Edit and delete variables

To edit or delete a variable, select the ellipsis (**...**) to the right of the variable, and then select **Edit** or **Delete**.

:::image type="content" source="../../media/variables/edit-delete-variable.png" alt-text="Screenshot of the Edit and Delete variable options in the card designer.":::

## Use variables in cards

There are various ways to use variables in cards. [Learn about working with variables in Power Apps](/powerapps-docs/maker/canvas-apps/working-with-variables.md).

A common use for variables is in Power Fx expressions. Refer to the variable by name in your formula. For an example, go to the [simple card tutorial](../../tutorials/hello-world-card.md). Your variables are recognized in the formula bar as well.

:::image type="content" source="../../media/variables/formula-bar-example.png" alt-text="Screenshot of an automatically filled variable name in the card designer formula bar.":::
