---
title: "Share a card in Teams (preview)"
description: "Learn how to share a card with your teammates"
keywords: "Card Designer, Power Apps, cards, share a card, Teams, send a card"
ms.date: 09/20/2022
ms.topic: article
author: iaanw
ms.author: iawilt
manager: shellyha
ms.reviewer: 
ms.custom: 
ms.collection: 
---

# Share a card in Microsoft Teams (preview)

[!INCLUDE[cards_preview_notice](../includes/preview-include.md)]

Cards are shared in Microsoft Teams through specific links that are copyable from the Play page. Cards require the Power Apps Teams app to be installed in the chat or channel to work.

   :::image type="content" source="../media/send-a-card/card-in-teams.png" alt-text="Screenshot of card in teams." border="true":::

## Add the Power Apps Teams app to conversations

The Power Apps Teams app identifies the card link, unfurls the card, and connects that card to the lightweight runtime. These all happen seamlessly when the app is added to the chat, channel, or meeting and when a card link is sent.

To add the Power Apps Teams app:

1. Open Microsoft Teams and click the **Apps** icon in the left-hand menu.
1. Search for "Power Apps" using the search bar in the top left and select the **Power Apps** app.

   :::image type="content" source="../media/send-a-card/power-apps-teams-app.png" alt-text="Screenshot of adding Power Apps in Teams." border="true":::

1. Press the chevron next to the **Add** button to add the app to a team, chat, or meeting. You can also press the **Add** button to add the app to your personal scope, which is used for [apps in Teams](../../teams/create-apps-overview.md). Having the app installed in your personal scope will also make Teams prompt you when you send card links to add the app to that conversation.
    1. If you see **Open**, then you have already added the **Power Apps** app to your personal scope. You will still need to add the app to the chat, channel, or meeting for cards to work.

   :::image type="content" source="../media/send-a-card/cards-add-teams-app.png" alt-text="Screenshot of the Open button options." border="true":::

## Get the card link

The card links points to the specific card instance that should be sent. On the Play page, pressing the **Send** button in the top right of the page will copy the card link. You can also directly copy your browser's address bar.  

   :::image type="content" source="../media/send-a-card/send-card-play-page.png" alt-text="Screenshot of link to send from the Play page" border="true":::

## Sending a card

Paste the link you copied from the Play page into a chat, meeting, or Teams channel where the Power Apps Teams app is added. Teams will automatically unfurl the card, which you can send. You and the receiver(s) might be prompted to add the app if it hasn't been added already. There might also be a few seconds of delay before the card unfurls, depending on the complexity of the card.
