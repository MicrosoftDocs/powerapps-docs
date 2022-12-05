---
title: "Use CreateMultiple and UpdateMultiple (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "You can use the CreateMultiple and UpdateMultiple messages to optimize bulk data operations." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 12/12/2022
author: divka78
ms.author: dikamath
ms.reviewer: jdaly
ms.topic: article
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
 - JimDaly
 - phecke
---

# Use CreateMultiple and UpdateMultiple (Preview)

The `CreateMultiple` and `UpdateMultiple` messages are unique because they are optimized for performance when performing multiple create or update operations on the same table. This is useful in cases where you are loading or updating records in bulk.

## Usage

The .NET SDK classes to use these messages are just like the individual operation classes, except they support multiple entities to be passed in their respective request properties.

|Message Name|Request Class|Response Class|
|---------|---------|---------|
|`Create`|[CreateRequest](xref:Microsoft.Xrm.Sdk.Messages.CreateRequest)<br/>Property:<br/>[Target](xref:Microsoft.Xrm.Sdk.Messages.CreateRequest.Target)|[CreateResponse](xref:Microsoft.Xrm.Sdk.Messages.CreateResponse)<br/>Property:<br/>[id](xref:Microsoft.Xrm.Sdk.Messages.CreateResponse.id)|
|`CreateMultiple`|[CreateMultipleRequest](/dotnet/api/microsoft.xrm.sdk.messages.createmultiplerequest)<br/>Property:<br/>[Targets](/dotnet/api/microsoft.xrm.sdk.messages.createmultiplerequest.targets)|[CreateMultipleResponse](/dotnet/api/microsoft.xrm.sdk.messages.createmultipleresponse)<br />Property:<br />[Ids](/dotnet/api/microsoft.xrm.sdk.messages.createmultipleresponse.ids)|
|`Update`|[UpdateRequest](xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest)<br/>Properties:<br/>[Target](xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest.Target)<br />[ConcurrencyBehavior](xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest.ConcurrencyBehavior)|[UpdateResponse](xref:Microsoft.Xrm.Sdk.Messages.UpdateResponse)|
|`UpdateMultiple`|[UpdateMultipleRequest](/dotnet/api/microsoft.xrm.sdk.messages.updatemultiplerequest)<br/>Properties:<br/>[Targets](/dotnet/api/microsoft.xrm.sdk.messages.updatemultiplerequest.targets)<br />[ConcurrencyBehavior](/dotnet/api/microsoft.xrm.sdk.messages.updatemultiplerequest.concurrencybehavior)|[UpdateMultipleResponse](/dotnet/api/microsoft.xrm.sdk.messages.updatemultipleresponse)|

As with all Dataverse messages, use the [IOrganizationService.Execute](xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute(Microsoft.Xrm.Sdk.OrganizationRequest)) method to send the request and the response type will be returned.

## Performance improvements

Consider this: If you create a *single* record using `Create` or `CreateMultiple`, the result is exactly the same. The same is true for `Update` and `UpdateMultiple`. Not only is the result the same, the performance is the same as well. `CreateMultiple` and `UpdateMultiple` provide greater efficiency and performance benefits as the number of records included in the `Targets` property increases.

Performance is improved because these messages apply the data operations in a single transaction against multiple rows in the table rather than as separate operations on individual rows. This design also enables improving performance by writing plug-ins that respond to these messages more efficiently than plug-ins that respond to individual create and update events.

Each time a plug-in is invoked, some milliseconds are required to instantiate the plug-in class containing the logic. For plug-ins registered for synchronous `Create` or `Update` steps, this adds time to each individual operation. When a plug-in is registered on `CreateMultiple` and `UpdateMultiple` events, the plug-in class is instantiated once and can process all the operations with greater efficiency.

## Message pipelines merged

As mentioned above, creating or updating a single record using the single or multiple version of the operation has the same result and performance characteristics. It must also have the same custom logic applied to it and developers must not be required to maintain this logic in two different places. In order to achieve this, we have *merged* the message processing pipelines for these messages. What does this mean?

This means:

- When `CreateMultiple` and `UpdateMultiple` messages are used the respective `Create` and `Update` events occur for each [Entity](xref:Microsoft.Xrm.Sdk.Entity) instance in the `Targets` parameter. Any existing plug-ins or other event handlers for the `Create` and `Update` events will continue to work as they always have. You are not required to write new plug-ins to manage events raised by these messages.
- When `Create` and `Update` messages are used, the respective `CreateMultiple` and `UpdateMultiple` events occur with a *single* [Entity](xref:Microsoft.Xrm.Sdk.Entity) instance passed in the `Targets` parameter. You can move any existing logic that currently responds to individual `Create` and `Update` events to the more efficient `CreateMultiple` and `UpdateMultiple` events and the logic will be applied for both single and multiple operations.

Before the introduction of `CreateMultiple` and `UpdateMultiple`, all custom logic has been on the `Create` or `Update` messages. That logic must continue to be applied when client applications use the `CreateMultiple` and `UpdateMultiple` messages.

With the introduction of the `CreateMultiple` and `UpdateMultiple` messages, for best performance we recommend that you begin to move any existing synchronous logic from `Create` and `Update` events to `CreateMultiple` and `UpdateMultiple` events. If you are introducing new logic, use the `CreateMultiple` and `UpdateMultiple` events rather than `Create` and `Update`. For asynchronous logic, such as Power Automate flows, there is no direct performance gain by moving logic to the multiple versions of these events because they occur after the operation has completed.

> [!IMPORTANT]
> With this design there is potential for duplicate logic to be applied on both the single and multiple versions of events for the operations. Dataverse does not try to prevent this because we cannot know your intent.
>
> It is the plug-in developer's responsibility to make sure that the same logic applied for the single version of events is migrated to the multiple version of the event *and removed* from the single version of the event. Otherwise, the logic will be applied twice.

More information: [Write plug-ins for CreateMultiple and UpdateMultiple (Preview)](../write-plugin-multiple-operation.md)

## Limitations

Keep these limitations in mind when using `CreateMultiple` and `UpdateMultiple` messages.

### Limited to certain tables

Currently, `CreateMultiple` and `UpdateMultiple` messages are limited to those tables which have been created recently. You can use these messages on a new custom table you create. These messages will be enabled for all tables that support individual `Create` and `Update` messages in the coming months.

You can test whether individual tables support these messages today using the examples below.

#### [SDK for .NET](#tab/sdk)

This static method can be used to detect whether a given table supports any specific named message, including `CreateMultiple` or `UpdateMultiple`.

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

The following `GET` request detects whether the `CreateMultiple` message is available for a custom table with the logical name`sample_example`. Replace the `@message` and `@table` parameters for the message and table you want to test.

**Request**

```http
GET [Organization Uri]/api/data/v9.2/sdkmessagefilters?$select=sdkmessagefilterid&$filter=sdkmessageid/name eq @message and primaryobjecttypecode eq @table&@message='CreateMultiple'&@table='sample_example' HTTP/1.1
Content-Type: application/json
```

When the table supports the message, an `sdkmessagefilterid` value will be returned. If it is not supported, the `value` will be an empty array.

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

### Message Size and Time limits

The efficiency gained per operation using `CreateMultiple` and `UpdateMultiple` messages increases with the number of entities included in the `Targets` parameter, so with projects that perform bulk operations there is incentive to try and use the largest possible number.

There is currently no set limit on the number of entities you might try to send with your requests, but generally we expect that 1000 entities per request is a reasonable place to start. The kinds of errors you may encounter can usually be addressed by sending fewer entities with each request. We recommend you include the ability to configure the number of entities sent so that you can adapt by sending fewer.

#### Message size limits

When you have a plug-in registered for any message you may encounter the [Message size exceeded when sending context to Sandbox](../troubleshoot-plug-in.md#error-message-size-exceeded-when-sending-context-to-sandbox) error when the total size of the request exceeds 116.85 MB. With `CreateMultiple` and `UpdateMultiple` it is more likely you will hit this limit as you send larger payloads.

This error will not occur if there is no plug-in registered for the event. You can avoid this error by disabling the plugin(s) or by sending your request with the `BypassCustomPluginExecution` optional parameter. More information: [Bypass Custom Business Logic](../bypass-custom-business-logic.md)

#### Time Limits

If you are using the Dataverse [ServiceClient](xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient), you may encounter this error `The request channel timed out attempting to send after 00:04:00. Increase the timeout value passed to the call to Request or increase the SendTimeout value on the Binding. The time allotted to this operation may have been a portion of a longer timeout.`

The default timeout set using ServiceClient is 4 minutes, which is very long for any synchronous operation. You can change this using the static [ServiceClient.MaxConnectionTimeout](xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient.MaxConnectionTimeout) property. The default timeout using [CrmServiceClient](xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient) is 2 minutes.

> [!NOTE]
> Before you increase the time limits, you should consider reducing the number of entities passed in the `Targets` parameter.

### No continue on error

The `ExecuteMultiple` message supports the option that will continue processing requests even when one or more requests fail. Due to the fact that `CreateMultiple` and `UpdateMultiple` messages achieve performance improvements by unifying all operations in a single transaction, it isn't possible to support the continue on error behaviors.

You should use `CreateMultiple` and `UpdateMultiple` messages when you have a high degree of confidence that all the operations will succeed. You may want to use a strategy that will allow the set of operations to fall back to use `ExecuteMultiple` if `CreateMultiple` and `UpdateMultiple` messages fail.

### .NET SDK only

Currently the `CreateMultiple` and `UpdateMultiple` messages are only available to be used with the .NET SDK. The capability to use these operations using Web API is coming soon.

### Not supported for use in Plug-ins

At this time we don't support using `CreateMultiple` or `UpdateMultiple` within plug-ins, but we plan to support this soon.

## Frequently Asked Questions

The following are frequently asked question related to the introduction of these messages.

### Will there be an UpsertMultiple?

We are still evaluating whether an `UpsertMultiple` is necessary.

### Will there be a DeleteMultiple?

There are no plans to have `DeleteMultiple`. Delete operations frequently include cascading operations which can result in unpredictable execution times. We already have a `BulkDelete` message that enables asynchronous deletion of records that match a query.

### Will Retrieve and RetrieveMultiple logic be merged?

There are no plans to change `Retrieve` and `RetrieveMultiple` message behavior. Attempting to merge the message pipeline for these messages would be highly problematic because these have been separate messages for many years and developers have always needed to maintain logic for them separately. Also, we discourage applying custom logic for these messages due to the impact they can have on performance. More information: [Limit the registration of plug-ins for Retrieve and RetrieveMultiple messages](../best-practices/business-logic/limit-registration-plugins-retrieve-retrievemultiple.md)

### See Also

[Write plug-ins for CreateMultiple and UpdateMultiple](../write-plugin-multiple-operation.md)<br />
[Sample: Use CreateMultiple and UpdateMultiple](samples/create-update-multiple.md)<br />
[Sample: CreateMultiple and UpdateMultiple plug-ins](samples/createmultiple-updatemultiple-plugin.md)<br />
[Use messages with the Organization service](use-messages.md)<br />


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]