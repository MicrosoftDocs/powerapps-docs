---
title: "Auditing overview (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Programmatically use the auditing capability of Microsoft Dataverse to record data changes over time for use in analysis and reporting purposes." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 05/21/2022
ms.reviewer: jdaly
ms.topic: overview
author: Bluebear7 # GitHub ID
ms.subservice: dataverse-developer
ms.author: munzinge # MSFT alias of Microsoft employees only
manager: mayadu # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
 - JimDaly
 - phecke
---

# Auditing overview

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

Dataverse auditing provides capabilities to meet the external and internal auditing, compliance, security, and governance policies that are common to many enterprises. Dataverse auditing logs changes that are made to records and logs user access. Developers can use the tables and APIs that support the auditing feature to create client applications or programmatically interact with auditing data.

> [!IMPORTANT]
> For a complete description of the auditing concepts, capabilities, how it is exposed in apps, and tasks for administrators, see [Administrators Guide: Manage Dataverse auditing](/power-platform/admin/manage-dataverse-auditing).
>
> This content for developers expects that you are already familiar with the documentation for administrators. The Dataverse tables and APIs provide the functionality to support the clients used by administrators and apps.

You can use Dataverse tables and APIs to:

- Retrieve and change organization settings for auditing.
- Detect which tables and columns are enabled for auditing.
- Enable or disable tables and columns for auditing.
- Retrieve a history of audited data changes.
- Delete audit data.

## Organization settings

The [Organization table](../reference/entities/organization.md) contains properties that control how auditing is enabled for an environment.

You can retrieve column values to determine:

- Whether auditing is enabled for the environment.
- The number of days to retain audit log records.
- Whether user access logging is enabled.
- The interval that controls how often user access is logged.

If you have system administrator or system customizer roles, you can update these values to change the auditing behavior.

More information: [Configure organization settings](configure-auditing.md#configure-organization-settings)

## Table and column settings

When auditing is enabled for the organization, those tables which are enabled for auditing will begin writing audit data when data changes.

When auditing is enabled for a table, those columns which are enabled for auditing will be included in the audit data. By default all columns that support auditing are enabled.

You can use Dataverse APIs to query this the table and column definitions to determine which tables and columns are enabled for auditing.

If you have system administrator or system customizer roles, you can update these values to change the auditing behavior.

More information: [Configure tables and columns](configure-auditing.md#configure-tables-and-columns)

## Retrieve audit history

Audit history data is stored in the [Auditing (Audit) table](../reference/entities/audit.md). You should use the following messages to retrieve detailed audit history data:

|Message|Description|
|---------|---------|
|`RetrieveAuditDetails`|Retrieve the full audit details from an audit record.|
|`RetrieveAttributeChangeHistory`|Retrieves the change history for an single column of an audited record.|
|`RetrieveRecordChangeHistory`|Retrieve all audited data changes for a specific record.|

More information: [Retrieve the history of audited data change](retrieve-audit-data.md)

## Delete audit data

You may need to delete audit data because:

- You need to comply with a request from a customer to delete their history.
- You want to use less log capacity space.

> [!NOTE]
> You cannot directly delete records in the [Auditing (Audit) table](../reference/entities/audit.md)

Dataverse provides the following messages to delete audit history data:

|Message|Description|
|---------|---------|
|`DeleteRecordChangeHistory`|Deletes all the audit change history records for a particular record.|
|`BulkDelete`|Asynchronously deletes records identified by a query. This message can be used to delete large numbers of audit records without blocking other activities.|
|`DeleteAuditData`|For customers using customer managed encryption keys or on-premises Dynamics 365, deletes all audit data records up until a specified end date.|

More information: [Delete audit data](delete-audit-data.md)
  
### See also

[Administrators Guide: Manage Dataverse auditing](/power-platform/admin/manage-dataverse-auditing)<br />
[Configure auditing](configure-auditing.md)<br />
[Retrieve the history of audited data changes](retrieve-audit-data.md)<br />
[Delete audit data](delete-audit-data.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]