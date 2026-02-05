[!INCLUDE [preview-banner](~/../shared-content/shared/preview-includes/preview-banner.md)]

Agent feed enables human-agent collaboration in apps by surfacing agent-generated, actionable tasks that users can review, validate, and complete. With agent feed, apps act as a collaboration surface where users supervise and interact with agent work through a unified, task-based feed.

## Prerequisites

- The agent feed shows when at least one agent is supervised in the app.
- Learn how to [Add agents to an app](../maker/model-driven-apps/add-agents-to-app.md)

> [!IMPORTANT]
>
> - This is a preview feature.
> - Preview features aren't meant for production use and might have restricted functionality. These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?linkid=2216214), and are available before an official release so that customers can get early access and provide feedback.
> - This feature is being gradually rolled out across regions and might not be available yet in your region.
> - This feature is only available in English language and replaces older Microsoft Copilot Studio activity-based agent feed version.

> [!NOTE]
> Currently, agent feed items in model‑driven apps are visible to all users who have access to the Agent Task table. To prevent unintended exposure, don't configure agents to log tasks targeted at specific users.

## Use agent feed to supervise agents

To allow users to view agent's activity in the app, agent must be connected to Power Apps MCP Server. Agent feed appears at the top of the site map in a model-driven app.
   :::image type="content" source="media/agent-supervision/agent-feed-sitemap.png" alt-text="Agent feed sitemap" lightbox="media/agent-supervision/agent-feed-sitemap.png":::

You can view the feed in the side pane or expand it to full screen.
   :::image type="content" source="media/agent-supervision/agent-feed-expand.png" alt-text="Agent feed expand":::
   :::image type="content" source="media/agent-supervision/agent-feed-expanded.png" alt-text="Agent feed expanded":::

The feed shows a list of agent tasks. Each item can includes:

1. Title of the task
1. Description of the tasks with optional steps
1. The agent's name and icon
1. A timestamp of when the task was logged
   :::image type="content" source="media/agent-supervision/agent-feed-card-map.png" alt-text="Agent feed card map":::

Activity is grouped into two sections:

- **Needs Attention**: Shows tasks that are waiting for your input or need your attention. These are logged using request_assistance or invoke_data_entry mcp tools.
- **Completed**: Displays all other agent feed tasks, including tasks completed by the user and tasks completed by the agent that are logged for review using the request_review MCP tool.

By default, 20 agent tasks are loaded in each section with lazy loading enabled as user scrolls. The sections are sorted chronologically by the last modification date of each action.

You can filter the feed by agents 
 :::image type="content" source="media/agent-supervision/agent-feed-filters.png" alt-text="Agent feed filters":::

View agent feed in a side pane to support multitasking or expand it to full screen for focused review.

## Take action on agent activity

You can take these actions on tasks under **needs attention** tab in agent feed:

- **Complete**: Move an task from the **needs attention** section to **Completed** after completing the task the agent couldn't finish. This action is available for the agent taks logged using **request_assistance** mcp tool.

   :::image type="content" source="media/agent-supervision/agent-feed-mark-complete.png" alt-text="Agent feed mark as complete button":::

- **Accept and complete**: Move a data entry task from the **Needs attention** section to **Completed** after revieweing and accepting the data entry suggestions from **invoke_data_entry** mcp tool. Accept and complete button is available inside the agent pane associated with the agent feed task.

   :::image type="content" source="media/agent-supervision/agent-feed-accept-complete.png" alt-text="Agent feed accept and complete button":::

- **Dismiss**: Remove an data entry task logged via  **invoke_data_entry** mcp tool from the **Needs attention** section if it's no longer relevant. Dismiss button is available inside the agent pane associated with the agent feed task.
  
   :::image type="content" source="media/agent-supervision/agent-feed-dismiss.png" alt-text="Agent feed dismiss button":::

> [!NOTE]
> All actions can be performed either from the main screen in the feed or from the details page of a specific action.

- **Request_review tasks**: Tasks logged via request_review mcp tool do not have any actions for the users. They are informational tasks completed automomously by agent and can be found in completed agent feed tab.

     :::image type="content" source="media/agent-supervision/agent-feed-request-review.png" alt-text="Agent feed request review tasks":::


## Navigation

Agent feed tasks generated through the request_assistance or request_review MCP tools can reference a Dataverse record as a related navigation link in the agent description. This allows users to easily open and review associated data when interacting with the feed item at runtime.

:::image type="content" source="media/agent-supervision/agent-feed-navigate-to-record.png" alt-text="Agent feed record navigation button":::