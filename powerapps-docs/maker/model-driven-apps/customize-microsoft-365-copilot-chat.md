---
title: Customize Microsoft 365 Copilot chat in model-driven apps (preview)
description: Learn how to customize Microsoft 365 Copilot chat with declarative agents, custom engine agents, and Copilot Studio agents in Power Apps model-driven apps.
author: Mattp123
ms.service: powerapps
ms.subservice: mda-maker
ms.author: hemantg
ms.reviewer: matp
ms.date: 12/12/2025
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

Microsoft 365 Copilot chat in model-driven apps enables users to interact with custom agents that extend Copilot's capabilities beyond standard functionality. By customizing agents, you can create tailored experiences that address your organization's specific business processes and data requirements. For more information, see [Use agents in Microsoft 365 Copilot](../../user/use-microsoft-365-copilot-model-driven-apps.md#use-agents-in-microsoft-365-copilot)

This article describes the different types of agents you can build and integrate with Microsoft 365 Copilot chat in model-driven apps. You'll learn about the capabilities and use cases for each agent type, helping you choose the right approach for your customization needs.

> [!IMPORTANT]
>
> - This feature is in preview.  
> - Preview features aren't meant for production use and might have restricted functionality These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?linkid=2189520), and are available before an official release so that customers can get early access and provide feedback.
> - This feature is in the process of rolling out and might not be available in your region yet.


You can customize agents in several ways to fit your organization's needs.

|Agent Type  |Description  |Common use cases  |
|---------|---------|---------|
|Declarative Agent     |   Configured using low-code tools and templates, allowing quick setup for common scenarios within Microsoft 365 Copilot.      |   Automating routine tasks, answering FAQs, and providing guided workflows.      |
|Custom Engine Agent     |   Developed with custom logic and integrations, offering advanced capabilities tailored to specific business needs.      |   Complex business processes, custom data integrations, and specialized automation.      |
|Copilot Studio Agent     |    Built and managed in Microsoft Copilot Studio, enabling integration with Teams and Microsoft 365 for conversational experiences.     |    Interactive chatbots, team collaboration, and personalized support within Microsoft 365 apps.     |

Use the following information to find the best solution for your organization:

- [Microsoft 365 Copilot Agents Overview](/microsoft-365-copilot/extensibility/agents-overview) documentation provides guidance on how to [choose what type of agent to build](/microsoft-365-copilot/extensibility/agents-overview#choose-what-type-of-agent-to-build).
 - Create agents as  [Declarative Agents for Microsoft 365 Copilot](/microsoft-365-copilot/extensibility/overview-declarative-agent) or as [Custom engine agents for Microsoft 365](/microsoft-365-copilot/extensibility/overview-custom-engine-agent).
 - Use [Microsoft Copilot Studio](/microsoft-copilot-studio/fundamentals-what-is-copilot-studio) to [connect and configure an agent for Teams and Microsoft 365](/microsoft-copilot-studio/publication-add-bot-to-microsoft-teams), making it available in Microsoft 365 Copilot Chat.
 - Review guidance on how to [Choose between Microsoft 365 Copilot and Copilot Studio to build your agent](/microsoft-365-copilot/extensibility/copilot-studio-experience).

> [!NOTE]
> When you select an agent in Microsoft 365 Copilot chat in a model-driven app, the agent doesn't answer Dataverse data questions unless you configure it to do so. It does use information from your chat history that might have information about your data. To allow questions about your Dataverse data, remove the selected agent.

## Related information

- [Add Microsoft 365 Copilot chat for app users in model-driven apps (preview)](add-microsoft-365-copilot.md)
- [Use Microsoft 365 Copilot chat in model-driven apps](../../user/use-microsoft-365-copilot-model-driven-apps.md)
