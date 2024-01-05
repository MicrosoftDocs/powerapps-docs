---
title: Set up mobile offline  | Microsoft Docs
description: Set up and configure mobile offline for model-driven apps made with Power Apps.
author: trdehove
ms.component: pa-user
ms.topic: quickstart
ms.date: 10/27/2023
ms.subservice: mobile
ms.author: trdehove
ms.custom: ""
ms.reviewer: sericks
ms.assetid: 
search.audienceType: 
  - maker
---

# Set up mobile offline 

Use the [modern app designer](../maker/model-driven-apps/app-designer-overview.md) to enable your model-driven apps for offline use on a mobile device. When offline mode is enabled, users can interact with their data without internet connectivity on the [Power Apps mobile app](https://powerapps.microsoft.com/downloads/).

## Prerequisites 

Verify the following prerequisites before you enable mobile offline: 

- Environment maker, system administrator, or system customizer role is needed to configure offline mode for model-driven apps. These roles have Create, Read, Write, Delete, and Share privileges on the **Mobile offline profile** table. More information: [About predefined security roles](../maker/model-driven-apps/share-model-driven-app.md#about-predefined-security-roles)

- Users with the basic user role can open and use an offline application. This role has the Read privilege for the **Mobile offline profile** table.

   If you have a custom security role, make sure you have the Read privilege for the **Mobile offline profile** table. More information: [Miscellaneous privileges](/power-platform/admin/miscellaneous-privileges)

## Optimize your app for mobile offline 

Mobile apps run on smaller screens with limited connectivity. Before you enable offline mode, make sure your model-driven app is optimized for offline and mobile use. Consider the number of user scenarios that you want to cover and the amount of data the app will use. Create an app that's simple and lightweight.

If you have desktop and remote mobile users, optimize the user experience by creating two separate apps. Create an online app for your office users and another app for your mobile users who might have limited connectivity.

Follow these best practices when building an app for mobile offline use:

- Identify the on-the-go scenarios that are functionally related, such as tasks that are performed by users who work in the field.
- Reduce the complexity of your app by limiting the amount of app metadata that needs to be downloaded on a user's device. Only add the tables and views that are needed for your mobile users. More information: [Add pages to your app](../maker/model-driven-apps/create-a-model-driven-app.md#add-pages-to-your-app)
- Only keep views that are necessary, and remove any that aren't needed on a day-to-day basis. For example, keep the **My active accounts** view and remove the **All accounts** view. Keep your forms lightweight for a smooth and intuitive experience on small-screen devices. The following are possible optimizations for forms on mobile:

  - Build dedicated forms for mobile use.

  - Share forms across the mobile and desktop experience, but disable some fields on mobile.
   
      > [!div class="mx-imgBorder"]
      > ![Form properties.](media/mobile-offline-image2.png)

## Enable your app for offline use

1. Sign in to [Power Apps](https://make.powerapps.com).

1. On the left pane, select **Apps**, and then select the model-driven app that you want to enable for offline.

1. Select **More (...)** > **Edit** to open the modern app designer.

1. On the command bar, select **Settings**.

1. On the **General** tab, set the **Can be used offline** toggle to **On**.

1. Select the type of offline profile: **Default** or **Advanced**.

    - If you select **Default**, the app is enabled for offline use for all users. Select an existing offline profile, or select **New profile with current app data**. To set up a new offline profile, see [Set up a mobile offline profile](setup-mobile-offline.md#set-up-a-mobile-offline-profile).

   	- If you select **Restricted to selected users**, the app is enabled for offline use only for a selected list of users. Select one or multiple offline profiles, or select **New profile with current app data**. To set up a new offline profile, see [Set up a mobile offline profile](setup-mobile-offline.md#set-up-a-mobile-offline-profile).
  
    > [!Note]
    > You must have admin privileges to assign users to an offline profile.
    
1. Close the **Settings** page, and then save and publish your app. When you're done, the app will be set up for offline use.

## Set up a mobile offline profile

The mobile offline profile represents the dataset that's synced on a user's device. The profile contains the tables, including related filters, that are applied when data is synced to a user's device. For more information about offline profiles, see [Offline profile guidelines](mobile-offline-guidelines.md).

> [!Note]
> If the offline profile is in advanced mode, it is required to add users to the offline profile. If you don't add a user to the offline profile, the user can't use the app in offline mode.

### Enable a table for offline

A table needs to be enabled for offline to add it to a offline profile. Some tables are enabled for offline by default. Follow these steps to verify whether a table is enabled for offline.

1. Sign in to [Power Apps](https://make.powerapps.com). 

1. In the left pane, select **Data** > **Tables**. 
1. Select the table that you want to add to an offline profile, and then, on the command bar, select **Settings**.
    
1. In the **Edit table** settings, select **Advanced options**, and in the **Rows in this table** section, select **Can be taken offline**.

   > [!NOTE]
   > An app can only be linked to one profile. However, a profile can be shared between multiple apps. This can be useful when different apps share the same dataset, which then only needs to be downloaded once on the device and is shared between the apps.
   
    :::image type="content" source="media/mobile-offline-image8.png" alt-text="Enable a table for offline use.":::

### Generate a default profile

The modern app designer can generate a default offline profile that's based on how the app is configured.

> [!NOTE]
> The default offline profile is a starting point to help you quickly build an offline profile. The default profile won't compute the optimal filters for each table. If you have a complex app, the auto-generated profile might be partially successful because only part of the app might be set up correctly for offline use. With this in mind, it's important that you review and adjust the proposed filters based on your organization's needs.

1. Select **New profile with current app data**. 

    :::image type="content" source="media/mobile-offline-image7-1.png" alt-text="Create a new profile.":::

1. Review the proposed filters for each table. Make sure that the data downloaded on users' devices is limited to only what's necessary. Focus on the most-often-used tables in your app, which in most cases have the **Organization rows** filter set.

    :::image type="content" source="media/mobile-offline-image9.png" alt-text="Default auto-generated profile.":::

  The tables that are added to the profile also have the **Related rows only** filter. These are tables that are used in some views and need to have related information available, so you might not need to modify them based on your organization's needs.

### Add a table to an offline profile and apply filters

Applying an appropriate filter for each of the tables configured in the offline profile is critical to limit the amount of data that's downloaded on users' devices.

Keep in mind, that you can have 15 related tables in a custom filter. You can also have 15 relationships. These are distinct checks that might not add up. The 15 relationships limit is transitive, meaning if table B has N relationships, and you add a reference to table B in table A, then it will increase the relationship count of A by N+1; one plus the N already in table B. This limit is per profile item for table in the profile.

1. Select **Add table**.
   
    :::image type="content" source="media/mobile-offline-image9-2.png" alt-text="Add a table.":::

1. Choose a table, and then define the filters. 
 
1. Set the following filters:

   1. Choose the row that you want to make available offline. For the **Custom** option, use the [expression builder](../maker/model-driven-apps/create-edit-view-filters.md) to set up advanced conditions.
   1. **Relationships** lists the different relationships available between the current table and other tables added in the offline profile. Selecting a relationship will ensure that related rows following that relationship are downloaded and made available offline.
   1. **Files** and **Images** define which columns for a file or image need to be downloaded offline. For files, you can choose to download every column or none at all. For images, you can select each column you want to download granularly.
   1. **Sync interval** defines the sync frequency to be applied on the device to sync the data with the server. If a table's data doesn't change frequently, like a catalog or a product table, you might want to focus on only syncing data when necessary, such as refreshing only once a day.
   
     > [!NOTE]
     > You can only have up to 15 related tables in a profile. If you exceed the limit, then you will get an error and won't be able to publish the offline profile.
      
1. Select **Add + save** to add your table and filters to the profile.

1. When all tables are properly configured for the profile, select **Done** > **Publish your application**.

When the app is published, the app will be enabled for offline use.

### Add users to an offline profile

If you selected the **Default** offline profile mode, all your users who have access to the app can also use it in offline mode.

However, if you selected **Restricted to selected users**, you have to manually add users (requires admin privileges) to the offline profile. The app will be enabled for offline use only for those configured users.

1.  Select **Add users (requires admin privileges)**.

    :::image type="content" source="media/advanced-mobile-offline-profile.png" alt-text="Restricted to selected users auto-generated profile.":::

1.  Sign in to the Power Platform admin center.

1.  In the **Users with offline access** area, select **Add users**.

1.  Select the users that you want to add to the mobile offline profile. The users that are added, based on teams, are listed under each team. User's that are added individually are listed as individual users.

1.  When you're done adding people, select **Save**.

> [!Note]
> If you made any changes to a Microsoft Entra ID group team, you must remove and add the team back to the mobile offline profile for the changes to take effect.

## Enable mobile offline classic

Offline-first is the default mode when you enable an app for offline use. If you want to switch to the [offline classic mode](mobile-offline-overview.md#offline-first-vs-classic-offline), you need to enable it for each of your model-driven apps. It's a separate app setting for each app.

1.  Sign in to [Power Apps](https://make.powerapps.com).

1.  On the left pane, select **Apps**, and then select the model-driven app that you want to enable for offline.

1.  Select **More** (**...**) &gt; **Edit** to open the modern app designer.

1.  On the command bar, select **Settings**.

1.  On the **Features** tab, set the **Enable offline classic** toggle to **Yes**.

1.  Select **Save** and then publish the app.

## Sync conflict 

When a user makes changes to data in an offline app, updates to each column are pushed back to Dataverse as soon as the network is available. The last update to each column is stored in Dataverse, so this sync won't fail due to conflicting changes. 
 
Server-side plug-ins and validation can invalidate changes. Those changes are reverted locally, and an error is written to the **Sync Errors** Dataverse table.

## Define sync settings on mobile 
You can enable users to control the automatic sync intervals or the connection type to synchronize the data.

1. On the command bar, select **Settings**.

2. Select the **Upcoming** tab:

    - Set the **Allow users to adjust sync frequency** option to **On** to adjust the sync interval to sync more or less frequently depending on individual needs. Users can choose to not automatically sync, if they only want to sync on demand.
    - Set the **Allow users to sync on Wi-Fi only** option to **On** to let users choose if their automatic sync happens on cellular networks and Wi-Fi connections or only when connected to a Wi-Fi network.
 

[!INCLUDE[footer-include](../includes/footer-banner.md)]
