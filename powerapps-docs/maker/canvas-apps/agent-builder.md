---
title: Automate your business processes with agent builder in a canvas app
description: How to create an agent to help automate business processes in a canvas app using agent builder.
author: noazarur-microsoft
ms.topic: article
ms.date: 4/14/2025
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

Agent builder in Power Apps enables organizations to transition into the AI-first era by using the knowledge, logic, and actions of an app to create copilot agents. These agents handle daily tasks, streamline processes, enhance productivity, and optimize overall business efficiency. Watch this brief video to see how to build an agent:

> [!VIDEO 284820d9-7fbc-4c8f-bf20-e8678614ed3d]

 Makers can easily create agents that automate processes within their existing canvas apps. Agent builder uses the app's metadata and the desired agent goal to generate a comprehensive step-by-step process. This process is then combined with extracted skills from the app, resulting in a fully equipped copilot that offers detailed instructions and actions.

Once the agent is created, makers can add triggers, make edits, conduct testing, and publish the agent in Microsoft Copilot Studio.

> [!IMPORTANT]
> - This is a preview feature.
> - Preview features aren't meant for production use and might have restricted functionality. These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?linkid=2189520), and are available before an official release so that customers can get early access and provide feedback.

## Prerequisites

- Copliot Features Admin Toggle must be enabled for environment and tenant. Ensure you meet the prerequisites and region availability in [Copilot in Power Apps overview (preview)](ai-overview.md).
- Tenant setting for "Publish Copilots with AI features" must be enabled.
- Include a Dataverse database in your environment. Learn more in [Add a Microsoft Dataverse database](/power-platform/admin/create-database).
- Environment must be in the United States region. Depending on where your environment is hosted, you might need to allow data movement across regions. Learn more in [Copilots and generative AI features that are available when you enable data movement across regions](/power-platform/admin/geographical-availability-copilot#copilots-and-generative-ai-features-that-are-available-when-you-enable-data-movement-across-regions).
- Ensure block unamanged customizations is disabled. Learn more in [Block unmanaged customizations in Dataverse environments](power-platform/alm/block-unmanaged-customizations).

## Create an agent

To streamline your manual process, generate an agent that replicates the steps you typically follow to complete tasks.

1. Sign in to [Power Apps](https://make.powerapps.com).
1. Select **Agents** in the left navigation pane.
1. Select **Create an agent from an app** **CreateAgentEntry Screenshot**
2. Select your app and then select **Next** on the command bar. **SelectApp Screenshot**
1. Alternatively, select **Apps** in the left navigation pane. Select your app and then select **Create agent from app (Preview)** on the command bar. You can also select **Commands** (![Commands button.](media/power-apps-page-icons/apps-commands-menu-to-edit.png)) for the app and then select **Create agent from app (Preview)**.

    :::image type="content" source="media/agent-builder/ab-create-agent-from-app.png" alt-text="Create agent from app":::

1. Select a suggestion or in the text box describe the process you want to automate and then select **Next**.

**Suggestion screenshot**

    When you choose a suggestion, the text box is automatically filled in. You can edit and add more details about what you want the agent to do. To improve the agent's accuracy, use simple, everyday language and be specific, such as:
     - Submit completed claim forms to the database for processing.
     - Generate reports for claims filed within a specific date range.

1. Based on the suggestion or the information that you provide for the agent's goal and the app's metadata, agent builder generates step-by-step instructions to replace your manual process and extracts triggers and knowledge. Review the instructions for accuracy and make any necessary edits. Review the extracted knowledge and triggers for accuracy and make any necessary edits.

   **ProcessSummary Screenshot**



### Regenerate instructions to improve response

You can also revise the description to better represent the process you want to automate. When you're done, select the **Regenerate instructions** to receive updated instructions that match the new goal of the agent.

**RegenerateInstructions Screenshot**

### Best practices

When you edit the instructions, follow these suggestions:

- Use clear and specific wording in the instructions. For example, "Filter the claims data using the approval status" rather than "Filter the data."

- Verify the instructions to ensure they meet their goal.

- Keep each of the sentences for the instructions relatively simple. If there are too many details and conditions in one of the sentences, it might not work as intended.

- Ensure the logical flow of the instructions is easy to follow. Avoid adding new instructions at the end of the instruction set. Instead, move instructions in line to maintain a logical sequence. 
  
  Here's example instructions:

    1. Read the data from the table.

    2. Process the data with pending status.

    3. If amount is less than $50 auto approve it and mark it as approved.

    4. Update the table with new status.

    5. And if the amount is more than $50 but less than $500 check to see if it's an approved item.

    6. Additionally if the amount is more than $500 update the status to manual review.

    To improve the logical flow in this example, move steps #5 and #6 after step #3.

## Limitations

- If a data source connection isn't found, it's not possible to extract actions for app. In such cases, agent builder still generates an agent, including the actions that can be converted, or none if no actions can be converted.

- Deprecated Excel connectors aren't supported, but the following Excel connectors are supported:

  - [Excel Online (Business)](connections/connection-excel.md)
  - [Excel Online](connections/connection-excel.md)

- Agent builder is only available in regions where Microsoft Copilot Studio generative agents are available.

- This feature is currently available only for canvas apps.

- This feature is available only in English (en-US).

## Provide feedback

Unless feedback is disabled by your admin, each step in agent builder includes a **Like** (thumbs up) and **Dislike** button (thumbs down).

After reviewing the agent's responses, you can also provide feedback in your own words. When you're done, select **Submit**.

## Related information

[FAQ for agent builder in canvas apps](../common/faq-agent-builder.md)


