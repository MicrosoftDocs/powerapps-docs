---
title: Add canvas apps and cloud flows to solution by default (preview)
description: Learn about how to configure an environment to adding all new canvas apps and cloud flows to default solution through various methods.
author: tapanm-msft

ms.topic: article
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 08/10/2022
ms.subservice: canvas-maker
ms.author: hasharaf
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - tapanm-msft
---

# Add canvas apps and cloud flows into Dataverse solution by default (preview)

[This article is pre-release documentation and is subject to change.]

You can [create canvas apps from within a solution](add-app-solution.md) or [create a cloud flow in a solution](/power-automate/create-flow-solution) in the solutions section in Power Apps or Power Automate. However, creating canvas apps and cloud flows inside solutions is optional, and requires manual steps.

Canvas apps and cloud flows can now be created in a solution by default. For more information about solutions, see [Solutions overview](../data-platform/solutions-overview.md), and [application lifecycle management (ALM) guide](/power-platform/alm/overview-alm).

Canvas apps and cloud flows in a solution are defined in Dataverse and are more manageable because of Dataverse capabilities including [connection references](/power-apps/maker/data-platform/create-connection-reference), [environment variables](/power-apps/maker/data-platform/environmentvariables), the [Dataverse API](/power-apps/developer/data-platform/webapi/overview), and solution-based [application lifecycle management (ALM)](/power-platform/alm). 

> [!IMPORTANT]
> - This is a preview feature.
> - [!INCLUDE[cc_preview_features_definition](../../includes/cc-preview-features-definition.md)]

## Prerequisites

- Solutions are stored in Dataverse. A Power Platform environment must have a Dataverse database to use this feature. Environments created without a Dataverse database can’t use this feature.
- You must have **Write** privilege to [CanvasApp table](../../developer/data-platform/reference/entities/canvasapp.md) to create canvas apps in solutions. You must have **Write** privilege to [Workflow table](../../developer/data-platform/reference/entities/workflow.md) to create cloud flows in solutions. For more information, see [security roles and privileges](/power-platform/admin/security-roles-privileges). 
- A canvas app or cloud flow within a solution must be shared with you before you can view or edit.

> [!IMPORTANT]
> Ensure you review the [considerations](#considerations) before enabling canvas apps in solutions by default.

## Supported entry points for canvas apps

There are different entry points that can be used to create canvas apps. Canvas apps that are created within solution by default using this feature require the use of some of these entry points. Hence, it becomes important to understand how this feature can be utilized. 

The following table summarizes which entry points benefit from canvas apps within solution by default.

| Entry point | Available for canvas apps within a solution by default?  |
| - | - |
| [Canvas apps from Dataverse](data-platform-create-app.md) | Yes |
| Canvas apps from other data sources, such as [SharePoint](app-from-sharepoint.md), [Excel](get-started-create-from-data.md), [Azure Blob Storage](connections/connection-azure-blob-storage.md), and [others](connections-list.md#popular-connectors) | Yes |
| [Blank canvas app](create-blank-app.md) </br> **NOTE**: [Power Apps](https://make.powerapps.com) > **Apps** > **New app** > **Canvas** also creates a blank canvas app. | Yes |
| [Canvas apps from template](get-started-test-drive.md) | No |
| Canvas apps created by [customizing SharePoint forms](customize-list-form.md) | No |
| Canvas apps created directly from [Azure portal](https://portal.azure.com) using [Azure SQL Database](app-from-azure-sql-database.md) | No |

## Supported entry points for cloud flows

There are different entry points for creating cloud flows. The following table summarizes which entry points are suppported by the switch for creat

| Entry point | Available for cloud flows within a solution by default?  |
| - | - |
| [Create a cloud flow from blank](/power-automate/get-started-logic-flow) | Private Preview |
| [Create a cloud flow from a template](/power-automate/get-started-logic-template) | Private Preview |
| Create a cloud flow from API | Private Preview |
| Create a cloud flow from Power Automate Management connector | Private Preview |
| Create a cloud flow from PowerShell | Private Preview |
| [Create a cloud flow from OneDrive](/power-automate/onedrive-business-launch-panel) | No |
| [Create a cloud flow from SharePoint](https://support.microsoft.com/en-us/office/create-a-flow-for-a-list-or-library-a9c3e03b-0654-46af-a254-20252e580d01) | No |
| Create a cloud flow from other integration points, such as [the Excel add-in](/business-applications-release-notes/april18/microsoft-flow/build-run-flows-excel) | No | 

## Enable the feature

This feature is disabled by default and must be enabled manually. To enable this feature, go to Power Platform admin center by going to **Environments** > select an environment > **Settings** > **Product** > **Features**, and view the **Create in Dataverse solutions** switches. Toggle on the desired switch: Canvas apps and/or Cloud flows. More information: [Manage feature settings](/power-platform/admin/settings-features)

![image](https://user-images.githubusercontent.com/13593424/202789228-877e69a0-5b83-459b-afe3-63fb1fe37e3d.png)

## Check canvas apps and cloud flows in solutions

To view canvas app and cloud flow objects inside a solution, use the [solution view](../data-platform/solutions-area.md). Only users that have access to the object added inside a solution can view it in a solution view.

## Export and import via solutions

Once this feature is enabled, consider using solutions [export](../data-platform/export-solutions.md) and [import](../data-platform/import-update-export-solutions.md) instead of [export and import of canvas app packages](export-import-app.md). 

## Considerations

- Increase in capacity consumption of Dataverse environment and cost implications due to that increased capacity consumption. 
- Known solution limitations related to canvas apps still apply to canvas apps created within solutions by default. 
- This feature also enables the automatic creation of environment variables when adding data sources for your apps. 
- By default, this feature saves all canvas apps to the default solution named **Common Data Services Default Solution** published by **Microsoft Dataverse Default Publisher**. However, we recommend that you use a non-default solution for canvas apps. To learn about adding existing canvas apps to solutions, see [Add an existing canvas app to a solution](add-app-solution.md#add-an-existing-canvas-app-to-a-solution).
- When you toggle the feature switch in the Power Platform admin center, the Dataverse property `enablecanvasappsinsolutionsbydefault` in the organization table is updated.  The value can be reviewed using the following sample ODATA snippet: `[org URI]/api/data/v9.0/organizations`. More information: [Organization table reference](/power-apps/developer/data-platform/reference/entities/organization)
- If you're planning to change the prefix for the default publisher, or solution for your environment, see [Solution publisher prefix](/power-platform/alm/solution-concepts-alm#solution-publisher-prefix), [Create solution publisher prefix](../data-platform/create-solution.md#create-a-solution-publisher) and [Change solution publisher prefix](../data-platform/create-solution.md#change-a-solution-publisher).

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
