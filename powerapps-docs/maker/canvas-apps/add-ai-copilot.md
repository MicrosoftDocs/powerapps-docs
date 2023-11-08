---
title: Add Copilot control for canvas app users
description: Add Copilot AI control for apps users to your canvas app.
author: mduelae
ms.topic: conceptual
ms.custom: canvas
ms.collection: get-started
ms.reviewer: 
ms.date: 3/13/2023
ms.subservice: canvas-maker
ms.author: tapanm
search.audienceType: 
  - maker
contributors:
  - mduelae
---

# Add Copilot Control to a canvas app (preview)

[This article is prerelease documentation and is subject to change.]

The Copilot control is a next-generation AI assistant that makers can add to their canvas apps for end-users. This is an AI-powered experience for app users to get insights about the data in their apps through conversation in natural language. Makers can add this control to any canvas app and choose what data it can answer questions about.

> [!IMPORTANT]
> - To use this capability your environment must be in the US region.
> - Preview features aren’t meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.
> - For more information, go to our [preview terms](https://go.microsoft.com/fwlink/?linkid=2189520).
> - This capability is powered by [Azure OpenAI Service](/azure/cognitive-services/openai/overview).
> - This capability  may be subject to usage limits or capacity throttling.
> - Copilot control isn't supported and won't work for environments that have customer-managed key (CMK) or have lockbox.

## Step 1 - Enable Copilot for your environment

In order for end users to use the Copilot chat experience in a canvas app, an admin must first turn on the feature, **Allow users to analyze data using an AI-powered chat experience in canvas and model-driven apps (preview)** in their environment. For more information, see [Manage feature settings](/power-platform/admin/settings-features#copilot-preview).

When the feature setting is turned on, a maker can then enable **Copilot component** from the app settings in Power Apps Studio and then add the Copilot control to the app, allowing end users to use the AI-powered chat experience.

## Step 2 - Enable Copilot component for a canvas app 

Open your [canvas app open for editing](edit-app.md) in Power Apps Studio:

1. On the command bar, select **Settings** > **Upcoming features**.
2. From the **Preview** tab, set the toggle for **Copilot component** to **On**.

   > [!div class="mx-imgBorder"]
   > ![Turn on Copilot control.](media/copilot/copilot-1.png)

## Step 3 - Add Copilot control to your canvas app

Add the **Copilot (preview)** control to your canvas app enabling end users to gain insights about the data in their apps through the chat experience.

With your [canvas app open for editing](edit-app.md) in Power Apps Studio:

1. On the app authoring menu, select **Insert** and select **Copilot (preview)** to add this control.

   > [!div class="mx-imgBorder"]
   > ![Add the copilot control.](media/copilot/Copilot-Insert-menu.png)

### Choose data for Copilot

1. When the Copilot control is added to the canvas app, select a data source from the pane. Copilot can only provide data insights on a single Dataverse table when an end user asks a question. 

   > [!div class="mx-imgBorder"]
   > ![Select a data source.](media/copilot/copilot-3.png)

   Or, from the control **Properties** tab, select **Data source (Items)** and choose a Dataverse table for your data source.
   
   > [!div class="mx-imgBorder"]
   > ![Select fields or views.](media/copilot/copilot-choose-data-properties.png)
   
   > [!TIP]
   > Any Dataverse table in your environment that's not added to your canvas app can be added as a datasource for Copilot control.

2. Select the specific **Fields** and/or **View** that the Copilot control answers questions for.
   
3. To configure the selected table and its columns for use in Copilot, see [Configure tables to use Copilot](../data-platform/table-settings-for-copilot.md).

  > [!NOTE]
  > Copilot can only answer questions for smaller datasets in a canvas app. The only exception to the dataset limit is when a Dataverse table is selected as the data source. 


### Configure the Copilot control (optional)

In addition to choosing the data source for Copilot, you can also configure the following Copilot properties in a canvas app:

- **Title**: Replaces the control's default title of **Have a question about this app? Ask Copilot**, and can be replaced with a more appropriate title that reflects the assistance that the Copilot control can provide to app users.

- **Introductory message**: Replaces the control's default introductory message of **Copilot can answer questions about the data in this app, and help you navigate. It's always learning from your feedback**. The current description of the Copilot control can be enhanced to provide a more specific explanation of how it benefits app users.

- **Data summary**: Helps Copilot control give better responses to questions from app users. We recommend a brief 2-3 lines that describe what the app is and which types questions the Copilot control will answer. This property doesn't impact the control's UI.

- **Placeholder text**: Replaces the control's default placeholder text in the text input box **Ask a question about the data in this app, or tell me what you're looking for**. We recommend that you provide a concise message to app users, explaining what types of questions the Copilot control can address.

   > [!div class="mx-imgBorder"]
   > ![Configure the control.](media/copilot/updated-copilot-properties.png)


## Provide feedback

App users and makers can provide feedback by selecting **Like** (thumbs up) or **Dislike** (thumbs down) button for each response that Copilot provides. Optionally, app users can also enter additional feedback in the text box and then select **Submit**.

### Disable feedback for app users

Admins can disable the option for apps users to provide feedback to Microsoft from the Copilot chat experience.

1. Sign in to [Power Apps](https://make.powerapps.com).
2. On the [left navigation pane](intro-maker-portal.md#1--left-navigation-pane), select **Tables** > **Organization**.
3. In the **Organization columns and data** section, select the list of columns and search for **Allow users to provide feedback for App Copilot**.
4. Set the toggle to **No**.


## See also

[Build apps through conversation (preview)](ai-conversations-create-app.md)

[Add Chatbot control to a canvas app (preview)](add-ai-chatbot.md)

[Leverage Azure OpenAI Service in AI Builder (preview)](/ai-builder/prebuilt-azure-openai) 




[!INCLUDE[footer-include](../../includes/footer-banner.md)]
