---
title: "Create a model-driven app using the designer | MicrosoftDocs"
description: Learn how to create a model-driven app.
ms.custom: ""
ms.date: 01/27/2025
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: get-started
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "PowerApps"
author: "Mattp123"
ms.subservice: mda-maker
ms.author: "emcoope"
ms.reviewer: "matp"
search.audienceType: 
ms.collection: bap-ai-copilot
  - maker
contributors:
  - asheehi1
---
# Create a model-driven app with the app designer

In this article, you learn the basics of how to create a model-driven app that can be shared and distributed to other environments.

## Prerequisites

Verify the availability of the following prerequisites before you start to create a model-driven app:

- A Power Platform environment used for app development.
- An environment maker, system administrator, or system customizer security role.

For more information, go to the following articles:

- [Create an environment](/power-platform/admin/create-environment)
- [Environment strategy for ALM](/power-platform/alm/environment-strategy-alm)
- [About predefined security roles](share-model-driven-app.md#about-predefined-security-roles)

## Create an app

1. On the [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) **Home** page, select **Solutions** from the left navigation pane. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]

1. Open an unmanaged solution or [create a new solution](../data-platform/create-solution.md).
   > [!NOTE]
   > Unmanaged solutions can be identified when the solution has a **No** in the **Managed** column.
   > 
   > Although the **Default Solution** is an unmanaged solution, it is in most circumstances not recommended to create or edit customizations in the default solution.

1. Select **New** > **App** > **Model-driven app**.
1. On the **New model-driven app** dialog box, enter a **Name** and optionally, a **Description**, and then select **Create**.
1. On the command bar select **Add page**, and then on the **New page** screen, select **Dataverse table**, and then select **Next**.
1. From the list of tables, select **Account**, select **Contact**, and then select **Add**.

On the **Pages** left pane, under **Navigation** the layout for the app is displayed.

   :::image type="content" source="media/navigation-area.png" alt-text="Select the navigation area from the navigation pane":::

Notice the preview pane displays your app. When you select a component, such as the **Accounts form**, it affects what's displayed in the preview and property panes. If your environment includes data that you have access to view, that also appears in the preview.
:::image type="content" source="media/create-app.png" alt-text="App created with account and contact tables." lightbox="media/create-app.png":::

To save and publish the app, select **Save**, and then select **Publish**.

To see how the app runs in a full browser window, on the command bar, select **Play**.

## Create an app description with Copilot

If your app is in a [managed environment](/power-platform/admin/managed-environment-overview), you can use AI to help create a description for your app.

> [!IMPORTANT]
>
> - To use this capability your app must be in a [managed environment](/power-platform/admin/managed-environment-overview).
> - This capability is powered by [ Azure OpenAI Service](/azure/cognitive-services/openai/overview).
> - This capability is in process of rolling out, and might not be available in your region yet.
> - This capability might be subject to usage limits or capacity throttling.
> - To understand capabilities and limitations of AI-powered and Copilot features in Power Apps, go to [Responsible AI FAQs for Power Apps](../common/responsible-ai-overview.md)

When you save and publish your app, on the **Publish** dialog box select **Create descriptions using AI** to replace your current description or, if your app doesn't have a description, Copilot generates one for you.

You can also generate an app description in app designer by going to, **Settings** > **General** tab. Under **Description** select, **Create descriptions using AI**.

For information that describes the AI impact of Power Apps generate app descriptions with Copilot feature, go to [FAQ for generate app descriptions with Copilot](../common/ai-app-descriptions-faq.md).

### Enable or disable AI-generated app descriptions

The app AI-generated descriptions are managed by a setting in the Power Platform admin center.

1. Go to https://admin.powerplatform.microsoft.com/environments.
1. Select an environment, and then select **Edit managed environments**.
1. Under the section titled **Enable AI-generated app descriptions**, select or clear **AI-generated app descriptions**
1. Select **Save**.

Clear the browser cache and close any active Power Apps (make.powerapps.com) browser windows. The feature is now be enabled or disabled.

## Next steps

- [Add areas, groups, and subareas for app navigation](app-navigation.md)
- [Create, add and remove forms, views or dashboards](create-add-remove-forms-views-dashboards.md)
- [Create and remove pages](create-remove-pages.md)
- [Configure app properties (Preview)](app-properties.md)
- [Configure app properties](manage-app-properties.md)
