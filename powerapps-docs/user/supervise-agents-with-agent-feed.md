---
title: "Supervise agents in model-driven apps with agent feed" 
description: Learn how to supervise agents with agent feed in your model-driven app.
ms.date: 05/22/2025
ms.reviewer: "smurkute"
ms.topic: "how-to"
author: "jacobwilkinson"
ms.subservice: end-user
ms.author: "jacwilkinson"
contributors: 
ms.service: "powerapps"
search.audienceType: 
  - enduser
---
# Supervise agents in model-driven apps with agent feed (preview)

[!INCLUDE [preview-banner](~/../shared-content/shared/preview-includes/preview-banner.md)]

Agent feed in Power Apps lets business users easily manage and work with agents directly in their apps. It makes apps a central hub for human-agent collaboration by showing a complete activity feed of what agents do for them, wherever they are in the app. 

## Prerequisites

- The agent feed shows when at least one agent is supervised in the app.
- Learn how to [Add agents to an app](../maker/model-driven-apps/add-agents-to-app.md)

> [!IMPORTANT]
>
> - This is a preview feature.
> - Preview features aren't meant for production use and might have restricted functionality. These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?linkid=2216214), and are available before an official release so that customers can get early access and provide feedback.
> - This feature is being gradually rolled out across regions and might not be available yet in your region.
> - This feature is only available in the English language.

> [!NOTE]
> Currently, only the owner of an agent can view and supervise that agent’s data in a model-driven app. Support for sharing agent history with other users is a top priority and is in development.

## Use agent feed to supervise agents

When you enable agent feed, it appears at the top of the site map in a model-driven app.
   :::image type="content" source="media/agent-supervision/agent-feed-sitemap.png" alt-text="Agent feed sitemap" lightbox="media/agent-supervision/agent-feed-sitemap.png":::

You can view the feed in the side pane or expand it to full screen.
   :::image type="content" source="media/agent-supervision/agent-feed-expand.png" alt-text="Agent feed expand":::
   :::image type="content" source="media/agent-supervision/agent-feed-collapse.png" alt-text="Agent feed collapse":::

The feed shows a list of agent activity. Each item includes:

1. The last step taken by the agent
1. A timestamp of the most recent activity
1. The agent's name and icon
   :::image type="content" source="media/agent-supervision/agent-feed-card-map.png" alt-text="Agent feed card map":::

> [!NOTE]
> You can only supervise up to ten agents at a time in the feed.

Activity is grouped into two sections:

- **To-do**: Shows actions that need your attention, like those that failed, completed with errors, or are waiting for input.
- **Other**: Shows all other action types, including those completed by the agent or user, dismissed actions, and those still in progress.

By default, 25 actions load in each section. Select **See more** at the bottom of a section to load 25 more actions. Refreshing the feed resets the view to the first 25 actions in each section. The sections are sorted chronologically by the last modification of each action.

Select an action to open a detailed view that includes:

1. An AI-generated summary of the agent's actions
1. Error details for actions that need assistance
1. A step-by-step activity map of the agent's execution
   :::image type="content" source="media/agent-supervision/agent-feed-details-pane-map.png" alt-text="Agent feed details map":::

The activity map starts with the trigger that initiates the action and continues through each step the agent takes. These steps can include tools, connectors, articles, or knowledge sources set up by the agent’s creator. This view is similar to the Activity view in Copilot Studio and gives a clear visualization of the agent’s logic and behavior.

You can filter the feed by agent or by status. Available status filters include:

|Filter|Description|
|-----|------|
|**Needs assistance**|The action failed, completed with errors, or is waiting for user input.|
|**Completed by user**|The action previously needed assistance but was marked complete by the user.|
|**Completed by agent**|The action was completed successfully by the agent.|
|**Dismissed**|The action was dismissed by the user after being flagged as needing assistance.|
|**In progress**|The action is currently being executed by the agent.|

View agent feed in a side pane to support multitasking or expand it to full screen for focused review.

## Take action on agent activity

> [!NOTE]
> The actions you take on agent actions only change their status. You need to manually take over the agent action and fix it as needed. We're developing more robust human-in-the-loop capabilities.

You can take these actions on activity in the feed:

- **Mark as complete**: Move an action from the **To-do** section to **Other** after completing the task the agent couldn't finish.

   :::image type="content" source="media/agent-supervision/agent-feed-mark-complete.png" alt-text="Agent feed mark as complete button":::

- **Dismiss**: Remove an action from the **To-do** section if it's no longer relevant. You see this option only when you hover over an agent action in the feed.

   :::image type="content" source="media/agent-supervision/agent-feed-dismiss.png" alt-text="Agent feed dismiss button":::

- **Undo**: Revert a previous mark-as-complete or dismiss action if you did it by mistake. You see this option only when you hover over an agent action in the feed.

   :::image type="content" source="media/agent-supervision/agent-feed-undo.png" alt-text="Agent feed undo button":::

> [!NOTE]
> All actions can be performed either from the main screen in the feed or from the details page of a specific action. 

## Navigation

For actions that use a Dataverse tool, users will be provided with a direct link to either the Dataverse record or entity associated with that action depending on which is more relevant to that action. This enables seamless for further review or follow-up. 

:::image type="content" source="media/agent-supervision/agent-feed-navigate-to-record.png" alt-text="Agent feed record navigation button":::

> [!NOTE]
> Direct links aren't currently supported for non-Dataverse tools.

## Related information

[Add agents to an app](../maker/model-driven-apps/add-agents-to-app.md)     
[Customize Copilot Chat](../maker/model-driven-apps/customize-copilot-chat.md)
