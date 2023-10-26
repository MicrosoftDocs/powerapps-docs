---
title: Work offline on your mobile device (classic mode)
description: How to work on your mobile device in offline mode
ms.custom: 
ms.date: 10/26/2023
ms.reviewer: sericks
ms.suite: 
ms.tgt_pltfrm: 
ms.topic: article
applies_to: Dynamics 365 apps
ms.assetid: 6828238b-1645-4710-a192-0014acb03196
caps.latest.revision: 97
ms.author: trdehove
author: trdehove
search.audienceType: 
  - admin
  - customizer
  - enduser
---

# Work offline on your mobile device (classic mode)

You can work with your data in offline mode even when you don't have internet access. The mobile app provides a rich offline experience that lets you work with commands like create, read, update, and delete, along with some special commands, so you always stay productive. After you're back online, changes you've made are synchronized with your apps in the Microsoft Dataverse environment.

If you're working on a record and lose your network connection, any updates made to the record are saved in offline mode and will be synchronized to the app after you're back online. When the record is synchronized with the app, it follows the filter rule for availability in offline mode.

## Download updates to work in offline mode

After you've installed the mobile app and your admin has [enabled mobile offline classic mode](setup-mobile-offline.md#enable-mobile-offline-classic), the next time you access the mobile app, you'll be prompted to download offline updates. After you download the updates, you can start using the mobile app in offline mode.

When you see the dialog box that asks you to download updates to work offline, select **Download**. 

:::image type="content" source="media/mobile-offline-classic-prompt.png" alt-text="Download updates on your mobile device for mobile offline.":::

Offline data starts downloading as you continue to use the app. Data is downloaded while the app is active, so keep your phone unlocked with the app visible until the initial download is complete. The data can be [downloaded in the background](sync-data-offline-background.md) depending on the platform you use.  

## Download offline data later

If you didn't want to download offline data and selected **Skip for now**, you won't be able to use the app in offline mode until you manually download the updates.

1. On the screen, select the **Globe** icon.

1. On the **Device Status** page, select **Download offline updates**.

1. The download will start, and the status will change to **Initializing**.

1. When the download of offline data is complete, you'll get a notification that you can start working in offline mode.

## See whether offline mode is available

When offline updates are complete, you can check to see whether mobile offline mode is available. On the home screen, select the **Globe** icon and check on the [Device Status page](offline-sync-icon.md)
  
## Work in offline mode

After the offline download is complete, you can use the mobile app in offline mode.

When you have no connectivity, you'll automatically have access to the downloaded data so you can continue working while you're on the go. The data will be automatically synced with the server as soon as connectivity is restored.

When you have intermittent connectivity, we recommend that you switch to offline mode. As long as offline mode is turned on, the updates that you make on your device won't be synced with the server and you can continue to work with the local data on your device. To push the changes you've made to the server and refresh your local data, turn off the **Work in offline mode** toggle.

**To work in offline mode**

1. On the screen, select the **Globe** icon.

2. Turn on the **Work in offline mode** toggle.

[!INCLUDE[footer-include](../includes/footer-banner.md)]
