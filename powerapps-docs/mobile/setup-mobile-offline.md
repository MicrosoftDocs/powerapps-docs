---
title: Configure mobile offline for Power Apps mobile (preview) | Microsoft Docs
description: Set up and configure mobile offline for the Power Apps mobile.
author: mduelae
ms.service: powerapps
ms.component: pa-user
ms.topic: quickstart
ms.date: 11/19/2021
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

# Configure mobile offline for Power Apps mobile (preview)




## Default roles setup for offline applications

-   The **environment maker, system customizer or system administrator** role is needed to configure offline for model driven apps. These roles have create/read/write/delete and share access on the "mobile offline profile" table.

-   Users with the **basic user** role can open and use an offline application. This role has the read access to the "mobile offline profile" table.

If you need to use a custom security role, you may want to edit it accordingly:

*Edit your security role &gt; Core Records tab &gt; Mobile Offline profile*

![A picture containing calendar Description automatically generated](media/image1.png)


Mobile offline allows users to use the [Power Apps mobile](https://powerapps.microsoft.com/downloads/) app in offline mode. Model-driven app users can interact with their data, even when they don't have internet connection.


## Configuring your model-driven app for offline (Preview)

The [modern app designer](https://docs.microsoft.com/en-us/powerapps/maker/model-driven-apps/app-designer-overview) comes with a new way of configuring offline for your model-driven applications. It is a streamlined experience which removes many steps that were required before through the legacy app designer and the Power platform admin center.

### Create or edit your mobile model-driven application and optimize it for mobile use

First, you want to optimize your application for mobile offline usage, this is a recommended step for you to ensure your users will have a smooth experience on their devices. Mobile applications often need to run on small screen devices with limited connectivity. In those conditions, it is critical to ensure your application is fast and remains usable. This can be achieved by keeping your application simple and lightweight in terms of number of covered scenarios and amount of data it must deal with.

When possible, it is recommended to have a separate application for each core role in your organization. For instance, if you have desktop/office users as well as remote workers who use mobile devices, you may avoid having them using the same application and have two different applications: one online application for your office users and one mobile offline application for remote workers. This way you can build optimal and simpler experiences for both roles.

Good practices for building mobile offline applications:

1.  Identify the **on-the-go scenarios** that are functionally related (i.e.: which would be performed by a specific worker on a given day) and need to be completed in the field (not at the office).

This step will help you reduce the complexity of your application and limit the amount of application metadata to be downloaded on the device.

2.  List then [**only add the tables and views absolutely needed**](https://docs.microsoft.com/en-us/powerapps/maker/model-driven-apps/create-a-model-driven-app#add-pages-to-your-app) in your application.

Make sure you only keep the needed views and remove the unnecessary ones. For instance, you may want to avoid adding the "All accounts" view and keep the ones like the "My active accounts".

3.  Keep your forms lightweight for a smooth and intuitive experience on small screen devices

You have 2 options for having mobile-optimized forms:

1.  Build dedicated forms for mobile use

2.  Share forms across mobile and desktop experience while having some fields disabled on mobile

![](media/image2.png)


## Enable your app for offline use (preview)

The new offline configuration experience in the modern app designer is a preview feature and needs to be enabled first.

1. **Open** your application using the modern app designer.

2.  Select **Settings** &gt; **Upcoming** tab.

3.  Go to the **Upcoming** tab and set the "**Offline setup from the modern app designer**" toggle to On

![Graphical user interface  application  Teams Description automatically generated](media/image5.png)

4.  You should then see the Offline configuration displayed in the **General** tab.

![](media/image6.png)

## Enable offline for your application

1.  From **Settings &gt; General**

2.  Set the **"Can be used offline"** toggle to On

3.  Select an existing or create a new offline profile (more information in the <u>mobile offline profiles</u> section)


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
