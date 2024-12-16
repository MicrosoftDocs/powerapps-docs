---
title: Long-term data retention
description: Learn how to use retention policies to transfer data from your Microsoft Dataverse transactional database to a managed data lake for cost-efficient long-term storage.
ms.date: 12/12/2024
ms.topic: how-to
author: pnghub
ms.author: gned
ms.reviewer: pehecke
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
ms.custom: bap-template
---

# Long-term data retention

[Long-term data retention](../../maker/data-platform/data-retention-overview.md) automates the transfer of data from your Microsoft Dataverse transactional database to a managed data lake for cost-efficient archival storage. Start by [configuring tables for long-term retention](../../maker/data-platform/data-retention-set.md#enable-a-table-for-long-term-retention). Then, create retention policies that define the data to archive. Scheduled retention runs transfer rows that match the criteria.

> [!IMPORTANT]
> To use all long term data retention features you must meet both of the requirements described here: [Dataverse long term data retention overview](../../maker/data-platform/data-retention-overview.md#dataverse-long-term-data-retention-overview).


## Retrieve retained data

You can retrieve data that has been retained using FetchXml and [QueryExpression ](/dotnet/api/microsoft.xrm.sdk.query.queryexpression).

With FetchXml, set the [fetch element](fetchxml/reference/fetch.md) `datasource` attribute value to `"retained"`.

```xml
<fetch datasource="retained">
   <entity name="account">
      <attribute name="accountId" />
   </entity>
</fetch>
```

With [QueryExpression ](/dotnet/api/microsoft.xrm.sdk.query.queryexpression), set the [QueryExpression.DataSource property](/dotnet/api/microsoft.xrm.sdk.query.queryexpression.datasource) to `retained`.

> [!NOTE]
> There is currently no way to retrieve retained data using [Dataverse Web API](webapi/query/overview.md) using an OData style query. [You can use FetchXml with the Dataverse Web API](fetchxml/retrieve-data.md)
  
## Set up a retention policy

To create retention policies, use our APIs, the maker portal, or solution installation. The following code sample demonstrates the use of APIs to create a retention policy.

### [SDK for .NET](#tab/sdk)

The following code uses the [Organization service](org-service/overview.md) and the [IOrganizationService.Create(Entity) method](xref:Microsoft.Xrm.Sdk.IOrganizationService.Create%2A) to create a retention policy that retains all closed opportunities and runs yearly. Valid recurrence parameters are `DAILY`, `WEEKLY`, `MONTHLY`, and `YEARLY`. To run retention only once, set the recurrence value to empty.

```csharp
public void CreateRetentionConfig(IOrganizationService orgService)
{
    Entity retentionConfig = new Entity("retentionconfig");
    retentionConfig["retentionconfigid"] = Guid.NewGuid();
    retentionConfig["entitylogicalname"] = "incident";
    retentionConfig["name"] = "Retain all closed opportunities";
    retentionConfig["uniquename"] = "ui_RetainAllClosedOpportunities";
    retentionConfig["statecode"] = new OptionSetValue(0);
    retentionConfig["statuscode"] = new OptionSetValue(10);
    retentionConfig["criteria"] = "<fetch> " +
        "<entity name=\"opportunity\"> " +
            "<attribute name=\"name\" /> " +
            "<attribute name=\"statecode\" />" +
            "<attribute name=\"actualvalue\" />" +
            "<attribute name=\"actualclosedate\" />" +
            "<attribute name=\"customerid\" />" +
            "<attribute name=\"opportunityid\" />" +
            "<order attribute=\"actualclosedate\" descending=\"true\" />" +
            "<filter type=\"and\">" +
                "<filter type=\"or\">" +
                    "<condition attribute=\"statecode\" operator=\"eq\" value=\"1\" />" +
                    "<condition attribute=\"statecode\" operator=\"eq\" value=\"2\" />" +
                "</filter>" +
            "</filter>" +
        "</entity></fetch>";
    retentionConfig["starttime"] = DateTime.Parse("2024-05-01T00:00:00");
    retentionConfig["recurrence"] = "FREQ=YEARLY;INTERVAL=1";
    try
    {
        var retentionConfigId = orgService.Create(retentionConfig);
        Console.WriteLine($"Retention policy created with Id : {retentionConfigId}");
    }
    catch (Exception ex)
    {
        throw new Exception($"Create retention policy failed: {ex.Message})", ex);
    }
}
```

The output of this code is "Retention policy created with Id : c1a9e932-89f6-4f17-859c-bd2101683263".

### [Web API](#tab/webapi)

The following Web API example creates a retention policy that retains all closed opportunities and runs yearly. Valid recurrence parameters are `DAILY`, `WEEKLY`, `MONTHLY`, and `YEARLY`. To run retention only once, set the recurrence value to empty. This example uses the <xref:Microsoft.Dynamics.CRM.retentionconfig?displayProperty=nameWithType> entity type.

**Request:**

```http
POST [Organization Uri]/api/data/v9.1/retentionconfigs
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json

{
"statecode": 0,
 "name": "Retain all closed opportunities",
 "uniquename": "ui_RetainAllClosedOpportunities",
 "statuscode": 10,
 "criteria": 
      "<fetch>
          <entity name=\"opportunity\">
              <attribute name=\"name\" />
              <attribute name=\"statecode\" />
              <attribute name=\"actualvalue\" />
              <attribute name=\"actualclosedate\" />
              <attribute name=\"customerid\" />
              <attribute name=\"opportunityid\" />
              <order attribute=\"actualclosedate\" descending=\"true\" />
              <filter type=\"and\">
                  <filter type=\"or\">
                      <condition attribute=\"statecode\" operator=\"eq\" value=\"1\" />
                      <condition attribute=\"statecode\" operator=\"eq\" value=\"2\" />
                  </filter>
              </filter>
          </entity>
      </fetch>",
 "starttime": "2023-05-01T00:00:00",
 "recurrence": "FREQ=YEARLY;INTERVAL=1",
 "retentionconfigid": "35cc1317-20b7-4f4f-829d-5d9d5d77f712",
 "entitylogicalname": "incident"
}
```

---

## Validate your retention policy

The long-term retention process moves data from Dataverse transactional storage to a managed data lake. You can no longer run transactional operations on the data after it moves to the data lake. It's important to make sure your retention policies are correct. You can add your own validations by optionally registering a custom [plug-in](plug-ins.md) on the `ValidateRetentionConfig` message.

### [SDK for .NET](#tab/sdk)

```csharp
class SampleValidateRetentionConfigPlugin : IPlugin
{
    public void Execute(IServiceProvider serviceProvider)
    {
        var pluginContext = (IPluginExecutionContext)serviceProvider.GetService(typeof(IPluginExecutionContext));
        var entityName = pluginContext.PrimaryEntityName;
        if( pluginContext.InputParameters.TryGetValue("FetchXml", out var fetchXml) )
        {
            // Add custom validation against the Fetch XML. 
        }
        else
        {
            throw new Exception("No critiera provided.");
        }
    }
}
```

### [Web API](#tab/webapi)

The Web API doesn't support the development of plug-ins

---

## Custom logic while retention executes

Long-term retention is an asynchronous process that executes whenever a retention policy is set up. It performs the following operations:

1. Mark rows (records) ready for retention.
1. Copy marked rows to the data lake.
1. Purge rows from the source database.
1. Roll back the marked rows if the purge fails.

You can optionally register custom plug-ins to execute when rows are being marked for retention, when rows are being purged at the source, or when rows marked for retention are rolled back. Writing plug-in code applies to SDK for .NET programming only. The Web API doesn't support plug-in development.

### Custom logic when row is marked for retention

As part of marking rows for retention, Dataverse invokes the `BulkRetain` and `Retain` messages. You can add custom logic by registering a plug-in on execution of those messages. Examples of custom logic include marking more rows for retention or performing validation before rows are marked for retention

This code sample shows a custom plug-in that's executed during retention of a single table row.

```csharp
class SampleRetainPlugin : IPlugin
{
    public void Execute(IServiceProvider serviceProvider)
    {
        var pluginContext = (IPluginExecutionContext)serviceProvider.GetService(typeof(IPluginExecutionContext));
        var entityName = pluginContext.PrimaryEntityName;
        if( pluginContext.InputParameters.TryGetValue("Target", out var _target) )
        {
            EntityReference target = (EntityReference)_target;
            Console.WriteLine($"Request came for table : {target.Name} with id : {target.Id}");
            // Add your logic for validation or additional operation. 
            // For example - you can call Retain on Additional row of another table. 
        }
        else
        {
            throw new Exception("No target present.");
        }
    }
}
```

For a rollback retain operation, write your plug-in similar to the above example, except register it on the `RollbackRetain` message.

### Custom logic on bulk retain

This code sample demonstrates custom logic on the last page execution of a `BulkRetain` message operation

```csharp
class SampleBulkRetainPlugin : IPlugin
{
    // Send notification when bulk retain execution is done. 
    public void Execute(IServiceProvider serviceProvider)
    {
        var pluginContext = (IPluginExecutionContext)serviceProvider.GetService(typeof(IPluginExecutionContext));
        var entityName = pluginContext.PrimaryEntityName;
        if(pluginContext.OutputParameters != null 
            && pluginContext.OutputParameters.TryGetValue("HasMoreRecords", out var _hasMoreRecords) )
        {    
            if(!(bool)_hasMoreRecords)
            {
                Console.WriteLine("This is a last execution of this request.");
                // SendNotifcation that retention for an entity is completed. 
            }
        }
    }
}
```

### Custom logic when row is deleted due to retention

Dataverse executes the `PurgeRetainedContent` message to delete the transactional data rows that were successfully moved to the data lake. The `PurgeRetainedContent` message internally executes a `Delete` message operation to delete the table rows that were successfully moved

You can register a custom plug-in on the `PurgeRetainedContent` message if you need custom logic during the purge operation at the table level. Optionally, you can register a custom plug-in on the `Delete` message if you need to invoke code when a row is deleted due to retention. You can determine whether the deletion happened due to retention or not by checking the plug-in's [ParentContext](xref:Microsoft.Xrm.Sdk.IPluginExecutionContext.ParentContext) property. The `ParentContext` property value for the `Delete` message operation due to retention is "PurgeRetainedContent."

This code sample blocks the purge on a table when rows aren't ready for purging

```csharp
class SamplePurgeRetainedContentPlugin : IPlugin
{
    // Block purge if all the rows are not validatd. 
    public void Execute(IServiceProvider serviceProvider)
    {
        var pluginContext = (IPluginExecutionContext)serviceProvider.GetService(typeof(IPluginExecutionContext));
        var entityName = pluginContext.PrimaryEntityName;
        if( pluginContext.InputParameters.TryGetValue("MaxVersionToPurge", out var _maxVersiontoPurge) )
        {
            long MaxVersionToPurge = (long)_maxVersiontoPurge;
            var rowsToBePurged = GetToBePurgedRows(entityName, MaxVersionToPurge);
            // Add custom validation to process rowsToBePurged.
        }
    }

    public EntityCollection GetToBePurgedRows(string  entityName, long maxVersionToPurge)
    {
        IOrganizationService organizationService; // Create OrgService. 
        QueryExpression queryExpression = new QueryExpression()
        {
            EntityName = entityName,
            ColumnSet = new ColumnSet(new string[] { "versionnumber", "msft_datastate" })
        };
        queryExpression.Criteria.AddCondition("msft_datastate", ConditionOperator.Equal, 1);
        queryExpression.Criteria.AddCondition("versionnumber", ConditionOperator.LessEqual, maxVersionToPurge);
        var response = organizationService.RetrieveMultiple(queryExpression);
        return response;
    }
}
```

This code sample applies to the delete operation due to retention

```csharp
class SampleDeletePlugin : IPlugin
{
    public void Execute(IServiceProvider serviceProvider)
    {
        if (IsDeleteDueToRetention(serviceProvider))
        {
            // Write your code to handle delete during retention
        }
        else
        {
            // Write your code to handle normal delete without retention
        }
    }

    private bool IsDeleteDueToRetention(IServiceProvider serviceProvider)
    {
        var currentContext = (IPluginExecutionContext)serviceProvider.GetService(typeof(IPluginExecutionContext));
        while (currentContext != null)
        {
            if (string.Equals(currentContext.MessageName, "PurgeRetainedContent"))
            {
                return true;
            }
            else
            {
                currentContext = currentContext.ParentContext;
            }
        }
        return false;
    }
}
```

## Query retention policy and execution details

Retention policy details are stored in the `RetentionConfig` table. Retention execution details are stored in the `RetentionOperation` and `RetentionOperationDetail` tables. You can query these tables to get the retention policy and execution details.

The following code provides a few examples of FetchXML that can be used to query the date retention detail table rows. FetchXML is a proprietary XML-based query language. It can be used with SDK-based queries using <xref:Microsoft.Xrm.Sdk.Query.FetchExpression> and by the Web API using the `fetchXml` query string

This code sample shows a simple query to return all active retention policies for an email order by name.

### [SDK for .NET](#tab/sdk)

```csharp

public EntityCollection GetActivePolicies(IOrganizationService orgService)
{
    string fetchXml = @"
    <fetch>
      <entity name='retentionconfig'>
        <attribute name='retentionconfigid' />
        <attribute name='name' />
        <attribute name='createdon' />
        <attribute name='starttime' />
        <attribute name='recurrence' />
        <attribute name='entitylogicalname' />
        <attribute name='criteria' />
        <order attribute='name' descending='false' />
        <filter type='and'>
          <condition attribute='entitylogicalname' operator='eq' value='email' />
          <condition attribute='statuscode' operator='eq' value='10' />
        </filter>
      </entity>
    </fetch>";

    var query = new FetchExpression(fetchXml);

    EntityCollection results = orgService.RetrieveMultiple(query);

    results.Entities.ToList().ForEach(x => {
      Console.WriteLine(x.Attributes["name"]);
    });

    return(results);
}
```

### [Web API](#tab/webapi)

 [Learn how to use FetchXml with the Web API](./webapi/use-fetchxml-web-api.md)

---

### More examples of FetchXML query strings

This code sample illustrates using a FetchXML statement to retrieve all paused retention policies for an email.  
  
```xml  
<fetch>
  <entity name="retentionconfig">
    <attribute name="retentionconfigid" />
    <attribute name="name" />
    <attribute name="createdon" />
    <attribute name="starttime" />
    <attribute name="recurrence" />
    <attribute name="entitylogicalname" />
    <attribute name="criteria" />
    <order attribute="name" descending="false" />
    <filter type="and">
      <condition attribute="entitylogicalname" operator="eq" value="email" />
      <condition attribute="statuscode" operator="eq" value="20" />
    </filter>
  </entity>
</fetch>
```  

This code sample shows how to use a FetchXML statement to retrieve all retention operations for a retention policy.

```xml  
<fetch>
  <entity name="retentionoperation">
    <attribute name="retentionoperationid" />
    <attribute name="name" />
    <attribute name="statuscode" />
    <attribute name="statecode" />
    <attribute name="starttime" />
    <attribute name="rootentitylogicalname" />
    <attribute name="endtime" />
    <attribute name="criteria" />
    <order attribute="name" descending="false" />
    <filter type="and">
      <condition 
         attribute="retentionconfigid" 
         operator="eq" 
         value="{35CC1317-20B7-4F4F-829D-5D9D5D77F763}" />
    </filter>
  </entity>
</fetch>
```

This code sample shows a FetchXML statement that retrieves details for a retention operation.

```xml  
<fetch>
  <entity name="retentionoperationdetail">
    <attribute name="retentionoperationdetailid" />
    <attribute name="name" />
    <attribute name="createdon" />
    <attribute name="retentionoperationid" />
    <attribute name="retentioncount" />
    <attribute name="isrootentity" />
    <attribute name="failedcount" />
    <attribute name="entitylogicalname" />
    <order attribute="name" descending="false" />
    <filter type="and">
      <condition attribute="retentionoperationid" operator="eq" value="{35CC1317-20B7-4F4F-829D-5D9D5D77F763}"/>
    </filter>
  </entity>
</fetch>
```

This code sample illustrates the FetchXML statement that retrieves details about a failure that occurred during a retention operation.

```xml
<fetch>
  <entity name="retentionfailuredetail">
    <attribute name="retentionfailuredetailid" />
    <attribute name="name" />
    <attribute name="createdon" />
    <attribute name="recordid" />
    <attribute name="operation" />
    <attribute name="message" />
    <order attribute="name" descending="false" />
    <filter type="and">
      <condition attribute="operationid" operator="eq" value="35CC1317-20B7-4F4F-829D-5D9D5D77F763" />
    </filter>
  </entity>
</fetch>
```

### See also

[Manage data retention policies](../../maker/data-platform/data-retention-manage.md)  
[View long-term retained data](../../maker/data-platform/data-retention-view.md)  
[Delete data in bulk](delete-data-bulk.md)  
[Use the Microsoft Dataverse Web API](webapi/overview.md)

[!INCLUDE [footer-include](../../includes/footer-banner.md)]
