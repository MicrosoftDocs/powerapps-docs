---
title: "Long-term data retention (Microsoft Dataverse) | Microsoft Docs"
description: "Dataverse long-term data retention enables customers to retain their historical transactional data with Dataverse long term retention."
ms.custom: 
ms.date: 02/28/2024
ms.reviewer: "pehecke"
ms.topic: "article"
author: "kagoswami"
ms.subservice: dataverse-developer
ms.author: "kagoswami"
search.audienceType: 
  - developer
---

# Long-term data retention

*Long-term retention* (LTR) is a capability that enables customers to retain their historical transactional data with Dataverse long term retention. To perform retention operations, you're required to set up retention policies by defining criteria for a given parent (root) data table. Based on the policy, retention runs at the scheduled time and rows are retained across the parent and child tables that match the criteria.

More information: [Dataverse long term data retention overview](../../maker/data-platform/data-retention-overview.md), [Enable a table for long term retention](../../maker/data-platform/data-retention-set.md#enable-a-table-for-long-term-retention)

> [!IMPORTANT]
> To use all long term data retention features you must meet both of the requirements described here: [Dataverse long term data retention overview](../../maker/data-platform/data-retention-overview.md#dataverse-long-term-data-retention-overview).
  
## Retention policy setup and validation

Retention policy set-up can be done using our APIs, the maker portal, and solution installation. The following code example demonstrates the retention APIs to create a retention policy.

### [SDK for .NET](#tab/sdk)

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
    retentionConfig["criteria"] = "<fetch version=\"1.0\" output-format=\"xml-platform\" mapping=\"logical\" distinct=\"false\"> " +
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

More information:

- [What is the SDK for .NET](org-service/overview.md)
- [IOrganizationService.Create Method](xref:Microsoft.Xrm.Sdk.IOrganizationService.Create%2A)

### [Web API](#tab/webapi)

The following Web API example is for retention policy set up to retain all the closed opportunities, and this policy is run on a yearly basis. This example uses the <xref:Microsoft.Dynamics.CRM.retentionconfig?displayProperty=nameWithType>.

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
      "<fetch version=\"1.0\" output-format=\"xml-platform\" mapping=\"logical\" distinct=\"false\">
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

> [!NOTE]
> If you want to run retention only once, set the recurrence value as empty.
> Valid recurrence parameters are: DAILY, WEEKLY, MONTHLY, and YEARLY.

---

### Custom plug-in on ValidateRetentionConfig

The data retention process moves data from Dataverse transactional storage to Dataverse long term retention. Once data is retained with long term retention, you can't perform any transactional operations on that data. It's important to make sure that incorrect policies aren't being set up for data retention. You can add your own validations by optionally registering a custom [plug-in](plug-ins.md) on the `ValidateRetentionConfig` message.

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

Plug-in development isn't supported by the Web API.

---

More information: <xref:Microsoft.Dynamics.CRM.ValidateRetentionConfig?displayProperty=nameWithType>, [Set a data retention policy for a table](../../maker/data-platform/data-retention-set.md)

## Custom logic while retention executes

Long-term retention is an asynchronous process that executes whenever a retention policy is set up. Internally, the following operations are performed.

1. Mark rows (records) ready for retention
1. Copy marked rows to the data lake  
1. Purge rows from the source database
1. Roll back the marked rows if the above purge fails

During retention execution, you can optionally register custom plug-ins while rows are being marked for retention, when rows are getting purged at the source, or when marked rows for retention get rolled back.

The following sections provide more information about writing custom plug-in code for invocation during the above mentioned operations. Writing plug-in code applies to SDK for .NET programming only.

### Custom logic when row is marked for retention

As part of marking rows for retention, Dataverse invokes the `BulkRetain` and `Retain` messages. You can add custom logic by optionally registering a plug-in on execution of those messages. Some examples of such logic would be having more rows marked for retention or performing validation before rows are being marked for retained.

This code sample shows a custom plug-in to be executed during retention of a single table row.

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

> [!NOTE]
> For a rollback retain operation, write your plug-in similar to the above example except register it on
> the `RollbackRetain` message.

### Custom logic on bulk retain

The plug-in code shown demonstrates custom logic on the last page execution of a `BulkRetain` message operation.

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

### Custom logic while row gets deleted due to retention

Dataverse executes the `PurgeRetainedContent` message to delete the transactional data rows that were successfully retained with Dataverse long term retention. The `PurgeRetainedContent` message internally executes a `Delete` message operation to delete the retained table rows that were successfully moved.

You can optionally register a custom plug-in on the `PurgeRetainedContent` message if you need any custom logic invoked during the purge operation at the table level. Optionally, you can register a custom plug-in on the `Delete` message if you need to invoke code when a row gets deleted due to retention. You can identify whether the delete happened due to retention or not by checking the plug-in's [ParentContext](xref:Microsoft.Xrm.Sdk.IPluginExecutionContext.ParentContext) property. The `ParentContext` property value for the `Delete` message operation due to retention is "PurgeRetainedContent".

The plug-in code shown below blocks the purge on a table whenever rows aren't ready for purge.

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

The example plug-in code shown applies to the delete operation due to retention.

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

Retention policy details are stored in the `RetentionConfig` table. Retention execution details are stored in `RetentionOperation` and `RetentionOperationDetail` tables. You can query these tables to get the retention policy and execution details.

Here are a few examples of FetchXML that can be used to query the retention details. FetchXML is a proprietary XML-based query language that can be used with SDK based queries using <xref:Microsoft.Xrm.Sdk.Query.FetchExpression> and by the Web API using the `fetchXml` query string.

The following example shows a simple query to return all active retention policies for an email order by name.

### [SDK for .NET](#tab/sdk)

```csharp

public EntityCollection GetActivePolicies(IOrganizationService orgService)
{
    string fetchXml = @"
    <fetch version='1.0' output-format='xml-platform' mapping='logical' distinct='false'>
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

More information: [Query data using FetchXml](fetchxml/overview.md)

---

### More examples of FetchXML query strings

In the following example, the FetchXML statement retrieves all paused retention policies for an email.  
  
```xml  
<fetch version="1.0" output-format="xml-platform" mapping="logical" distinct="false">
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

In the following example, the FetchXML statement retrieves all retention operations for a retention policy.

```xml  
<fetch version="1.0" output-format="xml-platform" mapping="logical" distinct="false">
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
      <condition attribute="retentionconfigid" operator="eq" uiname="All closed opportunities" uitype="retentionconfig" value="{35CC1317-20B7-4F4F-829D-5D9D5D77F763}" />
    </filter>
  </entity>
</fetch>
```

In the following example, the FetchXML statement retrieves detailed retention operation details for a retention operation.

```xml  
<fetch version="1.0" output-format="xml-platform" mapping="logical" distinct="false">
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
      <condition attribute="retentionoperationid" operator="eq"  uitype="retentionoperation" value="{35CC1317-20B7-4F4F-829D-5D9D5D77F763}"/>
    </filter>
  </entity>
</fetch>
```

In the following example, the FetchXML statement retrieves failure details while executing a retention operation.

```xml
<fetch version="1.0" output-format="xml-platform" mapping="logical" distinct="false">
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
[View long term retained data](../../maker/data-platform/data-retention-view.md)  
[Delete data in bulk](delete-data-bulk.md)  
[Use the Microsoft Dataverse Web API](webapi/overview.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
