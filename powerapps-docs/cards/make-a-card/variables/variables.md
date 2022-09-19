---
title: Use variable
description: Learn about storing data in variables
ms.date: 09/20/2022
ms.topic: article
author: iaanw
ms.author: iawilt
manager: shellyha
ms.reviewer: 
ms.custom: 
ms.collection: 
---

# Variables

Variables are used to store data within the context of a card. That data can be of different types like table, text, or a number. The value can also be temporary, where it resets for every card session, or permanent, where it is shared across all sessions for a specific card instance. Variables have unique names, which is how they are referenced in [formulas](../../make-a-card/power-fx/intro-to-pfx.md).

For example, if you wanted a card that counted how many times a user pressed a button during a session, you would create a temporary number variable. If you wanted to capture the name of the last user to press a button for a card instance, you would use a permanent text variable. If you wanted to save data between card instances, you would use a [data connection](../connectors/connector-intro.md).

## Prerequisites

- A [Power Apps](https://powerapps.microsoft.com/) account.
- A card. For an example, see the [simple card tutorial](../../tutorials/hello-world-card.md).
- Familiarity with the [Card Designer](../make-a-card/designer-overview.md).

## Add a variable

To add variables in cards, do the following.

1. Go to [Power Apps](https://make.test.powerapps.com/) and select **Cards (preview)**.
1. On the left, select **Cards** and select the card you want to test add a connector to.
1. On the left, select **Variables**. Then select **+ New variable**.

    :::image type="content" source="../../media/variables/new-variable.png" alt-text="Screenshot of the + Add variable button":::

1. The **New variable** window will appear. Set the following values:
    - **Name**: the name of your variable.
    - **Type**: the type of variable.
    - **Default value**: the default value of the variable, prior to input.
    - **Value Persistance**: whether the variable is temporary (resets every time the card's opened) or permanent.

    You can also customize sender options, as well as the **Title** and **Description** of the variable. These may be helpful for testing and debugging.
1. After you've entered everything select **Save**. The new variable will appear in the **Variables** list and can be used anywhere in your card.

### Edit and delete variables

If you want to to edit or delete a variable, select the three dots next to the variable and choose the option that works for you.

:::image type="content" source="../../media/variables/edit-delete-variable.png" alt-text="Screenshot of the Edit and Delete variable button":::

>[!NOTE]
> After creation, the variable **Name** and **Type** cannot be edited. If you need to change these values, create a new variable.

## Use variables in cards

There are a variety of ways to use variables in cards. The most common option is memory storage, especially for user input.

To use variables in Power Fx expressions simply add the variable name to your formula. For an example, see the [simple card tutorial](../../tutorials/hello-world-card.md). Your variables should be recognized in the formula bar as well, shown below:

:::image type="content" source="../../media/variables/formula-bar-example.png" alt-text="Screenshot of auto-filling variable name in formula bar button":::
