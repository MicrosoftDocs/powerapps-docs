---

title: Mobile offline for model-driven apps overview
description: Learn how to configure model-driven apps for offline mode.
author: trdehove
ms.component: pa-user
ms.topic: quickstart
ms.date: 05/29/2024
ms.subservice: mobile
ms.author: trdehove
ms.custom: ""
ms.reviewer: smurkute
ms.assetid: 
search.audienceType: 
  - enduser
searchScope:
  - "Power Apps"
---

# Mobile offline for model-driven apps overview

Wouldn't it be great to use your mobile app without worrying about spotty internet connectivity? With model-driven apps made with Power Apps and the new, mobile offline-first experience, it's possible. People who need to work from remote locations can continue to work seamlessly without worrying about their internet connection.

With the new, mobile offline experience enabled for your model-driven apps, not only can you continue working in offline mode, you also have better device performance, a more responsive app, and less drain on the battery because fewer connections are being made to the server.

An internet connection is required to sync data between your mobile device and Microsoft Dataverse.

To get started with mobile offline, an app maker needs to enable and define the tables that are available for offline use by using the [modern app designer](../maker/model-driven-apps/app-designer-overview.md). For more information, go to [Set up mobile offline](setup-mobile-offline.md).

## Mobile offline is offline-first by default

_Offline-first_ means that all the data you might need when offline is copied to your mobile device. This requires initial network access to download the data. Once you have your data, you only work with the data on your local device all the time. This is true both when your device is connected and disconnected to the network.

Moving in and out of network access doesn't affect performance of the app because it's using local data. Power Apps monitors network access and automatically syncs the changes you make locally with the server, and downloads any updates made on the server. The offline features automatically handle spotty network connections, download data, upload data, handle conflict detection, and more. The built-in, offline features minimize system resources and are highly performant.

When offline mode is configured and enabled for your model-driven app, anyone who uses the [Power Apps mobile app](run-powerapps-on-mobile.md) can also use the app in offline mode. By default, the Power Apps mobile app runs offline-first, either with or without an internet connection. This functionality optimizes offline performance and creates a consistent experience for users as they change locations:

- **Online**: Occurs when an internet connection is available, but offline mode isn't set up. The mobile app functions similar to using the app with an internet connection on your PC. When the internet connection is lost, the mobile app is unusable. This isn't recommended.
- **Offline-first without an internet connection**: Data is downloaded and all changes are saved to your mobile device. When the internet connection is restored, the changes are automatically synced to the server.
- **Offline-first with an internet connection**: Data is downloaded to the device and all changes are saved locally. Because there's an internet connection, the app automatically attempts to sync every few minutes.

> [!IMPORTANT]
> For more information about how to set up mobile offline for canvas apps, go to [Develop offline-capable canvas apps](../maker/canvas-apps/offline-apps.md)

## Offline-first vs. classic offline

With the offline-first experience, it's important to understand the key benefits of the _offline-first experience_ versus the _classic offline experience_.

| **Offline-first** | **Classic offline** |
|-------------------------|-------------------------|
| <ul><li>Your data is always the same, regardless of your network connection.</li><li>There's no toggle for users to switch from offline to online mode. A user never forgets to sync their changes back to the server because the app does it automatically.</li></ul>| <ul><li>Users have the option to skip the initial offline sync and stay online, which means that users in your organization might not have the same experience.</li><li>Users have to remember to disable the **Work in offline mode** toggle before they can sync changes with the server.</li><li>To save your changes in offline mode, you need to set the **Work in offline mode** toggle to **On**. Otherwise, when you're working on a row and suddenly lose your internet connection, your changes are lost.</li><li>The rows you see in offline mode are listed from the local database. This means that the rows you see in offline mode vs. online mode can be different.</li></ul> |
