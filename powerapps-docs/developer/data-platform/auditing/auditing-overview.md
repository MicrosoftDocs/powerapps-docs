---
title: "Auditing overview (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Read how to use the auditing capability of Microsoft Dataverse to record column and table data changes over time for use in analysis and reporting purposes." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 05/10/2022
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

<!-- The purpose of the overview topic is to provide a single page view of capabilites without going into detail -->

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

Dataverse auditing provides capabilities to meet the external and internal auditing, compliance, security, and governance policies that are common to many enterprises. Dataverse auditing logs changes that are made to records and logs user access.

> [!IMPORTANT]
> For a complete description of the auditing capabilites, how it is exposed in apps, and tasks for administrators, see [Administrators Guide: Manage Dataverse auditing](/power-platform/admin/manage-dataverse-auditing). 
>
> This content for developers expects that you are already familar with the capabilities described there. The Dataverse tables and APIs provide the functionality to support the clients used by administrators and apps.

You can use Dataverse tables and APIs to:

- Retrieve and change organization settings for auditing.
- Detect which tables and columns are enabled for auditing.
- Enable or disable tables and columns for auditing.
- Retrieve a history of audited data changes.
- Delete audit data.

## Organization settings

The Organization table contains properties that control how auditing is enabled for an environment. The organization table has a single row. 

You can retrieve column values in this row to determine:

- Whether auditing is enabled for the environment.
- The number of days to retrain audit log records.
- Whether user access logging is enabled.
- The interval that controls how often user access is logged.

If you have system administrator or system customizer roles, You can update these values to change the auditing behavior.

More information: [Configure organization settings](configure-auditing.md#configure-organization-settings)


## Table and column settings

When auditing is enabled for the organization, those tables which are enabled for auditing will begin writing audit data when data changes.

When auditing is enabled for a table, those columns which are enabled for auditing will be included in the audit data. By default all columns that support auditing are enabled but auditing is disabled at the table and organization level.

You can use Dataverse APIs to query this data to determine which tables and columns are enabled for auditing.

If you have system administrator or system customizer roles, you can update these values to change the auditing behavior.

More information: [Configure tables and columns](configure-auditing.md#configure-tables-and-columns)

## Retrieve audit history

Audit history data is stored in the [Auditing (Audit) table](reference/entities/audit.md). This table doesn't include detail about individual column changes. You must use the following messages to retrieve detailed audit history data:

|Message|Description|
|---------|---------|
|`RetrieveAttributeChangeHistory`|Retrieves the change history for an single column of an audited record.|
|`RetrieveAuditDetails`|Retrieves the change history for all columns changed for a specific audit record.|
|`RetrieveRecordChangeHistory`|Retrieves all attribute changes for an audited record.|

More information: [Retrieve the history of audited data change](retrieve-audit-data.md)

## Delete audit data

You may need to delete audit data because:
- You need to comply with a request from a customer to delete their history.
- You want to use less log capacity space.

Dataverse provides the following messages to delete audit history data:

|Message|Description|
|---------|---------|
|`DeleteRecordChangeHistory`|Deletes all the audit change history records for a particular record|
|`DeleteAuditData `|Deletes all audit data records up until a specified end date.|
|`BulkDelete`|Asynchronously deletes records identified by a query. This message can be used to delete large numbers of audit records without blocking other activities|

> [!NOTE]
> You cannot directly delete records in the [Auditing (Audit) table](reference/entities/audit.md)

More information: [Delete audit data](delete-audit-data.md)

<!-- The below needs to be moved to retrieve audit data -->

## Audit table

Data for auditing events is in the [Auditing (Audit) table](reference/entities/audit.md). In the Web API the <xref:Microsoft.Dynamics.CRM.audit?text=audit EntityType> provides this data.

The following table summarizes important columns in the audit table.

|SchemaName<br />LogicalName<br />DisplayName  |Type  |Description  |
|---------|---------|---------|
|`Action`<br />`action`<br />Event|Choice|More than 70 options that represent the name of the message that caused the change. Each option has an integer and a localizable label value. For example:<br />0 = Unknown<br />1 = Create<br /> 2 = Update<br />3 = Delete<br />4 = Activate<br />5 = Deactivate<br />And so on... See [Action Choices/Options](/power-apps/developer/data-platform/reference/entities/audit#action-choicesoptions) for the complete list. |
|`AttributeMask`<br />`attributemask`<br />Changed Field|Memo|May contain a comma separated list of numbers that correspond to the <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata>.<xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.ColumnNumber> for the columns changed in the transaction for the action. |
|`AuditId`<br />`auditid`<br /> Record Id|Unique Identifier|The primary key for the audit table.|
|`CallingUserId`<br />`callinguserid`<br />Calling User|Lookup|The calling user when impersonation is used for the operation. Otherwise null. |
|`CreatedOn`<br />`createdon`<br />Changed Date|DateTime|When the audit record was created.|
|`ObjectId`<br />`objectid`<br />Record|Lookup|The unique identifier for the record that was audited.|
|`ObjectTypeCode`<br />`objecttypecode`<br />Entity|EntityName|The logical name of the entity referred to by the `objectid` column.|
|`Operation`<br />`operation`<br />Operation|Choice|The operation that cased the audit. One of 4 values:<br />1 = Create<br />2 = Update<br />3 = Delete<br />4 = Access<br />|
|`UserId`<br />`userid`<br />Changed By|Lookup|The user who caused the change|

<!-- |`RegardingObjectId`<br />`regardingobjectid`<br />Regarding |Lookup|         |
|`TransactionId`<br />`transactionid`<br />Transaction Id|         |         |
|`UserAdditionalInfo`<br />`useradditionalinfo`<br />User Info|         |         | -->

### audit table relationships

The audit table has only two Many-to-one relationships with the `systemuser` table:

|Relationship|Table|Description  |
|---------|---------|---------|
|`lk_audit_userid`|systemuser|Relates the user to all the audit records created because of changes they made.|
|`lk_audit_callinguserid`|systemuser|Relates the user to any of the audit records they created while impersonating another user.|

> [!NOTE]
> The audit entity supports only one link entity in a query. Since only two relationships exist with the `systemuser` table, this means you can include data from either the `callinguserid` or `userid` columns, but not both at the same time.
> You cannot build queries using QueryExpression or FetchXml that join audit data with other tables other than the two formal relationships that exist with the `systemuser` table.

<!-- Questions: 
Why is the Audit TransactionId frequently an empty GUID (but not always)? Does it matter?
Is UserAdditionalInfo ever not null?
Is RegardingObjectId ever not null? -->





## Audit messages



<!-- Organizations often need to be in compliance with various regulations to ensure availability of customer interaction history, audit logs, access reports, and security incident tracking reports. Organizations may want to track changes in Microsoft Dataverse data for security and analytical purpose.  
  
 Dataverse supports an auditing capability where table and column data changes within an organization can be recorded over time for use in analysis and reporting purposes. Auditing is supported on all custom and most customizable tables and columns. Auditing is not supported on table or column definition changes, retrieve operations, export operations, or during authentication. For information on how to configure auditing, see [Configure tables and columns for auditing](configure-entities-attributes-auditing.md).  
  
## Supported for auditing

 The following lists auditing capabilities for Dataverse:  
  
* Audit of customizable tables
* Audit of custom tables
* Configure tables for audit
* Configure columns for audit
* Privilege-based audit trail viewing
* Privilege-based audit summary viewing
* Audit log deletion for a partitioned SQL database  
* Audit log deletion for a non-partitioned SQL database 
* Audit of record create, update, and delete operations
* Audit of relationships (1:N, N:N) 
* Audit of audit events
* Audit of user access
* Adherence to regulatory standards
* Auditing APIs for developers
  
## Not supported for auditing  
 The following lists what cannot be audited for Dataverse:  
  
* Audit of read operations
* Audit of table and column definition changes

However, you can enable audit of read operations from the Power Platform admin center (PPAC). More information: [Enable auditing](/power-platform/admin/enable-use-comprehensive-auditing#enable-auditing)
  
## Key concepts  
 The following bullets identify some key auditing concepts:  
  
-   You can enable or disable auditing at the organization, table, and column levels. If auditing is not enabled at the organization level, auditing of tables and columns, even if it is enabled, does not occur. By default, auditing is enabled on all auditable table columns, but is disabled at the table and organization level.  
  
-   The ability to retrieve and display the audit history is restricted to users who have certain security privileges: View Audit History, and View Audit Summary. There are also privileges specific to partitions: View Audit Partitions, and Delete Audit Partitions. See the specific message request documentation for information about the required privileges for each message.  
  
-   Audited data changes are stored in records of the **audit** table.  
  
## Data that can be audited  
 The following list identifies the data and operations that can be audited:  
  
-   Create, update, and delete operations on records.  
  
-   Changes to the shared privileges of a record.  
  
-   N:N association or disassociation of records.  
  
-   Changes to security roles.  
  
-   Audit changes at the table, column, and organization level. For example, enabling audit on a table.  
  
-   Deletion of audit logs.  
  
-   When (date/time) a user accesses Dataverse data, for how long, and from what client.  
  
 Enabling or disabling of field level security by setting the <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.IsSecured> column cannot be audited.   -->
  
### See also

[Administrators Guide: Manage Dataverse auditing](/power-platform/admin/manage-dataverse-auditing)<br />
[Configure tables and columns for auditing](configure-entities-attributes-auditing.md) 

[!INCLUDE[footer-include](../../includes/footer-banner.md)]