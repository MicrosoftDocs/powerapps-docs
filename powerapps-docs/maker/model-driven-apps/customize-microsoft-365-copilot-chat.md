---
title: Customize Microsoft 365 Copilot chat in model-driven apps (preview)
description: Learn how to customize Microsoft 365 Copilot chat in model-driven apps
author: Mattp123
ms.service: powerapps
ms.subservice: mda-maker
ms.author: hemantg
ms.reviewer: matp
ms.date: 05/21/2025
ms.update-cycle: 180-days
ms.topic: how-to
applies_to: 
  - "powerapps"
search.audienceType: 
  - maker
contributors:
  - makolomi
  - Jacob-Wilkinson
ms.collection: bap-ai-copilot
ai-usage: ai-assisted
---
# Customize Microsoft 365 Copilot chat with an agent (preview)

Microsoft 365 Copilot chat in model-driven apps lets you use any agent available in Microsoft 365 Copilot right from the side pane. When an agent is available within Micrsoft 365 Copilot, you can interact with your agent by either choosing it from the navigation panel or @ mentioning it. One of the benefits of @ mentioning an agent is that you can add or remove it from an ongoing conversation, which allows you to have several agents collaborating in one conversation. When you select an agent from the navigation panel, you have a direct conversation only with the agent you selected.

:::image type="content" source="media/m365-copilot-at-mention.png" alt-text="Screenshot that shows how to @ mention agents in Microsoft 365 Copilot.":::
:::image type="content" source="media/m365-copilot-open-nav-panel.png" alt-text="Screenshot that shows how to open the Microsoft 365 Copilot navigation panel.":::
:::image type="content" source="media/m365-copilot-nav-panel-agents.png" alt-text="Screenshot that shows agents in the Microsoft 365 Copilot navigation panel.":::

The Microsoft 365 Copilot [Agents Overview](/microsoft-365-copilot/extensibility/agents-overview) documentation also provides guidance on how to [Choose what type of agent to build](/microsoft-365-copilot/extensibility/agents-overview#choose-what-type-of-agent-to-build). You can create agents as [Declarative Agents for Microsoft 365 Coiplot](/microsoft-365-copilot/extensibility/overview-declarative-agent) or as [Custom engine agents for Microsoft 365](/microsoft-365-copilot/extensibility/overview-custom-engine-agent). A popular Power Platform option is to use [Microsoft Copilot Studio](/microsoft-copilot-studio/fundamentals-what-is-copilot-studio), then [Connect and configure an agent for Teams and Microsoft 365](/microsoft-copilot-studio/publication-add-bot-to-microsoft-teams) to make it available within Microsoft 365 Copilot Chat. There's also guidance on how to [Choose between Microsoft 365 Copilot and Copilot Studio to build your agent](/microsoft-365-copilot/extensibility/copilot-studio-experience).

> [!IMPORTANT]
>
> - This is a preview feature.
> - Preview features aren't meant for production use and might have restricted functionality. These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?linkid=2216214), and are available before an official release so that customers can get early access and provide feedback.
>
> When you explicitly select an agent in Microsoft 365 Copilot chat in model-driven apps, the agent no longer answers questions about the Dataverse table data in the app unless you explicitly configure your agent to do so. However, the agent uses information from the chat history. To get the side chat to answer questions about the Dataverse table data in the app again, you need to remove the explicit agent selection.

## Related information

- [Add Microsoft 365 Copilot for app users in model-driven apps (preview)](add-microsoft-365-copilot.md)
- [Use Microsoft 365 Copilot chat in model-driven apps](../../user/use-microsoft-365-copilot-model-driven-apps.md)
