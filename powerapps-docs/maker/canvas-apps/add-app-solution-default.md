---
title: Add canvas apps and cloud flows to a solution by default (preview)
description: Learn how to configure an environment to add new canvas apps and cloud flows to a solution by default.
author: ChrisGarty
ms.author: cgarty
ms.reviewer: angieandrews
ms.topic: conceptual
ms.custom: canvas, bap-template
ms.date: 04/04/2023
ms.subservice: canvas-maker
search.audienceType: 
  - maker
contributors:
  - mduelae
---

# Add canvas apps and cloud flows to a solution by default (preview)

[This article is prerelease documentation and is subject to change.]

You can [create a canvas app in a solution](add-app-solution.md) in Power Apps or [create a cloud flow in a solution](/power-automate/create-flow-solution) in Power Automate. Creating a canvas app or a cloud flow in a solution previously required manual steps. Now you can create them in a solution by default.

Because canvas apps and cloud flows in a solution are defined in Microsoft Dataverse, you can use Dataverse capabilities to manage them, including [connection references](/power-apps/maker/data-platform/create-connection-reference), [environment variables](/power-apps/maker/data-platform/environmentvariables), the [Dataverse API](/power-apps/developer/data-platform/webapi/overview), [role-based security](/power-platform/admin/database-security#environments-with-a-dataverse-database), and solution-based [application lifecycle management (ALM)](/power-platform/alm).

> [!IMPORTANT]
> This is a preview feature. [!INCLUDE [cc_preview_features_definition](../../includes/cc-preview-features-definition.md)]

## Prerequisites

- Solutions are stored in Dataverse, so the environment must have a Dataverse database to use this feature. If yours doesn't, [add a Dataverse database](/power-platform/admin/create-database).
- To create canvas apps in solutions, you must have **Write** privileges to the [CanvasApp table](../../developer/data-platform/reference/entities/canvasapp.md). To create cloud flows in solutions, you should have the [Environment Maker role](/power-platform/admin/database-security#predefined-security-roles). For more information, see [security roles and privileges](/power-platform/admin/security-roles-privileges).
- A canvas app or cloud flow in a solution must be shared with you before you can view or edit it.

> [!IMPORTANT]
> Before you enable the creation of canvas apps and cloud flows in solutions by default, review the [considerations](#considerations).

## Supported creation methods and entry points

Several methods and entry points are available for creating canvas apps and cloud flows. 

### Canvas apps creation methods and entry points

The following table summarizes the methods that allow you to create canvas apps in a solution by default.

| Method | Available for canvas apps in a solution by default? |
| --- | --- |
| [Create a canvas app from Dataverse](data-platform-create-app.md) | Yes |
| Create a canvas app from other data sources, such as [SharePoint](app-from-sharepoint.md), [Excel](get-started-create-from-data.md), [Azure Blob Storage](connections/connection-azure-blob-storage.md), and [others](connections-list.md#popular-connectors) | Yes |
| [Create a blank canvas app](create-blank-app.md)</br> **NOTE**: [Power Apps](https://make.powerapps.com) > **Apps** > **New app** > **Canvas** also creates a blank canvas app. | Yes |
| [Create a canvas app from a template](get-started-test-drive.md) | No |
| Create a canvas app by [customizing SharePoint forms](customize-list-form.md) | No |
| Create a canvas app directly from [Azure portal](https://portal.azure.com) using [Azure SQL Database](app-from-azure-sql-database.md) | No |

### Cloud flows creation methods and entry points

The following table summarizes the methods that allow you to create cloud flows in a solution by default.

| Method | Available for cloud flows in a solution by default? |
| --- | --- |
| [Create a cloud flow from blank in a portal](/power-automate/get-started-logic-flow) | Yes |
| [Create a cloud flow from a template in a portal](/power-automate/get-started-logic-template) | Yes |
| Create a cloud flow from Power Automate Management connector | Yes |
| Create a cloud flow from PowerShell | Yes |
| Create a cloud flow from Power Apps | Yes |
| [Create a cloud flow from Teams](/power-automate/teams/teams-app-create) | Yes |
| [Create a cloud flow from OneDrive](/power-automate/onedrive-business-launch-panel) | Yes |
| Create a cloud flow from Dynamics 365 | Yes |
| [Create a cloud flow from the Excel add-in](/business-applications-release-notes/april18/microsoft-flow/build-run-flows-excel) | Yes |
| [Create a cloud flow from the Power Automate mobile app](/power-automate/mobile/mobile-create-flow) | Yes |
| [Create a cloud flow from SharePoint](https://support.microsoft.com/office/create-a-flow-for-a-list-or-library-a9c3e03b-0654-46af-a254-20252e580d01) | No, ETA August |
| Create a cloud flow from Project Roadmap | No, ETA September |

> [!IMPORTANT]
> Unsupported entry points will fail to create any cloud flow until that support is added to create a solution cloud flow with that entry point. You must first create a cloud flow in a solution using a supported method.

## Enable the feature

This feature is disabled by default. You must enable it before you can use it.

1. Sign in to the Power Platform admin center and select an environment.
1. Go to **Settings** > **Product** > **Features**.
1. Under **Create new canvas apps and cloud flows in Dataverse solutions (Preview`)**, turn on **Canvas apps** and **Cloud flows** as desired.

[Learn more about managing feature settings](/power-platform/admin/settings-features).

## View canvas apps and cloud flows in solutions

To view canvas app and cloud flow objects in a solution, use the [solution view](../data-platform/solutions-area.md). You must have access to the object added inside a solution to view it in a solution view.

## Export and import using solutions

Once the feature is enabled, use solutions [export](../data-platform/export-solutions.md) and [import](../data-platform/import-update-export-solutions.md) instead of [exporting and importing legacy packages of canvas apps and flows](export-import-app.md). Legacy packages can be imported in environments with the environment setting turned off.

## Considerations

Take the following considerations into account before you decide to create canvas apps and cloud flows in a solution by default.

- Your Dataverse environment capacity consumption and related cost may increase.

- Known solution limitations related to canvas apps still apply to canvas apps created in solutions by default.

- This feature automatically creates environment variables when you add data sources for your apps.

- By default, this feature saves all canvas apps to the default solution, **Common Data Services Default Solution**, published by **Microsoft Dataverse Default Publisher**. However, we recommend that you save your canvas apps to a different solution. [Learn more about adding existing canvas apps to solutions](add-app-solution.md#add-an-existing-canvas-app-to-a-solution).

- When you turn the feature on or off for canvas apps and cloud flows in the Power Platform admin center, the Dataverse properties `enablecanvasappsinsolutionsbydefault` and `enableFlowsInSolutionByDefault` in the organization table are updated. You can view the value of these properties using the following sample ODATA snippet: `[org URI]/api/data/v9.0/organizations`. For more information, see [Organization table reference](/power-apps/developer/data-platform/reference/entities/organization).

- If you're planning to change the prefix for the default publisher or solution for your environment, see [Solution publisher prefix](/power-platform/alm/solution-concepts-alm#solution-publisher-prefix), [Create solution publisher prefix](../data-platform/create-solution.md#create-a-solution-publisher) and [Change solution publisher prefix](../data-platform/create-solution.md#change-a-solution-publisher).

- Non-solution canvas apps and non-solution cloud flows can be added into a solution to add them into Dataverse, but there's no way to revert back.

## Known issues

- The **Monitor** > **Cloud flow activity** page doesn't support solution cloud flows.

- [Audit log events for cloud flow permissions](/power-platform/admin/logging-power-automate#see-audited-events) that provide visibility into sharing aren't updated for solution cloud flows.

- The [List Flows as Admin API](/connectors/flowmanagement/#list-flows-as-admin) doesn't return solution cloud flows that haven't previously been turned on (published). The identifier returned is the Logic Apps ID, and unpublished flows don't have one. This API will be updated later to return all solution cloud flows.

- The [List Flows API](/connectors/flowmanagement/#list-my-flows) doesn't return any solution cloud flows. This will be updated later to return solution cloud flows when the [List Flows as Admin API](/connectors/flowmanagement/#list-flows-as-admin) is updated.

### See also

[Solutions overview](../data-platform/solutions-overview.md)  
[Application lifecycle management (ALM) guide](/power-platform/alm/overview-alm)

[!INCLUDE [footer-include](../../includes/footer-banner.md)]
