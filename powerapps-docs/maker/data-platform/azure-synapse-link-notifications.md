---
title: Receive Azure Synapse Link for Dataverse notifications in Power Apps
description: This article explains how to receive status notifications for Azure Synapse Link for Dataverse.
author: "JasonHQX"
ms.author: jasonhuang
ms.reviewer: matp
ms.service: powerapps
ms.subservice: dataverse-maker
ms.topic: how-to
ms.date: 03/20/2024
ms.custom: template-how-to 
---
# Receive Azure Synapse Link for Dataverse notifications in Power Apps

The state of your Azure Synapse Link for Dataverse is stored in a Microsoft Dataverse table with real-time updates. You can customize a notification using Power Automate flows or Power BI to stay on top of the state of your Azure Synapse Link for Dataverse activity instead of manually checking the Azure Synapse Link for Dataverse profile page in Power Apps (make.powerapps.com).

The Azure Synapse Link for Dataverse profile and its synchronization status are stored in six system-generated read-only tables within Dataverse. These tables are designed to refresh and update in real time, ensuring that the information contained within them remains accurate and up to date at all times.

## How notification works with Azure Synapse Link for Dataverse

To customize a notification, monitor the data changes in a Dataverse table related to the synchronization status of Azure Synapse Link. By tracking these changes, you can export the updated data for visualization using Power BI or set up an automated cloud flow that activates whenever there's a change in the Azure Synapse Link for Dataverse state. This is achieved by reading the row change from any of the Azure Synapse Link state tables.

## Connector to use for a Power Automate flow

We recommend users have the appropriate Power Platform licensing to use Power Automate to customize the trigger function. Use the Dataverse connector, which triggers a flow when a row is added, modified, or deleted in the selected Dataverse table. More information: [Trigger flows when a row is added, modified, or deleted - Power Automate](/power-automate/dataverse/create-update-delete-trigger)

Several options are available for using Power Automate to send notifications. Here are some examples.

|Action  |Connector reference  |
|---------|---------|
|Send a Teams instant message   | [Microsoft Teams](/connectors/teams/#post-message-in-a-chat-or-channel)        |
|Send a text message to mobile device     |  [Azure Communication Services SMS](/connectors/serwersms/#send-sms-message)    |
|Send an email to one or more recipients   |  [Mail](/connectors/sendmail/#send-an-email-notification-(v3)) <br /> [Office 365 Outlook](/connectors/office365/)        |
|Send a notification to Power Apps or Power BI     |  [Power Apps Notification](/connectors/powerappsnotification/) <br />[Power BI](/connectors/powerbi/#add-rows-to-a-dataset)       |

## Dataverse tables and columns used to track state

There are tables that store all Azure Synapse Link profile information. The two main tables listed below provide all sync state information for your Azure Synapse Link profile.

|Table name  |Description  |Table reference  |
|---------|---------|---------|
|Azure Synapse Link external table state      |  This table has data only if you have Delta Lake profile. <br /><br /> This table represents external nonpartitioned tables state in connected Synapse workspace. <br /><br /> One record per synced entity including metadata table like option set.       |  [synapselinkexternaltablestate](/power-apps/developer/data-platform/reference/entities/synapselinkexternaltablestate)       |
|Azure Synapse Link profile table state   |  This table represents the sync state of the Azure Synapse Link entity in Azure Data Lake storage. <br />One record per synced entity excluding metadata table such as option set.       | [synapselinkprofileentitystate](/power-apps/developer/data-platform/reference/entities/synapselinkprofileentitystate)        |

Here are some useful columns for monitoring the health of your Azure Synapse Link in each table:

- `EntityName` and `SynapseWorkspaceName` can be used as the primary identification of the selected table. Synapse workspace name is the same as Azure Synapse Link profile name shown in Power Apps.
- `LastSynchronizedOn` returns the date and time when the latest round of the Delta Lake conversion was successfully completed for each table.
- `RecordCount` returns the total number of records in the Delta Lake profile, minus soft-delete records for each table.
- `TableState` is marked as **created** if the link to the data lake and Delta Lake conversion is active and error-free.

A soft-delete in the Azure Synapse Link external table state table is performed: `LastSyncState` and `TableState` are marked as deleted for removed tables.

Azure Synapse Link profile entity state tables:

- `EntityName` and profile can be used as the primary identification of the selected table. The profile is the same as the Azure Synapse Link profile name shown in Power Apps.
- `InitialSyncProcessCompletedTime` and `InitialSyncState` return the initial sync completion status, which includes both metadata and raw data. The initial sync state marks as **Completed** once the initial sync completes.
- `LakeRecordCount` returns the total records exported to Data Lake in CSV format.
- `LastSyncedDataTime` returns the date and time when the latest round of the data lake file updated or created successfully for each table.
- `SyncState` shows as **InProgress** if the link to data lake is active and error-free.

> [!NOTE]
> `LakeRecordCount` is different from Dataverse record count for the following reasons:
>
> - Sync latency.
> - Append-only mode captures transactions and appends one additional row for each CUD operation.

The remaining four tables provide additional details for Azure Synapse Link setup information:

|Table name  |Description  |Table reference  |
|---------|---------|---------|
|Azure Synapse database  | This table captures linked Azure Data Lake storage and Synapse workspace and setup metadata information (one record per Azure Synapse Link profile).        | [synapsedatabase](/power-apps/developer/data-platform/reference/entities/synapsedatabase)       |
|Azure Synapse Link profile  | This table captures Azure Synapse Link profile information (one record per Azure Synapse Link profile). A soft-delete in this table is performed: `ProfileState` is marked as **deleted** for deleted profile.       | [synapselinkprofile](/power-apps/developer/data-platform/reference/entities/synapselinkprofile)        |
|Azure Synapse Link profile entity |  This table captures entity metadata within the connected Azure Synapse Link profile (one record per synced table).       | [synapselinkprofileentity](/power-apps/developer/data-platform/reference/entities/synapselinkprofileentity)       |
|Azure Synapse Link schedule | This table captures Azure Synapse Link profile information for incremental folder update or delta lake conversion time interval (one record per Azure Synapse Link profile).        | [RecurrenceInterval](/power-apps/developer/data-platform/reference/entities/synapselinkschedule#BKMK_RecurrenceInterval)   |

## See also

[What is Azure Synapse Link for Dataverse?](export-to-data-lake.md)
