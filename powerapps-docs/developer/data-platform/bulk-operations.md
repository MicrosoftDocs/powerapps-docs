---
title: Use bulk operation messages (preview)
description: Learn how to use special APIs to perform operations on multiple rows of data in a Microsoft Dataverse table. 
ms.date: 08/02/2023
author: divkamath
ms.author: dikamath
ms.reviewer: jdaly
ms.topic: how-to
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
contributors:
 - JimDaly
ms.custom: bap-template
---

# Use bulk operation messages (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

> [!IMPORTANT]
> This is a preview feature.
>
> [!INCLUDE [cc-preview-features-definition](../../includes/cc-preview-features-definition.md)]

To get the best performance when you run operations on multiple rows of a Microsoft Dataverse table, use one of the following bulk operation messages:

- [`CreateMultiple`](#createmultiple): Creates multiple records of the same type in a single request.
- [`UpdateMultiple`](#updatemultiple): Updates multiple records of the same type in a single request.
- `UpsertMultiple`: *Coming soon*
- [`DeleteMultiple`](#deletemultiple): For elastic tables only. Deletes multiple records of the same type in a single request.

## Examples

The following code samples show how to use bulk operation messages. You can download the samples from [github.com/microsoft/PowerApps-Samples](https://github.com/microsoft/PowerApps-Samples):

- [Sample: SDK for .NET Use CreateMultiple and UpdateMultiple (preview)](org-service/samples/create-update-multiple.md)
- [Sample: Web API Use CreateMultiple and UpdateMultiple (preview)](webapi/samples/create-update-multiple.md)
- [Elastic table sample code (preview)](elastic-table-samples.md)

### CreateMultiple

##### [SDK for .NET](#tab/sdk)

Uses the [CreateMultipleRequest class](xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest).

```csharp
/// <summary>
/// Demonstrates the use of the CreateMultiple Message
/// </summary>
/// <param name="service">The authenticated IOrganizationService instance.</param>
/// <param name="recordsToCreate">A list of records of the same table to create.</param>
/// <returns>The Guid values of the records created.</returns>
static Guid[] CreateMultipleExample(IOrganizationService service,
    List<Entity> recordsToCreate)
{

    // Create an EntityCollection populated with the list of entities.
    EntityCollection entities = new(recordsToCreate)
    {
        // All the records must be for the same table.
        EntityName = recordsToCreate[0].LogicalName
    };

    // Instantiate CreateMultipleRequest
    CreateMultipleRequest createMultipleRequest = new()
    {
        Targets = entities,
    };

    // Send the request
    CreateMultipleResponse createMultipleResponse =
                (CreateMultipleResponse)service.Execute(createMultipleRequest);

    // Return the Ids of the records created.
    return createMultipleResponse.Ids;
}
```

##### [Web API](#tab/webapi)

Uses the [CreateMultiple action](xref:Microsoft.Dynamics.CRM.CreateMultiple).

> [!IMPORTANT]
> You must set the `@odata.type` property for each item in the `Targets` parameter.

**Request:**

```http
POST [Organization Uri]/api/data/v9.2/sample_examples/Microsoft.Dynamics.CRM.CreateMultiple
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
Content-Type: application/json; charset=utf-8
Content-Length: 396

{
    "Targets": [
        {
            "sample_name": "sample record 0000001",
            "@odata.type": "Microsoft.Dynamics.CRM.sample_example"
        },
        {
            "sample_name": "sample record 0000002",
            "@odata.type": "Microsoft.Dynamics.CRM.sample_example"
        },
        {
            "sample_name": "sample record 0000003",
            "@odata.type": "Microsoft.Dynamics.CRM.sample_example"
        }
    ]
}
```

**Response:**

```http
HTTP/1.1 200 OK
OData-Version: 4.0

{
    "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.CreateMultipleResponse",
    "Ids": [
        "8f4c3f92-312b-ee11-bdf4-000d3a993550",
        "904c3f92-312b-ee11-bdf4-000d3a993550",
        "914c3f92-312b-ee11-bdf4-000d3a993550"
    ]
}
```

---

### UpdateMultiple

Just like when you update individual records, the data you send with `UpdateMultiple` must contain only the values you're changing. Learn how to [update records with SDK for .NET](org-service/entity-operations-update-delete.md) and [update records with the Web API](webapi/update-delete-entities-using-web-api.md#basic-update).

##### [SDK for .NET](#tab/sdk)

Uses the [UpdateMultipleRequest class](xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest).

```csharp
/// <summary>
/// Demonstrates the use of the UpdateMultiple message.
/// </summary>
/// <param name="service">The authenticated IOrganizationService instance.</param>
/// <param name="recordsToUpdate">A list of records to create.</param>
static void UpdateMultipleExample(IOrganizationService service, List<Entity> recordsToUpdate) {
    // Create an EntityCollection populated with the list of entities.
    EntityCollection entities = new(recordsToUpdate)
    {
        // All the records must be for the same table.
        EntityName = recordsToUpdate[0].LogicalName
    };

    // Use UpdateMultipleRequest
    UpdateMultipleRequest updateMultipleRequest = new()
    {
        Targets = entities,
    };

    service.Execute(updateMultipleRequest);
}
```

##### [Web API](#tab/webapi)

Uses the [UpdateMultiple action](xref:Microsoft.Dynamics.CRM.UpdateMultiple).

> [!IMPORTANT]
> You must set the `@odata.type` property for each item in the `Targets` parameter.

**Request:**

```http
POST [Organization Uri]/api/data/v9.2/sample_examples/Microsoft.Dynamics.CRM.UpdateMultiple?tag=CreateUpdateMultiple
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
Content-Type: application/json; charset=utf-8
Content-Length: 621

{
    "Targets": [
        {
            "sample_name": "sample record 0000001 Updated",
            "@odata.type": "Microsoft.Dynamics.CRM.sample_example",
            "sample_exampleid": "8f4c3f92-312b-ee11-bdf4-000d3a993550"
        },
        {
            "sample_name": "sample record 0000002 Updated",
            "@odata.type": "Microsoft.Dynamics.CRM.sample_example",
            "sample_exampleid": "904c3f92-312b-ee11-bdf4-000d3a993550"
        },
        {
            "sample_name": "sample record 0000003 Updated",
            "@odata.type": "Microsoft.Dynamics.CRM.sample_example",
            "sample_exampleid": "914c3f92-312b-ee11-bdf4-000d3a993550"
        }
    ]
}
```

**Response:**

```http
HTTP/1.1 204 NoContent
OData-Version: 4.0
```

---

### DeleteMultiple

`DeleteMultiple` is available only for elastic tables.

##### [SDK for .NET](#tab/sdk)

You must use the [OrganizationRequest class](xref:Microsoft.Xrm.Sdk.OrganizationRequest) because the SDK doesn't have a `DeleteMultipleRequest` class. Learn how to [use messages with the Organization service](org-service/use-messages.md).

The following `DeleteMultipleExample` static method uses the `DeleteMultiple` message with the [OrganizationRequest class](xref:Microsoft.Xrm.Sdk.OrganizationRequest) to delete multiple rows from the `contoso_SensorData` elastic table using the alternate key to include the `partitionid` to uniquely identify the rows.

```csharp
public static void DeleteMultipleExample(IOrganizationService service)
{
    string tableLogicalName = "contoso_sensordata";

    List<EntityReference> entityReferences = new() {
        {
            new EntityReference(logicalName: tableLogicalName,
               keyAttributeCollection: new KeyAttributeCollection
               {
                  { "contoso_sensordataid", "3f56361a-b210-4a74-8708-3c664038fa41" },
                  { "partitionid", "deviceid-001" }
               })
        },
        { new EntityReference(logicalName: tableLogicalName,
               keyAttributeCollection: new KeyAttributeCollection
               {
                  { "contoso_sensordataid", "e682715b-1bba-415e-b2bc-de9327308423" },
                  { "partitionid", "deviceid-002" }
               })
        }
    };

    OrganizationRequest request = new(requestName:"DeleteMultiple")
    {
        Parameters = {
            {"Targets", new EntityReferenceCollection(entityReferences)}
        }
    };

    service.Execute(request);
}
```

##### [Web API](#tab/webapi)

The following example shows how to use the `DeleteMultiple` action to delete multiple rows from the `contoso_SensorData` elastic table including the `partitionid` to uniquely identify the rows.

> [!NOTE]
> At the time of this writing, the Web API `DeleteMultiple` action is a private action. You won't find it in the [CSDL $metadata document](webapi/web-api-service-documents.md#csdl-metadata-document) or in the Dataverse <xref:Microsoft.Dynamics.CRM.ActionIndex?displayProperty=fullName>. This action will become public soon. You can use it while it's private.

**Request:**

```http
POST [Organization Uri]/api/data/v9.2/contoso_sensordatas/Microsoft.Dynamics.CRM.DeleteMultiple
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
Content-Type: application/json; charset=utf-8
Content-Length: 603

{
    "Targets": [
        {
            "@odata.type": "Microsoft.Dynamics.CRM.contoso_sensordata",
            "contoso_sensordataid": "6114ca58-0928-ee11-9965-6045bd5cd155",
            "partitionid": "Device-ABC-1234"
        },
        {
            "@odata.type": "Microsoft.Dynamics.CRM.contoso_sensordata",
            "contoso_sensordataid": "6214ca58-0928-ee11-9965-6045bd5cd155",
            "partitionid": "Device-ABC-1234"
        },
        {
            "@odata.type": "Microsoft.Dynamics.CRM.contoso_sensordata",
            "contoso_sensordataid": "6314ca58-0928-ee11-9965-6045bd5cd155",
            "partitionid": "Device-ABC-1234"
        }
    ]
}
```

**Response:**

```http
HTTP/1.1 204 NoContent
OData-Version: 4.0
```

---

## Standard and elastic table usage

Both standard and elastic tables benefit from a significant performance boost when you use bulk operation messages, but you need to use them differently. The following table summarizes the differences.

|Difference|Standard|Elastic|
| --------- | --------- | --------- |
| [Number of records](#number-of-records) | Operations are more efficient with a larger number of records. There's no limit on the number of records, but there are message size and time limits. | We recommend sending 100 records at a time. |
| [On Error behavior](#on-error-behavior) | All operations roll back on error. | Partial success is possible. |
| [Availability](#availability) | Not all standard tables support these messages. | Messages are available for all elastic tables. |
| [DeleteMultiple](#deletemultiple) | Not available. Use the SDK [BulkDeleteRequest class](xref:Microsoft.Crm.Sdk.Messages.BulkDeleteRequest) or the Web API [BulkDelete action](xref:Microsoft.Dynamics.CRM.BulkDelete) instead. [Learn how to delete data in bulk](delete-data-bulk.md). | Available using the SDK [OrganizationRequest class](xref:Microsoft.Xrm.Sdk.OrganizationRequest). The Web API `DeleteMultiple` action is private, but you can use it now. It will become public soon. |

Standard and elastic table usage is different because standard tables use Azure SQL and support transactions. Elastic tables use Azure Cosmos DB, which doesn't support transactions but is able to handle large amounts of data at high levels of throughput with low latency. The following sections provide more details. [Learn more about bulk operations on elastic tables](use-elastic-tables.md#bulk-operations-with-elastic-tables).

### Number of records

The number of records that you should include with each request depends on whether you're using standard or elastic tables.

> [!TIP]
> Both standard and elastic tables have greater throughput when you [send bulk operation messages in parallel](send-parallel-requests.md).

#### Number of records with standard tables

Bulk operations on standard tables are optimized to perform on multiple rows in a single transaction. Operations become more efficient, and performance increases overall, as the number of operations per request increases. This optimization also allows for any plug-in steps that are registered for the bulk operation to be more efficient. Each time a plug-in is invoked for a single operation, some milliseconds are required to invoke the plug-in class containing the logic. When a plug-in is registered for a bulk operation message, the class is invoked once and can process all the operations more efficiently. [Learn how to write plug-ins for CreateMultiple and UpdateMultiple (preview)](write-plugin-multiple-operation.md).

This performance benefit gives you an incentive to send the largest number of records you can in each request. However, as the number of records increases, the size of the request increases, too, and the request takes longer to process. Eventually, you'll encounter [message size and time limits](#message-size-and-time-limits). If you hit these limits, the entire operation fails. There's no set limit on the number of records you can send. You may need to experiment to find the best number. Generally, we expect that 1,000 records per request is a reasonable place to start if the size of the record data is small and there are no plug-ins. The kinds of errors you may encounter can usually be addressed by sending fewer records with each request. We recommend that you include the ability to configure the number of entities sent so that you can adapt by sending fewer.

#### Number of records with elastic tables

Because there's no transaction with elastic tables, there's no performance benefit in trying to send a large number of records per request. We recommend that you send 100 operations per request and send requests in parallel to achieve maximum throughput.

### On Error behavior

The behavior when errors occur depends on whether you're using standard tables or elastic tables.

#### On Error behavior with standard tables

Any error that occurs in a bulk operation with a standard table causes the entire operation to roll back. You should only use bulk operations on standard tables when you have a high degree of confidence that all the operations will succeed. You may want to use the SDK [ExecuteMultipleRequest class](xref:Microsoft.Xrm.Sdk.Messages.ExecuteMultipleRequest) or Web API `$batch` to allow the set of operations to fall back if the bulk operation fails. If the success rate for your initial attempts is low, this strategy results in worse performance. Only use this fallback strategy when you expect most operations to succeed.

#### On Error behavior with elastic tables

With elastic tables, a bulk operation may partially succeed. You can use the error details to identify which records failed.

##### [SDK for .NET](#tab/sdk)

When you use the SDK to perform a bulk operation on an elastic table, a [FaultException](xref:System.ServiceModel.FaultException%601) of type [OrganizationServiceFault](xref:Microsoft.Xrm.Sdk.OrganizationServiceFault) is thrown if a failure occurs. Use the following code to get the status of each record.

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

##### [Web API](#tab/webapi)

When you use the Web API to perform a bulk operation on an elastic table, you need to pass the `Prefer` header with value `odata.include-annotations=*` or `odata.include-annotations=Microsoft.PowerApps.CDS.ErrorDetails.*`, which gives the status of each record. [Learn how to include more details with errors](webapi/compose-http-requests-handle-errors.md#include-more-details-with-errors).

---

### Availability

Bulk operation message availability depends on whether you're using standard tables or elastic tables. All elastic tables support the `CreateMultiple`, `UpdateMultiple`, and `DeleteMultiple` messages.

#### Availability with standard tables

You can use the `CreateMultiple` and `UpdateMultiple` bulk operation messages with custom standard tables and many common standard tables, but not all. You should test whether individual standard tables support these messages. The following examples show you how to do that.

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

Use the following `GET` request to detect whether a message is available for a table. The request tests whether the `sample_example` table supports the `CreateMultiple` message. Replace the `@message` and `@table` parameter values for the message and table you want to test.

**Request:**

```http
GET [Organization Uri]/api/data/v9.2/sdkmessagefilters?$select=sdkmessagefilterid&$filter=sdkmessageid/name eq @message and primaryobjecttypecode eq @table&@message='CreateMultiple'&@table='sample_example' HTTP/1.1
Content-Type: application/json
```

If the table supports the message, an `sdkmessagefilterid` value is returned. Otherwise, the value is an empty array.

**Response:**

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

#### DeleteMultiple availability

`DeleteMultiple` is supported only for elastic tables. Elastic tables don't support [table relationship cascading behavior](configure-entity-relationship-cascading-behavior.md), which can result in unpredictable execution times for delete operations. If you use `DeleteMultiple` on a standard table, you get the error: `DeleteMultiple has not yet been implemented.`


## Message pipelines merged

Each of the bulk operation messages has a corresponding message that operates on individual rows: `Create`, `Update`, `Upsert`, and `Delete`. These messages have existed for a long time, and many organizations have customized logic that depends on the events that occur when these messages are used.

A key requirement of the bulk operation messages is that organizations must not be required to maintain custom logic in two places. To have the same custom logic and maintain it in one place, we've *merged* the message processing pipelines for these messages. What does this mean?

- When a bulk operation message is used, the respective `Create` and `Update` event occurs for each [Entity](xref:Microsoft.Xrm.Sdk.Entity) instance in the `Targets` parameter. Any plug-ins or other event handlers for the corresponding individual events continue to work as they always have. You don't need to write new plug-ins to manage events raised by these messages.

- When a single operation message is used, the respective bulk operation event occurs with an [EntityCollection](xref:Microsoft.Xrm.Sdk.EntityCollection) containing a *single* [Entity](xref:Microsoft.Xrm.Sdk.Entity) instance passed in the `Targets` parameter.  You can move any logic that responds to single operation events to the more efficient bulk operation events and the logic is applied for both individual and multiple operations.

   > [!NOTE]
   > Don't migrate custom logic to the `DeleteMultiple` message until [Known issue: DeleteMultiple plug-ins not invoked for Delete](#deletemultiple-plug-ins-not-invoked-for-delete) is resolved.

Before the introduction of bulk operation messages, all custom logic was on the single operation messages. That logic must continue to be applied when client applications use the bulk operation messages. For tables used with high-volume bulk operations, we recommend that you begin to move any synchronous logic from single message events to bulk operation events. If you're introducing new logic, use the bulk operation events rather than the single operation events.

> [!CAUTION]
> With this design, duplicate logic can potentially be applied on both the single and multiple versions of events. Dataverse doesn't try to prevent this because we can't know your intent.
>
> It's your responsibility to make sure that the same logic applied for the single version of events is migrated to the multiple version of the event *and removed* from the single version of the event. Otherwise, the logic will be applied twice.

[Learn how to write plug-ins for CreateMultiple and UpdateMultiple (preview)](write-plugin-multiple-operation.md).

## Limitations

Keep the following limitations in mind when you use bulk operation messages.

### Message size and time limits

With standard tables, there's a performance incentive to send more records with each request. However, the number of records you can send is limited by the size of the payload and the amount of time required to process the operation.

#### Message size limits

When you have a plug-in registered for any message, you may encounter the ["Message size exceeded when sending context to Sandbox"](/troubleshoot/power-platform/power-apps/dataverse/dataverse-plug-ins-errors#error-message-size-exceeded-when-sending-context-to-sandbox) error when the total size of the request exceeds 116.85 MB. With bulk operation messages, you're more likely to hit this limit as you send larger payloads.

This error doesn't occur if there's no plug-in registered for the event. To avoid the error, disable any plugins or send your request with the [`BypassCustomPluginExecution` optional parameter](bypass-custom-business-logic.md#).

#### Time limits

If you're using the Dataverse [ServiceClient](xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient), you may encounter this error:

> `The request channel timed out attempting to send after 00:04:00. Increase the timeout value passed to the call to Request or increase the SendTimeout value on the Binding. The time allotted to this operation may have been a portion of a longer timeout.`

The default timeout set using ServiceClient is 4 minutes, which is long for any synchronous operation. You can change this value using the static [ServiceClient.MaxConnectionTimeout](xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient.MaxConnectionTimeout) property. The default timeout using [CrmServiceClient](xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient) is 2 minutes.

> [!NOTE]
> Before you increase the time limits, you should consider reducing the number of records that are passed in the `Targets` parameter.

### Not supported for use in plug-ins

At this time, we don't support using bulk operation messages in plug-ins. More information:[Don't use batch request types in plug-ins and workflow activities](best-practices/business-logic/avoid-batch-requests-plugin.md).

## Known issues

The following issues will be addressed before the bulk operations feature becomes generally available.

### UpdateMultipleRequest.ConcurrencyBehavior doesn't work

<xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest.ConcurrencyBehavior> specifies the type of optimistic [concurrency behavior](xref:Microsoft.Xrm.Sdk.ConcurrencyBehavior) that should be applied. Possible values are `AlwaysOverwrite`, `Default`, and `IfRowVersionMatches`. Currently, the `Default` option is always applied, regardless of what you set. The behavior depends on whether [EntityMetadata.IsOptimisticConcurrencyEnabled](xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.IsOptimisticConcurrencyEnabled) is set for the table.

### DeleteMultiple plug-ins not invoked for Delete

As part of the changes we made to [merge message pipelines](#message-pipelines-merged), any custom logic for the multiple version of the message must also be invoked when the single version of the message is invoked. At this time, plug-in steps registered for the `DeleteMultiple` message *are not* being called when `Delete` is used. Plug-in steps registered for `Delete` *are* being invoked when `DeleteMultiple` is used.

You shouldn't migrate custom logic from `Delete` to `DeleteMultiple` until this issue is resolved. You can use `DeleteMultiple` and any logic that's associated with the `Delete` message still works.

## Frequently asked questions (FAQ)

If you don't find an answer in this article to questions you have about using bulk operation messages, use the button at the bottom of the page to **Submit and view feedback for This Page**. You need a GitHub account to submit feedback.

### Will Retrieve and RetrieveMultiple logic be merged?

We don't plan to change `Retrieve` and `RetrieveMultiple` message behavior. These have been separate messages for many years and developers have always needed to maintain logic for them separately. Attempting to merge the message pipeline for them would be highly problematic. Also, we discourage applying custom logic for these messages due to the [impact they can have on performance](best-practices/business-logic/limit-registration-plugins-retrieve-retrievemultiple.md).

### How are API limits applied?

There are two types of API limits. The bulk operation messages don't provide any way to bypass either type.

#### Service protection limits

As described in [Service protection API limits](api-limits.md), limits have three facets. Two of these limits are evaluated on a five-minute sliding window and apply when using these messages.

- **Number of requests**: Each bulk operation message counts as single request that accrues to the limit of 6,000 requests per user, per server, during the five-minute window. Because these requests group individual operations, *the likelihood of hitting this limit is reduced*.
- **Execution time**: Because each bulk operation message request typically takes longer, if you're sending requests in parallel, *you're more likely to hit the execution time limit* of 20 minutes per user, per server, during the five-minute window.

#### Power Platform Request (API Entitlement) limits

These limits are based on data changes: `Create`, `Update`, and `Delete` operations. Each item included in the `Targets` parameter of a bulk operation request accrues to this limit. [Learn more about request limits and allocations](/power-platform/admin/api-request-limits-allocations).

### See also

[Elastic tables (preview)](elastic-tables.md)  
[Write plug-ins for CreateMultiple and UpdateMultiple (preview)](write-plugin-multiple-operation.md)  
[Sample: SDK for .NET Use CreateMultiple and UpdateMultiple (preview)](org-service/samples/create-update-multiple.md)  
[Sample: Web API Use CreateMultiple and UpdateMultiple (preview)](webapi/samples/create-update-multiple.md)  
[Sample: CreateMultiple and UpdateMultiple plug-ins](org-service/samples/createmultiple-updatemultiple-plugin.md)  
[Use messages with the Organization service](org-service/use-messages.md)
