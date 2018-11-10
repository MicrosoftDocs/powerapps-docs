---
title: Build your first model-driven app from scratch with PowerApps | Microsoft Docs
description: Learn how to build a simple model-driven app
documentationcenter: ''
author: Mattp123
manager: kvivek
editor: ''
tags: ''
ms.service: powerapps
ms.devlang: na
ms.topic: conceptual
ms.component: model
ms.date: 10/15/2018
ms.author: matp
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---

# Build your first model-driven app from scratch
Model-driven app design is a component-focused approach to app development. In this topic, you simplify how to create a model-driven app by using one of the standard entities that's available in your PowerApps environment.

> [!TIP]
> To learn all about building model-driven apps, start here: [Understand model-driven app components](model-driven-app-components.md). 

## Sign in to PowerApps
Sign in to [PowerApps](https://web.powerapps.com/). If you don’t already have a [!INCLUDE [powerapps](../../includes/powerapps.md)] account, select the **Get started free** link. 

## Create your model-driven app

1.	Select the environment you want, or go to the [PowerApps admin center](https://admin.powerapps.com/) to create a new one.

  > [!IMPORTANT]
  > If the **Model-driven** design mode isn't available, you may need to [Create an environment](https://docs.microsoft.com/powerapps/administrator/create-environment).   

2. On the **Home** page, select the **Start from blank** option for a model-driven app.
![Start-from-blank_model](media/build-first-model-driven-app/start-from-blank-model-driven.png)

3.	On the **Create a New App** page, enter the following details, and then select **Done**: 
  - **Name**: Enter a name for the app, such as *Myfirstapp*. 
  - **Description**: Type a short description of what the app is or does, such as *This is my first app*.
For information about the additional app properties, see [Create an app](https://docs.microsoft.com/dynamics365/customer-engagement/customize/create-edit-app#create-an-app).
 
    ![Create-new-app](media/build-first-model-driven-app/create-new-app.png)

## Add components to your app
From the app designer you add components to your app.
1.	Select the **Open the Site Map Designer** arrow to open the sitemap designer. 

    ![Create-new-sitemap](media/build-first-model-driven-app/new-sitemap.png)

2.	On the sitemap designer select **New Subarea**, in the right pane select the **Properties** tab, and then select the following properties.
  - **Type**: Entity
  - **Entity**: Account

    ![Add components to sitemap](media/build-first-model-driven-app/sitemap.png)

3.	Select **Save And Close**.
4.	On the app designer canvas select **Forms**, and then on the right pane under the **Main Forms** group select the **Account** form.

    ![Account main form](media/build-first-model-driven-app/main-form.png)

5.	On the app designer canvas select **Views**, and then select the **Active Accounts**, **All Accounts**, and **My Active Accounts** views.

    ![Account views](media/build-first-model-driven-app/views.png)

6. On the app designer canvas select **Charts**, and then select the **Accounts by Industry** chart.
7. On the app designer toolbar, select **Save**.

    ![App designer toolbar save](media/build-first-model-driven-app/app-designer-toolbar.png)
 
<!-- ##  Validate your app
This step checks for component dependencies that are required for the app to work, but haven't yet been added to the app. 

1. On the app designer canvas, select the component that indicates a dependency, such as the **Forms** component. Then, on the right-pane select the **Required** tab, expand **Entity Dependencies** and then select all required dependencies. 

    ![Add dependencies](media/build-first-model-driven-app/resolve-dependencies.png)

2. Select **Add Dependencies**.
3. On the app designer toolbar, select **Save**.  -->

## Publish your app
On the app designer toolbar, select **Publish**.

After publishing the app it's ready for you to run or share with others.

![Simple account entity app](media/build-first-model-driven-app/accounts-quickstart-app.png)

## Next steps
In this topic, you built a simple model-driven app. 
- To see how your app looks when you run it, see [Run a model-driven app on a mobile device](../../user/run-app-client-model-driven.md).
- To learn how to share your app, see [Share a model-driven app](share-model-driven-app.md).
- To get started and learn all about building model-driven apps, see [Understand model-driven app components](model-driven-app-components.md)
