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
contributors:
  - mduelae
  - anuitz
---

# Send a card automatically with a flow (preview)

[!INCLUDE[cards_preview_notice](../includes/preview-include.md)]

Use Power Automate to send cards. By setting up a flow that is triggered by an event, you can automate the process of sending cards. For instance, you can create a flow that requests the assigned individual to approve or reject an expense when a new record is added to Dataverse. Alternatively, you can create a flow that sends a daily status update every morning.

## Prerequisites

- [Power Automate](https://make.powerautomate.com) account
- Create a [card](../tutorials/hello-world-card.md)
- The [Power Apps Teams app](send-card-in-teams.md#add-power-apps-to-teams) installed in the chat, group chat, or channel that the card will be sent to

## Cards for Power Apps connector

The **Cards for Power Apps** connector is used to create instances of cards to send using a flow. The connector has no triggers and two actions:

- **Create card instance** - Enables the user to select a specific card to create an instance of with customizable input variables. Returns the card instance as `Card` dynamic content.
- **Get the card description** - Returns information about a user-specified card, including the ID, environmentId, name, description, author, etc.

   :::image type="content" source="../media/send-a-card/cards-connector.png" alt-text="Screenshot of the cards for Power Apps connector.":::

## Send card in Teams using the Teams connector

Sending a card in Teams requires a card instance. To get a card instance, use the **Cards for Power Apps** connector actions. The **Create card instance** action has `Card` dynamic content that can be used with the **Teams** connector **Post card in a chat or channel** action.

1. Create or modify an existing flow
1. Make sure the flow has a trigger. In the screenshot below, the trigger is when a new account record is created.
1. Create or get the card instance you want to send using the **Cards for Power Apps** connector. In the screenshot, we created a card instance of the `Account Card` and setting the `Body` input variable to the `Account Name` of the newly created account record.
1. Add an action to **Post card in a chat or channel** using the **Teams** connector.
1. On the action, set **Post as** to `Power Apps (Preview)`.
1. On the action, set **Post in**, **Team** & **Channel**, or **Group chat** to the conversation you want to send the card in. In the example screenshot, this is to the `Cards for Power Apps (Customer Channel)` Teams in the `General` channel.
1. On the action, set **Card** to the `Card` dynamic content from the **Cards for Power Apps** connector action you added earlier.

   :::image type="content" source="../media/send-a-card/card-in-flow-example.png" alt-text="Screenshot a flow that creates a card instance when an account record is created and sends it in Teams.":::

## Managing your flow in a solution

For more details on managing your flow that uses the Card for Power Apps Connector, see [Manage cards in solutions](../manage-cards/manage-cards.md).

## Common issues and resolutions

1. If your card doesn't have any input variables, it will show an empty body parameter after selecting a card to create an instance of. You can ignore that parameter and continue building your flow.
