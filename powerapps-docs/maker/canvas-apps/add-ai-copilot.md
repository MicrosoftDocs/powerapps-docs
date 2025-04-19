---
title: Add a Copilot control to a canvas app (preview)
description: Learn how to add a Copilot control, an AI assistant, to your canvas apps in Microsoft Power Apps.
author: mduelae
ms.topic: conceptual
ms.custom:
  - canvas
  - ai-gen-diyeditor
ms.collection: 
    - bap-ai-copilot
    - get started
ms.reviewer: 
ms.date: 4/16/2025
ms.subservice: canvas-maker
ms.author: tapanm
search.audienceType: 
  - maker
contributors:
  - mduelae
ai-usage: ai-assisted
---

# Add a Copilot control to a canvas app (preview)

[!INCLUDE [preview-banner](~/../shared-content/shared/preview-includes/preview-banner.md)]

The Copilot control is an AI assistant that you can add to your canvas apps. Copilot lets app users get insights about the data in your app through natural language conversations with an AI-powered copilot. Makers can add the control to any canvas app and choose which data provide answers.

> [!IMPORTANT]
>
> - This is a preview feature.
> - Preview features aren't meant for production use and might have restricted functionality. These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?linkid=2216214), and are available before an official release so that customers can get early access and provide feedback.

> [!NOTE]
>
> This feature is powered by [Azure OpenAI Service](/azure/cognitive-services/openai/overview).

## Prerequisites

Ensure you meet the prerequisites and region availability in [Copilot in Power Apps overview (preview)](ai-overview.md).

Copilot doesn't work in environments that have a customer-managed key or [Customer Lockbox](/azure/security/fundamentals/customer-lockbox-overview).

### Set up Copilot for your environment

Before app users can use the Copilot chat experience in a canvas app, a Power Platform administrator must enable **Allow users to analyze data using an AI-powered chat experience in canvas and model-driven apps** in the [Power Platform admin center](https://admin.powerplatform.microsoft.com/home). Learn more in [Manage feature settings](/power-platform/admin/settings-features#copilot-preview).

:::image type="content" source="media/copilot/copilot-for-app-users-on.png" alt-text="Screenshot of the Power Platform admin center environment settings, showing Copilot features.":::

### Set up Copilot for your canvas app

Before you can add a Copilot control to your canvas app, you need to turn on **Copilot component** and **Edit in Copilot Studio** in the app settings in [Power Apps](https://make.powerapps.com/).

**Copilot component**: Turns on the Copilot feature in your canvas app so that you can add the Copilot control to your app and connect it to a copilot.

**Edit in Copilot Studio**: Lets you customize the copilot using Copilot Studio. If you leave this option off, only the default copilot is available in your app.

1. Open your [canvas app for editing](edit-app.md) in Power Apps Studio. On the command bar, select **Settings** > **Updates**.

1. On the **Preview** tab, find and turn on the **Copilot component** and **Edit in Copilot Studio** settings.

   :::image type="content" source="media/copilot/copilot-component-edit-in-copilot-studio.png" alt-text="Screenshot of app settings in Power Apps Studio, with the Copilot component and Edit in Copilot Studio options highlighted.":::

## Add the Copilot control to your canvas app

Now that all settings are configured, with your [canvas app open for editing](edit-app.md):

1. In the app [authoring menu](power-apps-studio.md#5--app-authoring-menu), select **Insert**, and then select **Copilot (preview)**.

1. You're prompted to add a data source to Copilot. Select a Dataverse table as the data source.

:::image type="content" source="media/copilot/add-data-to-copilot.png" alt-text="Screenshot of the Copilot control properties pane, with the Create new copilot button highlighted.":::

> [!NOTE]
> The Copilot control only supports Dataverse tables for the data source.

## Customize the copilot using Copilot Studio

Copilot Studio is an app that lets you create and edit copilots for your apps. You can define your copilot's topics, actions, and other features. For example, you can make your copilot respond to specific questions about your app's data or perform actions like opening a screen or sending an email.

You can customize your newly connected copilot in Power Apps through the properties menu in Power Apps.

1. With the Copilot control on your canvas selected, choose **Edit** next to the **Customize copilot** field in **Properties**.

1. If you don't have a copilot created already, select **Create new copilot** in the **Customize Copilot** pane. A Copilot control in Power Apps Studio does not support enabling an existing Copilot from Copilot Studio.

   :::image type="content" source="media/copilot/edit-in-copilot-studio.png" alt-text="Screenshot of the Copilot control properties pane, with the Edit and Edit in Copilot Studio buttons highlighted." lightbox="media/copilot/edit-in-copilot-studio.png":::

   [Copilot Studio](https://web.powerva.microsoft.com/) opens in a new tab. Any modifications made in Copilot Studio appear in your connected copilot in your canvas app.

Learn more in [Quickstart: Create and deploy a copilot](/microsoft-copilot-studio/fundamentals-get-started).

## Collect feedback from app users

Makers and app users can provide feedback on how satisfied they are with the copilot's responses by selecting the **Like** (thumbs up) or **Dislike** (thumbs down) button for each response. They can enter detailed feedback in the text box and then select **Submit**.

Their feedback is sent to Microsoft to help us improve the Copilot control.

## Disallow feedback from app users

If you don't want your app users to provide feedback to Microsoft, turn off the feedback option.

1. Sign in to [Power Apps](https://make.powerapps.com) and select **Tables** from the [left navigation pane](intro-maker-portal.md#1--left-navigation-pane).

1. Select the **Organization** table from the list.

1. In the **Organization columns and data** section, select the column headers list. The **Show existing column** popup appears.

1. Search for **Allow users to provide feedback for App Copilot** and make sure the check box in unchecked.

1. Select **Save**.

:::image type="content" source="media/copilot/allow-users-feedback-setting.png" alt-text="Screenshot that shows how to get to the Show existing column popup." lightbox="media/copilot/allow-users-feedback-setting.png":::

## Related information

- [Build apps through conversation (preview)](ai-conversations-create-app.md)
- [Use your prompt in Power Automate](/ai-builder/use-a-custom-prompt-in-flow)
- [Add Copilot for app users in model-driven apps](../model-driven-apps/add-ai-copilot.md)
- [Power Apps Copilot control (video)](https://youtu.be/11mTv6vZTvY?feature=shared)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
