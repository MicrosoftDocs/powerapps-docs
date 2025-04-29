---
title: Sync data offline in the background
description: Sync Power Apps data offline in the background.
ms.custom: 
ms.date: 05/29/2024
ms.reviewer: smurkute
ms.suite: 
ms.tgt_pltfrm: 
ms.topic: article
applies_to: 
caps.latest.revision: 1
ms.author: trdehove
author: trdehove
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Sync data offline in the background

For an app to be available in offline mode, the app and data must be downloaded, or synced to your device. 

Data can only be synced regularly when Power Apps or Field Service are running in the foreground of your device, with the screen unlocked. However, an ongoing sync can continue when the app is in the background or the screen is locked. Syncing data in this way depends on operating system capabilities which are different for iOS, Android, and Windows. 

## iOS devices

Sync happens when Power Apps (Player) is active and in the foreground. If Power Apps moves to the background, any ongoing sync pauses. Scheduled synchronizations don't start while the app is in the background.  

## Android devices

An ongoing sync starts only when Power Apps (Player) is in the foreground and active. Once synchronization starts, it continues even if Power Apps moves to the background, as long as the app stays open and active. However, scheduled synchronizations don't start while the app is in the background.  

## Windows devices

An ongoing sync can continue when Power Apps or Field Service is minimized or when the device is locked. 

The behavior on Windows depends on the **Let this app run in the background** setting.  

- If you're using Windows 10, see [Manage background activity for apps in Windows](https://support.microsoft.com/en-us/windows/manage-background-activity-for-apps-in-windows-4f32dffe-b97c-40e8-a790-3ca10373a1ef) for more information.

- If you're using Windows 11, complete the following steps:

  1. Go to **Settings** > **Apps** > **Installed apps**.  

  2. Next to **Power Apps** or **Field Service**, select the **More options** icon (three horizontal dots). Then select **Advanced options**.

  3. In the **Background apps permissions** area, go to the **Let this app run in the background** setting. Select **Power optimized (recommended)** from the list. 



