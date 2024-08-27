---
title: View offline sync status
description: Learn how to interpret the offline sync icon in the mobile app navigation bar.
ms.date: 06/06/2023
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

The  **offline sync** (globe) icon indicates the synchronization status of the Power Apps mobile app. At a glance, you can tell whether:

- The app is connected to the network
- A data refresh is in progress
- Updated data on the device is waiting to synchronize with the server 
- The app experienced an error or warning while syncing

The offline sync icon is always visible in the main app navigation bar on iOS, Android, and Windows devices. (It's not visible in web browsers.)

:::image type="content" source="media/offline-sync-icon-small.png" alt-text="Screenshot of a mobile app, with the offline sync icon in the app navigation bar highlighted.":::

## Sync status icons

The **offline sync** (globe) icon changes based on the app's sync status. The following table describes the possible sync states and the icons associated with them.

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

- **First sync**: This offline sync is the initial offline sync that occurs for the Power Apps mobile app. All data in the offline profile is downloaded to the device. A user must use the Power Apps mobile app in online mode until the first sync is completed.

  The first sync, which is the longest, is triggered when you sign in to the Power Apps mobile app. It also triggers after using the Reconfigure action (not recommended).

- **Delta sync**: This offline sync is faster than the first sync and occurs regularly based on the offline configuration for the organization. For example, a delta sync could occur every five minutes. Only data that changed since the last sync downloads to the mobile device.

- **Full delta sync**: When you select **Refresh** on the **Device status** page, you trigger a full sync. A full sync doesn't redownload data, but it does recheck every record on the device, so it might take longer than a regular delta sync.

- **Grid sync**: If you select **Refresh** on a grid or calendar view, the app immediately synchronizes all tables visible in the view. When the sync is complete, the view refreshes automatically.

## Device Status page

When you select the offline sync icon, the **Device Status** page opens. The **Device Status** page provides details such as the network status, what data was downloaded, whether data is waiting to be uploaded, or the amount of storage the app uses.

:::image type="content" source="media/mobile-offline-sync-settings.png" alt-text="The status page of a mobile app showing the sync settings.":::

### Sync status 

The **Sync status** area of the page tracks the overall offline status of the app. If the status is in error, see [Troubleshoot offline sync errors](/troubleshoot/power-platform/power-apps/mobile-apps/mobile-offline-troubleshooting) and the **Downloaded data** area provides the status of each individual table. When the status appears as **Available**, offline mode is available and data synced successfully.  

The status can be **Not available** due to an error during the first sync or if you dismissed downloading offline data (only applies to [offline classic mode](work-in-offline-mode.md)). If the status is **Not available**, try downloading the updates again.

You can use the **Device Status** page to see the number of files and images to be downloaded and the current progress in the  **Files available** section.

### Offline sync settings (Preview)

If your admin [enabled sync settings](setup-mobile-offline.md#define-sync-settings-on-mobile-preview) for the app, you can control when offline synchronizations are triggered.

- Set the **Wifi only** setting to **On** to sync your data only when the device is connected to a Wi-Fi network. Enable this setting when you need to save your data plan or your battery, especially if you are in a low-network area.

- If you want to sync less frequently, change the sync interval value from the **Auto sync** setting. You can keep the default value as defined by your admin by selecting **Auto**, or you can pick a longer interval that meets your needs. If you choose **Manual**, the sync only happens when you select the **Check for updates** button in the **Device Status** page.   

### Online mode (Preview)

If your admin [enabled the online mode](setup-mobile-offline.md#enable-online-mode-preview) for the app, you can tempararily switch the app to online mode.    

If you want to access online data directly from the server and your device is connected to the network, set the **online mode** setting to **On**. In this mode, the app loads data directly from the server in grids, forms and search pages. You can change back to offline mode anytime by setting the **online mode** to **Off**. If you close the app and launch it again later, the online mode is automatically reset to Off. 

When you work in online mode and the device lose network connectivity, you see the notification "Network disconnected. Switch to offline mode to continue working with the app". Use the Switch button to open the Devices status page and set the online mode to Off.  

## Notifications

On iOS, Android, and Windows devices, app sync notifications are consistent across the different sync states.

## Known issues

- The first time the app syncs, the offline sync icon continues to spin until the user switches from online mode to offline mode. 

- If the app has pending changes to upload, the number shown is the total of individual updates applied to rows, files, and images in your app, as opposed to the number of updated rows, files, and images.     

### See also
[Troubleshoot offline sync errors in the Power Apps mobile app](/troubleshoot/power-platform/power-apps/mobile-apps/mobile-offline-troubleshooting)
