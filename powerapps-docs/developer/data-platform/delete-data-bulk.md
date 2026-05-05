---
title: Delete Data in Bulk to Reduce Storage Use
description: Learn how to delete data in bulk to remove stale records, improve data quality, and manage storage consumption. Use bulk delete jobs to get started.
ms.date: 04/28/2026
ms.topic: how-to
author: MsSQLGirl
ms.subservice: dataverse-developer
ms.author: jukoesma
ms.reviewer: pehecke
search.audienceType: 
  - developer
ms.custom: bap-template
---

# Delete data in bulk

[!INCLUDE [cc-terminology](includes/cc-terminology.md)]

The bulk deletion feature in Microsoft Dataverse helps you maintain data quality and manage the consumption of system storage by deleting data you no longer need. For example, you can delete the following data in bulk:  
  
- Stale data
- Data that's no longer relevant to the business
- Unneeded test or sample data
- Data that were incorrectly imported from other systems
  
You can perform the following operations:  
  
- Delete data across multiple tables.
- Delete records in a specific table.
- Receive email notifications when a bulk deletion finishes.
- Delete data periodically.
- Schedule the start time of a recurring bulk delete.
- Retrieve information about failures that occurred during a bulk deletion.

To delete multiple rows in elastic tables, you can also use the [`DeleteMultiple` message](use-elastic-tables.md#use-deletemultiple-with-elastic-tables). `DeleteMultiple` deletes records in a single elastic immediately, rather than using a bulk delete job.
  
## Run bulk delete

To delete data in bulk, use the `BulkDelete` message to submit a bulk delete job. By using the SDK, use the [BulkDeleteRequest class](xref:Microsoft.Crm.Sdk.Messages.BulkDeleteRequest). By using the Web API, use the [BulkDelete action](xref:Microsoft.Dynamics.CRM.BulkDelete). Specify the query expressions that describe the records to delete in the `QuerySet` property of your request.
  
A bulk delete job is represented by a record in the [`Bulk Delete Operation` (`BulkDeleteOperation`) table](reference/entities/bulkdeleteoperation.md). A bulk delete operation record includes the following information:  
  
- The number of records the job deleted
- The number of records the job failed to delete
- Whether the job is set to recur
- The start time of the job
  
The bulk delete job runs asynchronously without blocking other activities. It only deletes records that were created before the job starts to run. The job deletes the specified records according to cascading rules based on [table relationship cascading behavior](configure-entity-relationship-cascading-behavior.md).

If a bulk delete job fails or ends prematurely, the operation doesn't roll back any deleted records. The record data remains deleted. A record of failures is stored in the [`Bulk Delete Failure` (`BulkDeleteFailure`) table](reference/entities/bulkdeletefailure.md). You can retrieve information from the table about the error that caused the failure.
  
To run a bulk delete job, you must have `BulkDelete` and `Delete` privileges on the table types you're deleting. You must also have read permissions on the table records that you specify in the `QuerySet` property. A system administrator has the necessary permissions by default. Grant them to other users.
  
You can perform a bulk deletion on all tables that support the `Delete` message.
  
If the delete action on a specific table type triggers a plug-in or a workflow (process), the bulk delete job triggers the plug-in or workflow every time it deletes a table record of that type.

## Control bulk delete processing

The `Options` parameter on the `BulkDelete` action or message request allows you to control how the bulk delete job processes table rows (records). You can use the parameter to:

- Disable the recycle bin for bulk-deleted records. Disabling the recycle bin improves performance by skipping the overhead of storing deleted records for recovery.
- Enable sandbox fast delete mode to bypass the standard SDK pipeline (plug-ins, workflows, recycle bin). Fast delete achieves higher deletion throughput.

### Use the Options parameter

The `Options` parameter accepts a `BulkDeleteOptions` object with the following properties.

| Property | Type | Default | Description |
|---|---|---|---|
| `CanRecoverDeletedRecords` | Boolean | null (recycle bin enabled) | When set to false, records deleted by the bulk delete job are permanently removed and can't be recovered from the recycle bin. |
| `RunJobForSandbox` | Boolean | null (standard pipeline) | When set to true, the bulk delete job uses the high-performance sandbox delete mode, bypassing plug-ins, workflows, and the recycle bin. |

#### Example: Options parameter

The following examples demonstrate how to use the `Options` parameter with the `BulkDelete` action or message request.

##### [Web API](#tab/webapi)

Use the `Options` property in the request body of the [BulkDelete action](xref:Microsoft.Dynamics.CRM.BulkDelete). The `Options` parameter is a [BulkDeleteOptions complex type](xref:Microsoft.Dynamics.CRM.BulkDeleteOptions).

**Request:**

```http
POST [Organization Uri]/api/data/v9.2/BulkDelete HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
Accept: application/json
Content-Type: application/json

{
    "QuerySet": [
        {
            "@odata.type": "Microsoft.Dynamics.CRM.QueryExpression",
            "EntityName": "account",
            "ColumnSet": {
                "AllColumns": true
            },
            "Distinct": false
        }
    ],
    "JobName": "Delete all accounts",
    "SendEmailNotification": false,
    "ToRecipients": [],
    "CCRecipients": [],
    "RecurrencePattern": "",
    "StartDateTime": "2026-03-13T06:30:00Z",
    "Options": {
        "CanRecoverDeletedRecords": true,
        "RunJobForSandbox": false
    }
}
```

**Response:**

```http
HTTP/1.1 200 OK
OData-Version: 4.0

{
    "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.BulkDeleteResponse",
    "JobId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
}
```

###### Options parameter values

| Scenario | CanRecoverDeletedRecords | RunJobForSandbox | Effect |
| -- | -- | -- | -- |
| Default (standard delete) | true or omitted | false or omitted | Records go through standard pipeline. Deleted records stored in recycle bin if enabled.|
| Skip recycle bin|  false | false or omitted | Records go through standard pipeline. Recycle bin is bypassed for this job.|
| Sandbox fast delete | false | true | Bypasses SDK pipeline and recycle bin. Maximum throughput.|

##### [SDK for .NET](#tab/sdk)

Use the [BulkDeleteRequest class](xref:Microsoft.Crm.Sdk.Messages.BulkDeleteRequest) and set the `Options` parameter in the request's `Parameters` collection. The value is a `BulkDeleteOptions` object from the Microsoft.Xrm.Sdk namespace.

```csharp
using Microsoft.Crm.Sdk.Messages;
using Microsoft.Xrm.Sdk;
using Microsoft.Xrm.Sdk.Query;

static Guid BulkDeleteWithOptions(IOrganizationService service)
{
    var request = new BulkDeleteRequest
    {
        JobName = "Delete all accounts",
        QuerySet = new QueryExpression[]
        {
            new QueryExpression
            {
                EntityName = "account",
                ColumnSet = new ColumnSet(true)
            }
        },
        StartDateTime = DateTime.UtcNow,
        RecurrencePattern = string.Empty,
        SendEmailNotification = false,
        ToRecipients = Array.Empty<Guid>(),
        CCRecipients = Array.Empty<Guid>()
    };

    // Set bulk delete options
    request["Options"] = new BulkDeleteOptions
    {
        CanRecoverDeletedRecords = true,
        RunJobForSandbox = false
    };

    BulkDeleteResponse response =
        (BulkDeleteResponse)service.Execute(request);
    return response.JobId;
}
```

The `BulkDeleteOptions` class is available in the Microsoft.Xrm.Sdk namespace. Ensure you're using the recent version of the SDK assemblies.

---

### Control recycle bin behavior

By default, when the recycle bin is enabled for your environment, all records deleted by a bulk delete job are stored in the recycle bin before deletion. The recycle bin allows administrators to recover accidentally deleted records, but adds significant I/O overhead for each deleted record.
To disable the recycle bin for a bulk delete job, set `CanRecoverDeletedRecords` to `false` in the `Options` parameter. This setting can approximately double the deletion throughput by eliminating the overhead of:

- Creating DeletedItemReference records
- Copying record data to recycle bin storage tables
- Updating restore data blobs for each deleted record

> [!WARNING]
> When `CanRecoverDeletedRecords` is set to false, deleted records are permanently removed and can't be recovered from the recycle bin. This action is irreversible. Ensure that you verified the query criteria and have appropriate backups before running a bulk delete job with this option. This setting only affects the current bulk delete job; it doesn't change the environment-level recycle bin configuration.

#### Example: Disable the recycle bin for faster deletion

Permanently delete records without storing them in the recycle bin.

##### [Web API](#tab/webapi)

```http
POST [Organization Uri]/api/data/v9.2/BulkDelete HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
Accept: application/json
Content-Type: application/json

{
    "QuerySet": [
        {
            "@odata.type": "Microsoft.Dynamics.CRM.QueryExpression",
            "EntityName": "account",
            "ColumnSet": {
                "AllColumns": true
            },
            "Distinct": false
        }
    ],
    "JobName": "Delete accounts - skip recycle bin",
    "SendEmailNotification": false,
    "ToRecipients": [],
    "CCRecipients": [],
    "RecurrencePattern": "",
    "StartDateTime": "2026-03-13T06:30:00Z",
    "Options": {
        "CanRecoverDeletedRecords": false
    }
}
```

##### [SDK for .NET](#tab/sdk)

```csharp
static Guid BulkDeleteSkipRecycleBin(IOrganizationService service)
{
    var request = new BulkDeleteRequest
    {
        JobName = "Delete accounts - skip recycle bin",
        QuerySet = new QueryExpression[]
        {
            new QueryExpression
            {
                EntityName = "account",
                ColumnSet = new ColumnSet(true)
            }
        },
        StartDateTime = DateTime.UtcNow,
        RecurrencePattern = string.Empty,
        SendEmailNotification = false,
        ToRecipients = Array.Empty<Guid>(),
        CCRecipients = Array.Empty<Guid>()
    };

    // Disable recycle bin for this job
    request["Options"] = new BulkDeleteOptions
    {
        CanRecoverDeletedRecords = false
    };

    BulkDeleteResponse response =
        (BulkDeleteResponse)service.Execute(request);
    return response.JobId;
}
```

---

### Sandbox fast delete

For scenarios that require maximum deletion throughput, you can enable sandbox fast delete mode by setting `RunJobForSandbox` to `true`. In this mode, the bulk delete job bypasses the standard SDK pipeline entirely and uses direct cascade engine deletion, achieving higher throughput.

When sandbox fast delete is enabled, the following are skipped:

- Preoperation and post-operation plug-in execution
- Synchronous and asynchronous workflow triggers
- Recycle bin storage (records are permanently deleted)
- Custom business logic registered on the Delete message

The following are preserved when performing fast delete:

- Cascade delete rules based on table relationship configuration
- Referential integrity (foreign key relationships)
- Security privilege checks
- Sync change tracking for downstream replication

> [!IMPORTANT]
> Sandbox fast delete mode bypasses the entire SDK plug-in pipeline. Any custom plug-ins, workflows, or business logic registered on the Delete message do NOT execute for records deleted in this mode. Included are audit plug-ins, integration plug-ins, and any custom validation logic. Additionally, records deleted in sandbox mode can't be recovered from the recycle bin. Use this option only when you're certain that no critical business logic depends on delete-time plug-in execution, and that permanent, irrecoverable deletion is acceptable.

#### Example: Sandbox fast delete

Learn how to use high-performance sandbox delete mode for maximum throughput.

##### [Web API](#tab/webapi)

```http
POST [Organization Uri]/api/data/v9.2/BulkDelete HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
Accept: application/json
Content-Type: application/json

{
    "QuerySet": [
        {
            "@odata.type": "Microsoft.Dynamics.CRM.QueryExpression",
            "EntityName": "account",
            "ColumnSet": {
                "AllColumns": true
            },
            "Distinct": false
        }
    ],
    "JobName": "Delete accounts - sandbox fast delete",
    "SendEmailNotification": false,
    "ToRecipients": [],
    "CCRecipients": [],
    "RecurrencePattern": "",
    "StartDateTime": "2026-03-13T06:30:00Z",
    "Options": {
        "CanRecoverDeletedRecords": false,
        "RunJobForSandbox": true
    }
}
```

##### [SDK for .NET](#tab/sdk)

```csharp
static Guid BulkDeleteSandboxFastDelete(IOrganizationService service)
{
    var request = new BulkDeleteRequest
    {
        JobName = "Delete accounts - sandbox fast delete",
        QuerySet = new QueryExpression[]
        {
            new QueryExpression
            {
                EntityName = "account",
                ColumnSet = new ColumnSet(true)
            }
        },
        StartDateTime = DateTime.UtcNow,
        RecurrencePattern = string.Empty,
        SendEmailNotification = false,
        ToRecipients = Array.Empty<Guid>(),
        CCRecipients = Array.Empty<Guid>()
    };

    // Enable sandbox fast delete (bypasses plug-ins & recycle bin)
    request["Options"] = new BulkDeleteOptions
    {
        CanRecoverDeletedRecords = false,
        RunJobForSandbox = true
    };

    BulkDeleteResponse response =
        (BulkDeleteResponse)service.Execute(request);
    return response.JobId;
}
```

---

## Long-term retained data

Bulk deletion is also available for long-term retained data. Run a bulk delete as you normally would, but set the query's `DataSource` field to *retained*.

### [SDK for .NET](#tab/sdk)

By using the SDK, you can use either <xref:Microsoft.Xrm.Sdk.Query.QueryExpression> or the [FetchXmlToQueryExpressionRequest class](xref:Microsoft.Crm.Sdk.Messages.FetchXmlToQueryExpressionRequest) with [IOrganizationService.Execute](xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute%2A) to convert FetchXml to a <xref:Microsoft.Xrm.Sdk.Query.QueryExpression>.

#### QueryExpression

Use the [QueryExpression.DataSource property](xref:Microsoft.Xrm.Sdk.Query.QueryExpression.DataSource) to indicate the query is for retained rows only. Set the value to `retained` to bulk-delete retained data.

```csharp
static Guid BulkDeleteRetainedAccountsExample(IOrganizationService service)
{
    var request = new BulkDeleteRequest
    {
        JobName = "Bulk Delete Retained Accounts"
    };

    // Create query and add additional filters as needed
    QueryExpression query = new QueryExpression
    {
        EntityName = "account",
        DataSource = "retained"
    };

    request.QuerySet = new QueryExpression[]{query};

    request.StartDateTime = DateTime.Now;
    request.RecurrencePattern = string.Empty;
    request.SendEmailNotification = false;
    request.ToRecipients = Array.Empty<Guid>();
    request.CCRecipients = Array.Empty<Guid>();

    BulkDeleteResponse response = (BulkDeleteResponse)service.Execute(request);
    return response.JobId;
}
```

#### FetchXML

Add the `datasource='retained'` attribute to the `fetch` element to indicate the query is for retained rows only.

```csharp
static Guid BulkDeleteRetainedAccountsFetchXmlExample(IOrganizationService service) {
            
    var convertRequest = new FetchXmlToQueryExpressionRequest
    {
        FetchXml = @"
        <fetch datasource='retained'>
            <entity name='account'>
        </entity>
        </fetch>"
    };

    FetchXmlToQueryExpressionResponse convertResponse = (FetchXmlToQueryExpressionResponse)service.Execute(convertRequest);

    var request = new BulkDeleteRequest
    { JobName = "Bulk Delete Retained Accounts" };

    request.QuerySet = new QueryExpression[]{convertResponse.Query};

    request.StartDateTime = DateTime.Now;
    request.RecurrencePattern = string.Empty;
    request.SendEmailNotification = false;
    request.ToRecipients = Array.Empty<Guid>();
    request.CCRecipients = Array.Empty<Guid>();
           
    BulkDeleteResponse response = (BulkDeleteResponse)service.Execute(request);
    return response.JobId;
}
```

### [Web API](#tab/webapi)

Set the <xref:Microsoft.Dynamics.CRM.QueryExpression> `DataSource` property to `retained` in a Web API [BulkDelete action](xref:Microsoft.Dynamics.CRM.BulkDelete) to indicate the query is for retained rows only.

**Request:**

```http
POST [Organization Uri]/api/data/v9.2/BulkDelete HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
Accept: application/json
Content-Type: application/json

{
    "QuerySet": 
    [
        {
            "EntityName": "contact",
            "DataSource": "retained",
            "Criteria":
            {
                "FilterOperator": "And",
                "Conditions": 
                [
                    {
                        "AttributeName": "firstname",
                        "Operator": "Equal",
                        "Values" : [{"Value":"Bob","Type":"System.String"}]
                    }
                ]
            }
        }
    ],
    "JobName": "Bulk Delete Retained Contacts",
    "SendEmailNotification": false,
    "RecurrencePattern": "",
    "StartDateTime": "2023-03-07T05:00:00Z",
    "ToRecipients": [],
    "CCRecipients": []
}
```

**Response:**

```http
HTTP/1.1 200 OK
{
    "@odata.context": "[Organization Uri]/api/data/v9.1/$metadata#Microsoft.Dynamics.CRM.BulkDeleteResponse",
    "JobId": "3093d67f-21f0-ed11-8b48-6045bdd92a32"
}
```

[Learn more about Web API actions](webapi/use-web-api-actions.md).

---

## Samples

Look at the following SDK for .NET samples for the bulk delete feature:

- [Sample: Bulk delete exported records](org-service/samples/bulk-delete-exported-records.md)
- [Sample: Bulk delete records that match common criteria](org-service/samples/bulk-delete-records-match-common-criteria.md)

### See also

- [Long-term data retention](long-term-retention.md)  
- [BulkDelete Action reference](/power-apps/developer/data-platform/webapi/reference/bulkdelete)
- [Delete data in bulk](delete-data-bulk.md)
- [Restore deleted records](restore-deleted-records.md)
- [Use Web API actions](./webapi/use-web-api-actions.md)
- [BulkDeleteOperation table reference](./reference/entities/bulkdeleteoperation.md)

[!INCLUDE [footer-include](../../includes/footer-banner.md)]
