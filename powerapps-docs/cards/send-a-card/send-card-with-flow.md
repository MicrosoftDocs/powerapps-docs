---
title: Send a card automatically with a flow (preview)
description: Learn how to send a card automatically using a Power Automate flow.
keywords: "Card Designer, Power Apps, cards, send a card, Power Automate, flow"
author: anuitz
ms.topic: reference
ms.custom: 
ms.reviewer: mkaur
ms.date: 03/07/2023
ms.author: anuitz
search.audienceType:
  - maker
search.app:
  - PowerApps
contributors:
  - mduelae
  - anuitz
---

# Send a card automatically with a flow (preview)

[!INCLUDE[cards_preview_notice](../includes/preview-include.md)]

A powerful way to send cards is through Power Automate. You can create a flow that automatically sends a card after it is triggered by an event. For example, create a flow that asks the assigned person to approve or decline an expense when it is that record is created in Dataverse or that sends a daily status check every morning.

## Prerequisites

- A [Power Automate](https://make.powerautomate.com) account
- A [card](../tutorials/hello-world-card.md)
- The [Power Apps Teams app](send-card-in-teams.md#add-power-apps-to-teams) installed in the chat, group chat, or channel that the card will be sent to

## Cards for Power Apps connector

The **Cards for Power Apps** connector is used to get or create instances of cards to send using a flow. The connector has no triggers and three actions:

- **Create card instance** - Enables the user to select a specific card to create an instance of with customizable input variables. Returns the card instance as `card` dynamic content.
- **Get the card instance** - Returns a card instance when given a user-specified card and a card instance id as `card` dynamic content.
- **Get the card description** - Returns information about a user-specified card, including the id, environmentId, name, description, author, etc.

   :::image type="content" source="../media/send-a-card/cards-connector.png" alt-text="Screenshot of the cards for Power Apps connector.":::

## Send card in Teams using the Teams connector

Sending a card in Teams requires a card instance. To get a card instance, use the **Cards for Power Apps** connector actions. The **Create card instance** action has `card` dynamic content and the **Get the card instance** action has `body` dynamic content that can be used directly with the **Teams** connector **Post card in a chat or channel** action.

1. Create or modify an existing flow
1. Make sure the flow has a trigger. In the example screenshot, the trigger is when a new account record is created.
1. Create or get the card instance you want to send using the **Cards for Power Apps** connector. In the example screenshot, we are created a card instance of the `Account Card` and setting the `Body` input variable to the `Account Name` of the newly created account record. 
1. Add an action to **Post card in a chat or channel** using the **Teams** connector.
1. On the action, set **Post as** to `Power Apps (Preview)`.
1. On the action, set **Post in**, **Team** & **Channel**, or **Group chat** to the conversation you want to send the card in. In the example screenshot, this is to the `Cards for Power Apps (Customer Channel)` Teams in the `General` channel.
1. On the action, set **Card** to the `card` or `body` dynamic content from the **Cards for Power Apps** connector action you added earlier.

   :::image type="content" source="../media/send-a-card/card-in-flow-example.png" alt-text="Screenshot a flow that creates a card instance when an account record is created and sends it in Teams.":::
