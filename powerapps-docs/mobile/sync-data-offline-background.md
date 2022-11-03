---
title: Sync Power Apps data offline in the background
description: Sync Power Apps data offline in the background.
ms.custom: 
ms.date: 11/02/2022
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
| **Sync continues in the background**   | Limited | Full  | Full (following the **Power Saving** setting) |
| **Details**                            | The initiated sync is suspended as soon as the app is in the background or when the device is locked. However, the OS will continue the sync for up to 5 min at a time when the device is not used. This happens more frequently when the device is plugged in. | The initiated sync continues when the app is in the background or when the device is locked. | The initiated sync continues when the app is minimized or when the device is locked. If the device is on power saving mode and running on battery, the sync will run for 10 minutes only, then suspended until the user unminimizes the app. 
The behavior on Windows depends on the app setting (learn more -> Manage background activity for apps in Windows (microsoft.com). We recommend using the default “Power optimized” value.|



