---
title: Add a chatbot to your canvas app (preview)
description: Learn how to add a Chatbot control to your canvas app and embed a published Microsoft Copilot Studio bot to help your app users with their requests.
author: mduelae
ms.author: tapanm
ms.topic: conceptual
ms.date: 7/9/2024
ms.custom: 
    - canvas
    - diy-editor
ms.collection: 
    - bap-ai-copilot
    - get started
ms.reviewer: 
ms.subservice: canvas-maker
search.audienceType: 
  - maker
contributors:
  - mduelae
ai-usage: ai-assisted
---

# Add a chatbot to your canvas app (preview)

> [!IMPORTANT]
> Effective September 5, 2024, Chatbot control (Preview) is deprecated. This control can no longer be inserted into apps, and is no longer supported. Use [Copilot control](add-ai-copilot.md) instead.

Add a Chatbot control to your canvas apps and embed a published [Microsoft Copilot Studio](/power-virtual-agents/fundamentals-what-is-power-virtual-agents) chatbot to assist your end-users with various requests&mdash;from providing simple answers to common questions to resolving issues requiring complex conversations. 

Add a chatbot to your canvas app without writing code or designing screens. With the Chatbot control in Power Apps, you can embed a published copilot, or chatbot, in your app to assist your app users with their requests&mdash;from providing simple answers to common questions to resolving issues requiring complex conversations. Learn more in [Microsoft Copilot Studio overview](/microsoft-copilot-studio/fundamentals-what-is-copilot-studio).

You can also add a Chabot control to a model-driven app. Learn more in [Overview of custom pages for model-driven apps](../model-driven-apps/model-app-page-overview.md). The control supports Teams-authenticated Microsoft Copilot Studio bots, too. You can select from a list of all published bots that are in the same environment as your app.

You can use an AI chatbot for straightforward conversations or AI-based copilot authoring for more complex conversations. Here's how they differ:

- AI chatbots follow a comprehensive tree of responses to assist your users. Learn more in [Quickstart: Create and deploy a copilot](/microsoft-copilot-studio/fundamentals-get-started).

- With AI-based copilot authoring, the bot can respond to the user using many prompts or by generating a response based on a "fallback" website that you set. The fallback website can include internal documents or publicly available websites. Learn more in [AI-based copilot authoring overview](/microsoft-copilot-studio/nlu-gpt-overview).

The Chabot control is customizable. Give your bot a name, change the size of the control window, and position it anywhere on the screen.

:::image type="content" source="media/chatbot-control/ai-chatbot-control-1.png" alt-text="Screenshot showing a sample Chabot control in a canvas app.":::

> [!IMPORTANT]
>
> - Preview features aren't meant for production use and might have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.
> - For more information, read our [preview terms](https://go.microsoft.com/fwlink/?linkid=2189520).
> - This capability is powered by [Azure OpenAI Service](/azure/cognitive-services/openai/overview).
> - This capability may be subject to usage limits or capacity throttling.

## Prerequisites

- Meet the prerequisites for Copilot features in Power Apps. Learn more in [Create conversational apps with Copilot in Power Apps](ai-overview.md).

- Create and publish a bot. Any bot will do, like an AI bot or a new Copilot Studio bot enriched with generative AI. Learn more in [Microsoft Copilot Studio overview](/microsoft-copilot-studio/fundamentals-what-is-copilot-studio).

## Add a control with a bot

With your [canvas app open for editing](edit-app.md):

1. In the app authoring menu, select **Insert**.

1. Expand the **Input** menu, and then select **Chatbot (preview)**.

1. Place the Chatbot control where you want it to appear on the app screen.

    :::image type="content" source="media/chatbot-control/ai-chatbot-control-3.png" alt-text="Screenshot of the Power Apps Studio editing window, showing a Chatbot control placed on the app screen.":::

1. In the **Chatbots** list, select a published bot to connect to the control, or select **New chatbot** to create one.

    All Microsoft Copilot Studio bots, whether published or unpublished, that are in the environment you're working in appear in the **Chatbots** list. However, you can only connect a published bot to the control. Unpublished bots appear dimmed.

1. Change the name, position, and size of the control as needed.

1. Save and publish your app.

## Key properties

You can modify the following properties of the Chatbot control:

- **Header label**: The bot's name as it appears to your app users. If you don't enter a header label, then the name is **Chatbot**.

- **Schema name**: The Microsoft Copilot Studio bot that you connected the Chatbot control to. To connect a different bot, select **Select bot** and then choose a bot from the list.

- **Visible**: Determines whether the bot is visible or not.
  
- **Position** and **Size**: Determine your bot's size and where it appears on the app screen.

:::image type="content" source="media/chatbot-control/ai-chatbot-control-4.png" alt-text="Screenshot of a Chatbot control and its properties in the Power Apps Studio editing window.":::

## Limitations

- The Chatbot control isn't available in the Power Apps mobile app.

- The Chatbot control isn't available in [Power Apps US Government](/power-platform/admin/powerapps-us-government) or Microsoft Azure operated by 21Vianet.

- You can't connect the Chatbot control to Microsoft Copilot Studio bots that were created outside the default location in your tenant.

## Related information

- [Copilot in Power Apps overview (preview)](ai-overview.md)
- [Quickstart: Create and deploy a copilot](/power-virtual-agents/preview/quickstart)
- [AI-based copilot authoring overview](/power-virtual-agents/nlu-gpt-overview)
- [Add a Copilot Control to a canvas app (preview)](add-ai-copilot.md)
- [Build apps through conversation (preview)](ai-conversations-create-app.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
