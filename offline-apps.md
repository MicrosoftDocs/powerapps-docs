# Offline apps

Mobile applications usually require internet connection to work properly. While remote workers need to use their applications to complete their tasks from anywhere, the issue is that network connectivity is often inconsistent throughout their workdays and can even become limited or inexistant.

Enabling mobile applications to be available while offline not only solves this problem but also comes with additional benefits like providing a more responsive, performant experience or saving the device's battery with less connections made to the server.

Model-driven applications can be enabled for offline use, so they become always available regardless of the network connectivity. This feature is available through Power Apps and Dynamics (Field Service, Sales) mobile applications.

Internet connections remain needed to sync back and forth data to Dataverse as well as for online-only scenarios.

Through the offline profile, the app maker can define the data (tables in Dataverse) needed offline and then the application will automatically keep it in sync between the device and the server.

<u>Note:</u> The following documentation describes the new offline configuration setup available in the modern app designer as well as offline-first available in preview now.

-   For documentation about the offline experience currently generally available, please refer to the [**Dynamics 365 documentation**](https://docs.microsoft.com/en-us/dynamics365/mobile-app/setup-mobile-offline).

-   For more information on how to set up mobile offline for canvas apps, see [**Develop offline-capable canvas apps**](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/offline-apps).

## Default roles setup for offline applications

-   The **environment maker, system customizer or system administrator** role is needed to configure offline for model driven apps. These roles have create/read/write/delete and share access on the "mobile offline profile" table.

-   Users with the **basic user** role can open and use an offline application. This role has the read access to the "mobile offline profile" table.

If you need to use a custom security role, you may want to edit it accordingly:

*Edit your security role &gt; Core Records tab &gt; Mobile Offline profile*

![A picture containing calendar Description automatically generated](media/image1.png)

## Next steps

Configure your model-driven app for offline (Preview)

# 

# Configuring your model-driven app for offline (Preview)

The [modern app designer](https://docs.microsoft.com/en-us/powerapps/maker/model-driven-apps/app-designer-overview) comes with a new way of configuring offline for your model-driven applications. It is a streamlined experience which removes many steps that were required before through the legacy app designer and the Power platform admin center.

## Create or edit your mobile model-driven application and optimize it for mobile use

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

## 

## Enable your app for offline use (preview)

#### Activate the offline configuration experience

The new offline configuration experience in the modern app designer is a preview feature and needs to be enabled first.

1. **Open** your application using the modern app designer.

2.  Select **Settings** &gt; **Upcoming** tab.

3.  Go to the **Upcoming** tab and set the "**Offline setup from the modern app designer**" toggle to On

![Graphical user interface  application  Teams Description automatically generated](media/image5.png)

4.  You should then see the Offline configuration displayed in the **General** tab.

![](media/image6.png)

#### Enable offline for your application

1.  From **Settings &gt; General**

2.  Set the **"Can be used offline"** toggle to On

3.  Select an existing or create a new offline profile (more information in the <u>mobile offline profiles</u> section)

<!-- -->

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

## Next steps

Use your offline application

# Use your offline application

After having enabled offline for your model-driven app, you can start using it through the mobile application in place in your organization ([Power Apps mobile](https://docs.microsoft.com/en-us/powerapps/mobile/run-powerapps-on-mobile), Dynamics for Phones, Dynamics Sales or Dynamics Field Service)

Depending on the application you're using and your setup, the offline experience on the device can be different:

**Classic offline** defines the current offline experience available to Power Apps or Dynamics Sales mobile users and **Offline-first** is the new end user experience already available in the Field Service mobile app and now in preview for everyone else.

In the below sections, we will highlight the differences between the two and show the advantages that comes with offline-first.

## Opening your offline model-driven app for the first time

For your app to be available offline, it needs to download the application and user data on the device first. This process is called initial offline sync.

The **application data** includes all the resources needed for the application to run properly (UX components, scripts, etc.) and the **user data** is the data described in the offline profile and stored in the Dataverse tables.

| Classic offline                                                                                                                                          | Offline-first                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![Graphical user interface  application Description automatically generated](media/image12.png) | ![Graphical user interface  application Description automatically generated](media/image13.png) |
| Users can skip the initial offline sync and stay online. This causes workers in your organization to not have the same experiences.                      | Initial offline sync is triggered for everyone consistently at app launch.                                                                               |

During the initial offline sync, you can see a notification at the bottom of the screen that shows the application is syncing the offline data. This can take a few minutes or even more depending on what has been configured in the offline profile.

![Graphical user interface  application Description automatically generated](media/image13.png)![A picture containing graphical user interface Description automatically generated](media/image14.png) ![Graphical user interface  application Description automatically generated](media/image15.png) ![Graphical user interface  application Description automatically generated](media/image16.png)

You can tap on **See details** or **the offline icon in the sitemap** to open the offline status page and see more information about the current sync progress:

![](media/image18.jpeg)

Once the sync completes, you can start using your application offline.

![Graphical user interface  table Description automatically generated](media/image19.jpeg)

Following the different sync intervals setup in your offline profile, the subsequent syncs to the server will happen automatically.

## Using the app offline

Once the initial sync is finished, the app can be used offline. While it is transparent with offline-first, the user must handle offline explicitly when in classic offline.

| Classic offline (when online)                                                                                                                                                                                                       | Classic offline (when no network)                                                                                                          | Offline-first                                                                                                                |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| ![](media/image20.png)                                                                                                                                                            | ![](media/image21.png)                                                                    | ![](media/image21.png)                                                      |
| User see records listed from the server and may be facing weird situations like editing an online record and suddenly losing connection. In that case, I may lose all my changes if I try to save them while not having connection. | When no network available, the records are listed from the local database and hence wouldn't be the same as when connected to the network. | With Offline-first, my data is always the same regardless of my network connectivity and relies on my offline profile setup. |

One option to avoid the confusing experience described above with classic offline between **with** and **without** network connectivity is to force the app to work offline (e.g.: Only access the local database).

| Classic offline                                                                                                                                                                                 | Offline first                                                                      |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| ![](media/image22.png)                                                                                                                        | ![](media/image23.png)           |
| Enabling the **Work in offline mode** toggle is an option to have a consistent experience but you have to remember to disable at some point to sync back all your changes since you enabled it. | No toggle to handle anymore, I never forget to sync back my changes to the server. |

**Note:** Some of the experiences (like Dashboards/Charts, multi-table BPFs or server-side plugins) which are only available online may not be available when enabling the offline-first (preview) feature. You need to validate that your app is fully functional before deploying to your end users.

## Enabling offline-first for your application (Preview)

Once you're ready to test offline-first, you can enable offline-first for each of your apps separately as it is an app setting.

1.  Open your application using the **modern app designer**

2.  Select **Settings** &gt; **Upcoming** tab.

3.  Go to the **Upcoming** tab and set the "**Disable classic offline**" toggle to On

4.  

Offline limitations cleanup

![Graphical user interface  application  Teams Description automatically generated](media/image24.png)

![Graphical user interface  text  application Description automatically generated](media/image25.png)
