---
title: Use suggested actions in the agent feed
description: Learn about suggested actions and how to use them in the agent feed.
ms.date: 07/31/2025
ms.reviewer: smurkute
ms.topic: how-to
author: jacob-wilkinson
ms.subservice: end-user
ms.author: jacwilkinson
contributors: 
ms.service: powerapps
search.audienceType: 
  - enduser
---
# Use suggested actions in the agent feed (Preview)

[!INCLUDE [preview-banner](~/../shared-content/shared/preview-includes/preview-banner.md)]

Suggested actions help users focus on what matters most by showing intelligent, context-aware recommendations for high-value records. These actions are defined by makers. They appear automatically when you go to a record in a model-driven app and guide you toward meaningful next steps.

## Prerequisites

- Suggested actions only appear in the agent feed after makers have configured them.
- Learn how to [configure suggested actions in model-driven apps](../maker/model-driven-apps/configure-suggested-actions.md).

> [!IMPORTANT]
>
> - This is a preview feature.
> - Preview features aren't meant for production use and might have restricted functionality. These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?linkid=2216214) and are available before an official release, letting customers get early access and provide feedback.
> - This feature is gradually rolling out across regions and might not yet be available in your region.
> - This feature is available only in English.

## How suggested actions work

Suggested actions are evaluated when a form loads. If the system determines that a configured action is relevant, it appears in the agent feed.
:::image type="content" source="media/suggested-actions/suggested-actions-agent-feed.png" alt-text="Screenshot of suggested actions in the agent feed." lightbox="media/suggested-actions/suggested-actions-agent-feed.png":::

Suggested actions are recommendations. They don't perform tasks for you. Instead, they highlight actions you might want to take based on maker configurations, the current record’s data, and your past behavior. You must complete the task yourself if it's applicable.

You can also select a previously generated suggested action to automatically navigate to the associated record. This allows you to revisit and complete tasks even after switching context.

Filter the agent feed to show only suggested actions, making it easier to focus on them.
:::image type="content" source="media/suggested-actions/suggested-actions-filtering.png" alt-text="Filtering suggested actions" lightbox="media/suggested-actions/suggested-actions-filtering.png":::

The following illustration shows each suggested action:
:::image type="content" source="media/suggested-actions/suggested-actions-card-map.png" alt-text="Suggested actions card" lightbox="media/suggested-actions/suggested-actions-card-map.png":::
Legend
1. A title that describes the task.
1. A timestamp.
1. A **Mark as complete** button.
1. A **Dismiss** button.
1. A rationale explaining why the action is suggested.
1. The name of the table's suggested action agent.


## Example workflow

A typical interaction with a suggested action might look like this:

1. **Navigate to a record:** Open a record from a table with suggested actions configured in a model-driven app. This triggers the system to evaluate whether any suggested actions apply.
1. **Review the suggested action:** A suggested action appears in the agent feed with a short title and a rationale explaining why it was suggested, and you decide if it's something you should act on.
1. **Take action manually:** Complete the task outside the agent feed (for example, update a field, send an email, or approve a request).
1. **Mark the action as complete:** After manually finishing the task, return to the agent feed and mark the action as complete.
1. **Or dismiss it:** If the action isn’t relevant and you decide not to do the task, dismiss it instead.

## Interacting with suggested actions

You can interact with suggested actions in two ways:

- **Mark as complete:** Use this when you have manually completed the suggested task.
  :::image type="content" source="media/suggested-actions/suggested-actions-mark-complete.png" alt-text="Mark an action as complete" lightbox="media/suggested-actions/suggested-actions-mark-complete.png":::
- **Dismiss:** Use this when the suggestion isn't relevant to your current workflow.
  :::image type="content" source="media/suggested-actions/suggested-actions-dismiss.png" alt-text="Dismiss an action" lightbox="media/suggested-actions/suggested-actions-dismiss.png":::

> [!IMPORTANT]
> Completing or dismissing an action helps improve future suggestions. The system uses this feedback to learn which actions are helpful and when they should be shown. Also, once you complete or dismiss an action, you can't undo it.

After interacting with a suggested action:
- **Completed actions** move from the **To do** section of the feed to the **Other** section of the feed, but clicking it still navigates you to the associated record.
- **Dismissed actions** are removed from the feed and won't reappear unless the system re-evaluates and determines they're still relevant.
- Actions expire if they aren't interacted with after two days and are then removed from the feed.

## How suggested actions differ from agent activity
- **Suggested actions** help reduce the mental effort of deciding what to do next. They guide you toward high-impact tasks based on context and history.
- **Agent activity** is for [supervising work that autonomous agents do](supervise-agents-with-agent-feed.md) on your behalf.

Both features are part of the agent feed because they contribute to the same goal of using AI to make your job easier.

## Related information

[Add agents to an app](../maker/model-driven-apps/add-agents-to-app.md)  
[Customize Copilot chat](../maker/model-driven-apps/customize-copilot-chat.md)  
