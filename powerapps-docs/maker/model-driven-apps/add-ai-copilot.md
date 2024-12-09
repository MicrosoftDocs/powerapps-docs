---
title: Add Copilot chat for app users in model-driven apps
description: Learn how to turn on Copilot chat in model-driven apps to help app users get AI-powered insights about their data.
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

# Add Copilot for app users in model-driven apps

Copilot chat for model-driven apps in Power Apps is a next-generation AI assistant that helps app users get insights about the data in their apps through conversation in natural language. Copilot chat helps app users boost their productivity through AI-powered insights and intuitive app navigation.

> [!IMPORTANT]
>
> This feature is generally available in Dynamics 365 apps and is available as a preview feature in Power Apps.
>
> - To use this capability, your environment must have its language set to English.
> - You must allow data movement across regions for Generative AI features as a prerequisite for using Copilot in Power Apps. This step is especially important if your organization and your environment are in different regions. Learn more in [Turn on copilots and generative AI features](/power-platform/admin/geographical-availability-copilot#enable-data-movement-across-regions).
> - Preview features aren't meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.
> - For more information, go to our [preview terms](https://go.microsoft.com/fwlink/?linkid=2189520).
> - This capability is powered by [Azure OpenAI Service](/azure/cognitive-services/openai/overview).
> - This capability may be subject to usage limits or capacity throttling.

When enabled, Copilot chat can be accessed through the Copilot icon in the right navigation bar in a model-driven app. The Copilot chat pane can be opened or minimized as desired.

:::image type="content" source="media/model-driven-app-copilot.png" alt-text="Screenshot of the Copilot chat pane in a model-driven app." lightbox="media/model-driven-app-copilot.png":::

Copilot chat in model-driven apps can answer questions about the Microsoft Dataverse table data in the environment. Copilot can also help you navigate the app. For example, when a user enters *take me to Online Cases* or *show me Cruise Support Tickets*, Copilot automatically opens the relevant app screens. Learn more in [Use Copilot chat in model-driven apps](../../user/use-copilot-model-driven-apps.md).

## Enable Copilot for model-driven apps in your environment

Power Platform administrators enable the Copilot chat feature in model-driven apps for all the users in their environments in the [Power Platform admin center](https://admin.powerplatform.microsoft.com).

> [!IMPORTANT]
>
> - Copilot chat for app users in model-driven apps isn't enabled by default. Administrators must manually enable this feature for their environments in the [Power Platform admin center](https://admin.powerplatform.microsoft.com).
> - Questions and answers about enterprise data environments that have a [customer-managed key](/power-platform/admin/customer-managed-key) or [Customer Lockbox](/power-platform/admin/about-lockbox) won't use your data stored in Dataverse. You might get answers from Copilot, but they won't be based on your Dataverse data.

1. Sign in to the Power Platform admin center at [https://admin.powerplatform.microsoft.com](https://admin.powerplatform.microsoft.com).

1. In the navigation pane, go to **Environments** and select the environment where you want to enable Copilot chat for app users in model-driven apps. Select **Settings** for this environment on the command bar.

1. In **Settings** for the selected environment, select **Product** > **Features**.

   :::image type="content" source="media/Environment_features.png" alt-text="Screenshot that shows where to set environment features.":::

1. In the **Features** section, set the value for **Allow users to analyze data using an AI-powered chat experience in canvas and model-driven apps** to the setting that's appropriate for your environment.

   - **Default**. Copilot chat is *disabled for a Power Apps licensed environment and enabled for a Dynamics 365 licensed environment*.
   - **On**. Copilot chat is enabled for the environment regardless of the environment licensing type.
   - **Off**. Copilot chat is disabled for the environment regardless of environment licensing type.
   :::image type="content" source="media/copilot_for_apps_users_on.png" alt-text="Screenshot that shows how to turn on Copilot in an environment.":::

1. **Save** your changes.

## Disable Copilot chat for a model-driven app

Makers can disable Copilot chat for a specific model-driven app. In app designer, open the model-driven app for **Edit**, and then select **Settings** on the command bar. Select **Upcoming** on the **Settings** screen, set **Copilot control** to **Default** or **Off**, and then select **Save**.

**Save** and **Publish** the model-driven app for the changes to take effect.

:::image type="content" source="media/turnoff_copilot_model_apps.png" alt-text="Screenshot that shows how to turn off Copilot chat in a model-driven app.":::

### Reset to environment value

Makers can set the Copilot control for the app to match the environment setting by selecting **Reset to environment value** on the **Upcoming** tab of app settings.

## Provide feedback in Copilot

To provide feedback to help us improve Copilot's responses, app users can select the "thumb up" or "thumb down" icon after each Copilot response. Optionally, app users can provide feedback in their own words about what they liked or what went wrong, or how they would like Copilot to improve.

### Disable feedback for app users

1. Sign in to [Power Apps](https://make.powerapps.com/).
1. Go to **Tables**, and then open the **Organization** table.
1. In the **Organization columns and data** section, select **+nnn more** to display the column search box.
1. In the search box, search for the **Allow users to provide feedback for App Copilot** column.
   :::image type="content" source="media/disable-mda-copilot-feedback1.png" alt-text="Screenshot that shows where to find the Allow users to provide feedback for App Copilot column.":::

1. Set the column to **No**, and then **Save** the table.
   :::image type="content" source="media/disable-mda-copilot-feedback2.png" alt-text="Screenshot that shows where to set the Allow users to provide feedback for App Copilot column to No.":::

### Known limitations

1. **Copilot for app users** allows users to retrieve information from Dataverse through read-only operations. This means that users can only view data that matches their queries and can't make any changes to the data.
1. Create, update, or other generic actions such as enable or disable Copilot and create a memo aren't supported.
1. [Summarization](/dynamics365/sales/copilot-overview#record-summarization) skill feature is available in [Dynamics 365 Sales copilot](/dynamics365/sales/copilot-overview) and not in **Copilot for app user**.
1. **Copilot for app users** isn't supported with the Power Apps mobile app.

## Related information

- [FAQ for Copilot chat in model-driven apps](../common/faqs-copilot-model-driven-app.md)
- [Responsible AI FAQs for Power Apps](../common/responsible-ai-overview.md)
- [Add Copilot control to a canvas app (preview)](../canvas-apps/add-ai-copilot.md)
- [Enable copilots and generative AI features in Power Apps](/power-platform/admin/geographical-availability-copilot#enable-data-movement-across-regions)
