---
title: Use Copilot chat in model-driven apps
description: Learn how to use Copilot chat to gain insights about the data in your model-driven apps.
author: srihas
ms.component: pa-user
ms.topic: overview
ms.date: 06/11/2024
ms.subservice: end-user
ms.author: srihas
ms.custom: ""
ms.reviewer: sericks
ms.assetid: 
search.audienceType: 
  - enduser
---

# Use Copilot chat in model-driven apps

Copilot chat for model-driven apps in Power Apps is a next-generation AI assistant that helps you gain insights into the data in your apps through conversations in natural language. Copilot chat helps you boost your productivity through AI-powered insights and navigation assistance.

> [!IMPORTANT]
>
> This feature is generally available in Dynamics 365 apps.
>
> This feature is a preview feature in Power Apps.
>
> - Preview features aren't meant for production use and might have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.
> - An administrator must enable Copilot chat in your application before it becomes visible in your app. More information: [Add Copilot for app users in model-driven apps](../maker/model-driven-apps/add-ai-copilot.md)

## Copilot pane

After Copilot chat is enabled, you can access it through the Copilot icon near the upper right of the page or through the Copilot icon that is right of the command bar. You can expand or collapse the Copilot pane as you want. By default, the pane is expanded after Copilot chat is enabled.

:::image type="content" source="media/copilot-icons.png" alt-text="Screenshot that shows the Copilot icons on a page.":::

## Use Copilot to ask questions

Copilot chat in model-driven apps can answer questions about the Dataverse table data in the app. It can also help you navigate the model-driven app. For example, if you enter **Navigate to challenges**, Copilot in the model-driven app automatically opens the relevant page in the app.

:::image type="content" source="media/navigate-to-challenges.png" alt-text="Screenshot where Copilot opened a page in response to a prompt.":::

## Copilot chat suggested questions

To help you get started, Copilot chat can suggest questions for you to ask. You can edit and personalize these questions (also known as _prompts_) based on your app and the type of insight that you need from Copilot.

To view more suggested prompts, select **View prompts** in the Copilot pane. Many of the suggested prompts have placeholders that you must replace with appropriate text to complete the question.

:::image type="content" source="media/ask-questions.png" alt-text="Screenshot that shows suggested prompts that have placeholders.":::

## Record picker to select object of the question

You can use the record picker to select the object of your question. Enter a slash (**/**) to open the record picker, and then enter the name of the record. Select the record that you want, and complete the question to make it meaningful. Finally, submit the question to Copilot to view the response. Record picker is available in Dynamics 365 Sales and Power Apps model-driven apps.

:::image type="content" source="media/record-picker.png" alt-text="Screenshot that shows the record picker being used to select the object of a question." lightbox="media/record-picker.png":::

For example, when you ask a question like "What are the details for Contoso?" there could be many accounts with names that include *Contoso*, such as Contoso Inc., Contoso Co., Contoso NW, and so on. What you really want are the details for Contoso Inc. Record picker helps copilot scope the question to the right record for a more relevant and accurate response.

> [!NOTE]
>
> - By using the record picker, you increase the likelihood that Copilot chat can understand your question and therefore respond with an accurate answer.
> - Record picker requires that [Dataverse Search is enabled and configured](/power-platform/admin/configure-relevance-search-organization) for the type-ahead search capability.

## Provide feedback

Every Copilot response includes a **Like** button ("thumbs up" icon) and a **Dislike** button ("thumbs down" icon). For each response, you can select one of these icons to provide feedback. This feedback helps improve Copilot chat.

### Provide positive feedback

1. In the Copilot pane, select the **Like** button for a Copilot response.
1. Optional: Provide feedback in your own words about what you liked.
1. Indicate whether you want to share your prompt and the generated response with Microsoft to help improve the service.
1. After you finish entering your feedback, select **Submit**.

### Provide feedback for improvement

1. In the Copilot pane, select the **Dislike** button in a Copilot response.
1. Optional: Provide feedback, such as feedback about the content of Copilot's response, a description in your own words about what went wrong, or a description of how you want Copilot to improve.
1. Indicate whether you want to share your prompt and the generated response with Microsoft to help improve the service.
1. After you finish entering your feedback, select **Submit**.
