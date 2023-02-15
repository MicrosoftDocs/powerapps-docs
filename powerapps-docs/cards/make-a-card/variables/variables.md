---
title: Add variables to a card (preview)
description: Learn how to add variables to your cards for Microsoft Power Apps.
ms.date: 11/17/2022
ms.topic: how-to
author: sericks007
ms.author: sericks
manager: tapanm-MSFT
ms.reviewer: 
ms.custom: 
ms.collection: 

---

# Add variables to a card (preview)

[!INCLUDE[cards_preview_notice](../../includes/preview-include.md)]

Variables store data for reuse. The data can be of different types, like table, text, or a number. Variables have unique names, which is how you refer to them in [Power Fx formulas](../../make-a-card/power-fx/intro-to-pfx.md). Insert, modify, and remove them in the [card designer](../designer-overview.md).

The value of a variable can be temporary, resetting after every card session, or permanent, shared across all sessions of a specific card instance.

As an example, you've created a card that counts how many times the user presses a button during a session. You would create a temporary number variable to store the number of button presses in the current instance of the card. If you also want to capture the name of the last user to press a button in a card instance, you would store it in a permanent text variable. If you further want to save the data between card instances, you would use a [data connection](../connectors/connector-intro.md).

## Prerequisites

- A [Power Apps](https://powerapps.microsoft.com/) account
- [A card](../../tutorials/hello-world-card.md)

## Create a variable

1. Sign in to [Power Apps](https://powerapps.microsoft.com/). Select **Cards**, and then select a card. If the **Cards** tab is not visible, select **More** and pin the **Cards** tab.
1. In the left pane of the card designer, select **Variables**
1. Select **+ New variable**.
1. In the **New variable** window, set the following values:

    - **Name**: The name of your variable (Required)
    - **Type**: The type of variable (Required)
    - **Default value**: The default value of the variable
    - **Value Persistence**: Whether the variable is temporary (resets every time the card is opened) or permanent

    You can't change the name or type of a variable. If you need to change them, create a new variable.

    You can also customize sender options and, under **Additional variable information**, the **Title** and **Description** of the variable. This information may be helpful for testing, debugging, and using your variable with Power Automate flows and Power Virtual Agents bots.

    :::image type="content" source="../../media/variables/new-variable.png" alt-text="Screenshot of the New variable window in the card designer.":::

1. Select **Save**.

### Using the default value for tables and records

The default value is used to set the structure for table and record variables. There are two ways to set the default value of a record or table variable:

- Using a Power Fx expression
- Using JSON

You can toggle between whether you are using Power Fx or JSON using the icon on the right.

:::image type="content" source="../../media/variables/default-value.png" alt-text="Screenshot of the how to toggle between JSON and Power Fx for setting the variable default value.":::

Using a Power Fx expression is helpful when you want the variable to store data from a data source, like Dataverse. For example, if you wanted a record that held a specific row from the **Account** table, you could set the default value to `First(account)`.

Using JSON is helpful when you are using the variable to store custom data. For example, if you wanted to collect a list of people's names, you could set the default value to `[{"First Name": "John", "Last Name": "Doe"}]`.

Variables are strongly typed and so setting the default value locks the variable into those types.

### Edit and delete variables

To edit or delete a variable, select the ellipsis (**...**) to the right of the variable, and then select **Edit** or **Delete**.

:::image type="content" source="../../media/variables/edit-delete-variable.png" alt-text="Screenshot of the Edit and Delete variable options in the card designer.":::

## Use variables in cards

There are various ways to use variables in cards. [Learn about working with variables in Power Apps](../../../maker/canvas-apps/working-with-variables.md).

A common use for variables is in Power Fx expressions. Refer to the variable by name in your formula. For an example, go to the [simple card tutorial](../../tutorials/hello-world-card.md). Your variables are recognized in the formula bar as well.

:::image type="content" source="../../media/variables/formula-bar-example.png" alt-text="Screenshot of an automatically filled variable name in the card designer formula bar.":::

### Updating the value of a variable

Variables can be updated using the [**Set**](/power-platform/power-fx/reference/function-set) function, excluding table variables which are added to using the [**Collect**](/power-platform/power-fx/reference/function-clear-collect-clearcollect) function.
