---
title: Monitoring dashboard (preview)
description: Learn how to use the Link to Fabric monitoring dashboard to check connection health, table sync status, errors, and seven days of daily health snapshots.
author: anibakore-msft
ms.author: banirud
ms.reviewer: matp
ms.service: powerapps
ms.subservice: dataverse-maker
ms.topic: how-to
ms.date: 11/11/2026
ms.custom: template-how-to
ai-usage: ai-assisted
---
# Monitoring dashboard (preview)

[!INCLUDE [preview-banner](../../../shared/preview-includes/preview-banner.md)]

Use the Link to Fabric monitoring dashboard to check connection health, table sync status, detailed errors, and seven days of health snapshots in one view. The dashboard helps you identify issues and understand what needs your attention.

[!INCLUDE [cc-preview-features-definition](../../../shared/preview-includes/preview-note-pp.md)]

This initial public preview supports only Link to Fabric connections that use [low-latency sync](fabric-link-to-data-platform.md#low-latency-sync). Other sync modes and Azure Synapse Link aren't included.

> [!NOTE]
>
> - The public preview is scheduled to begin rolling out on November 16, 2026, with availability across regions expected within one month. This timeline is subject to change.
> - Capabilities and displayed information might change as the preview evolves. This release focuses on in-product visibility and isn't an announcement of proactive alerts or notifications. Programmatic access to the dashboard's monitoring information is planned for future revisions, so you can integrate it into your own dashboards and monitoring tools.

## Open the dashboard

Before you begin, [create a link to Fabric](fabric-link-to-data-platform.md#create-a-link-to-fabric) that uses low-latency sync.

1. Sign in to [Power Apps](https://make.powerapps.com) and select your environment.
2. On the left navigation pane, select **Link data**. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
3. Select your Link to Fabric link that uses low-latency sync to open its monitoring dashboard.

## Understand your link's overall health

The summary at the top of the dashboard gives you an overview of the active link.

| Summary indicator | What it tells you |
|---|---|
| **Overall health** | A summary of link and table sync health. Use the sections below it to understand individual issues. |
| **Tables syncing** | How many tables are reported as syncing healthily. |
| **Tables delayed (>60 min)** | How many tables are reported as delayed beyond the dashboard's 60-minute threshold. |
| **Tables failed** | How many tables have a reported sync failure. |
| **Link errors** | How many errors are reported against the link's connection components. |

Use this summary to decide where to look next. A link-level error points you toward the connection checks. A delayed or failed table points you toward that table's sync details.

:::image type="content" source="media/Fabric/monitoring-dashboard1.png" alt-text="Screenshot of the monitoring dashboard showing overall health, link-level status, and table sync status." lightbox="media/Fabric/monitoring-dashboard1.png":::

*Draft dashboard screenshot. Labels might change before release. Counts and timestamps are examples from the environment shown.*

## Check the connection separately from table sync

The **Link Level Status** pane helps you check whether the connection components are working. In this preview, the pane shows Fabric shortcut availability.

If the Fabric shortcuts status indicates that shortcuts aren't created, select **Refresh Fabric tables** on the command bar. This action refreshes the Fabric shortcuts and is particularly useful when you migrate from an older version of Link to Fabric.

Available Fabric shortcuts don't, by themselves, mean every table is healthy. Use the table-level status to check the sync health of individual tables.

## Understand each table's sync status

The **Table Sync Status** section brings together health, sync state, key timestamps, source and destination row counts, and error details for individual tables.

Start with the health indicator.

| Status | What it means | What to do |
|---|---|---|
| **Healthy** | The table's sync is reported as healthy. | Use this status as the primary signal of sync health. A difference in displayed row counts alone doesn't override this status. |
| **Delayed** | The table is reported as delayed. The dashboard identifies delays greater than 60 minutes. | Review the sync timestamps, error details if present, and recent history. A delay isn't the same as a failed sync. |
| **Failed** | A sync failure has been reported for the table. | Read the detailed error to understand the issue and whether it requires your action. |

> [!IMPORTANT]
> The 60-minute delay threshold is a dashboard health indicator, not a sync latency commitment or service-level agreement (SLA). For latency planning guidance, see [Plan your latency for link to Fabric](fabric-link-plan-latency.md).

Use the additional fields to put the status in context.

| Field | How to read it |
|---|---|
| **Current State** | The reported sync state for the table. Read it alongside the health indicator. |
| **Entity Addition Time** | When the table was added to the link. |
| **Initial Sync Completed Time** | When the table's initial full sync completed. |
| **Last Delta Sync Time** | The reported time of the table's most recent incremental sync. |
| **Last Source Modified** | The reported source modification time in Microsoft Dataverse, providing context for source activity. |
| **Source Rows** | A point-in-time estimate of the record count in the Dataverse source, not its exact current state. |
| **Destination Rows** | A point-in-time estimate of the record count in the destination, not its exact current state. |
| Error details | Information about a reported sync failure, helping you understand what happened and whether action is needed. |

The timestamps provide context, but don't use a single timestamp or row count in isolation to decide whether sync has failed.

## Interpret record count estimates

Source and destination record counts shown in the dashboard are point-in-time estimates. They don't represent the exact current state of either system and aren't updated continuously.

The target for count freshness is to reflect data from within the last hour. This target isn't a guaranteed hourly refresh or a live, transaction-by-transaction comparison.

Differences in displayed record counts don't, on their own, indicate a sync issue. The estimates might reflect different moments while data continues to change and sync. For example, the source snapshot might include recent changes that aren't yet reflected in the destination snapshot. The displayed counts can differ even when the table's sync is healthy.

Use the table's **Healthy**, **Delayed**, or **Failed** status as the primary signal of sync health. Health status is separate from row-count freshness. It doesn't mean that the displayed counts must match or that every record is reconciled.

Before you raise a support ticket about a count difference:

- Review the table's sync health, timestamps, and error details.
- Validate the suspected discrepancy against the underlying data, taking snapshot timing into account.
- Don't raise a ticket based solely on a difference between the displayed estimates.

## Review error details when a sync fails

The dashboard surfaces detailed errors for failed table syncs. Some errors resolve on their own. Others need your help. Review the error details and any indicated customer action before you decide what to do next.

Don't assume that every error needs intervention or that every failed sync recovers without it. Use the details to make that distinction.

## Review seven days of daily health snapshots

The **Last 7 Days - Daily Health Summary** captures a snapshot once every 24 hours, at 00:00 UTC (midnight UTC). Each dated entry reflects the sync health of your tables and link at that moment, not a summary of health throughout the day.

Each snapshot shows the following values at the time it was taken:

- Overall health.
- Tables syncing.
- Tables delayed beyond the displayed threshold.
- Tables failed.
- Link errors.

Compare delayed or failed table counts and link errors across dates to identify repeated unhealthy checkpoints and prioritize investigation. After you take corrective action, review later snapshots to see whether reported health has improved at those checkpoints.

Health might fluctuate between snapshots. Issues that occur and resolve between them might not appear in the history. Repeated unhealthy snapshots don't prove that the same issue persisted continuously. A **Healthy** entry doesn't mean sync remained healthy throughout that day.

The following screenshots show table sync details and daily health snapshots.

:::image type="content" source="media/Fabric/monitoring-dashboard2.png" alt-text="Screenshot of table sync status showing table health, sync state, timestamps, and source row counts." lightbox="media/Fabric/monitoring-dashboard2.png":::

:::image type="content" source="media/Fabric/monitoring-dashboard3.png" alt-text="Screenshot of the seven-day daily health summary showing overall health, syncing tables, delayed tables, failed tables, and link errors for each date." lightbox="media/Fabric/monitoring-dashboard3.png":::

> [!IMPORTANT]
> Each daily entry captures sync health at 00:00 UTC. It isn't a full-day health summary, a record-by-record reconciliation, or a complete event history.

## Use the dashboard to investigate sync health

Follow this sequence to investigate an issue.

1. Start with overall health. Check whether the dashboard reports delayed tables, failed tables, or link errors.
2. Check the link components. If the connection or shortcuts have an issue, review those details.
3. Review affected tables. Use table health, sync state, timestamps, and error details together.
4. Treat record counts as estimates. They don't represent the exact current state. Verify any suspected discrepancy before you raise a support ticket.
5. Compare the seven days of daily health snapshots. Review health at the midnight UTC checkpoints, keeping in mind that these snapshots don't capture every change during the day.

## Related information

- [Create a link to Fabric](fabric-link-to-data-platform.md)
- [Plan your latency for link to Fabric](fabric-link-plan-latency.md)
- [Troubleshoot link to Fabric](fabric-troubleshoot.md)
