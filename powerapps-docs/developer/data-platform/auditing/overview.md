---
title: Auditing overview
description: Learn how to programmatically use the auditing capability of Microsoft Dataverse to record data changes over time for use in analysis and reporting.
ms.date: 06/02/2022
ms.topic: overview
ms.subservice: dataverse-developer
author: paulliew
ms.author: paulliew
ms.reviewer: jdaly
search.audienceType: 
  - developer
contributors:
 - JimDaly
 - phecke
ms.custom: bap-template
---

# Auditing overview

Microsoft Dataverse provides capabilities to meet the external and internal auditing, compliance, security, and governance policies that are common to many enterprises. Dataverse logs both user access and changes that are made to records. You can use the auditing tables and APIs to create client applications or programmatically interact with auditing data.

> [!NOTE]
> Refer to [Administrator's Guide: Manage Dataverse auditing](/power-platform/admin/manage-dataverse-auditing) for a complete description of auditing concepts and capabilities, how it's exposed in apps, and tasks for administrators. The tables and APIs described here support client applications used by administrators and can be used by developers for integration projects. This content doesn't describe all auditing concepts and capabilities.

You can use Dataverse tables and APIs to:

- Retrieve and change organization settings for auditing.
- Detect which tables and columns are enabled for auditing.
- Enable or disable tables and columns for auditing.
- Retrieve a history of audited data changes.
- Delete audit data.

## Organization settings

Properties of the [Organization table](../reference/entities/organization.md) control how auditing is enabled for an environment. Retrieve column values to determine:

- Whether auditing is enabled for the environment
- The number of days to retain audit log records
- Whether user access logging is enabled
- How often user access is logged

If you have the System Administrator or System Customizer role, you can configure organization settings to change the auditing behavior.

**More information:** [Configure organization settings](configure.md#configure-organization-settings)

## Table and column settings

When auditing is enabled for the organization, audit data is recorded in the tables that are enabled for auditing whenever data changes.

When auditing is enabled for a table, the columns that are enabled for auditing are included in the audit data.

Use Dataverse APIs to query table and column definitions to determine which tables and columns are enabled for auditing.

If you have the System Administrator or System Customizer role, you can configure tables and columns to change the auditing behavior.

**More information**: [Configure tables and columns](configure.md#configure-tables-and-columns)

## Retrieve audit history

Audit history data is stored in the [Auditing (Audit) table](../reference/entities/audit.md). Use the following messages to retrieve audit history data:

|Message|Description|
|---------|---------|
|`RetrieveAuditDetails`|Retrieve the full details of an audit record.|
|`RetrieveAttributeChangeHistory`|Retrieve the change history for a single column of an audited record.|
|`RetrieveRecordChangeHistory`|Retrieve the change history for all columns of an audited record.|

**More information**: [Retrieve the history of audited data changes](retrieve-audit-data.md):

## Delete audit data

You may need to delete audit data to comply with a customer's request to delete their history or to free up log capacity space. You can't directly delete records in the [Auditing (Audit) table](../reference/entities/audit.md). Instead, Dataverse provides the following messages to delete audit history data:

|Message|Description|
|---------|---------|
|`DeleteRecordChangeHistory`|Deletes all the change history for a particular record.|
|`BulkDelete`|Asynchronously deletes records identified by a query. This message can be used to delete large numbers of audit records without blocking other activities.|
|`DeleteAuditData`|For customers using customer-managed encryption keys, this message deletes all audit data records up to a specified end date.|

**More information**: [Delete audit data](delete-audit-data.md)
  
### See also

[Manage Dataverse auditing](/power-platform/admin/manage-dataverse-auditing)  
[Configure auditing](configure.md)  
[Retrieve the history of audited data changes](retrieve-audit-data.md)  
[Delete audit data](delete-audit-data.md)

[!INCLUDE [footer-include](../../../includes/footer-banner.md)]
