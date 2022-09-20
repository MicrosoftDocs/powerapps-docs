---
title: Create a simple card (Preview)
description: Learn about the basic elements of a Microsoft Power Apps card by creating a simple "Hello World" card.
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

[!INCLUDE[cards_preview_notice](../includes/preview-include.md)]

In this tutorial, you'll create a card that asks the user to enter their name, and then shows the name in the title of the card. You'll use the [card designer](../make-a-card/designer-overview.md), [variables](../make-a-card/variables/variables.md), and [Power Fx](../make-a-card/power-fx/intro-to-pfx.md).

## Prerequisites

- A [Power Apps](https://powerapps.microsoft.com/) account

## Create a card

1. Sign in to [Power Apps](https://make.powerapps.com) and select your environment.

1. In the left pane, select **Cards (preview)**.

1. Select **+ Create a card**.

1. Under **Card name**, type **HelloWorldCard**, and then select **Create**.

## Ask for text input

1. Select the text **Add and remove element to customize your new card.**, and then select the **Remove** icon (**X**) to delete it.

   :::image type="content" source="../media/hello-world-card/remove-placeholder-text-label.png" alt-text="Screenshot of the placeholder text label to remove in a new card in the card designer.":::

1. In the left pane, select **Insert**.
1. Select **Input** to expand the category, and then select **Text input**.

   :::image type="content" source="../media/hello-world-card/text-input-location.png" alt-text="Screenshot of the card designer tool pane with input elements shown and the Text input control highlighted.":::

1. With the new text input control selected, in the properties pane, enter *What's your name?* in the **Label** box.

   :::image type="content" source="../media/hello-world-card/edit-input-text-label.png" alt-text="Screenshot of a card with a labeled text input control in the card designer.":::

## Assign variables

1. In the **Name** box, replace the default value, `textInput1`, with *UserAnswer*. We're giving the text input control the name of a variable that we're going to associate with the user's input.

   :::image type="content" source="../media/hello-world-card/edit-input-text-variable-name.png" alt-text="Screenshot of the text input control properties with the Name entered.":::

   > [!TIP]
   > Give your variables descriptive and unique names to make them easier to use in Power Fx expressions.

   We need another variable to add the user's input to the card title, so let's create one now.

1. In the left pane, select **Variables**.

1. Select **+ New variable**.

1. Enter *UserName* under **Name** and enter *No Name* under **Default value**. Leave the other values as they are.

1. Select **Save**.

   :::image type="content" source="../media/hello-world-card/new-variable-setup.png" alt-text="Screenshot of the variable properties pane.":::

1. Select the card title, which is a text label control. Replace the **Text** with `="Hello " & UserName`.

   This will call the variable you just created in the title once the user has provided their name.

## Use Power Fx in buttons

1. To say "Hello" to the name from user input, you need to create a button that uses Power Fx. Under the **Display** menu, select **Button**. The button will appear under the Text input box.

1. Under **Title** enter "Say Hello". You'll see the text on the button update as soon as you finish typing.

   :::image type="content" source="../media/hello-world-card/rename-button-title.png" alt-text="Screenshot of the named button title and updated button on the card.":::

1. Select **PowerFx** under **Type** on the right. This moves your cursor up to the PowerFx bar at the top of the screen.

1. Enter the following Power Fx expression into the bar: `Set(UserName,UserAnswer)`

   This assigns value of `UserAnswer`, the user's input, to the `UserName` variable you put into the card title.

   :::image type="content" source="../media/hello-world-card/pfx-in-button.png" alt-text="Screenshot of Power Fx expression in button.":::

## Test the card

1. **Save** the card by selecting the button on the top right. You should always save changes before playing an updated card. Then select **Play**.

    Test your card and see how your input replaces the default value "No Name" in the card's title text. Note that if you replace the user input and select the button again the title text will change.

## Next steps

Learn how to use more cards functionality in the [simple shopping list](simple-shopping-list.md) tutorial.
