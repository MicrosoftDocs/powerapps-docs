---
title: View offline sync status
description: The offline sync icon is now always visible in the mobile navigation bar. The icon provides contextual information such as if the app is connected, if data is currently refreshing, whether there are pending user updates that have not synchronized yet, and whether the sync has an error or warning.
ms.date: 01/19/2023
ms.reviewer: 
ms.suite: 
ms.tgt_pltfrm: 
ms.topic: article
applies_to: Dynamics 365 apps
ms.author: sericks
author: sericks007
manager: tapanm-MSFT
search.audienceType: 
  - enduser
---

# View offline sync status

The offline sync icon is now always visible in the mobile navigation bar. The icon provides contextual information such as if the app is connected, if data is currently refreshing, whether there are pending user updates that have not synchronized yet, and whether the sync has an error or warning.

The offline sync icon is now visible in the main navigation on iOS and Android devices.

> [!div class="mx-imgBorder"]
> ![The offline sync icon is visible in the main navigation bar.](media/offline-sync-icon-small.png)

## Offline sync icon changes based on sync status
The offline sync icon changes based on sync status.  The following table provides more detail.

| Icon | Description|
|------|--------------|
| ![Icon showing that the app is connected to the internet.](media/connected.png "Icon showing that the app is connected to the internet.")| App is connected to the internet.|
| ![Icon showing that the app is not connected to the internet.](media/not-connected.png "Icon showing that the app is not connected to the internet.") |App is not connected to the internet.|
| ![Icon showing that the app is syncing data.](media/synching.png "Icon showing that the app is syncing data.") |App is syncing data.|
| ![Icon showing that the app has pending changes to upload.](media/upload-pending-changes.png "Icon showing that the app has pending changes to upload.") |App has pending changes to upload.|
| ![Icon showing that there is an error in the synchronization process.](media/error.png "Icon showing that there is an error in the synchronization process.") |There is an error in the synchronization process.|
| ![Icon showing that there is a warning in the synchronization process.](media/warning.png "Icon showing that there is a warning in the synchronization process.") |There is a warning in the sychronization process.|

## Offline Status page
When you select the offline sync icon, the **Offline Status** page is displayed. The **Offline Status** page provides detailed information about the sync status, such as what data was downloaded and if there is data yet to upload to the app, as shown in the following image.

> [!div class="mx-imgBorder"]
> ![When you select the offline sync icon, the **Offline Status** page is displayed.](media/OfflineStatusPage-NotConnected.png)
