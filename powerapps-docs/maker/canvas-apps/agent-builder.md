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

Agent builder in Power Apps enables organizations to rapidly transition into the AI-first era. By using existing knowledge, logic, and actions already built into the apps they create, makers can develop agents to handle tasks autonomously, eliminating repetitive processes, redefining individual productivity, and improving overall business efficiency. 

Agent builder helps users create copilot agents to automate their processes from existing applications. Agent builder takes your app metadata and the desired agent goal to create a step-by-step process the user currently takes to complete the process they are looking to automate. This process is then combined with deterministically extracted skills from the app to create a Copilot Studio copilot on the user’s behalf with instructions and actions. Once created, the user can add a trigger, edit, test, and publish the agent through Microsoft Copilot Studio. 

# How to create an agent with Agent Builder
Agent builder can help a user create an agent from an existing Canvas app. Agent builder will allow the user to automate a process through generating an agent that takes on the steps the user would have had to take in order to accomplish the task.   

You can access Agent builder from the app selector in the Home page or the Apps page of the Maker portal. Select the more menu next to the app that is currently associated with the process you would like to automate. Then select **Create agent from app**. 

**image 1**

Agent builder can generate suggestions based on your app for which processes within an app we can automate. Select a suggestion or in your own words describe what process you want the agent to automate.  If you select a suggestion the text box will automatically be populated, and we encourage you to edit and add more context to what you want the agent to do. To increase the agent's accuracy, when describing the desired goal for agent use everyday words and be specific: 
  - “Submit completed claim forms to the database for processing” 

  - “Generate reports for claims filed within a specific date range” 

**image 2**

Using the suggestion and/or the sentence the user provided for what the desired goal for the agent is and your app metadata, Agent builder generates step-by-step instructions for how the user currently completes process. We suggest you review closely for accuracy and edit the instructions as needed. You can also update the description to better describe the process you would like to automate and then press the **Regenerate Instructions** button to get updated instructions that reflect the updated goal of the agent.

**image 3**

# Known Limitations
We are unable to extract actions for apps if a data source connection was not found for some reason or a connection is not found. For these apps we will still proceed with creating the agent with the actions we can convert or none if we cannot convert any.  

We do not support the deprecated excel connector. However, we do support the following two excel connectors: 

  - https://learn.microsoft.com/en-us/connectors/excelonlinebusiness/ 

  - https://learn.microsoft.com/en-us/connectors/excelonline/ 

Agent builder is only available in regions where MCS generative agents are available. 

This feature is only currently available for Power Apps canvas applications.  

This language currently supported is English (US). 

#Provide Feedback

Unless your admin turned off the feedback feature, every step of Agent builder includes a **Like** button ("thumbs up" icon) and a **Dislike** button ("thumbs down" icon). For each response, you can select one of these icons to provide feedback that helps us improve Agent builder. Select the "thumbs up" or "thumbs down" icon as appropriate. Optionally, provide feedback in your own words about what you liked or didn't like about the response. When you're done, select **Submit**. 

## Related information

[FAQ about Agent Builder](../canvas-apps/agent-builder.md)
