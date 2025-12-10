---
title: Use Microsoft 365 Copilot chat in model-driven apps (preview)
description: Learn how to use Microsoft 365 Copilot chat to gain insights about the data in your model-driven apps.
author: srihas
ms.component: pa-user
ms.topic: overview
ms.date: 06/10/2025
ms.update-cycle: 180-days
ms.subservice: end-user
ms.author: srihas
ms.custom: ""
ms.reviewer: smurkute
ms.assetid: 
search.audienceType: 
  - enduser
ms.collection: 
    - bap-ai-copilot 
---

# Use Microsoft 365 Copilot chat in model-driven apps (preview)

[Microsoft 365 Copilot chat](/copilot/overview) for model-driven apps in Power Apps is a next-generation AI assistant that helps you gain insights into the data in your apps through conversations in natural language. Microsoft 365 Copilot chat boosts your productivity through AI-powered insights and navigation assistance.

> [!IMPORTANT]
>
> - This feature is in preview.  
> - Preview features aren't meant for production use and might have restricted functionality These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?linkid=2189520), and are available before an official release so that customers can get early access and provide feedback.

## Prerequisites

An administrator must enable Microsoft 365 Copilot chat in your application before it becomes visible in your app. For more information, see [Add Microsoft 365 Copilot chat for app users in model-driven apps](../maker/model-driven-apps/add-microsoft-365-copilot.md).

## Copilot pane

After Microsoft 365 Copilot chat is enabled, access it through the Copilot button near the upper-right corner of the page.

:::image type="content" source="media/microsoft-365-copilot-button.png" alt-text="Screenshot that shows the Copilot button on a page.":::

If both Microsoft 365 Copilot chat and [Copilot chat in model-driven apps](use-copilot-model-driven-apps.md) are enabled, you can access and try each option. The **Chat** option opens Microsoft 365 Copilot Chat, and the **App Skills** option opens [Copilot chat in model-driven apps](use-copilot-model-driven-apps.md). These terms align with Microsoft 365 apps for consistency.

:::image type="content" source="media/copilot-chat-switcher.png" alt-text="Screenshot that shows the Copilot split button showcasing Chat and App Skills options on a page.":::

Expand or collapse the Microsoft 365 Copilot pane as needed.

## Use Microsoft 365 Copilot to ask questions

Microsoft 365 Copilot chat in model-driven apps answers questions about the Dataverse table data in the app.

:::image type="content" source="media/microsoft-365-copilot-question-answer.png" alt-text="Screenshot that shows a question and response in Microsoft 365 Copilot." lightbox="media/microsoft-365-copilot-question-answer.png":::

## Microsoft 365 Copilot chat suggested questions

To help you get started, Microsoft 365 Copilot chat suggests questions to ask. Many suggested questions have placeholders you replace with appropriate text.

:::image type="content" source="media/microsoft-365-copilot-prompts.png" alt-text="Screenshot that shows suggested prompts that have placeholders." lightbox="media/microsoft-365-copilot-prompts.png":::

## Use agents in Microsoft 365 Copilot

> [!IMPORTANT]
>
> When you explicitly select an agent in Microsoft 365 Copilot chat in model-driven apps, the agent no longer answers questions about the Dataverse table data in the app unless you explicitly configure your agent to do so. However, the agent uses information from the chat history. To get the side chat to answer questions about the Dataverse table data in the app again, you need to remove the explicit agent selection.

Microsoft 365 Copilot chat in model-driven apps lets you use any agent available in Microsoft 365 Copilot right from the side pane. Once an agent is available within Microsoft 365 Copilot, you can interact with your agent by either choosing it from the navigation panel or @ mentioning it. 

:::image type="content" source="media/microsoft-365-copilot-opened-navigation.png" alt-text="Screenshot that shows how to open the Microsoft 365 Copilot navigation panel with different agents displayed." lightbox="media/microsoft-365-copilot-opened-navigation.png":::

One of the benefits of @ mentioning an agent is that you can add or remove it from an ongoing conversation, which lets you have several agents collaborating in one conversation. When you select an agent from the navigation panel, you have a direct conversation only with the agent you selected.

:::image type="content" source="media/microsoft-365-copilot-at-mention.png" alt-text="Screenshot that shows how to @ mention agents in Microsoft 365 Copilot.":::

## Related information

- [Add Microsoft 365 Copilot chat to model-driven apps](../maker/model-driven-apps/add-microsoft-365-copilot.md)
- [Customize Microsoft 365 Copilot chat in model-driven apps](../maker/model-driven-apps/customize-microsoft-365-copilot-chat.md)
