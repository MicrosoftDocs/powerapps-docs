---
title: "Create a model-driven app using the designer | MicrosoftDocs"
description: Learn how to create a model-driven app.
ms.custom: ""
ms.date: 04/30/2021
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "get-started-article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "PowerApps"
author: "Mattp123"
ms.author: "emcoope"
ms.reviewer: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - "PowerApps"
  - D365CE
---
# Create a model-driven app with the app designer

In this article you learn the basics of how to create a model-driven app that can be shared and distributed to other environments.

## Prerequisites
Verify the following prerequisites before you start creating an app:

- A Power Apps environment used for app development. More information [Create an environment](/power-platform/admin/create-environment) and [Environment strategy for ALM](/power-platform/alm/environment-strategy-alm).
- Environment maker, system administrator, or system customizer role. More information: [About predefined security roles](share-model-driven-app.md#about-predefined-security-roles)

## Create an app
1. On the [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) **Home** page, select **Solutions** from the left navigation pane.

1. Open an unmanaged solution or create a new one. More information: [Create a solution](../data-platform/create-solution.md) 

1. Select **New** > **App** > **Model-driven app**.

1. On the **New model-driven app** dialog box, enter a **Name** and optionally, a **Description**, and then select **Create**.
1. On the left navigation pane, select **Navigation** to display the navigation tree. 
   :::image type="content" source="media/navigation-area.png" alt-text="Select the navigation area from the Navigation pane":::

1. Notice that a basic site map is already created for you. Expand **Area1**, and then expand **Group1**.
   :::image type="content" source="media/default-site-map.png" alt-text="Default site map is created for you":::
1. Select **Group1** and change the title to *Accounts and Contacts*.
1. Select **Subarea1**, and make the following changes: 
   - **Title**: Accounts
   - **Content type**: Table
   - **Table**: Account

   > [!NOTE]
   > A subarea won't appear in the app preview until you add a content type to it.

1. On the command bar, select **New page**, select **Table based view and form**, and then select **Next**.
1. On the **New table view and form pages** dialog box, select **Contact**, leave the **Show in navigation** option selected, and then select **Add**. Note the following: 
   - Notice the preview pane displays your app. Selecting a component, such as a table, affects what's displayed in the preview. If your environment includes data that you have access to view, that also appears in the preview.
   :::image type="content" source="media/create-app.png" alt-text="App created with account and contact tables":::
1. Select **Save**, and then select **Publish**.

To see how the app runs in a full browser window, on the command bar, select **Preview**.

## Add, remove, and edit app components

By default, all forms, views, and dashboards are included for a table in the app. To remove one or more forms, views, and dashboards, in the left navigation pane select **Pages**, select the component you want, such as **Account form**. On the right properties pane, select **Manage forms** to add or remove one or more forms.

### See also
[Overview of the model-driven app designer](app-designer-overview.md)