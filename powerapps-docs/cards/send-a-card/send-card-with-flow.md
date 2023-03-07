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

Use Power Automate to send cards. By setting up a flow that is triggered by an event, you can automate the process of sending cards. For instance, you can create a flow that requests the assigned individual to approve or reject an expense when a new record is added to Dataverse. Additionally, you can create a flow that sends a daily status update every morning.

## Prerequisites

- [Power Automate](https://make.powerautomate.com) account
- Create a [card](../tutorials/hello-world-card.md)
- The [Power Apps Teams app](send-card-in-teams.md#add-power-apps-to-teams) installed in the chat, group chat, or channel that the card will be sent to

## Cards for Power Apps connector

The **Cards for Power Apps** connector is used to get or create instances of cards to send using a flow. The connector has no triggers and three actions:

- **Create card instance** - Enables the user to select a specific card to create an instance of with customizable input variables. Returns the card instance as `card` dynamic content.
- **Get the card instance** - Returns a card instance when given a user-specified card and a card instance id as `card` dynamic content.
- **Get the card description** - Returns information about a user-specified card, including the id, environmentId, name, description, author, etc.

   :::image type="content" source="../media/send-a-card/cards-connector.png" alt-text="Screenshot of the cards for Power Apps connector.":::

## Send card in Teams using the Teams connector

Sending a card in Teams requires a card instance. To get a card instance, use the **Cards for Power Apps** connector actions. The **Create card instance** action has `card` dynamic content and the **Get the card instance** action has `body` dynamic content that can be used with the **Teams** connector **Post card in a chat or channel** action.

1. Create or modify an existing flow
1. Make sure the flow has a trigger. In the example screenshot below, the trigger is when a new account record is created.
1. Create or get the card instance you want to send using the **Cards for Power Apps** connector. In the example screenshot, we created a card instance of the `Account Card` and setting the `Body` input variable to the `Account Name` of the newly created account record. 
1. Add an action to **Post card in a chat or channel** using the **Teams** connector.
1. On the action, set **Post as** to `Power Apps (Preview)`.
1. On the action, set **Post in**, **Team** & **Channel**, or **Group chat** to the conversation you want to send the card in. In the example screenshot, this is to the `Cards for Power Apps (Customer Channel)` Teams in the `General` channel.
1. On the action, set **Card** to the `card` or `body` dynamic content from the **Cards for Power Apps** connector action you added earlier.

   :::image type="content" source="../media/send-a-card/card-in-flow-example.png" alt-text="Screenshot a flow that creates a card instance when an account record is created and sends it in Teams.":::


## Common issues and resolutions

1. When you select a card from the drop-down to create a card instance, the connector action can sometimes show the error **GetCardDescription failed with InternalServerError**. This is a transient error, you need to try again and reselect a card. 

2. If your card doesn't have any input variables, it will show an empty body parameter after selecting a card to create an instance of. You can ignore that parameter and continue building your flow. 
