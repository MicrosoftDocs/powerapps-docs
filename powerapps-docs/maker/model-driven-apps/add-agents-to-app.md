---
title: "Add agents to your model-driven app" 
description: Learn how to add agents to your model-driven app in Power Apps.
ms.date: 08/28/2025
ms.reviewer: matp
ms.topic: how-to
author: adrianorth
ms.subservice: mda-maker
ms.author: aorth
contributors: Jacob-Wilkinson
ms.service: powerapps
search.audienceType: 
  - maker
---
# Add agents to your model-driven app (preview)

[!INCLUDE [preview-banner](~/../shared-content/shared/preview-includes/preview-banner.md)]

Model-driven apps support the use of agents to enhance user productivity and automate tasks. There are two types of agents available in model-driven apps: 

- *Autonomous agents*, created in Microsoft Copilot Studio, can be added to apps for supervised execution by users.

- *App assistant agents*, which can be created to provide custom topics, knowledge sources, and more within the model-driven app.

:::image type="content" source="media/add-agents-to-app/app-designer-agent-tab.png" alt-text="App designer Agents pane" lightbox="media/add-agents-to-app/app-designer-agent-tab.png":::

> [!IMPORTANT]
>
> - This is a preview feature.
> - Preview features aren't meant for production use and might have restricted functionality. These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?linkid=2216214), and are available before an official release so that customers can get early access and provide feedback.
> - This feature is available only in the English language.

Autonomous agents can be added to model-driven apps to assist users with task completion. When added to an app, these agents can be supervised by users, allowing them to validate completed tasks, intervene when errors occur, and complete tasks that the agent was unable to finish—all within the context of their regular workflows.

[Learn more about how to supervise agents](../../user/supervise-agents-with-agent-feed.md)

> [!IMPORTANT]
> Currently, only the owner of an agent can view and supervise that agent's data in a model-driven app.

## Add an autonomous agent to an app

You can add an agent to any model-driven app of your choosing. We recommend adding agents to model-driven apps that have related data. 

> [!NOTE]
> To be eligible for addition to an app, an agent must be published. A maker can verify an agent's eligibility to be added to an app via the right-hand properties pane where the requirements for an agent to be added to an app are displayed. The **Add to app** button is disabled for any agents that don't meet the requirements to be eligible for addition.
:::image type="content" source="media/add-agents-to-app/app-designer-properties-pane.png" alt-text="App Designer Properties pane":::
> Up to 10 agents can be added to an app at a time.

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
1. In the **In your app** dropdown, select **For supervision**.
1. Locate the agent you want to remove, select **...**, and then select **Remove from app**.

> :::image type="content" source="media/add-agents-to-app/app-designer-remove-agent.png" alt-text="App designer remove agent from app":::

> [!NOTE]
> Removing an agent from an app doesn't remove the agent from the environment.

## Working with an app assistant agent

The app assistant agent makes a model-driven app more intelligent and relevant for your organization by adding additional topics, knowledge sources, and more. The [Copilot Chat](add-ai-copilot.md), Agent APIs, and agent response components access the topics within this agent.

> :::image type="content" source="media/add-agents-to-app/app-designer-app-assistant-agent-not-configured.png" alt-text="App Designer Agents pane App assistant agent":::

> [!NOTE]
> The app assistant agent is a rename of interactive agent which is the improved experience for **... > Configure in Copilot Studio**. The agents created with the previous experiences are now shown as the **App assistant agent**.

### Creating an app assistant agent

When an app assistant agent is created, it's named as **Copilot in Power Apps - \<app name\>**. The created agent is associated with the app when the app is saved and published.

1. In the app designer, select the **Agents** pane.
1. Expand **Agent assistance**.
1. On **App assistant agent**, select **...** > **Configure**.

   A new browser tab for **Copilot Studio** is opened with the new agent.
   > [!NOTE]
   > Pop-ups need to be enabled in your web browser to allow editing the created agent.
1. After configure completes, the right pane is expanded showing the status of **Not published** and the agent name.
   > :::image type="content" source="media/add-agents-to-app/app-designer-app-assistant-agent-not-published.png" alt-text="App assistant agent property pane not published":::
1. Switch to the **Copilot Studio** browser tab or select **Edit in Copiot Studio** to add topics, knowledge, and so on, to the agent.
1. Save and publish the agent.
1. Switch to the app designer browser tab and select refresh in **Agents** pane header to show agent published status.
   > :::image type="content" source="media/add-agents-to-app/app-designer-app-assistant-agent-last-published.png" alt-text="App assistant agent last published status":::
1. In the app designer, save and publish the app.

### Editing an app assistant agent

After the app assistant agent has been initially configured, it can be edited from either the Agents pane or the App assistant agent property pane.

**Agent pane**
1. In the app designer, select the **Agents** pane.
1. Expand **Agent assistance**.
1. On **App assistant agent**, select **...** > **Edit in Copilot Studio**.

**Property pane**
1. In the app designer, select the **Agents** pane.
1. Expand **Agent assistance** and select **App assistant agent**.
1. In the property pane for App assistant agent, select **Edit in Copilot Studio**.

### Limitations

The app assistant agent isn't able to be defined or referenced in app designer for these Microsoft model-driven apps:

- Connected Field Service
- Customer Insights
- Customer Service Hub
- Customer Service workspace
- Dynamics 365 App for Outlook
- Field Service
- Field Service Mobile
- Inventory Visibility
- Omnichannel engagement hub
- Project Operations
- Sales Hub
- Sustainability

> [!NOTE]
> When a model-driven app includes both Lead and Opportunity tables, it implicitly uses the **Copilot in Dynamics 365 Sales** agent. The app designer doesn't show the app assistant agent, but the **Copilot in Dynamics 365 Sales** agent can be customized from Copilot Studio. 

## Related information

[Overview of App Designer](app-designer-overview.md)<br/>
[Customize Copilot Chat](customize-copilot-chat.md)
