---
title: Mobile offline for canvas apps (preview)
description: Learn how to create canvas apps for use offline on mobile devices in Microsoft Power Apps.
ms.date: 07/24/2023
ms.topic: overview
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

# Mobile offline for canvas apps (preview)

[This article is prerelease documentation and is subject to change.]

If users of your Dataverse-based canvas app may have spotty or no access to the Internet, you can easily provide [offline-first](#mobile-offline-first) access with simple switches and a canvas control. Basic offline-first apps are easy to make. Just build your app with normal [Power Fx formulas](/power-platform/power-fx/formula-reference), and Power Apps offline features handle everything else.

> [!IMPORTANT]
> The offline-first feature works with Dataverse tables only and doesn't support the following Power Fx functions:
>
> - CountRows
> - Filter or lookup on Lookup field
> - First
> - In
> - IsBlank
> - Relate
> - Search
> - StartsWith
> - Sum/Min/Max/Avg
> - Unrelate

You can also build complex offline apps using custom *offline profiles*. An offline profile is a set of filters and restrictions on the data your app loads to users' mobile devices. Offline profiles help you to optimize your app's performance by reducing the amount of data downloaded to the device. For example, while you may have access rights to millions of records in a table, your app may need only a thousand of them. If you download only a thousand records, your app performs better. If you need more than 15 tables in your offline app, you may want to consider using a custom offline profile.

To get started with mobile offline, turn on the offline feature in your app and in the tables your app uses. A basic offline screen template is automatically inserted into the app for you to use directly or as a starting point. [Set up mobile offline for canvas apps](canvas-mobile-offline-setup.md).

> [!IMPORTANT]
> [!INCLUDE [preview](../includes/cc-preview-features-definition.md)]
>
> This feature is in the process of rolling out and may not be available in your region yet.

## Mobile offline-first

*Offline-first* means that all the data users need when they're offline is copied to their mobile device. It requires network access to download the data initially, but after that, users work exclusively with the data stored locally on their device, even when they're online. Moving on and off the network doesn't affect the performance of the app because it's using local data. Power Apps monitors your app's network access. When it detects a connection, it automatically syncs any local changes to the server and downloads any updates from the server. The offline features handle conflict detection and minimize the use of system resources.

When you turn on the offline capability in your app, the app always runs offline-first, with or without an Internet connection. This functionality optimizes offline performance and creates a consistent experience for users as they change locations.

### See also

[Working with canvas apps offline](canvas-mobile-offline-working.md)
