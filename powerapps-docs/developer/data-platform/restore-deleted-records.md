---
title: Restore deleted records with code
description: Learn how to configure tables so that you can restore records deleted within a specified time period. 
ms.date: 01/30/2026
author: rijoshi1
ms.author: rijoshi
ms.reviewer: jdaly
ms.topic: how-to
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
contributors:
 - JimDaly
 - shahzorkhan123
 - TakeN0
ms.custom: bap-template
---
# Restore deleted records with code

[This article is prerelease documentation and is subject to change.]

Sometimes people delete records that they shouldn't. Administrators can enable deleted record keeping so that they can restore deleted records within a specified period of time. [Learn how administrators can restore deleted records](/power-platform/admin/restore-deleted-table-records).

[When deleted record keeping is enabled](/power-platform/admin/restore-deleted-table-records#enable-restore-table-records), developers can use the `Restore` message to restore deleted record before the specified period of time. The period of time can be up to 30 days.

## Retrieve deleted records that can be restored

To retrieve deleted records that can be restored, set the datasource of the query to '`bin`'.
The following examples return up to three deleted account records.

 ### [SDK for .NET](#tab/sdk)

When using the SDK, you can retrieve data using [FetchXml](fetchxml/overview.md) or [QueryExpression](/dotnet/api/microsoft.xrm.sdk.query.queryexpression).  

When you retrieve data by using FetchXml, set the [fetch element](fetchxml/reference/fetch.md) `datasource` attribute to '`bin`' when you retrieve records.

```csharp
static EntityCollection GetDeletedAccountRecordsFetchXml(IOrganizationService service) {

   string queryString = @"<fetch top='3' datasource='bin'>
                     <entity name='account'>
                        <attribute name='name' />
                     </entity>
                     </fetch>";
   
   FetchExpression query = new(queryString);

   return service.RetrieveMultiple(query);
}
```

When you retrieve data by using [QueryExpression](/dotnet/api/microsoft.xrm.sdk.query.queryexpression), set the [QueryExpression.DataSource](/dotnet/api/microsoft.xrm.sdk.query.queryexpression.datasource) property to '`bin`' when you retrieve records.

```csharp
static EntityCollection GetDeletedAccountRecordsQueryExpression(IOrganizationService service) {

   QueryExpression query = new("account") { 
         ColumnSet = new ColumnSet("name"),
         DataSource = "bin",
         TopCount = 3
   };

   return service.RetrieveMultiple(query);
}
```

- [Use FetchXml to retrieve data](fetchxml/retrieve-data.md)
- [Build queries with QueryExpression](org-service/build-queries-with-queryexpression.md)


### [Web API](#tab/webapi)

By using Web API, you can retrieve records with FetchXml or OData syntax.

> [!NOTE]
> Currently, by using Web API, you can only retrieve *deleted* records by using FetchXml.

When you retrieve data by using FetchXml, set the [fetch element](fetchxml/reference/fetch.md) `datasource` attribute to '`bin`' when you retrieve records.

This `Get-DeletedAccountRecords` PowerShell function returns up to three deleted account records.

This Web API example and others in this article depend on the `$environmentUrl` and `$baseHeaders` variables as described in [Quick Start Web API with PowerShell and Visual Studio Code](webapi/quick-start-ps.md).

```powershell
function Get-DeletedAccountRecords{

   $query = @()
   $query += "<fetch top='3' datasource='bin'>"
   $query += "<entity name='account'>"
   $query += "<attribute name='name' />"
   $query += "</entity>"
   $query += "</fetch>"

   $uri = $environmentUrl
   $uri += 'accounts'
   $uri += '?fetchXml=' + [uri]::EscapeUriString($query -join '')

   $RetrieveMultipleRequest = @{
      Uri     = $uri
      Method  = 'Get'
      Headers = $baseHeaders
   }
   Invoke-RestMethod @RetrieveMultipleRequest

}
```

- [Use FetchXml to retrieve data](fetchxml/retrieve-data.md)
- [Use PowerShell and Visual Studio Code with the Dataverse Web API](webapi/use-ps-and-vscode-web-api.md)

---

## Restore a deleted record

Use the `Restore` message to restore a deleted record. The `Target` parameter isn't a reference to a deleted record. It's a full record so you can set column values while you restore the record. All the original column values are restored unless you override them by setting values during the `Restore` operation.

> [!NOTE]
> At this time, you can only restore records by using the primary key value. You can't use an alternate key to restore a record.


How you restore a deleted record depends on whether you're using the SDK for .NET or Web API.

 ### [SDK for .NET](#tab/sdk)

How you restore a record by using the SDK for .NET depends on whether you're generating early bound types by using [pac modelbuilder](/power-platform/developer/cli/reference/modelbuilder), or if you're using the late bound style.

[Learn about late-bound and early-bound programming using the SDK for .NET](org-service/early-bound-programming.md)


#### Early bound example

The static `RestoreAccountRecordEarlyBound` method uses the `RestoreRequest<T>` and `Account` classes generated by using the [pac modelbuilder](/power-platform/developer/cli/reference/modelbuilder).

```csharp
/// <summary>
/// Restores an account record
/// </summary>
/// <param name="service">The authenticated IOrganizationService instance</param>
/// <param name="accountId">The ID of the deleted account record.</param>
/// <param name="originalName">The original name value for the account record.</param>
/// <returns>The ID of the restored account</returns>
static Guid RestoreAccountRecordEarlyBound(
    IOrganizationService service, 
    Guid accountId,
    string originalName)
{
    Account accountToRestore = new()
    {
        Id = accountId,
        // Appending '(Restored)' to the original name
        // to demonstrate overwriting a value.
        Name = originalName + " (Restored)"
    };

    RestoreRequest<Account> request = new()
    {
        Target = accountToRestore
    };

    var response = (RestoreResponse)service.Execute(request);
    return response.id;
}
```

#### Late bound example

The static `RestoreAccountRecordLateBound` method uses the [OrganizationRequest](/dotnet/api/microsoft.xrm.sdk.organizationrequest) class to invoke the `Restore` message, setting the `Target` parameter.

```csharp
/// <summary>
/// Restores an account record
/// </summary>
/// <param name="service">The authenticated IOrganizationService instance</param>
/// <param name="accountId">The ID of the deleted account record.</param>
/// <param name="originalName">The original name value for the account record.</param>
/// <returns>The ID of the restored account</returns>
static Guid RestoreAccountRecordLateBound(
   IOrganizationService service,
   Guid accountId,
   string originalName)
{
   Entity accountToRestore = new("account", accountId)
   {
         Attributes = {
            // Appending '(Restored)' to the original name
            // to demonstrate overwriting a value.
            {"name", originalName + " (Restored)"}
         }
   };

   OrganizationRequest request = new("Restore")
   {
         Parameters = {
            { "Target", accountToRestore }
         }
   };

   OrganizationResponse response = service.Execute(request);

   return (Guid)response.Results["id"];
}
```

[Use messages with the SDK for .NET](org-service/use-messages.md)

### [Web API](#tab/webapi)

Use the [Restore action](/power-apps/developer/data-platform/webapi/reference/restore) to restore deleted records. This operation returns a [RestoreResponse complex type](/power-apps/developer/data-platform/webapi/reference/restoreresponse) that has an `id` property set to the ID of the restored record.

#### Restore any type of record without overwriting column values

The `Restore-AnyRecord` PowerShell function shows how to restore any type of record by referencing it using the full URL to the record and the `@odata.id` annotation. Pass a relative URL like `contacts(0ad63f65-990d-ef11-9f89-6045bdece8bb)` to the `relativeUri` parameter of this function. However, with this approach you can't overwrite any values for the record.

```powershell
function Restore-AnyRecord{
   param(
      [Parameter(Mandatory)]
      [uri]$relativeUri
   )

   $uri = $environmentUrl + 'api/data/v9.2/'
   $uri += 'Restore'
   
   $body = @{
      'Target' = @{
         '@odata.id' = $environmentUrl + 'api/data/v9.2/' + $relativeUri
      }
   }

   $postHeaders = $baseHeaders.Clone()
   $postHeaders.Add('Content-Type', 'application/json')

   $RestoreRequest = @{
      Uri     = $uri
      Method  = 'Post'
      Headers = $postHeaders
      Body    = (ConvertTo-Json $body) 
   }
  
  $id = Invoke-RestMethod @RestoreRequest | Select-Object -ExpandProperty id

  return $id
}
```

#### Restore a record and overwrite column values

The `Restore-AccountRecord` PowerShell function shows how to restore an account record and overwrite a value. There are three requirements:

- [Specify the table type parameter](webapi/use-web-api-actions.md#specify-the-table-type-parameter) by using the `@odata.type` with the fully qualified name of the entity type. This annotation tells OData what type of record it is.
- To specify the record, include the primary key value, in this case `accountid` .
- Specify any properties you want to overwrite, in this case the `name` property.


```powershell
function Restore-AccountRecord {
   param(
      [Parameter(Mandatory)]
      [guid]$recordId,
      [Parameter(Mandatory)]
      [string]$originalName
   )
   
   $uri = $environmentUrl
   $uri += 'Restore'
   
   $body = @{
      'Target' = @{
         '@odata.type' = 'Microsoft.Dynamics.CRM.account'
         # Appending '(Restored)' to the original name
         # to demonstrate overwriting a value.
         'name'       = ($originalName + ' (Restored)')
         'accountid'  = $recordId.Guid
      }
   }

   $postHeaders = $baseHeaders.Clone()
   $postHeaders.Add('Content-Type', 'application/json')

   $RestoreRequest = @{
      Uri     = $uri
      Method  = 'Post'
      Headers = $postHeaders
      Body    = (ConvertTo-Json $body) 
   }
  
  $id = Invoke-RestMethod @RestoreRequest | Select-Object -ExpandProperty id

  return $id
}
```

---

### Best practices when restoring records

Avoid the following issues when restoring records:

- [Restore related records before restoring primary record](#restore-related-records-before-restoring-primary-record)
- [Don't specify primary key values when creating records](#dont-specify-primary-key-values-when-creating-records)
- [Records with matching alternate key values block restore](#records-with-matching-alternate-key-values-block-restore)
- [Records using removed Choice options aren't restored](#records-using-removed-choice-options-arent-restored)
- [Primary Key Violation on Delete](#primary-key-violation-on-delete)


#### Restore related records before restoring primary record

If some related records reference records that the cascade relationship removed, the restore operation fails. To avoid this problem, always restore the related records that the current record deletion didn't remove before trying to restore the primary record.

> Name: `RefCannotBeRestoredRecycleBinNotFound`<br />
> Code: `0x80049959`<br />
> Number: `-2147182247`<br />
> Message: `Entity with id '<Guid Value>' and logical name '<Entity.LogicalName>' does not exist. We cannot restore the reference '<Referred Primary Key Name>' that must be restored as part of this Restore call. ValueToBeRestored: <Guid Value>, ReferencedEntityName: <Referenced Entity Name>, AttributeName: <Referred Attribute Name>`


#### Don't specify primary key values when creating records

Always let Dataverse set the primary key when creating a record. If you create a new record that has the same primary key value as a deleted record, you can't restore the deleted record. If you want to restore the deleted record, delete the new record first.

> Name: `DuplicateExceptionRestoreRecycleBin`<br />
> Code: `0x80044a02`<br />
> Number: `-2147182279`<br />
> Message: `Please delete the existing conflicting record '<Entity Platform Name>' with primary key '<Primary Key Name>' and primary key value '<Primary Key Value>' before attempting restore.`

#### Records with matching alternate key values block restore

If you create a record that has the same alternate key column values as a deleted record, you can't restore the deleted record. If you want to restore the deleted record, delete the new record first.

> Name: `DuplicateExceptionEntityKeyRestoreRecycleBin`<br />
> Code: `0x80049929`<br />
> Number: `-2147182295`<br />
> Message: `Duplicate entity key preventing restore of record '<Entity Platform Name>' with primary key '<Primary Key Name>' and primary key value '<Primary Key Value>'. See inner exception for entity key details.`

#### Records using removed Choice options aren't restored

If you delete an optionset option, and that option was used in a deleted record, you can't restore the record because the option is now invalid. Before deleting an option set option, check that no records use that option, including deleted records.

> Name: `PicklistValueOutOfRangeRecycleBin`<br />
> Code: `0x80049949`<br />
> Number: `-2147182263`<br />
> Message: `Picklist value not valid, please add the invalid value back to the picklist before restoring record`


#### Primary Key Violation on Delete

If the record with the same primary key already exists, nothing happens. To enforce that all deleted items are recorded, set the `DoNotEnforcePrimaryKeyOrgSettingRecycleBin` setting by using the [OrgDBOrgSettings tool for Microsoft Dynamics CRM](/power-platform/admin/environment-database-settings). 

After enabling this setting, you might receive the following error:

> Name: `DuplicateExceptionRestoreRecycleBin`<br />
> Code: `0x80049939 `<br />
> Number: `-2147182279`<br />
> Message: `A record that has the attribute values Deleted Object already exists on Delete.`

## Detect which tables are enabled for deleted record keeping

Before you enable this feature, the [Deleted Record Keeping Configuration (RecycleBinConfig) table](reference/entities/recyclebinconfig.md) has no rows.

Over time, most tables will support deleted record keeping. [Solution components](/power-platform/alm/solution-concepts-alm#solution-components), [virtual tables](../../maker/data-platform/create-edit-virtual-entities.md), and [elastic tables](../../maker/data-platform/create-edit-elastic-tables.md) aren't supported for deleted record keeping. Some tables that aren't currently enabled might be enabled later (for example, tables with more than 600 columns). For a list of tables that don't support this feature, see [Tables not currently supported](#tables-not-currently-supported-for-deleted-record-keeping).

You can also [disable deleted record keeping for the environment](#disable-deleted-record-keeping-for-the-environment). If deleted record keeping isn't enabled for a table, you won't [find any records eligible to be restored](#retrieve-deleted-records-that-can-be-restored). You can query Dataverse to find out whether deleted record keeping is enabled for a table or not.

Tables that are enabled for deleted record keeping have a row in the `RecycleBinConfig` table where the `statecode` is active and `isreadyforrecyclebin` is true. The `RecycleBinConfig` table doesn't contain the name of the table, but refers to a row in the [Entity table](reference/entities/entity.md) where the `logicalname` column contains the [LogicalName](/dotnet/api/microsoft.xrm.sdk.metadata.entitymetadata.logicalname) of the table.

Use the following FetchXml query to detect which tables have deleted record keeping enabled:

```xml
<fetch>
  <entity name='recyclebinconfig'>
    <filter type='and'>
      <condition attribute='statecode'
        operator='eq'
        value='0' />
      <condition attribute='isreadyforrecyclebin'
        operator='eq'
        value='1' />
    </filter>
    <link-entity name='entity'
      from='entityid'
      to='extensionofrecordid'
      link-type='inner'
      alias='entity'>
      <attribute name='logicalname' />
      <order attribute='logicalname' />
    </link-entity>
  </entity>
</fetch>
```

[Learn to query data using FetchXml](fetchxml/overview.md)

## Detect which tables aren't enabled for deleted record keeping

To know which tables aren't enabled for deleted record keeping, use the following FetchXml query that is the reverse of the one found in [Detect which tables are enabled](#detect-which-tables-are-enabled-for-deleted-record-keeping).

```xml
<fetch>
  <entity name='entity'>
    <attribute name='logicalname' />
    <filter type='or'>
      <condition entityname='recyclebin'
        attribute='extensionofrecordid'
        operator='null' />
      <condition entityname='recyclebin'
        attribute='statecode'
        operator='ne'
        value='0' />
      <condition entityname='recyclebin'
        attribute='isreadyforrecyclebin'
        operator='ne'
        value='1' />
    </filter>
    <order attribute='logicalname' />
    <link-entity name='recyclebinconfig'
      from='extensionofrecordid'
      to='entityid'
      link-type='outer'
      alias='recyclebin' />
  </entity>
</fetch>
```

[Learn to query data using FetchXml](fetchxml/overview.md)

The results of this query as of May 2024 when this feature began are in [Tables not currently supported for deleted record keeping](#tables-not-currently-supported-for-deleted-record-keeping).


## Retrieve and set the automatic cleanup time period configuration for deleted record keeping

Set the value that determines how long deleted records are available to be restored in the [RecycleBinConfig.CleanupIntervalInDays](reference/entities/recyclebinconfig.md#BKMK_CleanupIntervalInDays) column where the [Name](reference/entities/recyclebinconfig.md#BKMK_Name) column value is `organization`. Every other row in the `RecycleBinConfig` table has a `CleanupIntervalInDays` column value of `-1`. This value indicates it uses the same values set for the `organization` table.

To specify a different value for another table, set the `CleanupIntervalInDays` column value where the `Name` matches the logical name of the table. This column accepts values up to 30. Don't set this value unless you want to use a value different from the organization default.

 ### [SDK for .NET](#tab/sdk)

Use this static `SetCleanupIntervalInDays` method to set the `CleanupIntervalInDays` column value for a specific table.

```csharp
/// <summary>
/// Updates the CleanupIntervalInDays value for a specified table
/// </summary>
/// <param name="service">The authenticated IOrganizationService instance</param>
/// <param name="entityId">The entityId of the table</param>
/// <param name="cleanupIntervalInDays">The new CleanupIntervalInDays value</param>
static void SetCleanupIntervalInDays(
    IOrganizationService service,
    Guid entityId,
    int cleanupIntervalInDays)
{

    QueryExpression query = new("recyclebinconfig")
    {
        ColumnSet = new ColumnSet("recyclebinconfigid"),
        Criteria = new FilterExpression(LogicalOperator.And)
        {
            Conditions = {
              {
                  new ConditionExpression(
                      attributeName: "extensionofrecordid",
                      conditionOperator: ConditionOperator.Equal,
                      value: entityId)
              }
          }
        }
    };

    EntityCollection records = service.RetrieveMultiple(query);

    if (records.Entities.Count.Equals(1))
    {
        Guid id = records.Entities[0].Id;

        Entity record = new(entityName: "recyclebinconfig", id: id)
        {
            Attributes = {
                { "cleanupintervalindays", cleanupIntervalInDays }
            }
        };

        service.Update(record);

    }
    else
    {
        throw new Exception($"Deleted record keeping configuration for table '{tableLogicalName}' not found.");
    }
}
```

[Use the SDK for .NET](org-service/overview.md)

### [Web API](#tab/webapi)

This `Set-CleanupIntervalInDays` PowerShell function retrieves the `recyclebinconfig` row that has the entityId that matches the `$tableEntityId` parameter. Then it updates the `cleanupintervalindays` column  property of the record to the value of the `$cleanupIntervalInDays` parameter.

This function depends on the `Get-Records` and `Update-Record` functions described in [Create table operations functions](webapi/use-ps-and-vscode-web-api.md#create-table-operations-functions).

```powershell
function Set-CleanupIntervalInDays{
      param(
         [Parameter(Mandatory)]
         [guid]$tableEntityId,
         [Parameter(Mandatory)]
         [int]$cleanupIntervalInDays
      )
      $records = (Get-Records `
         -setName 'recyclebinconfigs' `
         -query "?`$filter=_extensionofrecordid_value eq $($tableEntityId)").value
   
      if ($records.Count -eq 1) {
         $recyclebinconfigId = $records[0].recyclebinconfigid
   
         Update-Record `
               -setName 'recyclebinconfigs' `
               -id $recyclebinconfigId `
               -body @{
               'cleanupintervalindays' = $cleanupIntervalInDays
         }
      }
      else {
         Write-Host "Deleted record keeping configuration for table $tableEntityId not found."
      }
}
```

- [Use the Microsoft Dataverse Web API](webapi/overview.md)
- [Quick Start Web API with PowerShell and Visual Studio Code](webapi/quick-start-ps.md)
- [Use PowerShell and Visual Studio Code with the Dataverse Web API](webapi/use-ps-and-vscode-web-api.md)

---


## Disable deleted record keeping for the environment

> [!NOTE]
> The preferred way to disable deleted record keeping for an environment is to [turn it off in the Power Platform admin center](/power-platform/admin/restore-deleted-table-records#enable-restore-table-records). The method described here might change before the feature becomes generally available.

Delete the row in the [RecycleBinConfig](reference/entities/recyclebinconfig.md) table where the `name` value is `organization`. This action deletes all the records in the `RecycleBinConfig` table and disables deleted record keeping for the environment.

> [!IMPORTANT]
> Don't try to delete other individual records. It's important that Dataverse manages this action.

## Manage restoring records deleted by custom business logic

Dataverse provides a mechanism to manage desired actions for related records when a row is deleted. This configuration data is part of the definition of the relationship. When a related record is deleted, you can configure four possible behaviors:

|Delete Behavior|Description|
|---------|---------|
|**Cascade All**|Deletes the related records.|
|**Remove Link**|Sets the lookup columns to the deleted record to null.|
|**Cascade None**|Applies no changes to related records. (Internal Only) |
|**Restrict**|Prevents deleting the record to maintain data integrity. The record can't be deleted unless there are no records related for this relationship.|

[Learn more about relationship behaviors](../../maker/data-platform/create-edit-entity-relationships.md#behaviors).

When you configure the relationship for **Cascade All**, **Remove Link**, or **Restrict**, Dataverse manages these behaviors and there's nothing extra to do.

If you configure a relationship to use the **Remove Link** behavior but the relationship is supposed to delete the related record, you might need custom logic that applies some custom behavior. For example, you might wish to respond to this behavior differently and implement your own *'Cascade some'* behavior based on rules you define. For example, you might delete inactive records or records that weren't updated in a certain period of time. This logic is usually implemented by using a plug-in, but it could also be done by using Power Automate with the [Microsoft Dataverse connector: When a row is added, modified or deleted trigger](/connectors/commondataserviceforapps/#when-a-row-is-added,-modified-or-deleted).

If you have this kind of custom business logic, Dataverse doesn't know about it and can't automatically 'undo' your logic. However, you can register another plug-in on the `Restore` message to reverse whatever custom logic you have. Or you could use Power Automate and the [Microsoft Dataverse connector: When an action is performed trigger](/connectors/commondataserviceforapps/#when-an-action-is-performed).

> [!IMPORTANT]
> Be careful about the context when you register plug-in steps for the `Restore` message. The record you're restoring isn't available in the `PreOperation` stage. If you need to create related records, use the `PostOperation` stage. [Learn more about plug-in stages](event-framework.md#event-execution-pipeline).
>
> The [InputParameters](understand-the-data-context.md#inputparameters) and [OutputParameters](understand-the-data-context.md#outputparameters) of the `Restore` message are similar to `Create` message, so plug-ins written to be registered for the `Create` message can be re-used for the `Restore` message with fewer changes.

## Tables not currently supported for deleted record keeping

The query described in [Detect which tables aren't enabled](#detect-which-tables-arent-enabled-for-deleted-record-keeping) was used to generate [this list](/power-platform/admin/restore-deleted-table-records#tables-not-currently-supported-for-the-deleted-records-feature) in August 2024.



### See also

[Restore deleted Microsoft Dataverse table records](/power-platform/admin/restore-deleted-table-records)
