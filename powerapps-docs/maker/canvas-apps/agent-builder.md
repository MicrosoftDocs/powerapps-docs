---
title: Automate your business processes with agent builder in a canvas app
description: How to create an agent to help automate business processes in a canvas app using agent builder.
author: noazarur-microsoft
ms.topic: article
ms.date: 4/15/2025
ms.subservice: canvas-maker
ms.author: noazarur
ms.reviewer: mkaur
search.audienceType: 
  - maker
contributors:
  - noazarur-microsoft
---

# Build an AI agent to automate your business process (preview) 

[!INCLUDE [preview-banner](~/../shared-content/shared/preview-includes/preview-banner.md)]

Agent builder in Power Apps lets organizations transition into the AI-first era by using the knowledge, logic, and actions of an app to create copilot agents. These agents handle daily tasks, streamline processes, enhance productivity, and improve overall business efficiency. Watch this brief video to see how to build an agent:

> [!VIDEO 284820d9-7fbc-4c8f-bf20-e8678614ed3d]

 Makers can create agents that automate processes within their existing canvas apps. Agent builder uses the app's metadata and the desired agent goal to generate a comprehensive step-by-step process, extract knowledge, and identify triggers. This process, knowledge, and triggers are then combined with extracted skills from the app, resulting in a fully equipped copilot that offers detailed instructions, knowledge, triggers, and actions.

After creating the agent, makers can edit, test, and publish it in Microsoft Copilot Studio.

> [!IMPORTANT]
> - This is a preview feature.
> - Preview features aren't meant for production use and might have restricted functionality. These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?linkid=2189520), and are available before an official release so that customers can get early access and provide feedback.

## Prerequisites

- Preview Copilot features are enabled by default, but your admin can turn them off for an environment or tenant. More information: [Copilot in Power Apps overview (preview)](ai-overview.md#disable-copilot-in-power-apps).
- Your tenant administrator must turn on the [Publish Copilots with AI features](/microsoft-copilot-studio/security-and-governance) setting in the Power Platform admin center.
- Include a Dataverse database in your environment. More information: [Add a Microsoft Dataverse database](/power-platform/admin/create-database).
- The environment must be in the United States region. Depending on where the environment is hosted, you might need to allow data movement across regions. More information: [Copilots and generative AI features that are available when you enable data movement across regions](/power-platform/admin/geographical-availability-copilot#copilots-and-generative-ai-features-that-are-available-when-you-enable-data-movement-across-regions).
- Ensure that block unmanaged customizations is disabled. Learn more in [Block unmanaged customizations in Dataverse environments](/power-platform/alm/block-unmanaged-customizations).

## Create an agent

To streamline your manual process, generate an agent that replicates the steps you typically follow to complete tasks.

1. Sign in to [Power Apps](https://make.powerapps.com).
1. Select **Agents** in the left navigation pane. If you don't see **Agents**, select **More**, and then find and select **Agents**. 
1. Select **Create an agent from an app**.
    :::image type="content" source="media/agent-builder/ab-create-agent-from-app-new-menu.png" alt-text="Screenshot of creating an agent from an app":::

1. Select your app and then select **Next** on the command bar.
:::image type="content" source="media/agent-builder/ab-select-app-then-next.png" alt-text="Select an app and then select next":::

    Alternatively, you can select **Apps** in the left navigation pane. Select your app, and then select **Create agent from app (Preview)** on the command bar. You can also select **Commands** (![Commands button.](media/power-apps-page-icons/apps-commands-menu-to-edit.png)) for the app and then select **Create agent from app (Preview)**.

    :::image type="content" source="media/agent-builder/ab-create-agent-from-app.png" alt-text="Create agent from app":::

1. Select a suggestion, or in the text box, describe the process you want to automate, and then select **Next**.

    :::image type="content" source="media/agent-builder/ab-suggestions.png" alt-text="Select a suggestion or describe the process you want to automate":::

1. When you select a suggestion, the text box is automatically filled. You can edit it and add more details about what you want the agent to do. To improve the agent's accuracy, use simple, everyday language, and be specific, like:

   - Submit completed claim forms to the database for processing.
   - Generate reports for claims filed within a specific date range.

1. Based on the suggestion or the information that you provide for the agent's goal and the app's metadata, agent builder generates step-by-step instructions to replace your manual process and extracts triggers and knowledge. Review the instructions for accuracy, and make any necessary edits. Review the extracted knowledge and triggers for accuracy, and make any necessary edits.

    :::image type="content" source="media/agent-builder/ab-process-summary.png" alt-text="Reivew the process summary":::


### Regenerate instructions to improve the response

You can also revise the description to better represent the process you want to automate. When you're done, select the **Regenerate instructions** to receive updated instructions that match the new goal of the agent.

:::image type="content" source="media/agent-builder/ab-regenerate-instructions.png" alt-text="Regenerate instructions to improve response":::

### Best practices

When you edit the instructions, follow these suggestions:

- Use clear and specific wording in the instructions. For example, "Filter the claims data using the approval status" rather than "Filter the data."

- Verify the instructions to ensure they meet their goal.

- Keep each of the sentences for the instructions relatively simple. If there are too many details and conditions in one of the sentences, it might not work as intended.

- Ensure the logical flow of the instructions is easy to follow. Avoid adding new instructions at the end of the instruction set. Instead, move instructions in line to maintain a logical sequence. 
  
  Here are example instructions:

    1. Read the data from the table.

    2. Process the data with pending status.

    3. If amount is less than $50 auto approve it and mark it as approved.

    4. Update the table with new status.

    5. And if the amount is more than $50 but less than $500 check to see if it's an approved item.

    6. Additionally if the amount is more than $500 update the status to manual review.

    To improve the logical flow in this example, move steps 5 and 6 after step 3.

## Limitations

- If a data source connection isn't found, you can't extract actions for the app. In such cases, the agent builder generates an agent with the actions that can be converted, or none if no actions can be converted.

- Deprecated Excel connectors aren't supported. However, the following Excel connectors are supported:

  - [Excel Online (Business)](connections/connection-excel.md)
  - [Excel Online](connections/connection-excel.md)

- Agent builder is available only in regions where Microsoft Copilot Studio generative agents are available.
- This feature is available only for canvas apps.
- This feature is available only in English (EN-US).

## Provide feedback

Unless feedback is disabled by your admin, each step in the agent builder includes a **Like** (thumbs up) and **Dislike** button (thumbs down).

After reviewing the agent's responses, you can provide feedback in your own words. When you're done, select **Submit**.

## Related information

[FAQ for agent builder in canvas apps](../common/faq-agent-builder.md)


