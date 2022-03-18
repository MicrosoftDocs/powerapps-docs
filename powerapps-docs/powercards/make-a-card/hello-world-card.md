---
title: "Intro to Card elements"
description: "Learn about basic elements of a card by creating a simple card"
keywords: "Power Cards, Power Cards Designer, Power Apps, Cards, tutorial"
ms.date: 03/18/2022
ms.topic: article
author: eberhardts
ms.author: v-eberhardts
manager: shellyha
ms.reviewer: 
ms.custom: 
ms.collection: 
---

# Intro to Card Elements

In this tutorial, you'll learn how to ask a user for their name and then show that name in the title of a card.

1. Create a card in Power Cards: in your environment, go to Cards in the left pane, select Create, then select Basic card.

1. Name your card something you'll remember; here, we're using "HelloWorldCard". Once you've named your card, select Create card.

   1. If the name of the card has already been used, you won't be able to create the card

   :::image type="content" source="../media/flow-hello-world-card/name-card.png" alt-text="Screenshot of card being named Hello World Card." border="false":::

1. Remove the placeholder text box underneath the title.

1. Drag and drop an Input.Text onto your card underneath the title.

   :::image type="content" source="../media/flow-hello-world-card/add-input-text-box.png" alt-text="Screenshot showing a newly added input text box to card underneath card title." border="false":::

1. With the Input.Text selected, edit the Label on the right pane. This label will add text to the Input.Text box.

   1. In this example, we're going to ask the question "What's your name?", and you'll see the text fill in the space above the text box on the card.

   :::image type="content" source="../media/flow-hello-world-card/edit-input-text-label.png" alt-text="Screenshot showing an updated input text label and the resulting card with the same label." border="false":::

1. Select the Name box and add a descriptive name. This gives the user-provided text an easy to reference name that you'll be able to use in PowerFX expressions later in the card building process.

   1. In this example, we give this variable the name *UserAnswer*.

   :::image type="content" source="../media/flow-hello-world-card/edit-input-text-variable-name.png" alt-text="Screenshot of the updated value for input text name." border="false":::

1. Create another variable to use in the card, this one so the user can see their name added to the card title. Select Variables from the left pane and then select New variable.

   :::image type="content" source="../media/flow-hello-world-card/add-new-variable.png" alt-text="Screenshot showing the New variable button to create a` new variable in the card." border="false":::

1. Enter a descriptive variable name into the Name box. In this example, we'll use *UserName*.

1. Leave the Type as string and enter the *defaultName* into the Default value box. Then Save the card.

   :::image type="content" source="../media/flow-hello-world-card/new-variable-setup.png" alt-text="Screenshot of the variable properties to change for the default name variable." border="false":::

1. Select the title element on the card, and add the following title: `Hello ${UserName}`

   This will call the variable you just created in the title, once the user has provided their name.

   :::image type="content" source="../media/flow-hello-world-card/add-variable-to-card-title.png" alt-text="Screenshot of the using the username variable in the card title." border="false":::

1. Now add some Power FX to make the button work. Drag and drop a button from Elements onto the card, underneath the Input.Text box.

1. Add a descriptive title to the Title box; in this example, we'll use "Say hello". You'll see the text on the button update as soon as you finish typing.

   :::image type="content" source="../media/flow-hello-world-card/rename-button-title.png" alt-text="Screenshot of the named button title and updated button on the card." border="false":::

1. Select Power Fx in the right pane. This moves your cursor up to the PowerFX bar at the top of the screen.

1. Enter the following PowerFX into the bar: `Set(UserName,UserAnswer)`

   This will assign the provided name of the user to the UserName variable you put into the card title.

   :::image type="content" source="../media/flow-hello-world-card/pfx-in-button.png" alt-text="Screenshot of power fx expression in button." border="false":::

1. Save the card and then select Play to see the card in action.
