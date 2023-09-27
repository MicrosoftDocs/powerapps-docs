---
title: Configure model-driven apps for offline (preview)| Microsoft Docs
description: Configure model-driven apps for offline mode (preview).
author: trdehove

ms.component: pa-user
ms.topic: quickstart
ms.date: 02/01/2022
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

# Mobile offline overview (preview)

[This topic is pre-release documentation and is subject to change.]

Wouldn't it be great to use your mobile app without worrying about spotty internet connectivity? With model-driven apps made with Power Apps and the new mobile offline-first experience, it's possible. People who need to work from remote locations can continue to work seamlessly without worrying about their internet connection.

With the new mobile offline experience enabled for your model-driven apps, not only can you continue working in offline mode, you'll also have better device performance, a more responsive app, and less drain on the battery because fewer connections are being made to the server.

Note, an internet connection is required to sync data between your mobile device and Microsoft Dataverse.

To get started with mobile offline, an app maker needs to enable and define the tables that are available for offline by using the [modern app designer](../maker/model-driven-apps/app-designer-overview.md). For more information, go to [Set up mobile offline](setup-mobile-offline.md).

> [!IMPORTANT] 
> The mobile offline experience for canvas apps is in Preview.

## Mobile offline-first

After offline is configured, anyone who uses the [Power Apps mobile app](run-powerapps-on-mobile.md) can also use the app in offline mode. The Power Apps mobile app always runs offline-first, either with or without an internet connection. This new functionality optimizes offline performance and creates a consistent experience for users as they change locations:

-	**Online**: Occurs when an internet connection is available, but offline mode isn't set up. The mobile app functions similar to using the app with an internet connection on your PC. When the internet connection is lost, the mobile app is unusable. Not recommended.
-	**Offline-first without an internet connection**: Data is downloaded, and all changes are saved to your mobile device. When the internet connection is restored, the changes are automatically synced to the server.
- **Offline-first with an internet connection**: Data is downloaded to the device, and all changes are saved locally. Because there's an internet connection, the app will automatically attempt to sync every few minutes.

For more information, go to [Set up and use mobile offline-first](work-in-offline-mode.md).

> [!IMPORTANT] 
> - For information about the mobile offline setup exerience that is generally available, go to [Mobile offline overview (classic)](mobile-offline-overview-classic.md).
> - For more information about how to set up mobile offline for canvas apps, go to [Develop offline-capable canvas apps](../maker/canvas-apps/offline-apps.md)
> - The offline-first experience is in general availability for Field Service mobile app. For more information, see [Field Service (Dynamics 365) mobile app](/dynamics365/field-service/mobile-2020-power-platform).








