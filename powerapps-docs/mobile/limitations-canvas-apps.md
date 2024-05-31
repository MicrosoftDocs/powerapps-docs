---

title: Mobile offline limitations for canvas apps
description: Learn about the limitations for canvas apps that use mobile offline.
author: trdehove
ms.component: pa-user
ms.topic: quickstart
ms.date: 05/31/2024
ms.subservice: mobile
ms.author: trdehove
ms.reviewer: sericks
ms.assetid: 
search.audienceType: 
  - enduser
searchScope:
  - "Power Apps"
---

# Mobile offline limitations for canvas apps

Before you set up the mobile app in offline mode, be sure to read through the following limitations. We recommend that you also review [Best practices to use an app for offline](best-practices-offline.md) and [Optimize the offline profile](mobile-offline-guidelines.md).

## Limitations and known issues

- A **canvas app not in a solution** can't be used in offline mode.

- The offline-first feature **works for standalone, canvas apps only**. It doesn't work for [embedded canvas apps](../maker/model-driven-apps/embed-canvas-app-in-form.md), [custom pages](../maker/model-driven-apps/model-app-page-overview.md), or [canvas apps in Teams](../teams/overview.md).

- The offline-first feature works with Dataverse tables only and doesn't support the following Power Fx functions:
   - **Relate**
   - **Unrelate**
   - **UpdateIf**
   - **RemoveIf**
 
- **Filter on column look-up** only supports one level of look-up when the app is configured for offline use.

- **Many-to-many relationships** aren't supported in offline mode.
 
- **Non-Dataverse connectors** like Sharepoint aren't supported in offline mode.

- **Virtual tables** aren't not supported in offline mode.

- **Calculated and roll-up fields** - Calculated and roll-up fields&mdash;that are part of rows synced to the client&mdash;aren't reevaluated by the client. The reevaluation happens on the server when the updated row is synced.

- **Mapped fields** - When you run an app in offline mode, mapped fields aren’t prepopulated when you create a new record from a table that has fields mapped to another table.

- An **offline profile** can't be used in two canvas apps.

- If the **same offline profile** is used in a canvas app and in a model-driven app, it will create two separate local databases. 
 
- The **auto-generated offline profile** doesn't handle filters. As a result, for each table used in the app, it downloads *all* rows to which the user has permissions.

- Items in a gallery may appear in a **different order** in an offline-capable app if no [sort order](/power-platform/power-fx/reference/function-sort) is selected. Choose a sort order in the gallery control to make sure the app behaves consistently in mobile apps and web browsers.

- Data can only be synced regularly when Power Apps is running in the foreground of your device, with the screen unlocked. Learn more: [Sync data offline in the background](sync-data-offline-background.md)

## Profile filters limitations

|Profile details |Limitation|  
|-------------|---------|  
|Relationship defined for each table|A maximum of 15 relationships is allowed. The is a maximum of one many to many (M:M) or one to many (1:M) relationships within the 15 relationships. If any custom tables demand this scenario, then revisit the data model. No circular references or self-references are supported.|
|Images and files|Images and files are subject to the same limitations as any other table. Because of implicitly defined relationships, an offline profile can only contain up to 14 image columns, across all entities.|


