---
title: Work offline on your mobile device using the Power Apps mobile app (preview) | Microsoft Docs
description: Work offline on your mobile device using the Power Apps mobile app.
author: mustlaz
ms.service: powerapps
ms.component: pa-user
ms.topic: quickstart
ms.date: 11/24/2021
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

# Offline-first (preview)

This topic covers the new offline-first user experience. Once [offline is enabled](setup-mobile-offline.md) for your model-driven app, you can run it one of the following mobile apps:

- [Power Apps mobile](run-powerapps-on-mobile)
- [Dynamics 365 for Phones and Tablets](/dynamics365/mobile-app/overview)
- [Field Service (Dynamics 365) mobile app](/dynamics365/field-service/mobile-2020-power-platform)

Depending on the app you’re using and your set up, your offline experience may be different. 


## Offline-first vs. classic offline

With the new offline-first experience it's important to understand the key benifits of the new vs. the [classic offline experience](/dynamics365/mobile-app/work-in-offline-mode). 


**Classic offline with internet connection**

Users have the options to skip the initial offline sync and stay online which means user in your organization won't have the same experiences.


|Offline-first| Classic offline  |
|---------|---------|
| <ol><li>Your data is always the same regardless of your network connection </lo> <div></div> <div></div> !![Download offline data.](media/offline-first-classic-1.png)     |   <ol> <li> Users have the options to skip the initial offline sync and stay online which means user in your organization won't have the same experiences. <div></div> ![Download offline data.](media/offline-first-classic-1.png) </li> <li> The Work in offline mode toggle is something a user has to remember to disable to sync back all your changes with the server. <div></div> ![Download offline data.](media/offline-first-classic-2.png) </li> <div></div> <div></div>  ![The app-selector menu](media/app-selector2.png "The app-selector menu")   |



ser  listed from the server but if connection is lost while editing an online mode the row and suddenly losing connection. In that case, I may lose all my changes if I try to save them while not having connection

1. **Offline-first**: Your data is always the same regardless of your network connection. Th
 

For your app to be available offline, it needs to download the app and user data on the device first. This process is called initial offline sync.
The app data includes all the resources needed for the app to run properly and the user data configured in the offline profile and stored in Microsoft Dataverse tables.

With offline-first, during the initial offline sync, you'll get a notification stating that your app is syncing the offline data. This can take a few minutes or even more depending on what has been configured in the offline profile. The initial offline sync is triggered everything when the app is launched. Select **See details** to open the offline status page.

> [!div class="mx-imgBorder"]
> ![Initail offline sync.](media/offline-first-1.png)


You can also select the **Offline status** button to see more information about sync progress.

> [!div class="mx-imgBorder"]
> ![Offline status screen.](media/offline-first-2.png)


When the sync is complete, you can start using your application offline. Depending on the sync intervals set up in the offline profile, all subsequent syncs will happen automatically.


> [!div class="mx-imgBorder"]
> ![Offline status completed.](media/offline-first-3.png)




 
 
 
 
 
 
 
 
 
 
 
 This is the new preview experience.
2. **Class offline**: This is the [currect released offline experience](/dynamics365/mobile-app/work-in-offline-mode).





                                                                                             |
 User see records listed from the server and may be facing weird situations like editing an online record and suddenly losing connection. In that case, I may lose all my changes if I try to save them while not having connection.
 
 When no network available, the records are listed from the local database and hence wouldn't be the same as when connected to the network. | With Offline-first, my data is always the same regardless of my network connectivity and relies on my offline profile setup. |

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







[!INCLUDE[footer-include](../includes/footer-banner.md)]
