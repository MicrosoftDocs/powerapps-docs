---
title: Delete data in bulk
description: Learn how to use the bulk deletion feature in Microsoft Dataverse to delete data you no longer need, helping to maintain data quality and manage the consumption of system storage.
ms.date: 07/25/2023
ms.topic: how-to
author: mayadumesh
ms.subservice: dataverse-developer
ms.author: mayadu
ms.reviewer: pehecke
search.audienceType: 
  - developer
ms.custom: bap-template
---

# Delete data in bulk

[!INCLUDE [cc-terminology](includes/cc-terminology.md)]

The bulk deletion feature in Microsoft Dataverse helps you to maintain data quality and manage the consumption of system storage by deleting data you no longer need. For example, you can delete the following data in bulk:  
  
- Stale data
- Data that's no longer relevant to the business
- Unneeded test or sample data
- Data that was incorrectly imported from other systems
  
And you can perform the following operations:  
  
- Delete data across multiple tables.
- Delete records in a specific table.
- Receive email notifications when a bulk deletion finishes.
- Delete data periodically.
- Schedule the start time of a recurring bulk delete.
- Retrieve information about failures that occurred during a bulk deletion.

To delete multiple rows in elastic tables, you can also use the [`DeleteMultiple` message](use-elastic-tables.md#use-deletemultiple-with-elastic-tables). `DeleteMultiple` deletes records in a single elastic immediately, rather than using a bulk delete job.
  
## Run bulk delete

To delete data in bulk, use the `BulkDelete` message to submit a bulk delete job. With the SDK, use the [BulkDeleteRequest class](xref:Microsoft.Crm.Sdk.Messages.BulkDeleteRequest). With the Web API, use the [BulkDelete action](xref:Microsoft.Dynamics.CRM.BulkDelete). Specify the query expressions that describe the records to delete in the `QuerySet` property of your request.
  
A bulk delete job is represented by a record in the [`Bulk Delete Operation` (`BulkDeleteOperation`) table](reference/entities/bulkdeleteoperation.md). A bulk delete operation record includes the following information:  
  
- The number of records the job deleted
- The number of records the job failed to delete
- Whether the job is set to recur
- The start time of the job
  
The bulk delete job runs asynchronously without blocking other activities. It only deletes records that were created before the job starts to run. The job deletes the specified records according to cascading rules based on [table relationship cascading behavior](configure-entity-relationship-cascading-behavior.md).

If a bulk delete job fails or ends prematurely, any records it deleted aren't rolled back. They remain deleted. A record of failures is stored in the [`Bulk Delete Failure` (`BulkDeleteFailure`) table](reference/entities/bulkdeletefailure.md). You can retrieve information from the table about the error that caused the failure.
  
To run a bulk delete job, you must have `BulkDelete` and `Delete` privileges on the table types being deleted. You must also have read permissions on the table records that are specified in the `QuerySet` property. A system administrator has the necessary permissions by default. Other users must be granted them.
  
You can perform a bulk deletion on all tables that support the `Delete` message.
  
If the delete action on a specific table type triggers a plug-in or a workflow (process), the plug-in or workflow is triggered every time the bulk delete job deletes a table record of that type.
 
## Long-term retained data (preview)

Bulk deletion is also available for long-term retained data. Run a bulk delete as you normally would, but set the query's `DataSource` field to *retained*. 

### [SDK for .NET](#tab/sdk)

With the SDK you can use either <xref:Microsoft.Xrm.Sdk.Query.QueryExpression> or the [FetchXmlToQueryExpressionRequest class](xref:Microsoft.Crm.Sdk.Messages.FetchXmlToQueryExpressionRequest) with [IOrganizationService.Execute](xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute%2A) to convert FetchXml to a <xref:Microsoft.Xrm.Sdk.Query.QueryExpression>.

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
        <fetch version='1.0' output-format='xml-platform' mapping='logical' datasource='retained'>
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

Look at the following Organization service samples for the bulk delete feature:

- [Sample: Bulk delete exported records](org-service/samples/bulk-delete-exported-records.md)   
- [Sample: Bulk delete records that match common criteria](org-service/samples/bulk-delete-records-match-common-criteria.md)

### See also

[Long-term data retention](long-term-retention.md)  
[BulkDeleteOperation Table](reference/entities/bulkdeleteoperation.md)

[!INCLUDE [footer-include](../../includes/footer-banner.md)]
