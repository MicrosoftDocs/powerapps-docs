---
title: Mobile offline for canvas apps overview
description: Learn how to create canvas apps for use offline on mobile devices in Microsoft Power Apps.
ms.date: 06/05/2024
ms.topic: overview
ms.component: pa-user
ms.subservice: mobile
author: trdehove
ms.author: trdehove
ms.reviewer: smurkute
search.audienceType: 
  - enduser
searchScope:
  - "Power Apps"
ms.custom: bap-template
contributors:
- lancedMicrosoft
  
---

# Mobile offline for canvas apps overview

If users of your Dataverse-based canvas app have spotty or no Internet access, you can easily provide [offline-first](#mobile-offline-first) access with simple switches and a canvas control. Basic offline-first apps are easy to make. Just build your app with normal [Power Fx formulas](/power-platform/power-fx/formula-reference), and Power Apps offline features handle everything else.

You can also build complex offline apps using custom *offline profiles*. An offline profile is the configuration that determines the data synchronized to users’ devices. Offline profiles help you to optimize your app's performance by reducing the amount of data downloaded to the device. For example, while you may have access rights to millions of records in a table, your app may need only a thousand of them. If you download only a thousand records, your app performs better. If you need more than 15 tables in your offline app, you may want to consider using a custom offline profile.

To get started with mobile offline, turn on the offline feature in your app and in the tables your app uses. A basic offline screen template is automatically inserted into the app for you to use directly or as a starting point. [Set up mobile offline for canvas apps](canvas-mobile-offline-setup.md).

## Mobile offline-first

*Offline-first* means that all the data users need when they're offline is copied to their mobile device. It requires network access to download the data initially, but after that, users work exclusively with the data stored locally on their device, even when they're online. Moving on and off the network doesn't affect the performance of the app because it's using local data. Power Apps monitors your app's network access. When it detects a connection, it automatically syncs any local changes to the server and downloads any updates from the server. The offline features handle [conflict detection](resolve-sync-conflicts.md#sync-conflict) and minimize the use of system resources.

When you turn on the offline capability in your app, the app always runs offline-first, with or without an Internet connection. This functionality optimizes offline performance and creates a consistent experience for users as they change locations.

## Why use offline for canvas apps instead of LoadData/SaveData?

There are some key benefits to using the built-in offline functionality for canvas apps instead of LoadData/SaveData Power Fx functions.  

|Topic    |LoadData/SaveData | Built-in offline |
|---------|--------------------|------------------|
|Power Apps Studio support	|Custom	| Built-in|
|Code complexity	|Power Fx code complexity scales up with data complexity	|No code|
|Supported Power Fx functions |	All |	Partial (See [Mobile offline limitations for canvas apps](limitations-canvas-apps.md).)|
|App checker rules|	None	|Common configuration problems are flagged|
|Offline or connectivity user experience	| Not provided/custom only	|Automatic|
|[Sync user experience or status](canvas-mobile-offline-working.md#sync-status-icons)	|Not provided/custom only |	Automatic|
|[Image and file support](files-images-offline-canvas-apps.md)|	Yes, but may run into performance and memory limits	|Yes|
|[Optimized delta sync](canvas-mobile-offline-working.md#offline-delta-sync)|	No|	Yes|
|[Conflict resolution](resolve-sync-conflicts.md#sync-conflict)	|Manual	|Automatic|
|Local data store	|Files	|Transactional database|
|Automatically handles schema changes	|No	|Yes|
|Fast app launch with large datasets	|No	|Yes|
|Data size limit|	Device dependent, 30-70 MB in most cases	|Device dependent, 3 million rows|

### See also

[Work with canvas apps offline](canvas-mobile-offline-working.md)
