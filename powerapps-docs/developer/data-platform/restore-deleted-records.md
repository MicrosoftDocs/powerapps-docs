---
title: Restore deleted records with code(preview)
description: Learn how to configure tables to enable a recycle bin so that you can restore records deleted within a specified time period. 
ms.date: 04/30/2024
author: adkuppa
ms.author: adkuppa
ms.reviewer: jdaly
ms.topic: how-to
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
contributors:
 - JimDaly
 - TakeN0
ms.custom: bap-template
---
# Restore deleted records with code(preview)

[!INCLUDE [preview-include](../../cards/includes/preview-include.md)]

Sometimes people delete records that they shouldn't. Administrators can enable a recycle bin for tables so that they can restore deleted records within a specified period of time. [Learn how administrators can restore deleted records](/power-platform/admin/restore-deleted-table-records)

[When the recycle bin is enabled](/power-platform/admin/restore-deleted-table-records#enable-restore-table-records), developers can use the `Restore` message to restore deleted record before the specified period of time. The period of time can be up to 30 days.

This article will describe how you can do the following:

- Detect which tables are enabled for recycle bin
- Detect which tables do not have recycle bin enabled
- Retrieve the automatic cleanup time period configuration for the recycle bin
- Disable recycle bin for a table
- Retrieve deleted records that can be restored
- Restore a deleted record
- Manage restoring records deleted by cascade operations

## Detect which tables are enabled for recycle bin

Before the recycle bin feature is enabled, the [Recycle Bin Configuration (RecycleBinConfig) table](reference/entities/recyclebinconfig.md) will have no rows.

In time, we expect that all tables will be available to use the recycle bin feature. During this preview, some tables do not. For a list of tables that do not support recycle bin, see [Tables not currently supported for Recycle Bin](#tables-not-currently-supported-for-recycle-bin). Even after the preview, you can [disable recycle bin for specific tables](#disable-recycle-bin-for-a-table). In this case, you need to have a query to detect whether a table is enabled or not.

Tables that are enabled for recycle bin will have a row in the `RecycleBinConfig` where the `statecode` is active and `isreadyforrecyclebin` is true. The `RecycleBinConfig` table doesn't contain the name of the table, but refers to a row in the [Entity table](reference/entities/entity.md) where the `logicalname` contains the [LogicalName](/dotnet/api/microsoft.xrm.sdk.metadata.entitymetadata.logicalname) of the table.

### [SDK for .NET](#tab/sdk)

The following static `GetRecycleBinEnabledTables` method returns the `LogicalName` values for tables enabled for recycle bin.

```csharp
/// <summary>
/// Gets a list of LogicalNames for the tables enabled for RecycleBin
/// </summary>
/// <param name="service">The authenticated IOrganizationService instance</param>
/// <returns></returns>
static List<string> GetRecycleBinEnabledTables(IOrganizationService service)
{
    QueryExpression query = new("recyclebinconfig")
    {
        ColumnSet = new ColumnSet("recyclebinconfigid"),
        Criteria = new FilterExpression(LogicalOperator.And)
        {
            Conditions = {
                  {
               new ConditionExpression(
                 attributeName: "statecode",
                 conditionOperator: ConditionOperator.Equal,
                 value: 0),
               new ConditionExpression(
                 attributeName: "isreadyforrecyclebin",
                 conditionOperator: ConditionOperator.Equal,
                 value: true)
                  }
             }
        }
    };

    LinkEntity entityLink = query.AddLink(
        linkToEntityName: "entity",
        linkFromAttributeName: "extensionofrecordid",
        linkToAttributeName: "entityid");
    entityLink.Columns = new ColumnSet("logicalname");
    entityLink.EntityAlias = "entity";

    EntityCollection queryResults = service.RetrieveMultiple(query);

    List<string> tableNames = new();

    foreach (Entity recyclebinConfig in queryResults.Entities)
    {
        string logicalName = (string)recyclebinConfig
               .GetAttributeValue<AliasedValue>("entity.logicalname")
               .Value;

        tableNames.Add(logicalName);
    }

    tableNames.Sort();
    return tableNames;
}
```

- [Learn how to use the SDK for .NET](org-service/overview.md)
- [Build queries with QueryExpression](org-service/build-queries-with-queryexpression.md)


### [Web API](#tab/webapi)

The following `Get-RecycleBinEnabledTableNames` PowerShell function returns the `LogicalName` values for tables enabled for recycle bin.

> [!NOTE]
> This function depends on the `$environmentUrl` and `$baseHeaders` set as described in [Quick Start Web API with PowerShell and Visual Studio Code](webapi/quick-start-ps.md)

```powershell
function Get-RecycleBinEnabledTableNames {

   $query = 'api/data/v9.2/recyclebinconfigs?'
   $query += '$select=recyclebinconfigid&'
   $query += '$expand=extensionofrecordid($select=logicalname)&'
   $query += '$filter=statecode eq 0 and isreadyforrecyclebin eq true'

   $activeRecyclebinconfigsNames = (Invoke-RestMethod `
         -Uri ($environmentUrl + $query) `
         -Method Get `
         -Headers $baseHeaders).value

   $tableNames = @()
   $activeRecyclebinconfigsNames 
   | Sort-Object -Property { $_.extensionofrecordid.logicalname }
   | ForEach-Object {
      $tableNames += $_.extensionofrecordid.logicalname
   }

   return $tableNames
}
```

- [Learn to use the Dataverse Web API](webapi/overview.md)
- [Learn to use PowerShell and Visual Studio Code with the Dataverse Web API](webapi/use-ps-and-vscode-web-api.md)

---

## Detect which tables do not have recycle bin enabled

To know which tables can be enabled for recycle bin, you need to exclude all tables already enabled.

 ### [SDK for .NET](#tab/sdk)

This static `GetTablesEligibleForRecycleBin` method returns tables that are eligible to have recycle bin enabled.
It returns the all the public tables not returned by the `GetRecycleBinEnabledTables` method mentioned in [Detect which tables are enabled for recycle bin](#detect-which-tables-are-enabled-for-recycle-bin), and depends on that method.

```csharp
/// <summary>
/// Returns the logical names of tables not yet enabled for RecycleBin
/// </summary>
/// <param name="service">The authenticated IOrganizationService instance</param>
/// <returns>List of table logical names</returns>
static List<string> GetTablesEligibleForRecycleBin(IOrganizationService service)
{

    List<string> tablesEnabledForRecycleBin = GetRecycleBinEnabledTables(service);

    EntityQueryExpression query = new()
    {
        Properties = new MetadataPropertiesExpression("LogicalName"),
        Criteria = new MetadataFilterExpression(LogicalOperator.And)
        {
            Conditions = {
                 {
                     new MetadataConditionExpression(
                         propertyName:"LogicalName",
                         conditionOperator: MetadataConditionOperator.NotIn,
                         value: tablesEnabledForRecycleBin.ToArray() )
                 },
                                        {
                     new MetadataConditionExpression(
                         propertyName:"IsPrivate",
                         conditionOperator: MetadataConditionOperator.Equals,
                         value: false )
                 }

             }
        }
    };

    RetrieveMetadataChangesRequest request = new() { Query = query };
    var response = (RetrieveMetadataChangesResponse)service.Execute(request);

    List<string> tableNames = new();

    foreach (EntityMetadata entity in response.EntityMetadata)
    {
        tableNames.Add(entity.LogicalName);
    }

    tableNames.Sort();
    return tableNames;
}

```

- [Learn how to use the SDK for .NET](org-service/overview.md)
- [Learn to query table definitions](query-schema-definitions.md)


### [Web API](#tab/webapi)

This `Get-TablesEligibleForRecycleBin` PowerShell function returns tables that are eligible to have recycle bin enabled.

It returns the all the public tables not returned by the `Get-RecycleBinEnabledTableNames` PowerShell function mentioned in [Detect which tables are enabled for recycle bin](#detect-which-tables-are-enabled-for-recycle-bin), and depends on that function.

This function also depends on the `$environmentUrl` and `$baseHeaders` set as described in [Quick Start Web API with PowerShell and Visual Studio Code](webapi/quick-start-ps.md)

```powershell
function Get-TablesEligibleForRecycleBin {

   $tablesEnabledForRecycleBin = Get-RecycleBinEnabledTableNames

   $metadataQuery = [ordered]@{
      Properties = [ordered]@{
         AllProperties = $false.ToString()
         PropertyNames = @('LogicalName')
      }
      Criteria   = [ordered]@{
         FilterOperator = 'And'
         Conditions     = @(
            [ordered]@{
               ConditionOperator = 'NotIn'
               PropertyName      = 'LogicalName'
               Value             = [ordered]@{
                  Type  = 'System.String[]'
                  Value = "['$($tablesEnabledForRecycleBin -join ''',''')']"
               }
            }
            [ordered]@{
               ConditionOperator = 'Equals'
               PropertyName      = 'IsPrivate'
               Value             = [ordered]@{
                  Type  = 'System.Boolean'
                  Value = $false.ToString()
               }
            }
         )
      }
   }
   
   $metadataQueryJSON = $metadataQuery | ConvertTo-Json -Depth 10
   $requestQuery = 'api/data/v9.2/RetrieveMetadataChanges(Query=@p1)?@p1='
   $requestQuery += [System.Web.HttpUtility]::UrlEncode($metadataQueryJSON)
   $request = @{
      Method  = 'GET'
      Uri     = ($environmentUrl + $requestQuery)
      Headers = $baseHeaders
   }
   
   $response = Invoke-RestMethod @request
   $tableNames = $response.EntityMetadata | 
   Sort-Object -Property LogicalName | 
   Select-Object -ExpandProperty LogicalName
   
   return $tableNames
}
```

- [Learn to use the Dataverse Web API](webapi/overview.md)
- [Learn to query table definitions](query-schema-definitions.md)
- [Learn to use PowerShell and Visual Studio Code with the Dataverse Web API](webapi/use-ps-and-vscode-web-api.md)

---

## Retrieve and set the automatic cleanup time period configuration for the recycle bin

The value to determine how long deleted records will be available to be restored is set in the `RecycleBinConfig` `cleanupintervalindays` column where the `name` is `organization`. Every other row in the `RecycleBinConfig` table has a `cleanupintervalindays` column value of -1. This indicates it will use the same values set for the `organization` table.

To specify a different value for another table, set the `cleanupintervalindays` column value where the `name` matches the logical name of the table. While this column allows values up to 2,147,483,647, we recommend not setting it higher than 30.

 ### [SDK for .NET](#tab/sdk)

You can use this static `SetCleanupIntervalInDays` method to set the `cleanupintervalindays` column value for a specific table.

```csharp
/// <summary>
/// Updates the CleanupIntervalInDays value for a specified table
/// </summary>
/// <param name="service">The authenticated IOrganizationService instance</param>
/// <param name="tableLogicalName">The logical name of the table</param>
/// <param name="cleanupIntervalInDays">The new CleanupIntervalInDays value</param>
static void SetCleanupIntervalInDays(
    IOrganizationService service,
    string tableLogicalName,
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
                      attributeName: "name",
                      conditionOperator: ConditionOperator.Equal,
                      value: tableLogicalName)
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

This `Set-CleanupIntervalInDays` PowerShell function retrieves the `recyclebinconfig` row that has the name value that matches the `$tableLogicalName` parameter. Then it updates the `cleanupintervalindays` column  property of the record to the value of the `$cleanupIntervalInDays` parameter.

This function depends on the `Get-Records` and `Update-Record` functions described in [Create table operations functions](webapi/use-ps-and-vscode-web-api.md#create-table-operations-functions).

```powershell
function Set-CleanupIntervalInDays{
      param(
         [Parameter(Mandatory)]
         [string]$tableLogicalName,
         [Parameter(Mandatory)]
         [int]$cleanupIntervalInDays
      )
      $records = (Get-Records `
         -setName 'recyclebinconfigs' `
         -query "?`$filter=name eq '$($tableLogicalName)'").value
   
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
         Write-Host "Recycle bin configuration for table $tableLogicalName not found."
      }
}
```

- [Use the Microsoft Dataverse Web API](webapi/overview.md)
- [Quick Start Web API with PowerShell and Visual Studio Code](webapi/quick-start-ps.md)
- [Use PowerShell and Visual Studio Code with the Dataverse Web API](webapi/use-ps-and-vscode-web-api.md)

---

## Disable recycle bin for a table

To disable the recycle bin for a table, disable the `recyclebinconfig` record for the table by setting the [statecode](reference/entities/recyclebinconfig.md#BKMK_statecode) and [statuscode](reference/entities/recyclebinconfig.md#BKMK_statuscode) properties to their **Inactive** values, 2 and 1 respectively.

### [SDK for .NET](#tab/sdk)

Use this static `DisableRecycleBinForTable` method to disable the recycle bin for a specific table.

```csharp
/// <summary>
/// Disable the Recycle bin for a specified table
/// </summary>
/// <param name="service">The authenticated IOrganizationService instance</param>
/// <param name="tableLogicalName">The logical name of the table</param>
static void DisableRecycleBinForTable(
    IOrganizationService service,
    string tableLogicalName)
{

    QueryExpression query = new("recyclebinconfig")
    {
        ColumnSet = new ColumnSet("recyclebinconfigid")
    };
    LinkEntity entityLink = query.AddLink("entity", "extensionofrecordid", "entityid");
    entityLink.LinkCriteria.AddCondition("name", ConditionOperator.Equal, tableLogicalName);

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
        string message = $"Recycle bin configuration for table '{tableLogicalName}' not found.";
        throw new Exception(message);
    }
}
```

[Use the SDK for .NET](org-service/overview.md)


### [Web API](#tab/webapi)


Use this `Disable-RecycleBinForTable` PowerShell function to disable the recycle bin for a specific table.  This function depends on the `Get-Records` and `Update-Record` functions described in [Create table operations functions](webapi/use-ps-and-vscode-web-api.md#create-table-operations-functions)


```powershell
function Disable-RecycleBinForTable {
   param(
      [Parameter(Mandatory)]
      [string]$tableLogicalName
   )

   $query = "?`$filter=extensionofrecordid/name eq '"
   $query += $tableLogicalName
   $query += "'&`$select=recyclebinconfigid"

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
      Write-Host "Recycle bin configuration for table '$tableLogicalName' not found."
   }
}
```

- [Use the Microsoft Dataverse Web API](webapi/overview.md)
- [Use PowerShell and Visual Studio Code with the Dataverse Web API](webapi/use-ps-and-vscode-web-api.md)
- [Update a table row](webapi/update-delete-entities-using-web-api.md#basic-update)

---

## Retrieve deleted records that can be restored

To retrieve deleted records that can be restored, select the datasource of the query to '`bin`'.
The examples below return the top 3 deleted account records.

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
> Currently, you can only retrieve deleted records using FetchXml.

```powershell
function Get-DeletedAccountRecords{

   $query = @()
   $query += "<fetch top='3' datasource='bin'>"
   $query += "<entity name='account'>"
   $query += "<attribute name='name' />"
   $query += "</entity>"
   $query += "</fetch>"

   $uri = $baseURI
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

 **TODO: Explain how to do this**

 ### [SDK for .NET](#tab/sdk)

Content for SDK...


This is the class generated using the [pac modelbuilder](/power-platform/developer/cli/reference/modelbuilder) for the Restore Message:

**TODO: We don't want to include this class in the docs, we want to show how to use it. It has an unusual signature. We should also show how to use OrganizationRequest/OrganizationResponse without this generated class**

```csharp
   [System.Runtime.Serialization.DataContractAttribute(Namespace="http://schemas.microsoft.com/crm/2011/Contracts")]
   [Microsoft.Xrm.Sdk.Client.RequestProxyAttribute("Restore")]
   public partial class RestoreRequest<T> : Microsoft.Xrm.Sdk.OrganizationRequest
      where T : Microsoft.Xrm.Sdk.Entity, new ()
   {
      
      public bool MaintainLegacyAppServerBehavior
      {
         get
         {
            if (this.Parameters.Contains("MaintainLegacyAppServerBehavior"))
            {
               return ((bool)(this.Parameters["MaintainLegacyAppServerBehavior"]));
            }
            else
            {
               return default(bool);
            }
         }
         set
         {
            this.Parameters["MaintainLegacyAppServerBehavior"] = value;
         }
      }
      
      public bool CalculateMatchCodeSynchronously
      {
         get
         {
            if (this.Parameters.Contains("CalculateMatchCodeSynchronously"))
            {
               return ((bool)(this.Parameters["CalculateMatchCodeSynchronously"]));
            }
            else
            {
               return default(bool);
            }
         }
         set
         {
            this.Parameters["CalculateMatchCodeSynchronously"] = value;
         }
      }
      
      public RestoreRequest() : 
            this(new T())
      {
      }
      
      public RestoreRequest(T target)
      {
         this.Target = target;
         this.RequestName = "Restore";
      }
      
      public T Target
      {
         get
         {
            if (this.Parameters.Contains("Target"))
            {
               return ((T)(this.Parameters["Target"]));
            }
            else
            {
               return default(T);
            }
         }
         set
         {
            this.Parameters["Target"] = value;
         }
      }
      
      public bool SuppressDuplicateDetection
      {
         get
         {
            if (this.Parameters.Contains("SuppressDuplicateDetection"))
            {
               return ((bool)(this.Parameters["SuppressDuplicateDetection"]));
            }
            else
            {
               return default(bool);
            }
         }
         set
         {
            this.Parameters["SuppressDuplicateDetection"] = value;
         }
      }
      
      public bool ReturnRowVersion
      {
         get
         {
            if (this.Parameters.Contains("ReturnRowVersion"))
            {
               return ((bool)(this.Parameters["ReturnRowVersion"]));
            }
            else
            {
               return default(bool);
            }
         }
         set
         {
            this.Parameters["ReturnRowVersion"] = value;
         }
      }
      
      public string SolutionUniqueName
      {
         get
         {
            if (this.Parameters.Contains("SolutionUniqueName"))
            {
               return ((string)(this.Parameters["SolutionUniqueName"]));
            }
            else
            {
               return default(string);
            }
         }
         set
         {
            this.Parameters["SolutionUniqueName"] = value;
         }
      }
   }
   
   [System.Runtime.Serialization.DataContractAttribute(Namespace="http://schemas.microsoft.com/crm/2011/Contracts")]
   [Microsoft.Xrm.Sdk.Client.ResponseProxyAttribute("Restore")]
   public partial class RestoreResponse : Microsoft.Xrm.Sdk.OrganizationResponse
   {
      
      public RestoreResponse()
      {
      }
      
      public System.Guid id
      {
         get
         {
            if (this.Results.Contains("id"))
            {
               return ((System.Guid)(this.Results["id"]));
            }
            else
            {
               return default(System.Guid);
            }
         }
      }
   }
}
```

I was expecting that it would simply require an EntityReference...

```csharp
static void ExampleMethod(IOrganizationService service){

   // Add your code to demonstrate how to do something here
   // We want a static method where all input parameters
   // are visible
}
```


### [Web API](#tab/webapi)

Content for Web API...

**Request**

```http
POST [Organization Uri]/api/data/v9.2/sample_examples/Microsoft.Dynamics.CRM.CreateMultiple
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
Content-Type: application/json; charset=utf-8
Content-Length: 396

{
    "Targets": [
        {
            "sample_name": "sample record 0000001",
            "@odata.type": "Microsoft.Dynamics.CRM.sample_example"
        },
        {
            "sample_name": "sample record 0000002",
            "@odata.type": "Microsoft.Dynamics.CRM.sample_example"
        },
        {
            "sample_name": "sample record 0000003",
            "@odata.type": "Microsoft.Dynamics.CRM.sample_example"
        }
    ]
}
```

**Response**

```http
HTTP/1.1 200 OK
OData-Version: 4.0

{
    "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.CreateMultipleResponse",
    "Ids": [
        "8f4c3f92-312b-ee11-bdf4-000d3a993550",
        "904c3f92-312b-ee11-bdf4-000d3a993550",
        "914c3f92-312b-ee11-bdf4-000d3a993550"
    ]
}
```

---

### Errors that may occur when restoring records

> Name: `RefCannotBeRestoredRecycleBinNotFound`<br />
> Code: `0x80049959`<br />
> Number: `-2147182247`<br />
> Message: `Entity with id '<GuidValue>' and logical name '<EntityLogicalName>' does not exist. We cannot restore the reference '<ReferredAPrimaryKeyName>' that must be restored as part of this Restore call. ValueToBeRestored: <GuidValue>, ReferencedEntityName: <ReferencedEntityName>, AttributeName: <ReferredAttributeName>`

> Name: `DuplicateExceptionRestoreRecycleBin`<br />
> Code: `0x80044a02`<br />
> Number: `-2147182279`<br />
> Message: `Please delete the existing conflicting record '<EntityPlatformName>' with primary key '<PrimaryKeyName>' and primary key value '<PrimaryKeyValue>' before attempting restore.`

> Name: `DuplicateExceptionEntityKeyRestoreRecycleBin`<br />
> Code: `0x80049929`<br />
> Number: `-2147182295`<br />
> Message: `Duplicate entity key preventing restore of record '<EntityPlatformName>' with primary key '<PrimaryKeyName>' and primary key value '<PrimaryKeyValue>'. See inner exception for entity key details.`


> Name: `PicklistValueOutOfRangeRecycleBin`<br />
> Code: `0x80049949`<br />
> Number: `-2147182263`<br />
> Message: `Picklist value not valid, please add the invalid value back to the picklist before restoring record`


#### Primary Key Violation on Delete

If the record with same primary key was already deleted before, copy to Recycle Bin is ignored for the record. To enforce all deleted items are stored in Recycle Bin, you can set the `DoNotEnforcePrimaryKeyOrgSettingRecycleBin` setting using the [OrgDBOrgSettings tool for Microsoft Dynamics CRM](/power-platform/admin/environment-database-settings). 

After enabling this, you may receive the following error:

> Name: `DuplicateExceptionRestoreRecycleBin`<br />
> Code: `0x80049939 `<br />
> Number: `-2147182279`<br />
> Message: `A record that has the attribute values Deleted Object already exists on Delete.`


## Manage restoring records deleted by custom business logic

 **TODO: Explain the scenarios**

- Why this is necessary?
- When to do this?
- What to do
- Where to do this (i.e. is a plug-in the only way to do this?)


### Plug-in code example

```csharp
 public class IsSystemAdmin : IPlugin
{
   public void Execute(IServiceProvider serviceProvider)
   {
      // Obtain the tracing service
      ITracingService tracingService =
      (ITracingService)serviceProvider.GetService(typeof(ITracingService));

      // Obtain the execution context from the service provider.  
      IPluginExecutionContext context = (IPluginExecutionContext)
            serviceProvider.GetService(typeof(IPluginExecutionContext));

      if (context.InputParameters.Contains("Target") &&
            context.InputParameters["Target"] is EntityReference)
      {

            // Obtain the organization service reference which you will need for  
            // web service calls.  
            IOrganizationServiceFactory serviceFactory =
               (IOrganizationServiceFactory)serviceProvider.GetService(typeof(IOrganizationServiceFactory));
            IOrganizationService service = serviceFactory.CreateOrganizationService(context.UserId);

            try
            {
               //Get the userid 
               Guid userid = ((EntityReference)context.InputParameters["Target"]).Id;

               string systemUserRolesFetchXml = $@"<fetch mapping='logical' >
                  <entity name='systemuserroles'>
                  <attribute name='roleid'/>
                  <filter type='and'>
                     <condition attribute='systemuserid' operator='eq' value='{{0}}' /> 
                  </filter>
                  <link-entity name='role' alias='role' to='roleid' link-type='inner'>
                     <filter type='and'>
                        <condition alias='role' attribute='roletemplateid' operator='eq' value='627090FF-40A3-4053-8790-584EDC5BE201' /> </filter>
                  </link-entity>
                  </entity>
               </fetch>";

               FetchExpression systemuserrolesQuery = new FetchExpression(string.Format(systemUserRolesFetchXml, userid));

               EntityCollection systemuserrolesResults = service.RetrieveMultiple(systemuserrolesQuery);

               if (systemuserrolesResults.Entities.Count > 0)
               {
                  context.OutputParameters["HasRole"] = true;
               }
               else
               {
                  tracingService.Trace("System Administrator Role not found in systemuserroles");

                  //The user may have the role due to an indirect association from team membership.

                  string teamMemberShipFetchXml = $@"<fetch mapping='logical' >
                     <entity name='teamroles'>
                        <attribute name='roleid'/>
                        <link-entity name='teammembership' to='teamid' from='teamid' link-type='inner'>
                        <filter type='and'>
                           <condition attribute='systemuserid' operator='eq' value='{{0}}' />
                        </filter>
                        </link-entity>
                        <link-entity name='role' alias='role' to='roleid' from='roleid' link-type='inner'>
                        <filter type='and'>
                           <condition alias='role' attribute='roletemplateid' operator='eq' value='627090FF-40A3-4053-8790-584EDC5BE201' />
                        </filter>
                        </link-entity>
                     </entity>
                  </fetch>";

                  FetchExpression teammembershipQuery = new FetchExpression(string.Format(systemUserRolesFetchXml, userid));

                  EntityCollection teammembershipResults = service.RetrieveMultiple(systemuserrolesQuery);
                  if (systemuserrolesResults.Entities.Count > 0)
                  {
                        context.OutputParameters["HasRole"] = true;
                  }
                  else
                  {
                        tracingService.Trace("System Administrator Role not found in teamroles");
                        context.OutputParameters["HasRole"] = false;
                  }

               }

            }
            catch (FaultException<OrganizationServiceFault> ex)
            {
               throw new InvalidPluginExecutionException("An error occurred in IsSystemAdmin.", ex);
            }

            catch (Exception ex)
            {
               tracingService.Trace("IsSystemAdmin: {0}", ex.ToString());
               throw;
            }

      }
   }
}
```


### Scenario 1 TBD

 **TODO: If you have multiple scenarios, please create new sections for them.**


### Scenario 3 TBD

 **TODO: If you have multiple scenarios, please create new sections for them.**


## Tables not currently supported for Recycle Bin

:::row:::
   :::column:::
      `aaduser`<br />
      `aicopilot`<br />
      `aiplugin`<br />
      `aipluginconversationstartermapping`<br />
      `aipluginexternalschemaproperty`<br />
      `aipluginoperation`<br />
      `aipluginoperationresponsetemplate`<br />
      `annualfiscalcalendar`<br />
      `appaction_appactionrule_classicrules`<br />
      `appactionrule`<br />
      `appconfig`<br />
      `application`<br />
      `applicationuser`<br />
      `applicationuserrole`<br />
      `appmodulecomponent`<br />
      `appnotification`<br />
      `asyncoperation`<br />
      `attributeimageconfig`<br />
      `backgroundoperation`<br />
      `bot_botcomponent`<br />
      `bot_environmentvariabledefinition`<br />
      `botcomponent_aipluginoperation`<br />
      `botcomponent_connectionreference`<br />
      `botcomponent_environmentvariabledefinition`<br />
      `botcomponent_workflow`<br />
      `bulkdeletefailure`<br />
      `businessunit`<br />
      `callbackregistration`<br />
      `card`<br />
      `cardstateitem`<br />
      `catalogassignment`<br />
      `columnmapping`<br />
      `componentversion`<br />
      `componentversionnrddatasource`<br />
      `connectionreference`<br />
      `connectionroleassociation`<br />
      `copilotexamplequestion`<br />
      `copilotsynonyms`<br />
      `customapi`<br />
      `customapiresponseproperty`<br />
      `customcontroldefaultconfig`<br />
      `datalakefolder`<br />
      `datalakeworkspace`<br />
      `dataprocessingconfiguration`<br />
      `desktopflowbinary`<br />
      `displaystring`<br />
      `duplicaterulecondition`<br />
      `dvfilesearchattribute`<br />
      `dvtablesearch`<br />
      `dvtablesearchentity`<br />
      `entity`<br />
      `entitydataprovider`<br />
      `entityindex`<br />
      `entityrecordfilter`<br />
      `environmentvariabledefinition`<br />
      `eventexpanderbreadcrumb`<br />
      `expiredprocess`<br />
      `fabricaiskill`<br />
      `fieldpermission`<br />
      `fixedmonthlyfiscalcalendar`<br />
      `flowlog`<br />
      `flowmachinegroup`<br />
      `flowmachineimageversion`<br />
      `flowrun`<br />
      `goal`<br />
      `importentitymapping`<br />
      `importjob`<br />
      `importmap`<br />
      `interactionforemail`<br />
      `kbarticletemplate`<br />
      `lookupmapping`<br />
      `mainfewshot`<br />
      `managedproperty`<br />
      `metadataforarchival`<br />
      `mobileofflineprofileitem`<br />
      `mobileofflineprofileitemfilter`<br />
      `msdyn_aiconfiguration`<br />
      `msdyn_aitemplate`<br />
      `msdyn_componentlayer`<br />
      `msdyn_connectordatasource`<br />
      `msdyn_dataflow_datalakefolder`<br />
      `msdyn_dataflowtemplate`<br />
      `msdyn_dmsrequest`<br />
      `msdyn_entitylinkchatconfiguration`<br />
      `msdyn_insightsstorevirtualentity`<br />
      `msdyn_knowledgemanagementsetting`<br />
      `msdyn_mobileapp`<br />
      `msdyn_nonrelationalds`<br />
      `msdyn_pmanalysishistory`<br />
      `msdyn_pmcalendar`<br />
      `msdyn_pminferredtask`<br />
      `msdyn_pmprocesstemplate`<br />
      `msdyn_pmprocessversion`<br />
      `msdyn_pmtemplate`<br />
      `msdyn_salesforcestructuredobject`<br />
      `msdyn_schedule`<br />
      `msdyn_solutioncomponentcountdatasource`<br />
      `msdyn_solutioncomponentdatasource`<br />
      `msdyn_solutionhistory`<br />
      `msdyn_timelinepin`<br />
      `msdyn_workflowactionstatus`<br />
      `mspp_columnpermission`<br />
      `mspp_contentsnippet`<br />
      `mspp_entityformmetadata`<br />
      `mspp_entitypermission`<br />
      `mspp_pollplacement`<br />
      `mspp_publishingstate`<br />
      `mspp_redirect`<br />
      `mspp_sitemarker`<br />
      `mspp_webfile`<br />
      `mspp_webformmetadata`<br />
      `mspp_weblink`<br />
      `mspp_webpage`<br />
      `mspp_webrole`<br />
      `mspp_websiteaccess`<br />
      `mspp_webtemplate`<br />
      `newprocess`<br />
      `optionset`<br />
      `picklistmapping`<br />
      `pluginpackage`<br />
      `plugintype`<br />
      `powerbidataset`<br />
      `powerbireport`<br />
      `powerpagecomponent`<br />
      `powerpagesite`<br />
      `powerpageslog`<br />
      `principalentitymap`<br />
      `privilegesremovalsetting`<br />
      `processtrigger`<br />
      `publisheraddress`<br />
      `queue`<br />
      `recentlyused`<br />
      `recurringappointmentmaster`<br />
      `relationship`<br />
      `report`<br />
      `retaineddataexcel`<br />
      `ribbonmetadatatoprocess`<br />
      `roleeditorlayout`<br />
      `roletemplate`<br />
      `runtimedependency`<br />
      `savedqueryvisualization`<br />
      `sdkmessagefilter`<br />
      `sdkmessageprocessingstepimage`<br />
      `searchtelemetry`<br />
      `serviceendpoint`<br />
      `serviceplanappmodules`<br />
      `serviceplanmapping`<br />
      `sharedworkspaceaccesstoken`<br />
      `sharepointsite`<br />
      `sitemap`<br />
      `slaitem`<br />
      `solutioncomponent`<br />
      `solutioncomponentbatchconfiguration`<br />
      `solutioncomponentrelationshipconfiguration`<br />
      `subscriptionstatisticsoffline`<br />
      `synapsedatabase`<br />
      `synapselinkprofileentity`<br />
      `syncerror`<br />
      `systemuser`<br />
      `systemuserprofiles`<br />
      `teammobileofflineprofilemembership`<br />
      `teamroles`<br />
      `template`<br />
      `tracelog`<br />
      `transformationparametermapping`<br />
      `userform`<br />
      `userquery`<br />
      `virtualentitymetadata`<br />
      `webwizard`<br />
      `workflowbinary`<br />
      `workflowlog`<br />
      `workqueueitem`<br />
   :::column-end:::
   :::column:::
      `activityfileattachment`<br />
      `aicopilot_aiplugin`<br />
      `aipluginconversationstarter`<br />
      `aipluginexternalschema`<br />
      `aiplugininstance`<br />
      `aipluginoperationparameter`<br />
      `aiplugintitle`<br />
      `appaction`<br />
      `appactionmigration`<br />
      `appactionrule_webresource_scripts`<br />
      `appconfiginstance`<br />
      `applicationroles`<br />
      `applicationuserprofile`<br />
      `appmodule`<br />
      `appmoduleroles`<br />
      `appointment`<br />
      `attribute`<br />
      `attributemaskingrule`<br />
      `bot`<br />
      `bot_botcomponentcollection`<br />
      `botcomponent`<br />
      `botcomponent_botcomponent`<br />
      `botcomponent_dvtablesearch`<br />
      `botcomponent_msdyn_aimodel`<br />
      `botcomponentcollection`<br />
      `bulkdeleteoperation`<br />
      `calendar`<br />
      `canvasapp`<br />
      `cardentityconnections`<br />
      `catalog`<br />
      `channelaccessprofileentityaccesslevel`<br />
      `complexcontrol`<br />
      `componentversiondatasource`<br />
      `connectioninstance`<br />
      `connectionrole`<br />
      `connector`<br />
      `copilotglossaryterm`<br />
      `credential`<br />
      `customapirequestparameter`<br />
      `customcontrol`<br />
      `customcontrolresource`<br />
      `datalakefolderpermission`<br />
      `datalakeworkspacepermission`<br />
      `dependency`<br />
      `desktopflowmodule`<br />
      `duplicaterule`<br />
      `dvfilesearch`<br />
      `dvfilesearchentity`<br />
      `dvtablesearchattribute`<br />
      `elasticfileattachment`<br />
      `entityanalyticsconfig`<br />
      `entityimageconfig`<br />
      `entitykey`<br />
      `entityrelationship`<br />
      `environmentvariablevalue`<br />
      `exchangesyncidmapping`<br />
      `exportedexcel`<br />
      `featurecontrolsetting`<br />
      `fieldsecurityprofile`<br />
      `flowcredentialapplication`<br />
      `flowmachine`<br />
      `flowmachineimage`<br />
      `flowmachinenetwork`<br />
      `fxexpression`<br />
      `import`<br />
      `importfile`<br />
      `importlog`<br />
      `indexattributes`<br />
      `invaliddependency`<br />
      `keyvaultreference`<br />
      `mailmergetemplate`<br />
      `managedidentity`<br />
      `maskingrule`<br />
      `mobileofflineprofile`<br />
      `mobileofflineprofileitemassociation`<br />
      `monthlyfiscalcalendar`<br />
      `msdyn_aimodel`<br />
      `msdyn_appinsightsmetadata`<br />
      `msdyn_componentlayerdatasource`<br />
      `msdyn_dataflow`<br />
      `msdyn_dataflowconnectionreference`<br />
      `msdyn_datalakeds`<br />
      `msdyn_dmsrequeststatus`<br />
      `msdyn_helppage`<br />
      `msdyn_knowledgeassetconfiguration`<br />
      `msdyn_knowledgesearchfilter`<br />
      `msdyn_modulerundetail`<br />
      `msdyn_odatav4ds`<br />
      `msdyn_pmbusinessruleautomationconfig`<br />
      `msdyn_pmcalendarversion`<br />
      `msdyn_pmprocessextendedmetadataversion`<br />
      `msdyn_pmprocessusersettings`<br />
      `msdyn_pmrecording`<br />
      `msdyn_pmview`<br />
      `msdyn_salesforcestructuredqnaconfig`<br />
      `msdyn_slakpi`<br />
      `msdyn_solutioncomponentcountsummary`<br />
      `msdyn_solutioncomponentsummary`<br />
      `msdyn_solutionhistorydatasource`<br />
      `msdyn_tour`<br />
      `mspp_adplacement`<br />
      `mspp_columnpermissionprofile`<br />
      `mspp_entityform`<br />
      `mspp_entitylist`<br />
      `mspp_pagetemplate`<br />
      `mspp_powerpagescoreentityds`<br />
      `mspp_publishingstatetransitionrule`<br />
      `mspp_shortcut`<br />
      `mspp_sitesetting`<br />
      `mspp_webform`<br />
      `mspp_webformstep`<br />
      `mspp_weblinkset`<br />
      `mspp_webpageaccesscontrolrule`<br />
      `mspp_website`<br />
      `mspp_websitelanguage`<br />
      `navigationsetting`<br />
      `nlsqregistration`<br />
      `ownermapping`<br />
      `pluginassembly`<br />
      `plugintracelog`<br />
      `position`<br />
      `powerbimashupparameter`<br />
      `powerfxrule`<br />
      `powerpagecomponent_powerpagecomponent`<br />
      `powerpagesitelanguage`<br />
      `principalentitybusinessunitmap`<br />
      `privilege`<br />
      `processstage`<br />
      `publisher`<br />
      `quarterlyfiscalcalendar`<br />
      `queuemembership`<br />
      `recordfilter`<br />
      `recyclebinconfig`<br />
      `relationshipattribute`<br />
      `reportcategory`<br />
      `retentionconfig`<br />
      `role`<br />
      `roleprivileges`<br />
      `roletemplateprivileges`<br />
      `savedquery`<br />
      `sdkmessage`<br />
      `sdkmessageprocessingstep`<br />
      `searchresultscache`<br />
      `semiannualfiscalcalendar`<br />
      `serviceplan`<br />
      `serviceplancustomcontrol`<br />
      `sharedlinksetting`<br />
      `sharedworkspacenr`<br />
      `similarityrule`<br />
      `sla`<br />
      `solution`<br />
      `solutioncomponentattributeconfiguration`<br />
      `solutioncomponentconfiguration`<br />
      `solutionhistorydata`<br />
      `subscriptionsyncentryoffline`<br />
      `synapselinkprofile`<br />
      `synapselinkschedule`<br />
      `systemform`<br />
      `systemuserauthorizationchangetracker`<br />
      `systemuserroles`<br />
      `teamprofiles`<br />
      `teamtemplate`<br />
      `textanalyticsentitymapping`<br />
      `transformationmapping`<br />
      `translationprocess`<br />
      `usermobileofflineprofilemembership`<br />
      `userqueryvisualization`<br />
      `webresource`<br />
      `workflow`<br />
      `workflowcardconnections`<br />
      `workqueue`<br />
   :::column-end:::
:::row-end:::






## Markdown examples to delete when we are done

Each `##` section has a navigation link at the top of the page. Introduce key capabilities with a section. You may want to use this when you link between articles.

### Sub section

Each sub section provides a 'link-able' section of the doc. You may want to use this when you link between articles.

#### Sub-sub section

You can divide your sub sections with linkable headings. You shouldn't go deeper than `####` if you can avoid it.

## Tables

Please use markdown tables. HTML tables will render, but are not preferred. Try not to use more than three columns.


|Column1  |Column2  |Column3  |
|---------|---------|---------|
|Row1-1|Row2-1|Row2-1: When adding content to a row, all the content must be in a single line. <br /> If you need to add a break, use `<br />`.|
|Row1-2|Row2-2|Row2-2|
|Row1-3|Row2-3|Row2-3|
|Row1-4|Row2-4|Row2-4|
|Row1-5|Row2-5|Row2-5|

## Images

Put all your images in the media folder at the same level as the file.

:::image type="content" source="media/dev-resources-menu.png" alt-text="A screenshot of the developer resources menu in Power Apps.":::

## Code

When you include multiple lines of code, use this:

```csharp
// Hello world
```

If you use a word in a sentence to refer to a specific term that shouldn't be localized, surround it with backtick characters: `IObservable`.



## Links

There are several types of links you can use:

### Local links

You can link to other articles in the same repo with relative paths: [Search for Dataverse records](search/overview.md) , or [Update and delete table rows using the Web API](webapi/update-delete-entities-using-web-api.md), or [Update and delete table rows using the SDK for .NET](org-service/entity-operations-update-delete.md).

### Links to sections

You can add links to headings of other sections of the same document: [Detect which tables do not have recycle bin enabled](#detect-which-tables-do-not-have-recycle-bin-enabled)

You can link to headings of other sections of a different document: [DeleteMultiple Availability](deletemultiple.md#availability)

You can link to a section of another document on Microsoft Learn: [Power Platform CLI](/power-platform/developer/cli/introduction)

> [!NOTE]
> If you change the heading (or someone else changes the heading), the link will break. You (or they) will get a build warning when that happens.

### Other Microsoft Learn articles

You can link to other articles in different repos by removing `https://learn.microsoft.com/en-us` from the URL. For example: [Microsoft Power Platform developer documentation](/power-platform/developer/).

### Links to reference articles

If you want to link to a reference topic for a property, use this pattern: <xref:System.String.Length>, or [String.Length Property](xref:System.String.Length), or [String.IndexOf Method](xref:System.String.IndexOf%2A). After you have added one link, subsequent mentions can just use back ticks: `IndexOf` method.

The [Learn Authoring Pack](https://marketplace.visualstudio.com/items?itemName=docsmsft.docs-authoring-pack) provides a tool to make adding these easier when you are using a local clone of the repo.

> [!NOTE]
> I strongly recommend using VS Code with a local clone of the repo. Happy to give you a demo and help you get set up. [Learn more about using Visual Studio Code to work with our content](/bacx/make-major-changes?branch=main)

Different ways to link to a class name:

<!-- I prefer this  -->
- [RecalcEngine class](xref:Microsoft.PowerFx.RecalcEngine)
<!-- But these also work -->
- <xref:Microsoft.PowerFx.RecalcEngine>
- <xref:Microsoft.PowerFx.RecalcEngine?displayProperty=nameWithType>
- <xref:Microsoft.PowerFx.RecalcEngine?displayProperty=fullName>

## Numbering

With markdown, don't set explicit numbers. Always use `1` and markdown will order them for you.

1. First
1. Second
1. Third
1. Fourth

To add instructions within a list, add a new line and three characters:

1. First
   
   1. First One
   1. First Two
   1. First Three

1. Second
1. Third
   
   1. Third One
   1. Third Two
   1. Third Three

1. Fourth


## Alerts

There are several types of alerts you can use, but use them sparingly.

> [!NOTE]
> Information the user should notice even if skimming

> [!TIP]
> Optional information to help a user be more successful

> [!IMPORTANT]
> Essential information required for user success

> [!CAUTION]
> Negative potential consequences of an action

> [!WARNING]
> Dangerous certain consequences of an action



