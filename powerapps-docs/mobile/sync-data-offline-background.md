---
title: Sync Power Apps data offline in the background
description: Sync Power Apps data offline in the background.
ms.custom: 
ms.date: 11/03/2022
ms.reviewer: 
ms.suite: 
ms.tgt_pltfrm: 
ms.topic: article
applies_to: 
caps.latest.revision: 1
ms.author: sericks
author: sericks007
manager: tapanm-MSFT
search.audienceType: 
  - admin
  - customizer
  - enduser
search.app: 
  - D365CE
  - D365Sales
---

# Sync Power Apps data offline in the background

The offline synchronization process continues in the background as long as the app is not closed. The synchronization in the background relies on the OS capabilities which are different between iOS, Android, and Windows.

The following table provides details about the initial sync for each type of device.

|     &nbsp;                             | iOS | Android | Windows | 
|----------------------------------------|-----|----------|------------|
| **Sync continues in the background**   | Limited | Full  | Full (following the **Let this app run in the background** setting) |
| **Details**                            | The initiated sync is suspended as soon as the app is in the background or when the device is locked. However, the OS will continue the sync for up to 5 min at a time when the device is not used. This happens more frequently when the device is plugged in. | The initiated sync continues when the app is in the background or when the device is locked. | The initiated sync continues when the app is minimized or when the device is locked. If the device is on power saving mode and running on battery, the sync will run for 10 minutes only, then suspended until the user unminimizes the app.<br><br>The behavior on Windows depends on the **Let this app run in the background** setting. For more information, see [Manage background activity for apps in Windows](https://support.microsoft.com/en-us/windows/manage-background-activity-for-apps-in-windows-4f32dffe-b97c-40e8-a790-3ca10373a1ef). We recommend using the default **Power optimized** value.|



