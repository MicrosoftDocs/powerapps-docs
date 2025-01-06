---
title: Customize Copilot chat in model-driven apps
description: Learn how to customize Copilot chat in model-driven apps
author: Mattp123
ms.service: powerapps
ms.subservice: mda-maker
ms.author: hemantg
ms.reviewer: matp
ms.date: 12/09/2024
ms.topic: how-to
applies_to: 
  - "powerapps"
search.audienceType: 
  - maker
contributors:
  - makolomi
ms.collection: bap-ai-copilot
---

# Customize Copilot chat using Copilot Studio (Preview)

[!INCLUDE [preview-banner](~/../shared-content/shared/preview-includes/preview-banner.md)]

Customize Copilot chat to make it even more intelligent and relevant for your organization by adding additional topics, knowledge sources and more. 

> [!IMPORTANT]
>
> - This is a preview feature.
> - Preview features aren't meant for production use and might have restricted functionality. These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?linkid=2216214), and are available before an official release so that customers can get early access and provide feedback.

> [!NOTE]
>
> This feature is only available in standalone model-driven apps and is not yet supported for Dynamics 365 apps. Consequently, the **Configure in Copilot Studio** button will only be displayed in the app designer for standalone model-driven apps.

You can customize Copilot chat using [Microsoft Copilot Studio](/microsoft-copilot-studio/) and expand the capabilities to go beyond just handling Dataverse tables Q&A and out-of-the-box skills. Before customizing, make sure [copilot chat is enabled](/power-apps/maker/model-driven-apps/add-ai-copilot?branch=pr-en-us-10663#enable-copilot-for-model-driven-apps-in-your-environment) for your environment.  

1. Open your model driven app in edit mode to start customizing your copilot chat. 
1. Select triple dot "..." and then select **Configure in Copilot Studio**. You will be taken to Microsoft Copilot Studio where your app’s agent is set up. Note that every standalone model-driven app copilot has its own dedicated agent available for customizations. Setting up the agent for the firt time takes only a few seconds. 
   :::image type="content" source="media/mda-command-copilot-studio.png" alt-text="Open Copilot Studio to customize Copilot chat in model-driven app designer" lightbox="media/mda-command-copilot-studio.png":::
1. Customize your agent by adding [knowledge sources](#add-knowledge-to-copilot-chat) or [topics](#add-new-topic-to-copilot-chat). Customizing this agent only impacts the Copilot chat of the specific app it was provisioned for.
   :::image type="content" source="media/mda-copilot-chat-copilot-studio.png" alt-text="Model-driven-app Copilot chat in Copilot Studio" lightbox="media/mda-copilot-chat-copilot-studio.png":::
1. **Publish** the agent after you make customizations to ensure changes available to users.

## Add knowledge to Copilot chat

You can extend your app’s Copilot chat intelligence by adding additional knowledge sources in Copilot Studio. For example, you could add a link to an external public facing website like Power Apps documentation to enable your Copilot chat to respond to questions related to Power Apps. Another example is to upload your organization’s internal knowledge as a document to enable Copilot chat to respond to relevant queries that aren't a part of the app data. 

For more details, see how to add knowledge to copilot: [Add knowledge to an existing agent – Microsoft Copilot Studio](/microsoft-copilot-studio/knowledge-add-existing-copilot). 

> [!NOTE]
>
> Currently only [Public website](/microsoft-copilot-studio/knowledge-add-public-website) and [File upload](/microsoft-copilot-studio/knowledge-add-file-upload) knowledge source types are supported.

> [!NOTE]
>
> Copilot studio [Generative AI orchestraion](/microsoft-copilot-studio/advanced-generative-actions) is not supported currently. You can use classic orchestration topic whose trigger phrases match most closely the user's query for given skill. 


   :::image type="content" source="media/mda-copilot-chat-add-knowledge.png" alt-text="Add Knowledge to Model-driven-apps via Copilot Studio" lightbox="media/mda-copilot-chat-add-knowledge.png":::


## Add new topic to Copilot chat

 In Copilot Studio, you can add topics to your app’s copilot. These topics can be customized to use various trigger types and can respond with simple messages, adaptive cards or generative answer. Additionally topics can also initiate actions like flows, connectors, and plugins enabling seamless point in time integration with external systems. Learn more about topics and how to add AI skills: [Create and edit topics – Microsoft Copilot Studio](/microsoft-copilot-studio/authoring-create-edit-topics?tabs=webApp).
 
   :::image type="content" source="media/mda-copilot-chat-add-topic.png" alt-text="Add topic to Model-driven-apps via Copilot Studio" lightbox="media/mda-copilot-chat-add-topic.png":::
> 
> [!NOTE]
>
> Copilot studio's inline capability to "Test your agent" can be used to validate topics as they are added. However  topics using OOB model apps custom variables like  
Global.PA__Copilot_Model_PageContext.pageContext.id can only be tested in the published copilot. 

## Prompt guide customizations
A prompt library is a collection of pre-written, tested, and optimized prompts designed to help shape the interactions and responses of the copilot chat. They ensure that the copilot chat provides relevant, accurate, and contextually appropriate information based on the user’s needs and preferences.

   :::image type="content" source="media/mda-copilot-chat-prompt-guide.png" alt-text="Prompt guide for Model-driven apps copilot" lightbox="media/mda-copilot-chat-prompt-guide.png":::
>
The following steps detail how to add a specific queries to the prompt guide. We will append “Power Apps Help” section to the existing OOB copilot prompt guide. Alternatively, you can choose to completely replace OOB prompt guide. All these prompts shown via prompt guide to the end users are stored in the Copilot Studio agent backing the app. 

1. Open the agent backing the app in copilot studio and add a new blank topic.
   :::image type="content" source="media/mda-copilot-promptguide-addtopic.png" alt-text="Add blanck topic" lightbox="media/mda-copilot-promptguide-addtopic.png":::
1. Rename the topic to reflect the topic intent and change the topic trigger to “Event received”.
   :::image type="content" source="media/mda-copilot-promptguide-eventreceived.png" alt-text="Event recevied for topic" lightbox="media/mda-copilot-promptguide-eventreceived.png":::
1. Click on edit for Event received and set the event name as Microsoft.PowerApps.Copilot.RequestSparks which is reserved name for prompt guide.
   :::image type="content" source="media/mda-copilot-promptguide-requestspark.png" alt-text="Spark request for topic" lightbox="media/mda-copilot-promptguide-requestspark.png":::
1. Optionally you can set the conditions to prompt entries in case they are specific to app name, page context etc.  
condition: =Global.PA_Copilot_Model_SessionContext.appUniqueName = "yourAppName" or Global.PA__Copilot_Model_PageContext.pageContext.entityTypeName = "Entity name"
 1. Add an appropriate priotrity value so that the trigger is fired after the higher priority topics. Priority values can have 0 to 10k range with 0 being highest. We will use 200 for this example.
 1. Add a next step for variable management and parsing prompt guide entries JSON.
   :::image type="content" source="media/mda-copilot-promptguide-variable.png" alt-text="Parsing prompt guide entries" lightbox="media/mda-copilot-promptguide-variable.png":::
 1. 









## Known Limitations
1. ALM - Solution dependecies from App to corresponsind agent is not suupported for preview. As a workaround you can package the app and agent manually.
2. **Configure in Copilot Studio** action can fail if there are App with same initial characters in their name. Please rename the app and try again.
