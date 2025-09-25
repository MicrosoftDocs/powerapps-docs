---
title: Add canvas apps and cloud flows to a solution by default
description: Learn how to configure an environment to add new canvas apps and cloud flows to a solution by default.
author: ChrisGarty
contributors:
  - ChrisGarty
  - mduelae
ms.author: cgarty
ms.reviewer: angieandrews
ms.topic: how-to
ms.custom: canvas, bap-template
ms.date: 9/25/2025
ms.subservice: canvas-maker
search.audienceType: 
  - maker
---

# Add canvas apps and cloud flows to a solution by default

You can [create a canvas app in a solution](add-app-solution.md) in Power Apps or [create a cloud flow in a solution](/power-automate/create-flow-solution) in Power Automate. Creating a canvas app or a cloud flow in a solution previously required manual steps. Now you can create them in a solution by default.

Because canvas apps and cloud flows in a solution are defined in Microsoft Dataverse, you can use Dataverse capabilities to manage them, including [connection references](/power-apps/maker/data-platform/create-connection-reference), [environment variables](/power-apps/maker/data-platform/environmentvariables), the [Dataverse API](/power-apps/developer/data-platform/webapi/overview), [role-based security](/power-platform/admin/database-security#environments-with-a-dataverse-database), and solution-based [application lifecycle management (ALM)](/power-platform/alm).

> [!IMPORTANT]
> - The canvas apps setting is a preview feature.
> - Preview features aren't meant for production use and might have restricted functionality. These features are subject to [supplemental terms of use](https://www.microsoft.com/en-us/business-applications/legal/supp-powerplatform-preview/), and are available before an official release so that customers can get early access and provide feedback.

## Prerequisites

- Solutions are stored in Dataverse, so the environment must have a Dataverse database to use this feature. If yours doesn't, [add a Dataverse database](/power-platform/admin/create-database).
- To create canvas apps in solutions, you must have **write** privileges to the [CanvasApp table](../../developer/data-platform/reference/entities/canvasapp.md). To create cloud flows in solutions, you should have the [Environment Maker role](/power-platform/admin/database-security#predefined-security-roles). Learn more in [Security roles and privileges](/power-platform/admin/security-roles-privileges).
- A canvas app or cloud flow in a solution must be shared with you before you can view or edit it.

> [!IMPORTANT]
> Before you enable the creation of canvas apps and cloud flows in solutions by default, review the [Considerations](#considerations) section in this article.

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
| Create a canvas app by [customizing SharePoint forms](/sharepoint/dev/business-apps/power-apps/get-started/create-your-first-custom-form) | No |

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
| [Create a cloud flow from SharePoint](https://support.microsoft.com/office/create-a-flow-for-a-list-or-library-a9c3e03b-0654-46af-a254-20252e580d01) | Yes |
| Create a cloud flow from Project Roadmap | Yes |

> [!IMPORTANT]
> Unsupported entry points will fail to create any cloud flow until that support is added to create a solution cloud flow with that entry point. You must first create a cloud flow in a solution using a supported method.

## Enable the feature

This feature is enabled by default for cloud flows, however, it is disabled by default for canvas apps.  You must enable it before you can use it for canvas apps.

1. Sign in to the Power Platform admin center and select an environment.
1. Go to **Settings** > **Product** > **Features**.
1. Under **Create new canvas apps and cloud flows in Dataverse solutions**, turn on **Canvas apps (Preview`)**.

Learn more about managing feature settings in [Manage feature settings](/power-platform/admin/settings-features).

## View canvas apps and cloud flows in solutions

To view canvas app and cloud flow objects in a solution, use the [solution view](../data-platform/solutions-area.md). You must have access to the object added inside a solution to view it in a solution view.

## Export and import using solutions

Once the feature is enabled, use solutions [export](../data-platform/export-solutions.md) and [import](../data-platform/import-update-export-solutions.md) instead of [exporting and importing legacy packages of canvas apps and flows](export-import-app.md). Legacy packages can be imported in environments with the environment setting turned off.

## Move flows into a solution with PowerShell

Use the [Add-AdminFlowsToSolution](/powershell/module/microsoft.powerapps.administration.powershell/add-adminflowstosolution) cmdlet to move non-solution Power Automate flows into a solution for better lifecycle management and deployment. This command lets you migrate multiple flows by specifying environment and solution IDs, and targeting flows by name or ID. For more information, see [Microsoft.PowerApps.Administration.PowerShell Module](/powershell/module/microsoft.powerapps.administration.powershell).

## Considerations

Take the following considerations into account before you decide to create canvas apps and cloud flows in a solution by default.

- Your Dataverse environment capacity consumption and related cost might increase.
- Known solution limitations related to canvas apps still apply to canvas apps created in solutions by default.
- This feature automatically creates environment variables when you add data sources for your apps.
- By default, this feature saves all canvas apps to the default solution, **Common Data Services Default Solution**, published by **Microsoft Dataverse Default Publisher**. However, we recommend that you save your canvas apps to a different solution. [Learn more about adding existing canvas apps to solutions](add-app-solution.md#add-an-existing-canvas-app-to-a-solution).
- When you turn the feature on or off for canvas apps and cloud flows in the Power Platform admin center, the Dataverse properties `enablecanvasappsinsolutionsbydefault` and `enableFlowsInSolutionByDefault` in the organization table are updated. You can view the value of these properties using the following sample ODATA snippet: `[org URI]/api/data/v9.0/organizations`. Learn more in [Organization table reference](/power-apps/developer/data-platform/reference/entities/organization).
- If you're planning to change the prefix for the default publisher or solution for your environment, you can learn more in [Solution publisher prefix](/power-platform/alm/solution-concepts-alm#solution-publisher-prefix), [Create solution publisher prefix](../data-platform/create-solution.md#create-a-solution-publisher) and [Change solution publisher prefix](../data-platform/create-solution.md#change-a-solution-publisher).
- Non-solution canvas apps and non-solution cloud flows can be added into a solution to add them into Dataverse, but there's no way to revert back.

## Improvements

The following scenarios were improved to support cloud flows and canvas apps defined in Dataverse:

- The **Monitor** > **Cloud flow activity** page now supports solution cloud flows.
- The [List My Flows API](/connectors/flowmanagement/#list-my-flows) doesn't return any solution cloud flows.
- [Audit log events for cloud flow permissions](/power-platform/admin/logging-power-automate#see-audited-events) that provide visibility into sharing now include solution cloud flows.
- The [List Flows as Admin API](/connectors/flowmanagement/#list-flows-as-admin) now returns solution cloud flows that weren't previously turned on (published). This API now returns all non-solution and solution cloud flows.
- Flows with delegated authentication to Roadmap can be added into a solution and migrated to Dataverse.
- Flows with delegated authentication to SharePoint can be added into a solution and migrated to Dataverse.

## Is this feature generally available or preview?

As of October 29, 2024, the cloud flows setting is generally available. The canvas apps setting remains in preview.

The cloud flows setting is on by default.

## Does putting flows into Dataverse use Dataverse capacity?

Moderately. Flow definitions use a small amount of Dataverse storage. A large flow definition could reach 10 KB. With this worst case scenario: 10,000 flows x 10 KB = 100 MB or 0.1 GB. The small increase in Dataverse storage used provides significant benefits, since solution cloud flows are needed to leverage capabilities including [application lifecycle management (ALM)](/power-platform/alm/overview-alm), [governance with Dataverse](/power-platform/admin/governance-considerations), [automation center](/power-automate/automation-center-overview), [drafts and versioning](/power-automate/drafts-versioning), and [expanded security capabilities](/power-platform/admin/database-security#environments-with-a-dataverse-database).

### Related information

- [Solutions overview](../data-platform/solutions-overview.md)  
- [Application lifecycle management (ALM) guide](/power-platform/alm/overview-alm)

[!INCLUDE [footer-include](../../includes/footer-banner.md)]

