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

To use an app in offline mode, download the app and sync data to your device.

Data can only be synced reliably when the Power Apps mobile app or Field Service app is running in the foreground of your device, with the screen unlocked. However, an ongoing sync can continue when the app is in the background or when the screen is locked depending on the operating system’s capabilities.

## Android devices

An ongoing sync starts only when the Power Apps mobile app is in the foreground and open. Once sync starts, it continues even if the Power Apps mobile app is moved to the background, provided the app remains open. However, scheduled syncs don't start while the Power Apps mobile app is in the background.

## iOS devices

An ongoing sync starts only when the Power Apps mobile app is in the foreground and open. If the Power Apps mobile app is moved to the background, the ongoing sync is paused, and scheduled syncs don't start. 

## Windows devices

An ongoing sync can continue when Power Apps or Field Service is minimized or when the device is locked. 

The behavior on Windows depends on the **Let this app run in the background** setting.  

- If you're using Windows 10, see [Manage background activity for apps in Windows](https://support.microsoft.com/en-us/windows/manage-background-activity-for-apps-in-windows-4f32dffe-b97c-40e8-a790-3ca10373a1ef) for more information.

- If you're using Windows 11, complete the following steps:

  1. Go to **Settings** > **Apps** > **Installed apps**.  

  2. Next to **Power Apps** or **Field Service**, select the **More options** icon (three horizontal dots). Then select **Advanced options**.

  3. In the **Background apps permissions** area, go to the **Let this app run in the background** setting. Select **Power optimized (recommended)** from the list. 



