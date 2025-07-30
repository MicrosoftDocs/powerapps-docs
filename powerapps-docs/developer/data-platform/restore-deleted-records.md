---
title: Restore deleted records with code (preview)
description: Learn how to configure tables to enable a recycle bin so that you can restore records deleted within a specified time period. 
ms.date: 09/04/2024
author: adkuppa
ms.author: adkuppa
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
# Restore deleted records with code (preview)

[!INCLUDE [preview-include](../../cards/includes/preview-include.md)]

Sometimes people delete records that they shouldn't. Administrators can enable a recycle bin for tables so that they can restore deleted records within a specified period of time. [Learn how administrators can restore deleted records](/power-platform/admin/restore-deleted-table-records)

[When the recycle bin is enabled](/power-platform/admin/restore-deleted-table-records#enable-restore-table-records), developers can use the `Restore` message to restore deleted record before the specified period of time. The period of time can be up to 30 days.

## Retrieve deleted records that can be restored

To retrieve deleted records that can be restored, set the datasource of the query to '`bin`'.
The following examples return up to three deleted account records.

 ### [SDK for .NET](#tab/sdk)

When using the SDK, you can retrieve data using [FetchXml](fetchxml/overview.md) or [QueryExpression](/dotnet/api/microsoft.xrm.sdk.query.queryexpression).  

When you retrieve data using FetchXml, set the [fetch element](fetchxml/reference/fetch.md) `datasource` attribute to '`bin`' when you retrieve records.

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

When you retrieve data using [QueryExpression](/dotnet/api/microsoft.xrm.sdk.query.queryexpression), set the [QueryExpression.DataSource](/dotnet/api/microsoft.xrm.sdk.query.queryexpression.datasource) property to '`bin`' when you retrieve records.

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

With Web API, you can retrieve records using FetchXml or OData syntax.

> [!NOTE]
> Currently, with Web API you can only retrieve *deleted* records using FetchXml.

When you retrieve data using FetchXml, set the [fetch element](fetchxml/reference/fetch.md) `datasource` attribute to '`bin`' when you retrieve records.

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

Use the `Restore` message to restore a deleted record. The `Target` parameter isn't a reference to a deleted record, it's a full record so you can set column values while you restore the record. All the original column values are restored unless you override them by setting values during the `Restore` operation.

> [!NOTE]
> At this time you can only restore records using the primary key value. You can't use an alternate key to restore a record.


How you restore a deleted record depends on whether you're using the SDK for .NET or Web API.

 ### [SDK for .NET](#tab/sdk)

How you restore a record using the SDK for .NET depends on whether you're generating early bound types using [pac modelbuilder](/power-platform/developer/cli/reference/modelbuilder), or if you're using the late bound style.

[Learn about late-bound and early-bound programming using the SDK for .NET](org-service/early-bound-programming.md)


#### Early bound example

The static `RestoreAccountRecordEarlyBound` method uses the `RestoreRequest<T>` and `Account` classes generated using the [pac modelbuilder](/power-platform/developer/cli/reference/modelbuilder).

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

This `Restore-AnyRecord` PowerShell function shows how any type record can be restored by referencing it using the full URL to the record and the `@odata.id` annotation. Pass a relative URL like `contacts(0ad63f65-990d-ef11-9f89-6045bdece8bb)` to the `relativeUri` parameter of this function. However, with this approach you can't overwrite any values for the record.

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

This `Restore-AccountRecord` PowerShell function shows how to restore an account record and overwrite a value. There are three requirements:

- [Specify the table type parameter](webapi/use-web-api-actions.md#specify-the-table-type-parameter) using the `@odata.type` with the fully qualified name of the entity type. This annotation tells OData what type of record it is.
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

The following are issues you can avoid when restoring records:

- [Restore related records before restoring primary record](#restore-related-records-before-restoring-primary-record)
- [Don't specify primary key values when creating records](#dont-specify-primary-key-values-when-creating-records)
- [Records with matching alternate key values block restore](#records-with-matching-alternate-key-values-block-restore)
- [Records using removed Choice options aren't restored](#records-using-removed-choice-options-arent-restored)
- [Primary Key Violation on Delete](#primary-key-violation-on-delete)


#### Restore related records before restoring primary record

If some related records whose reference were removed as part of cascade relationship no longer exist, the restore operation fails. To avoid this problem, always restore the related records not deleted as part of current record before trying to restore the primary record.

> Name: `RefCannotBeRestoredRecycleBinNotFound`<br />
> Code: `0x80049959`<br />
> Number: `-2147182247`<br />
> Message: `Entity with id '<Guid Value>' and logical name '<Entity.LogicalName>' does not exist. We cannot restore the reference '<Referred Primary Key Name>' that must be restored as part of this Restore call. ValueToBeRestored: <Guid Value>, ReferencedEntityName: <Referenced Entity Name>, AttributeName: <Referred Attribute Name>`


#### Don't specify primary key values when creating records

It's generally a good practice to always let Dataverse set the primary key when creating a record. If you create a new record that has the same primary key value as a deleted record, the deleted record can't be restored. If you do, you must delete the new record before you can restore the deleted one.

> Name: `DuplicateExceptionRestoreRecycleBin`<br />
> Code: `0x80044a02`<br />
> Number: `-2147182279`<br />
> Message: `Please delete the existing conflicting record '<Entity Platform Name>' with primary key '<Primary Key Name>' and primary key value '<Primary Key Value>' before attempting restore.`

#### Records with matching alternate key values block restore

If you create a record that has the same alternate key column values as a deleted record, you can't restore it. If you do, you must delete the new record before you can restore the deleted one.

> Name: `DuplicateExceptionEntityKeyRestoreRecycleBin`<br />
> Code: `0x80049929`<br />
> Number: `-2147182295`<br />
> Message: `Duplicate entity key preventing restore of record '<Entity Platform Name>' with primary key '<Primary Key Name>' and primary key value '<Primary Key Value>'. See inner exception for entity key details.`

#### Records using removed Choice options aren't restored

If you delete an optionset option, and that option was used in a deleted record, you can't restore it because the option is now invalid. Before deleting an option set option, check that no records use that option, including deleted records.

> Name: `PicklistValueOutOfRangeRecycleBin`<br />
> Code: `0x80049949`<br />
> Number: `-2147182263`<br />
> Message: `Picklist value not valid, please add the invalid value back to the picklist before restoring record`


#### Primary Key Violation on Delete

If the record with same primary key was already deleted before, copy to recycle bin is ignored for the record. To enforce all deleted items are stored in recycle bin, you can set the `DoNotEnforcePrimaryKeyOrgSettingRecycleBin` setting using the [OrgDBOrgSettings tool for Microsoft Dynamics CRM](/power-platform/admin/environment-database-settings). 

After enabling this setting, you might receive the following error:

> Name: `DuplicateExceptionRestoreRecycleBin`<br />
> Code: `0x80049939 `<br />
> Number: `-2147182279`<br />
> Message: `A record that has the attribute values Deleted Object already exists on Delete.`

## Detect which tables are enabled for recycle bin

Before the recycle bin feature is enabled, the [Recycle Bin Configuration (RecycleBinConfig) table](reference/entities/recyclebinconfig.md) has no rows.

In time, we expect that eventually most tables will be available to use the recycle bin feature. [Solution components](/power-platform/alm/solution-concepts-alm#solution-components), [virtual tables](../../maker/data-platform/create-edit-virtual-entities.md), and [elastic tables](../../maker/data-platform/create-edit-elastic-tables.md) aren't supported for recycle bin. During this preview, some tables not currently enabled might be enabled later (For example, tables with more than 400 columns). For a list of tables that don't support recycle bin, see [Tables not currently supported for Recycle Bin](#tables-not-currently-supported-for-recycle-bin).

You can also [disable recycle bin for specific tables](#disable-recycle-bin-for-a-table) and [disable recycle bin for the environment](#disable-recycle-bin-for-the-environment). If the recycle bin isn't enabled for a table, you won't [find any records eligible to be restored](#retrieve-deleted-records-that-can-be-restored). You can query Dataverse to find out whether the recycle bin is enabled for a table or not.

Tables that are enabled for recycle bin have a row in the `RecycleBinConfig` table where the `statecode` is active and `isreadyforrecyclebin` is true. The `RecycleBinConfig` table doesn't contain the name of the table, but refers to a row in the [Entity table](reference/entities/entity.md) where the `logicalname` column contains the [LogicalName](/dotnet/api/microsoft.xrm.sdk.metadata.entitymetadata.logicalname) of the table.

Use the following FetchXml query to detect which tables have recycle bin enabled:

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

## Detect which tables don't have recycle bin enabled

To know which tables aren't enabled for recycle bin, use the following FetchXml query that is the reverse of the one found in [Detect which tables are enabled for recycle bin](#detect-which-tables-are-enabled-for-recycle-bin).

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

The results of this query as of May 2024 when this preview feature began are in [Tables not currently supported for Recycle Bin](#tables-not-currently-supported-for-recycle-bin)


## Retrieve and set the automatic cleanup time period configuration for the recycle bin

The value to determine how long deleted records are available to be restored is set in the [RecycleBinConfig.CleanupIntervalInDays](reference/entities/recyclebinconfig.md#BKMK_CleanupIntervalInDays) column where the [Name](reference/entities/recyclebinconfig.md#BKMK_Name) column value is `organization`. Every other row in the `RecycleBinConfig` table has a `CleanupIntervalInDays` column value of `-1`. This value indicates it uses the same values set for the `organization` table.

To specify a different value for another table, set the `CleanupIntervalInDays` column value where the `Name` matches the logical name of the table. This column allows values up to 30, we recommend not setting it unless different from organization default value.

 ### [SDK for .NET](#tab/sdk)

You can use this static `SetCleanupIntervalInDays` method to set the `CleanupIntervalInDays` column value for a specific table.

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
        throw new Exception($"Recycle bin configuration for table '{tableLogicalName}' not found.");
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
         Write-Host "Recycle bin configuration for table $tableEntityId not found."
      }
}
```

- [Use the Microsoft Dataverse Web API](webapi/overview.md)
- [Quick Start Web API with PowerShell and Visual Studio Code](webapi/quick-start-ps.md)
- [Use PowerShell and Visual Studio Code with the Dataverse Web API](webapi/use-ps-and-vscode-web-api.md)

---

## Disable recycle bin for a table

To disable the recycle bin for a table, disable the `recyclebinconfig` record for the table by setting the [statecode](reference/entities/recyclebinconfig.md#BKMK_statecode) and [statuscode](reference/entities/recyclebinconfig.md#BKMK_statuscode) properties to their **Inactive** values: `2` and `1` respectively.

> [!NOTE]
> The following queries compare the `EntityId` value against the [Entity.EntityId](reference/entities/entity.md#BKMK_EntityId) column value, which stores the table [EntityMetadata.MetadataId ](/dotnet/api/microsoft.xrm.sdk.metadata.metadatabase.metadataid).

### [SDK for .NET](#tab/sdk)

Use this static `DisableRecycleBinForTable` method to disable the recycle bin for a specific table.

```csharp
/// <summary>
/// Disable the Recycle bin for a specified table
/// </summary>
/// <param name="service">The authenticated IOrganizationService instance</param>
/// <param name="tableEntityId">The entityId of the table</param>
static void DisableRecycleBinForTable(
    IOrganizationService service,
    Guid tableEntityId)
{

    QueryExpression query = new("recyclebinconfig")
    {
        ColumnSet = new ColumnSet("recyclebinconfigid")
    };

    LinkEntity entityLink = query.AddLink(
      "entity", 
      "extensionofrecordid", 
      "entityid");

    entityLink.LinkCriteria.AddCondition(
      "extensionofrecordid", 
      ConditionOperator.Equal, 
      tableEntityId);

    EntityCollection recyclebinconfigs = service.RetrieveMultiple(query);

    if (recyclebinconfigs.Entities.Count.Equals(1))
    {

        var id = recyclebinconfigs.Entities[0].GetAttributeValue<Guid>("recyclebinconfigid");

        Entity recyclebinconfig = new("recyclebinconfig", id)
        {
            Attributes = {
                { "statecode", new OptionSetValue(1) },
                { "statuscode", new OptionSetValue(2) }
            }
        };

        service.Update(recyclebinconfig);
    }
    else
    {
        string message = $"Recycle bin configuration for table '{extensionofrecordid}' not found.";
        throw new Exception(message);
    }
}
```

[Use the SDK for .NET](org-service/overview.md)


### [Web API](#tab/webapi)


Use this `Disable-RecycleBinForTable` PowerShell function to disable the recycle bin for a specific table. This function depends on the `Get-Records` and `Update-Record` functions described in [Create table operations functions](webapi/use-ps-and-vscode-web-api.md#create-table-operations-functions)


```powershell
function Disable-RecycleBinForTable {
   param(
      [Parameter(Mandatory)]
      [guid]$tableId
   )

   $query = "?`$filter=_extensionofrecordid_value eq "
   $query += $tableId
   $query += "&`$select=recyclebinconfigid"

   $recyclebinconfigs = (Get-Records `
         -setName 'recyclebinconfigs' `
         -query $query).value

   if ($recyclebinconfigs.Count -eq 1) {
      $recyclebinconfigId = $recyclebinconfigs[0].recyclebinconfigid

      Update-Record `
         -setName 'recyclebinconfigs' `
         -id $recyclebinconfigId `
         -body @{
         'statecode'  = 1
         'statuscode' = 2
      } | Out-Null
   }
   else {
      Write-Host "Recycle bin configuration for table $tableId not found."
   }
}
```

- [Use the Microsoft Dataverse Web API](webapi/overview.md)
- [Use PowerShell and Visual Studio Code with the Dataverse Web API](webapi/use-ps-and-vscode-web-api.md)
- [Update a table row](webapi/update-delete-entities-using-web-api.md#basic-update)

---

## Disable recycle bin for the environment

> [!NOTE]
> The preferred way to disable recycle bin for an environment is to [turn it off in the Power Platform admin center](/power-platform/admin/restore-deleted-table-records#enable-restore-table-records). The method described here may change before the feature becomes generally available.

Delete the row in the [RecycleBinConfig](reference/entities/recyclebinconfig.md) table where the `name` value is `"organization"`. This triggers deleting all the records in the `RecycleBinConfig` table and disable recycle bin for the environment.

> [!IMPORTANT]
> Don't try to delete other individual records. It is important that Dataverse manage this.

## Manage restoring records deleted by custom business logic

Dataverse provides a mechanism to manage desired actions for related records when a row is deleted. This configuration data is part of the definition of the relationship. When a related record is deleted, there are four possible behaviors that you can configure:

|Delete Behavior|Description|
|---------|---------|
|**Cascade All**|The related records are deleted.|
|**Remove Link**|The lookup columns to the deleted record are set to null.|
|**Cascade None**|No changes are applied to related records. (Internal Only) |
|**Restrict**|Dataverse prevents deleting the record to maintain data integrity. The record can't be deleted unless there are no records related for this relationship.|

[Learn more about relationship behaviors](../../maker/data-platform/create-edit-entity-relationships.md#behaviors)

There's nothing to do when the relationship is configured for **Cascade All**, **Remove Link**, and **Restrict** because Dataverse manages these behaviors.

If you have a relationship configured to use the **Remove Link** behavior, but this relationship is supposed to delete the related record, you might have custom logic that applies some custom behavior. For example, you might wish to respond to this behavior differently and implement your own *'Cascade some'* behavior based on rules you define. For example, you might delete inactive records or records that weren't updated in a certain period of time. This logic is usually implemented using a plug-in, but it could also be done using Power Automate with the [Microsoft Dataverse connector: When a row is added, modified or deleted trigger](/connectors/commondataserviceforapps/#when-a-row-is-added,-modified-or-deleted).

If you have this kind of custom business logic, then Dataverse doesn't know about it and can't automatically 'undo' your logic. However, you can register another plug-in on the `Restore` message to reverse whatever custom logic you have. Or you could use Power Automate and the [Microsoft Dataverse connector: When an action is performed trigger](/connectors/commondataserviceforapps/#when-an-action-is-performed).

> [!IMPORTANT]
> Be careful about the context when you register plug-in steps for the `Restore` message. The record being restored will not be available in the `PreOperation` stage. If related records need to be created, use the `PostOperation` stage. [Learn more about plug-in stages](event-framework.md#event-execution-pipeline).
>
> The [InputParameters](understand-the-data-context.md#inputparameters) and [OutputParameters](understand-the-data-context.md#outputparameters) of the `Restore` message are similar to `Create` message, so plug-ins written to be registered for the `Create` message can be re-used for the `Restore` message with fewer changes.

## Tables not currently supported for Recycle Bin

The query described in [Detect which tables don't have recycle bin enabled](#detect-which-tables-dont-have-recycle-bin-enabled) was used to generate [this list](/power-platform/admin/restore-deleted-table-records#tables-not-currently-supported-for-recycle-bin) in August of 2024.



### See also

[Restore deleted Microsoft Dataverse table records (preview)](/power-platform/admin/restore-deleted-table-records)
