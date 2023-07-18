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
|`DeleteMultiple`|Recommended for elastic tables only, use the SDK [OrganizationRequest class](xref:Microsoft.Xrm.Sdk.OrganizationRequest) to delete multiple records of the same type.|

## Standard and Elastic table usage

Both standard and elastic tables see significant performance benefits when using these bulk operation messages, but you need to use them differently. The following table summarizes the differences.

||Standard|Elastic|
|---------|---------|---------|
|**Number of records**|Operations more efficient with larger number of records. There is no set limit, but there are message and time limits.|Recommend sending 100 records at a time.|
|**On Error behavior**|All operations rollback on error.|Partial success is possible.|
|**Availability**|Not all tables support these messages.|Messages available for all elastic tables.|
|**DeleteMultiple**|Not recommended. Use the SDK [BulkDeleteRequest class](xref:Microsoft.Crm.Sdk.Messages.BulkDeleteRequest) or the Web API [BulkDelete action](xref:Microsoft.Dynamics.CRM.BulkDelete). instead.|Recommended. More information: [Use DeleteMultiple with elastic tables](#use-deletemultiple-with-elastic-tables)|

Standard and elastic table usage is different because standard tables use Azure SQL and support transactions. Elastic tables use Azure Cosmos DB, which doesn't support transactions but is able to handle large amounts of data an high levels of throughput with low latency.

### Number of records

**With standard tables**, bulk operations are optimized to perform operations on multiple rows within a single transaction. Operations become more efficient, and therefore more performant overall, as the number of operations per request increases. This also allows for any plug-in steps registered for the bulk operation to be more efficient. Each time a plug-in is invoked for a single operation, some milliseconds are required to invoke the plug-in class containing the logic. When a plug-in is registered for a bulk operation message, the class is invoked once and can process all the operations more efficiently.

This performance benefit gives you an incentive to send the largest number of records you can in each request. However, as the number of records increases the size of the request becomes larger and takes longer to process. If you hit these limits, the entire operation will fail. There is no set limit. You will need to experiment to find the best number. Generally, we expect that 1000 records per request is a reasonable place to start if the size of the record data is small and there are no plug-ins. The kinds of errors you may encounter can usually be addressed by sending fewer records with each request. We recommend that you include the ability to configure the number of entities sent so you can adapt by sending fewer.

**With elastic tables**, there is no transaction, so there is no performance benefit in trying to send the largest number per request. We recommend sending 100 operations per request and sending requests in parallel to achieve maximum throughput.

> [!TIP]
> Both standard and elastic tables have greater throughput when you use bulk operations requests in parallel. More information: [Send parallel requests](send-parallel-requests.md)

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

**With elastic tables**, all elastic tables support bulk operations.



## Performance improvements for standard tables

## Message pipelines merged

## Limitations


## Use DeleteMultiple with elastic tables

Use the SDK [OrganizationRequest class](xref:Microsoft.Xrm.Sdk.OrganizationRequest) to delete multiple records of the same type.