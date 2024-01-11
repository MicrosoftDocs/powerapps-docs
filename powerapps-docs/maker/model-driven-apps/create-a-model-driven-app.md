---
title: "Create a model-driven app using the account page"
description: "Learn how to create a model-driven app that has the account table added to it."
ms.date: 10/26/2023
ms.subservice: mda-maker
ms.topic: tutorial
author: joel-lindstrom
ms.author: matp
ms.reviewer: matp
---
# Create a model-driven app that has an account table page

Model-driven app design is a component-focused approach to app development. Model-driven apps are especially well suited for process driven apps that are data dense and make it easy for users to move between related records. For example, if you are building an app to manage a complex process, such as onboarding new employees, managing a sales process, or member relationships in an organization like a bank, a model-driven app is a great choice. Model-driven apps also allow you to quickly build an app by combining components like forms, views, charts, and dashboards.

In this tutorial, you create a model-driven app by using one of the standard tables that is available in Microsoft Dataverse, the account table.

## Sign in to Power Apps

Sign in to [Power Apps](https://make.powerapps.com/). If you don't already have a Power Apps account, select the **Get started free** link.

## Select the environment

An environment in Power Apps is a space to store, manage, and share your organization’s business data, apps, chatbots, and flows. It also serves as a container to separate apps that might have different roles, security requirements, or target audiences.

Each environment can have one Dataverse database.

Select the environment you want, or go to the [Power Platform admin center](https://admin.powerplatform.microsoft.com/) to create a new one. You can choose the environment by selecting **Environment** from the upper right.

## Create your model-driven app

We recommend creating your model-driven app from a solution. A solution is a package that can contain Dataverse tables, forms, views, apps, flows, and other components. By building your model driven-app in a solution, you can easily move it to other environments or preserve a copy in your source control repository.

1. Select **Solutions** on the left navigation pane. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
1. Select **New solution**. More information: [Create a solution](/powerapps/maker/data-platform/create-solution).

1. Enter a **Display name** for your solution, such as **Power Apps Training**. Next, you add the account table that will be included in your model-driven app.

1. In your solution, select **Add existing**, and then select **Table.**

1. Under **Add existing tables** screen, select the **Account** table, and then select **Next**.

1. Select **Include all components**, and then select **Add.**

   Now that you have a solution and have added the account table to it, you're ready to create a model-driven app.

1. In your solution, select **New**, select **App**, and then select **Model-driven app.**

1. Enter a name for the app, such as *My new custom app2*, and then select **Create**.

   :::image type="content" source="media/create-a-model-driven-app/create-your-model-driven-app-2.png" alt-text="Enter a name and then select Create.":::

## Add pages to your app

Next, you add a new page to the model-driven app. 
1. Select **New page** from the **Pages** menu.

   :::image type="content" source="media/create-a-model-driven-app/add-pages-to-an-app-1.png" alt-text="Add a page to a model-driven app.":::

1. Select **Table based view and form**, and then select **Next**.

   :::image type="content" source="media/create-a-model-driven-app/add-pages-to-an-app-2.png" alt-text="Select a table-based view and form.":::

1. Select table such as **Contact**, and then select **Add**.

   :::image type="content" source="media/create-a-model-driven-app/add-pages-to-an-app-3.png" alt-text="Select the account table to add it to the app.":::

   The contact form and view appear in the pages menu.

1. Select **Contact views** to display the table views and charts right pane:
   - To remove a view, under **In this app** next to the view your want to remove select **...** > **Remove**. 
   - To add a view, under **Not in this app** next to the view you want to add select **...** > **+ Add**.
   - To edit a view, next to the view select **...** > **Edit** or **Edit in new tab**.

   :::image type="content" source="media/create-a-model-driven-app/add-pages-to-an-app-5.png" alt-text="Select the views to add in the app.":::

1. On the app designer command bar, select **Save**.

## Publish your app

On the app designer command bar, select **Publish**.

After publishing the app, it's ready for you to run or share with others.

### Create an app description with Copilot (preview)

[This section is prerelease documentation and is subject to change.]

> [!IMPORTANT]
> - To use this capability your app must be in a [managed  environment](/power-platform/admin/managed-environment-overview).
> - Preview features aren’t meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.
> - For more information, go to our [preview terms](https://go.microsoft.com/fwlink/?linkid=2189520).
> - This capability is powered by [ Azure OpenAI Service](/azure/cognitive-services/openai/overview).
> - This capability is in process of rolling out, and may not be available in your region yet.
> - This capability  may be subject to usage limits or capacity throttling.
> - To understand capabilities and limitations of AI-powered and Copilot features in Power Apps, see [Responsible AI FAQs for Power Apps](../common/responsible-ai-overview.md)

If your app is in a [managed  environment](/power-platform/admin/managed-environment-overview), you can use AI to help you create a description for your app.

When you save and publish your app, on the **Publish** dialog box select, **Create descriptions using AI** if you want to replace your current description or, if you do not have a description, Copilot will generate one for you.

You can also generate an app description by going to, **Settings** > **General**. Under **Description** select, **Create descriptions using AI**.

## Run your app on a desktop computer

1. To run your app, sign in to [Power Apps](https://make.powerapps.com/), and  on the left navigation pane, select **Apps**.

   :::image type="content" source="media/create-a-model-driven-app/run-your-app-on-desktop-1.png" alt-text="Select Apps.":::

1. Select the app from the app list. The app opens in your browser.

   ![Simple account table app.](media/create-a-model-driven-app/run-your-app-on-desktop-2.png "Simple account table app")

## Run your app on mobile

To run your app on your mobile device, follow these steps:

1. Download the app from your device's mobile app store:

   - IOS: [‎Power Apps on the App Store (apple.com)](https://apps.apple.com/us/app/power-apps/id1047318566)

   - Android: [Power Apps - Apps on Google Play](https://play.google.com/store/apps/details?id=com.microsoft.msapps&hl=en_US&gl=US)

1. Open the app, tap **Sign in**, and then enter your Microsoft work or school account.

1. Select your app from the list to run it.

### See also
[Overview of the model-driven app designer](app-designer-overview.md)
