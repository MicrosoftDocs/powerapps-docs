---
title: Mobile offline for canvas apps (preview)| Microsoft Docs
description: Learn about how to use canvas apps on your movile device in offline mode.
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

# Mobile offline for canvas apps (preview)

[This topic is pre-release documentation and is subject to change.]

You can easily enable canvas apps that are based on Dataverse for [offline-first](#mobile-offline-first) scenarios with simple switches and a simple canvas control. This feature is useful for field and remote workers or anyone with spotty or no access to the internet. 

Basic offline-first apps are easy to build. There is no need to use [PowerFx’s SaveData or LoadData functions](/power-platform/power-fx/reference/function-savedata-loaddata) or manage offline data with complex, collection schemes in PowerFx. Just build your app with normal [Power Fx formulas](/power-platform/power-fx/formula-reference) and the offline features handle all the complexity for you. 

> [!Important]
> This offline-first feature currently only works with Dataverse tables, and there are some Power Fx expressions that are not yet supported.  

Complex, offline apps are also supported. Complex, offline scenarios are enabled with custom *offline profiles*. An offline profile is a set of filters and restrictions on the data that you load to your device. For example, while you may have access rights to millions of records for a table, you may only need a thousand records for your app. If you only download a thousand records, your app will perform better. Use offline profiles to optimize your app’s performance by reducing the data downloaded to the mobile device. If you need more than 15 tables in your offline app, you may want to consider a custom offline profile. 

To get started with mobile offline for canvas apps, an app maker needs to enable the app for offline and enable the tables used in the app for offline. A basic offline screen template is automatically inserted into the app for you to use directly or as a starting point. More information: [Set up mobile offline for canvas apps](canvas-mobile-offline-setup.md).

## Mobile offline-first

*Offline-first* means that we copy all data you may need when offline down to your mobile device. This requires initial network access to download the data.  Once you have your data, you only work with the data on your local device all the time.  This is true both when you are online and offline.  Moving in and out of network access therefore does not affect performance of the app because it is using local data.  Power Apps monitors network access and automatically up syncs the changes you have made locally and downloads any updates made on the server. The offline features automatically handle spotty network connections, download and persistence of data, up sync, incremental / delta sync, conflict detection and more. The  built-in offline features minimize system resources and are highly performant. 

After offline is enabled for your app, two versions of the app are produced .  A normal canvas app that can be shared for normal online use and then one that is published to the Power Apps player store.  Both can be used but the [Power Apps mobile app](run-powerapps-on-mobile.md) from the Power Apps store will use the offline first feature.  The code is the same but the offline first app will use SQLite as the first level store and may have an additional set of filters on the data that reduces the data downloaded for offline use. The Power Apps mobile app always runs offline-first, either with or without an internet connection. This functionality optimizes offline performance and creates a consistent experience for users as they change locations:   

- **Offline-first without an internet connection**: Data is downloaded, and all changes are saved to your mobile device. When the internet connection is restored, the changes are automatically synced to the server.
- **Offline-first with an internet connection**: Data is downloaded to the device, and all changes are saved locally. Because there's an internet connection, the app will automatically attempt to sync every few minutes.

More information: [Working with canvas apps offline](canvas-mobile-offline-working.md).

## System requirements

To use canvas apps in offline mode, you must...
