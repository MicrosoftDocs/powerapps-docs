---
title: "Retrieve and delete the history of audited data changes (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Programmatically retrieve the audit change history or delete audit records." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 03/26/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
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

# Retrieve and delete the history of audited data changes

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

After auditing is enabled and data changes are made to those tables and columns being audited, you can proceed to obtain the data change history. Optionally, you can delete the audit records after you review the change history. Follow the sample code link at the end of this topic for more information.  
  
## Retrieve the change history

 There are several messages requests that can be used to retrieve the audit change history. These requests are differentiated by the nature of what they retrieve.
Refer to the sample link at the end of this topic for sample code that demonstrates some of these change history message requests.

> [!IMPORTANT]
> Large column values, such as [Email.Description](reference/entities/email.md#BKMK_Description) or [Annotation](reference/entities/annotation.md) are limited (capped) to 5KB or ~5,000 characters in length. A capped column value can be recognized by three dots at the end of the text, for example “lorem ipsum, lorem ip…”.
>
> Going forward, [Audit](reference/entities/audit.md) table records will be stored in Microsoft Dataverse’s log storage. Linking audit records with other table records using FetchXML will no longer be possible.

## Delete the change history for a record

 Use the <xref:Microsoft.Crm.Sdk.Messages.DeleteRecordChangeHistoryRequest> message to delete all the audit change history records for a particular record. This lets you delete the audit change history for a record instead of deleting all the audit records for a date range, which is covered in the next section. To delete the audit change history for a record, you must have a security role with the **prvDeleteRecordChangeHistory** privilege or be a System Administrator.

## Delete the change history for a date range

 You can delete `audit` records for a date range using the <xref:Microsoft.Crm.Sdk.Messages.DeleteAuditDataRequest> request. Audit data records are deleted sequentially from the oldest to the newest. The functionality of this request is slightly different based on the edition of Microsoft SQL Server being used by your Dataverse server. Dataverse uses an enterprise edition of SQL Server.

 If your Dataverse server uses SQL Server standard edition, which does not support the database partitioning feature, the <xref:Microsoft.Crm.Sdk.Messages.DeleteAuditDataRequest> request deletes all audit records created up to the end date specified in the <xref:Microsoft.Crm.Sdk.Messages.DeleteAuditDataRequest.EndDate> property.

 If your Dataverse server uses an Enterprise edition of SQL Server that does support partitioning, the <xref:Microsoft.Crm.Sdk.Messages.DeleteAuditDataRequest> request will delete all audit data in those partitions where the end date is before the date specified in the <xref:Microsoft.Crm.Sdk.Messages.DeleteAuditDataRequest.EndDate> property. Any empty partitions are also deleted. However, neither the current (active) partition nor the `audit` records in that active partition can be deleted by using this request or any other request.

 New partitions are automatically created by the Dataverse platform on a quarterly basis each year. This functionality is non-configurable and cannot be changed. You can obtain the list of partitions using the <xref:Microsoft.Crm.Sdk.Messages.RetrieveAuditPartitionListRequest> request. If the end date of any partition is later than the current date, you cannot delete that partition or any `audit` records in it.  

### See also

 [Data management in Dynamics 365](/dynamics365/customer-engagement/developer/manage-data)<br />
 [Audit table data changes](/dynamics365/customer-engagement/developer/audit-entity-data-changes)<br />
 [Audit user access](audit-user-access.md) <br />
 [Sample: Audit table data changes](org-service/samples/audit-entity-data-changes.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]