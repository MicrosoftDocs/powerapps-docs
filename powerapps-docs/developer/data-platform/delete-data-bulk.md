---
title: "Delete data in bulk (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Deleting data in bulk helps maintain data quality and manage the consumption of system storage by deleting data that is no longer needed." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 05/09/2023
ms.reviewer: "pehecke"
ms.topic: "article"
author: "mayadumesh" # GitHub ID
ms.subservice: dataverse-developer
ms.author: "jdaly" # MSFT alias of Microsoft employees only
search.audienceType: 
  - developer
---

# Delete data in bulk

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

The *bulk deletion* feature helps you to maintain data quality and manage the consumption of system storage in Microsoft Dataverse by deleting data that you no longer need. For example, you can delete the following data in bulk:  
  
- Stale data.  
  
- Data that is irrelevant to the business.  
  
- Unneeded test or sample data.  
  
- Data that is incorrectly imported from other systems.  
  
With bulk deletion, you can perform the following operations:  
  
- Delete data across multiple tables.  
  
- Delete records for a specified table.  
  
- Receive email notifications when a bulk deletion finishes.  
  
- Delete data periodically.  
  
- Schedule the start time of a recurring bulk delete.  
  
- Retrieve the information about the failures that occurred during a bulk deletion.  
  
## Run bulk delete

To delete data in bulk, you have to submit a bulk delete job by using the <xref:Microsoft.Crm.Sdk.Messages.BulkDeleteRequest> message. The bulk delete job runs asynchronously in the background without blocking other activities. The query expressions that describe the records on which to run the bulk delete job are specified in the <xref:Microsoft.Crm.Sdk.Messages.BulkDeleteRequest.QuerySet> property of this request.  
  
 A bulk delete job is represented by the bulk delete operation table. The schema name for this table is `BulkDeleteOperation`. A bulk delete operation record includes the following information:  
  
- Number of records that the bulk delete job deleted.  
  
- Number of records that the bulk delete job failed to delete.  
  
- Whether the bulk delete job is a recurring job or not.  
  
- Start time of the bulk delete job.  
  
  A bulk delete job only deletes records that are created before the job starts to run.  
  
> [!NOTE]
>  If a bulk delete job fails or ends prematurely, any records that were deleted before the failure or ending of the job are not rolled back and remain deleted. The failures of the `BulkDeleteOperation` are stored in the `BulkDeleteFailure` records and can be retrieved by using the <xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest> message or the  <xref:Microsoft.Xrm.Sdk.Messages.RetrieveMultipleRequest> message.  
  
 A bulk delete job deletes the specified records according to the cascading rules. These rules are based on the relationship type between the tables. For more information, see [Table Relationship Behavior](/dynamics365/customer-engagement/developer/entity-relationship-behavior).  
  
 To run a bulk delete job, a user must have the `BulkDelete` and `Delete` privileges for the table types being deleted. The user must also have read permissions to the table records that are specified in the <xref:Microsoft.Crm.Sdk.Messages.BulkDeleteRequest> message. By default, a system administrator has the necessary permissions; however, other users must be granted these permissions.  
  
 You can perform a bulk deletion on all tables that are supported by the delete action. For information about possible actions on table records, see [Actions on table records](/dynamics365/customer-engagement/developer/introduction-entities#ActionsOnEntityRecords).  
  
 If a plug-in or a workflow (process) is triggered by the delete action on a specific table type, it is triggered every time that a table record of this type is deleted by the bulk delete job.  
 
## Long-term retained data
Bulk delete is also available for long-term retained (LTR) data. To run bulk delete against LTR rows (records), run a bulk delete as you normally would against the corresponding table but set the query's `DataSource` field to "retained". There are several ways to do this:

### [SDK for .NET (QueryExpression)](#tab/sdk-queryexpression)
Developers can set the `DataSource` field available in the <xref:Microsoft.Xrm.Sdk.Query.QueryExpression> class to indicate that the query is for retained rows (records) only. This flag marks the bulk delete operation to delete retained data. Set `query.DataSource`= "retained" to bulk delete retained rows only.

```csharp
var bulkDeleteRequest = new BulkDeleteRequest();
bulkDeleteRequest.JobName = "Bulk Delete Retained Accounts";

// Create query and add additional filters as needed
QueryExpression query = new QueryExpression()
{
    EntityName = "account",
};
query.DataSource = "retained";

bulkDeleteRequest.QuerySet = new QueryExpression[]
{
    query
};

bulkDeleteRequest.StartDateTime = DateTime.Now;
bulkDeleteRequest.RecurrencePattern = String.Empty;
bulkDeleteRequest.SendEmailNotification = false;
bulkDeleteRequest.ToRecipients = new Guid[] { };
bulkDeleteRequest.CCRecipients = new Guid[] { };

BulkDeleteResponse bulkDeleteResponse = (BulkDeleteResponse)svc.Execute(bulkDeleteRequest);
```

### [SDK for .NET (FetchXML)](#tab/sdk-fetchxml)
Developers can set the `datasource='retained'` attribute inside a FetchXML expression to indicate that the query is for retained data. This flag marks the bulk delete operation to delete retained rows (records) only.

```csharp
var bulkDeleteRequest = new BulkDeleteRequest();
bulkDeleteRequest.JobName = "Bulk Delete Retained Accounts"

var convert = new FetchXmlToQueryExpressionRequest();
convert.FetchXml = @"
    <fetch version='1.0' output-format='xml-platform' mapping='logical' datasource='retained'>
	<entity name='account'>
	</entity>
    </fetch>";

FetchXmlToQueryExpressionResponse response = (FetchXmlToQueryExpressionResponse)svc.Execute(convert);

bulkDeleteRequest.QuerySet = new QueryExpression[]
{
    response.Query
};

bulkDeleteRequest.StartDateTime = DateTime.Now;
bulkDeleteRequest.RecurrencePattern = String.Empty;
bulkDeleteRequest.SendEmailNotification = false;
bulkDeleteRequest.ToRecipients = new Guid[] { };
bulkDeleteRequest.CCRecipients = new Guid[] { };

BulkDeleteResponse bulkDeleteResponse = (BulkDeleteResponse)svc.Execute(bulkDeleteRequest);
```

### [Web API](#tab/webapi)
Developers can call the <xref:Microsoft.Dynamics.CRM.BulkDelete?displayProperty=nameWithType> action using the Web API.

**Request**

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

**Response**

```http
HTTP/1.1 200 OK
{
    "@odata.context": "https://example.dynamics.com/api/data/v9.1/$metadata#Microsoft.Dynamics.CRM.BulkDeleteResponse",
    "JobId": "3093d67f-21f0-ed11-8b48-6045bdd92a32"
}
```

More information: [Use Web API actions](webapi/use-web-api-actions.md)

---

 
## Samples

Look at the following Organization service samples for the bulk delete feature:

- [Sample: Bulk delete exported records](org-service/samples/bulk-delete-exported-records.md)   
- [Sample: Bulk delete records that match common criteria](org-service/samples/bulk-delete-records-match-common-criteria.md)

### See also

[BulkDeleteOperation Table](reference/entities/bulkdeleteoperation.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
