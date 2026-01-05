---
title: How mobile offline works in Power Apps
description: Understand the data sync model in Power Apps Mobile, including incremental syncs, configurable intervals, and automatic resumption after connectivity returns.
#customer intent: As a Power Apps user, I want to understand how data sync works so that I can ensure my offline data stays up to date.
reviewer: shwetamurkute
author: Murugesh1985
ms.author: murugeshs
ms.reviewer: smurkute
ms.date: 12/23/2025
ms.topic: concept-article
---

# How offline first functionality works in Power Apps mobile

Offline first functionality in Power Apps mobile enables users to access and work with app data on their mobile devices without an active internet connection. This feature uses a local database on the device to store data. Changes made while the network is offline automatically sync with Dataverse when connectivity is restored. Changes made while network is online automatically sync with Dataverse based on the sync frequency configured by the maker in the offline settings.

## Offline profile

First, to create an offline-first app, maker must create the offline profile. The profile defines:

- Tables and columns available for offline use
- Optional filters to limit the data downloaded per table
- Relationships between tables for linked data access

After you create the profile, when you first open the app, the data for the offline profile downloads and stores locally on the device in a SQLite-based cache. This local copy becomes the primary data source for all app operations. The app doesn't access Dataverse directly, even when you're online. Learn more about setting up offline for canvas apps in [Set up mobile offline for canvas apps](canvas-mobile-offline-setup.md) and about setting up offline for model-driven apps in [Set up mobile offline for model-driven apps](setup-mobile-offline.md).

## Data synchronization

The sync process keeps offline data up to date with Dataverse through automatic synchronization:

- **Initial download**: When the app first opens, all data defined in the offline profile is downloaded to the local device.
- **Incremental updates**: Subsequent syncs fetch only changes (inserts, updates, deletes) since the last sync, reducing data transfer.
- **Configurable frequency**: Makers can set sync intervals (every few minutes, hourly, or daily) for each table in the offline profile in the maker studio.
- **Smart sync**: If no changes are detected across tables, the sync is skipped to save bandwidth.
- **Automatic resumption**: When the mobile device reconnects to the network, the sync operation resumes automatically.
- **Platform differences**: On iOS, syncs happen only in the foreground. On Android, syncs that start in the foreground continue even when the app moves to the background.

## Local storage and data access

All offline data is stored in a local database on the device, ensuring data availability regardless of network status.

**Read operations**: When offline, the app reads from the local cache for all data operations. This includes viewing records, searching, and filtering data.

**Write operations**: Changes made offline are queued locally and pushed to Dataverse when connectivity is restored. Users can continue making modifications without interruption.

**Data retention**: Retention duration isn't fixed by the platform. Data persists as long as the app and offline profile remain installed on the device. There's no automatic expiry unless:

- The user clears the app cache or uninstalls the app
- The maker updates the offline profile, which can trigger a full refresh
- The user sign out of the app before the sync is complete

## Offline-first behavior

When the mobile app is configured as offline-first, queries always run against the local device data, regardless of network availability. This ensures consistent performance and eliminates latency from server round trips.

Complex lookups and relationships use predownloaded related tables stored locally. Users can navigate between related records without requiring an active connection.

**Online mode option**: In model driven apps, makers can set up an **Online mod** feature. Once configured, users can toggle this option to access data directly from Dataverse instead of the local device data. Meanwhile, the app continues syncing data in the background, allowing users to switch back to offline mode at any time without losing functionality. Learn more in [Turn on Online mode](setup-mobile-offline.md#turn-on-online-mode)

## Maker controls and optimization

Makers have several tools to optimize data download, offline performance and control the offline experience:

- **Column selection**: Choose specific columns to minimize payload size and reduce download time
- **Relationship configuration**: Define parent-child table relationships for linked data access
- **Sync frequency**: Configure sync intervals and filters for each table individually
- **Media settings**: Configure which images and files should be downloaded for offline access

These controls allow makers to balance offline functionality with performance and storage constraints on mobile devices. Learn more about how to optimize offline profile in [Optimize the offline profile](mobile-offline-guidelines.md)

## Building offline app screens

Screens in an offline-enabled app are built on top of the offline profile and should be designed with offline scenarios in mind:

**Data binding**: Controls such as galleries and forms bind to tables defined in the offline profile, ensuring data availability offline.

**Conditional logic**: Screens should handle offline scenarios by disabling actions that require live server calls, such as certain API integrations or real-time data operations.

**Optimized layouts**: Galleries and forms should show essential columns only, reducing load time and improving performance on mobile devices.

**Write-back handling**: Input controls queue changes locally and should display status indicators (for example, "Pending Sync") until connectivity returns and synchronization completes.

## Offline-first design benefits

The offline-first architecture provides several advantages over traditional online-only applications:

- **Faster load times**: No round trips to the server for every screen or data query, resulting in near-instantaneous data access
- **Consistent experience**: Users interact with the same local dataset whether online or offline, eliminating connectivity-dependent behavior changes
- **Reduced network dependency**: Only sync operations hit the server, not every read operation, minimizing bandwidth usage and improving reliability

This design ensures that users can work productively in any network environment, from stable Wi-Fi connections to areas with intermittent or no connectivity.