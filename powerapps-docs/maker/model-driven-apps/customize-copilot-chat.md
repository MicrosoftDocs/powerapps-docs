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

Customize Copilot chat and make it even more intelligent and relevant for your organization by adding additional knowledge sources, topics and more. 

> [!IMPORTANT]
>
> - This is a preview feature.
> - Preview features aren't meant for production use and might have restricted functionality. These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?linkid=2216214), and are available before an official release so that customers can get early access and provide feedback.

> [!NOTE]
>
> This feature is only available in standalone model-driven apps and is not supported in Dynamics 365 apps. Consequently, the **Configure in Copilot Studio** button will only be displayed in the app designer for standalone model-driven apps.

You can customize Copilot chat using [Microsoft Copilot Studio](/microsoft-copilot-studio/) and expand the capabilities to go beyond just handling Dataverse tables Q&A and out-of-the-box skills. Make sure [copilot chat is enabled](/power-apps/maker/model-driven-apps/add-ai-copilot?branch=pr-en-us-10663#enable-copilot-for-model-driven-apps-in-your-environment) for this environment.  

1. Open your model driven app in edit mode to start customizing your copilot chat. 
1. Select **Configure in Copilot Studio**. Once you select it, you're taken to Microsoft Copilot Studio where your app’s copilot is set up. Note that every standalone model-driven app has its own deidcated copilot available for customizations. Setting up the Copilot for the firt time takes only a few seconds. 
   :::image type="content" source="media/mda-command-copilot-studio.png" alt-text="Open Copilot Studio to customize Copilot chat in model-driven app designer" lightbox="media/mda-command-copilot-studio.png":::
1. Customize your copilot by adding [knowledge sources](#add-knowledge-to-copilot-chat) or [topics](#add-new-topic-to-copilot-chat) to extend the intelligence of your app’s copilot chat. Customizing this Copilot only impacts the Copilot chat of your app.
   :::image type="content" source="media/mda-copilot-chat-copilot-studio.png" alt-text="Model-driven-app Copilot chat in Copilot Studio" lightbox="media/mda-copilot-chat-copilot-studio.png":::
1. **Publish** the copilot whenever you make customizations to the Copilot to ensure changes available to users.


## Add knowledge to Copilot chat

You can extend your app’s Copilot chat intelligence by adding additional knowledge in Copilot Studio. For example, you could add a link to an external website like Power Apps documentation to enable your Copilot chat to respond to questions related to Power Apps. Another example is to add your organization’s internal knowledge sources to enable Copilot chat to respond to relevant queries that aren't a part of the app data. 

Learn how to add knowledge to copilot: [Add knowledge to an existing agent – Microsoft Copilot Studio](/microsoft-copilot-studio/knowledge-add-existing-copilot). Currently only [Public website](/microsoft-copilot-studio/knowledge-add-public-website) and [File upload](/microsoft-copilot-studio/knowledge-add-file-upload) knowledge source types are supported.

> [!NOTE]
>
> Copilot studio [Generative AI orchestraion](/microsoft-copilot-studio/advanced-generative-actions) is not supported currently. You can use classic orchestration topic whose trigger phrases match most closely the user's query for given skill. 

## Add new topics to Copilot chat

You can make your app’s copilot chat more intelligent by extending it with additional AI capabilities that are relevant for users’ day to day tasks. You do so by adding topics to your app’s copilot in Copilot Studio. Learn about AI topics and how to add AI skills: [Create and edit topics – Microsoft Copilot Studio](/microsoft-copilot-studio/authoring-create-edit-topics?tabs=webApp)

