---
title: Customize Microsoft 365 Copilot chat in model-driven apps (preview)
description: Learn how to customize Microsoft 365 Copilot chat with declarative agents, custom engine agents, and Copilot Studio agents in Power Apps model-driven apps.
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

Microsoft 365 Copilot chat in model-driven apps enables users to interact with custom agents that extend Copilot's capabilities beyond standard functionality. By customizing agents, you can create tailored experiences that address your organization's specific business processes and data requirements.

This article describes the different types of agents you can build and integrate with Microsoft 365 Copilot chat in model-driven apps. You'll learn about the capabilities and use cases for each agent type, helping you choose the right approach for your customization needs.

> [!IMPORTANT]
>
> - This is a preview feature.
> - Preview features aren't meant for production use and might have restricted functionality. > - These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?linkid=2216214), and are available before an official release so that customers can get early access and provide feedback.

You can customize agents in several ways to fit your organization's needs.

|Agent Type  |Description  |Common use cases  |
|---------|---------|---------|
|Declarative Agent     |   Configured using low-code tools and templates, allowing quick setup for common scenarios within Microsoft 365 Copilot.      |   Automating routine tasks, answering FAQs, and providing guided workflows.      |
|Custom Engine Agent     |   Developed with custom logic and integrations, offering advanced capabilities tailored to specific business needs.      |   Complex business processes, custom data integrations, and specialized automation.      |
|Copilot Studio Agent     |    Built and managed in Microsoft Copilot Studio, enabling integration with Teams and Microsoft 365 for conversational experiences.     |    Interactive chatbots, team collaboration, and personalized support within Microsoft 365 apps.     |

- The [Microsoft 365 Copilot Agents Overview](/microsoft-365-copilot/extensibility/agents-overview) documentation provides guidance on how to [choose what type of agent to build](/microsoft-365-copilot/extensibility/agents-overview#choose-what-type-of-agent-to-build).
 - You can create agents as  [Declarative Agents for Microsoft 365 Copilot](/microsoft-365-copilot/extensibility/overview-declarative-agent) or as [Custom engine agents for Microsoft 365](/microsoft-365-copilot/extensibility/overview-custom-engine-agent).
 - A popular Power Platform option is to use [Microsoft Copilot Studio](/microsoft-copilot-studio/fundamentals-what-is-copilot-studio), then [connect and configure an agent for Teams and Microsoft 365](/microsoft-copilot-studio/publication-add-bot-to-microsoft-teams) to make it available within Microsoft 365 Copilot Chat. 
 - There's also guidance on how to [Choose between Microsoft 365 Copilot and Copilot Studio to build your agent](/microsoft-365-copilot/extensibility/copilot-studio-experience).

> [!NOTE]
> When you explicitly select an agent in Microsoft 365 Copilot chat in model-driven apps, the agent no longer answers questions about the Dataverse table data in the app unless you explicitly configure your agent to do so. However, the agent uses information from the chat history. To get the side chat to answer questions about the Dataverse table data in the app again, you need to remove the explicit agent selection.

## Related information

- [Add Microsoft 365 Copilot for app users in model-driven apps (preview)](add-microsoft-365-copilot.md)
- [Use Microsoft 365 Copilot chat in model-driven apps](../../user/use-microsoft-365-copilot-model-driven-apps.md)
