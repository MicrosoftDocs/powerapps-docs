---
title: Create a simple card (Preview)
description: Learn about basic elements of a card by creating a simple "Hello World" card
ms.date: 09/19/2022
ms.topic: article
author: iaanw
ms.author: iawilt
manager: shellyha
ms.reviewer: 
ms.custom: 
ms.collection: 
---

# Create a simple card

In this tutorial, you'll learn how to create a card, ask a user for their name, and then show that name in the title of the card.

## Prerequisites

- Access to [Power Apps](https://powerapps.microsoft.com/).
- Familiarity with the [Card Designer](../make-a-card/designer-overview.md), [variables](../make-a-card/variables/variables.md), and [Power Fx](../make-a-card/power-fx/intro-to-pfx.md).

## Create a card

1. Go to [Power Apps](https://make.powerapps.com) and select **Cards (preview)** on the left. Make sure that you're in the correct environment.

1. Select the **Create a card** button.

1. Enter "HelloWorldCard" under **Card name** and then select **Create**. If the name of the card has already been used, you won't be able to create the card.

   :::image type="content" source="../media/hello-world-card/name-card.png" alt-text="Screenshot of card being named HelloWorldCard." border="false":::

## Customize your card

1. Double-click on the **Text label** that has "Add and remove element to customize your new card.". Select the Remove button (X) at the top of the box to delete it.

   :::image type="content" source="../media/hello-world-card/remove-placeholder-text-label.png" alt-text="Screenshot of placeholder text label to remove in the card." border="false":::

1. Under the **Insert** menu, select **Input**. Then select **Text input**.

   :::image type="content" source="../media/hello-world-card/text-input-location.png" alt-text="Screenshot showing where Text input is under the Insert>Input menu" border="false":::

1. A new **Text input** box will appear on your card. This lets you gather text input from users who interact with the card.

    With the **Text input** selected, edit the **Label** on the right by entering "What's your name?". This label will add text to the **Text input** box.

   :::image type="content" source="../media/hello-world-card/edit-input-text-label.png" alt-text="Screenshot showing an updated input text label and the resulting card with the same label." border="false":::

### Assign variables

1. Under **Name** enter `UserAnswer`. This is the name of the variable associated with the input the user enters.

   :::image type="content" source="../media/hello-world-card/edit-input-text-variable-name.png" alt-text="Screenshot of the updated value for input text name." border="false":::

    Using a descriptive and unique variable name makes it easier to use in Power Fx expressions later in the card building process.

1. Now create another variable. This variable will be used to add the user's input (their name, `UserName`) to the card title. Select **Variables** from the left pane and then select **New variable**.

   :::image type="content" source="../media/hello-world-card/add-new-variable.png" alt-text="Screenshot showing the New variable button to create a new variable in the card." border="false":::

1. Enter `UserName` under **Name**. Leave the **Type** as **Text** and enter `No Name` as the **Default value**. Keep the **Value Persistance** set to **Temporary**. Then select **Save**.

   :::image type="content" source="../media/hello-world-card/new-variable-setup.png" alt-text="Screenshot of the variable properties to change for the default name variable." border="false":::

1. Select the **Text label** at the top of the card. Replace the **Text** with `"Hello " & UserName`.

   This will call the variable you just created in the title once the user has provided their name.

   :::image type="content" source="../media/hello-world-card/add-variable-to-card-title.png" alt-text="Screenshot of the using the username variable in the card title." border="false":::

## Use Power Fx in buttons

1. To say "Hello" to the user, you need to create a button that uses Power Fx. Under the **Display** menu, select **Button**. The button will appear under the Text input box.

1. Under **Title** enter "Say Hello". You'll see the text on the button update as soon as you finish typing.

   :::image type="content" source="../media/hello-world-card/rename-button-title.png" alt-text="Screenshot of the named button title and updated button on the card." border="false":::

1. Select **PowerFx** under **Type** on the right. This moves your cursor up to the PowerFx bar at the top of the screen.

1. Enter the following Power Fx expression into the bar: `Set(UserName,UserAnswer)`

   This assigns value of `UserAnswer`, the user's input, to the `UserName` variable you put into the card title.

   :::image type="content" source="../media/hello-world-card/pfx-in-button.png" alt-text="Screenshot of Power Fx expression in button." border="false":::

1. **Save** the card and then select **Play** to see the card in action.
