---
title: Create a simple card
description: Learn about basic elements of a card by creating a simple "Hello World" card
ms.date: 2/29/2024
ms.topic: how-to
author: iaanw
ms.author: iawilt
ms.reviewer: 
ms.custom: 
ms.collection: 
---

# Create a simple card (preview)

[!INCLUDE[cards-deprecation-banner](~/includes/cards-deprecation-notice.md)]

In this article, you create a card that asks the user to enter their name, and then shows the name in the title of the card. You use the [card designer](../make-a-card/designer-overview.md), [variables](../make-a-card/variables/variables.md), and [Power Fx](../make-a-card/power-fx/intro-to-pfx.md).

## Prerequisites

A [Power Apps](https://powerapps.microsoft.com/) account

## Create a card

1. Sign in to [Power Apps](https://make.powerapps.com) and select your environment.

1. From the navigation menu, select **...More** > **Cards**.

1. Select **+ Create a card**.

1. Under **Card name**, type *HelloWorldCard*, and then select **Create**.

## Ask for text input

1. Select the text **Add and remove element to customize your new card.**, and then select the **Remove** icon (**X**) to delete it.

   :::image type="content" source="../media/hello-world-card/remove-placeholder-text-label.png" alt-text="Screenshot of the placeholder text label to remove in a new card in the card designer.":::

1. From the navigation menu, select **+ Insert**.
1. In the tool pane, select **Input** to expand the category, and then select **Text input**.

   :::image type="content" source="../media/hello-world-card/text-input-location.png" alt-text="Screenshot of the card designer tool pane with input controls shown and the Text input control highlighted.":::

1. In the text input properties pane, set **Label** to *What's your name?*.

   :::image type="content" source="../media/hello-world-card/edit-input-text-label.png" alt-text="Screenshot of a card with a labeled text input control in the card designer." lightbox="../media/hello-world-card/edit-input-text-label.png":::

## Assign variables

1. From the navigation menu, select **Tree View** and change the **textInput1** name to *UserAnswer*.

    We give the text input control the name of a variable that is associated with the user's input. Any input control name can be used as a variable, for example a text input, button, or text label.

   :::image type="content" source="../media/hello-world-card/edit-input-text-title-name.png" alt-text="Screenshot of the text input control from the Tree View navigation menu with a changed name.":::

   > [!TIP]
   > Give your variables descriptive and unique names to make them easier to use in Power Fx expressions.

   We need another variable to add the user's input to the card title, so let's create one now.

1. From the navigation menu, select **Variables**.
1. Select **+ New variable**.
1. In the **New variable** window, enter *UserName* under **Name** and enter *No Name* under **Default value**. Leave the other values as they are.
1. Select **Save**.

   :::image type="content" source="../media/hello-world-card/new-variable-setup.png" alt-text="Screenshot of the variable properties pane.":::

1. In your canvas, select the card title, which is a text label control. In the control's properties pane, set **Text** to *="Hello " & UserName*.

   This expression changes the card title to the string "Hello " followed by the value of the variable you created. You can enter the expression in the formula bar or the properties pane.

    :::image type="content" source="../media/hello-world-card/card-title-with-variable.png" alt-text="Screenshot of a text expression entered in the card title's Text property." lightbox="../media/hello-world-card/card-title-with-variable.png":::

## Add a Power Fx button

1. From the navigation menu, select **+ Insert**.
1. In the tool pane, select **Input** to expand the category, and then select **Button**.
1. In the button properties pane, set **Title** to *Say Hello*.

   :::image type="content" source="../media/hello-world-card/rename-button-title.png" alt-text="Screenshot of the named button properties pane and the button in the card.":::

1. In the properties pane next to **On select**, select **PowerFx** to place your cursor in the formula bar.
1. Type the following Power Fx expression in the formula bar: *Set(UserName, UserAnswer)*

   This [Set()](/power-platform/power-fx/reference/function-set) function expression assigns the value of the user's input, `UserAnswer`, to the `UserName` variable of the text label (the card title), when the button is selected. Another way to read the expression is _Set the value of the variable UserName equal to the value of UserAnswer_. Since the expression is bound to the button's **On select** property, also called **Verb** next to the formula bar, it runs when the user selects the button.

   :::image type="content" source="../media/hello-world-card/pfx-in-button.png" alt-text="Screenshot of the Power Fx expression in the formula bar, assigned to the button's OnSelect property.":::

## Test the card

You should always save your changes before you play a card. Select **Save**, and then select **Play**.

Test your card a few times with different inputs. Make sure your input replaces the default value "No Name" in the card title each time.

## Next steps

Learn how to make a slightly more complex card in the [simple shopping list](simple-shopping-list.md) tutorial.
