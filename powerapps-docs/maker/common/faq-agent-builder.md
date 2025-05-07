---
title: FAQ about agent builder in canvas apps (preview)
description: This FAQ provides information about the AI technology used in agent builder with key considerations and details about how AI is used, how it was tested and evaluated, and any specific limitations.
ms.date: 4/15/2025
author: noazarur-microsoft
ms.author: noazarur
ms.reviewer: mkaur
ms.topic: faq
ms.subservice: common
ms.custom: transparency-note
 - responsible-ai-faqs
ms.collection: 
    - bap-ai-copilot
---

# FAQ for agent builder in canvas apps (preview)

These frequently asked questions (FAQ) describe the AI impact of agent builder in canvas apps.

## What is agent builder?  
Agent builder lets users create copilot agents to automate their processes. The goal of agent builder is to help users create copilot agents using their existing applications. Agent builder takes your app metadata and the desired agent goal to create a step-by-step process the user currently takes to complete the process they're looking to automate. This process is then combined with deterministically extracted skills from the app to create a Copilot Studio copilot on the user’s behalf with instructions, actions, triggers, and knowledge. Once created, the user can edit, test, and publish the agent through Microsoft Copilot Studio. 

## What can agent builder do? 
Agent builder can help a user create an agent. Agent builder can generate suggestions for which processes within an app we can automate. Using the suggestion and/or the sentence the user provided for what the desired goal for the agent is agent builder provides a process for how the user currently completes the task. Agent builder also extracts [actions](/microsoft-copilot-studio/advanced-plugin-actions), [triggers](/microsoft-copilot-studio/authoring-triggers-about), and [knowledge](/microsoft-copilot-studio/knowledge-copilot-studio) from the app metadata. Using the process instructions generated from agent builder and the triggers, knowledge, and actions extracted from agent builder the user can edit, test, and publish the agent in Microsoft Copilot Studio.   

## What is the intended use of agent builder?
The intended use of agent builder is to create agents to automate processes with a focus on data entry. The system allows the user to automate the process of data through generating an agent that takes on the steps the user would take to accomplish the task. The system wasn't designed, and we don't recommend customers to create agents for medical, legal, or hiring purposes. Agent builder was also not designed to be used to create an agent that has nothing to do with the app or generate an agent from an app that has no content. 

## How was agent builder evaluated? What metrics are used to measure performance?  
We qualitatively tested the model's agent generation capabilities by testing against an internal set of benchmark applications and expected high quality agent outputs. Additionally, we have set up reports and dashboards to track the usage, net promoter score (NPS), and engagement of the feature. We have also set up monitors to track the success rate of agent generation, app understanding, and AI inference. Top errors that occur to the users are logged as part of our monitors to help us understand what’s causing the issues. If you encounter any issues with the content generated, provide feedback. Your feedback is used to enhance Microsoft's products and services. Your organization's IT admins have access to your feedback data for management purposes. For more information, read the [Privacy Statement](https://www.microsoft.com/en-us/privacy/privacystatement).

## What are the limitations of agent builder? How can users minimize the impact of agent builder’s limitations when using the system?  
- This feature is only currently available for Power Apps canvas applications. 

- Preview features aren’t meant for production use and might have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback. 

- For more information, see [preview terms](https://www.microsoft.com/business-applications/legal/supp-powerplatform-preview/). 

- This capability is powered by [Azure OpenAI Service](/azure/ai-services/openai/overview). 

- This capability is in the process of rolling out and might not be available in your region yet.

- This capability can be subject to usage limits or capacity throttling. 

- Your environment must be in the United States region. 

## What operational factors and settings allow for effective and responsible use of agent builder? 

Follow these procedures to make the most out of the feature: 

- Use everyday words to describe the desired goal for agent: 

  - “Submit completed claim forms to the database for processing” 

  - “Generate reports for claims filed within a specific date range” 

- Review all suggestions for accuracy and appropriateness before proceeding to the next step.

## Authenticating actions after publishing
If your agent is missing authentication to perform an action or is configured to request user authentication, it sends a message to the user asking for credentials. If an agent's flow is interrupted because it can't receive information or an action failed, it can't continue the session. If you want your agent to run autonomously, each action must be configured with working maker authentication that doesn't require user input. You can also instruct your agent to not request credentials from users.

Because triggers use maker authentication, be aware of what data potential users can access through a published agent that has triggers. See the [Data protection with triggers](/microsoft-copilot-studio/authoring-triggers-about#data-protection-for-agents-with-triggers) section for more information. 

## Related information

[Build an agent to automate your business process (preview)](../canvas-apps/agent-builder.md)


