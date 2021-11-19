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

Wouldn't it be great to use your mobile app without worrying about spotty connectivity? With model-driven Power Apps this is possiable. People that need to work from remote locations can continue to work seemlessly without internet connection. 

When you enable model-driven apps to work in offline mode, it also has additional benefits such as better device performance, the app is more resonsive, and saves your battery with less connections made to the server. However, you do need nternet connections to sync your data back and forth with Microsoft Dataverse.

> [!IMPORTANT]
> This topic covers the new offline set up experience using the [modern app designer](../maker/model-driven-apps/create-model-driven-app) and the [offline first experience](link TBD).
>   - For information about the current (which will become the previous experience) mobile offline set up, see  [Configure mobile offline synchronization](/dynamics365/mobile-app/setup-mobile-offline).
>   - For more information on how to set up mobile offline for canvas apps, see [Develop offline-capable canvas apps](../maker/canvas-apps/offline-apps.md).

You can an enable any of your model-driven apps for offline and run them on [Power Apps mobile](run-powerapps-on-mobile), [Dynamics 365 for Phones and Tablets](/dynamics365/mobile-app/overview), and [Field Service (Dynamics 365) mobile app](/dynamics365/field-service/mobile-2020-power-platform). 

To get started with mobile offline, an app maker will need to define the tables in Dataverse for offline so the app can automatically keep it in sync between the device and the server.


## Default roles setup for offline applications

-   The **environment maker, system customizer or system administrator** role is needed to configure offline for model driven apps. These roles have create/read/write/delete and share access on the "mobile offline profile" table.

-   Users with the **basic user** role can open and use an offline application. This role has the read access to the "mobile offline profile" table.

If you need to use a custom security role, you may want to edit it accordingly:

*Edit your security role &gt; Core Records tab &gt; Mobile Offline profile*

![A picture containing calendar Description automatically generated](media/image1.png)


