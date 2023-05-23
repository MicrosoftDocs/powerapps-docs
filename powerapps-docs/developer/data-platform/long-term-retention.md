---
title: "Long-term data retention (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Dataverse long-term data retention enables customers to transfer data from their transactional database to the Dataverse managed data lake." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: 
ms.date: 05/18/2023
ms.reviewer: "pehecke"
ms.topic: "article"
author: "kagoswami" # GitHub ID
ms.subservice: dataverse-developer
ms.author: "kagoswami" # MSFT alias of Microsoft employees only
search.audienceType: 
  - developer
---

# Long-term data retention (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

*Long-term retention* (LTR) is a Dataverse capability that enables customers to transfer their data from a transactional database to the Dataverse managed data lake. To perform the LTR operations, you are required to set up retention policies by defining the criteria for a given table. Based on the policy, retention will run at the scheduled time and retain rows matching the critiera.     
   
More information: [Dataverse long term data retention overview](../../maker/data-platform/data-retention-overview.md), [Enable a table for long term retention](../../maker/data-platform/data-retention-set.md#enable-a-table-for-long-term-retention)

> [!IMPORTANT]
> - This is a preview feature.
> - [!INCLUDE [cc-preview-features-definition](../../includes/cc-preview-features-definition.md)]
> - For public preview, only non-production environments are allowed for previewing the long-term data retention feature. Production and Dataverse for Teams environments can't be used with this feature.
> - No additional Power Platform licensing requirement is required to experience this feature during the preview. However, there will be a licensing requirement once the feature is generally available.
> - Pricing information for long term data retention will be available at general availability.
  
## Retention policy setup and validation
Retention policy setup can be done using API, maker portal and solution installation. Below example shows how to setup retention policy using Web API and SDK Message. 

The following code example demonstrates the retention APIs to create retention policy.
 
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

**Output**:
```
Retention policy created with Id : c1a9e932-89f6-4f17-859c-bd2101683263
```
More information:

- [What is the Organization service](org-service/overview.md)
- [IOrganizationService.Create Method](xref:Microsoft.Xrm.Sdk.IOrganizationService.Create%2A)

### [Web API](#tab/webapi)

The following is an example of a Web API request of retention policy setup to retain all the closed opportunities, and will be run on a yearly basis. This example uses the <xref:Microsoft.Dynamics.CRM.retentionconfig?displayProperty=nameWithType>.

**Request**

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
> Valid recurrence parameters are: DAILY, WEEKLY, MONTHLY, YEARLY

---
 
Retention moves data from transaction storage to data lake. Once data moved to the data lake, customer can not perform any transactional operations on the data. And hence it is important to make sure that incorrect policies are not being setup for retention. You can add your own validations by optionally registering the custom plugin to *ValidateRetentionConfig* message.


### [Custom plugin on ValidateRetentionConfig](#tab/sdk)

```csharp
class SampleValidateRetentionConfigPlugin : IPlugin
{
    public void Execute(IServiceProvider serviceProvider)
    {
        var pluginContext = (IPluginExecutionContext)serviceProvider.GetService(typeof(IPluginExecutionContext));
        var entityName = pluginContext.PrimaryEntityName;
        if( pluginContext.InputParameters.TryGetValue("FetchXml", out var fetchXml) )
        {
            // Add custom validation against the fetch XML. 
        }
        else
        {
            throw new Exception("No critiera provided.");
        }
    }
}
```

More information: <xref:Microsoft.Dynamics.CRM.ValidateRetentionConfig?displayProperty=nameWithType>, [Set a data retention policy for a table](../../maker/data-platform/data-retention-set.md)

## Custom logic while retention execution
Long term retention is an async process which gets executed whenever retention policy is setup. Behind the scene it does below operations.   
        1. Mark records ready for retention  
        2. Copy marked records to the data lake  
        3. Purge records from source.  
        4. Rollback marked record if purge fails.   

During retention execution you can optionally add custom plugin during the process of records are being marked for the retention, when records are getting purged at the source or when marked record for retention get rolledback. 

### Custom logic while record gets marked for retention
As part of marking record for retention, platform calls *BulkRetain* and *Retain* message. You can add custom logic (such as having additional records marked for retenion, validation before records are being marked for retained) by optionally registering plugin to *BulkRetain* and *Retain* message.

#### [Custom plugin while retention of single row](#tab/sdk)

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
            // For example - you can call Retain on Additional record of another table. 
        }
        else
        {
            throw new Exception("No target present.");
        }
    }
}
```
> [!NOTE]
> To run the simpilar plugin for rollback retain, write plugin similar to above on *RollbackRetain* message. 
> More information: <xref:Microsoft.Dynamics.CRM.RollbackRetain?displayProperty=nameWithType>

#### [Custom plugin on BulkRetain](#tab/sdk)
Below is the sample plugin logic when you want to add the custom logic on the last page execution of Bulk Retain. 

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

More information: <xref:Microsoft.Dynamics.CRM.BulkRetain?displayProperty=nameWithType>
More information: <xref:Microsoft.Dynamics.CRM.Retain?displayProperty=nameWithType>

### Custom logic while record gets deleted due to retention
Platform calls *PurgeRetainedContent* to delete the rows which are successfully moved to data lake. PurgeRetainedContent internal calls the *Delete* method to delete the retained table rows which are successfully moved to data lake.     

You can optionally add a custom plugin to *PurgeRetainedContent* message, if you need any custom logic during the purge operation at the table label. Optionally You can also  modify or create custom plugin for *Delete* message if you need a specific custom logic when record gets deleted due to retention. You can identify whether the delete happened due to retention or not by checking the ParentContext. ParentContext for the Delete API due to retention would be *PurgeRetainedContent*. 

#### [Sample plugin to block purge unless record are validated](#tab/sdk)
Below is the sample plugin to block the purge on table whenever records are not ready for purge. 

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

#### [Sample plugin for delete record due to retention](#tab/sdk)
Below is the sample code for custom plugin for the delete due to retention. 
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
Retention policy details are stored in the *RetentionConfig* table. Retention execution details are stored in *RetentionOperation* and *RetentionOperationDetail* table. You can query these tables to get the retention policy and execution details. 

Below are few examples of sample FetchXML which can be used to query the retention details. FetchXml is a proprietary XML-based query language that can be used with SDK Assembly queries using <xref:Microsoft.Xrm.Sdk.Query.FetchExpression> and by the Web API using the `fetchXml` query string. More information: [Use FetchXml with Web API](../webapi/use-fetchxml-web-api.md)

The following example shows a simple query to return all active retention policies for an email order by name.

#### [FetchXml to retrieve all active retention policies ](#tab/sdk)

```csharp
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

EntityCollection results = svc.RetrieveMultiple(query);

results.Entities.ToList().ForEach(x => {
  Console.WriteLine(x.Attributes["name"]);
});
```

### Other example FetchXML query strings

In the following example, the **FetchXML** statement retrieves all paused retention policies for an email.  
  
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

In the following example, the **FetchXML** statement retrieves all retention operations for retention policy.
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

In the following example, the **FetchXML** statement retrieves detailed retention operation details for retention operation.
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

---

### See also

[Manage data retention policies](../../maker/data-platform/data-retention-manage.md)  
[View long term retained data](../../maker/data-platform/data-retention-view.md)  
[Delete data in bulk](delete-data-bulk.md)  
[Use the Microsoft Dataverse Web API](webapi/overview.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
