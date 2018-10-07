---
title: "Delete data in bulk (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Deleting data in bulk helps maintain data quality and manage the consumption of system storage by deleting data that is no longer needed." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "mayadumesh" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Delete data in bulk

The *bulk deletion* feature helps you to maintain data quality and manage the consumption of system storage in Common Data Service (CDS) for Apps by deleting data that you no longer need. For example, you can delete the following data in bulk:  
  
- Stale data.  
  
- Data that is irrelevant to the business.  
  
- Unneeded test or sample data.  
  
- Data that is incorrectly imported from other systems.  
  
With bulk deletion, you can perform the following operations:  
  
- Delete data across multiple entities.  
  
- Delete records for a specified entity.  
  
- Receive email notifications when a bulk deletion finishes.  
  
- Delete data periodically.  
  
- Schedule the start time of a recurring bulk delete.  
  
- Retrieve the information about the failures that occurred during a bulk deletion.  
  
## Run bulk delete

To delete data in bulk, you have to submit a bulk delete job by using the <xref:Microsoft.Crm.Sdk.Messages.BulkDeleteRequest> message. The bulk delete job runs asynchronously in the background without blocking other activities. The query expressions that describe the records on which to run the bulk delete job are specified in the <xref:Microsoft.Crm.Sdk.Messages.BulkDeleteRequest.QuerySet> property of this request.  
  
 A bulk delete job is represented by the bulk delete operation entity. The schema name for this entity is `BulkDeleteOperation`. A bulk delete operation record includes the following information:  
  
- Number of records that the bulk delete job deleted.  
  
- Number of records that the bulk delete job failed to delete.  
  
- Whether the bulk delete job is a recurring job or not.  
  
- Start time of the bulk delete job.  
  
  A bulk delete job only deletes records that are created before the job starts to run.  
  
> [!NOTE]
>  If a bulk delete job fails or ends prematurely, any records that were deleted before the failure or ending of the job are not rolled back and remain deleted. The failures of the `BulkDeleteOperation` are stored in the `BulkDeleteFailure` records and can be retrieved by using the <xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> message or the  <xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> message.  
  
 A bulk delete job deletes the specified records according to the cascading rules. These rules are based on the relationship type between the entities. For more information, see [Entity Relationship Behavior](/dynamics365/customer-engagement/developer/entity-relationship-behavior).  
  
 To run a bulk delete job, a user must have the `BulkDelete` and `Delete` privileges for the entity types being deleted. The user must also have read permissions to the entity records that are specified in the <xref:Microsoft.Crm.Sdk.Messages.BulkDeleteRequest> message. By default, a system administrator has the necessary permissions; however, other users must be granted these permissions.  
  
 You can perform a bulk deletion on all entities that are supported by the delete action. For information about possible actions on entity records, see [Actions on Entity Records](/dynamics365/customer-engagement/developer/introduction-entities#ActionsOnEntityRecords).  
  
 If a plug-in or a workflow (process) is triggered by the delete action on a specific entity type, it is triggered every time that an entity record of this type is deleted by the bulk delete job.  
  
## Samples

Look at the following Organization service samples for the bulk delete feature:

- [Sample: Bulk Delete Exported Records](org-service/samples/bulk-delete-exported-records.md)   
- [Sample: Bulk Delete Records That Match Common Criteria](org-service/samples/bulk-delete-records-match-common-criteria.md)

### See also

[BulkDeleteOperation Entity](reference/entities/bulkdeleteoperation.md)