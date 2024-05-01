---
title: Restore deleted records (preview)
description: Learn how to use configure tables to enable a recycle bin so that you can restore records deleted within a specified time period. 
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
# Restore deleted records (preview)

**TODO:Add your introduction here. Quickly establish the value proposition and why people should read more.**

In markdown, new paragraphs are separated by a new line.

Sometimes people delete records that they shouldn't. Administrators can configure a recycle bin for tables so that records deleted for that table can be restored within a specified period of time. **TODO: Add link to Admin guide article describing how administrators can do this.**

Developers can use Dataverse APIs to restore records using the `Restore` message. This message can only be used on tables that are configured to enable the recycle bin. This article will explain how to:

- Detect which tables have a recycle bin enabled
- Detect which tables do not have recycle bin enabled
- Enable a recycle bin for a table
- Retrieve deleted records that can be restored
- Restore a deleted record
- Manage restoring records deleted by cascade operations

## Detect which tables have a recycle bin enabled

Tables that are enabled for recycle bin will have a row in the [Recycle Bin Configuration (RecycleBinConfig)  table](reference/entities/recyclebinconfig.md) where the `statecode` is active. The `RecycleBinConfig` table doesn't contain the name of the table, but refers to a row in the [Entity table](reference/entities/entity.md) where the `logicalname` contains the [LogicalName](/dotnet/api/microsoft.xrm.sdk.metadata.entitymetadata.logicalname) of the table.

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
               value: 0)
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
   $query += '$filter=statecode eq 0'

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
It returns the all the public tables not returned by the `Get-RecycleBinEnabledTableNames` method, and depends on that method. 

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
It returns the all the public tables not returned by the `Get-RecycleBinEnabledTableNames` PowerShell function, and depends on that function. 

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

## Enable a recycle bin for a table

 **TODO: Explain how to do this**

 **TODO: Provide code snippets for both SDK and Web API**

 ### [SDK for .NET](#tab/sdk)

Content for SDK...

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

## Retrieve deleted records that can be restored

 **TODO: Explain how to do this**

 **TODO: Provide code snippets for both SDK and Web API**

 ### [SDK for .NET](#tab/sdk)

Content for SDK...

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

## Restore a deleted record

 **TODO: Explain how to do this**

 ### [SDK for .NET](#tab/sdk)

Content for SDK...

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

 **TODO: Provide code snippets for both SDK and Web API**

## Manage restoring records deleted by cascade operations

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

You can add links to headings of other sections of the same document: [Detect which tables have a recycle bin enabled](#detect-which-tables-have-a-recycle-bin-enabled)

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



