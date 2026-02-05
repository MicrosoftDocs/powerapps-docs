---
title: "Add agents to your model-driven app" 
description: Learn how to add agents to your model-driven app in Power Apps.
ms.date: 02/04/2026
ms.reviewer: matp
ms.topic: how-to
author: adrianorth
ms.subservice: mda-maker
ms.author: aorth
contributors: Jacob-Wilkinson, HemantGaur
ms.service: powerapps
search.audienceType: 
  - maker
---
# Add agents to your model-driven app (preview)

[!INCLUDE [preview-banner](~/../shared-content/shared/preview-includes/preview-banner.md)]

Model-driven apps support the use of agents to enhance user productivity and automate tasks. There are two types of agents available in model-driven apps: 

- *Autonomous agents*, created in Microsoft Copilot Studio, collaborate with users through the new Power Apps MCP Server, allowing agents to generate actionable agent feed tasks for users to review results or step in with inputs to unblock and complete Human‑in‑the‑Loop flows.

- *App assistant agents*, which can be created to provide custom topics, knowledge sources, and more within the model-driven app.

:::image type="content" source="media/add-agents-to-app/app-designer-agent-tab.png" alt-text="App designer Agents pane" lightbox="media/add-agents-to-app/app-designer-agent-tab.png":::

> [!IMPORTANT]
>
> - This is a preview feature.
> - Preview features aren't meant for production use and might have restricted functionality. These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?linkid=2216214), and are available before an official release so that customers can get early access and provide feedback.
> - This feature is available only in the English language and it replaces older Microsoft Copilot Studio activity based agent feed version

Autonomous agents can be added to model-driven apps to help users get work done faster. Using Power Apps MCP Server, agents can post actionable tasks for user review, allowing human to validate results, step in when needed, and finish work the agent couldn’t complete—without leaving their app.

[Learn more about how to supervise agents](../../user/supervise-agents-with-agent-feed.md)

> [!IMPORTANT]
> Currently, agent feed items in model‑driven apps are visible to all users who have access to the Agent Task table. To prevent unintended exposure, agents configured to various apps should not log tasks targeted at specific users.

## Add an autonomous agent to an app

You can add an agent to any model-driven app of your choosing. We recommend adding agents to model-driven apps that have related data. 

> [!NOTE]
> To be eligible for addition to an app, an agent must be connected to Power Apps MCP Server or be published. A maker can verify an agent's eligibility to be added to an app via the right-hand properties pane where the requirements for an agent to be added to an app are displayed. The **Add to app** button is disabled for any agents that don't meet the requirements to be eligible for addition.
> :::image type="content" source="media/add-agents-to-app/app-designer-properties-pane.png" alt-text="App Designer Properties pane":::

1. Sign in to Power Apps, select **Apps**, and then select **Edit** for the app you want to modify.
1. In the app designer, go to the **Agents** tab.
1. Under the **Agent feed** dropdown, the **In your environment** dropdown appears that lists all agents in your environment. Locate the agent you want to add.
1. Select **...** (more options) next to the agent, and then select **Add to app**.
    :::image type="content" source="media/add-agents-to-app/app-designer-add-agent-to-app.png" alt-text="App designer add agent to app":::
1. Verify agent feed is added to your app with all added agents by saving, publishing, and playing your app. Previewing agent feed in the app designer isn't currently supported.
1. To view or edit the agent in Copilot Studio, select **Edit in Microsoft Copilot Studio**.
   :::image type="content" source="media/add-agents-to-app/app-designer-edit-in-copilot-studio.png" alt-text="App Designer edit in Copilot Studio":::

> [!IMPORTANT]
> Use the **Create agent** button to open Copilot Studio for agent creation. Note that even if the agent is created through a link inside the app designer, the maker must ensure it meets all requirements to be added to the app.

## Remove an autonomous agent from an app

1. In the app designer, go to the **Agents** tab.
1. In the **Agent feed** dropdown, select **In your feed**.
1. Locate the agent you want to remove, select **...**, and then select **Remove from feed**.

> :::image type="content" source="media/add-agents-to-app/app-designer-remove-agent.png" alt-text="App designer remove agent from app":::

> [!NOTE]
> Removing an agent from an app doesn't remove the agent from the environment.

## Working with an app assistant agent

The app assistant agent makes a model-driven app more intelligent and relevant for your organization by adding additional topics, knowledge sources, and more. The [Copilot Chat](add-ai-copilot.md), Agent APIs, and agent response components access the topics within this agent. Learn more at [Add app assistant agent](add-app-assistant-agent.md).

:::image type="content" source="media/add-agents-to-app/app-designer-app-assistant-agent-not-configured.png" alt-text="App Designer Agents pane App assistant agent":::

> [!NOTE]
> The app assistant agent is a rename of interactive agent, which is the improved experience for **... > Configure in Copilot Studio**. The agents created with the previous experiences are now shown as the **App assistant agent**.

## Related information

[Overview of App Designer](app-designer-overview.md)

[Add app assistant agent](add-app-assistant-agent.md)
