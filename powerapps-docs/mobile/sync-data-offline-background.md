---
title: Sync data offline in the background
description: Sync Power Apps data offline in the background.
ms.custom: 
ms.date: 06/24/2025
ms.reviewer: smurkute
ms.suite: 
ms.tgt_pltfrm: 
ms.topic: article
applies_to: 
caps.latest.revision: 1
ms.author: murugeshs
author: Murugesh1985
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Sync data offline in the background

To use an app in offline mode, download the app and sync data to your device.

You can sync data reliably only when the Power Apps mobile app or Field Service app is open, running in the foreground, and your device screen is unlocked. Learn more about sync behavior in [Work with canvas apps offline](canvas-mobile-offline-working.md).

The background sync behavior on Windows depends on the **Let this app run in the background** setting.  

- If you're using Windows 10, see [Manage background activity for apps in Windows](https://support.microsoft.com/en-us/windows/manage-background-activity-for-apps-in-windows-4f32dffe-b97c-40e8-a790-3ca10373a1ef) for more information.

- If you're using Windows 11, complete the following steps:

  1. Go to **Settings** > **Apps** > **Installed apps**.  

  2. Next to **Power Apps** or **Field Service**, select the **More options** icon (three horizontal dots). Then select **Advanced options**.

  3. In the **Background apps permissions** area, go to the **Let this app run in the background** setting. Select **Power optimized (recommended)** from the list. 