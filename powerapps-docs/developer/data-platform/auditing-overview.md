---
title: "Auditing overview (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Read how to use the auditing capability of Microsoft Dataverse to record column and table data changes over time for use in analysis and reporting purposes." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 05/10/2022
ms.reviewer: "pehecke"
ms.topic: overview
author: "Bluebear73" # GitHub ID
ms.subservice: dataverse-developer
ms.author: "munzinge" # MSFT alias of Microsoft employees only
manager: "mayadu" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Auditing overview

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

The Dataverse auditing provides capabilities to meet the external and internal auditing, compliance, security, and governance policies that are common to many enterprises. Dataverse auditing logs changes that are made to records and logs user access.

> [!IMPORTANT]
> For a complete description of the auditing capabilites, how it is exposed in apps, and tasks for administrators, see [Administrators Guide: Manage Dataverse auditing](/power-platform/admin/manage-dataverse-auditing). This content for developers expects that you are already familar with the capabilities described there.

You can use Dataverse tables and APIs to:

- Retrieve and change organization settings for auditing.
- Detect which tables and columns are enabled for auditing.
- Enable or disable tables and columns for auditing.
- Retrieve a history of audited data changes.
- Delete audit data.

## Audit table

Data for auditing events is in the [Auditing (Audit) table](reference/entities/audit.md). In the Web API exposes this using the <xref:Microsoft.Dynamics.CRM.audit?text=audit EntityType>.

The following table summarizes important columns in the audit table.

|SchemaName<br />LogicalName<br />DisplayName  |Type  |Description  |
|---------|---------|---------|
|`Action`<br />`action`<br />Event|Choice|More than 70 options that represent the name of the message that caused the change. Each option has an integer and a localizable label value. For example:<br />0 = Unknown<br />1 = Create<br /> 2 = Update<br />3 = Delete<br />4 = Activate<br />5 = Deactivate<br />And so on... |
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

> [!NOTE]
> The audit entity supports only one link entity in a query. Since only two relationships exist with the `systemuser` table, this means you can include data from either the `callinguserid` or `userid` columns, but not both at the same time.
> You cannot build queries using QueryExpression or FetchXml that join audit data with other tables other than the two formal relationships that exist with the `systemuser` table.

Questions: 
Why is the Audit TransactionId frequently an empty GUID (but not always)? Does it matter?
Is UserAdditionalInfo ever not null?
Is RegardingObjectId ever not null?





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

[Configure tables and columns for auditing](configure-entities-attributes-auditing.md) 

[!INCLUDE[footer-include](../../includes/footer-banner.md)]