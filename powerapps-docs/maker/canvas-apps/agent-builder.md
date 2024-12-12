---
title: Automate your business processes with Agent Builder in canvas apps
description: How to create an agent to help automate business processes with Agent Builder.
author: noazarur-microsoft

ms.topic: article
ms.date: 11/6/2024
ms.subservice: canvas-maker
ms.author: noazarur
ms.reviewer: mkaur
search.audienceType: 
  - maker
contributors:
  - noazarur-microsoft
---

# Automate your business process with Agent Builder (preview) 

[!INCLUDE [preview-banner](~/../shared-content/shared/preview-includes/preview-banner.md)]

Agent Builder in canvas apps enables organizations to swiftly transition into the AI-first era. By leveraging existing knowledge, logic, and actions embedded in their apps, makers can develop agents to autonomously handle tasks, eliminate repetitive processes, redefine productivity, and enhance overall business efficiency.

Agent Builder assists users in creating copilot agents to automate processes from existing applications. It utilizes your app metadata and the desired agent goal to generate a step-by-step process. This process is combined with extracted skills from the app to create a Copilot Studio copilot with instructions and actions. Once created, you can add a trigger, edit, test, and publish the agent in Microsoft Copilot Studio.

> [!IMPORTANT]
> - This is a preview feature.
> - Preview features aren't meant for production use and might have restricted functionality. These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?linkid=2189520), and are available before an official release so that customers can get early access and provide feedback.

## Create an agent

Agent Builder lets you to create an agent from an existing canvas app. It streamlines the process by generating an agent that replicates the steps you would take to complete the task.

1. Sign in to [Power Apps](https://make.powerapps.com).
1. Select **Apps** in the left navigation pane.
1. Select your app and then select **Create agent from app (Preview)** on the command bar. You can also select **Commands** (![Commands button.](media/power-apps-page-icons/apps-commands-menu-to-edit.png)) for the app and then select **Create agent from app (Preview)**.

    :::image type="content" source="media/agent-builder/ab-create-agent-from-app.png" alt-text="Create agent from app":::

1. Select a suggestion or in the text box describe the process you want the agent to automate and then select **Next**.

    :::image type="content" source="media/agent-builder/ab-select-next-to-regenerate-instructions.png" alt-text="Select next to generate instructions":::

    When you choose a suggestion, the text box will automatically fill in. You can edit and add more details about what you want the agent to do. To improve the agent's accuracy, use simple, everyday language and be specific, such as:
     - Submit completed claim forms to the database for processing.
     - Generate reports for claims filed within a specific date range.

1. Based on the suggestion or the information that you provide for the agent's goal and your app metadata, Agent Builder generates step-by-step instructions for your current process. Review the instructions for accuracy and make any necessary edits.

  **Image of instructions**
  
 When editing the instructions we suggest the following: 

  - Use clear and specific wording in the instructions. For example, "Filter the claims data using the approval status" rather than "Filter the data". 

  - Verify the instructions to ensure their goal is met by the generated / modified instructions. 

  - Keep each of the sentences for the instructions relatively simple. If there are too many details and conditions in one of the sentences it might not work as intended. 

  - Make sure the logical flow of the instructions is easy to follow. Avoid adding new instructions at the end of the whole instruction set, we suggest moving instructions in line to ensure a logical flow. 
 
     For Example:  
       1. Read the data from the Table 
       2. Process the data with pending status 
       3. If amount is less than $50 auto approve it and mark it as Approved 
       4. Update the Table with new status 
       
       5. And if the amount is more than $50 but less than $500 check to see if it is an approved item 
       6. Additionally if the amount is more than $500 update the status to manual review. 
       
       This could potentially cause some issues since the logic is not straight forward for the LLM, we suggest moving instructions #5 and #6 to be in between 3 and 4. 

1. You can also revise the description to better represent the process you want to automate. When you're done, select the **Regenerate instructions** to receive updated instructions that match the new goal of the agent.

    :::image type="content" source="media/agent-builder/ab-regenerate-instructions.png" alt-text="regenerate instructions":::



## Limitations

- We are unable to extract actions for apps if a data source connection ins't found or isn't found. For these apps Agent Builder will still proceed with creating the agent with the actions it can convert or none if we cannot convert any.  

- We don't support the deprecated excel connector. However, we do support the following two excel connectors:

  - [Excel Online (Business)](connections/connection-excel.md)
  - [Excel Online](connections/connection-excel.md)

- Agent builder is only available in regions where Microsoft Copilot Studio generative agents are available.

- This feature is only currently available for canvas apps.

- This featuere is only available in English (US).

## Feedback

Unless your admin has disabled the feedback feature, each step of Agent Builder includes a **Like** button (a "thumbs up" icon) and a **Dislike** button (a "thumbs down" icon). You can use these icons to provide feedback on each response, helping us improve Agent Builder. Simply select the "thumbs up" or "thumbs down" icon as appropriate. Additionally, you can provide feedback in your own words about what you liked or didn't like about the response. When you're finished, select **Submit**.


## Related information

[FAQ about Agent Builder](../canvas-apps/agent-builder.md)
