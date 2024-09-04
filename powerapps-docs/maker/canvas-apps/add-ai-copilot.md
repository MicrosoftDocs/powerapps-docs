---
title: Add a copilot to your canvas app (preview)
description: Learn how to add a next-generation AI assistant to your canvas apps to help your app users with their requests.
author: mduelae
ms.topic: conceptual
ms.custom:
  - canvas
  - ai-gen-diyeditor
ms.collection: 
    - bap-ai-copilot
    - get started
ms.reviewer: 
ms.date: 7/9/2024
ms.subservice: canvas-maker
ms.author: tapanm
search.audienceType: 
  - maker
contributors:
  - mduelae
ai-usage: ai-assisted
---

# Add a copilot to your canvas app (preview)

[!INCLUDE [preview-banner](~/../shared-content/shared/preview-includes/preview-banner.md)]

The Copilot control is a next-generation AI assistant that you can add to your canvas apps. It lets app users get insights about the data in your app through natural language conversations with an AI-powered bot. You can add the control to any canvas app and choose what data it can provide answers for.

> [!IMPORTANT]
>
> - This feature is available only in certain regions. Learn more in [Explore Copilot features by geography and languages](https://releaseplans.microsoft.com/en-US/availability-reports/?report=copilotfeaturereport).
> - To use Copilot in Power Apps and other generative AI features, you need to allow data movement across regions. Learn more in [Copilots and generative AI features that are available when you enable data movement across regions](/power-platform/admin/geographical-availability-copilot#copilots-and-generative-ai-features-that-are-available-when-you-enable-data-movement-across-regions).
> - Preview features aren't meant for production use and might have limited functionality. These features are available before an official release so that you can try them out and give us feedback.
> - For more information, read our [preview terms](https://go.microsoft.com/fwlink/?linkid=2189520).
> - This feature is powered by [Azure OpenAI Service](/azure/cognitive-services/openai/overview).
> - This feature might be subject to usage limits or capacity throttling.
> - Copilot doesn't work in environments that have a customer-managed key or Customer Lockbox.

## Prerequisites

- Your environment must be in the United States region.

- Your browser language must be set to English (United States).

- Meet the prerequisites for Copilot features in Power Apps. Learn more in [Create conversational apps with Copilot in Power Apps](ai-overview.md).

### Set up Copilot for your environment

Before app users can use the Copilot chat experience in a canvas app, an administrator needs to turn on **Allow users to analyze data using an AI-powered chat experience in canvas and model-driven apps (preview)** in your environment. Learn more in [Manage feature settings](/power-platform/admin/settings-features#copilot-preview).

:::image type="content" source="media/copilot/copilot-for-app-users-on.png" alt-text="Screenshot of the Power Platform admin center environment settings, showing Copilot features.":::

### Set up Copilot for your canvas app

Before you can add a Copilot control to your canvas app, you need to turn on **Copilot component** and **Edit in Copilot Studio** in your app settings.

- **Copilot component**: Turns on the Copilot feature in your canvas app so that you can add the Copilot control to your app and connect it to a copilot.
- **Edit in Copilot Studio**: Lets you customize the copilot using Copilot Studio. If you leave this option off, only the default copilot is available in your app.

1. Open your [canvas app for editing](edit-app.md) in Power Apps Studio. On the command bar, select **Settings** > **Updates**.

1. On the **Preview** tab, turn on **Copilot component** and **Edit in Copilot Studio**.

    :::image type="content" source="media/copilot/copilot-component-edit-in-copilot-studio.png" alt-text="Screenshot of app settings in Power Apps Studio, with the Copilot component and Edit in Copilot Studio options highlighted.":::

## Add the Copilot control to your canvas app

With your [canvas app open for editing](edit-app.md):

1. In the app authoring menu, select **Insert**, and then select **Copilot (preview)**.

1. Create a copilot to connect to, or connect to an existing one:

    - To connect the Copilot control to a new copilot, select **Create new copilot**.

      :::image type="content" source="media/copilot/customize-copilot.png" alt-text="Screenshot of the Copilot control properties pane, with the Create new copilot button highlighted.":::

    - To connect it to an existing copilot, select the **Advanced** properties tab. In the **BotSchemaName** property, select a published copilot from the list. The copilot must be published in the environment you're working in.

## Customize the copilot using Copilot Studio

The default Copilot control is connected to a generic bot that can answer common questions about Power Apps. To customize the bot, use Copilot Studio.

Copilot Studio is an app that lets you create and edit chatbots for your apps. You can use it to define a bot's topics, actions, and other features. For example, you can make your bot respond to specific questions about your app's data or perform actions like opening a screen or sending an email.

1. With the Copilot control selected, select **Edit** next to the **Customize copilot** property.

1. Select **Edit in Copilot Studio**.

    Copilot Studio opens in a new tab.

    :::image type="content" source="media/copilot/edit-in-copilot-studio.png" alt-text="Screenshot of the Copilot control properties pane, with the Edit and Edit in Copilot Studio buttons highlighted.":::

Learn more in [Quickstart: Create and deploy a copilot](/microsoft-copilot-studio/fundamentals-get-started).

## Collect feedback from app users

App users can indicate how satisfied they are with the bot's responses by selecting the **Like** (thumbs up) or **Dislike** (thumbs down) button for each response. They can enter detailed feedback in the text box and then select **Submit**.

Their feedback is sent to Microsoft to help us improve the Copilot control. You can view the feedback in Copilot Studio.

## Disallow feedback from app users

If you don't want your app users to provide feedback to Microsoft, turn off the feedback option.

1. Sign in to [Power Apps](https://make.powerapps.com).

1. In the [left navigation pane](intro-maker-portal.md#1--left-navigation-pane), select **Tables** > **Organization**.

1. In the **Organization columns and data** section, select the list of columns and search for **Allow users to provide feedback for App Copilot**.

1. Set the toggle to **No**.

## Related information

- [Build apps through conversation (preview)](ai-conversations-create-app.md)
- [Add a Chatbot control to a canvas app (preview)](add-ai-chatbot.md)
- [Text generation model (preview)](/ai-builder/prebuilt-azure-openai)
- [Add Copilot for app users in model-driven apps](../model-driven-apps/add-ai-copilot.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
