---
title: "Delete audit data (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Explains how to configure programatically delete audit data." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 06/03/2022
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
|`DeleteRecordChangeHistory`|Deletes all the audit change history records for a particular record.|
|`BulkDelete`|Asynchronously deletes records identified by a query. This message can be used to delete large numbers of audit records without blocking other activities.|
|`DeleteAuditData`|For customers using customer managed encryption keys this message deletes all audit data records up until a specified end date.|

> [!NOTE]
> You cannot directly delete records in the [Auditing (Audit) table](../reference/entities/audit.md)

## Delete the change history for a record

Use the `DeleteRecordChangeHistoryRequest` message to delete all the audit change history records for a particular record. This lets you delete the audit change history for a record instead of deleting all the audit records for a date range. 

To delete the audit change history for a record, you must have the System Administrator security role or a security role with the `prvDeleteRecordChangeHistory` privilege. More information: [Example: Check whether a user has a privilege](../security-access-coding.md#example-check-whether-a-user-has-a-privilege)

### DeleteRecordChangeHistoryRequest Message

Specify the record using the `Target` parameter. The `DeletedEntriesCount` property of the response tells you how many audit records were deleted.

# [Web API](#tab/webapi)

The following example uses the <xref:Microsoft.Dynamics.CRM.RetrieveRecordChangeHistory?text=DeleteRecordChangeHistoryRequest Action> to delete the audited data changes for an account record.

**Request**

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

**Response**

```http
HTTP/1.1 200 OK
OData-Version: 4.0

{
 "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.DeleteRecordChangeHistoryResponse",
 "DeletedEntriesCount": 4
}
```

More information:

 - [Use Web API actions](../webapi/use-web-api-actions.md)
 - <xref:Microsoft.Dynamics.CRM.RetrieveRecordChangeHistory?text=DeleteRecordChangeHistoryRequest Action>
 - <xref:Microsoft.Dynamics.CRM.DeleteRecordChangeHistoryResponse?text=DeleteRecordChangeHistoryResponse ComplexType>


# [SDK for .NET](#tab/sdk)

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

More information:

- <xref:Microsoft.Crm.Sdk.Messages.DeleteRecordChangeHistoryRequest?text=DeleteRecordChangeHistoryRequest Class>
- <xref:Microsoft.Crm.Sdk.Messages.DeleteRecordChangeHistoryResponse?text=DeleteRecordChangeHistoryResponse Class>
- <xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute*?text=IOrganizationService.Execute Method>

---

## Use BulkDelete to delete audit data

You can delete audit records your organization no longer needs to retain to comply with internal and external auditing requirements using the `BulkDelete` message. Deleting audit data using bulk delete will run in the background and allows you to define recurrence patterns, start time, and other parameters that help you to manage your bulk deletion jobs.

### BulkDelete Message

# [Web API](#tab/webapi)

The following example deletes audit records with an action value of 64 (User Access via Web) from the audit log. You can modify your bulk delete job according to your needs.

**Request**

```http
POST [Organization URI]/api/data/v9.1/BulkDelete HTTP/1.1  
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

More information:

- <xref:Microsoft.Dynamics.CRM.BulkDelete?text=BulkDelete Action>
- <xref:Microsoft.Dynamics.CRM.BulkDeleteResponse?text=BulkDeleteResponse ComplexType>
- <xref:Microsoft.Dynamics.CRM.QueryExpression?text=QueryExpression ComplexType>


# [SDK for .NET](#tab/sdk)

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

More information:

- <xref:Microsoft.Crm.Sdk.Messages.BulkDeleteRequest?text=BulkDeleteRequest Class>
- <xref:Microsoft.Crm.Sdk.Messages.BulkDeleteResponse?text=BulkDeleteResponse Class>
- <xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute*?text=IOrganizationService.Execute Method>
- <xref:Microsoft.Xrm.Sdk.IOrganizationService.Retrieve*?text=IOrganizationService.Retrieve Method>

---

## Delete the change history for a date range

If you use customer managed encryption keys you can delete `audit` records for a date range using the `DeleteAuditData` message. Audit data records are deleted sequentially from the oldest to the newest.

> [!NOTE]
> Even if you are using customer managed encryption keys you should consider using Bulk Delete rather than `DeleteAuditData` message. See [Use BulkDelete to delete audit data](#use-bulkdelete-to-delete-audit-data)

The `DeleteAuditData` message will delete all audit data in those partitions where the end date is before the date specified in the `EndDate` property. Any empty partitions are also deleted. However, neither the current (active) partition nor the `audit` records in that active partition can be deleted by using this request or any other request.

New partitions are automatically created by the Dataverse platform on a quarterly basis each year. This functionality is non-configurable and cannot be changed. You can obtain the list of partitions using the `RetrieveAuditPartitionList` message. If the end date of any partition is later than the current date, you cannot delete that partition or any `audit` records in it.

### See also

[Auditing overview](overview.md)<br />
[Configure auditing](configure.md)<br />
[Retrieve the history of audited data changes](retrieve-audit-data.md)


[!INCLUDE [footer-banner](../../../includes/footer-banner.md)]