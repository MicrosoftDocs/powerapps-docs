---
title: Bulk Operation messages (preview)
description: Learn how to use special APIs to perform operations on multiple rows of data. These API provide performance benefits compared to other options. 
ms.date: 07/21/2023
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

Use the following bulk operation messages get the best performance when performing data operations on multiple rows of data in a table:

|Message |Details|
|---------|---------|
|`CreateMultiple`|Use the SDK [CreateMultipleRequest class](xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest) or the Web API `CreateMultiple` action to create multiple records of the same type in a single request.|
|`UpdateMultiple`|Use the SDK [UpdateMultipleRequest class](xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest) or the Web API `UpdateMultiple` action to update multiple records of the same type in a single request.|
|`UpsertMultiple`|*Coming soon*|
|`DeleteMultiple`|For elastic tables only. Use the SDK [OrganizationRequest class](xref:Microsoft.Xrm.Sdk.OrganizationRequest) to delete multiple records of the same type. This message isn't available in the Web API yet.|

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

The number of records you should include with each request is different depending on whether you are using standard or elastic tables.

#### Number of records with standard tables

Bulk operations with standard tables are optimized to perform operations on multiple rows within a single transaction. Operations become more efficient, and therefore more performant overall, as the number of operations per request increases. This also allows for any plug-in steps registered for the bulk operation to be more efficient. Each time a plug-in is invoked for a single operation, some milliseconds are required to invoke the plug-in class containing the logic. When a plug-in is registered for a bulk operation message, the class is invoked once and can process all the operations more efficiently. More information: [Write plug-ins for CreateMultiple and UpdateMultiple (Preview)](write-plugin-multiple-operation.md)

This performance benefit gives you an incentive to send the largest number of records you can in each request. However, as the number of records increases, the size of the request becomes larger and takes longer to process and you will encounter limits. If you hit these limits, the entire operation will fail. There is no set limit on the number of records to send. You will need to experiment to find the best number. Generally, we expect that 1000 records per request is a reasonable place to start if the size of the record data is small and there are no plug-ins. The kinds of errors you may encounter can usually be addressed by sending fewer records with each request. We recommend that you include the ability to configure the number of entities sent so you can adapt by sending fewer. More information: [Message size and time limits](#message-size-and-time-limits)

#### Number of records with elastic tables

Because there is no transaction with elastic tables, there is no performance benefit in trying to send the largest number per request. We recommend sending 100 operations per request and sending requests in parallel to achieve maximum throughput.

> [!TIP]
> Both standard and elastic tables have greater throughput when you use bulk operation messages in parallel. More information: [Send parallel requests](send-parallel-requests.md)

### On Error behavior

The behavior when errors occur is different depending on whether you are using standard or elastic tables.

#### On Error behavior with standard tables

Any error that occurs within a bulk operation with a standard table will cause the entire operation to rollback. You should only use bulk operations with standard tables when you have a high degree of confidence that all the operations will succeed. You may want to use a strategy that allows the set of operations to fall back to use the SDK [ExecuteMultipleRequest class](xref:Microsoft.Xrm.Sdk.Messages.ExecuteMultipleRequest) or Web API `$batch` if the bulk operation fails. If the success rate for your initial try is low, this strategy will result in worse performance. Only use this fall back strategy when most operations are expected to succeed.

#### On Error behavior with elastic tables

With elastic tables a bulk operation may partially succeed and you can detect which records have failed from the error details.

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

Bulk operation message availability is different depending on whether you are using standard or elastic tables. All elastic tables support the `CreateMultiple`, `UpdateMultiple`, and `DeleteMultiple` messages.

#### Availability with standard tables

You can use the `CreateMultiple` and `UpdateMultiple` bulk operation messages for custom tables and most common tables.

You can test whether individual standard tables support these messages today using the examples below.

##### [SDK for .NET](#tab/sdk)

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

##### [Web API](#tab/webapi)

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

### DeleteMultiple

At this time, `DeleteMultiple` is supported only for elastic tables because elastic tables don't support [table relationship cascading behavior](configure-entity-relationship-cascading-behavior.md). Relationship cascading behavior can result in unpredictable execution times for delete operations. If you use `DeleteMultiple` on a standard table you will get the error `DeleteMultiple has not yet been implemented.`

For standard tables, we recommend using the SDK [BulkDeleteRequest class](xref:Microsoft.Crm.Sdk.Messages.BulkDeleteRequest) or Web API [BulkDelete action](xref:Microsoft.Dynamics.CRM.BulkDelete), that enables asynchronous deletion of records that match a query. More information: [Delete data in bulk](delete-data-bulk.md)

With elastic tables, the `DeleteMultiple` message is not yet available for use with the Web API and the SDK doesn't include a `DeleteMultipleRequest` class. Until these are available, use the SDK [OrganizationRequest class](xref:Microsoft.Xrm.Sdk.OrganizationRequest) to delete multiple records of the same type.



## Message pipelines merged

Each of the bulk operation messages has a corresponding single message: `Create`, `Update`, `Upsert`, and `Delete`. These messages have existed for a long time and many people have customized logic that depends on the events that occur when these messages are used.

A key requirement for these bulk operation messages is that people must not be required to maintain this logic in two different places. In order to have the same custom logic and maintain that logic in a single place, we've *merged* the message processing pipelines for these messages. What does this mean?

- When the bulk operation messages are used, the respective `Create` and `Update` events occur for each [Entity](xref:Microsoft.Xrm.Sdk.Entity) instance in the `Targets` parameter. Any existing plug-ins or other event handlers for the corresponding single events continue to work as they always have.

   This means you aren't required to write new plug-ins to manage events raised by these messages.

- When the single operation messages are used, the respective bulk operation events occur with an [EntityCollection](xref:Microsoft.Xrm.Sdk.EntityCollection) containing a *single* [Entity](xref:Microsoft.Xrm.Sdk.Entity) instance passed in the `Targets` parameter.

   This means you can move any existing logic that currently responds to single operation events to the more efficient bulk operation events and the logic is applied for both single and multiple operations.

Before the introduction of bulk operation messages, all custom logic has been on the single operation messages. That logic must continue to be applied when client applications use the bulk operation messages.

With the introduction of the bulk operation messages, for tables used with high-volume bulk operations, we recommend that you begin to move any existing synchronous logic from single message events to bulk operation events. If you're introducing new logic, use the bulk operation events rather than the single operation events.

> [!CAUTION]
> With this design there is potential for duplicate logic to be applied on both the single and multiple versions of events for the operations. Dataverse does not try to prevent this because we cannot know your intent.
>
> It is the plug-in developer's responsibility to make sure that the same logic applied for the single version of events is migrated to the multiple version of the event *and removed* from the single version of the event. Otherwise, the logic will be applied twice.

More information: [Write plug-ins for CreateMultiple and UpdateMultiple (Preview)](write-plugin-multiple-operation.md)

## Limitations

Keep the following limitations in mind when using bulk operation messages.

### Message size and time limits

As mentioned in [Number of records](#number-of-records), with standard tables there is a performance incentive to send more records with each request. However, the number of records you can send is limited by the size of the payload and the amount of time required to process the operation.

#### Message size limits

When you have a plug-in registered for any message, you may encounter the [Message size exceeded when sending context to Sandbox](/troubleshoot/power-platform/power-apps/dataverse/dataverse-plug-ins-errors#error-message-size-exceeded-when-sending-context-to-sandbox) error when the total size of the request exceeds 116.85 MB. With bulk operation messages, it's more likely to hit this limit as you send larger payloads.

This error doesn't occur if there's no plug-in registered for the event. You can avoid this error by disabling the plugin(s) or by sending your request with the `BypassCustomPluginExecution` optional parameter. More information: [Bypass Custom Business Logic](bypass-custom-business-logic.md)

#### Time limits

If you're using the Dataverse [ServiceClient](xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient), you may encounter this error `The request channel timed out attempting to send after 00:04:00. Increase the timeout value passed to the call to Request or increase the SendTimeout value on the Binding. The time allotted to this operation may have been a portion of a longer timeout.`

The default timeout set using ServiceClient is 4 minutes, which is long for any synchronous operation. You can change this using the static [ServiceClient.MaxConnectionTimeout](xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient.MaxConnectionTimeout) property. The default timeout using [CrmServiceClient](xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient) is 2 minutes.

> [!NOTE]
> Before you increase the time limits, you should consider reducing the number of records passed in the `Targets` parameter.

### Not supported for use in Plug-ins

At this time, we don't support using bulk operation messages within plug-ins. More information: [Do not use batch request types in plug-ins and workflow activities](best-practices/business-logic/avoid-batch-requests-plugin.md)

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

No. There are no plans to change `Retrieve` and `RetrieveMultiple` message behavior. Attempting to merge the message pipeline for these messages would be highly problematic because these have been separate messages for many years and developers have always needed to maintain logic for them separately. Also, we discourage applying custom logic for these messages due to the impact they can have on performance. More information: [Limit the registration of plug-ins for Retrieve and RetrieveMultiple messages](best-practices/business-logic/limit-registration-plugins-retrieve-retrievemultiple.md)

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
[Sample: SDK for .NET Use CreateMultiple and UpdateMultiple (preview)](org-service/samples/create-update-multiple.md)   
[Sample: Web API Use CreateMultiple and UpdateMultiple (preview)](webapi/samples/create-update-multiple.md)   
[Sample: CreateMultiple and UpdateMultiple plug-ins](org-service/samples/createmultiple-updatemultiple-plugin.md)   
[Use messages with the Organization service](org-service/use-messages.md)   