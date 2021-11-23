---
title: Set up mobile offline (preview) | Microsoft Docs
description: Set up and configure mobile offline for model-drive Power Apps.
author: mduelae
ms.service: powerapps
ms.component: pa-user
ms.topic: quickstart
ms.date: 11/22/2021
ms.subservice: mobile
ms.author: mkaur
ms.custom: ""
ms.reviewer: ""
ms.assetid: 
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---

# Set up mobile offline (preview)

[This topic is pre-release documentation and is subject to change.]

Use the [modern app designer](../maker/model-driven-apps/app-designer-overview) to enable your model-driven apps for offline use on a mobile device. When offline mode is enabled, users can interact with their data without internet connection on [Power Apps mobile](https://powerapps.microsoft.com/downloads/).


## Prerequisites 

Verify the following prerequisites before you enable mobile offline: 

- Environment maker, system administrator, or system customizer role is needed to configure offline mode for model driven apps. These roles have create/read/write/delete and share access on the **mobile offline profile** table. More information: [About predefined security roles](share-model-driven-app.md#about-predefined-security-roles)

- Users with the **basic user** role can open and use an offline application. This role has the read access to the **mobile offline profile** table.

If you need to use a custom security role, edit it accordingly:

- Edit your security role &gt; Core Records tab &gt; Mobile Offline profile.

  > [!div class="mx-imgBorder"] 
  > ![Required security roles to use mobile offline.](media/mobile-offline-image1.png)


##  Optimize your app for mobile offline 

Before you enable offline mode, make sure your model-driven app is optimized for offline and mobile use. Mobile apps run on smaller screens with limited connectivity so it's important that the app is fast and always aviliable. Create an app that is simple and lightweight. Also, consider the number of user scenarios that you want to cover and the amount of data the app will use.

If you have two types of users in your organizers such as desktop and remote mobile users then create two seperate apps. Optimize the user experience and create an online app for your office users and another app for your mobile users that may have limited connectivity. 

Follow these best practices when building an app for mobile offline use:

- Identify the on-the-go scenarios that are functionally related, such as which would be performed by a specific user on a given day and need to be completed in the field.
- Reduce the complexity of your app and limit the amount of application metadata that will be downloadeded on the device. Only add the tables and views absolutely needed in a mobile scenario. For more information, see [Add pages to your app](../maker/model-driven-apps/create-a-model-driven-app#add-pages-to-your-app).
- Only keep the needed views and remove the unnecessary ones. For instance, you may want to avoid adding the **All accounts** view and keep the ones like the **My active accounts**. Keep your forms lightweight for a smooth and intuitive experience on small screen devices. You have the following options for mobile-optimized forms:

   - Build dedicated forms for mobile use

   - Share forms across mobile and desktop experience while having some fields disabled on mobile

    
      > [!div class="mx-imgBorder"]
      > ![](media/image2.png)


## Enable your app for offline use (preview)

Set up the new mobile offline experience in the [modern app designer (preview)](../maker/model-driven-apps/app-designer-overview).

1. Sign in to [Power Apps (preview)](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) 

2. On the left nav, select **Apps** and then select the model-driven app that you want enable for offline.

4. Select ... > **Edit** > **Edit in preview** to open the modern app designer.

    > [!div class="mx-imgBorder"]
    > ![Edit an app](media/offline-edit-app.png)
 
4. On the command bar, select **Settings**.

    > [!div class="mx-imgBorder"]
    > ![Select setting on the command bar](media/mobile-offline-image4.png)

5. Select the **Upcoming** setting and then set the **Offline setup from the modern app designer** toggle to **On**.

    > [!div class="mx-imgBorder"]
    > ![Set the Offline setup from the modern app designer toggle to on ](media/mobile-offline-image5.png)

6.  Select the **General** setting and then set the **Can be used offline** toggle to **On**.

    > [!div class="mx-imgBorder"]
    > ![Set Can be used offline toggle to on](media/mobile-offline-image6.png)

3.  Select an existing offline profile or select **New profile wiht current app data**. For more information, see [Mobile offline profiles]().


4.  Close the Settings dialog, then save and publish your application. You're done, the application is setup for offline.

## Mobile offline profiles

The offline profile represents the dataset that will be synced locally on the device and used by the app. It consists of a list of tables with the related filters to be applied when syncing the data on to the device.

**Pre-requisite**: Tables need to be enabled for offline to be able to add them to an offline profile. If you cannot add your table to your offline profile, you should make sure it is correctly enabled through the **Data &gt; Tables &gt; 'Table name' &gt; Settings:**

**Tip**: While an app can only be linked to one single profile, a profile can be shared between multiple apps. This can be useful when different apps share the same dataset to only download it once on the device and have it shared between the apps locally.

### Default profiles

The modern app designer comes with a capability to generate a default offline profile based on the application setup.

**Note**: This option is meant to help you build an offline profile tailored for your application like identifying all the tables needed to be added to your profile but it may not be perfect:

-   It won't be able to compute the most optimal filters for each of your tables. It is recommended that you review and adjust the proposed filters with the most appropriate ones based on the business needs.

-   If your application is too complex, the auto-generation may be partially successful (i.e.: Only a part of the application would be properly setup for offline) and you would need to tweak the profile or the app accordingly.

To generate a default profile for your application, you can select the "**+ New profile with current app data**" option. This action will open the new offline profile panel and will trigger the profile creation based on your application setup (e.g.: Tables and views setup in your application).

![Graphical user interface  application Description automatically generated](media/image9.png)

**Important**: Review and tweak the different proposed filters for each table to make sure the data downloaded on users' devices is limited to just the necessary. You can focus on the mostly used tables in your application (these have a filter which is likely set to "Organization rows").

The tables which have been added to the profile and have a "Related rows only" are the ones that are used in some views and need to have related information available, you may not need to modify them.

### Add a table to an offline profile and apply filters

Applying an appropriate filter for each of the tables configured in the offline profile is critical to limit the amount of data downloaded on users' devices.

You can add a table to a profile by selecting the "**Add table**" option:

![Graphical user interface  text  application  email Description automatically generated](media/image10.png)

Once the table is selected, you can define the right filters.

The first section is meant to define the set of needed records. It can be one of the following options:

-   Organization records (user, team or business unit)

-   All records

-   Related records only

-   Custom (this option relies on the expression builder which allows advanced conditions setup)

The second section (relationships) lists the different relationships available between the current table and other tables added in the offline profile.

Selecting a relationship will ensure related records following that relationship will be downloaded and made available offline.

![Graphical user interface  application Description automatically generated](media/image11.png)

The third section (Files / Images) allows you to define what table columns of type file or image need to be downloaded offline. For images, each column can be selected granularly but not for files (it's all or nothing).

The last section (Sync interval) defines the sync frequency to be applied on the device to sync the data with the server. If your table data doesn't change frequently like a catalog or product table, you may want to refresh it only once a day and hence focus on only syncing data when necessary.

After having adjusted the filters, you can click on **Add** to add your table and filters to your profile.

Once all tables are properly configured in your profile, you can click on **Done** and **publish your application** to apply your changes.

Your app is now enabled for offline use and all users having access to your application will be able to use it offline.






[!INCLUDE[footer-include](../includes/footer-banner.md)]
