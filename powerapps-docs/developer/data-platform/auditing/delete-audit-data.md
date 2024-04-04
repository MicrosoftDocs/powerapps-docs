---
title: Delete audit data
description: Learn how to programmatically delete audit data stored in Microsoft Dataverse.
ms.date: 06/03/2023
ms.reviewer: jdaly
ms.topic: how-to
ms.author: paulliew
author: paulliew
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
contributors:
 - JimDaly
 - phecke
ms.custom: bap-template
---

# Delete audit data

You may need to delete audit data to comply with a customer's request to delete their history or to free up log capacity space. You can't directly delete records in the [Auditing (Audit) table](../reference/entities/audit.md). Instead, Dataverse provides the following messages to delete audit history data:

|Message|Description|
|---------|---------|
|`DeleteRecordChangeHistory`|Deletes all the audit change history records for a particular record.|
|`BulkDelete`|Asynchronously deletes records identified by a query. Use this message to delete large numbers of audit records without blocking other activities.|
|`DeleteAuditData`|For customers using customer-managed encryption keys, deletes all audit data records up to a specified end date.|

[!INCLUDE [gdpr-dsr-delete-note](~/../shared-content/shared/privacy-includes/gdpr-dsr-delete-note.md)]

## Delete the change history for a record

Use the `DeleteRecordChangeHistoryRequest` message to delete all the audit change history records for a particular record rather than all the audit records for a date range.

To delete the audit change history for a record, [make sure you have](../security-access-coding.md#example-check-whether-a-user-has-a-privilege) the System Administrator security role or a security role with the `prvDeleteRecordChangeHistory` privilege.

### DeleteRecordChangeHistoryRequest message

Use the `Target` parameter to specify the record. The `DeletedEntriesCount` property of the response tells you how many audit records were deleted.

#### [Web API](#tab/webapi)

The following example uses the [DeleteRecordChangeHistory Action](xref:Microsoft.Dynamics.CRM.DeleteRecordChangeHistory) to delete the audited data changes for an account record.

**Request:**

```http
POST [Organization URI]/api/data/v9.2/DeleteRecordChangeHistory HTTP/1.1
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0
If-None-Match: null

{
 "Target": {
  "@odata.type": "Microsoft.Dynamics.CRM.account",
  "accountid": "611e7713-68d7-4622-b552-85060af450bc"
 }
}
```

**Response:**

```http
HTTP/1.1 200 OK
OData-Version: 4.0

{
 "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.DeleteRecordChangeHistoryResponse",
 "DeletedEntriesCount": 4
}
```

Learn more about:

- [Using Web API actions](../webapi/use-web-api-actions.md).
- [DeleteRecordChangeHistory Action](xref:Microsoft.Dynamics.CRM.DeleteRecordChangeHistory)
- [DeleteRecordChangeHistoryResponse ComplexType](xref:Microsoft.Dynamics.CRM.DeleteRecordChangeHistoryResponse)

#### [SDK for .NET](#tab/sdk)

```csharp
/// <summary>
/// Deletes record change history for a specific record and shows
/// how many records were deleted.
/// </summary>
/// <param name="svc">The IOrganizationService instance to use.</param>
/// <param name="target">The specified record.</param>
static void ShowDeleteRecordChangeHistory(
IOrganizationService svc, 
EntityReference target) 
{
    var req = new DeleteRecordChangeHistoryRequest { 
        Target = target
    };

    var resp = (DeleteRecordChangeHistoryResponse)
               svc.Execute(req);

    Console.WriteLine($"Audit records deleted:{resp.DeletedEntriesCount}");
}

```

Learn more about:

- [DeleteRecordChangeHistoryRequest Class](xref:Microsoft.Crm.Sdk.Messages.DeleteRecordChangeHistoryRequest)
- [DeleteRecordChangeHistoryResponse Class](xref:Microsoft.Crm.Sdk.Messages.DeleteRecordChangeHistoryResponse)
- [IOrganizationService.Execute Method](xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute%2A)

---

## Use BulkDelete to delete audit data

Use the `BulkDelete` message to delete audit records your organization no longer needs to retain to comply with internal and external auditing requirements. The bulk delete operation runs in the background and allows you to define recurrence patterns, start time, and other parameters.

### BulkDelete message

The following example deletes audit records with an action value of 64 (User Access via Web).
#### [Web API](#tab/webapi)

**Request:**

```http
POST [Organization URI]/api/data/v9.1/BulkDelete
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  

{
 "QuerySet": [
  {
   "EntityName": "audit",
   "Criteria": {
    "FilterOperator": "And",
    "Conditions": [
     {
      "AttributeName": "action",
      "Operator": "Equal",
      "Values": [
       {
        "Type": "System.String",
        "Value": "64"
       }
      ]
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

**Response:**

```HTTP
HTTP/1.1 200 OK
Content-Type: application/json; odata.metadata=minimal
OData-Version: 4.0

{
 "@odata.context": "[Organization URI]/api/data/v9.0/$metadata#Microsoft.Dynamics.CRM.BulkDeleteResponse",
 "JobId": "[Job Id]"
}
```

Learn more about:

- [BulkDelete Action](xref:Microsoft.Dynamics.CRM.BulkDelete)
- [BulkDeleteResponse ComplexType](xref:Microsoft.Dynamics.CRM.BulkDeleteResponse)
- [QueryExpression ComplexType](xref:Microsoft.Dynamics.CRM.QueryExpression)

#### [SDK for .NET](#tab/sdk)

```csharp
/// <summary>
/// Creates a BulkDelete job to delete audit record history for a 
/// specific action and shows the job created.
/// </summary>
/// <param name="svc">IOrganizationService to use</param>
/// <param name="actionValue">The audit action value</param>
static void BulkDeleteAuditHistoryByAction(IOrganizationService svc, int actionValue)
{
    Guid jobId;

    var querySet = new QueryExpression(entityName: "audit");
    querySet.Criteria.AddCondition(
        attributeName: "action",
        conditionOperator: ConditionOperator.Equal,
        values: actionValue);

    var req = new BulkDeleteRequest
    {
        QuerySet = new QueryExpression[] { querySet },
        JobName = $"Bulk Delete of audit records with action = {actionValue}",
        SendEmailNotification = false,
        ToRecipients = new Guid[] { },
        CCRecipients = new Guid[] { },
        RecurrencePattern = string.Empty,
        StartDateTime = DateTime.UtcNow
    };

    try
    {
        var resp = (BulkDeleteResponse)svc.Execute(req);
        jobId = resp.JobId;

        Entity bulkDeleteJob =
            svc.Retrieve(
                entityName: "asyncoperation",
                id: jobId,
                columnSet: new ColumnSet("name", "statecode", "statuscode"));

        Console.WriteLine($"Job Name: {bulkDeleteJob["name"]}");
        Console.WriteLine($"Job Id: {bulkDeleteJob.Id}");
        Console.WriteLine($"State: {bulkDeleteJob.FormattedValues["statecode"]}");
        Console.WriteLine($"Status: {bulkDeleteJob.FormattedValues["statuscode"]}");

    }
    catch (Exception ex)
    {
        Console.WriteLine(ex.Message);
    }
}
```

Learn more about:

- [BulkDeleteRequest Class](xref:Microsoft.Crm.Sdk.Messages.BulkDeleteRequest)
- [BulkDeleteResponse Class](xref:Microsoft.Crm.Sdk.Messages.BulkDeleteResponse)
- [IOrganizationService.Execute Method](xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute%2A)
- [IOrganizationService.Retrieve Method](xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve%2A)

---

## Delete the change history for a date range

If you use customer-managed encryption keys, you can use the `DeleteAuditData` message to delete audit records for a date range. Audit data records are deleted sequentially from oldest to newest.

> [!NOTE]
> Even if you're using customer-managed encryption keys, you should consider using [Bulk Delete](#use-bulkdelete-to-delete-audit-data) rather than the `DeleteAuditData` message.

The `DeleteAuditData` message deletes all audit data in partitions where the end date is before the date specified in the `EndDate` property. Any empty partitions are also deleted. The current (active) partition and the audit records in it can't be deleted using this request or any other.

Dataverse automatically creates partitions every quarter. You can't change or stop this behavior. You can use the `RetrieveAuditPartitionList` message to obtain the list of partitions. If the end date of any partition is later than the current date, you can't delete that partition or any audit records in it.

### See also

[Auditing overview](overview.md)  
[Configure auditing](configure.md)  
[Retrieve the history of audited data changes](retrieve-audit-data.md)  
[Administrator's Guide: Recover database space by deleting audit logs](/power-platform/admin/recover-database-space-deleting-audit-logs)

[!INCLUDE [footer-banner](../../../includes/footer-banner.md)]
