---
title: "Manage your Azure Synapse Link with Environment Events | MicrosoftDocs"
description: "Learn how to manage your Azure Synapse Link for Dataverse profiles with Environment events."
ms.custom: ""
ms.date: 11/01/2021
ms.reviewer: "Mattp123"

ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "conceptual"
applies_to: 
  - "powerapps"
author: "sabinn-msft"
ms.assetid: 
ms.subservice: dataverse-maker
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
contributors: "sama-zaki"
---

# Manage your Azure Synapse Link during environment lifecycle events



Azure Synapse Link for Dataverse provides a continuous pipeline of data from Dataverse to Azure Synapse Analytics and/or Azure Data Lake. Once the link is created it continuously writes all the initial data as well as any incremental data. When you make changes to your Power Platform environment, this can affect the state of your Azure Synapse Link for Dataverse. This article explains the behavior  of the Azure Synapse Link for Dataverse and possible user action during environment lifecycle events.

> [!NOTE]
> Azure Synapse Link for Microsoft Dataverse was formerly known as Export to data lake. The service was renamed effective May 2021 and will continue to export data to Azure Data Lake as well as Azure Synapse Analytics.

## Environment lifecycle events overview

|Environment operation |Synapse link          |Data                  |User action           |
|----------------------|----------------------|----------------------|----------------------|
|Backup and restore |Stops syncing |Maintained |Use solutions to transport the link across environments |
|Copy |Source continues syncing |Source is maintained |Use solutions to transport the link across environments |
|Delete |Stops syncing |Maintained |None |
|Edit the properties |Error |Maintained |Unlink and relink |
|Move |Source stops syncing |Source is maintained |Use solutions to transport the link across environments |
|Recover |Continue syncing |Maintained |None |
|Reset |Removed |Maintained |Delete data before recreating the link |

## Backup and restore an environment

Azure Synapse Link for Dataverse profiles are not part of an [environment backup or the subsequent restore](/power-platform/admin/backup-restore-environments). Once an environment is restored, use solutions to [export and import the configuration](./azure-synapse-link-solution.md) to preserve the configuration of the Azure Synapse Link across environments.

## Copy an environment

Azure Synapse Link for Dataverse profiles are not copied as part of the [copy an environment](/power-platform/admin/copy-environment) process. To preserve the configuration of the Azure Synapse Link across environments, use solutions to [export and import the configuration](./azure-synapse-link-solution.md).

## Delete an environment

When an [environment is deleted](/power-platform/admin/delete-environment), all Azure Synapse Link profiles are deleted and the data sync is stopped. All data written at the time of deletion is still available in your Azure Synapse Analytics workspace and/or Azure Data Lake.

## Edit the properties of an environment

Azure Synapse Link for Dataverse profiles will fail if the environment name or URL environment properties are changed. You will need to unlink the Azure Synapse Link, optionally deleting the file system, and create a new link.

## Move an environment

If an [environment is migrated from one tenant to another](/power-platform/admin/move-environment-tenant), all Azure Synapse Link profiles are deleted and the data sync is stopped. All data written at the time of deletion is still available in your Azure Synapse Analytics workspace and/or Azure Data Lake. To preserve the configuration of the Azure Synapse Link across environments, use solutions to [export and import the configuration](./azure-synapse-link-solution.md).

## Recover an environment

When [recovering a deleted environment](/power-platform/admin/recover-environment) within the grace period, all Azure Synapse Link for Dataverse will be available and will continue syncing data with no user action as long as the data in your Azure Synapse Analytics workspace and/or Azure Data Lake has not been modified.

## Reset an environment

If an [environment is reset](/power-platform/admin/reset-environment), all Azure Synapse Link for Dataverse profiles will be removed from the environment. All the corresponding data in Azure Synapse Analytics workspace and/or Azure Data Lake will still be available but will not be synced. You may need to clean up the data in the Azure Synapse Analytics workspace and/or Azure Data Lake and you'll need to re-create the Azure Synapse Link for Dataverse.

### See also

[Azure Synapse Link for Dataverse](./export-to-data-lake.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
