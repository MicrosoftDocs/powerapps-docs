---
title: View offline sync status
description: Learn how to interpret the offline sync icon in the mobile app navigation bar.
ms.date: 06/05/2023
ms.author: trdehove
author: trdehove
ms.reviewer: sericks
ms.topic: conceptual
ms.service: powerapps
ms.custom: bap-template
applies_to: Dynamics 365 apps
search.audienceType: 
  - enduser
---

# View offline sync status

The offline sync icon indicates the synchronization status of the Power Apps mobile app. At a glance, you can tell:

- Whether the app is connected to the network
- Whether a data refresh is in progress
- Whether updated data is waiting to sync
- Whether the app has experienced an error or warning while syncing

The offline sync icon is always visible in the main app navigation on iOS and Android devices.

:::image type="content" source="media/offline-sync-icon-small.png" alt-text="Screenshot of a mobile app, with the offline sync icon in the app navigation bar highlighted.":::

## Sync status icons

The offline sync icon changes based on the app's sync status. The following table describes the possible sync states and the icons associated with them.

| Icon | Description |
|------|--------------|
| ![Icon showing that the app is connected to the internet.](media/connected.png "Icon showing that the app is connected to the internet.")| The app is connected to the internet. |
| ![Icon showing that the app isn't connected to the internet.](media/not-connected.png "Icon showing that the app isn't connected to the internet.") | The app is not connected to the internet. |
| ![Icon showing that the app is syncing data.](media/synching.png "Icon showing that the app is syncing data.") | The app is syncing data. |
| ![Icon showing that the app has pending changes to upload.](media/upload-pending-changes.png "Icon showing that the app has pending changes to upload.") | The app has pending changes to upload. |
| ![Icon showing that the synchronization process encountered an error.](media/error.png "Icon showing that the synchronization process encountered an error.") | The synchronization process encountered an error. |
| ![Icon showing that the synchronization process encountered a warning.](media/warning.png "Icon showing that the synchronization process encountered a warning.") | The synchronization process encountered a warning. |

## Types of offline syncs
Data is synchronized from Dataverse to your device over the lifetime of your app using several synchronization modes.

- **First sync** - This sync is the initial offline sync that occurs for the Power Apps mobile app. All data in the offline profile is downloaded to the device. A user must use the Power Apps mobile app in online mode until the first sync is completed.

  The first sync, which is the longest sync, is triggered when you sign-in to the Power Apps mobile app. It is also triggered after using the Reconfigure action (not recommended).

- **Delta sync** - This sync is the fastest sync, and occurs regularly based on the offline configuration for the organization. For example, a delta sync could occur every five minutes. Only data that has changed since the last sync occurred is downloaded to the mobile device.

- **Full delta sync** - When you select **Refresh** on the **Device status** page, you trigger a full sync. A full sync doesn't redownload data, but it does recheck every record on the device, so it may take longer than a regular delta sync.

- **Grid sync** - If you select **Refresh** on a grid or calendar view, the app will immediately synchronize all tables visible in the view. When the sync is complete, the view will refresh automatically.

## Offline Status page

When you select the offline sync icon, the **Offline Status** page opens. The **Offline Status** page provides details such as what data was downloaded, whether there is data waiting to upload, and the amount of storage the app is using.

:::image type="content" source="media/OfflineStatusPage-NotConnected.png" alt-text="The Offline Status page of a mobile app.":::

## Notifications

On iOS and Android devices, app sync notifications are consistent across the different sync states.

## Known issues

- The first time the app syncs, the offline sync icon continues to spin until the user switches from online mode to offline mode.
- If the app has pending changes to upload, the number that's shown is the total of updated, added, and removed rows, files, and images.
