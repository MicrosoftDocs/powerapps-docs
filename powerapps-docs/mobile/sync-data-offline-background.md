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

For a model-driven app to be available in offline mode, the app and user data must be downloaded on your device. This process is called *initial offline sync*. The initial offline sync for model-driven apps can continue as Power Apps runs in the background, as long as the app is not closed.

The initial offline sync process that continues while Power Apps runs in the bacground relies on the operating system capabilites, which are different for iOS, Android, and Windows devices.

## iOS devices

The initial offline sync is limited on iOS devices.  The initial offline sync is suspended as soon as the Power Apps app runs in the background or when the device is locked. However, the operating system will continue the initial offline sync, for up to five minutes at a time, when the device is not in use.

The initiated sync is suspended as soon as the app is in the background or when the device is locked. However, the OS will continue the sync for up to 5 min at a time when the device is not used. This happens more frequently when the device is plugged in.

| Example scenarios | What happens to the synchronization process |
|-------------------------|-------------------------|
| <ol type="1"></br><li>Open Power Apps.</li></br><li>Leave the app open.</li></br><li>Screen locks.</li></br></ol> | If a sync is active while the screen is locked, the sync will be suspended and will resume in 15 minutes. |
| <ol type="1"></br><li>Open Power Apps.</li></br><li>Leave and go to another app.</li></br><li>Stop working on device, so the screen locks.</li></br></ol> | If a sync is active while the screen is locked, the sync will be suspended and will resume in 15 minutes. |
| <ol type="1"></br><li>Open Power Apps.</li></br><li>Continue working in Power Apps, so that the screen doesn't lock.</li></br></ol> | The synch will continue until it is complete.<br><br>New syncs can start while Power Apps is in use. |
| <ol type="1"></br><li>Open Power Apps.</li></br><li>Leave and go to another app.</li></br></ol> | Active sync will pause and not complete.<br><br>New syncs will not start. |

## Android devices

The initial offline sync can continue when Power Apps runs in the background or when the device is locked. 

## Windows devices
The initial offline sync can continue when Power Apps is minimized or when the device is locked. 

If the device is on power saving mode and running on the battery, the sync will run for ten minutes only. After the ten minutes, the sync will be suspended until the user maximizes the app.

The behavior on Windows devices depends on the **Let this app run in the background** setting. For more information, see [Manage background activity for apps in Windows](https://support.microsoft.com/en-us/windows/manage-background-activity-for-apps-in-windows-4f32dffe-b97c-40e8-a790-3ca10373a1ef). We recommend using the default **Power optimized** value.




