---
title: Environment lifecycle for link to Fabric and long-term retention
description: Understand how environment copy, restore, move, delete, recover, and reset operations affect link to Microsoft Fabric sync and long-term retained data.
author: anibakore-msft
ms.author: banirud
ms.reviewer: matp
ms.service: powerapps
ms.subservice: dataverse-maker
ms.topic: concept-article
ms.date: 11/02/2026
ms.custom: template-concept
ai-usage: ai-assisted
---

# Environment lifecycle for link to Fabric and long-term retention

When you copy, restore, edit, move, delete, recover, or reset a Power Platform environment, the operation can affect link to Microsoft Fabric and long-term retention. Use this article to plan the operation and identify what you need to do afterward. The guidance covers operations on Microsoft Dataverse environments and finance and operations apps environments.

In this article, *synced data* means the replica managed by link to Fabric. *Retained data* means inactive data archived through long-term retention. For Azure Synapse Link profiles that export to your own storage, see [Azure Synapse Link environment lifecycle behavior](azure-synapse-link-olc.md).

## General principle

*Treat link configuration, synced data, and retained data as separate outcomes of an environment operation.* Keeping a link doesn't mean that sync continues without reinitialization, and copying an environment doesn't transfer its retained data.

- *Link configuration:* Whether you need to create a new Fabric link depends on the operation and whether you perform it on the Dataverse environment or the finance and operations apps environment.
- *Synced data:* After a copy or restore, all linked tables in the target environment start a full initial sync, even if the link remains.
- *Retained data:* A copy doesn't copy the source's retained data. A restore returns retained data to the restore point.

> [!WARNING]
> A full copy removes any existing retained data in the target environment. A restore removes records archived after the restore point from the retained-data lake. Review these effects before you start; a full resync doesn't bring back retained data excluded by the operation.

## Copy or restore an environment

The following table shows what happens to the Fabric link when you copy or restore a Dataverse environment or a finance and operations apps environment. The *source* is the environment you copy or restore from, and the *target* is the environment that receives the data.

| Operation | Dataverse | Finance and operations apps |
|-----------|-----------|-----|
| Copy | The target's Fabric link is removed. [Create a new link](fabric-link-to-data-platform.md#create-a-link-to-fabric) in the target. The source's link remains intact and continues syncing. | Fabric links remain intact in both the source and target. The source continues syncing. |
| Restore | The target's existing Fabric link is removed. Create a new link in the target. | The Fabric link remains intact. |

> [!NOTE]
> After a copy or restore of either environment, link to Fabric reinitializes sync in the target. All linked tables go through a full initial sync and post-processing, even if the link remains intact. Large tables can take significant time to complete. Plan downstream reporting accordingly.

For [edit](azure-synapse-link-olc.md#edit-the-properties-of-an-environment), [move to another tenant](azure-synapse-link-olc.md#move-an-environment), [recover](azure-synapse-link-olc.md#recover-an-environment), and [reset](azure-synapse-link-olc.md#reset-an-environment) operations, link to Fabric follows the behavior described in [Azure Synapse Link environment lifecycle operations](azure-synapse-link-olc.md).

For instructions on copy and restore operations, see [Copy an environment](/power-platform/admin/copy-environment) and [Back up and restore environments](/power-platform/admin/backup-restore-environments).

## Long-term retained data after a copy or restore

The following behavior applies to retained data in both Dataverse and finance and operations apps environments. It's separate from whether the Fabric link remains.

| Operation | What happens to retained data | What to expect |
|-----------|-------------------------------|----------------|
| Full copy. | The source's retained data isn't copied to the target environment's lake. Any existing retained data in the target is removed. | Don't expect the target to contain the source's retained history. |
| Restore. | Retained data is restored to the restore point. Records archived between the restore point and the time of the restore are removed from the lake. | Expect retained history as of the restore point, not the time you start the restore. |

> [!NOTE]
> Minimal copy (customizations and schemas only) isn't supported for long-term retained data.

Retention policy definitions and retained records aren't the same thing. You can transport policy definitions in solutions, but solutions don't transport retained records. For more information, see [Solution-aware retention policies](data-retention-overview.md#solution-aware-retention-policies).

## What to expect during resync

After a copy or restore, sync in the target starts again from the beginning. A link that remains intact still requires a full resync; it doesn't resume from its previous position.

1. If the operation removes the Fabric link, [create a new link](fabric-link-to-data-platform.md#create-a-link-to-fabric) in the target environment before expecting data to sync.
2. Monitor all required tables. Each table goes through initial sync and then post-processing before sync completes.
3. Allow time for large tables to finish. Completion time depends on data volume and workload; don't assume that environment copy or restore completion means the data is ready in Fabric.
4. Verify that all required tables finish syncing and that downstream reports use the expected environment and data before you rely on them.

For more information about sync status and performance, see [Manage a link to Fabric](fabric-link-to-data-platform.md#manage-link-to-fabric) and [Plan your latency for link to Fabric](fabric-link-plan-latency.md).

## Delete an environment

When you [delete an environment](/power-platform/admin/delete-environment), all link to Fabric synced data is removed, and sync stops. This rule applies to operations on both Dataverse and finance and operations apps environments. Don't rely on the link to Fabric replica as an independent backup of the deleted environment.

This behavior differs from [Azure Synapse Link deletion behavior](azure-synapse-link-olc.md#delete-an-environment): sync stops, but data already written to your Azure Synapse Analytics workspace or Azure Data Lake remains available.

## Related content

- [Create a link to Microsoft Fabric](fabric-link-to-data-platform.md).
- [Dataverse long-term data retention overview](data-retention-overview.md).
- [Manage Azure Synapse Link during environment lifecycle events](azure-synapse-link-olc.md).
