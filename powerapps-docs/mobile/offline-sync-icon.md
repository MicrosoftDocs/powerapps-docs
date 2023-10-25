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
| ![Icon showing that the app isn't connected to the internet.](media/not-connected.png "Icon showing that the app isn't connected to the internet.") | The app isn't connected to the internet. |
| ![Icon showing that the app is syncing data.](media/synching.png "Icon showing that the app is syncing data.") | The app is syncing data. |
| ![Icon showing that the app has pending changes to upload.](media/upload-pending-changes.png "Icon showing that the app has pending changes to upload.") | The app has pending changes to upload. |
| ![Icon showing that the synchronization process encountered an error.](media/error.png "Icon showing that the synchronization process encountered an error.") | The synchronization process encountered an error. |
| ![Icon showing that the synchronization process encountered a warning.](media/warning.png "Icon showing that the synchronization process encountered a warning.") | The synchronization process encountered a warning. |

## Types of offline syncs
Data is synchronized from Dataverse to your device over the lifetime of your app using several synchronization modes.

- **First sync**: This sync is the initial offline sync that occurs for the Power Apps mobile app. All data in the offline profile is downloaded to the device. A user must use the Power Apps mobile app in online mode until the first sync is completed.

  The first sync, which is the longest sync, is triggered when you sign in to the Power Apps mobile app. It's also triggered after using the Reconfigure action (not recommended).

- **Delta sync**: This sync is the fastest sync and occurs regularly based on the offline configuration for the organization. For example, a delta sync could occur every five minutes. Only data that has changed since the last sync is downloaded to the mobile device.

- **Full delta sync**: When you select **Refresh** on the **Device status** page, you trigger a full sync. A full sync doesn't redownload data, but it does recheck every record on the device, so it may take longer than a regular delta sync.

- **Grid sync**: If you select **Refresh** on a grid or calendar view, the app immediately synchronizes all tables visible in the view. When the sync is complete, the view refreshes automatically.

## Device Status page

When you select the offline sync icon, the **Device Status** page opens. The **Device Status** page provides details such as what data was downloaded, whether data is waiting to be uploaded, and the amount of storage the app uses.

The **Sync Status** tracks the offline status of the whole app and also the status of each individual entity. When the status appears as **Available**, offline mode is available and data has been synced successfully.
   > [!NOTE]
   > The status here can be **Not Available** due to an error or if you missed downloading offline updates. If the status is **Not Available** due to missing the latest offline updates, try downloading the updates again.

You can use the **Device Status** page to see the number of files and images to be downloaded and the current progress.

- The number of images is listed for the **Image Descriptor** table.
- The number of files are listed for each table in the **files available** section.

## Offline sync settings 
If your admin [enabled sync settings](setup-mobile-offline.md#define-sync-settings-on-mobile) for the app, you can control when offline synchronizations are triggered. 
  - Set the **Wi-Fi** setting to **On** to sync your data only when the device is connected to a Wi-Fi network. Enable this setting when you need to save your data plan or your battery, especially if you are in a low network area.
  - Change the sync interval value from the **Auto sync** setting if you want to sync less frequently. You can keep the default value by selecting **"Auto"**, or you can pick a longer interval that meets your needs. If you choose **"Manual"**, the sync only happens when you clik on the **Check for updates** button in the** Device Status** page. This setting only applies to changes coming from the server - when you change data in the app, it is immediately synchronized as soon as you have network.  
 
:::image type="content" source="media/mobile-offline-sync-settings.png" alt-text="The Offline Status page of a mobile app showing the sync settings.":::
## Notifications

On iOS and Android devices, app sync notifications are consistent across the different sync states.

## Known issues

- The first time the app syncs, the offline sync icon continues to spin until the user switches from online mode to offline mode.
- If the app has pending changes to upload, the number that's shown is the total of updated, added, and removed rows, files, and images.
