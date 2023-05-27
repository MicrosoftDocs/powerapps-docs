---
title: "Use CreateMultiple and UpdateMultiple (Microsoft Dataverse) (preview) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "You can use the CreateMultiple and UpdateMultiple messages to optimize bulk data operations." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 05/26/2023
author: divkamath
ms.author: dikamath
ms.reviewer: jdaly
ms.topic: article
contributors:
 - JimDaly
 - phecke
---

# Use CreateMultiple and UpdateMultiple (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../../includes/cc-beta-prerelease-disclaimer.md)]

> [!IMPORTANT]
> This is a preview feature.
> 
> [!INCLUDE [cc-preview-features-definition](../../../includes/cc-preview-features-definition.md)]
> 
> This article describes how `CreateMultiple` and `UpdateMultiple` messages are used for standard tables. These messages are also used by elastic tables, and the behavior can be different. See [Bulk operations with elastic tables (Preview)](../bulk-operations-elastic-tables.md) for more information about using these messages, as well as `DeleteMultiple`.

The `CreateMultiple` and `UpdateMultiple` messages are optimized for performance when performing multiple create or update operations on the same table. This optimization is useful in cases where you're loading or updating records in bulk.

## Usage

The .NET SDK classes to use these messages are just like the individual operation classes, except they support multiple entities to be passed in their respective request properties.

|Message Name|Request Class|Response Class|
|---------|---------|---------|
|`Create`|[CreateRequest](xref:Microsoft.Xrm.Sdk.Messages.CreateRequest)<br/>Property:[Target](xref:Microsoft.Xrm.Sdk.Messages.CreateRequest.Target)|[CreateResponse](xref:Microsoft.Xrm.Sdk.Messages.CreateResponse)<br/>Property:[id](xref:Microsoft.Xrm.Sdk.Messages.CreateResponse.id)|
|`CreateMultiple`|[CreateMultipleRequest](xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest)<br/>Property:[Targets](xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest.Targets)|[CreateMultipleResponse](xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleResponse)<br />Property:[Ids](xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleResponse.Ids)|
|`Update`|[UpdateRequest](xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest)<br/>Properties:<br/>- [Target](xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest.Target)<br />- [ConcurrencyBehavior](xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest.ConcurrencyBehavior)|[UpdateResponse](xref:Microsoft.Xrm.Sdk.Messages.UpdateResponse)|
|`UpdateMultiple`|[UpdateMultipleRequest](xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest)<br/>Properties:<br/>- [Targets](xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest.Targets)<br />- [ConcurrencyBehavior](xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest.ConcurrencyBehavior)|[UpdateMultipleResponse](xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleResponse)|

As with all Dataverse messages, use the [IOrganizationService.Execute](xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute(Microsoft.Xrm.Sdk.OrganizationRequest)) method to send the request, and the response type is returned. More information: [Use messages with the Organization service](use-messages.md)

## Performance improvements

Using standard tables with `CreateMultiple` and `UpdateMultiple`, operations become more efficient and performant as the number of records passed with the `Targets` parameter increases.

Consider this: If you create a *single* record using `Create` or `CreateMultiple`, the result is exactly the same. The same is true for `Update` and `UpdateMultiple`. Not only is the result the same, the performance is the same as well. `CreateMultiple` and `UpdateMultiple` provide greater efficiency and performance benefits as the number of records included in the `Targets` property increases.

With standard tables, performance is improved because these messages apply the data operations in a single transaction against multiple rows in the table rather than as separate operations on individual rows. This design also enables improving performance by writing plug-ins that respond to these messages more efficiently than plug-ins that respond to individual `Create` or `Update` events. 

Each time a plug-in is invoked, some milliseconds are required to invoke the plug-in class containing the logic. For plug-ins registered for synchronous `Create` or `Update` steps, this invocation adds time to each individual operation. When a plug-in is registered on `CreateMultiple` and `UpdateMultiple` events, the plug-in class is invoked once and can process all the records with greater efficiency. More information: [Write plug-ins for CreateMultiple and UpdateMultiple (Preview)](../write-plugin-multiple-operation.md)

## Message pipelines merged

As mentioned above, creating or updating a single record using the single or multiple version of the operation has the same result and performance characteristics. It must also have the same custom logic applied to it. Developers must not be required to maintain this logic in two different places. In order to have the same custom logic and maintain that logic in a single place, we've *merged* the message processing pipelines for these messages. What does this mean?

- When `CreateMultiple` and `UpdateMultiple` messages are used, the respective `Create` and `Update` events occur for each [Entity](xref:Microsoft.Xrm.Sdk.Entity) instance in the `Targets` parameter. Any existing plug-ins or other event handlers for the `Create` and `Update` events continue to work as they always have.

   You aren't required to write new plug-ins to manage events raised by these messages.

- When `Create` and `Update` messages are used, the respective `CreateMultiple` and `UpdateMultiple` events occur with an [EntityCollection](xref:Microsoft.Xrm.Sdk.EntityCollection) containing a *single* [Entity](xref:Microsoft.Xrm.Sdk.Entity) instance passed in the `Targets` parameter.

   You can move any existing logic that currently responds to individual `Create` and `Update` events to the more efficient `CreateMultiple` and `UpdateMultiple` events and the logic is applied for both single and multiple operations.

Before the introduction of `CreateMultiple` and `UpdateMultiple`, all custom logic has been on the `Create` or `Update` messages. That logic must continue to be applied when client applications use the `CreateMultiple` and `UpdateMultiple` messages.

With the introduction of the `CreateMultiple` and `UpdateMultiple` messages, for tables used with high-volume bulk operations, we recommend that you begin to move any existing synchronous logic from `Create` and `Update` events to `CreateMultiple` and `UpdateMultiple` events. If you're introducing new logic, use the `CreateMultiple` and `UpdateMultiple` events rather than `Create` and `Update`.

> [!CAUTION]
> With this design there is potential for duplicate logic to be applied on both the single and multiple versions of events for the operations. Dataverse does not try to prevent this because we cannot know your intent.
>
> It is the plug-in developer's responsibility to make sure that the same logic applied for the single version of events is migrated to the multiple version of the event *and removed* from the single version of the event. Otherwise, the logic will be applied twice.

More information: [Write plug-ins for CreateMultiple and UpdateMultiple (Preview)](../write-plugin-multiple-operation.md)

## Limitations

Keep these limitations in mind when using `CreateMultiple` and `UpdateMultiple` messages.

### Limited to certain standard tables

Currently, `CreateMultiple` and `UpdateMultiple` messages aren't available for all standard tables. These messages will be enabled for all standard tables that support individual `Create` and `Update` messages in the coming months.

> [!NOTE]
> All elastic tables support these messages.

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

### Message size and time limits

With standard tables, the efficiency gained per operation using `CreateMultiple` and `UpdateMultiple` messages increases with the number of entities included in the `Targets` parameter, so there's incentive to try to use the largest possible number with projects that perform bulk operations.

There's currently no set limit on the number of entities you might try to send with your requests. If you send too many records in a single request, the entire request fails. You need to experiment to find the best number. Generally, we expect that 1000 entities per request is a reasonable place to start if the size of the record data is small and there are no plug-ins. The kinds of errors you may encounter can usually be addressed by sending fewer entities with each request. We recommend you include the ability to configure the number of entities sent so that you can adapt by sending fewer.

#### Message size limits

When you have a plug-in registered for any message, you may encounter the [Message size exceeded when sending context to Sandbox](../troubleshoot-plug-in.md#error-message-size-exceeded-when-sending-context-to-sandbox) error when the total size of the request exceeds 116.85 MB. With `CreateMultiple` and `UpdateMultiple`, it's more likely to hit this limit as you send larger payloads.

This error doesn't occur if there's no plug-in registered for the event. You can avoid this error by disabling the plugin(s) or by sending your request with the `BypassCustomPluginExecution` optional parameter. More information: [Bypass Custom Business Logic](../bypass-custom-business-logic.md)

#### Time limits

If you're using the Dataverse [ServiceClient](xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient), you may encounter this error `The request channel timed out attempting to send after 00:04:00. Increase the timeout value passed to the call to Request or increase the SendTimeout value on the Binding. The time allotted to this operation may have been a portion of a longer timeout.`

The default timeout set using ServiceClient is 4 minutes, which is long for any synchronous operation. You can change this using the static [ServiceClient.MaxConnectionTimeout](xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient.MaxConnectionTimeout) property. The default timeout using [CrmServiceClient](xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient) is 2 minutes.

> [!NOTE]
> Before you increase the time limits, you should consider reducing the number of entities passed in the `Targets` parameter.

### No continue on error

The `ExecuteMultiple` message supports the option that continues processing requests even when one or more requests fail. Because `CreateMultiple` and `UpdateMultiple` messages with standard tables achieve performance improvements by unifying all operations in a single transaction, it isn't possible to support the continue-on-error behaviors.

> [!NOTE]
> Elastic tables do not have transactions, so partial success is possible. More information: [Bulk operations with elastic tables (Preview)](../bulk-operations-elastic-tables.md)

You should use `CreateMultiple` and `UpdateMultiple` messages with standard tables when you have a high degree of confidence that all the operations will succeed. You may want to use a strategy that allows the set of operations to fall back to use `ExecuteMultiple` if `CreateMultiple` and `UpdateMultiple` messages fail. If the success rate for your initial try is low, this strategy will result in worse performance. Only use this fall back strategy when most operations are expected to succeed.

### .NET SDK only

Currently the `CreateMultiple` and `UpdateMultiple` messages are only available to be used with the .NET SDK. The capability to use these operations using Web API is coming soon.

### Not supported for use in Plug-ins

At this time, we don't support using `CreateMultiple` or `UpdateMultiple` within plug-ins. More information: [Do not use batch request types in plug-ins and workflow activities](../best-practices/business-logic/avoid-batch-requests-plugin.md)

## Known issues

The following are known issues that will be addressed before this feature becomes generally available.

### UpdateMultipleRequest.ConcurrencyBehavior not working

<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest.ConcurrencyBehavior> specifies the type of optimistic concurrency behavior that should be applied. Possible values are `AlwaysOverwrite`, `Default`, and `IfRowVersionMatches`.

Currently the `Default` option is always applied regardless of what you set. The behavior depends on whether [EntityMetadata.IsOptimisticConcurrencyEnabled](xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.IsOptimisticConcurrencyEnabled) is set for the table.

More information: [ConcurrencyBehavior Enum](xref:Microsoft.Xrm.Sdk.ConcurrencyBehavior)


## Frequently Asked Questions

The following are frequently asked question related to the introduction of these messages.

> [!NOTE]
> If you haven't found answers to questions you have about using `CreateMultiple` and `UpdateMultiple` in this article, please use the button at the bottom of this article to **Submit and view feedback for This Page**. You will need a GitHub account to submit feedback.

### Will there be an UpsertMultiple?

Yes. We plan to release `UpsertMultiple` later.

### Will there be a DeleteMultiple?

At this time, `DeleteMultiple` is supported only for elastic tables, which is a preview feature. Elastic tables don't support cascading operations. More information: [Bulk operations with elastic tables (Preview)](../bulk-operations-elastic-tables.md)  

For standard tables, cascading operations can result in unpredictable execution times. If we support `DeleteMultiple` for standard tables, it may not be the best choice. For standard tables, we recommend the `BulkDelete` message that enables asynchronous deletion of records that match a query.

### Will Retrieve and RetrieveMultiple logic be merged?

No. There are no plans to change `Retrieve` and `RetrieveMultiple` message behavior. Attempting to merge the message pipeline for these messages would be highly problematic because these have been separate messages for many years and developers have always needed to maintain logic for them separately. Also, we discourage applying custom logic for these messages due to the impact they can have on performance. More information: [Limit the registration of plug-ins for Retrieve and RetrieveMultiple messages](../best-practices/business-logic/limit-registration-plugins-retrieve-retrievemultiple.md)

### How are API limits applied?

There are two kinds of API limits:

[!INCLUDE [cc-api-limits-summary-table](../../../includes/cc-api-limits-summary-table.md)]

#### Service Protection limits

As described in [Service protection API limits](../api-limits.md), limits have three facets. Two of these limits are evaluated on a 5-minute sliding window and apply when using these messages.

- **Number of requests**: Each `CreateMultiple` and `UpdateMultiple` request counts as single request that accrues to the limit of 6000 requests per user, per server, during the 5-minute window. Because these requests group individual operations, the likelihood of hitting this limit is reduced.
- **Execution time**: Because each `CreateMultiple` and `UpdateMultiple` typically request takes longer, and if you're sending requests in parallel, you're more likely to hit the execution time limit that is 20 minutes per user, per server, during the 5-minute window. More information: [Send parallel requests](../send-parallel-requests.md)

#### Power Platform Request (API Entitlement) limits

These limits are based on data changes, so each item included in the `Targets` parameter of a `CreateMultiple` and `UpdateMultiple` request accrue to this limit. These messages don't provide a means to bypass these limits.

### See Also

[Write plug-ins for CreateMultiple and UpdateMultiple](../write-plugin-multiple-operation.md)<br />
[Sample: Use CreateMultiple and UpdateMultiple](samples/create-update-multiple.md)<br />
[Sample: CreateMultiple and UpdateMultiple plug-ins](samples/createmultiple-updatemultiple-plugin.md)<br />
[Use messages with the Organization service](use-messages.md)<br />
[Bulk operations with elastic tables (Preview)](../bulk-operations-elastic-tables.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
