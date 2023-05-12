---
title: Working with canvas apps offline (preview)| Microsoft Docs
description: This article explains how to work with canvas apps in offline mode on your mobile device.
author: trdehove
ms.component: pa-user
ms.topic: quickstart
ms.date: 04/17/2023
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
[This topic is pre-release documentation and is subject to change.]

With the [offline-first](canvas-mobile-offline-overview.md#mobile-offline-first) experience, you can work with your Power Apps canvas app on your mobile device anytime, even when you don't have internet access. The mobile app provides a rich offline experience so that you can always stay productive. After you're back online, changes you've made are synchronized with your server in the Microsoft Dataverse environment.

If you're working on a record and lose network connection, any updates made to the record are saved in offline mode and will be synchronized to the server after you're back online.

With offline-first, all the calls to Dataverse data are executed against a local database mirroring the Dataverse server and are scoped to the need of the app.

:::image type="content" source="media/conceptual-image.png" alt-text="Conceptual diagram showing that with offline-first, all the calls to Dataverse data are executed against a local Database mirroring the Dataverse server and scoped to the need of the app.":::

> [!Important]
> [!include [preview](../includes/cc-preview-features-definition.md)]

## Initial offline sync

For the app to be available in offline mode, app and user data must be downloaded on your device. This process is called the *initial offline sync*.

The initial offline sync happens when you open the canvas app. You'll see a message stating that your app is syncing the offline data with the **number of rows and tables that are downloaded** on your device. This can take a few minutes or longer, depending on what has been configured in the app. 

If the initial offline sync isn't complete, it will be triggered every time the app is opened.

## Offline delta sync

Canvas apps can be fully customized. However, if the app is using the offline template, it comes with default capabilities, such as synchronization errors or warnings, network connectivity status, and whether the data on the device is in sync with the server.

The offline sync icon indicates the synchronization status of the Power Apps mobile app. At a glance, you can tell:

-   Whether the app is connected to the network

-   Whether a data refresh is in progress

-   Whether updated data is waiting to sync

-   Whether the app has experienced an error or warning while syncing

### Sync status icons

The offline sync icon changes based on the app's sync status. When testing your offline app, it's easy to lose track of whether you are online or offline, so be sure to check that sync status icon.

When online, Power Apps is currently set to sync every 5 minutes.

| Icon | Description |
|------|--------------|
| ![Icon showing that the app is connected to the internet.](media/connected.png "Icon showing that the app is connected to the internet.")| The app is connected to the internet. |
| ![Icon showing that the app isn't connected to the internet.](media/not-connected.png "Icon showing that the app isn't connected to the internet.") | The app is not connected to the internet. |
| ![Icon showing that the app is syncing data.](media/synching.png "Icon showing that the app is syncing data.") | The app is syncing data. |
| ![Icon showing that the app has pending changes to upload.](media/upload-pending-changes.png "Icon showing that the app has pending changes to upload.") | The app has pending changes to upload. |
| ![Icon showing that the synchronization process encountered an error.](media/error.png "Icon showing that the synchronization process encountered an error.") | The synchronization process encountered an error. |
| ![Icon showing that the synchronization process encountered a warning.](media/warning.png "Icon showing that the synchronization process encountered a warning.") | The synchronization process encountered a warning. |

By clicking on the icon, you get a description of the state.

## Known issues
- Key Power Fx functions that are not yet supported include *StartsWith*, *In*, and *With*.  If you use the 'App from Data' feature you will get an app that has a search text field that uses a *StartsWith* formula which will fail silently.  

