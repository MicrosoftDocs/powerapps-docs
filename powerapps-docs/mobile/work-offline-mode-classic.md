---
title: Work with model-driven apps offline (classic mode)
description: Learn how to work on your mobile device in offline mode
ms.custom: 
ms.date: 05/06/2024
ms.reviewer: smurkute
ms.suite: 
ms.tgt_pltfrm: 
ms.topic: how-to
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

# Work with model-driven apps offline (classic mode)

You can work with your data even when you don't have internet access by using the app in offline mode. The mobile app provides a rich offline experience that lets you work with commands like create, read, update, and delete, so you always stay productive. After you're back online, changes are synchronized with your apps in the Microsoft Dataverse environment.

If you're working on a record and lose your network connection, any updates made to the record are saved in offline mode and will be synchronized to the app after you're back online. When the record is synchronized with the app, it uses the filters, added on the table in the offline profile, for availability in offline mode.

## Download updates to work in offline mode

When your admin [enables mobile offline classic mode](setup-mobile-offline.md#enable-mobile-offline-classic), you are prompted to download offline updates. After downloading the updates, you can start using the app on your mobile device in offline mode.

When you see the dialog box that asks you to download updates to work offline, select **Download**.

:::image type="content" source="media/mobile-offline-classic-prompt.png" alt-text="Download updates on your mobile device for mobile offline.":::

Offline data starts downloading as you continue to use the app. Data is downloaded while the app is active, so keep your phone unlocked with the app visible until the initial download is complete. The data can be [downloaded in the background](sync-data-offline-background.md) depending on the platform you use.  

## Download offline data later

If you don't want to download offline data and select **Skip for now**, you can't use the app in offline mode until you manually download the updates.

1. On the screen, select the **offline sync** (globe) icon.

1. On the **Device Status** page, select **Download offline updates**.

1. The download starts, and the status changes to **Initializing**.

1. When the download of offline data is complete, you get a notification that you can start working in offline mode.

## See whether offline mode is available

When offline updates are complete, you can check to see whether mobile offline mode is available. On the home screen, select the **offline sync** (globe) icon and check on the [Device Status page](offline-sync-icon.md).
  
## Work in offline mode

After the offline download is complete, you can use the mobile app in offline mode.

When you have no connectivity, you automatically have access to the downloaded data so you can continue working while you're on the go. The data automatically syncs with the server as soon as connectivity is restored.

When you have intermittent connectivity, we recommend that you switch to offline mode. As long as offline mode is turned on, the updates you make on your device aren't synced with the server and you can continue working with the local data on your device. To push the changes made to the server and refresh your local data, turn off the **Work in offline mode** toggle.

To work in offline mode, complete the following steps:

1. On the screen, select the **offline sync** (globe) icon.

2. Turn on the **Work in offline mode** toggle.

[!INCLUDE[footer-include](../includes/footer-banner.md)]
