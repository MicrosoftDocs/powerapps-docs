---
title: Customize M365 Copilot chat in model-driven apps
description: Learn how to customize M365 Copilot chat in model-driven apps
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
# Customize M365 Copilot chat with an agent (preview)

> [!IMPORTANT]
>
> - This is a preview feature.
> - Preview features aren't meant for production use and might have restricted functionality. These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?linkid=2216214), and are available before an official release so that customers can get early access and provide feedback.
>
> When you explicitly select an agent in M365 Copilot chat in model-driven apps, the agent will no longer answer questions about the Dataverse table data in the app unless you have explicitly configured your agent to do so.  However, the agent will use information from the chat history.  To get the side chat to answer questions about the Dataverse table data in the app again, you will need to remove the explicit agent selection.

M365 Copilot chat in model-driven apps allows you to use any agent available in M365 Copilot right from the side pane. Once an agent is available within M365 Copilot, you can interact with your agent by either choosing it from the navigation panel or @ mentioning it.

:::image type="content" source="media/m365-copilot-open-nav-panel.png" alt-text="Screenshot that shows how to open the M365 Copilot navigation panel.":::
:::image type="content" source="media/m365-copilot-nav-panel-agents.png" alt-text="Screenshot that shows agents in the M365 Copilot navigation panel.":::
:::image type="content" source="media/m365-copilot-at-mention.png" alt-text="Screenshot that shows how to @ mention agents in M365 Copilot.":::

Within the M365 Copilot [Agents Overview](https://learn.microsoft.com/microsoft-365-copilot/extensibility/agents-overview) documention, there is also guidance on how to [Choose what type of agent to build](https://learn.microsoft.com/microsoft-365-copilot/extensibility/agents-overview#choose-what-type-of-agent-to-build). You can create agents as [Declarative Agents for Microsoft 365 Coiplot](https://learn.microsoft.com/microsoft-365-copilot/extensibility/overview-declarative-agent) or as [Custom engine agents for Microsoft 365](https://learn.microsoft.com/microsoft-365-copilot/extensibility/overview-custom-engine-agent). A popular Power Platform option is to use [Microsoft Copilot Studio](https://learn.microsoft.com/microsoft-copilot-studio/fundamentals-what-is-copilot-studio), then [Connect and configure an agent for Teams and Microsoft 365](https://learn.microsoft.com/microsoft-copilot-studio/publication-add-bot-to-microsoft-teams) to make it available within M365 Copilot Chat.

## Related information

- [Add M365 Copilot chat to model-driven apps](../model-driven-apps/add-m365-copilot.md)
- [Use M365 Copilot chat in model-driven apps](../model-driven-apps/use-m365-copilot-model-driven-apps.md)
