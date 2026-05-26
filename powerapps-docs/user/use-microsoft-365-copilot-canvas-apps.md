---
title: Use Microsoft 365 Copilot in canvas apps (preview)
description: Learn how to use Microsoft 365 Copilot to gain insights about the data in your canvas apps.
author: devkeydet
ms.component: pa-user
ms.topic: overview
ms.date: 04/15/2026
ms.update-cycle: 180-days
ms.subservice: end-user
ms.author: marcsc
ms.custom: ""
ms.reviewer: smurkute
ms.assetid: 
search.audienceType: 
  - enduser
ms.collection: 
    - bap-ai-copilot 
---

# Use Microsoft 365 Copilot in canvas apps (preview)

[Microsoft 365 Copilot](/copilot/overview) for apps is a next-generation AI assistant that helps you gain insights into the data in your apps through conversations in natural language. Microsoft 365 Copilot boosts your productivity through AI-powered insights and navigation assistance.

> [!IMPORTANT]
>
> - This feature is in preview.  
> - Preview features aren't meant for production use and might have restricted functionality. These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?linkid=2189520). They're available before an official release so that customers can get early access and provide feedback.
> -  This feature is in the process of rolling out and might not be available in your region yet.

## Prerequisites

An administrator must enable Microsoft 365 Copilot in your application before it becomes visible in your app. For more information, see [Add Microsoft 365 Copilot for app users](/power-apps/maker/canvas-apps/microsoft-365-copilot-canvas-app).

> [!NOTE]
> - To use the Microsoft 365 Copilot feature in your app, you must have a Microsoft 365 Copilot license.
> - You must have access to an [early release cycle environment](/power-platform/admin/early-release) to use this feature.

## Copilot pane

After Microsoft 365 Copilot is enabled, access it through the Copilot button near the upper-right corner of the page.

:::image type="content" source="/power-apps/user/media/microsoft-365-copilot-button-canvas.png" alt-text="Screenshot that shows the Copilot button on a page.":::

## Use Microsoft 365 Copilot to ask questions

Microsoft 365 Copilot in apps answers questions about the Dataverse tables or SharePoint list data in the app.

:::image type="content" source="/power-apps/user/media/microsoft-365-copilot-question-answer-canvas.png" alt-text="Screenshot that shows a question and response in Microsoft 365 Copilot." lightbox="/power-apps/user/media/microsoft-365-copilot-question-answer-canvas.png":::

## Share your feedback

Help us improve Copilot responses by using the feedback controls on each response. Provide feedback for every response:

- If a response is high quality and helpful, select the thumbs up button.
- If a response is incorrect, incomplete, or not helpful, select the thumbs down button.

When you provide feedback, share as much information as possible. For example, include what you expected to see, what was missing or incorrect, and any relevant context. The more detail you share, the better we can understand your feedback and continuously improve responses.

:::image type="content" source="/power-apps/user/media/microsoft-365-copilot-feedback.png" alt-text="Screenshot of Microsoft 365 Copilot in a model-driven app, highlighting the thumbs up and thumbs down feedback buttons for a response." lightbox="/power-apps/user/media/microsoft-365-copilot-feedback.png":::

## Microsoft 365 Copilot suggested questions

To help you get started, Microsoft 365 Copilot suggests questions to ask. Many suggested questions have placeholders you replace with appropriate text.

:::image type="content" source="/power-apps/user/media/microsoft-365-copilot-prompts.png" alt-text="Screenshot that shows suggested prompts that have placeholders." lightbox="/power-apps/user/media/microsoft-365-copilot-prompts.png":::

## Use agents in Microsoft 365 Copilot

> [!IMPORTANT]
>
> When you explicitly select an agent in Microsoft 365 Copilot in apps, the agent no longer answers questions about the Dataverse table or SharePoint list data in the app unless you explicitly configure your agent to do so. However, the agent uses information from the chat history. To get the side chat to answer questions about the Dataverse table or SharePoint list data in the app again, you need to remove the explicit agent selection.

Microsoft 365 Copilot in apps lets you use any agent available in Microsoft 365 Copilot right from the side pane. Once an agent is available within Microsoft 365 Copilot, you can interact with your agent by either choosing it from the navigation panel or @ mentioning it.

:::image type="content" source="/power-apps/user/media/microsoft-365-copilot-opened-navigation.png" alt-text="Screenshot that shows how to open the Microsoft 365 Copilot navigation panel with different agents displayed." lightbox="/power-apps/user/media/microsoft-365-copilot-opened-navigation.png":::

One of the benefits of @ mentioning an agent is that you can add or remove it from an ongoing conversation, which lets you have several agents collaborating in one conversation. When you select an agent from the navigation panel, you have a direct conversation only with the agent you selected.

:::image type="content" source="/power-apps/user/media/microsoft-365-copilot-at-mention.png" alt-text="Screenshot that shows how to @ mention agents in Microsoft 365 Copilot.":::

## Limitations

- M365 Copilot in canvas apps supports apps that use either SharePoint or Dataverse as a data source but not both within the same app.
- During the initial preview phase, for SharePoint, only applications containing a single SharePoint list will return answers to questions.
- If your canvas app connects to a SharePoint list through an environment variable, Microsoft 365 Copilot responses will not reference data from that SharePoint list.
- Microsoft 365 Copilot for canvas apps allows users to view data by using read-only operations. This capability means that users can only view data that matches their queries and can't make any changes. To make changes, customization with an agent is required.
- Microsoft 365 Copilot for canvas apps isn't available in the Power Apps mobile app.
- As this feature is being gradually deployed, certain settings in the Power Platform Admin Center might not be accessible yet, depending on the geographic location of your tenant.

## Related information

- [Customize Microsoft 365 Copilot with an agent](../maker/model-driven-apps/customize-microsoft-365-copilot-chat.md)
- [Add Microsoft 365 Copilot for app users in canvas apps (preview)](../maker/canvas-apps/microsoft-365-copilot-canvas-app.md)
