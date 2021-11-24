---
title: Work offline on your mobile device using the Power Apps mobile app (preview) | Microsoft Docs
description: Work offline on your mobile device using the Power Apps mobile app.
author: mustlaz
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
  - enduser
search.app: 
  - PowerApps
  - D365CE
---

# Work offline mode on your mobile device (preview)

Use Power Apps mobile in offline mode when you don't have internet access. Once the initial sync is finished, the app can be used offline. While it is transparent with offline-first, the user must handle offline explicitly when in classic offline.

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



> [!IMPORTANT]
> The [Work offline on your mobile device](/dynamics365/mobile-app/work-in-offline-mode) topic covers how to work in offline for both Power Apps mobile and the Dynamics 365 phones and tablet app. The process is the same for both apps. 




[!INCLUDE[footer-include](../includes/footer-banner.md)]
