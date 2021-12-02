---
title: Configure model-driven apps for offline (preview)| Microsoft Docs
description: Configure model-driven apps for offline (preview).
author: mduelae
ms.service: powerapps
ms.component: pa-user
ms.topic: quickstart
ms.date: 11/29/2021
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

# Mobile offline overview (preview)

[This topic is pre-release documentation and is subject to change.]

Wouldn't it be great to use your mobile app without worrying about spotty internet connection? With model-driven Power Apps and the new mobile offline-first experience, its possible. People that need to work from remote locations can continue to work seamlessly without worrying connectivity. 

When model-driven apps are enabled for mobile offline, not only can you continue doing your work, you'll also have better device performance, a more responsive app, and it will save battery power with fewer connections made to the server. 

Note, internet connection is required to sync data between your mobile device and Microsoft Dataverse.

To get started with mobile offline, an app maker will need to enable and define the tables that are available for offline using the [modern app designer](../maker/model-driven-apps/app-designer-overview.md). For more information, see [Set up mobile offline](setup-mobile-offline.md)


## Mobile offline-first

Once offline is configured anyone that uses [Power Apps mobile](run-powerapps-on-mobile.md) can also use the app in offline mode. Power Apps mobile always runs offline-first, both with and without internet connection. This functionality optimizes performance and creates a consistent experience for users as they move through areas with and without internet connection. 

1.	**Online**: Occurs when there is internet but and offline isn't set up. When internet is lost, the mobile app is unusable. Not recommended.
2.	**Offline-first without internet connection**: Data is downloaded to the device and all changes are saved locally to your mobile device. When internet is restored, the changes are automatically synced to the server.
3. **Offline-first with internet connection**: Data is downloaded to the device and all changes are saved locally; but because there is internet connection the app will automatically attempt to sync every few minutes.

For more information, see [Set up and use mobile offline-first](work-in-offline-mode.md).

> [!IMPORTANT] 
>   - For information about the classic mobile offline set up, see [Configure mobile offline synchronization](/dynamics365/mobile-app/setup-mobile-offline).
>   - For more information on how to set up mobile offline for canvas apps, see [Develop offline-capable canvas apps](../maker/canvas-apps/offline-apps.md)
>   - For information on how to use the Field Service mobile app using offline-first, see [Field Service (Dynamics 365) mobile app](/dynamics365/field-service/mobile-2020-power-platform).








