---
title: Migrate an existing Fabric link to low-latency sync
description: Learn how to migrate an existing Dataverse Link to Microsoft Fabric to low-latency sync, check prerequisites, and resolve common migration issues.
author: anibakore-msft
ms.author: banirud
ms.reviewer: matp
ms.service: powerapps
ms.subservice: dataverse-maker
ms.topic: how-to
ms.date: 11/23/2026
ms.custom: template-how-to
ai-usage: ai-generated
---
# Migrate an existing Fabric link to low-latency sync

If you already use Link to Microsoft Fabric with Microsoft Dataverse, use **Migrate now** to move your existing link to [low-latency sync](fabric-link-to-data-platform.md#low-latency-sync). Low-latency sync provides faster initial and incremental sync.

This article applies to existing Fabric links. To create a new link, see [Link to Microsoft Fabric](fabric-link-to-data-platform.md).

## How migration works

Migration switches your Fabric shortcuts to data that's already being synchronized through low-latency sync. It doesn't restart synchronization or trigger another initial sync.

1. Your data is already syncing through low-latency sync in the background before **Migrate now** appears. The service verifies that this sync is working before making migration available.
2. After you select **Migrate now** and confirm migration, the service deletes the shortcuts associated with your existing Fabric link.
3. The service switches your Fabric link to the existing low-latency sync and creates replacement shortcuts for your linked tables.

> [!IMPORTANT]
> Migration is a one-way operation. After your link switches to low-latency sync, the service permanently deletes the old synchronized data copy maintained by the previous sync. You can't revert to the previous sync. Your source data in Dataverse remains unchanged.

> [!NOTE]
> If new shortcut creation fails after your link switches to low-latency sync, wait until the migration attempt is no longer running, and then select **Refresh Fabric tables** to create the missing shortcuts. You don't need to migrate again. If shortcuts are still missing after the refresh, contact [Microsoft customer support](/power-platform/admin/get-help-support).

## Prerequisites

Before you migrate, complete these checks:

- **Working link and connection.** Confirm that your existing Fabric link works and that you can use its connection for the correct Dataverse environment. Resolve existing sync or access issues first; migration doesn't fix them. If the connection is invalid or unavailable, [update the connection](fabric-link-to-data-platform.md#update-the-connection-used-by-an-existing-fabric-link) before you start.
- **Required permissions.** Use an account with the same permissions required to create a Fabric link: the System Administrator security role in Dataverse, administrator access to the Fabric workspace, and Capacity Contributor or capacity administrator access to its capacity. Confirm that you can access the connection and lakehouse. For the full requirements, see [Prerequisites for Link to Fabric](fabric-link-to-data-platform.md#prerequisites).
- **Supported finance and operations build, if applicable.** If your link includes finance and operations apps tables, check the [minimum supported builds](fabric-link-to-data-platform.md#prerequisites-for-finance-and-operations-apps).
- **Tested migration.** Test the migration in a nonproduction environment before you migrate your production environment.

> [!NOTE]
> Before you select **Migrate now**, hold **Ctrl** and refresh the Power Apps page so that your latest authentication token is used. Complete any sign-in prompts before you continue.

## Plan for the migration

Migration replaces your existing Fabric shortcuts with shortcuts that use low-latency sync. Schedule migration during a maintenance window: the linked Fabric workspace is unavailable while migration is in progress, and the duration depends on your data volume. Don't use the workspace until migration completes. Validate your reports, queries, pipelines, and semantic models afterward.

Review the [differences between low-latency sync and earlier Fabric links](fabric-link-faq.yml#differences-between-low-latency-sync-and-earlier-fabric-links) before you begin. These differences include changes to choice metadata, Delta Lake compatibility, and empty-string handling. Also check any downstream readers that depend on the earlier INT96 timestamp format: low-latency sync uses INT64 timestamps.

> [!IMPORTANT]
> Don't unlink and relink to start or recover a migration. Unlinking removes the Fabric lakehouse and its shortcuts. Use the migration action when it's available, or contact [Microsoft customer support](/power-platform/admin/get-help-support) if you can't proceed.

> [!NOTE]
> **Unlink** and **Refresh Fabric tables** aren't allowed while migration is in progress. Wait until the migration attempt is no longer running before you use either action.

If you need to change the connection before migration, be aware that **Update connection** can remove existing shortcuts when the link is ready to migrate. Proceed with migration to create the low-latency shortcuts. If you must defer migration but need the existing shortcuts restored, contact Microsoft customer support.

## Migrate your existing link

Start migration when **Migrate now** is available for your link. If the link already shows **Low-latency mode**, use [Verify the migration](#verify-the-migration) instead.

1. Sign in to [Power Apps](https://make.powerapps.com) and select the environment that contains your Fabric link.
2. On the left navigation pane, select **Link data**, and then locate your existing link under **Fabric Links**. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
3. Hold **Ctrl** and refresh the page so that your latest authentication token is used. Complete any sign-in prompts before you continue.
4. Select **Migrate now** in the migration banner. Depending on your experience, the migration action might be labeled **Migrate shortcuts**.

   :::image type="content" source="media/Fabric/migrate-option.png" alt-text="Screenshot of the Link data page with the migration banner and Migrate now button." lightbox="media/Fabric/migrate-option.png":::

5. In the confirmation dialog, review the downtime notice and prerequisites. If you already attempted migration and an error occurred, the dialog displays the error details. The following example shows a shortcut deletion error. Use [Common errors and resolutions](#common-errors-and-resolutions) to choose the appropriate recovery action.

   :::image type="content" source="media/Fabric/migrate-low-latency-dialog.png" alt-text="Screenshot of the migration confirmation dialog showing the downtime notice, confirmation checkbox, and an error from a previous migration attempt." lightbox="media/Fabric/migrate-low-latency-dialog.png":::

6. Select the checkbox to confirm that you tested migration in a nonproduction environment, understand the expected downtime, and read the prerequisites. Then select **Accept and migrate now**.
7. Wait for migration to finish. Keep the dialog open, and don't perform other actions while migration is in progress. Don't start another migration from a different browser tab or repeatedly select the migration action. If a request times out, refresh the page to check the current status before you take another action.

   :::image type="content" source="media/Fabric/migrate3.png" alt-text="Screenshot of the migration dialog showing that migration is in progress and the action buttons are disabled." lightbox="media/Fabric/migrate3.png":::

8. When migration completes, a success notification appears on the link details page. Confirm that your link shows **Low-latency mode** on the **Link data** page, and then verify the shortcuts and data in Fabric.

   :::image type="content" source="media/Fabric/migrate4.png" alt-text="Screenshot of the Link to Fabric details page with a notification that migration to low-latency sync completed successfully." lightbox="media/Fabric/migrate4.png":::

If the migration action is missing, disabled, or reports that the link isn't ready, confirm that your existing Fabric link works and resolve any existing issues first. Migration doesn't fix existing sync or access issues. Then refresh the page. If the action remains unavailable and the link isn't already using low-latency sync, contact Microsoft customer support.

## Verify the migration

Check both the link and the data before you resume dependent workloads:

1. On the **Link data** page, confirm that your Fabric link shows **Low-latency mode**.
2. Open the Fabric lakehouse and confirm that the expected table shortcuts are present and readable. If shortcuts are missing after the link switches to low-latency sync, select **Refresh Fabric tables** in Power Apps. If they're still missing, contact Microsoft customer support.
3. Confirm that the expected tables have completed initial sync and that recent Dataverse changes appear in Fabric. Where available, use the [monitoring dashboard (preview)](fabric-link-monitoring-dashboard.md) to review table sync health and errors. A difference in displayed row-count estimates alone doesn't indicate a sync failure.
4. Validate the SQL analytics endpoint and your downstream reports, queries, pipelines, and semantic models. If shortcuts are readable but SQL tables are missing or stale, refresh the SQL analytics endpoint metadata in Fabric or wait for endpoint sync.

> [!NOTE]
> After a successful migration, the SQL analytics endpoint can take up to six hours to refresh its metadata and cached data, depending on load. During this time, endpoint tables might appear missing or stale even when the Fabric shortcuts are readable. This delay doesn't mean that migration failed.
>
> **Refresh Fabric tables** creates or repairs Fabric shortcuts and updates table metadata. It doesn't repair source data sync or refresh SQL analytics endpoint metadata. Don't run migration again to resolve data-access issues after migration completes.

## Common errors and resolutions

Use the current status and error message to choose your next action. If migration is still running, you can't use **Unlink** or **Refresh Fabric tables**. Retry migration only when the migration action is offered. After the migration attempt finishes and the link switches to low-latency sync, use **Refresh Fabric tables** for missing shortcuts rather than migrating again.

| Error or symptom | Resolution |
|---|---|
| **Migrate now** is missing, disabled, or reports that the link isn't ready. | Ensure that your existing Fabric link works. Resolve existing sync, connection, or access issues first; don't assume that migration fixes them. Then refresh the page and check whether the link already shows **Low-latency mode**. If it doesn't and migration remains unavailable, contact Microsoft customer support. Don't unlink and relink to make the action appear. |
| You selected **Migrate now**, but progress stops or the request times out. | Refresh the page to check the current status. Wait while migration is progressing. Retry only when the migration action is offered. A timeout doesn't necessarily mean that migration stopped. Contact support if progress doesn't resume. |
| The request reports **Already migrating**, including an HTTP 409 response that indicates an active migration. | Refresh the page and wait for the active migration to finish. Avoid parallel requests from multiple tabs. If the status remains stuck, contact support rather than repeatedly retrying. An HTTP 409 can also indicate a shortcut conflict; check the error details before choosing a recovery action. |
| The error says that the existing shortcuts couldn't be deleted. | Wait briefly, and then retry **Migrate shortcuts** when it's offered. Don't use **Refresh Fabric tables** for this failure. If old shortcuts remain, follow [Resolve conflicts caused by old shortcuts](#resolve-conflicts-caused-by-old-shortcuts) before contacting support. |
| The error says that shortcuts were deleted but the Fabric profile couldn't be updated. | Retry **Migrate shortcuts** when it's offered. Don't manually recreate the old shortcuts. If the action is unavailable or the retry fails, contact support. |
| The error says that not all new shortcuts could be created, or shortcuts are missing after the link shows **Low-latency mode**. | Select **Refresh Fabric tables** on the active Fabric link. Don't run migration again. If refresh is blocked or shortcuts are still missing, contact support. |
| The connection is invalid, can't be found, or its credentials no longer work. | On the currently linked profile, select **Update connection** and choose a valid connection for this Dataverse environment. Confirm that you can access it. Then retry the appropriate action: migration if it's still offered, or **Refresh Fabric tables** after the link switches to low-latency sync. |
| Migration or refresh fails with **Access denied**, **Unauthorized**, or HTTP 403. | Ask your administrator to verify your [required permissions](#prerequisites), including connection, workspace, and lakehouse access. Refresh the Power Apps page and complete any sign-in prompts. Retry the same action after access is restored. |
| **Refresh Fabric tables** tells you to select **Migrate now**. | Migrate the shortcuts first, and then use **Refresh Fabric tables** if shortcuts are still missing. If you must defer migration but need to refresh existing shortcuts, contact support for assistance. |
| Expected or newly added tables are missing. | Confirm that the tables are selected in **Manage tables** and that initial sync has finished. Then use **Refresh Fabric tables** on the active low-latency link. If the tables remain missing, contact support. |
| Shortcuts exist, but data is empty, stale, incorrect, or inaccessible. | Check the connection, permissions, and affected tables' sync health. Resolve any reported connection or sync errors. Don't migrate again. If the issue persists, contact support with the affected table names. |
| Shortcuts are readable, but SQL analytics endpoint tables are missing or stale. | After a successful migration, allow up to six hours for the endpoint to refresh its metadata and cached data, depending on load. You can also refresh the SQL analytics endpoint metadata in Fabric. This action is different from **Refresh Fabric tables** in Power Apps. If the tables are still missing or stale after six hours, contact support. Don't migrate again. |
| **Update connection** repeatedly fails, or shortcut access remains broken afterward. | Contact support. Don't move the lakehouse, unlink and relink, or run migration again as a workaround. |
| A shortcut-name conflict is reported, possibly with an HTTP 409 response. | Check whether shortcuts from the old Fabric link were deleted. If they remain, follow [Resolve conflicts caused by old shortcuts](#resolve-conflicts-caused-by-old-shortcuts). Don't delete unrelated or replacement shortcuts. If no old shortcuts remain or the conflict persists, contact support. |
| **Unlink** or **Refresh Fabric tables** is rejected during migration. | These actions aren't allowed while migration is in progress. Wait for the migration attempt to stop running. If migration is stuck, contact support. Don't use unlinking and relinking as a recovery step. |

### Resolve conflicts caused by old shortcuts

If shortcut deletion fails or a shortcut conflict occurs, check the old shortcuts before you raise a support ticket:

1. Confirm that the migration attempt is no longer running. Don't manually delete shortcuts during an active migration.
2. In the Fabric lakehouse, check whether shortcuts associated with the old Fabric link remain. If you can't identify them confidently, contact support instead of deleting shortcuts.
3. Check dependencies on the lakehouse and its shortcuts, including pipelines and notebooks. Use [lineage view](/fabric/governance/lineage) and inspect pipeline and notebook references. Before you delete old shortcuts, ensure that no dependent items reference the lakehouse or its shortcuts. Update or remove those references first.
4. Manually delete only the remaining shortcuts associated with the old Fabric link. Don't delete the lakehouse, replacement low-latency shortcuts, or unrelated shortcuts. Then retry **Migrate shortcuts** only if it's offered. If the link has already switched to low-latency sync, use **Refresh Fabric tables** instead.

If the conflict persists after these checks, contact Microsoft customer support. Include the shortcut names and the dependency checks you completed.

## Get help

If the issue persists, contact [Microsoft customer support](/power-platform/admin/get-help-support). Include the following information:

- The error message and correlation or reference ID, if shown.
- The time of the failure in UTC.
- The Dataverse environment and Fabric workspace and lakehouse identifiers.
- The affected table names and whether their shortcuts are missing or unreadable.
- The current migration status, whether **Low-latency mode** is shown, and the actions you already tried.
- A sanitized HTTP Archive (HAR) file containing the browser network requests and responses from the failure, so support can trace the exact error. Start recording in your browser's developer tools before the failing action, and export the recording after the error appears. Don't restart an active or completed migration solely to capture a trace.

> [!IMPORTANT]
> HAR files can contain authentication headers, cookies, and customer data. Export a sanitized HAR file and review it before sharing. Remove passwords, authentication tokens, cookies, connection secrets, and sensitive customer data. Share diagnostic files only through the secure upload method provided for your support case.

## Related information

- [Link to Microsoft Fabric](fabric-link-to-data-platform.md)
- [Low-latency sync](fabric-link-to-data-platform.md#low-latency-sync)
- [Fabric link for Dataverse FAQ](fabric-link-faq.yml)
- [Monitoring dashboard (preview)](fabric-link-monitoring-dashboard.md)
- [Troubleshoot link to Fabric](fabric-troubleshoot.md)
