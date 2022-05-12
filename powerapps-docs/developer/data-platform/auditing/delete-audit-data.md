---
title: "Delete audit data (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Explains how to configure programatically delete audit data." # 115-145 characters including spaces. This abstract displays in the search result.
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

# Delete audit data

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

## Delete the change history for a record

 Use the <xref:Microsoft.Crm.Sdk.Messages.DeleteRecordChangeHistoryRequest> message to delete all the audit change history records for a particular record. This lets you delete the audit change history for a record instead of deleting all the audit records for a date range, which is covered in the next section. To delete the audit change history for a record, you must have a security role with the **prvDeleteRecordChangeHistory** privilege or be a System Administrator.

## Delete the change history for a date range

 You can delete `audit` records for a date range using the <xref:Microsoft.Crm.Sdk.Messages.DeleteAuditDataRequest> request. Audit data records are deleted sequentially from the oldest to the newest. The functionality of this request is slightly different based on the edition of Microsoft SQL Server being used by your Dataverse server. Dataverse uses an enterprise edition of SQL Server.

 If your Dataverse server uses SQL Server standard edition, which does not support the database partitioning feature, the <xref:Microsoft.Crm.Sdk.Messages.DeleteAuditDataRequest> request deletes all audit records created up to the end date specified in the <xref:Microsoft.Crm.Sdk.Messages.DeleteAuditDataRequest.EndDate> property.

 If your Dataverse server uses an Enterprise edition of SQL Server that does support partitioning, the <xref:Microsoft.Crm.Sdk.Messages.DeleteAuditDataRequest> request will delete all audit data in those partitions where the end date is before the date specified in the <xref:Microsoft.Crm.Sdk.Messages.DeleteAuditDataRequest.EndDate> property. Any empty partitions are also deleted. However, neither the current (active) partition nor the `audit` records in that active partition can be deleted by using this request or any other request.

 New partitions are automatically created by the Dataverse platform on a quarterly basis each year. This functionality is non-configurable and cannot be changed. You can obtain the list of partitions using the <xref:Microsoft.Crm.Sdk.Messages.RetrieveAuditPartitionListRequest> request. If the end date of any partition is later than the current date, you cannot delete that partition or any `audit` records in it.

## Delete audit data flexibly using BulkDelete

You can delete audit records your organization no longer needs to retain to comply with internal and external auditing requirements using the [BulkDelete](xref:Microsoft.Dynamics.CRM.BulkDelete) action in the Web API or the [BulkDelete](xref:Microsoft.Crm.Sdk.Messages.BulkDeleteRequest) message in the Organization Service. Deleting audit data using bulk delete will run in the background and allows you to define recurrence patterns, start time, and other parameters that help you to manage your bulk deletion jobs.

### Basic audit bulk delete example

This basic example deletes audit records of type 64 (User Access via Web) from the audit log. You can find the full list of audit actions in the [audit entity reference](../reference/entities/audit.md) and modify your bulk delete job according to your needs.

**Request**

```http
POST [Organization URI]/api/data/v9.1/BulkDelete HTTP/1.1  
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  

{
  "QuerySet":
      [
        {
          "EntityName": "audit",
          "Criteria": {
              "FilterOperator": "And",
              "Conditions": [
                  {
                    "AttributeName": "action",
                    "Operator": "Equal",
                    "Values": [ {"Type": "System.String", "Value": "64"} ]
                  }
              ],
              "Filters": []
          }
        }
      ],
      "JobName": "Bulk Delete of audit records with action = 64",
      "SendEmailNotification": false,
      "ToRecipients": [],
      "CCRecipients": [],
      "RecurrencePattern": "",
      "StartDateTime": "2022-02-02T10:00:00.000Z"
}
```

**Response**

```HTTP
HTTP/1.1 200 OK
Content-Type: application/json; odata.metadata=minimal
OData-Version: 4.0

{
  "@odata.context": "[Organization URI]/api/data/v9.0/$metadata#Microsoft.Dynamics.CRM.BulkDeleteResponse",
  "JobId": "[Job Id]"
}
```

### See also

[Auditing overview](auditing-overview.md)<br />
[Configure auditing](configure-auditing.md)<br />
[Retrieve the history of audited data changes](retrieve-audit-data.md)


[!INCLUDE [footer-banner](../../../includes/footer-banner.md)]