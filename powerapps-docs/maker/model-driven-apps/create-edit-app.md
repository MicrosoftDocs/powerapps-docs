---
title: "Create or edit a model-driven app using the app designer in Power Apps | MicrosoftDocs"
description: "Learn how to create or edit apps using the app designer"
keywords: ""
ms.date: 03/05/2020
ms.service: powerapps
ms.custom: 
ms.topic: get-started-article
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
author: "Mattp123"
ms.assetid: 2a44229e-44f0-4c4e-ba21-a476210d0a12
ms.subservice: mda-maker
ms.author: "matp"
manager: "kvivek"
ms.reviewer: 
ms.suite: 
ms.tgt_pltfrm: 
caps.latest.revision: 19
topic-status: Drafting
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---

# Create a model-driven app using the app designer

This topic describes the basics of creating and editing a model-driven app that can be shared and distributed to other environments.

## Prerequisites to creating model-driven apps

Verify the following prerequisites before creating an app:
- A Power Apps [environment](model-driven-app-glossary.md#environment) used for app development must exist within the tenant. More information [Create an environment](/power-platform/admin/create-environment) and [Environment strategy for ALM](/power-platform/alm/environment-strategy-alm).
- The environment used will need to have a Dataverse database associated with it.  Dataverse environments can exist with or without a database and generally these are provisioned on creation of the environment.  The database holds the tables and other components that will be used by the model-driven app. [Create and manage environments in Dataverse](https://docs.microsoft.com/learn/modules/create-manage-environments/)
- Dataverse [tables](model-driven-app-glossary.md#table) with forms, views will need to exist within the database.  These tables will most likely need to have [relationships](model-driven-app-glossary.md#relationship) configured for them.
- Within the environment the app developer needs to have an Environment maker, system administrator, or system customizer role. More information: [About predefined security roles](./share-model-driven-app.md#about-predefined-security-roles)

## Create a model-driven app  

1.  Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).  

1. Choose the environment by selecting the environment icon ![Environment icon.](media/icon-environment.PNG "Environment icon")
1. Select **Solutions** from the left navigation pane.

1. Open an unmanaged solution or create a new one. More information: [Create a solution](../data-platform/create-solution.md)
1. Select **New** > **App** > **Model-driven app**.  
1. There a two options.  [Modern app designer](app-designer-overview.md) and Classic App designer.  Select **Classic App Designer**.  
1. On the **Create a New App** page, enter the following details:

    - **Name**: Enter a name for the app.  
  
    - **Unique Name**: The unique name is automatically populated based on the app name that is specified. It is prefixed with a publisher prefix. It is possible to change the part of the unique name that's editable. The unique name can only contain English characters and numbers.  
  
        > [!NOTE]
        >  The publisher prefix is the text that's added to any table or column created for a solution that has this publisher.
  
    - **Description**: Type a short description of what the app is or does.  
  
    > [!div class="mx-imgBorder"]
    > ![Create a new app.](media/create-new-app.png "Create a new app")

     - **Icon**: By default, the **Use Default App** thumbnail check box is checked. To select a different web resource as an icon for the app, clear the check box, and then select an icon from the drop-down list. This icon will be displayed on the preview tile of the app.  
  
    - **Use existing solution to create the App (Optional)**: Select this option to create the app from a list of installed solutions. When this option is selected, **Done** switches to **Next** on the header. If **Next** is selected, the **Create app from existing solution** page opens. From the **Select Solution** drop-down list, select a solution. If any site map is available for the selected solution, the **Select Sitemap** drop-down list will appear. Select the site map, and then select **Done**.

      > [!NOTE]
      > By selecting **Default Solution** when the site map is added, the components that are associated with that site map are automatically added to the app.  

      > [!div class="mx-imgBorder"]
      > ![Use existing solution to create the app page.](media/use-existing-solution-to-create-the-app.png "Use an existing solution to create the app")

    - **Choose a welcome page (Optional)**: This option allows a designer to select from the web resources available in your organization. The welcome pages created can contain information that's useful to users, such as links to videos, upgrade instructions, or getting started information. The welcome page is displayed when an app is opened. Users can select **Do not show this Welcome Screen next time** on the welcome page to disable the page so it doesn't appear the next time the app starts. Notice that the **Do not show this Welcome Screen next time** option is a user-level setting and can't be controlled by administrators or app makers. More information about how to create a web resource, such as an HTML file that can be used as a welcome page: [Create and edit web resources to extend the web application](create-edit-web-resources.md)  

    To edit app properties later, go to the **Properties** tab in the app designer. More information: [Manage app properties](manage-app-properties.md)  
  
     > [!NOTE]
     >  It is not possible to change the unique name and app URL suffix on the **Properties** tab.  
  
2. Select **Done** or if **Use an existing solution to create the App** is selected select **Next** to select from the available solutions that were imported in the organization, then select **Done**.  
  
3.  A new app is created and is shown in **Draft** status. This is shown in the [App designer](model-driven-app-glossary.md#app-designer).

    :::image type="content" source="media/app-designer-draft.png" alt-text="App designer shown in draft stage":::

## Configure the site map

The site map describes the components that make up our model driven app.

1. Select the **Open the Site Map Designer** edit button (pencil icon) to open the sitemap designer.

      > [!div class="mx-imgBorder"]
      > ![Create-new-sitemap.](media/build-first-model-driven-app/new-sitemap.png "Create a site Map for the app")

    Notice that when an app is first created a site map must be configured for it.

1. On the sitemap designer, select **New Subarea**.

   :::image type="content" source="media/build-first-model-driven-app/new-subarea.png" alt-text="Select new subarea.":::

1. In the right pane, select the **Properties** tab, and then select the following properties.

- **Type**: **Entity**
  
- **Entity**: **Account**

    > [!div class="mx-imgBorder"] 
    > ![Add components to sitemap.](media/build-first-model-driven-app/sitemap.png "Properties tab for new subarea")

    When the **Title** property is left blank, the app uses the table name in the app's left navigation pane. For this app, **Accounts** will be displayed in the app at runtime.
4.  Select **Save And Close** to close the sitemap designer.

## Finalizing the app

   By default, all the account table's forms, views, charts, and dashboards are enabled for the app. From the app designer **Components** tab on the right pane, components can be cleared so that they aren't available in the app at runtime. It is also possible to create new components, such as a custom form. For this app, leave all components enabled.

  :::image type="content" source="media/app-designer-form-component-properties.png" alt-text="Model-driven App designer in draft stage":::

1. On the app designer toolbar, select **Save**.

6. After your app is saved, on the app designer toolbar, select **Publish** to make it available to run and share.

Much of the rest of design experience revolves around continuing to develop the site map in addition to configuring the app through the app designer. More information: [Add or edit app components](add-edit-app-components.md)

## Play your app

On the app designer toolbar, select **Play**.  This will only be available once the app is published.

  :::image type="content" source="media/app-designer-play.png" alt-text="App designer in draft stage":::

- To create a record, select **+ New**.
- To view a chart, on the app command bar select **Show Chart**. 
- To change the view, select the **My Active Accounts** view, and then select the view required.
  
  > [!div class="mx-imgBorder"]
  > ![Simple account table app.](media/build-first-model-driven-app/accounts-quickstart-app.png "Run the app")

To learn more about how to use your app, see [Basic navigation in a model-driven app](../../user/navigation.md).

## Edit an app  
  
1.  Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).  
2. Choose the environment by selecting the environment icon ![Environment icon.](media/icon-environment.PNG "Environment icon")
3. Select **Solutions**.
4. Choose the solution that contains the model-driven app where editing is required.
5. On the left navigation pane select **Apps**, select a model-driven app, and then on the toolbar select **Edit**.
6. As with creating an app editing experience will center around creating a strong [site map](model-driven-app-glossary.md#site-map)
7. In the app designer add or edit components to the app, as required. More information: [Add or edit app components](add-edit-app-components.md)  

## Next steps

[Share an app](share-model-driven-app.md)

[Edit the site map](model-driven-app-glossary.md#table)

[Add or edit app components](add-edit-app-components.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]