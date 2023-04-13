---
title: Working with canvas apps offline (preview)| Microsoft Docs
description: This article explains how to work with canvas apps in offline mode on your mobile device.
author: trdehove
ms.component: pa-user
ms.topic: quickstart
ms.date: 04/12/2023
ms.subservice: mobile
ms.author: trdehove
ms.custom: ""
ms.reviewer: sericks
ms.assetid: 
search.audienceType: 
  - enduser
searchScope:
  - "Power Apps"
---

# Working with canvas apps offline (preview)

Work with your data in offline mode even when you don't have internet access. The mobile app provides a rich offline experience that lets you work with commands like create, read, update, and delete—along with some special commands—so you always stay productive. After you're back online, changes you've made are synchronized with your apps in the Microsoft Dataverse environment.

If you're working on a record and lose network connection, any updates made to the record are saved in offline mode and will be synchronized to the app after you're back online.

The app data includes all the resources needed for the app to run properly. The User data is defined by the offline profile that is auto-generated from the processing of the code of the app.

With offline-first, all the calls to Dataverse data are executed against a local Database mirroring the Dataverse server and scoped to the need of the app.

:::image type="content" source="media/conceptual-image.png" alt-text="Conceptual diagram showing that with offline-first, all the calls to Dataverse data are executed against a local Database mirroring the Dataverse server and scoped to the need of the app.":::

## Initial Offline sync

For the app to be available in offline mode, app and user data must be downloaded on your device. This process is called *initial offline sync*.

The initial offline sync happens during the loading of the canvas app. you'll get a loading experience stating that your app is syncing the offline data with the **number of rows and tables that are downloaded**. This can take a few minutes or longer, depending on what has been configured in the app. If the initial offline sync isn't complete, it will be triggered every time the app is opened.

:::image type="content" source="media/initial-offline-sync.png" alt-text="Image of the mobile screen that indicates the app is syncing the offline data.":::

## Offline delta sync

Canvas apps can be fully customized. However if the app is using the offline template, it comes with Out Of The Box capabilities such as synchronization errors or warning, network connectivity status, and last but nor least whether the data on the device are in sync with the server and the other way around.

The offline sync icon indicates the synchronization status of the Power Apps mobile app. At a glance, you can tell:

-   Whether the app is connected to the network

-   Whether a data refresh is in progress

-   Whether updated data is waiting to sync

-   Whether the app has experienced an error or warning while syncing

## Sync status icons

The offline sync icon changes based on the app's sync status. For more information about the possible sync states and the icons associated with them, see [Sync status icons(offline-sync-icon.md#sync-status-icons).

By clicking on the icon, you can have a clear description of the different states.
