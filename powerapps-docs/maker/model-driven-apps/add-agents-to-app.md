---
title: "Add agents to your model-driven app" 
description: Learn how to add agents to your model-driven app in Power Apps.
ms.date: 06/04/2025
ms.reviewer: "matp"
ms.topic: "how-to"
author: "adrianorth"
ms.subservice: mda-maker
ms.author: "aorth"
contributors: Jacob-Wilkinson
ms.service: "powerapps"
search.audienceType: 
  - maker
---
# Add agents to your model-driven app (preview)

[!INCLUDE [preview-banner](~/../shared-content/shared/preview-includes/preview-banner.md)]

Model-driven apps support the use of agents to enhance user productivity and automate tasks. There are two types of agents available in model-driven apps: 

- *Autonomous agents*, created in Microsoft Copilot Studio, can be added to apps for supervised execution by users.

- *Interactive agents*, which can be created to provide custom topics, knowledge sources, and more within the model-driven app.

:::image type="content" source="media/add-agents-to-app/app-designer-agent-tab.png" alt-text="App designer Agents pane" lightbox="media/add-agents-to-app/app-designer-agent-tab.png":::

> [!IMPORTANT]
>
> - This is a preview feature.
> - Preview features aren't meant for production use and might have restricted functionality. These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?linkid=2216214), and are available before an official release so that customers can get early access and provide feedback.
> - This feature is being gradually rolled out across regions and might not be available yet in your region.
> - To access the feature, you must use an [early release cycle environment](/power-platform/admin/early-release#create-early-release-cycle-environments) and use [https://make.preview.powerapps.com/](https://make.preview.powerapps.com/)

Autonomous agents can be added to model-driven apps to assist users with task completion. When added to an app, these agents can be supervised by users, allowing them to validate completed tasks, intervene when errors occur, and complete tasks that the agent was unable to finish—all within the context of their regular workflows.

[Learn more about how to supervise agents](../user/supervise-agents-with-agent-feed.md)

> [!IMPORTANT]
> Currently, only the owner of an agent can view and supervise that agent’s data in a model-driven app.

## Add an autonomous agent to an app

You can add an agent to any model-driven app of your choosing. We recommend adding agents to model-driven apps that have related data. 

> [!NOTE]
> To be eligible for addition to an app, an agent must be published, have [generative AI enabled](/microsoft-copilot-studio/advanced-generative-actions), and include at least one [trigger](/microsoft-copilot-studio/authoring-triggers-about). A maker can verify an agent's eligibility to be added to an app via the right-hand properties pane where the requirements for an agent to be added to an app are displayed. The **Add to app** button is disabled for any agents that don't meet the requirements to be eligible for addition.
:::image type="content" source="media/add-agents-to-app/app-designer-properties-pane.png" alt-text="App Designer Properties pane":::

1. Sign in to Power Apps, select **Apps**, and then select **Edit** for the app you want to modify.
1. In the app designer, go to the **Agents** tab.
1. In the **In your environment** dropdown list all agents in your environment are displayed. Locate the agent you want to add.
1. Select **...** (more options) next to the agent, and then select **Add to app**.
    :::image type="content" source="media/add-agents-to-app/app-designer-add-agent-to-app.png" alt-text="App designer add agent to app":::
1. Verify agent feed has been added to your app with all added agents by saving, publishing, and playing your app. Previewing agent feed in the app designer isn't currently supported.
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

## Working with an interactive agent

The interactive agent makes a model-driven app more intelligent and relevant for your organization by adding additional topics, knowledge sources, and more. The [Copilot Chat](add-ai-copilot.md), Agent APIs, and agent response components access the topics within this agent.

> :::image type="content" source="media/add-agents-to-app/app-designer-interactive-agent.png" alt-text="App Designer Agents pane Interactive agent":::

> [!NOTE]
> The interactive agent is the improved experience for **... > Configure in Copilot Studio** and is gradually rolling out. The agents created with the previous experience are now shown as the **Interactive agent**.

### Creating an interactive agent

When an interactive agent is created, it's named as **Copilot in Power Apps - \<app name\>**. The created agent is associated with the app when saved and published.

1. In the app designer, select the **Agents** pane.
1. Expand **In your app** > **AI capabilities**.
1. On **Interactive agent**, select **...** > **Configure**.
1. Select **Configure in Copilot Studio** to create the agent.
1. While the agent is being created, **Setting up your app's copilot** is shown in the popup.

   A new browser tab for **Copilot Studio** is opened with the new agent.
   > [!NOTE]
   > Pop-ups need to be enabled in your web browser to allow editing the created agent.
1. Select refresh in pane header after popup to show the created agent.
   > :::image type="content" source="media/add-agents-to-app/app-designer-interactive-agent-created.png" alt-text="Interactive agent with created agent":::
1. Switch to the **Copilot Studio** browser tab to add topics, knowledge, and so on, to the agent.
1. Save and publish the agent.
1. Switch to the app designer browser tab to save and publish the app.

## Related information

[Overview of App Designer](app-designer-overview.md)<br/>
[Customize Copilot Chat](customize-copilot-chat.md)
