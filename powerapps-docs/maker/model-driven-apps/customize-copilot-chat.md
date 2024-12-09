---
title: Customize Copilot chat for app users in model-driven apps
description: Learn how to customize Copilot chat in model-driven apps to help app users get AI-powered insights about their data.
author: Mattp123
ms.service: powerapps
ms.subservice: mda-maker
ms.author: yogupt
ms.reviewer: matp
ms.date: 12/05/2024
ms.topic: how-to
applies_to: 
  - "powerapps"
search.audienceType: 
  - maker
contributors:
  - makolomi
ms.collection: bap-ai-copilot
---

# Customize Copilot chat to make it even more intelligent

Customize Copilot chat and make it even more intelligent and relevant for your organization by adding additional knowledge sources and AI skills. Add these sources and skills using Microsoft Copilot Studio for the Copilot to use in addition to the app data for responding to relevant queries for users.

1. Open your model driven app in edit mode to start customizing your copilot chat. Make sure copilot chat is enabled for this environment.  
1. Select **Configure in Copilot Studio**. Once you select it, you're taken to Microsoft Copilot Studio where your app’s copilot is set up. Setting up the Copilot takes only a few seconds.
   :::image type="content" source="media/mda-command-copilot-studio.png" alt-text="Open Copilot Studio to customize Copilot chat in model-driven app designer" lightbox="media/mda-command-copilot-studio.png":::
1. Customize your copilot by adding [knowledge sources](#bring-your-knowledge-to-copilot-chat) or [topics](#add-new-ai-skills-to-copilot-chat) to extend the intelligence of your app’s copilot chat. Customizing this Copilot only impacts the Copilot chat of your app.
   :::image type="content" source="media/mda-copilot-chat-copilot-studio.png" alt-text="Model-driven-app Copilot chat in Copilot Studio" lightbox="media/mda-copilot-chat-copilot-studio.png":::
1. **Publish** your app. After the Copilot is created for your app for the first time or anytime you make customizations to the Copilot, make sure to publish the app to make changes available to users.

## Bring your knowledge to Copilot chat

Extend your app’s Copilot chat intelligence by adding additional knowledge in Copilot Studio. For example, you could add a link to an external travel website to enable your Copilot chat to respond to questions related to travel news. Another example is to add your organization’s internal knowledge sources to enable Copilot chat to respond to relevant queries that aren't a part of the app data. Learn how to add knowledge to copilot: [Add knowledge to an existing agent – Microsoft Copilot Studio](/microsoft-copilot-studio/knowledge-add-existing-copilot)

## Add new AI skills to Copilot chat

You can make your app’s copilot chat more intelligent by extending it with additional AI capabilities that are relevant for users’ day to day tasks. You do so by adding topics to your app’s copilot in Copilot Studio. Learn about AI topics and how to add AI skills: [Create and edit topics – Microsoft Copilot Studio](/microsoft-copilot-studio/authoring-create-edit-topics?tabs=webApp)

