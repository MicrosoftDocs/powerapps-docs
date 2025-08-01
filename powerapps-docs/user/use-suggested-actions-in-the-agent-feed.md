
---
title: "Use suggested actions in the agent feed" 
description: Learn about suggested actions and how to use them in the agent feed.
ms.date: 07/31/2025
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
# Use suggested actions in the agent feed (preview)

[!INCLUDE [preview-banner](~/../shared-content/shared/preview-includes/preview-banner.md)]

Suggested actions help users focus on what matters most by surfacing intelligent, context-aware recommendations for high-value records. These actions are defined by makers. They appear automatically when you navigate to a record in a model-driven app and are designed to guide you toward meaningful next steps.

## Prerequisites

- Suggested actions only appear in the agent feed after makers have configured them
- Learn how to [Configure suggested actions in model-driven apps](../maker/model-driven-apps/configure-suggested-actions-in-model-driven-apps.md)

> [!IMPORTANT]
>
> - This is a preview feature.
> - Preview features aren't meant for production use and might have restricted functionality. These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?linkid=2216214), and are available before an official release so that customers can get early access and provide feedback.
> - This feature is being gradually rolled out across regions and might not be available yet in your region.
> - This feature is only available in the English language.

## How suggested actions work

Suggested actions are evaluated when a form loads. If the system determines that a configured action is relevant, it will appear in the agent feed.
:::image type="content" source="media/suggested-actions/suggested-actions-agent-feed.png" alt-text="Suggested actions in the agent feed" lightbox="media/suggested-actions/suggested-actions-agent-feed.png":::

Suggested actions are recommendations. They do not perform tasks for you. Instead, they highlight actions you may want to take based on maker configurations, the current record’s data and your past behavior. You must complete the task yourself if it is applicable.

You can also click a previously generated suggested action to automatically navigate to the associated record. This allows you to revisit and complete tasks even after switching context.


> [!TIP]
> You can filter the agent feed to show only suggested actions, making it easier to focus on them.
> :::image type="content" source="media/suggested-actions/suggested-actions-filtering.png" alt-text="Filtering suggested actions" lightbox="media/suggested-actions/suggested-actions-filtering.png":::

Each suggested action includes:
1. A title that describes the task
1. Timestamp
1. Mark as complete button
1. Dismiss button
1. A rationale explaining why the action is being suggested
1. Name of the tables's suggested action agent
:::image type="content" source="media/suggested-actions/suggested-actions-card-map.png" alt-text="Filtering suggested actions" lightbox="media/suggested-actions/suggested-actions-card-map.png":::

## Example workflow

A typical interaction with suggested action might look like this:
1. **Navigate to a record:** You open a record from a table with suggested actions configured in a model-driven app. This triggers teh system to evaluate whether any suggested actions apply.
1. **Review the suggested action:** A suggested action appears in the agent feed with a short title and a rationale explaining why it was suggested, and you decide if it is something you should act on.
1. **Take action manually:** You complete the task outside the agent feed (for example, updating a field, sending an email, or approving a request).
1. **Mark the action as complete:** After manually finishing the task, you return to the agent feed and mark the action as complete.
1. **Or dismiss it:** If the action wasn’t relevant and you decided not to perform the task, you dismiss it instead. 

## Interacting with suggested actions

You can interact with suggested actions in two ways:
-**Mark as complete:** Use this wehn you have manually completed the suggested task.
:::image type="content" source="media/suggested-actions/suggested-actions-mark-completed.png" alt-text="Filtering suggested actions" lightbox="media/suggested-actions/suggested-actions-mark-complete.png":::
-**Dismiss:** Use this when the suggestion is not relevant to your current workflow.
:::image type="content" source="media/suggested-actions/suggested-actions-dismiss.png" alt-text="Filtering suggested actions" lightbox="media/suggested-actions/suggested-actions-dismiss.png":::

> [!IMPORTANT]
> Completing or dismissing an action helps improve future suggestions. The system uses this feedback to learn which actions are helpful and when they should be shown. Also, note that once you complete or dismiss an action, you cannot undo it.

After you interact with a suggested action:
- **Completed actions** move from the **To do** section of the feed to the **Other** section of the feed, but clicking it still navigates you to the associated record.
- **Dismissed actions** are removed from the feed and will not reappear unless the system re-evaluates and determines they are still relevant.
- Actions expire if they have not been interscted with after two days and are then removed from the feed.

## How suggested actions differ from agent activity
- **Suggested actions** help reduce the mental effort of deciding what to do next. They guide you toward high-impact tasks based on context and history.
- **Agent activity** is for the purpose of [supervising work that autonomous agents do](supervise-agents-with-agent-feed.md) on your behalf.

Both features are part of the agent feed because they contribute to the same goal of using AI to make you job easiser.

## Related information

[Add agents to an app](../maker/model-driven-apps/add-agents-to-app.md)     
[Customize Copilot Chat](../maker/model-driven-apps/customize-copilot-chat.md)

