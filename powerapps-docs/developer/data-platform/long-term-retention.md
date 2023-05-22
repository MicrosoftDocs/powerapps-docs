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

*Long-term retention* (LTR) is a Dataverse capability that enables customers to transfer their data from a transactional database to the Dataverse managed data lake. To perform the LTR operations, you are required to set up retention policies by defining the criteria for a given table. To set up the retention policy, you should have your environment (organization) and tables both enabled for retention.

More information: [Dataverse long term data retention overview](../../maker/data-platform/data-retention-overview.md), [Enable a table for long term retention](../../maker/data-platform/data-retention-set.md#enable-a-table-for-long-term-retention)

> [!IMPORTANT]
> - This is a preview feature.
> - [!INCLUDE [cc-preview-features-definition](../../includes/cc-preview-features-definition.md)]
> - For public preview, only non-production environments are allowed for previewing the long-term data retention feature. Production and Dataverse for Teams environments can't be used with this feature.
> - No additional Power Platform licensing requirement is required to experience this feature during the preview. However, there will be a licensing requirement once the feature is generally available.
> - Pricing information for long term data retention will be available at general availability.
  
## Configure retention policy using code

You can set up the retention policy by creating an entry in the retention configuration table. As part of retention policy set up, the platform will validate the policy against a set of system rule defined under ValidateRetentionConfig SDK Message. 

More information: <xref:Microsoft.Dynamics.CRM.ValidateRetentionConfig?displayProperty=nameWithType>, [Set a data retention policy for a table](../../maker/data-platform/data-retention-set.md)

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

## Configure retention policy using solution import

The retention policy can be configured during solution import. More information about solutions: [Solutions overview](../../maker/data-platform/solutions-overview.md).

Below is sample solution customization.xml code to create a retention policy.

```xml
<retentionconfig retentionconfigid="8fd449d1-f389-4f63-84c6-023c77275359">
  <criteria><fetch version="1.0" output-format="xml-platform" mapping="logical" distinct="true">
    <entity name="incident">
        <attribute name="title"/>
        <attribute name="incidentid"/>
        <attribute name="prioritycode"/>
        <filter type="and">
            <condition attribute="prioritycode" operator="eq" value="3"/>
        </filter>
    </entity>
  </fetch></criteria>
  <entitylogicalname>incident</entitylogicalname>
  <iscustomizable>1</iscustomizable>
  <name>Resolved Cases in EastR1</name>
  <recurrence>FREQ=MONTHLY;INTERVAL=1</recurrence>
  <referenceconfigid>360ec029-5688-42e0-bc56-34833c8233d5</referenceconfigid>
  <starttime>5/5/2023 6:32:50 PM</starttime>
  <statecode>0</statecode>
  <statuscode>10</statuscode>
  <timezoneruleversionnumber>0</timezoneruleversionnumber>
  <uniquename>ui_360ec029-5688-42e0-bc56-34833c8233d5</uniquename>
</retentionconfig>

```

## Add custom validation to the retention policy

Table and app owners can add their own custom validations whenever a retention policy is created or updated. This validation can be done by registering a custon [plug-in](apply-business-logic-with-code.md) against the `ValidateRetentionConfig` action.

`ValidateRetentionConfig` is a bound action, which gets bound to the table whenever retention is enabled.

More information: <xref:Microsoft.Dynamics.CRM.ValidateRetentionConfig?displayProperty=nameWithType>

The following code example demonstrates retention policy validation.

### [SDK for .NET](#tab/sdk)

```csharp
public void ValidateRetentionConfig(IOrganizationService orgService)
{
    var request = new OrganizationRequest
    {
        RequestName = "ValidateRetentionConfig"
    };

    string xml = "<fetch version='1.0' output-format='xml-platform' mapping='logical' distinct='false'>< entity name = 'account' >< attribute name = 'accountid' />< order attribute = 'name' descending = 'false' /></ entity ></ fetch > ";
    request.Parameters["FetchXml"] = xml;
    request.Parameters.Add("EntityName", "account");

    OrganizationResponse response = orgService.Execute(request);

    if (response != null
        && response.Results != null)
    {
        if (response.Results.TryGetValue("IsValidationSuccessful", out var IsValidationSuccessful))
        {
            Console.WriteLine($"IsValidationSuccessful : {IsValidationSuccessful}");
        }
    }
}
```

**Output**
```
IsValidationSuccessful : True
```

### [Web API](#tab/webapi)

The following example validates all closed opportunities, and will be run on a yearly basis.

**Request**

```http
POST [Organization Uri]/api/data/v9.1/ValidateRetentionConfig
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json

{
"FetchXml": "<fetch version='1.0' output-format='xml-platform' mapping='logical' distinct='false'>
    <entity name='account'>
        <attribute name='accountid' />
        <order attribute='name' descending='false' />
        <filter type='and'>
            <condition attribute='name' operator='like' value='Name%' />
        </filter>
    </entity>
  </fetch>",
"EntityName" : "account"
}
```

**Response**

```http
HTTP/1.1 200 OK
{
  "@odata.context": "[Organization Uri]/api/data/v9.1/$metadata#Microsoft.Dynamics.CRM.ValidateRetentionConfigResponse",
  "IsValidationSuccessful": true,
  "ErrorMessage": null
}
```

---

## Custom logic during retention process
Long term retention is an async process which gets executed whenever retention policy is setup. Behind the scene it does below operations.   
        1. Mark records ready for retention  
        2. Copy marked records to the data lake  
        3. Purge records from source.  
        4. Rollback marked record if purge fails. 
  
You can perform custom operation in form of additional validation and/or pre and post processing by registring a custom plugin on below SDK Messages. 

## BulkRetain
A message named *BulkRetain* executes whenever retenion policy execution happens. You can optionally register a custom plug-in to be executed whenever rows matching to criteria are being marked for retention

More information: <xref:Microsoft.Dynamics.CRM.BulkRetain?displayProperty=nameWithType>

### [SDK for .NET](#tab/sdk)

```csharp
public void BulkRetain(IOrganizationService orgService)
{
    var request = new OrganizationRequest
    {
        RequestName = "BulkRetain"
    };

    string xml = "<fetch version=\"1.0\" output-format=\"xml-platform\" mapping=\"logical\" distinct=\"false\"> " +
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
    request.Parameters["FetchXml"] = xml;
    request.Parameters["PageSize"] = 10;
    request.Parameters["OperationId"] = Guid.NewGuid().ToString();
    request.Parameters.Add["EntityName"] = "opportunity";
    
    try
    {
        bool hasMoreRecords = true;
        while (hasMoreRecords) { 
            OrganizationResponse response = orgService.Execute(request);
            if (response?.Results != null )
            {
                if (response.Results.TryGetValue("PagingCookie", out var pagingCookie))
                {
                    request.Parameters["PagingCookie"] = pagingCookie;
                }

                if (response.Results.TryGetValue("HasMoreRecords", out var _hasMoreRecords))
                {
                    hasMoreRecords = (bool) _hasMoreRecords;
                }

                if (response.Results.TryGetValue("EntityCountCollection", out var entityRecordCollection))
                {
                    foreach (var entityRecord in (EntityRecordCountCollection)entityRecordCollection)
                    {
                        Console.WriteLine($"Entity Name: {entityRecord.Key}, Retained Record Count: {entityRecord.Value}");
                    }
                }
            }
        }
    }
    catch (Exception ex)
    {
        throw new Exception($"Bulk Retain request failed. Error: {ex.Message})", ex);
    }
    
}
```

**Output**
```
Entity Name: opportunity, Retained Record Count: 10
Entity Name: opportunity, Retained Record Count: 10
Entity Name: opportunity, Retained Record Count: 2
```


### [Web API](#tab/webapi)

The following example executes bulk retention on the an opportunity table.

**Request**

```http
POST [Organization Uri]/api/data/v9.1/BulkRetain
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json

{
  "OperationId":"fd2639b2-f300-408c-b605-75febff98d4f" ,
  "PageSize":10,
  "FetchXml": "<fetch version=\"1.0\" output-format=\"xml-platform\" mapping=\"logical\" distinct=\"false\"> <entity name=\"opportunity\"> <attribute name=\"name\" /> <attribute name=\"statecode\" /><attribute name=\"actualvalue\" /><attribute name=\"actualclosedate\" /><attribute name=\"customerid\" /><attribute name=\"opportunityid\" /><order attribute=\"actualclosedate\" descending=\"true\" /><filter type=\"and\"><filter type=\"or\"><condition attribute=\"statecode\" operator=\"eq\" value=\"1\" /><condition attribute=\"statecode\" operator=\"eq\" value=\"2\" /></filter></filter></entity></fetch>",
  "EntityName": "opportunity"
}

```

**Response**

```http
HTTP/1.1 200 OK
{
  "@odata.context": "http://10.139.166.40/CITTest/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.BulkRetainResponse",
    "PagingCookie": "<cookie page=\"1\"><versionnumber last=\"2036955\" first=\"2036955\" /><actualclosedate lastnull=\"1\" firstnull=\"1\" /><opportunityid last=\"{1EE2137D-99F8-ED11-884E-000D3A7080DA}\" first=\"{1EE2137D-99F8-ED11-884E-000D3A7080DA}\" /></cookie>",
    "HasMoreRecords": true,
    "FailedRecords": 0,
    "EntityCountCollection": {
        "Count": 1,
        "IsReadOnly": false,
        "Keys": [
            "opportunity"
        ],
        "Values": [
            10
        ]
    }
}
```

> [!NOTE]
> If you get HasMoreRecords as true in response, there are records remaining for the criteria. 


## Retain
A message named *Retain* executes whenever a table row is marked for retention. You can optionally register a custom plug-in to be executed when the row is being marked for retention.

More information: <xref:Microsoft.Dynamics.CRM.Retain?displayProperty=nameWithType>

The following example executes retention on the an email record.

### [SDK for .NET](#tab/sdk)

```csharp
public void Retain(IOrganizationService orgService)
{

    var request = new OrganizationRequest { RequestName = "Retain" };
    request.Parameters["Target"] = new EntityReference("email", new Guid("8b9cc8c0-8c08-46cf-a5c3-00057edc8e4e"));

    try
    {
        OrganizationResponse response = orgService.Execute(request);
        if (response?.Results != null && response.Results.TryGetValue("EntityCountCollection", out var entityRecordCollection))
        {
            // Put your logic here. 
            foreach( var entityRecord in (EntityRecordCountCollection) entityRecordCollection)
            {
                Console.WriteLine($"Entity Name: {entityRecord.Key}, Retained Record Count: {entityRecord.Value}");
            }
        }
    }
    catch (Exception ex)
    {
        throw new Exception($"Retain request failed. Error: {ex.Message})", ex);
    }
}
```

**Output**
```
Entity Name: activityparty, Retained Record Count: 2
Entity Name: activitypointer, Retained Record Count: 1
Entity Name: email, Retained Record Count: 1
```

### [Web API](#tab/webapi)


**Request**

```http
POST [Organization Uri]/api/data/v9.1/Retain
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json

{
"OperationId":"fd2639b2-f300-408c-b605-75febff98d4f" ,
"Target":{
"@odata.type": "Microsoft.Dynamics.CRM.email",
"activityid": "8b9cc8c0-8c08-46cf-a5c3-00057edc8e4e"}
}
```

**Response**

```http
HTTP/1.1 200 OK
{
  "@odata.context": "[Organization Uri]/api/data/v9.1/$metadata#Microsoft.Dynamics.CRM.RetainResponse",
  "EntityCountCollection": {
      "Count": 3,
      "IsReadOnly": false,
      "Keys": [
          "activityparty",
          "activitypointer",
          "email"
      ],
      "Values": [
          2,
          1,
          1
      ]
  }
}
```

## Rollback Retain

A message named *RollbackRetain* executes whenever a marked table row for retention is rolled back to normal one on failure of further processing. You can optionally register a custom plug-in to be executed whenever retention for the row is rolledback. 

More information: <xref:Microsoft.Dynamics.CRM.RollbackRetain?displayProperty=nameWithType>

The following example executes rollback retention on the an email record.

### [SDK for .NET](#tab/sdk)

```csharp
public void RollbackRetain(IOrganizationService orgService)
{

    var request = new OrganizationRequest { RequestName = "RollbackRetain" };
    request.Parameters["Target"] = new EntityReference("email", new Guid("8b9cc8c0-8c08-46cf-a5c3-00057edc8e4e"));

    try
    {
        OrganizationResponse response = orgService.Execute(request);
        if (response?.Results != null && response.Results.TryGetValue("EntityCountCollection", out var entityRecordCollection))
        {
            // Put your logic here. 
            foreach( var entityRecord in (EntityRecordCountCollection) entityRecordCollection)
            {
                Console.WriteLine($"Entity Name: {entityRecord.Key}, Rollback Record Count: {entityRecord.Value}");
            }
        }
    }
    catch (Exception ex)
    {
        throw new Exception($"RollbackRetain request failed. Error: {ex.Message})", ex);
    }
}
```

**Output**
```
Entity Name: activityparty, Rollback Record Count: 2
Entity Name: activitypointer, Rollback Record Count: 1
Entity Name: email, Rollback Record Count: 1
```

### [Web API](#tab/webapi)

**Request**

```http
POST [Organization Uri]/api/data/v9.1/RollbackRetain
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json

{
"OperationId":"fd2639b2-f300-408c-b605-75febff98d4f" ,
"Target":{
"@odata.type": "Microsoft.Dynamics.CRM.email",
"activityid": "8b9cc8c0-8c08-46cf-a5c3-00057edc8e4e"}
}
```

**Response**

```http
HTTP/1.1 200 OK
{
  "@odata.context": "[Organization Uri]/api/data/v9.1/$metadata#Microsoft.Dynamics.CRM.RollbackRetainResponse",
  "EntityCountCollection": {
      "Count": 3,
      "IsReadOnly": false,
      "Keys": [
          "activityparty",
          "activitypointer",
          "email"
      ],
      "Values": [
          2,
          1,
          1
      ]
  }
}
```

## Purge of retained record
Platform calls *PurgeRetainedContent* to delete the rows which are successfully moved to data lake. PurgeRetainedContent internal calls the *Delete* method to delete the retained table rows which are successfully moved to data lake.     

You can optionally add a custom plugin to *PurgeRetainedContent* message, if you need any custom logic during the purge operation at the table label. Optionally You can also  modify or create custom plugin for *Delete* message if you need a specific custom logic when record gets deleted due to retention. You can identify whether the delete happened due to retention or not by checking the ParentContext. ParentContext for the Delete API due to retention would be *PurgeRetainedContent*. 

Below is the sample code for custom plugin for the delete due to retention. 

### [Sample Plugin](#tab/sdk)

```csharp
class SampleRetentionDeletePlugin : IPlugin
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
        var currentContext = GetPluginContext(serviceProvider);

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

    private IPluginExecutionContext GetPluginContext(IServiceProvider serviceProvider)
    {
        return (IPluginExecutionContext)serviceProvider.GetService(typeof(IPluginExecutionContext));
    }
}
```

---

### See also

[Manage data retention policies](../../maker/data-platform/data-retention-manage.md)  
[View long term retained data](../../maker/data-platform/data-retention-view.md)  
[Delete data in bulk](delete-data-bulk.md)  
[Use the Microsoft Dataverse Web API](webapi/overview.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
