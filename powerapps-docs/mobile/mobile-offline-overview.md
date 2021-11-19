---
title: Configure model-driven apps for offline (preview)| Microsoft Docs
description: Configure model-driven apps for offline (preview).
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
  - enduser
search.app: 
  - PowerApps
  - D365CE
searchScope:
  - "Power Apps"
---

# Overview of mobile offline (preview)

Wouldn't it be great to be able to use apps on your mobile device without worrying about spotty connectivity? With Power Apps mobile this is possiable. Users that need to work from remote locations can continue working seemlessly without internet connection. 


Enable your mobile applications so that it's available while offline not only solves this problem but also comes with additional benefits like providing a more responsive, performant experience or saving the device's battery with less connections made to the server.

Model-driven applications can be enabled for offline use, so they become always available regardless of the network connectivity. This feature is available through Power Apps and Dynamics (Field Service, Sales) mobile applications.

Internet connections remain needed to sync back and forth data to Dataverse as well as for online-only scenarios.

Through the offline profile, the app maker can define the data (tables in Dataverse) needed offline and then the application will automatically keep it in sync between the device and the server.

The following documentation describes the new offline configuration setup available in the modern app designer as well as offline-first available in preview now.


> [!IMPORTANT]
> - For documentation about the offline experience currently generally available, please refer to,  [Configure mobile offline synchronization](/dynamics365/mobile-app/preview-setup-mobile-offline).
> - For more information on how to set up mobile offline for canvas apps, see [Develop offline-capable canvas apps](../maker/canvas-apps/offline-apps.md).

## Default roles setup for offline applications

-   The **environment maker, system customizer or system administrator** role is needed to configure offline for model driven apps. These roles have create/read/write/delete and share access on the "mobile offline profile" table.

-   Users with the **basic user** role can open and use an offline application. This role has the read access to the "mobile offline profile" table.

If you need to use a custom security role, you may want to edit it accordingly:

*Edit your security role &gt; Core Records tab &gt; Mobile Offline profile*

![A picture containing calendar Description automatically generated](media/image1.png)


