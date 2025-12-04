---
title: Use M365 Copilot chat in model-driven apps
description: Learn how to use M365 Copilot chat to gain insights about the data in your model-driven apps.
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

# Use M365 Copilot chat in model-driven apps

[M365 Copilot chat](https://learn.microsoft.com/copilot/overview) for model-driven apps in Power Apps is a next-generation AI assistant that helps you gain insights into the data in your apps through conversations in natural language. M365 Copilot chat helps you boost your productivity through AI-powered insights and navigation assistance.

> [!IMPORTANT]
>
> This feature is in preview.  
>
> - Preview features aren't meant for production use and might have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.
> - For more information, go to our [preview terms](https://go.microsoft.com/fwlink/?linkid=2189520).
> - An administrator must enable M365 Copilot chat in your application before it becomes visible in your app. More information: [Add M365 Copilot for app users in model-driven apps](../maker/model-driven-apps/add-m365-copilot.md)
> - M365 Copilot Chat will eventually replace [Copilot chat in model-driven apps](use-copilot-model-driven-apps.md).  For a period of time, the transition from one to the other will be at the discretion of the app maker. App makers will be able to control whether an end user has one, the other, or both available to them.

## Copilot pane

After M365 Copilot chat is enabled, you can access it through the Copilot button near the upper-right corner of the page.

:::image type="content" source="media/m365-copilot-button.png" alt-text="Screenshot that shows the Copilot button on a page.":::

If M365 Copilot chat and [Copilot chat in model-driven apps](use-copilot-model-driven-apps.md) are both enabled, you will have the option to try both. The **Chat** option represents M365 Copilot and the **App Skills** option represents [Copilot chat in model-driven apps](use-copilot-model-driven-apps.md).  These terms are used to align with M365 apps for consistency.

:::image type="content" source="media/copilot-chat-switcher.png" alt-text="Screenshot that shows the Copilot split button showcasing Chat and App Skills options on a page.":::

You can expand or collapse the M365 Copilot pane as you want.

## Use M365 Copilot to ask questions

M365 Copilot chat in model-driven apps can answer questions about the Dataverse table data in the app.

:::image type="content" source="media/m365-copilot-question.png" alt-text="Screenshot that shows asking a question in M365 Copilot.":::
:::image type="content" source="media/m365-copilot-question-response.png" alt-text="Screenshot that shows a question and response in M365 Copilot.":::

## M365 Copilot chat suggested questions

To help you get started, M365 Copilot chat suggests questions for you to ask. Many of the suggested questions have placeholders that you must replace with appropriate text to complete the question.

:::image type="content" source="media/m365-copilot-prompts.png" alt-text="Screenshot that shows suggested prompts that have placeholders.":::

## Use agents in M365 Copilot

> [!IMPORTANT]
>
> When you explicitly select an agent in M365 Copilot chat in model-driven apps, the agent will no longer answer questions about the Dataverse table data in the app unless you have explicitly configured your agent to do so.  However, the agent will use information from the chat history.  To get the side chat to answer questions about the Dataverse table data in the app again, you will need to remove the explicit agent selection.

M365 Copilot chat in model-driven apps allows you to use any agent available in M365 Copilot right from the side pane. Once an agent is available within M365 Copilot, you can interact with your agent by either choosing it from the navigation panel or @ mentioning it. One of the benefits of @ mentioning an agent is that you can add or remove it from an ongoing conversation, which allows you to have several agents collaborating in one conversation. When selecting an agent from the navigation panel, you are having a direct conversation only with the agent you selected.

:::image type="content" source="media/m365-copilot-at-mention.png" alt-text="Screenshot that shows how to @ mention agents in M365 Copilot.":::
:::image type="content" source="media/m365-copilot-open-nav-panel.png" alt-text="Screenshot that shows how to open the M365 Copilot navigation panel.":::
:::image type="content" source="media/m365-copilot-nav-panel-agents.png" alt-text="Screenshot that shows agents in the M365 Copilot navigation panel.":::

## Related information

- [Add M365 Copilot chat to model-driven apps](../model-driven-apps/add-m365-copilot.md)
- [Customize M365 Copilot chat in model-driven apps](../model-driven-apps/m365-customize-copilot-chat.md)
