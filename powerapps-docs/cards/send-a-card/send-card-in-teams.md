---
title: Share a card in Teams
description: Learn how to share a card with your teammates in Teams."
keywords: "Card Designer, Power Apps, cards, share a card, Teams, send a card"
ms.date: 09/20/2022
ms.topic: article
author: iaanw
ms.author: iawilt
ms.reviewer: 
ms.custom: 
ms.collection: 
---

# Share a card in Teams

An easy way to share your cards is to include a link to them in Microsoft Teams. The **Send** button on the **Play** page generates a link that you can copy and then paste into a chat, channel, or meeting. Power Apps must be installed in the Teams chat, channel, or meeting for the card to work and will be installed automatically unless the app is blocked in the organization.

   :::image type="content" source="../media/send-a-card/card-in-teams.png" alt-text="Screenshot of a Power Apps card shared in a Teams chat.":::

## Prerequisites

- A [Power Apps](https://powerapps.microsoft.com/) account
- [A card](../tutorials/hello-world-card.md)

## Send the card link to Teams

The card link points to a specific card instance that's previewed on the **Play** page.

1. On the **Play** page, select **Send** to copy the card link.

    You can also copy the URL in your browser's address bar.  

   :::image type="content" source="../media/send-a-card/send-card-play-page.png" alt-text="Screenshot of a card link copied on the Play page.":::

1. Paste the link in a Teams chat, meeting, or channel where the Power Apps app has been added.

If the Power Apps app hasn't been added yet, you and the receivers may be prompted to add it before the card can be displayed. There may also be a brief delay before the card opens, depending on its complexity.

## Add Power Apps to Teams

The Power Apps app in Teams identifies the card link and displays the card in the chat, channel, or meeting in which the link was posted. While the Power Apps app should be installed automatically, Teams users, or a Teams admin, can manually install the Power Apps app in a chat, channel, or meeting if needed.

1. In Microsoft Teams, select the **Apps** icon in the left bar.
1. Search for and select the **Power Apps** app.

   :::image type="content" source="../media/send-a-card/power-apps-teams-app.png" alt-text="Screenshot of the Teams app search page, with the Power Apps app highlighted.":::

1. Select the arrow next to the **Add** button to add the app to a channel, chat, or meeting.

   :::image type="content" source="../media/send-a-card/add-teams-app.png" alt-text="Screenshot of the Power Apps app page in Teams, with the Add button and add options highlighted.":::

   Select the **Add** button itself to install the app in your [personal scope in Teams](../../teams/create-apps-overview.md).

   If the button label is **Open**, not **Add**, then you've already installed the Power Apps app in your personal scope. You'll still need to add the app to a chat, channel, or meeting for cards to work in a Teams message.
