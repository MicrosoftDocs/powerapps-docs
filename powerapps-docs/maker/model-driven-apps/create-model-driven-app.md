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
ms.subservice: mda-maker
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

Verify the availability of the following prerequisites before you start to create a model-driven app:

- A Power Platform environment used for app development.
- An environment maker, system administrator or system customizer use role.

For more information review the following articles:

- [Create an environment](/power-platform/admin/create-environment).
- [Environment strategy for ALM](/power-platform/alm/environment-strategy-alm).
- [About predefined security roles](share-model-driven-app.md#about-predefined-security-roles).

## Create an app

1. On the [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) **Home** page, select **Solutions** from the left navigation pane.

1. Open an unmanaged solution or [create a new solution](../data-platform/create-solution.md)
   > [!NOTE]   
   > Unmanaged solutions can be recognised by the open lock in the **Managed Externally?** column.
   > :::image type="content" source="media/unmanaged-solutions.png" alt-text="Select the navigation area from the Navigation pane":::
   > Although the **Default Solution** is an unmanaged solution it is in most circumstances not recommmended to edit the default solution.
1. Select **New** > **App** > **Model-driven app**.
1. On the **New model-driven app from blank** dialog box, select **Modern app designer**, and then select **Create**. :::image type="content" source="media/new-model-driven-app-from-blank.png" alt-text="New model-driven app from blank":::
1. On the **New model-driven app** dialog box, enter a **Name** and optionally, a **Description**, and then select **Create**.
1. On the left navigation pane, select **Navigation** to display the navigation tree. 

   :::image type="content" source="media/navigation-area.png" alt-text="Select the navigation area from the Navigation pane":::
   > [!TIP]
   > Use the menu toggle to show or hide the names of the menu options. :::image type="content" source="media/menu-toggle.png" alt-text="Toggle the menu to show or hide the name of the menu options":::
1. Notice that a basic navigation structure is already created for you. Expand **Area1**, and then expand **Group1**.
   :::image type="content" source="media/default-site-map.png" alt-text="Default site map is created for you":::
1. Select **Group1** and change the title in the property pane to for example *Accounts and Contacts*. :::image type="content" source="media/edit-navigation-group-title.png" alt-text="edit the group's title in the property pane":::
1. Select **Subarea1**, and make for example the following changes:

   - **Content type**: Table
   - **Table**: Account
   - **Title**: Accounts

   > [!NOTE]
   >
   > - A subarea won't appear in the app preview until you add a content type to it.
   > - By default, all forms and views are included for a table that's added to a page. To remove one or more components, see [Create, add, and remove forms, views, or dashboards](#create-add-and-remove-forms-views-or-dashboards).

1. On the command bar, select **New page**, select **Table based view and form**, and then select **Next**.
1. On the **New table view and form pages** dialog box, select **Contact**, leave the **Show in navigation** option selected, and then select **Add**. Note the following: 
   - Notice the preview pane displays your app. Selecting a component, such as a table, affects what's displayed in the preview. If your environment includes data that you have access to view, that also appears in the preview.
   :::image type="content" source="media/create-app.png" alt-text="App created with account and contact tables.":::
1. Select **Save**, and then select **Publish**.

To see how the app runs in a full browser window, on the command bar, select **Play**.




### Next Steps

- [Create, add and remove forms, views or dashboards](create-add-remove-forms-views-dashboards.md)
- [Create and remove pages](create-remove-pages.md)
- [App navigation](app-navigation.md)
  
### See Also

- [Overview of the model-driven app designer](app-designer-overview.md)
- [Configure app properties (Preview)](manage-app-properties-preview.md)
- [Configure app properties](manage-app-properties.md)
