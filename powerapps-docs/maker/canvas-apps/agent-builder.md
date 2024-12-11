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

Agent Builder in canvas apps enables organizations to swiftly transition into the AI-first era. By leveraging existing knowledge, logic, and actions embedded in their apps, makers can develop agents to autonomously handle tasks, eliminate repetitive processes, redefine productivity, and enhance overall business efficiency.

Agent Builder assists users in creating copilot agents to automate processes from existing applications. It utilizes your app metadata and the desired agent goal to generate a step-by-step process. This process is combined with extracted skills from the app to create a Copilot Studio copilot with instructions and actions. Once created, you can add a trigger, edit, test, and publish the agent in Microsoft Copilot Studio.. 

## Create an agent

Agent Builder lets you to create an agent from an existing canvas app. It streamlines the process by generating an agent that replicates the steps you would take to complete the task.

1. Access Agent builder from the app selector on the Home page or the Apps page of the Maker portal. 
1. Select the more menu next to the app associated with the process you want to automate. 
1. Then select **Create agent from app**. 

**image 1**

Agent builder can suggest processes within your app to automate. Select a suggestion or describe the process you want the agent to automate. If you select a suggestion, the text box will be automatically populated. Edit and add more context to what you want the agent to do. To increase the agent's accuracy, use everyday words and be specific: 
  - “Submit completed claim forms to the database for processing” 

  - “Generate reports for claims filed within a specific date range” 

**image 2**

Using the suggestion and/or the sentence you provided for the desired goal for the agent and your app metadata, Agent builder generates step-by-step instructions for how you currently complete the process. We suggest you review closely for accuracy and edit the instructions as needed. You can also update the description to better describe the process you would like to automate and then press the **Regenerate Instructions** button to get updated instructions that reflect the updated goal of the agent.

**image 3**

# Known Limitations
  - We are unable to extract actions for apps if a data source connection was not found for some reason or a connection is not found. For these apps we will still proceed with creating the agent with the actions we can convert or none if we cannot convert any.  

  - We do not support the deprecated excel connector. However, we do support the following two excel connectors: 

    - /connectors/excelonlinebusiness/ 

    - /connectors/excelonline/ 

  - Agent builder is only available in regions where Microsoft Copilot Studio generative agents are available. 

  - This feature is only currently available for canvas apps.

  - This language currently supported is English (US). 

# Provide Feedback

Unless your admin turned off the feedback feature, every step of Agent builder includes a **Like** button ("thumbs up" icon) and a **Dislike** button ("thumbs down" icon). For each response, you can select one of these icons to provide feedback that helps us improve Agent builder. Select the "thumbs up" or "thumbs down" icon as appropriate. Optionally, provide feedback in your own words about what you liked or didn't like about the response. When you're done, select **Submit**. 

## Related information

[FAQ about Agent Builder](../canvas-apps/agent-builder.md)
