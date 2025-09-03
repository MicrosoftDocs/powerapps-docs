---
title: "Add an app assistant agent to your model-driven app" 
description: Learn how to add an app assistant agent to your model-driven app in Power Apps.
ms.date: 09/03/2025
ms.reviewer: matp
ms.topic: how-to
author: adrianorth
ms.subservice: mda-maker
ms.author: aorth
ms.service: powerapps
search.audienceType: 
  - maker
---
# Add an app assistant agent to your model-driven app (preview)

The app assistant agent makes a model-driven app more intelligent and relevant for your organization by adding additional topics, knowledge sources, and more. The [Copilot Chat](add-ai-copilot.md), Agent APIs, and agent response components access the topics within this agent.

:::image type="content" source="media/add-agents-to-app/app-designer-app-assistant-agent-not-configured.png" alt-text="App Designer Agents pane App assistant agent":::

[!INCLUDE [preview-note-pp.md](../../../shared/preview-includes/preview-note-pp.md)]

> [!NOTE]
> The app assistant agent is a rename of interactive agent, which is the improved experience for **... > Configure in Copilot Studio**. The agents created with the previous experiences are now shown as the **App assistant agent**.

## Create an app assistant agent

When an app assistant agent is created, it's named as **Copilot in Power Apps - \<app name\>**. The created agent is associated with the app when the app is saved and published.

1. In the app designer, select the **Agents** pane.
1. Expand **Agent assistance**.
1. On **App assistant agent**, select **...** > **Configure**.

   A new browser tab for **Copilot Studio** is opened with the new agent.
   > [!NOTE]
   > Pop-ups need to be enabled in your web browser to allow editing the created agent.
1. After configure completes, the right pane is expanded showing the status of **Not published** and the agent name.
   :::image type="content" source="media/add-agents-to-app/app-designer-app-assistant-agent-not-published.png" alt-text="App assistant agent property pane not published":::
1. Switch to the **Copilot Studio** browser tab or select **Edit in Copilot Studio** to add topics, knowledge, and so on, to the agent.
1. Save and publish the agent.
1. Switch to the app designer browser tab and select refresh in **Agents** pane header to show agent published status.
   :::image type="content" source="media/add-agents-to-app/app-designer-app-assistant-agent-last-published.png" alt-text="App assistant agent last published status":::
1. In the app designer, save and publish the app.

### Editing an app assistant agent

After the app assistant agent has been initially configured, it can be edited from either the **Agents** pane or the **App assistant agent property** pane.

**Agent** pane:

1. In the app designer, select the **Agents** pane.
1. Expand **Agent assistance**.
1. On **App assistant agent**, select **...** > **Edit in Copilot Studio**.

**App assistant agent** property pane:

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

[Overview of App Designer](app-designer-overview.md)

[Add agents to your model-driven app](add-agents-to-app.md)

[Customize Copilot Chat](customize-copilot-chat.md)

