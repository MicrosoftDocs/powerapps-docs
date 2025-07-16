---

title: Mobile offline limitations for canvas apps
description: Learn about the limitations for canvas apps that use mobile offline.
author: Murugesh1985
ms.component: pa-user
ms.topic: quickstart
ms.date: 07/16/2025
ms.subservice: mobile
ms.author: murugeshs
ms.reviewer: smurkute
ms.assetid: 
search.audienceType: 
  - enduser
searchScope:
  - "Power Apps"
---

# Mobile offline limitations for canvas apps

Before you set up the mobile app in offline mode, be sure to read through the following limitations. We recommend that you also review [Best practices for developing an app for offline use](best-practices-offline.md) and [Optimize the offline profile](mobile-offline-guidelines.md).

## Capabilities not supported in offline-enabled apps

|Area |Description|  
|-------------|---------|  
| Canvas app types|The offline-first feature works for standalone canvas apps only. It doesn't work for embedded canvas apps, custom pages, or canvas apps in Teams.|
|Connectors|Non-Dataverse connectors, like SharePoint, aren't supported in offline mode.|
|Dataverse table types| Virtual tables and elastic tables aren't supported in offline mode.|
|Shared offline profile| If the same, offline profile is used in a canvas app and in a model-driven app, it creates two, separate local databases. |

> [!NOTE]
> If your app connects to data from Excel, CSV files, or SharePoint lists, you can [start with Copilot](/power-apps/maker/data-platform/create-edit-entities-portal?#tabpanel_1_sharepoint) to import data to Dataverse. Once your data is in Dataverse, you can turn on offline support for your canvas apps with one selection.

## Offline runtime limitations


|Area |Description|  
|-------------|---------| 
|Offline record limit|The total number of records synced is limited to 3,000,000. Attempts to sync a larger number of records fail. This number also includes hidden tables used for offline capabilities.|
| Power automate| Power automate flows aren't supported in offline mode.|
| Power Fx functions|The offline-first feature works with Dataverse tables only and doesn't support the following Power Fx functions: Relate, Unrelate |
|Relationship |In offline mode, canvas apps don't support many-to-many relationships. <br><br>Filtering on column lookups is limited to one level of the relationship when the app is configured for offline use. Self-referential lookups are also not supported in offline mode. Consider following examples to understand the relationship with Account and Contact information. <br><br> **Supported Lookups**: <br><br>Lookups are supported for one level of relationship. For example:  <br><br>`Filter(Account, 'ContactID'.'Zipcode' = "11056")` <br><br>This retrieves all accounts with the zipcode 11056. <br><br> **Unsupported Lookups**: <br><br> 1. **Self-referential Lookups**: Self-referential lookups aren't supported. For example: <br><br>`Filter(Account, 'Parent Account'. 'Name' = "John Doe")` <br><br>This doesn't work because the parent account is a self-reference to the account table. <br><br> 2. **Multi-level Relationship Lookups**: Lookups involving more than one level of the relationship aren't supported. For example: <br><br>`Filter(Account, 'ContactID'.'Map'.Latitude = "38'53")` <br><br> This doesn't work because it involves more than one level of relationship (Account > Contact > Map). <br><br>  **Note**: The same limitations apply to the lookup function and the filter function mentioned earlier.|
|Tables | Notes aren't supported in offline mode in canvas apps. |
|Column types |Calculated and roll-up fields&mdash;that are part of rows synced to the client&mdash;aren't reevaluated by the client. The reevaluation happens on the server when the updated row is synced.<br><br>When you run an app in offline mode, mapped fields aren’t prepopulated when you create a new record from a table that has fields mapped to another table.|
|Sort order|Items in a gallery may appear in a different order in an offline-capable app if no [sort order](/power-platform/power-fx/reference/function-sort) is selected. Choose a sort order in the gallery control to make sure the app behaves consistently in mobile apps and web browsers.|
|Background synchronization|Data can only be synced regularly when Power Apps is running in the foreground of your device, with the screen unlocked. Learn more in [Sync data offline in the background](sync-data-offline-background.md).|

## Profile filters limitations

|Area |Description|  
|-------------|---------|  
|Relationship defined for each table|A maximum of 15 relationships is allowed. There's a maximum of one many-to-many (M:M) or one-to-many (1:M) relationships within the 15 relationships. If any custom tables demand this scenario, then revisit the data model. No circular references or self-references are supported.|
|Images and files|Images and files are subject to the same limitations as any other table. Because of implicitly defined relationships, an offline profile can only contain up to 14 image columns, across all entities.|
|Auto-generated offline profile| The auto-generated offline profile doesn't handle filters. As a result, for each table used in the app, it downloads *all* rows to which the user has permissions.|

### See also
[Troubleshoot offline sync errors in the Power Apps mobile app](/troubleshoot/power-platform/power-apps/mobile-apps/mobile-offline-troubleshooting)
