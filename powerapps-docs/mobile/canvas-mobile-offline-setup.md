---
title: Set up mobile offline for canvas apps (preview)| Microsoft Docs
description: This article explains how to set up mobile offline for canvas apps.
author: trdehove
ms.component: pa-user
ms.topic: quickstart
ms.date: 04/12/2023
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

## Prerequisites

Verify the following prerequisites before you enable mobile offline:

-   The **Environment maker**, **System administrator**, or **System customizer** role is required to configure offline mode for canvas apps. These roles have Create, Read, Write, Delete, and Share privileges on the **Mobile offline profile** table. More information: [<u>About predefined security roles</u>](../maker/model-driven-apps/share-model-driven-app.md#about-predefined-security-roles)

-   Users with the **Basic user** role can open and use an offline application. This role has the Read privilege for the **Mobile offline profile** table.

    If you have a custom security role, make sure you have the Read privilege for the **Mobile offline profile** table. More information: [Miscellaneous privileges](/power-platform/admin/miscellaneous-privileges).
    
- The canvas app must be associated to a solution. More information: [Create a canvas app from within a solution](../maker/canvas-apps/add-app-solution.md)

## Optimize your app for mobile offline

Mobile apps run on small screens with limited connectivity. Before you enable offline mode, make sure your canvas app is optimized for offline and mobile use. Consider the number of user scenarios that you want to cover and the amount of data the app will use. Create an app that's simple and lightweight.

Follow these best practices when building an app for mobile offline use:

-   Identify the on-the-go scenarios that are functionally related, such as tasks that are performed by users who work in the field.

-   Reduce the complexity of your app by limiting the amount of tables that need to be downloaded on a user's device. Sometimes it is better to have two apps instead of one.

-   Use views that are optimized for the experience rather than displaying a large set of data. For example, it is preferable to use the **My active accounts** view, rather than the **All accounts** view.

## Enable tables for offline use

Tables used by your offline-first app must be enabled for offline use. Note that some built-in tables are enabled for offline use, by default. 

Keep in mind that if you are using a table provided by a different solution, the solution author may not want the table to be enabled for offline use. Therefore, it may not be possible to enable some tables for offline use. However, you can enable any new custom table for offline use.

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

Enable your app for offline use in the [Power Apps studio](../maker/canvas-apps/power-apps-studio.md).

1.  In the navigation pane, select **Apps**, 
1.  Select check mark next to the canvas app that you want to enable for offline use.
1.  Select **Edit** in the command bar.
1.  Select **Settings**.
1.  In the window that appears, select **Upcoming Features**, and then select **Experimental**. 
1.  Set the **Dataverse Offline** option to **On**.

    :::image type="content" source="media/dataverse-offline.png" alt-text="Dataverse offline option.":::

1.  Select **General**. Then do the following:
  
    - Set the **Can be used offline** option to **On**.
    - We recommend that you use an **auto-generated profile**. When an auto-generated profile is used, the app downloads on the device the tables that are used in your app.

    :::image type="content" source="media/can-be-used-offline.png" alt-text="Can be used offline option.":::

    > [!Note]
    > A page using the **Offline** template is automatically inserted. The page contains an icon hooked up with the [Connection](/power-platform/power-fx/reference/signals#connection) Power Fx function. The icon has multiple variant that reflect the offline sync status. You can decide to use it or not, and you can also customize it as appropriate.

1.  Close the **Settings** window, and then save and publish your app. When you're done, the app will be set up for offline use.

## Set up a mobile offline profile (optional)

The mobile offline profile is auto-generated by default. However, it is possible to create and assign an offline profile to a canvas app.

To create an offline profile, follow these steps:

1.  Go to Power Platform admin center, [<u>https://admin.powerplatform.microsoft.com</u>](https://admin.powerplatform.microsoft.com/) and sign-in as an admin.

2.  In the navigation pane, select **Environments**.

3.  Select an environment, and then select **Settings**.

4.  Expand **Users + permissions**, and then select **Mobile configuration**.

5.  Select **Create new profile** to create a new profile for mobile offline. If you already have a profile that you want to edit, select it from the list.

6.  Enter a name and description for your mobile offline profile. Select **Create** to create the mobile offline profile.

7.  After the profile is created, select it to open the profile so you can continue editing it.

8.  In the **Data available offline** area, select **Add table** to add a table to the profile.

9.  Select a table from the list of tables shown. Only tables that can be enabled for mobile offline appear in the list. Select **Next**.

10. Select a filter based on the ownership type for the table. Table ownership is decided when you create a table. For more information, see [<u>Types of tables</u>](../maker/common-data-service/types-of-entities.md).

    | **Table ownership type** | **Available Data Download Filter options** |
    |-------------------------|-------------------------|
    | **User or Team** | <ul><li><blockquote>**Download Related rows only** - Make related data for this table available offline. If you don't set any relationships, no rows for this table will be available.</br></blockquote></li></br><li><blockquote>**All rows** - Make all rows for this table available offline.</br></blockquote></li></br><li><blockquote>**Other data filter** - Make only the specified rows for this table available offline and then choose from the following:</br></blockquote></br><ul></br><li><blockquote>**Download user rows** - Make only your rows available offline.</br></blockquote></li></br><li><blockquote>**Download team rows** - Make your team's rows available offline.</br></blockquote></li></br><li><blockquote>**Download my business unit's rows** - Make your business unit's rows available offline.</br></blockquote></li></br></ul></li></br></ul> |
    | **Organization** | <ul></br><li><blockquote></br>**Download related rows only** - Make related data for this table available offline. If you don't set any relationships, no rows for this table will be available.</br></blockquote></li></br><li><blockquote></br>**All rows** - Make all rows for this table available offline.</br></blockquote></li></br></ul> |
    | **Business** | <ul></br><li><blockquote></br>**Download related data only** - Make related data for this table available offline. If you don't set any relationships, no rows for this table will be available.</br></blockquote></li></br><li><blockquote></br>**All rows** - Make all rows for this table available offline.</br></blockquote></li></br><li><blockquote></br>**Other rows** - Make only the specified rows for this table available offline and choose from the following:</br></blockquote></br><ul></br><li><blockquote></br>**Download my business unit's rows** - Make your business unit's rows available offline.</br></blockquote></li></br></ul></li></br></ul> |
    | **None** | <ul></br><li><blockquote></br>**Download related rows only**. Make related data for this table available offline. If you don't set any relationships, no rows for this table will be available.</br></blockquote></li></br></ul> |


    If **Custom** is selected, admins can define a custom filter based on the following rules. Admins can create filters up to three levels.

    | ** **                         | ** **                      | ** **                          |
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

11. In the **Include \[table name\] rows related to these tables** area, select the related table relationships. You need to have added the table you want to create the relationship with. For example, if you want to add a relationship between the Account and Contact tables, then you need to add both tables to the mobile offline profile.

    For example, if you select **Contact \| Field name: Primary contact** this means for every contact, the system will also download the account related to it.

    :::image type="content" source="media/include-account-records.png" alt-text="Include accounts records options.":::

12. Select **Save** to add the table to your profile so you can continue editing it.

## Limitations and know issues

The following is not supported

-   A canvas app doesn't work in offline on a web browser.

-   The Auto generated offline profile is not optimized yet for the app. For each table used in the app, it downloads the rows that the user has permissions on.

-   Non Dataverse connectors like Sharepoint are not supported in offline. If you use a non-Dataverse connector, the app can only access the data when the device is connected to the network

-   Dataverse Files and Images are not supported in an offline-enabled canvas app, neither when the device is connected to the network, nor when it is not connected. This is because the app operate in offline-first
