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

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

In this article you learn the basics of how to create a model-driven app that can be shared and distributed to other environments.

## Prerequisites
Verify the following prerequisites before you start creating an app: 

- A Power Apps environment used for app development. More information [Create an environment](/power-platform/admin/create-environment) and [Environment strategy for ALM](/power-platform/alm/environment-strategy-alm).
- Environment maker, system administrator, or system customizer role. More information: [About predefined security roles](share-model-driven-app.md#about-predefined-security-roles)

## Create an app

1. On the [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) **Home** page, select **Solutions** from the left navigation pane.

1. Open an unmanaged solution or create a new one. More information: [Create a solution](../data-platform/create-solution.md) 

1. Select **New** > **App** > **Model-driven app**.
1. On the **New model-driven app from blank** dialog box, select **Modern app designer**, and then select **Create**.
1. On the **New model-driven app** dialog box, enter a **Name** and optionally, a **Description**, and then select **Create**.
1. On the left navigation pane, select **Navigation** to display the navigation tree. 
   :::image type="content" source="media/navigation-area.png" alt-text="Select the navigation area from the Navigation pane.":::

1. Notice that a basic site map is already created for you. Expand **Area1**, and then expand **Group1**.
   :::image type="content" source="media/default-site-map.png" alt-text="Default site map is created for you.":::
1. Select **Group1** and change the title to *Accounts and Contacts*.
1. Select **Subarea1**, and make the following changes: 
   - **Content type**: Table
   - **Table**: Account
   - **Title**: Accounts

   > [!NOTE]
   > - A subarea won't appear in the app preview until you add a content type to it.
   > - By default, all forms and views are included for a table that's added to a page. To remove one or more components, see [Create, add, and remove forms, views, or dashboards](#create-add-and-remove-forms-views-or-dashboards).

1. On the command bar, select **New page**, select **Table based view and form**, and then select **Next**.
1. On the **New table view and form pages** dialog box, select **Contact**, leave the **Show in navigation** option selected, and then select **Add**. Note the following: 
   - Notice the preview pane displays your app. Selecting a component, such as a table, affects what's displayed in the preview. If your environment includes data that you have access to view, that also appears in the preview.
   :::image type="content" source="media/create-app.png" alt-text="App created with account and contact tables.":::
1. Select **Save**, and then select **Publish**.

To see how the app runs in a full browser window, on the command bar, select **Play**.

## App navigation

By default, a new model-driven app's navigation (or sitemap) is created that includes one area named **Area1**, one group named **Group1**, and one subarea named **Subarea1**. You can change the default area, group, and subarea names to something that is more meaningful to your users or configure a different site map. 

In a model-driven app, there are the three main app runtime navigation components.

1. Areas. For apps with more than one area, a switch control is displayed in the lower left navigation pane. In the screenshot below, the current area is named *Accounts*.
1. Groups. Group names appear as a navigation element in an app with the subarea names within the group listed beneath it. In the screenshot below, one group is named *Accounts* and one is named *New Group*.
1. Subareas. Subareas and pages appear under the group that they're configured within in the app designer. In the screenshot below, one subarea is named *All accounts revenue* and another subarea is named *Contacts*.

   :::image type="content" source="media/default-sitemap.png" alt-text="Default model-driven app site map.":::

### Create a group or subarea

1. On the left navigation pane, select **Navigation**.
1. Select **Add**, and then select **Group** or **Subarea**.
1. Complete the properties pane for the group or subarea.
   - For groups:
      - **Title**: Enter a title used to describe the group.
      - **ID**: The system generates an identifier for the group. Except the system generated ID or enter a new one.
   - For subareas:
      - **Content type**: Select either **Table** or **Dashboard**.
      - **Table** or **Dashboard**: Depending on the content type you selected, select a table or dashboard from the list.
      - **Title**: Leave the default title or enter a title used to describe the subarea.
1. To save your app navigation changes select **Save**.
1. To publish the changes to make them available to users, select **Publish**.

### Remove a group or subarea

1. On the left navigation pane, select **Navigation**.
1. Select the group or subarea you want, select **...**, and then select **Remove**.

## Create and remove pages

App designer pages are containers for one or more tables or dashboards. You can choose whether to have the page appear in the app navigation (site map) or not.

To create a page, select **New page**, select the page type of either **Table based view and form** or **Dashboard**, and then select **Next**. If you don't want your page to appear in the app's site map, clear **Show in navigation**. Select the components you want and then select **Add**. 

To remove a page, select a page, select **...**, and then select **Remove**.

To remove a component from a page, expand a page, select the component, such as a form, view, or dashboard, select **...**, and then select **Remove**.

## Create, add, and remove forms, views, or dashboards

Create, add, or remove one or more forms or views for a table.

1. On the left navigation pane select **Pages**, and then select the component you want, such as **Account form**. 
1. On the right properties pane, select **Manage forms**.
1. On the **Manage forms** flyout, select the forms you want to add or remove, and then select **Save**. Alternatively, select **New form** to open the form designer to create a new form.
   :::image type="content" source="media/app-design-manage-forms.png" alt-text="Manage forms interface.":::

1. Select **Publish** to make the changes available to users.

## Configure app properties

From the **Settings** dialog box you can make app-level changes such as app name and description.

1. On the command bar select **Settings**.
1. On the **General** tab, select from the following options: 
   - **Name**: The name of the app.
   - **Description**: A description of the app is optional.
   <!-- - **Can be used offline**: Allows users to run the app and interact with data without an internet connection. More information: [Configure mobile offline synchronization for Power Apps mobile](../../mobile/setup-mobile-offline.md) -->

### See also

[Overview of the model-driven app designer](app-designer-overview.md)