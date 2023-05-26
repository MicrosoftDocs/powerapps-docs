---
title: Set up mobile offline for canvas apps (preview)| Microsoft Docs
description: This article explains how to set up mobile offline for canvas apps.
author: trdehove
ms.component: pa-user
ms.topic: quickstart
ms.date: 05/16/2023
ms.subservice: mobile
ms.author: trdehove
ms.custom: ""
ms.reviewer: sericks
ms.assetid: 
search.audienceType: 
  - enduser
searchScope:
  - "Power Apps"
---

# Set up mobile offline for canvas apps (preview)

[This topic is pre-release documentation and is subject to change.]

When offline mode is enabled in the Power Apps mobile app, users who need to work from remote locations can work seamlessly without worrying about their internet connection.

> [!Important]
> [!include [preview](../includes/cc-preview-features-definition.md)]
>
> This feature is in process of rolling out and may not be available in your region yet.

## Prerequisites

Verify the following prerequisites before you enable mobile offline.

- You must be running a recent version of Power Apps mobile app. 

  |Feature | Required minimum version | 
  |--------|---------------------------|
  | Power Apps Studio | 3.23052.00| 
  | Power Apps mobile app | 3.23053.00 | 
  |Auto-generated offline profile | 3.23053.00 | 
    
- The canvas app must be in a solution. More information: [Create a canvas app from within a solution](../maker/canvas-apps/add-app-solution.md)

- The canvas app must use Dataverse data only.

-   The Environment maker, System administrator, or System customizer role is required to configure offline mode for canvas apps. These roles have Create, Read, Write, Delete, and Share privileges on the **Mobile offline profile** table. More information: [<u>About predefined security roles</u>](../maker/model-driven-apps/share-model-driven-app.md#about-predefined-security-roles)

-   Users with the Basic user role can open and use an offline application. This role has the Read privilege for the **Mobile offline profile** table.

    If you have a custom security role, make sure you have the Read privilege for the **Mobile offline profile** table. More information: [Miscellaneous privileges](/power-platform/admin/miscellaneous-privileges)

## Optimize your app for mobile offline

Mobile apps run on small screens with limited connectivity. Before you enable offline mode, make sure your canvas app is optimized for offline and mobile use. Consider the number of user scenarios that you want to cover and the amount of data the app will use. Create an app that's simple and lightweight.

Follow these best practices when building an app for mobile offline use:

-   Identify the on-the-go scenarios that are functionally related, such as tasks that are performed by users who work in the field.

-   Reduce the complexity of your app by limiting the amount of tables that need to be downloaded on a user's device. Sometimes it is better to have two apps instead of one.

-   Use views that are optimized for the experience rather than displaying a large set of data. For example, it is preferable to use the **My active accounts** view, rather than the **All accounts** view.

## Enable tables for offline use

Tables used by your offline-first app must be enabled for offline use. Note that some built-in tables are enabled for offline use, by default. 

Keep in mind that if you are using a table provided by a different solution, the solution author may not want the table to be enabled for offline use. Therefore, it may not be possible to enable some tables for offline use. However, you can enable any new, custom table for offline use.

Follow these steps to enable a table for offline use.

1.  Sign in to [Power Apps](https://make.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
2.  In the navigation pane, select **Tables**.
3.  Select the table you want to enbable for offline use.
4.  Select **Edit**.
5.  Select **Edit table properties**. 
6.  In the **Edit table** pane, select **Advanced options**. Then scroll to the **Rows in this table** section.
7.  Select **Can be taken offline**.

    :::image type="content" source="media/can-be-taken-offline.png" alt-text="Select the **Can taken offline** option.":::

## Enable your app for offline use

Enable your app for offline use in [Power Apps studio](../maker/canvas-apps/power-apps-studio.md).

1.  In the navigation pane, select **Apps**. 
1.  Select check mark next to the canvas app that you want to enable for offline use.
1.  Select **Edit** in the command bar.
1.  Select **Settings**.
1.  In the window that appears, select **Upcoming Features**, and then select **Experimental**. 
1.  Set the **Dataverse offline** option to **On**.

    :::image type="content" source="media/dataverse-offline.png" alt-text="Dataverse offline option.":::

1.  Select **General**.
  
1. Set the **Can be used offline** option to **On**.
1. Select an offline profile. You have two options:

    - Use an auto-generated profile. An auto-generated profile will be available soon and is the recommended option. 
        When an auto-generated profile is used, the app downloads the tables that are used in your app.
    - Create your own profile. See [Set up a mobile offline profile](#set-up-a-mobile-offline-profile) and customize it for your needs. Then click the **Refresh** icon to see your new profile in the list.

        :::image type="content" source="media/can-be-used-offline.png" alt-text="Can be used offline option.":::
    
       > [!Note]
       > If you don’t see the **Can be used offline** option, make sure that the app is in a solution. More information: [Create a canvas app from within a solution](../maker/canvas-apps/add-app-solution.md)

        A page using the **Offline** template is automatically inserted. The page contains an icon that uses the [Connection](/power-platform/power-fx/reference/signals#connection) Power Fx function. The icon reflects the [offline sync status](canvas-mobile-offline-working.md#sync-status-icons). You can decide whether you want to use it, and you can also customize it, as appropriate.
        
       > [!Note]
       > If you are enabling a brand new canvas app for offline use, make sure the default first screen is based on the **Offline** template.
        
1.  Close the **Settings** window, and then save and publish your app. When you're done, the app will be set up for offline use.

## Set up a mobile offline profile

You can create and assign an offline profile to a canvas app. More information: [Offline profile guidelines](mobile-offline-guidelines.md)

> [!Note]
> The selected offline profile must be updated and published.
>
> When the offline profile used by a canvas app is updated and published, the canvas app must also be published afterward.

### Create an offline profile with admin rights

To create an offline profile with admin rights, follow these steps:

1.  Go to [Power Platform admin center](https://admin.powerplatform.microsoft.com/) and sign-in as an admin.

2.  In the navigation pane, select **Environments**.

3.  Select an environment, and then select **Settings**.

4.  Expand **Users + permissions**, and then select **Mobile configuration**.

5.  Select **Create new profile** to create a new profile for mobile offline. If you already have a profile that you want to edit, select it from the list.

6.  Enter a name and description for your mobile offline profile. Select **Create** to create the mobile offline profile.

7.  After the profile is created, select it to continue editing it.

8.  In the **Data available offline** area, select **Add table** to add a table to the profile.

9.  Select a table from the list of tables shown. Only tables that can be enabled for mobile offline appear in the list. Select **Next**.

10. Select a filter, based on the ownership type for the table. Table ownership is decided when you create a table. More information: [<u>Types of tables</u>](../maker/common-data-service/types-of-entities.md).

    | Table ownership type| Available filter options for data download  |
    |-------------------------|-------------------------|
    | User or team | <ul><li>**Download related rows only** - Make related data for this table available offline. If you don't set any relationships, no rows for this table will be available.</br></li></br><li>**All rows** - Make all rows for this table available offline.</br></li></br><li>**Other data filter** - Make only the specified rows for this table available offline, and then choose from the following:</br></br><ul><li>**Download user rows** - Make only your rows available offline.</br></li></br><li>**Download team rows** - Make your team's rows available offline.</br></li></br><li>**Download my business unit's rows** - Make your business unit's rows available offline.</br></li></br></ul></li></ul> |
    | Organization | <ul><li>**Download related rows only** - Make related data for this table available offline. If you don't set any relationships, no rows for this table will be available.</br></li></br><li>**All rows** - Make all rows for this table available offline.</br></li></ul> |
    | Business | <ul><li>**Download related data only** - Make related data for this table available offline. If you don't set any relationships, no rows for this table will be available.</br></li></br><li>**All rows** - Make all rows for this table available offline.</br></li><br><li>**Other rows** - Make only the specified rows for this table available offline and choose from the following:</br></blockquote></br><ul><li>**Download my business unit's rows** - Make your business unit's rows available offline.</br></li></ul></li></ul> |
    | None | <ul><li>**Download related rows only**. Make related data for this table available offline. If you don't set any relationships, no rows for this table will be available.</br></li></ul> |


    If **Custom** is selected, admins can define a custom filter based on the following rules. Admins can create filters up to three levels.

    |Rules                      |  &nbsp;                      |  &nbsp;                 |
    |-------------------------------|----------------------------|--------------------------------|
    | equal                         | not equal                  | gt – greater than              |
    | ge – greater than or equal to | le – less than or equal to | lt – less than                 |
    | like                          | not-like                   | in                             |
    | not-in                        | null                       | not-null                       |
    | eq-userid                     | ne-userid                  | eq-userteams                   |
    | eq-useroruserteams            | eq-useroruserhierarchy     | eq-useroruserhierarchyandteams |
    | eq-businessid                 | ne-businessid              | eq-userlanguage                |
    | begins-with                   | not-begin-with             | ends-with                      |
    | not-end-with                  |                            |                                |

11. In the **Include \[table name\] records related to these tables** area, select the related table relationships. You must have added the table that you want to create the relationship with. For example, if you want to add a relationship between the Account and Contact tables, then you need to add both tables to the mobile offline profile.

    For example, if you select **Contact \| Field name: Primary contact** this means for every contact, the system will also download the account related to it.

    :::image type="content" source="media/include-account-records.png" alt-text="Include accounts records options.":::

12. Select **Save** to add the table to your profile so you can continue editing it.

### Create an offline profile without admin rights

Coming soon, you’ll be able to create an offline profile directly in Power Apps Studio. Until then, a great way to configure an offline profile is to create a simple model-driven app in your test environment with the same tables, and then auto-generate an offline profile from the tables in that app. You’ll be able to select this offline profile from Power Apps Studio.

1. Create a model-driven app.
2. [Enable the app for offline use](setup-mobile-offline.md).
3. [Generate a default profile](setup-mobile-offline.md#generate-a-default-profile) and [add tables to the offline profile and apply filters](setup-mobile-offline.md#add-a-table-to-an-offline-profile-and-apply-filters).
4. Publish the model-driven app.
5. Select this offline profile in your canvas app.

## Create a canvas offline app

To make it easier, we’ve create an offline template that we recommend you to use for each page of the app. The template contains a navigation bar with a placeholder for the name of the app and the Globe icon that gives the user a quick view of the server connectivity and sync state, putting offline at the center of the experience so that the user always knows whether your device and data are ready to go. 

As soon as the app is enabled for offline, a new page created from the offline template is automatically inserted:  

:::image type="content" source="media/new-page.png" alt-text="The template contains a navigation bar with a placeholder for the name of the app and the Globe icon that gives the user a quick view of the server connectivity and sync state":::

You can also add a new page from this template as any other template: 
  
:::image type="content" source="media/offline-template.png" alt-text="Select the Offline template.":::

The globe icon of the template uses different icons depending on the PowerFx Connection.Sync function. You can also create your own icon and set the Icon property using the following PowerFx script: 

```PowerFx
Switch(Connection.Sync, 

   ConnectionSync.Connected, Icon.Globe,  

   ConnectionSync.ConnectedWithWarning, Icon.GlobeWarning, 

   ConnectionSync.ConnectedPendingUpsync, Icon.GlobeChangesPending, 

   ConnectionSync.ConnectedError, Icon.GlobeError, 

   ConnectionSync.ConnectedRefresh, Icon.GlobeRefresh, 

   ConnectionSync.NotConnected, Icon.GlobeNotConnected,  

   ConnectionSync.NotConnectedWithWarning, Icon.GlobeWarning, 

   ConnectionSync.NotConnectedPendingUpsync, Icon.GlobeChangesPending, 

   ConnectionSync.NotConnectedSyncError, Icon.GlobeError) 
```

## Limitations and known issues

- The auto-generated offline profile does not handle filters. As a result, for each table used in the app, it downloads **all** rows on which the user has permissions.

- Non-Dataverse connectors, like Sharepoint, are not supported in offline mode.

- Some Dataverse tables aren't supported in offline mode. More information: [Mobile offline capabilities and limitations](offline-capabilities.md)

- Items in a gallery may appear in a different order in an offline-enabled app if no [sort order](/power-platform/power-fx/reference/function-sort) is selected. Choose a sort order in the gallery control to ensure that the app behaves consistently in mobile apps and web browsers.

- Canvas apps that are in offline mode, do not yet support files or images. This means that if you are using a Dataverse table that has an image on it, it may create some unanticipated errors.  For instance, if you are using a gallery, you need to make sure that the template and the layout is not using images. 
