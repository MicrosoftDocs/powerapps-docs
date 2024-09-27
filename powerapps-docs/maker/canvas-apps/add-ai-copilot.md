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
ms.date: 9/25/2024
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

The Copilot control is an AI assistant that you can add to your canvas apps in Microsoft Powr Apps. Copilot lets app users get insights about the data in your app through natural language conversations with an AI-powered copilot. You can add the control to any canvas app and choose which data provide answers.

> [!IMPORTANT]
>
> - This is a preview feature.
> - Preview features aren't meant for production use and might have restricted functionality. These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?linkid=2216214), and are available before an official release so that customers can get early access and provide feedback.

> [!NOTE]
>
> This feature is powered by [Azure OpenAI Service](/azure/cognitive-services/openai/overview).

## Availability

- This feature might be subject to usage limits or capacity throttling.
- Copilot doesn't work in environments that have a customer-managed key or [Customer Lockbox](/azure/security/fundamentals/customer-lockbox-overview).

## Prerequisites

- Your environment must be in the United States region with your browser language set to English (United States). Check regions for the future in [Explore Copilot features by geography and languages](https://releaseplans.microsoft.com/en-US/availability-reports/?report=copilotfeaturereport).
- [Turn on copilots and generative AI features](/power-platform/admin/geographical-availability-copilot#turn-on-copilots-and-generative-ai-features-1) to allow data movement across regions. Learn more in [Copilots and generative AI features that are available when you enable data movement across regions](/power-platform/admin/geographical-availability-copilot#copilots-and-generative-ai-features-that-are-available-when-you-enable-data-movement-across-regions).

### Set up Copilot for your environment

Before app users can use the Copilot chat experience in a canvas app, a Power Platform admininstrator must enable the following settings in the [Power Platform admin center](https://admin.powerplatform.microsoft.com/home).

- Open your environment and go to **Settings** > **Product** > **Features**.
- Under **Copilot**, toggle to **On** these settings:
  - **Enable new AI-powered Copilot features for people who make apps**. Learn more in [Prerequisites for the Copilot features in Power Apps](ai-overview.md#prerequisites).
  - **Allow users to analyze data using an AI-powered chat experience in canvas and model-driven apps**. Learn more in [Manage feature settings](/power-platform/admin/settings-features#copilot-preview).

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

1. You're prompted to add a data source to Copilot. Add a data source.

:::image type="content" source="media/copilot/add-data-to-copilot.png" alt-text="Screenshot of the Copilot control properties pane, with the Create new copilot button highlighted.":::

## Customize the copilot using Copilot Studio

Copilot Studio is an app that lets you create and edit copilots for your apps. You can define your copilot's topics, actions, and other features. For example, you can make your copilot respond to specific questions about your app's data or perform actions like opening a screen or sending an email.

You can customize your newly connected copilot in Power Apps through the properties menu in Power Apps.

1. With the Copilot control on your canvas selected, choose **Edit** next to the **Customize copilot** field in **Properties**.

1. If you don't have a copilot created already, select **Create new copilot** in the **Customize Copilot** pane. With an exsiting copilot, you see **Edit in Copilot Studio** instead. Choose an option to create or edit your copilot in Copilot Studio.

   :::image type="content" source="media/copilot/edit-in-copilot-studio.png" alt-text="Screenshot of the Copilot control properties pane, with the Edit and Edit in Copilot Studio buttons highlighted." lightbox="media/copilot/edit-in-copilot-studio.png":::

   [Copilot Studio](https://web.powerva.microsoft.com/) opens in a new tab. Any modifications made in Copilot Studio appear in your connected copilot in your Power Apps app.

Learn more in [Quickstart: Create and deploy a copilot](/microsoft-copilot-studio/fundamentals-get-started).

## Collect feedback from app users

App users can indicate how satisfied they are with the copilot's responses by selecting the **Like** (thumbs up) or **Dislike** (thumbs down) button for each response. They can enter detailed feedback in the text box and then select **Submit**.

Their feedback is sent to Microsoft to help us improve the Copilot control. You can view the feedback in Copilot Studio.

## Disallow feedback from app users

If you don't want your app users to provide feedback to Microsoft, turn off the feedback option.

1. Sign in to [Power Apps](https://make.powerapps.com) and select **Tables** from the [left navigation pane](intro-maker-portal.md#1--left-navigation-pane).

1. Select the **Organization** table from the list.

1. In the **Organization columns and data** section, select the column headers list. The **Show existing column** popup appears.

1. Search for **Allow users to provide feedback for App Copilot** and make sure the check box in unchecked.

1. Select **Save**.

:::image type="content" source="media/copilot/allow-users-feedback-setting.png" alt-text="Screenshot that shows how to get to the Show existing column popup." lightbox="media/copilot/allow-users-feedback-setting.png":::

## See also

- [Build apps through conversation (preview)](ai-conversations-create-app.md)
- [Use your prompt in Power Automate](/ai-builder/use-a-custom-prompt-in-flow)
- [Add Copilot for app users in model-driven apps](../model-driven-apps/add-ai-copilot.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
