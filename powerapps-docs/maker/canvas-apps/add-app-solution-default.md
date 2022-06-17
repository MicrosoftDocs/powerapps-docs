---
title: Add canvas apps to solution by default
description: In Power Apps, learn about how to configure environment for adding all new canvas apps to default solution through various methods.
author: tapanm-msft

ms.topic: article
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 10/21/2021
ms.subservice: canvas-maker
ms.author: hasharaf
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - tapanm-msft
---

# Add canvas apps to solution by default

You can [create canvas apps from within a solution](add-app-solution.md) by initiating a canvas app creation from the solutions section in Power Apps. However, creating canvas apps inside solutions is optional, and requires manual steps. Hence, not all new canvas apps are created inside solutions. With this feature, canvas apps can now be included and created from within a solution by default. For more information about solutions, see [Solutions overview](../data-platform/solutions-overview.md), and [application lifecycle management (ALM) guide](/power-platform/alm/overview-alm).

Canvas apps included in solution by default benefit from reusing Microsoft Dataverse components such as connection references and environment variables. This feature reduces overhead and redundancy to manage individual canvas apps that aren’t part of a solution.

For example, an environment with hundreds of canvas apps that live outside of a solution requires manual efforts to move them into solution to enable ALM. With this release, such manual intervention is eliminated.

## Prerequisites

- Solutions are stored in Dataverse. A Power Platform environment must have a Dataverse database to use this feature. Environments created without a Dataverse database can’t use this feature.
- You must have **Write** privilege to [CanvasApp table](../../developer/data-platform/reference/entities/canvasapp.md) to create canvas apps in solutions. For more information, see [security roles and privileges](/power-platform/admin/security-roles-privileges). 
- A canvas app within a solution must be shared with you before you can view or edit.

> [!IMPORTANT]
> Ensure you review the [considerations](#considerations) before enabling canvas apps in solutions by default.

## Supported methods

There are different methods available to get started while creating canvas apps. Canvas apps that are created within solution by default using this feature require the use of some of these methods. Hence, it becomes important to understand how this feature can be utilized. 

The following table summarizes which methods benefit from canvas apps within solution by default.

| Method | Available for canvas apps within a solution by default?  |
| - | - |
| [Canvas apps from Dataverse](data-platform-create-app.md) | Yes |
| Canvas apps from other data sources, such as [SharePoint](app-from-sharepoint.md), [Excel](get-started-create-from-data.md), [Azure Blob Storage](connections/connection-azure-blob-storage.md), and [others](connections-list.md#popular-connectors) | Yes |
| [Blank canvas app](create-blank-app.md) </br> **NOTE**: [Power Apps](https://make.powerapps.com) > **Apps** > **New app** > **Canvas** also creates a blank canvas app. | Yes |
| [Canvas apps from template](get-started-test-drive.md) | No |
| Canvas apps created by [customizing SharePoint forms](customize-list-form.md) | No |
| Canvas apps created directly from [Azure portal](https://portal.azure.com) using [Azure SQL Database](app-from-azure-sql-database.md) | No |

## Enable the feature

Canvas apps within solutions by default feature is disabled by default and must be enabled manually. To enable this feature, go to Power Platform admin center by going to [Environments] > [select an environment] > [Settings] > [Product] > [Features], and enable the feature **Canvas apps in Dataverse by default**. More information: [Manage feature settings](/power-platform/admin/settings-features)

## Check canvas apps in solution 

To view canvas apps inside a solution, use the [solution view](../data-platform/solutions-area.md). Only users that have access to the canvas app added inside a solution can view the app in a solution view. 

## Export and import standalone canvas app 

Once this feature is enabled, consider using solutions [export](../data-platform/export-solutions.md) and [import](../data-platform/import-update-export-solutions.md) instead of [export and import of standalone canvas app](export-import-app.md). 

## Considerations

- Increase in capacity consumption of Dataverse environment. 
- Cost implications due to increased capacity consumption. 
- Known solution limitations related to canvas apps still apply to canvas apps created within solutions by default. 
- This feature also enables the automatic creation of environment variables when adding data sources for your apps. 
- By default, this feature saves all canvas apps to the default solution named **Common Data Services Default Solution** published by **Microsoft Dataverse Default Publisher**. However, we recommend that you use a non-default solution for canvas apps.
- When you toggle the feature switch in the Power Platform admin center, the Dataverse property `enablecanvasappsinsolutionsbydefault` in the organization table is updated.  The value can be reviewed using the following sample ODATA snippet.

[!INCLUDE[footer-include](../../includes/footer-banner.md)]