---
title: Use Copilot in model-driven apps (preview)
description: Learn how to use Copilot in model-driven apps.
author: srihas
ms.component: pa-user
ms.topic: overview
ms.date: 03/13/2024
ms.subservice: end-user
ms.author: srihas
ms.custom: ""
ms.reviewer: sericks
ms.assetid: 
search.audienceType: 
  - enduser
---

# Use Copilot in model-driven apps (preview)

[This article is prerelease documentation and is subject to change.]

Copilot for model-driven apps in Power Apps is a next-generation AI assistant to help you get insights about the data in your apps through conversation in natural language. Copilot helps you boost your productivity through AI-powered insights and navigation assistance. 

> [!IMPORTANT]
> - Preview features aren’t meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.
> - An administrator must enable Copilot in your application for you to see it in your app. More information: [Add copilot for app users in model-driven apps](../maker/model-driven-apps/add-ai-copilot.md)

## Copilot pane 

When enabled, Copilot can be accessed through the Copilot icon in the right navigation bar or through the Copilot icon in the top bar in a model-driven app. The copilot pane can be expanded or collapsed as desired. When enabled, the pane is expanded by default.

picture

## Use Copilot to ask questions 

Copilot in model-driven apps can answer questions about the Microsoft Dataverse table data in the app. Copilot can also help you navigate the model-driven app. For example, when a user enters Navigate me to Online Cases, the copilot in the model-driven app automatically opens the relevant page in the app. 

picture

## Copilot suggested questions 

Copilot can suggest questions for you to ask to help you get started. These questions (also called prompts) can be edited and personalized for your app and the type of insight you need from Copilot. 

You see more suggested prompts by selecting View prompts within the Copilot pane. Many of the suggested questions have placeholders that you need to replace with an appropriate text that completes the question. 

picture

## Record picker to select object of the question 

You can use the record picker to select the object of your question. Type “/” character to open the record picker and continue typing the name of the record. Then select the record of your choice and complete the question to make it meaningful. Submit the question to Copilot to view the response. 

picture

> [!Note]
> - Using record picker will increase the chances of Copilot understanding the question, and thus responding with an accurate answer.
> - Record picker needs [Dataverse Search to be enabled and configured](/power-platform/admin/configure-relevance-search-organization) for the typeahead search capability. 

## Provide feedback 

To provide feedback to help improve copilot, select the thumb up or thumb down icon included in each copilot response. Feedback can be submitted for each copilot response. 

### Provide positive feedback 

1. On the right navigation bar, select the thumb up icon. 
2. Optionally, provide feedback in your own words about what you liked. 
3. Select **Submit** after you're done entering your feedback. 

### Provide feedback for improvement 

1. On the right navigation bar, select the thumb down icon. 
2. Optionally, provide feedback, such as feedback about the content of copilot’s response, or a description in your own words about what went wrong, or how you would like copilot to improve. 
3. Select **Submit** after you're done entering your feedback. 

