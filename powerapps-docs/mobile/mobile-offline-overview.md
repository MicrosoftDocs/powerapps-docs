---
title: Configure model-driven apps for offline (preview)| Microsoft Docs
description: Configure model-driven apps for offline (preview).
author: mduelae
ms.service: powerapps
ms.component: pa-user
ms.topic: quickstart
ms.date: 11/23/2021
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
searchScope:
  - "Power Apps"
---

# Overview of mobile offline (preview)

Wouldn't it be great to use your mobile app without worrying about a spotty internet connection? With model-driven Power Apps, it's possiable. People that need to work from remote locations can continue to work seamlessly without worrying connectivity. 

When model-driven apps are enabled for mobile offline, not only can you continue doing your work, you'll also have better device performance, a more resonsive app, and it'll save battery power with less connections made to the server. 

Note, internet connection is required to sync data between your mobile device and Microsoft Dataverse.

To get started with mobile offline, an app maker will need to enable and define the tables that will be available for offline use in Dataverse. For more information, see [Set up mobile offline](setup-mobile-offline.md)



## Understanding offline vs. online capabilities

Once an offline is configured any users that use access to the app can also use it in offline mode. The Power Apps mobile always runs offline-first, both with and without internet connection. This functionality optimizes performance and creates a consistent experience for users as they move through areas with and without internet connection. 

1.	**Online**: Occurs when there is internet but and offline isn't set up. When internet is lost or diminished, the mobile app is unusable. Not recommended.
2.	**Offline First without internet connection**: Data is downloaded to the device and all changes are saved locally to your mobile device. When internet is restored, the changes are synced to the server.
3. **Offline First with internet connection**: Data is downloaded to the device and all changes are saved locally; but because there is internet connection, the user can manually sync to receive the latest data from the server (like a new booking). The app will also automatically attempt to sync every few minutes. For more information, see [sync filters](#sync-intervals) in this article.

In summary, an offline-first application will always read from the local device database and will only leverage an active internet connection during the synchronization process. This makes it important that your offline profile is configured to sync all data to the device that the frontline worker requires during their working hours.


Then the app will automatically sync data between your device and the server. For more information, see [Set up mobile offline](setup-mobile-offline.md)

Run all your model-driven apps on [Power Apps mobile](run-powerapps-on-mobile) including customer engagement apps (such as [Dynamics 365 Sales](/dynamics365/sales-professional/help-hub.md), [Dynamics 365 Customer Service](/dynamics365/customer-service/help-hub.md), and [Dynamics 365 Marketing](/dynamics365/marketing/help-hub.md)). 




> [!IMPORTANT]
> This topic covers the new offline set up experience using the [modern app designer](../maker/model-driven-apps/create-model-driven-app) and the new [offline first experience](link TBD).
>   - The new experience also works with [Dynamics 365 for Phones and Tablets](/dynamics365/mobile-app/overview) and [Field Service (Dynamics 365) mobile app](/dynamics365/field-service/mobile-2020-power-platform). 
>   For information about the current  mobile offline set up (which will become the previous experience), see  [Configure mobile offline synchronization](/dynamics365/mobile-app/setup-mobile-offline).
>   - For more information on how to set up mobile offline for canvas apps, see [Develop offline-capable canvas apps](../maker/canvas-apps/offline-apps.md).








