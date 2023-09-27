---
title: Sync data in the background
description: Sync Power Apps data offline in the background.
ms.custom: 
ms.date: 11/10/2022
ms.reviewer: sericks
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

For a model-driven app to be available in offline mode, the app and data must be downloaded, or synced to your device. 

Data can only be synced regularly when Power Apps or Field Service are running in the foreground of your device, with the screen unlocked. However, an ongoing sync can continue when the app is in the background or the screen is locked. Syncing data in this way depends on operating system capabilities which are different for iOS, Android, and Windows. 

## iOS devices

On devices running iOS 13.0 or later, an ongoing sync is suspended as soon as Power Apps or Field Service are moved to the background or when the device is locked. The ongoing sync may be resumed and completed while the app is in the background using native iOS functionality. 

The operating system prioritizes background activities, such as the ongoing sync, based on app usage, connectivity, and power state. Ongoing syncs are more likely to be completed in the background if Power Apps or Field Service have been used frequently on the device and when the device is plugged in. 

If a user has a large amount of data to sync, we recommend opening the app while the device is charging to increase priority of the sync. 

## Android devices

An ongoing sync can continue when Power Apps or Field Service runs in the background or when the device is locked. The user will see a notification in the Android notification center that says, “The app is downloading records so that they are accessible offline.” 

## Windows devices

An ongoing sync can continue when Power Apps or Field Service is minimized or when the device is locked. 

The behavior on Windows depends on the **Let this app run in the background** setting.  

- If you're using Windows 10, see [Manage background activity for apps in Windows](https://support.microsoft.com/en-us/windows/manage-background-activity-for-apps-in-windows-4f32dffe-b97c-40e8-a790-3ca10373a1ef) for more information.
- If you're using Windows 11, complete the following steps:

  1. Go to **Settings > Apps > Installed apps**.  
  2. Next to **Power Apps** or **Field Service**, select the **More options** icon (three horizontal dots). Then select **Advanced options**.
  3. In the **Background apps permissions** area, go to the **Let this app run in the background** setting. Select **Power optimized (recommended)** from the list shown. 



