---
title: Add Power Virtual Agents chatbot to Power Apps portals page to answer questions using a bot. | Microsoft Docs
description: Learn about how to add Power Virtual Agents chatbot to Power Apps portals page to answer questions using a bot.
author: neerajnandwana-msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 12/01/2020
ms.author: nenandw
ms.reviewer: tapanm
---

# Add chatbot to a page

Power Apps portals allows you to add a [Power Virtual Agents chatbot](https://docs.microsoft.com/power-virtual-agents/fundamentals-what-is-power-virtual-agents) to answer questions posted by visitor to your portal page. A bot can be configured with different topics and trigger phrases to automatically respond during a conversation with a visitor.

## Prerequisites

Before you add a Power Virtual Agents chatbot to a Power Apps portals page, you must create a chatbot first. To learn about how to create a chatbot, go to [Create and delete Power Virtual Agents bots](https://docs.microsoft.com/power-virtual-agents/authoring-first-bot).

## Add chatbot component

To add a chatbot component to portal page:

1. Go to [Power Apps](https://make.powerapps.com).

1. Select **Apps** from the left pane.

1. Select your portal.

1. Select **Edit** to open the portals Studio.

1. Select **Components** from the left pane.

1. Select **Chatbot** component.

    ![Add chatbot component to a page](media/add-chatbot/add-chatbot.png "Add chatbot component to a page")

1. Enter **Bot ID** in the chatbot component configuration pane that appears on the left.

    ![Enter bot ID](media/add-chatbot/enter-bot-id.png "Enter bot ID")

    > [!NOTE]
    > To learn about how to get the bot ID, go to [Get a Power Virtual Agents bot ID](#get-the-power-virtual-agents-bot-id).

1. If necessary, update the display name.

1. If necessary, update the chat window height, width, header background color, and header text color.

Chatbot component is now added to your portal page. Browse your portal to interact with the chatbot.

## Get the Power Virtual Agents bot ID

To get the ID of a chatbot created using Power Virtual Agents:

1. Go to [Power Virtual Agents](https://powerva.microsoft.com).

1. From the top-right side of the screen, select the **Bots panel**.

    ![Bots panel](media/add-chatbot/bots-panel.png "Bots panel")

1. Select the environment that the bot is created in.

    ![Select environment](media/add-chatbot/select-environment.png "Select environment")

1. Select the bot that you want to get the bot ID for.

    ![Select your bot](media/add-chatbot/select-bot.png "Select your bot")

1. Expand **Manage** from the left pane.

    ![Select Manage](media/add-chatbot/select-manage.png "Select Manage")

1. Select **Channels**.

    ![Select Channels](media/add-chatbot/select-channels.png "Select Channels")

1. Select **Custom website** channel.

    ![Select Custom Website](media/add-chatbot/select-custom-website.png "Select Custom Website")

1. Copy the bot ID from the embed code.

    ![Copy the bot ID](media/add-chatbot/bot-id.png "Copy the bot ID")

1. Paste the bot ID into the **Bot ID** text box inside Power Apps portals Studio while adding the [chatbot component](#add-chatbot-component).

### See also

- [Add the bot to your live website](https://docs.microsoft.com/power-virtual-agents/publication-connect-bot-to-web-channels)
