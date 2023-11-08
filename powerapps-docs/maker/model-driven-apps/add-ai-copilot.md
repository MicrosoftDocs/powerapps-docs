---
title: Copilot in model-driven apps | MicrosoftDocs
description: Learn how Copilot in a model-driven apps can assist app users.
author: Mattp123
ms.service: powerapps
ms.subservice: mda-maker
ms.author: mijosh
ms.reviewer: matp
ms.date: 08/10/2023
ms.topic: how-to
applies_to: 
  - "powerapps"
search.audienceType: 
  - maker
---
# Add Copilot for app users to model-driven apps (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

Copilot for model-driven apps in Power Apps is a next-generation AI assistant for app users to get insights about the data in their apps through conversation in natural language. Copilot helps app users boost their productivity through AI-powered insights and intuitive app navigation.

> [!IMPORTANT]
>
> - This is a preview feature.
> - To use this capability your environment must be in the US region.
> - Preview features aren’t meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.
> - For more information, go to our [preview terms](https://go.microsoft.com/fwlink/?linkid=2189520).
> - This capability is powered by [Azure OpenAI Service](/azure/cognitive-services/openai/overview).
> - This capability  may be subject to usage limits or capacity throttling.

When enabled, Copilot can be accessed through the Copilot icon in the right navigation bar in a model-driven app. The Copilot pane can be opened or minimized as desired. Copilot in model-driven apps answers questions about the configured Microsoft Dataverse table data in the app. Copilot can also help you navigate the app. For example, when a user enters *take me to Online Cases* or *show me Cruise Support Tickets*.

:::image type="content" source="media/model-driven-app-copilot.png" alt-text="Copilot right pane in a model-driven app" lightbox="media/model-driven-app-copilot.png":::

## Enable Copilot for model-driven apps feature for your environment
Environment administrators can enable Copilot feature in model-driven apps for all the users in their environments in [Power Platform admin center](https://admin.powerplatform.microsoft.com).

1. Sign in to the Power Platform admin center at https://admin.powerplatform.microsoft.com.

2. In the navigation pane, go to **Environments** and select the enviornment where you want to enable Copilot for app users in model-driven apps in. Click on **Settings** for this environment in the top menu.

  > [!div class="mx-imgBorder"]
  > ![Select environment Settings.](media/Environment_settings.png)
 
3. In **Settings** for the seleceted environment, navigate to **Product** section and select **Features** option.

  > [!div class="mx-imgBorder"]
  > ![Select Copilot feature for the environment.](media/Environment_features.png)

4. In **Features** section, set the value for **Allow users to analyze data using an AI-powered chat experience in canvas and model-driven apps** to **On** in the dropdown control.
   
  > [!div class="mx-imgBorder"]
  > ![Set Copilot feature ON for the envrironment](media/Copilot_for_apps_users_ON.png)

 
## Set your environment to receive monthly updates for model-driven apps
Makers must set their environment to receive monthly model-driven apps updates as a prerequisite for having Copilot for end users in model-driven apps.
1. Sign in to the Power Platform admin center at https://admin.powerplatform.microsoft.com.
2. In the navigation pane, go to **Environments** and select the enviornment where you want to enable Copilot for app users in model-driven apps in. Click on **Settings** for this environment in the top menu.
3.  Go to **Product** section and select **Behavior** option.  Set **Release channel** for model-driven apps to **Monthly channel** in the dropdown control.
   
  > [!div class="mx-imgBorder"]
  > ![Set Release channel to Monthly channel for model driven apps](media/Behavior_release_channel.png)

 More information: [Behavior settings](/power-platform/admin/settings-behavior#settings) and [Changing release channels for model-driven apps](channel-change.md).
 
## Configure Dataverse tables and columns for Copilot 
   
Environment administators must configure the Dataverse tables Copilot will using for the responses. You must choose both the tables and the columns of importance for Copilot to search accross to produce relevant, high quality data inisghts.

More information: [Configure tables to use Copilot](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/table-settings-for-copilot).

For every Dataverse table to be used by Copilot, do these 2 Steps in **Tables** pane at [Power Apps](https://make.powerapps.com/) to configure your tables and columns for Copilot use:

* Select a Dataverse table and go to its **Properties > Advanced options** option in the top menu. Enable **Track Changes** and **Appear in search results** settings for the table and **Save**. More information: [Enable table indexing](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/table-settings-for-copilot#enable-indexing).
 

* Open this table and select **Views** option from **Data experiences** section. Then, select and open **Quick Find [table name]** view in from the list. Click on **Edit find table columns** option at the bottom of the right hand pane. Select the columns of importance and click **Apply** to add them to the list. 

  > [!div class="mx-imgBorder"]
  > ![Add table colummns to quick find view](media/Index_columns.png)

Next, **Save and publish** your table changes. More information: [Enable column indexing](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/table-settings-for-copilot#configure-columns).

  > [!NOTE]
  > Questions and answers for enterprise data environments that have [customer managed key](/power-platform/admin/customer-managed-key) or [Customer Lockbox](/power-platform/admin/about-lockbox) won't use your data stored in Dataverse. You might get answers from Copilot, but they won't be based on your Dataverse database.

## Provide feedback in Copilot

To provide feedback to help improve Copilot, app users can select the thumbs up or thumbs down icons included in each Copilot response. Feedback can be submitted for each Copilot response in the pane.

### Provide positive feedback

1. On the right navigation bar, select the “thumbs up” icon.
1. Optionally, provide feedback in your own words about what you liked.
1. Select **Submit** after you're done entering your feedback.

### Provide feedback for improvement

1. On the right navigation bar, select the “thumbs down” icon.
1. Optionally, provide feedback, such as feedback about the content of Copilot’s response, or a description in your own words about what went wrong, or how you would like Copilot to improve.
1. Select **Submit** after you're done entering your feedback.

## Disable feedback

If you want to disable the ability for users to submit feedback about Copilot in model-driven apps, follow these steps.

1. Sign in to [Power Apps](https://make.powerapps.com/).
1. Go to **Tables**, and then open the **Organization** table.
1. In the **Organization columns and data** section, select **+nnn more** to display the column search box.
1. In the search box search for the *Allow users to provide feedback for App Copilot* column.
   :::image type="content" source="media/disable-mda-copilot-feedback1.png" alt-text="Find the Allow users to provide feedback for App Copilot column":::

1. Set the column to **No**, and then **Save** the table.
   :::image type="content" source="media/disable-mda-copilot-feedback2.png" alt-text="Set the Find the Allow users to provide feedback for App Copilot column to No":::

## See also

[FAQ for Copilot in model-driven apps](../common/faqs-copilot-model-driven-app.md) <br />
[Responsible AI FAQs for Power Apps](../common/responsible-ai-overview.md) <br />
[Add Copilot control to a canvas app (preview)](../canvas-apps/add-ai-copilot.md)
