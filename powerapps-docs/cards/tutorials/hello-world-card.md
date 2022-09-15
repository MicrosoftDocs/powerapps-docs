---
title: Create a simple card (Preview)
description: Learn about basic elements of a card by creating a simple "Hello World" card
ms.date: 09/20/2022
ms.topic: article
author: iaanw
ms.author: iawilt
manager: shellyha
ms.reviewer: 
ms.custom: 
ms.collection: 
---

# Create a simple card (Preview)

This tutorial shows you how to create a card, ask a user for their name, and then show that name in the title of the card.

## Prerequisites

- A [Power Apps](https://powerapps.microsoft.com/) account.
- Familiarity with the [Card Designer](../make-a-card/designer-overview.md), [variables](../make-a-card/variables/variables.md), and [Power Fx](../make-a-card/power-fx/intro-to-pfx.md).

## Create a card

1. Go to [Power Apps](https://make.powerapps.com) and select **Cards (preview)** on the left.

1. Select **+ Create a card**.

1. Enter "HelloWorldCard" under **Card name** and then select **Create**.

## Ask for text input

1. Double-click on the **Text label** that has "Add and remove element to customize your new card.". Select the Remove button (X) at the top of the box to delete it.

   :::image type="content" source="../media/hello-world-card/remove-placeholder-text-label.png" alt-text="Screenshot of placeholder text label to remove in the card." border="false":::

1. Under the **Insert** menu, select **Input**. Then select **Text input**.

   :::image type="content" source="../media/hello-world-card/text-input-location.png" alt-text="Screenshot showing where text input is under the Insert>Input menu" border="false":::

1. A new **Text input** box will appear on your card. This lets you gather text input from users who interact with the card.

    With the **Text input** selected, edit the **Label** on the right by entering "What's your name?". This label will add text to the **Text input** box.

   :::image type="content" source="../media/hello-world-card/edit-input-text-label.png" alt-text="Screenshot showing an updated input text label and the resulting card with the same label." border="false":::

## Assign variables

1. Under **Name** enter `UserAnswer`. This is the name of the variable associated with the input the user enters.

   :::image type="content" source="../media/hello-world-card/edit-input-text-variable-name.png" alt-text="Screenshot of the updated value for input text name." border="false":::

    Using a descriptive and unique variable name makes it easier to use in Power Fx expressions later in the card building process.

1. Now create another variable. This variable will be used to add the user's input (their name, `UserName`) to the card title. Select **Variables** from the left pane and then select **New variable**.

   :::image type="content" source="../media/hello-world-card/add-new-variable.png" alt-text="Screenshot showing the New variable button to create a new variable in the card." border="false":::

1. Enter `UserName` under **Name**. Leave the **Type** as **Text** and enter `No Name` as the **Default value**. Keep the **Value Persistance** set to **Temporary**. Then select **Save**.

   :::image type="content" source="../media/hello-world-card/new-variable-setup.png" alt-text="Screenshot of the variable properties to change for the default name variable." border="false":::

1. Select the **Text label** at the top of the card. Replace the **Text** with `="Hello " & UserName`.

   This will call the variable you just created in the title once the user has provided their name.

## Use Power Fx in buttons

1. To say "Hello" to the name from user input, you need to create a button that uses Power Fx. Under the **Display** menu, select **Button**. The button will appear under the Text input box.

1. Under **Title** enter "Say Hello". You'll see the text on the button update as soon as you finish typing.

   :::image type="content" source="../media/hello-world-card/rename-button-title.png" alt-text="Screenshot of the named button title and updated button on the card." border="false":::

1. Select **PowerFx** under **Type** on the right. This moves your cursor up to the PowerFx bar at the top of the screen.

1. Enter the following Power Fx expression into the bar: `Set(UserName,UserAnswer)`

   This assigns value of `UserAnswer`, the user's input, to the `UserName` variable you put into the card title.

   :::image type="content" source="../media/hello-world-card/pfx-in-button.png" alt-text="Screenshot of Power Fx expression in button." border="false":::

## Test the card

1. **Save** the card by selecting the button on the top right. You should always save changes before playing an updated card. Then select **Play**.

    Test your card and see how your input replaces the default value "No Name" in the card's title text. Note that if you replace the user input and select the button again the title text will change.

## Next steps

Learn how to use more cards functionality in the [simple shopping list](simple-shopping-list.md) tutorial.
