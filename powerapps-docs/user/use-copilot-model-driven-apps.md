---
title: Use Copilot chat in model-driven apps
description: Learn how to use Copilot chat to gain insights about the data in your model-driven apps.
author: srihas
ms.component: pa-user
ms.topic: overview
ms.date: 01/08/2026
ms.update-cycle: 180-days
ms.subservice: end-user
ms.author: srihas
ms.custom: ""
ms.reviewer: smurkute
ms.assetid: 
search.audienceType: 
  - enduser
ms.collection: 
    - bap-ai-copilot 
---

# Use Copilot chat in model-driven apps

Copilot chat for model-driven apps in Power Apps is a next-generation AI assistant that helps you gain insights into the data in your apps through conversations in natural language. Copilot chat helps you boost your productivity through AI-powered insights and navigation assistance.

> [!IMPORTANT]
>
> - This feature is generally available in Dynamics 365 apps, but remains a preview feature in Power Apps.
>
> - Preview features aren't meant for production use and might have restricted functionality These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?linkid=2189520), and are available before an official release so that customers can get early access and provide feedback.


> [!NOTE]
>
> Copilot chat in Power Apps is a preview feature that will be deprecated for model-driven apps in environments not [enabled for Dynamics 365 apps](/power-platform/admin/create-environment#create-an-environment-with-a-database), starting January 2026. We recommend switching to [Microsoft 365 Copilot chat](use-microsoft-365-copilot-model-driven-apps.md). During the transition period, makers can enable either one or both chat experiences. For more information, see [Deprecation of Copilot chat in model-driven apps](/power-platform/important-changes-coming#deprecation-of-copilot-chat-in-model-driven-apps)

## Prerequisites

An administrator must enable Copilot chat in your application before it becomes visible in your app. More information: [Add Copilot for app users in model-driven apps](../maker/model-driven-apps/add-ai-copilot.md).

## Copilot pane

After Copilot chat is enabled, you can access it through the Copilot icon near the upper-right corner of the page or through the Copilot icon at the right side of the command bar. You can expand or collapse the Copilot pane as you want. By default, the pane is expanded after Copilot chat is enabled.

:::image type="content" source="media/copilot-icons.png" alt-text="Screenshot that shows the Copilot icons on a page.":::

## Use Copilot to ask questions

Copilot chat in model-driven apps can answer questions about the Dataverse table data in the app. It can also help you navigate the app. For example, if you enter **Navigate to challenges**, Copilot automatically opens the relevant page in the app.

:::image type="content" source="media/navigate-to-challenges.png" alt-text="Screenshot that shows that Copilot opened a page in response to a request.":::

## Copilot chat suggested questions

To help you get started, Copilot chat can suggest questions for you to ask. You can edit and personalize these questions (also known as prompts) based on your app and the type of insight that you need from Copilot.

To view more suggested questions, select **View prompts** in the Copilot pane. Many of the suggested questions have placeholders that you must replace with appropriate text to complete the question.

:::image type="content" source="media/ask-questions.png" alt-text="Screenshot that shows suggested prompts that have placeholders.":::

## Use the record picker

When you ask a question, you can use the record picker to select the object of your question. The record picker helps Copilot chat understand the context of your question and provide a more accurate response.

Enter a slash (**/**) to open the record picker, and then enter the name of the record. Select the record that you want, and complete the question to make it meaningful. Finally, submit the question to Copilot to view the response.

For example, you ask Copilot "What are the details for Contoso?" Many accounts might have "Contoso" in their name, such as Contoso, Inc., Contoso Co., and Contoso NW. What you really want are the details for Contoso, Inc. The record picker helps Copilot scope the question to the right record for a more relevant and accurate response.

:::image type="content" source="media/record-picker.png" alt-text="Screenshot that shows the record picker being used to select the object of a question." lightbox="media/record-picker.png":::

The record picker is available in Dynamics 365 Sales and Power Apps model-driven apps.

> [!NOTE]
>
> - By using the record picker, you increase the likelihood that Copilot chat can understand your question and therefore respond with an accurate answer.
> - The record picker requires that [Dataverse search is enabled and configured](/power-platform/admin/configure-relevance-search-organization) for the type-ahead search capability.

## Provide feedback

Unless your admin turned off the feedback feature, every Copilot response includes a **Like** button ("thumbs up" icon) and a **Dislike** button ("thumbs down" icon). For each response, you can select one of these icons to provide feedback that helps us improve Copilot chat. Select the "thumbs up" or "thumbs down" icon as appropriate. Optionally, provide feedback in your own words about what you liked or didn't like about the response. When you're done, select **Submit**.
