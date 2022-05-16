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
|`DeleteAuditData`|Deletes all audit data records up until a specified end date.|
|`BulkDelete`|Asynchronously deletes records identified by a query. This message can be used to delete large numbers of audit records without blocking other activities.|

> [!NOTE]
> You cannot directly delete records in the [Auditing (Audit) table](reference/entities/audit.md)

## Delete the change history for a record

Use the `DeleteRecordChangeHistoryRequest` message to delete all the audit change history records for a particular record. This lets you delete the audit change history for a record instead of deleting all the audit records for a date range. To delete the audit change history for a record, you must have the System Administrator security role or a security role with the `prvDeleteRecordChangeHistory` privilege.

### DeleteRecordChangeHistoryRequest Message

Specify the record using the `Target` parameter. The `DeletedEntriesCount` property of the response tells you how many audit records were deleted.

# [Web API](#tab/webapi)

The following example uses the <xref:Microsoft.Dynamics.CRM.RetrieveRecordChangeHistory?text=DeleteRecordChangeHistoryRequest Action> to delete the audited data changes for an account record.

**Request**

```http
POST https://crmue.api.crm.dynamics.com/api/data/v9.2/DeleteRecordChangeHistory HTTP/1.1
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
    "@odata.context": "https://crmue.api.crm.dynamics.com/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.DeleteRecordChangeHistoryResponse",
    "DeletedEntriesCount": 4
}
```

More information:

 - [Use Web API actions](../webapi/use-web-api-actions.md)
 - <xref:Microsoft.Dynamics.CRM.RetrieveRecordChangeHistory?text=DeleteRecordChangeHistoryRequest Action>
 - <xref:Microsoft.Dynamics.CRM.DeleteRecordChangeHistoryResponse?text=DeleteRecordChangeHistoryResponse ComplexType>


# [.NET SDK](#tab/sdk)

This `ShowDeleteRecordChangeHistory` static method deletes the audited data changes the record specified by the `target` parameter and shows the number of records that are deleted.

```csharp
/// <summary>
/// Deletes record change history for a specific record
/// </summary>
/// <param name="svc">The IOrganizationService instance to use.</param>
/// <param name="target">The specified record.</param>
static void ShowDeleteRecordChangeHistory(IOrganizationService svc, EntityReference target) {

    DeleteRecordChangeHistoryRequest req = new DeleteRecordChangeHistoryRequest { 
        Target = target
    };

    DeleteRecordChangeHistoryResponse resp = (DeleteRecordChangeHistoryResponse)svc.Execute(req);

    Console.WriteLine($"Audit records deleted:{resp.DeletedEntriesCount}");
}

```

More information:

- <xref:Microsoft.Crm.Sdk.Messages.DeleteRecordChangeHistoryRequest?text=DeleteRecordChangeHistoryRequest Class>
- <xref:Microsoft.Crm.Sdk.Messages.DeleteRecordChangeHistoryResponse?text=DeleteRecordChangeHistoryResponse Class>
- <xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute*?text=IOrganizationService.Execute Method>

---

## Delete the change history for a date range

You can delete `audit` records for a date range using the `DeleteAuditData` message. Audit data records are deleted sequentially from the oldest to the newest.

The `DeleteAuditData` message will delete all audit data in those partitions where the end date is before the date specified in the `EndDate` property. Any empty partitions are also deleted. However, neither the current (active) partition nor the `audit` records in that active partition can be deleted by using this request or any other request.

> [!NOTE]
> Behavior for Dynamics 365 on-premises may be different depending on which version of SQL Server is used. The Dataverse behavior is based on the Enterprise edition of SQL server. The on-premises behavior is different when SQL Server standard edition is used because that version doesn't support the database partitioning feature. In that case the `DeleteAuditData` message deletes all audit records created up to the end date specified in the `EndDate` property.

New partitions are automatically created by the Dataverse platform on a quarterly basis each year. This functionality is non-configurable and cannot be changed. You can obtain the list of partitions using the `RetrieveAuditPartitionList` message. If the end date of any partition is later than the current date, you cannot delete that partition or any `audit` records in it.

### DeleteAuditData Message

# [Web API](#tab/webapi)

<!-- The following example doesn't work in my environment.

According to {{webapiurl}}RetrieveAuditPartitionList
I don't have any partitions. -->

**Request**

```http
POST https://crmue.api.crm.dynamics.com/api/data/v9.2/DeleteAuditData HTTP/1.1

Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0
If-None-Match: null

{
    "EndDate": "2021-04-09T00:00:00Z"
}

```

**Response**

```http
HTTP/1.1 400 Bad Request

OData-Version: 4.0

{"error":{"code":"0x80040203","message":"There are no partitions ending before the given date"}}
```

More information:

# [.NET SDK](#tab/sdk)

This `MethodName` static method

```csharp
/// <summary>
/// Shows the results of the DeleteAuditData messages
/// </summary>
/// <param name="svc">The IOrganizationService instance to use.</param>
/// <param name="endDate">The date to delete audit records before.</param>
static void ShowDeleteAuditData(IOrganizationService svc, DateTime endDate) {

    DeleteAuditDataRequest req = new DeleteAuditDataRequest { 
        EndDate = endDate
    };

    try
    {
        DeleteAuditDataResponse resp = (DeleteAuditDataResponse)svc.Execute(req);
        Console.WriteLine($"Partitions Deleted: {resp.PartitionsDeleted}");
    }
    catch (Exception ex)
    {
        Console.WriteLine($"Error: {ex.Message}");
        throw ex;
    }
}
```

More information:

---

## Delete audit data flexibly using BulkDelete

You can delete audit records your organization no longer needs to retain to comply with internal and external auditing requirements using the `BulkDelete` message. Deleting audit data using bulk delete will run in the background and allows you to define recurrence patterns, start time, and other parameters that help you to manage your bulk deletion jobs.

### BulkDelete Message

# [Web API](#tab/webapi)

The following example deletes audit records of type 64 (User Access via Web) from the audit log. You can find the full list of audit actions in [Audit Actions](retrieve-audit-data.md#audit-actions) and modify your bulk delete job according to your needs.

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

More information:

# [.NET SDK](#tab/sdk)

This `MethodName` static method

```csharp
```

More information:

---

### See also

[Auditing overview](auditing-overview.md)<br />
[Configure auditing](configure-auditing.md)<br />
[Retrieve the history of audited data changes](retrieve-audit-data.md)


[!INCLUDE [footer-banner](../../../includes/footer-banner.md)]