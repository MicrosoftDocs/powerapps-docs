---
title: Add a Copilot control for canvas app users
description: Add Copilot AI control for apps users to your canvas app.
author: mduelae
ms.topic: conceptual
ms.custom: canvas
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
---

# Add a Copilot Control to a canvas app (preview)

[This article is prerelease documentation and is subject to change.]

The Copilot control is a next-generation AI assistant that can be integrated in your canvas app. It enables end users to use a chat experience that is powered by AI. This feature allows app users to obtain insights about the data in their apps through natural language conversations. Makers can add the control to any canvas app and choose what data it can provide answers for.

> [!IMPORTANT]
> - To see if this feature is available in your region, see the [Product availability report](https://releaseplans.microsoft.com/en-US/availability-reports/?report=copilotfeaturereport).
> - You need to allow data movement across regions for generative AI features as a prerequisite to use copilots in Power Apps. This step is important if your organization and your environment are in different regions. More information: [Enable copilots and generative AI features](/power-platform/admin/geographical-availability-copilot#enable-data-movement-across-regions).
> - Preview features aren’t meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.
> - For more information, go to our [preview terms](https://go.microsoft.com/fwlink/?linkid=2189520).
> - This capability is powered by [Azure OpenAI Service](/azure/cognitive-services/openai/overview).
> - This capability  may be subject to usage limits or capacity throttling.
> - Copilot control isn't supported and won't work for environments that have customer-managed key (CMK) or have lockbox.
> - Your environment must be in the United States region.
> - Your account must have English (United States) as the browser language.

## Step 1 - Enable Copilot for your environment

Before end users can use the Copilot chat experience in a canvas app, an administrator must first turn on, **Allow users to analyze data using an AI-powered chat experience in canvas and model-driven apps (preview)** feature in their [environment](https://admin.powerplatform.microsoft.com). For more information, see [Manage feature settings](/power-platform/admin/settings-features#copilot-preview).

> [!div class="mx-imgBorder"]
> ![Set Copilot feature ON for the envrironment](media/copilot/Copilot_for_apps_users_ON.png)

When the feature setting is turned on, a maker can go to the app settings in Power Apps Studio and turn on, **Copilot component**. Then add the Copilot control to a canvas app and allow end users use the AI-powered chat experience.

## Step 2 - Enable Copilot component for a canvas app 

Open your [canvas app open for editing](edit-app.md) in Power Apps Studio:

1. On the command bar, select **Settings** > **Upcoming features**.
2. From the **Preview** tab, set the toggle for **Copilot component** to **On**.
  
   > [!div class="mx-imgBorder"]
   > ![Turn on Copilot control.](media/copilot/copilot-1.png)

   
> [!IMPORTANT]
>  Your browser language must be set to **English (United States)**.

## Step 3 - Add Copilot control to your canvas app

Add the **Copilot (preview)** control to your canvas app to let end users gain insights about the data in their apps through the chat experience.

With your [canvas app open for editing](edit-app.md) in Power Apps Studio:

- On the app authoring menu, select **Insert** and select **Copilot (preview)** to add this control.

   > [!div class="mx-imgBorder"]
   > ![Add the copilot control.](media/copilot/Copilot-Insert-menu.png)

## Connect to a custom copilot  

You can customize the **Copilot (preview)** control and use [Copilot Studio](/microsoft-copilot-studio/fundamentals-get-started) to add capabilities such as more topics, plugin actions, and other capabilities.

### Turn on Edit in Copilot Studio 

To connect the **Copilot (preview)** control to a Copilot Studio Copilot, you must enable the **Edit in Copilot Studio** feature from the app settings in Power Apps Studio.

1. On the command bar, select **Settings** > **Upcoming features**.
2. From the **Preview** tab, set the toggle for **Edit in Copilot Studio** to **On**.

   > [!div class="mx-imgBorder"]
   > ![Turn on Edit in Copilot Studio.](media/copilot/edit-in-copilot-studio-setting.png)

### Create a new copilot  

1. On the app authoring menu, select **Insert** > **Copilot (preview)**.
2. On the properties pane, select **Edit** next to the **Customize copilot** property and then select **Create new copilot** to create a new copilot using Microsoft Copilot Studio. You can also set this value to an existing copilot in the **Advanced** properties tab.
  
   > [!div class="mx-imgBorder"]
   > ![Create a new copilot.](media/copilot/customize-copilot.png)

### Edit and customize in Copilot Studio

To create a new copilot that you can edit in Copilot Studio, select **Edit** next to the **Customize copilot** property and then select **Edit in Copilot Studio**. For more information see, [Microsoft Copilot Studio quickstart](/microsoft-copilot-studio/fundamentals-get-started).
  
   > [!div class="mx-imgBorder"]
   > ![Edit and customize in Copilot Studio.](media/copilot/edit-in-copilot-studio.png)


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

[Add Copilot for app users in model-driven apps (preview)](../model-driven-apps/add-ai-copilot.md)

[Enable copilots and generative AI features in Power Apps](/power-platform/admin/geographical-availability-copilot#enable-data-movement-across-regions)




[!INCLUDE[footer-include](../../includes/footer-banner.md)]
