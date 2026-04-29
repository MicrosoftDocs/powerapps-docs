---
title: Bulk delete control options
description: Learn how to control deletion of bulk data using code.
#customer intent: Write code to control bulk deletion of data.
ms.date: 04/28/2026
author: phecke
ms.author: pehecke
ms.reviewer: pehecke
ms.subservice: dataverse-developer
---

# Bulk delete control options

The `Options` parameter on the `BulkDelete` action or message allows you to control how the bulk delete job processes table rows (records). You can use the parameter to:

- Disable the recycle bin for bulk-deleted records. Disabling the recycle bin improves performance by skipping the overhead of storing deleted records for recovery.
- Enable sandbox fast delete mode to bypass the standard SDK pipeline (plug-ins, workflows, recycle bin). Fast delete achieves higher deletion throughput.

## Use the Options parameter

The `Options` parameter accepts a `BulkDeleteOptions` object with the following properties.

| Property | Type | Default | Description |
|---|---|---|---|
| CanRecoverDeletedRecords | Boolean | null (recycle bin enabled) | When set to false, records deleted by the bulk delete job are permanently removed and can't be recovered from the recycle bin. |
| RunJobForSandbox | Boolean | null (standard pipeline) | When set to true, the bulk delete job uses the high-performance sandbox delete mode, bypassing plug-ins, workflows, and the recycle bin. |

### Example: Options parameter

The following examples demonstrate how to use the `Options` parameter with the `BulkDelete` action or message request.

#### [Web API](#tab/webapi)

Use the `Options` property in the request body of the `BulkDelete` action. The `Options` object is a `BulkDeleteOptions` complex type.

**Request:**

```http
POST [Organization Uri]/api/data/v9.2/BulkDelete HTTP/1.1
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
Content-Type: application/json

{
    "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.BulkDeleteResponse",
    "JobId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
}
```

##### Options parameter values

| Scenario | CanRecoverDeletedRecords | RunJobForSandbox | Effect |
| -- | -- | -- | -- |
| Default (standard delete) | true or omitted | false or omitted | Records go through standard pipeline. Deleted records stored in recycle bin if enabled.|
| Skip recycle bin|  false | false or omitted | Records go through standard pipeline. Recycle bin is bypassed for this job.|
| Sandbox fast delete | false | true | Bypasses SDK pipeline and recycle bin. Maximum throughput.|

#### [SDK for .NET](#tab/sdk)

Use the `BulkDeleteRequest` class and set the `Options` parameter in the request's `Parameters` collection. The value is a `BulkDeleteOptions` object from the Microsoft.Xrm.Sdk namespace.

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

## Control recycle bin behavior

By default, when the recycle bin is enabled for your environment, all records deleted by a bulk delete job are stored in the recycle bin before deletion. The recycle bin allows administrators to recover accidentally deleted records, but adds significant I/O overhead for each deleted record.
To disable the recycle bin for a bulk delete job, set `CanRecoverDeletedRecords` to `false` in the `Options` parameter. This setting can approximately double the deletion throughput by eliminating the overhead of:

- Creating DeletedItemReference records
- Copying record data to recycle bin storage tables
- Updating restore data blobs for each deleted record

> [!WARNING]
> When `CanRecoverDeletedRecords` is set to false, deleted records are permanently removed and can't be recovered from the recycle bin. This action is irreversible. Ensure that you verified the query criteria and have appropriate backups before running a bulk delete job with this option. This setting only affects the current bulk delete job; it doesn't change the environment-level recycle bin configuration.

### Example: Disable the recycle bin for faster deletion

Permanently delete records without storing them in the recycle bin.

#### [Web API](#tab/webapi)

```http
POST [Organization Uri]/api/data/v9.2/BulkDelete HTTP/1.1
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

#### [SDK for .NET](#tab/sdk)

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

## Sandbox fast delete

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

### Example: Sandbox fast delete

Learn how to use high-performance sandbox delete mode for maximum throughput.

#### [Web API](#tab/webapi)

```http
POST [Organization Uri]/api/data/v9.2/BulkDelete HTTP/1.1
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

#### [SDK for .NET](#tab/sdk)

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

### See also

- [BulkDelete Action reference](/power-apps/developer/data-platform/webapi/reference/bulkdelete)
- [Delete data in bulk](delete-data-bulk.md)
- [Restore deleted records](restore-deleted-records.md)
- [Use Web API actions](./webapi/use-web-api-actions.md)
- [BulkDeleteOperation table reference](./reference/entities/bulkdeleteoperation.md)
