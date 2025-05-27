---
title: "Supervise agents in model-driven apps with agent feed" 
description: Learn how to supervise agents with agent feed in your model-driven app.
ms.date: 05/22/2025
ms.reviewer: ""
ms.topic: ""
author: "jacobwilkinson"
ms.subservice: 
ms.author: ""
contributors: 
ms.service: "powerapps"
search.audienceType: 
  - 
---
# Supervise agents in model-driven apps with agent feed (preview)

[!INCLUDE [preview-banner](~/../shared-content/shared/preview-includes/preview-banner.md)]

The agent feed in Power Apps introduces an intuitive experience for business users to manage and collaborate with agents directly within their apps—transforming apps into the central hub for human-agent collaboration by surfacing a comprehensive activity feed that shows what agents are doing on their behalf, wherever they are in the app. 

## Prerequisites
- Agent feed is available in model-driven apps with the modern, refreshed look enabled. 
- The agent feed is displayed when at least one agent is to be supervised in the app.  
- Generative agents must be enabled in the environment. 

> [!IMPORTANT]
>
> - This is a preview feature.
> - Preview features aren't meant for production use and might have restricted functionality. These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?linkid=2216214), and are available before an official release so that customers can get early access and provide feedback.
> - This feature is being gradually rolled out across regions and might not be available yet in your region.

> [!NOTE]
> Currently, only the owner of an agent can view and supervise that agent’s data in a model-driven app. Support for sharing agent history with other users is a top priority and is actively being developed.

## Use agent feed to supervise agents
Once enabled, agent feed appears at the top of the site map in a model-driven app.
> :::image type="content" source="media/agent-supervision/agent-feed-sitemap.png" alt-text="Agent feed sitemap":::

The feed can be viewed in the side pane or expanded into a full screen.
> :::image type="content" source="media/agent-supervision/agent-feed-expand.png" alt-text="Agent feed expand":::
> :::image type="content" source="media/agent-supervision/agent-feed-collapse.png" alt-text="Agent feed collapse":::

The feed displays a list of agent activity, each showing:
1. The last step taken by the agent
1. A timestamp of the most recent activity
1. The agent's name and icon
> :::image type="content" source="media/agent-supervision/agent-feed-card-map.png" alt-text="Agent feed card map":::

Activity is grouped into two sections:
- **To-do**: Displays actions that require user attention, such as those that failed, completed with errors, or are waiting for input. 
- **Other**: Displays all other action types, including those completed by the agent or user, dismissed actions, and those still in progress.

By default, 25 actions are loaded into each section. Select **See more** at the bottom of a section to load 25 additional actions. Refreshing the feed resets the view to the first 25 actions in each section. The sections are sorted chronologically based on the last modification of each action. 

Selecting an action opens a detailed view that includes: 
1. An AI-generated summary of the agent's actions
1. Error details for actions that need assistance
1. A step-by-step activity map of the agent's execution
> :::image type="content" source="media/agent-supervision/agent-feed-details-pane-map.png" alt-text="Agent feed details map":::

The activity map begins with the trigger that initiated the action and continues through each step taken by the agent. These steps may include tools, connectors, topics, or knowledge sources configured by the agent’s creator. This view is similar to the Activity view in Copilot Studio and provides a clear visualization of the agent’s logic and behavior. 

You can filter the feed by agent or by status. Available status filters include: 
|Filter|Description|
|-----|------|
|**Needs assistance**|The action failed, completed with errors, or is waiting for user input.|
|**Completed by user**|The action previously needed assistance but was marked complete by the user.|
|**Completed by agent**|The action was completed successfully by the agent.|
|**Dismissed**|The action was dismissed by the user after being flagged as needing assistance.|
|**In progress**|The action is currently being executed by the agent.|

Agent feed can be viewed in a side pane to support multitasking or expanded to full screen for focused review. 

## Take action on agent activity
Users can take the following actions on activity in the feed:
- **Mark as complete**: Move an action from the **To-do** section to **Other** after completing the task the agent could not finish.
  > :::image type="content" source="media/agent-supervision/agent-feed-mark-complete.png" alt-text="Agent feed mark as complete button":::
- **Dismiss**: Remove an action from the **To-do** section if it is no longer relevant. This option is only visible when hovering over an agent action in the feed.
  > :::image type="content" source="media/agent-supervision/agent-feed-dismiss.png" alt-text="Agent feed dismiss button":::
- **Undo**: Revert a previous mark-as-complete or dismiss action if it was done in error. This option is also only visible when hovering over an agent action in the feed.
  > :::image type="content" source="media/agent-supervision/agent-feed-undo.png" alt-text="Agent feed undo button":::

> [!NOTE]
> All actions can be performed either from the main screen in the feed or from the details page of a specific action. 

## Navigation
For actions that use a Dataverse tool, users will be provided with a direct link to either the Dataverse record or entity associated with that action depending on which is more relevant to that action. This enables seamless for further review or follow-up. 
> :::image type="content" source="media/agent-supervision/agent-feed-navigate-to-record.png" alt-text="Agent feed record navigation button":::

## Related information

[Add agents to an app](/maker/model-driven-apps/add-agents-to-app.md)<br/>
[Customize Copilot Chat](customize-copilot-chat.md)
