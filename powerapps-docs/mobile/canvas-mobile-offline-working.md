---
title: Work with canvas apps offline (preview)
description: Learn how to work with canvas apps in offline mode on your mobile device.
ms.date: 07/24/2023
ms.topic: how-to
ms.component: pa-user
ms.subservice: mobile
author: trdehove
ms.author: trdehove
ms.reviewer: sericks
search.audienceType: 
  - enduser
searchScope:
  - "Power Apps"
ms.custom: bap-template
---

# Work with canvas apps offline (preview)

[This article is prerelease documentation and is subject to change.]

[Canvas apps](../maker/index.md) are a type of app that nondevelopers can make with Microsoft Power Apps. If a canvas app is designed for [offline use](canvas-mobile-offline-overview.md), you can work with it on your mobile device even when you don't have Internet access. All the data the app needs is stored locally on your device. Any changes you make are synchronized with the app server the next time your device connects to the network. If you're in the middle of changing some data and you lose your network connection, the app saves your changes and uploads them to the server when you're back online.

> [!IMPORTANT]
> [!INCLUDE [preview](../includes/cc-preview-features-definition.md)]
>
> This feature is in the process of rolling out and may not be available in your region yet.

## Initial offline sync

Before the app can work offline, it needs to download to your device all the data it needs to have available. This process is called the *initial offline sync*. It can take a few minutes or longer, depending on how the app was designed.

The initial offline sync happens automatically when you open the app. A message tells you the app is syncing the offline data and the number of rows and tables that are downloaded. If the initial sync doesn't complete, it's triggered every time you open the app.

## Offline delta sync

After the initial offline sync, the data that's stored locally is kept in sync with data on the app server whenever your device has a network connection. These periodic updates are known as "delta" syncs. "Delta" is shorthand for data that's changed. Power Apps syncs every five minutes when you're online.

## Sync status icons

Depending on how the app was designed, it includes information about its synchronization status in the form of a globe with various icons. At a glance, you can tell:

- Whether the app is connected to the network
- Whether a data update is in progress
- Whether updated data is waiting to sync
- Whether an error or warning occurred while data was syncing

The following table describes the icons and their meanings.

| Icon | Description |
|------|--------------|
| ![Icon showing that the app is connected to the internet.](media/connected.png "Icon showing that the app is connected to the internet.")| The app is connected to the Internet. |
| ![Icon showing that the app isn't connected to the internet.](media/not-connected.png "Icon showing that the app isn't connected to the internet.") | The app isn't connected to the Internet. |
| ![Icon showing that the app is syncing data.](media/synching.png "Icon showing that the app is syncing data.") | The app is syncing data. |
| ![Icon showing that the app has pending changes to upload.](media/upload-pending-changes.png "Icon showing that the app has pending changes to upload.") | The app has pending changes to upload. |
| ![Icon showing that the synchronization process encountered an error.](media/error.png "Icon showing that the synchronization process encountered an error.") | The synchronization process encountered an error. |
| ![Icon showing that the synchronization process encountered a warning.](media/warning.png "Icon showing that the synchronization process encountered a warning.") | The synchronization process encountered a warning. |

To get a description of the sync state, select the icon.

## Known issue

Key Power Fx functions that aren't yet supported include *StartsWith*, *In*, and *With*. When creating an app that has a search text field that uses a *StartsWith* formula, the search fails silently.
