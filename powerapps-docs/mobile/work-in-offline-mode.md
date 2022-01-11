---
title: Work offline on your mobile device using the Power Apps mobile app (preview) | Microsoft Docs
description: Work offline on your mobile device using the Power Apps mobile app.
author: mustlaz
ms.service: powerapps
ms.component: pa-user
ms.topic: quickstart
ms.date: 01/11/2022
ms.subservice: mobile
ms.author: mkaur
ms.custom: ""
ms.reviewer: ""
ms.assetid: 
search.audienceType: 
  - enduser
search.app: 
  - PowerApps
  - D365CE
---

# Set up and use mobile offline-first (preview)

[This topic is pre-release documentation and is subject to change.]

This topic covers the new mobile offline-first set up and user experience. Once [offline is enabled](setup-mobile-offline.md) for your model-driven app, you can run it on of the following mobile apps:

- [Power Apps mobile](run-powerapps-on-mobile.md)
- [Dynamics 365 for Phones and Tablets](/dynamics365/mobile-app/overview)
- [Field Service (Dynamics 365) mobile app](/dynamics365/field-service/mobile-2020-power-platform)

Depending on the app that you setup and use, your offline experience may be different. 


## Offline-first vs. classic offline

With the new offline-first experience, it's important to understand the key benefits of the new offline-first experience vs. the [classic offline experience](/dynamics365/mobile-app/work-in-offline-mode). 



|Offline-first| Classic offline  |
|---------|---------|
| <ol><li>Your data is always the same regardless of your network connection. </lo> <div></div> <div></div> ![Offline-first on mobile.](media/offline-first-classic-3.png) <li> There's no toggle for users to switch from offline to online mode. A user will never forget to sync their changes back to the server because the app will do it automatically. <div></div> ![Sync data back to server.](media/offline-first-classic-4.png) </li>     |   <ol> <li> Users have the option to skip the initial offline sync and stay online, which means users in your organization won't have the same experience. <div></div> ![Skip download offline data.](media/offline-first-classic-1.png) </li> <li> The **Work in offline mode** toggle is something a user has to remember to disable in order to sync changes with the server. <div></div> ![User must turn off work offline toggle to synce data.](media/offline-first-classic-2.png) </li> <div></div> </li> <li> When there's no network, the rows are listed from the local database so they won't be the same when you connect back to the server. When you're editing and lose internet connection, your changes will be lost since you can't save changes in offline mode without connectivity. </li>  |


## Enable mobile offline-first

To use offline-first, you need to enable it for each of your model-driven apps. It's a separate app setting for each app.

1. Sign in to [Power Apps (preview)](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) 

2. On the left nav, select **Apps** and then select the model-driven app that you want enable for offline.

3. Select ... > **Edit** > **Edit in preview** to open the modern app designer.

    > [!div class="mx-imgBorder"]
    > ![Edit an app](media/offline-edit-app.png)
 
4. On the command bar, select **Settings**.

    > [!div class="mx-imgBorder"]
    > ![Select setting on the command bar](media/mobile-offline-image4.png)

5. On the **Upcoming** tab, set the **Disable classic offline** toggle to **On**.

6. Close the **Settings** dialog and then save and publish the app.


Some features such as dashboards, charts, multi-table business process flows, and server-side sync are only available when you're online. Be sure to validate your app and make sure that it's fully functional before it's deployed. 

## Use mobile offline-first

For the app to be available in offline mode, app and user data must be downloaded on your device. This process is called initial offline sync.
The app data includes all the resources needed for the app to run properly and user data that is configured for the offline profile and stored in Microsoft Dataverse tables.

With offline-first, during the initial offline sync, you'll get a notification stating that your app is syncing the offline data. This can take a few minutes or longer depending on what has been configured in the offline profile. If the initial offline sync hasn't completed, it'll be triggered every time the app is launched. Select **See details** to open the offline status page.

> [!div class="mx-imgBorder"]
> ![Offline status screen.](media/offline-first-1.png)

You can also select the **Offline status** button to see more information about sync progress.

> [!div class="mx-imgBorder"]
> ![See more information about sync process.](media/offline-first-2.png)

When the initial sync is complete, you can start using the app in offline mode.

> [!div class="mx-imgBorder"]
> ![Offline status completed.](media/offline-first-3.png)











[!INCLUDE[footer-include](../includes/footer-banner.md)]
