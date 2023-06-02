---
title: View offline sync status
description: Learn how to interpret the offline sync icon in the mobile app navigation bar.
ms.date: 06/02/2023
ms.author: sericks
author: sericks007
ms.reviewer: 
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

## Types of syncs
There are three different types of syncs that can occur on your mobile device.

- **First sync** - This sync is the initial sync that occurs on the mobile device. All data in the offline profile is downloaded to the device. A user can use the Power Apps mobile app in online mode until the sync is completed.

  The first sync, which is the longest sync, is triggered when you sign-in to the Power Apps mobile app.

- **Incremental delta sync** - This sync is the fastest sync, and occurs every 5 minutes. Only the data that has changed since the last sync is downloaded to the mobile device.

- **Full delta sync** - This sync checks all records for changes. Only new or updated data is downloaded to your mobile device. This type of sync runs slower for organizations with a high number of records.

  Users are free to use the Power Apps mobile app during the full delta sync. However, users must refresh a page (or navigate away from a page, and then come back to that page) to see updated data on the page. 

## Offline Status page

When you select the offline sync icon, the **Offline Status** page opens. The **Offline Status** page provides details such as what data was downloaded, whether there is data waiting to upload, and the amount of storage the app is using.

:::image type="content" source="media/OfflineStatusPage-NotConnected.png" alt-text="The Offline Status page of a mobile app.":::

## Notifications

On iOS and Android devices, app sync notifications are consistent across the different sync states.

## Known issues

- The first time the app syncs, the offline sync icon continues to spin until the user switches from online mode to offline mode.
- If the app has pending changes to upload, the number that's shown is the total of updated, added, and removed rows, files, and images.
