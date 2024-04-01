---
title: Use Copilot in model-driven apps 
description: Learn how to use Copilot in model-driven apps.
author: srihas
ms.component: pa-user
ms.topic: overview
ms.date: 03/19/2024
ms.subservice: end-user
ms.author: srihas
ms.custom: ""
ms.reviewer: sericks
ms.assetid: 
search.audienceType: 
  - enduser
---

# Use Copilot in model-driven apps 

Copilot for model-driven apps in Power Apps is a next-generation AI assistant to help you get insights about the data in your apps through conversation in natural language. Copilot helps you boost your productivity through AI-powered insights and navigation assistance. 

> [!IMPORTANT]
> This feature is generally available in Dynamics 365 apps.
>
> This feature is a preview feature in Power Apps.
> - Preview features aren’t meant for production use and may have restricted functionality.
> - Preview features are available before an official release so that customers can get early access and provide feedback.
> - An administrator must enable Copilot in your application for you to see it in your app. More information: [Add copilot for app users in model-driven apps](../maker/model-driven-apps/add-ai-copilot.md)

## Copilot pane 

When enabled, Copilot can be accessed through the Copilot icon near the top-right part of your screen or through the Copilot icon that is left of the command bar. The Copilot pane can be expanded or collapsed, as desired. When enabled, the pane is expanded by default.

:::image type="content" source="media/copilot-icons.png" alt-text="Copilot icons":::

## Use Copilot to ask questions 

Copilot in model-driven apps can answer questions about the Microsoft Dataverse table data in the app. Copilot can also help you navigate the model-driven app. For example, when a user enters **Navigate to challenges**, Copilot in the model-driven app automatically opens the relevant page in the app. 

:::image type="content" source="media/navigate-to-challenges.png" alt-text="Navigate to challenges entered as a prompt.":::

## Copilot suggested questions 

Copilot can suggest questions for you to ask to help you get started. These questions (also called _prompts_) can be edited and personalized for your app and the type of insight you need from Copilot. 

You see more suggested prompts by selecting **View prompts** within the Copilot pane. Many of the suggested questions have placeholders that you need to replace with an appropriate text that completes the question. 

:::image type="content" source="media/ask-questions.png" alt-text="Edit a prompt to ask a question.":::

## Record picker to select object of the question 

You can use the record picker to select the object of your question. Type “**/**” character to open the record picker and continue typing the name of the record. Then select the record of your choice and complete the question to make it meaningful. Submit the question to Copilot to view the response. 

:::image type="content" source="media/record-picker.png" alt-text="Use the record picker to select the object of your question.":::

> [!Note]
> - Using record picker increases the chances of Copilot understanding the question, and thus responding with an accurate answer.
> - Record picker needs [Dataverse Search to be enabled and configured](/power-platform/admin/configure-relevance-search-organization) for the type-ahead search capability. 

## Provide feedback 

To provide feedback to help improve Copilot, select the **Like** or **Dislike** icon included in each Copilot response. Feedback can be submitted for each Copilot response. 

### Provide positive feedback 

1. In the **Copilot** pane, select the **Like** icon on a Copilot response. 
1. Optionally, provide feedback in your own words about what you liked.
1. Indicate if you want to share your prompt and generated response with Microsoft to improve the service.
1. Select **Submit** after you're done entering your feedback. 

### Provide feedback for improvement 

1. In the **Copilot** pane, select the **Dislike** icon on a Copilot response. 
1. Optionally, provide feedback, such as feedback about the content of Copilot’s response, or a description in your own words about what went wrong, or how you would like Copilot to improve.
1.  Indicate if you want to share your prompt and generated response with Microsoft to improve the service.
1. Select **Submit** after you're done entering your feedback. 

