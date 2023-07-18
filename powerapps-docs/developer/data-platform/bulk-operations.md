---
title: Bulk Operation messages (preview)
description: Learn how to use special APIs to perform operations on multiple rows of data. These API provide performance benefits compared to other options. 
ms.date: 04/03/2022
author: divkamath
ms.author: dikamath
ms.reviewer: jdaly
ms.topic: conceptual
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
contributors:
 - JimDaly
---
# Bulk Operation messages (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

> [!IMPORTANT]
> This is a preview feature.
> 
> [!INCLUDE [cc-preview-features-definition](../../includes/cc-preview-features-definition.md)]

Use the following bulk operations messages get the best performance when performing data operations on multiple rows of data:

|Message |Details|
|---------|---------|
|`CreateMultiple`|Use the SDK [CreateMultipleRequest class](xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest) or the Web API `CreateMultiple` action to create multiple records of the same type in a single request.|
|`UpdateMultiple`|Use the SDK [UpdateMultipleRequest class](xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest) or the Web API `UpdateMultiple` action to update multiple records of the same type in a single request.|
|`UpsertMultiple`|*Coming soon*|
|`DeleteMultiple`|For elastic tables only, use the SDK [OrganizationRequest class](xref:Microsoft.Xrm.Sdk.OrganizationRequest) to delete multiple records of the same type. This message isn't available in the Web API yet.|

## Standard and Elastic table usage

Both standard and elastic tables see significant performance benefits when using these bulk operation messages, but you need to use them differently. The following table summarizes the differences.

||Standard|Elastic|
|---------|---------|---------|
|**[Number of records](#number-of-records)**|Operations are more efficient with larger number of records. There is no set limit, but there are message size and time limits.|Recommend sending 100 records at a time.|
|**[On Error behavior](#on-error-behavior)**|All operations rollback on error.|Partial success is possible.|
|**[Availability](#availability)**|Not all standard tables support these messages.|Messages available for all elastic tables.|
|**[DeleteMultiple](#deletemultiple)**|Not available. Use the SDK [BulkDeleteRequest class](xref:Microsoft.Crm.Sdk.Messages.BulkDeleteRequest) or the Web API [BulkDelete action](xref:Microsoft.Dynamics.CRM.BulkDelete) instead.|Available using SDK [OrganizationRequest class](xref:Microsoft.Xrm.Sdk.OrganizationRequest) .|

Standard and elastic table usage is different because standard tables use Azure SQL and support transactions. Elastic tables use Azure Cosmos DB, which doesn't support transactions but is able to handle large amounts of data an high levels of throughput with low latency. The following sections provide more details.

### Number of records

**With standard tables**, bulk operations are optimized to perform operations on multiple rows within a single transaction. Operations become more efficient, and therefore more performant overall, as the number of operations per request increases. This also allows for any plug-in steps registered for the bulk operation to be more efficient. Each time a plug-in is invoked for a single operation, some milliseconds are required to invoke the plug-in class containing the logic. When a plug-in is registered for a bulk operation message, the class is invoked once and can process all the operations more efficiently. More information: [Write plug-ins for CreateMultiple and UpdateMultiple (Preview)](write-plugin-multiple-operation.md)

This performance benefit gives you an incentive to send the largest number of records you can in each request. However, as the number of records increases, the size of the request becomes larger and takes longer to process and you will encounter limits. If you hit these limits, the entire operation will fail. There is no set limit on the number of records to send. You will need to experiment to find the best number. Generally, we expect that 1000 records per request is a reasonable place to start if the size of the record data is small and there are no plug-ins. The kinds of errors you may encounter can usually be addressed by sending fewer records with each request. We recommend that you include the ability to configure the number of entities sent so you can adapt by sending fewer.

**With elastic tables**, there is no transaction, so there is no performance benefit in trying to send the largest number per request. We recommend sending 100 operations per request and sending requests in parallel to achieve maximum throughput.

> [!TIP]
> Both standard and elastic tables have greater throughput when you use bulk operation messages in parallel. More information: [Send parallel requests](send-parallel-requests.md)

### On Error behavior

**With standard tables**, any error that occurs within a bulk operation will cause the entire operation to rollback. You should only use bulk operations with standard tables when you have a high degree of confidence that all the operations will succeed. You may want to use a strategy that allows the set of operations to fall back to use the SDK [ExecuteMultipleRequest class](xref:Microsoft.Xrm.Sdk.Messages.ExecuteMultipleRequest) or Web API `$batch` if the bulk operation fails. If the success rate for your initial try is low, this strategy will result in worse performance. Only use this fall back strategy when most operations are expected to succeed.

**With elastic tables**, a bulk operation may partially succeed and you can detect which records have failed from the error details.

# [SDK for .NET](#tab/sdk)

When you use the SDK to perform a bulk operation with an elastic table, a [FaultException](xref:System.ServiceModel.FaultException%601) of type [OrganizationServiceFault](xref:Microsoft.Xrm.Sdk.OrganizationServiceFault) is thrown if a failure occurs. You can get the status of each record using the following code.

```csharp
if (ex.Detail.ErrorDetails.TryGetValue("Plugin.BulkApiErrorDetails", out object errorDetails))
{
   List<BulkApiErrorDetail> bulkApiErrorDetails = JsonConvert.DeserializeObject<List<BulkApiErrorDetail>>(errorDetails.ToString());
}

public class BulkApiErrorDetail
{
   public int RequestIndex { get; set; }
   public string Id { get; set; }
   public int StatusCode { get; set; }
}
```

# [Web API](#tab/webapi)

When using Web API to perform a bulk operation with an elastic table, you need to pass the `Prefer` header with value `odata.include-annotations=*` or `odata.include-annotations=Microsoft.PowerApps.CDS.ErrorDetails.*`, which gives the status of each record. More information: [Include more details with errors](webapi/compose-http-requests-handle-errors.md#include-more-details-with-errors)

---
### Availability

**With standard tables**, you can use the `CreateMultiple` and `UpdateMultiple` bulk operation messages for all tables that support the `Create` and `Update` messages except the following:

Account, Contact, ... TBD

You can test whether individual standard tables support these messages today using the examples below.

#### [SDK for .NET](#tab/sdk)

Use this static method to detect whether a given table supports any specific named message, including `CreateMultiple` or `UpdateMultiple`.

```csharp
/// <summary>
/// Detect whether a specified message is supported for the specified table.
/// </summary>
/// <param name="service">The IOrganizationService instance.</param>
/// <param name="entityLogicalName">The logical name of the table.</param>
/// <param name="messageName">The name of the message.</param>
/// <returns></returns>
public static bool IsMessageAvailable(
    IOrganizationService service,
    string entityLogicalName,
    string messageName)
{
    QueryExpression query = new("sdkmessagefilter")
    {
        ColumnSet = new ColumnSet("sdkmessagefilterid"),
        Criteria = new FilterExpression(LogicalOperator.And)
        {
            Conditions = {
            new ConditionExpression(
                attributeName:"primaryobjecttypecode",
                conditionOperator: ConditionOperator.Equal,
                value: entityLogicalName)
            }
        },
        LinkEntities = {
            new LinkEntity(
                linkFromEntityName:"sdkmessagefilter",
                linkToEntityName:"sdkmessage",
                linkFromAttributeName:"sdkmessageid",
                linkToAttributeName:"sdkmessageid",
                joinOperator: JoinOperator.Inner)
            {
                    LinkCriteria = new FilterExpression(LogicalOperator.And){
                    Conditions = {
                        new ConditionExpression(
                            attributeName:"name",
                            conditionOperator: ConditionOperator.Equal,
                            value: messageName)
                        }
                    }
            }
        }
    };

    EntityCollection entityCollection = service.RetrieveMultiple(query);

    return entityCollection.Entities.Count.Equals(1);
}
```

#### [Web API](#tab/webapi)

Use the following `GET` request to detect whether a message is available for a table. The request below tests whether the `sample_example` table supports the `CreateMultiple` message.  Replace the `@message` and `@table` parameter values for the message and table you want to test.

**Request**

```http
GET [Organization Uri]/api/data/v9.2/sdkmessagefilters?$select=sdkmessagefilterid&$filter=sdkmessageid/name eq @message and primaryobjecttypecode eq @table&@message='CreateMultiple'&@table='sample_example' HTTP/1.1
Content-Type: application/json
```

When the table supports the message, an `sdkmessagefilterid` value is returned. If it isn't supported, the `value` is an empty array.

**Response**

```http
HTTP/1.1 200 OK
Content-Type: application/json; odata.metadata=minimal
OData-Version: 4.0

{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#sdkmessagefilters(sdkmessagefilterid)",
    "value": [
        {
            "@odata.etag": "W/\"2009110\"",
            "sdkmessagefilterid": "f9bedb46-856e-ed11-9561-002248081470"
        }
    ]
}
```

---

**With elastic tables**, all tables support bulk operations.

## DeleteMultiple

At this time, `DeleteMultiple` is supported only for elastic tables because elastic tables don't support [table relationship cascading behavior](configure-entity-relationship-cascading-behavior.md).

**With standard tables**, relationship cascading behavior can result in unpredictable execution times. If we support `DeleteMultiple` for standard tables, it may not be the best choice. For standard tables, we recommend using the SDK [BulkDeleteRequest class](xref:Microsoft.Crm.Sdk.Messages.BulkDeleteRequest) or Web API [BulkDelete action](xref:Microsoft.Dynamics.CRM.BulkDelete), that enables asynchronous deletion of records that match a query.

**With elastic tables**, the `DeleteMultiple` message is not available for use with the Web API and the SDK doesn't include a DeleteMultipleRequest class. Use the SDK [OrganizationRequest class](xref:Microsoft.Xrm.Sdk.OrganizationRequest) to delete multiple records of the same type.

## Message pipelines merged

## Limitations

### Message size and time limits

### Not supported for use in Plug-ins

## Known issues

The following are known issues that will be addressed before this feature becomes generally available.

### UpdateMultipleRequest.ConcurrencyBehavior not working

<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest.ConcurrencyBehavior> specifies the type of optimistic concurrency behavior that should be applied. Possible values are `AlwaysOverwrite`, `Default`, and `IfRowVersionMatches`.

Currently the `Default` option is always applied regardless of what you set. The behavior depends on whether [EntityMetadata.IsOptimisticConcurrencyEnabled](xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.IsOptimisticConcurrencyEnabled) is set for the table.

More information: [ConcurrencyBehavior Enum](xref:Microsoft.Xrm.Sdk.ConcurrencyBehavior)


## Frequently Asked Questions (FAQ)

The following are frequently asked question related to the introduction of these messages.

> [!NOTE]
> If you haven't found answers to questions you have about using bulk operation messages in this article, please use the button at the bottom of this article to **Submit and view feedback for This Page**. You will need a GitHub account to submit feedback.

### Will Retrieve and RetrieveMultiple logic be merged?

No. There are no plans to change `Retrieve` and `RetrieveMultiple` message behavior. Attempting to merge the message pipeline for these messages would be highly problematic because these have been separate messages for many years and developers have always needed to maintain logic for them separately. Also, we discourage applying custom logic for these messages due to the impact they can have on performance. More information: [Limit the registration of plug-ins for Retrieve and RetrieveMultiple messages](../best-practices/business-logic/limit-registration-plugins-retrieve-retrievemultiple.md)

### How are API limits applied?

There are two types of API limits. The bulk operation messages do not provide any way to bypass either of these limits.

#### Service Protection limits

As described in [Service protection API limits](api-limits.md), limits have three facets. Two of these limits are evaluated on a 5-minute sliding window and apply when using these messages.

- **Number of requests**: Each bulk operation message counts as single request that accrues to the limit of 6000 requests per user, per server, during the 5-minute window. Because these requests group individual operations, *the likelihood of hitting this limit is reduced*.
- **Execution time**: Because each bulk operation message typically request takes longer, and if you're sending requests in parallel, *you're more likely to hit the execution time limit* that is 20 minutes per user, per server, during the 5-minute window.

#### Power Platform Request (API Entitlement) limits

These limits are based on data changes, so each item included in the `Targets` parameter of a bulk operation request accrue to this limit. More information: [Requests limits and allocations](/power-platform/admin/api-request-limits-allocations)

### See also

[Elastic tables (preview)](elastic-tables.md)   
[Write plug-ins for CreateMultiple and UpdateMultiple (Preview)](write-plugin-multiple-operation.md)   
[Sample: Use CreateMultiple and UpdateMultiple (preview)](org-service/samples/create-update-multiple.md)   
[Sample: CreateMultiple and UpdateMultiple plug-ins](org-service/samples/createmultiple-updatemultiple-plugin.md)   
[Use messages with the Organization service](use-messages.md)  