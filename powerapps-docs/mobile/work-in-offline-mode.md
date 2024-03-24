---

title: Work offline on your mobile device (offline-first mode)
description: Learn how to work offline on your mobile device.
author: trdehove
ms.component: pa-user
ms.topic: quickstart
ms.date: 10/26/2023
ms.subservice: mobile
ms.author: trdehove
ms.custom: ""
ms.reviewer: sericks
ms.assetid: 
search.audienceType: 
  - enduser
---

# Work offline on your mobile device (offline-first mode)

For a model-driven app to be available in offline mode, app and user data must be downloaded on your device. This process is called *initial offline sync*.

The app data includes all the resources needed for the app to run properly. User data includes data configured for the offline profile and stored in Microsoft Dataverse tables.

During the initial offline sync, you receive a notification stating that your app is syncing the offline data with the number of rows downloaded. The notification also indicates how much disk space is used. The initial offline sync can take a few minutes or longer, depending on what is configured in the offline profile. If the initial offline sync isn't complete, it triggers every time the app is opened. You also get the same notification when you resume the app after a long period of inactivity.

:::image type="content" source="media/mobile-offline-first-notification-1.png" alt-text="Offline status screen.":::

For more information about offline sync status, see [offline sync icon](offline-sync-icon.md).

:::image type="content" source="media/mobile-offline-device-status-page.png" alt-text="See more information about the sync process.":::

When the initial sync is complete, you can start using the app in offline mode.

When you refresh your data on a grid view, you get notification stating, **Updating data...**.

:::image type="content" source="media/mobile-offline-first-update-notification.png" alt-text="Refreshing offline status.":::

[!INCLUDE[footer-include](../includes/footer-banner.md)]
