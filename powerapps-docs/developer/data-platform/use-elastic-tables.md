---
title: "Use elastic tables using code (preview) (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn how to perform data operations on elastic tables using code" # 115-145 characters including spaces. This abstract displays in the search result.
ms.topic: article
ms.date: 05/27/2022
author: pnghub
ms.author: gned
ms.reviewer: jdaly
search.audienceType: 
  - developer
contributors:
 - sumantb-msft
 - JimDaly
---

# Use elastic tables using code (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

This article describes how to perform data operations on elastic tables using code.

## Work with session token

As mentioned in [Consistency level](elastic-tables.md#consistency-level), you can achieve session level consistency by passing the current session token with your requests. If you don't include the session token, the data you retrieve may not include data changes you have just made.

### Getting the session token

You'll find the session token as `x-ms-session-token` value in the response of all write operations.

#### [SDK for .NET](#tab/sdk)

For any [OrganizationResponse](xref:Microsoft.Xrm.Sdk.OrganizationResponse) that performs a write operation, you can capture the `x-ms-session-token` in the [Results](xref:Microsoft.Xrm.Sdk.OrganizationResponse.Results) collection.

> [!NOTE]
> [DeleteResponse](xref:Microsoft.Xrm.Sdk.Messages.DeleteResponse) does not currently return the x-ms-session-token. More information: [Known issues:  x-ms-session-token value not returned for delete operations](elastic-tables.md#x-ms-session-token-value-not-returned-for-delete-operations)

```csharp
string sessionToken = response.Results["x-ms-session-token"].ToString();
```

#### [Web API](#tab/webapi)

The session token value is returned as the `x-ms-session-token` response header.

> [!NOTE]
> DELETE operations do not currently return the `x-ms-session-token`. More information: [Known issues:  x-ms-session-token value not returned for delete operations](elastic-tables.md#x-ms-session-token-value-not-returned-for-delete-operations)

```http
x-ms-session-token: 240:8#144100870#7=-1
```

---

### Sending the session token

How you send the session token in a read operation depends on whether you're using the SDK or Web API.
#### [SDK for .NET](#tab/sdk)

When performing an operation that retrieves data, set the `SessionToken` optional parameter on the [OrganizationRequest](xref:Microsoft.Xrm.Sdk.OrganizationRequest).

```csharp

var request = new RetrieveRequest
{
   Target = new EntityReference("contoso_sensordata", sensordataid),
   ColumnSet = new ColumnSet("contoso_value"),
   ["partitionId"] = deviceId,
   ["SessionToken"] = sessionToken
};

```

More information: [Use optional parameters](optional-parameters.md)


#### [Web API](#tab/webapi)

When performing a `GET` operation, use the `MSCRM.SessionToken` request header to pass corresponding `x-ms-session-token` to retrieve the most up-to-date row value.

```http
MSCRM.SessionToken: 240:8#144100870#7=-1
```

---

## Specifying PartitionId

As mentioned in [Partitioning and horizontal scaling](elastic-tables.md#partitioning-and-horizontal-scaling), each elastic table has a `partitionid` column that you must use if you choose to apply a partitioning strategy for the table. Otherwise, don't set a value for the `partitionid` column.

Once you have specified a non-null value to the `partitionid` column while creating a row, you must specify it when performing any other data operation on the row. You can't change this value later.

If you don't set a `partitionid` for a record when it's created, the `partitionid` column value remains null and you can't change it later. In this case, you can identify records using the primary key as you normally do with standard tables. Specifying `partitionid` isn't required.

> [!NOTE]
> The examples in this article assume that you are specifying a non-null value to the `partitionid` column.

You can set the `partitionid` value in following ways when performing various data operations.

### Using Alternate Key

As mentioned in [Alternate keys](create-elastic-tables.md#alternate-keys), every elastic table has an alternate key named `KeyForNoSqlEntityWithPKPartitionId`. This alternate key combines the primary key of the table with the `partitionid` column.

You can use this alternate key to specify `partitionid` when using `Retrieve`, `Update` or `Delete` operations.

#### [SDK for .NET](#tab/sdk)

This example shows how you can use alternate key to specify `partitionid` when using `Retrieve`, `Update` and `Delete` requests on elastic tables.

```csharp
    var keys = new KeyAttributeCollection() {
        { "contoso_sensordataid", sensordataid },
        { "partitionid", deviceId }
    };

    var entity = new Entity("contoso_sensordata", keys)
```

#### [Web API](#tab/webapi)

This example shows how you can use the special syntax in Web API to refer to records using the alternate key when performing `GET`, `PATCH` and `DELETE` operation on a single row of an elastic table. More information: [Use an alternate key to reference a record](use-alternate-key-reference-record.md?tabs=webapi)

> `<entity set name>(<primary key name>=<primary key value>,partitionid='<partitionid value>')`

> [!NOTE]
> The primary key value is a GUID, so no single quote characters are needed. `partitionid` is a string, so it requires single quote characters.

For example:

```http
/contoso_sensordatas(contoso_sensordataid=e61a662e-68d8-487e-94e7-ae3a22fd4bbd,partitionid='device-001')
```

---
### Using partitionId parameter

Currently, you can use a `partitionId` parameter to specify the value of `partitionid` column only for `Retrieve` and `Delete` operations. More information: [Known Issue: partitionId optional parameter not available for all messages](elastic-tables.md#partitionid-optional-parameter-not-available-for-all-messages)

#### [SDK for .NET](#tab/sdk)

> [!NOTE]
> `partitionId` parameter will not work with `Create`, `Update` or `Upsert` messages and will be ignored if sent.

```csharp
request["partitionId"] = "device-001"
```

#### [Web API](#tab/webapi)

> [!NOTE]
> `partitionId` parameter will not work with `POST` or `PATCH` requests and will be ignored if sent.

For example:

```http
/contoso_sensordatas(<primary key value>)?partitionId='<partitionid value>'
```

---

### Using `partitionid` column directly

For `Create`, `Upsert` or `Update` operations, you can directly specify the value of `partitionid` column.

#### [SDK for .NET](#tab/sdk)

This example shows how you can directly specify the `partitionid` column in `Entity` when executing a `Create`, `Upsert`, or `Update` operation.

```csharp
    var entity = new Entity("contoso_sensordata", sensordataid)
    {
        Attributes = {
            { "partitionid", "device-001" }
        }
    };
```

#### [Web API](#tab/webapi)

This example shows how you can directly specify the value of `partitionid` column in request body when making a `POST` or `PATCH` request.

For example:

```json
{
  "partitionid": "deviceid-001"
}
```

---

## Create a record in an elastic table

This example creates a new row in `contoso_SensorData` table with `partitionid` set to `deviceid`. It also sets `ttlinseconds` column that ensures that row expires after one day (86,400 seconds) and deleted from Dataverse automatically.

These examples also capture the value of the `x-ms-session-token` that you can use when retrieving the created record.

#### [SDK for .NET](#tab/sdk)

```csharp
/// <summary>
/// Demonstrates creating a record with a partitionid and capturing the session token
/// </summary>
/// <param name="service">Authenticated client implementing the IOrganizationService interface</param>
/// <param name="deviceId">The value used as partitionid for the contoso_sensordata table. </param>
/// <param name="sessionToken">The current session token</param>
/// <returns>The Id of the created record.</returns>
public static Guid CreateExample(
    IOrganizationService service, 
    string deviceId, 
    ref string sessionToken )
{
    var entity = new Entity("contoso_sensordata")
    {
        Attributes =
            {
               { "contoso_deviceid", deviceId },
               { "contoso_sensortype", "Humidity" },
               { "contoso_value", 40 },
               { "contoso_timestamp", DateTime.UtcNow},
               { "partitionid", deviceId },
               { "ttlinseconds", 86400  }  // 86400  seconds in a day
            }
    };

    var request = new CreateRequest { 
        Target = entity
    };

    var response = (CreateResponse)service.Execute(request);

    // Capture the session token
    sessionToken = response.Results["x-ms-session-token"].ToString();

    return response.id;            
}
```

Use the `x-ms-session-token` value returned to set the `SessionToken` optional parameter when retrieving the record you created. More information: [Sending the session token](#sending-the-session-token)

#### [Web API](#tab/webapi)

**Request**

```http
POST [Organization URI]/api/data/v9.2/contoso_sensordatas
Content-Type: application/json
OData-MaxVersion: 4.0
OData-Version: 4.0
Accept: application/json

{
  "contoso_deviceid": "deviceid-001",
  "contoso_sensortype": "Humidity",
  "contoso_value": 40,
  "contoso_timestamp": "2023-05-15T22:36:24Z",
  "partitionid": "deviceid-001",
  "ttlinseconds": 86400
}
```

**Response**

```http
HTTP/1.1 204 No Content
OData-Version: 4.0
x-ms-session-token: 240:8#144035050#7=-1
OData-EntityId: [Organization URI]/api/data/v9.2/sensordata(7eb682f1-ca75-e511-80d4-00155d2a68d1)
```

Use the `x-ms-session-token` value returned with the `MSCRM.SessionToken` request header to retrieve the latest version of a record. More information: More information: [Sending the session token](#sending-the-session-token)

---

## Update a record in an elastic table

This example updates the `contoso_value` and `contoso_timestamp` values of an existing row in `contoso_SensorData` table using the `contoso_sensordataid` primary key and `partitionid` = `'device-001'`.

If you're using a partitioning strategy, the primary key and `partitionid` columns are required to uniquely identify an existing elastic table row. The `partitionid` of an existing row can't be updated and is only being used to uniquely identify the row to update.

This example uses the `KeyForNoSqlEntityWithPKPartitionId` alternate key to uniquely identify the record using both the primary key and the `partitionid`. More information: [Alternate keys](create-elastic-tables.md#alternate-keys)

#### [SDK for .NET](#tab/sdk)

This example shows using the `partitionid` value as an alternate key.

```csharp
/// <summary>
/// Demonstrates updating elastic table row with partitionid as alternate key.
/// </summary>
/// <param name="service">Authenticated client implementing the IOrganizationService interface</param>
/// <param name="sensordataid">The unique identifier of the contoso_sensordata table.</param>
/// <param name="deviceId">The value used as partitionid for the contoso_sensordata table. </param>
/// <param name="sessionToken">The current session token</param>
public static void UpdateExample(
    IOrganizationService service, 
    Guid sensordataid, 
    string deviceId, 
    ref string sessionToken)
{
    var keys = new KeyAttributeCollection() {
        { "contoso_sensordataid", sensordataid },
        { "partitionid", deviceId }
    };

    var entity = new Entity("contoso_sensordata", keys)
    {
        Attributes = {
            { "contoso_value", 60 },
            { "contoso_timestamp", DateTime.UtcNow }
        }
    };

    var request = new UpdateRequest { 
        Target = entity,
        ["SessionToken"] = sessionToken
    };

    var response = (UpdateResponse)service.Execute(request);

    // Capture the session token
    sessionToken = response.Results["x-ms-session-token"].ToString();
}
```

More information: [Use an alternate key to reference a record > Using the Entity class](use-alternate-key-reference-record.md#using-the-entity-class)

#### [Web API](#tab/webapi)


**Request**

```http
PATCH [Organization URI]/api/data/v9.2/contoso_sensordatas(contoso_sensordataid=<Guid Value>,partitionId='deviceid-001')
Content-Type: application/json
OData-MaxVersion: 4.0
OData-Version: 4.0
Accept: application/json
MSCRM.SessionToken: 240:8#144035978#7=-1
If-Match: *

{
  "contoso_value": 60,
  "contoso_timestamp": "2023-05-15T22:36:24Z"
}
```

**Response**

```http
HTTP/1.1 204 No Content
OData-Version: 4.0
OData-EntityId: [Organization URI]/api/data/v9.2/contoso_sensordatas(contoso_sensordataid=21d455f2-70f3-ed11-8848-000d3a993550,partitionid='deviceid-001')
x-ms-session-token: 240:8#144035978#7=-1
```

---

## Retrieve a record in an elastic table

If an elastic table record was created setting the `partitionid` value, you must use the `partitionid` value together with the primary key value to uniquely identify a record.

If the `partitionid` wasn't set, you can retrieve the record normally using only the primary key value.

#### [SDK for .NET](#tab/sdk)

There are two different ways to compose a request to retrieve a record using the `partitionid` value.

This example uses the [RetrieveRequest](xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest) class with the `Target` property set to an  [EntityReference](xref:Microsoft.Xrm.Sdk.EntityReference) created using the constructor that accepts a [KeyAttributeCollection](xref:Microsoft.Xrm.Sdk.KeyAttributeCollection) to use the `KeyForNoSqlEntityWithPKPartitionId` alternate key. More information: [Using the EntityReference class](use-alternate-key-reference-record.md#using-the-entityreference-class)


```csharp
public static void RetrieveExampleAlternateKey(IOrganizationService service, Guid sensorDataId, string deviceId) {

    var keys = new KeyAttributeCollection() {
        { "contoso_sensordataid", sensorDataId },
        { "partitionid", deviceId }
    };

    var entityReference = new EntityReference("contoso_sensordata", keys);

    var request = new RetrieveRequest { 
        ColumnSet = new ColumnSet("contoso_value"),
        Target = entityReference
    };

    var response = (RetrieveResponse)service.Execute(request);

    Console.WriteLine($"contoso_value: {response.Entity.GetAttributeValue<int>("contoso_value")}");
}
```

This example uses an optional parameter named `partitionId` on the [RetrieveRequest](xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest) class. More information: [Use optional parameters](optional-parameters.md)

```csharp
public static void RetrieveExampleOptionalParameter(IOrganizationService service, Guid sensorDataId, string deviceId)
{
    var entityReference = new EntityReference("contoso_sensordata", sensorDataId);

    var request = new RetrieveRequest
    {
        ColumnSet = new ColumnSet("contoso_value"),
        Target = entityReference,
        ["partitionId"] = deviceId
    };

    var response = (RetrieveResponse)service.Execute(request);

    Console.WriteLine($"contoso_value: {response.Entity.GetAttributeValue<int>("contoso_value")}");
}
```

#### [Web API](#tab/webapi)

The following example uses the `partitionId` query parameter.

**Request**

```http
GET [Organization URI]/api/data/v9.2/sensordata(<sensordataid value>)?partitionId=deviceid-001&$select=contoso_value,contoso_timestamp
Accept: application/json
Content-Type: application/json
MSCRM.SessionToken : htjy#4567
OData-MaxVersion: 4.0
OData-Version: 4.0
```

**Response**

```http
HTTP/1.1 200 OK
Content-Type: application/json; odata.metadata=minimal
OData-Version: 4.0

{
"@odata.context": "[Organization URI]/api/data/v9.2/$metadata#sensordata/$entity",  
"@odata.etag": "W/\"502186\"",  
"contoso_value": 60
"contoso_timestamp" : "2023-05-01Z06:00:00"
}
```

You could also use the alternate key:

`contoso_sensordatas(contoso_sensordataid=<Guid Value>,partitionId='deviceid-001')`

---

## Query rows of an elastic table

When you query the rows of an elastic table, you get best performance if you limit your query to a specific partition. If you don't limit your query to a specific partition, your query returns data across all logical partitions, which isn't as fast.


> [!NOTE]
> When used this way, the parameter must use the name `partitionId` (capital 'I') rather than `partitionid` (all lower case).
> 
> When specifying a filter this way, you don't need to specify the filter criteria on `partitionid` in your query in the normal manner (using FetchXML `condition`, [QueryExpression](xref:Microsoft.Xrm.Sdk.Query.QueryExpression) [ConditionExpression](xref:Microsoft.Xrm.Sdk.Query.ConditionExpression), or Web API `$filter`.)
> 
> A filter on the `partitionid` value in the normal manner will not have the same performance benefits as specifying it with the `partitionId` shown below.

These examples retrieve the first 5000 rows in the `contoso_SensorData` table that belong to logical `partitionid` = `'deviceid-001'`.

#### [SDK for .NET](#tab/sdk)

```csharp
public static EntityCollection RetrieveMultipleExample(IOrganizationService service)
{
   var request = new RetrieveMultipleRequest
   {
         Query = new QueryExpression("contoso_sensordata")
         {
            ColumnSet = new ColumnSet("contoso_value")
         },
         ["partitionId"] = "deviceid-001"
   };

   var response = (RetrieveMultipleResponse)service.Execute(request);
   return response.EntityCollection;
}
```

#### [Web API](#tab/webapi)

**Request**

```http
GET [Organization URI]/api/data/v9.2/sensordata?partitionId=deviceid-001
&$select=contoso_sensortype,contoso_value,contoso_timestamp
Accept: application/json
Content-Type: application/json
OData-MaxVersion: 4.0
OData-Version: 4.0
```

**Response**

```http
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  

{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#contoso_sensorata/$entity",
    "value": [
        {
            "@odata.etag": "W/\"81052965\"",
            "contoso_sensortype" : "Humidity",
            "contoso_value": "60",
            "contoso_timestamp" : "2023-05-01Z06:00:00"
        },
        {
            "@odata.etag": "W/\"81052965\"",
            "contoso_sensortype" : "Temperature",
            "contoso_value": "110",
            "contoso_timestamp" : "2023-05-02Z06:10:00"
        },
        {
            "@odata.etag": "W/\"81052965\"",
            "contoso_sensortype" : "Pressure",
            "contoso_value": "230",
            "contoso_timestamp" : "2023-05-01Z16:30:00"
        }
    ]
}
```

---

### Return related rows in a query

Elastic tables currently don't support returning related rows when executing a query.
Dataverse throws an error with code `0x80048d0b` and message **Link entities are not supported** when trying to do so.

However, elastic tables support returning related rows when retrieving a single row.

## Upsert a record in an elastic table

> [!IMPORTANT]
> Upsert operations with elastic tables are different than with standard tables. Upsert operations are expected to contain the full payload and will over-write any existing record data.

With elastic tables, if a record with a given ID and `partitionid` doesn't exist, it will be created. If it already exists, it is replaced.

#### [SDK for .NET](#tab/sdk)

This example upserts a row in the `contoso_SensorData` table with the specified `id` and `partitionid` = `deviceid-001`.

```csharp
/// <summary>
/// Demonstrates an upsert operation
/// </summary>
/// <param name="service">Authenticated client implementing the IOrganizationService interface</param>
/// <param name="id">The id of the record to update or create.</param>
/// <param name="sessionToken">The current session token</param>
/// <returns>Whether a record was created or not</returns>
public static bool UpsertExample(IOrganizationService service, Guid id, ref string sessionToken)
{
    var entity = new Entity("contoso_sensordata", id)
    {
        Attributes = {
            { "contoso_deviceid", "deviceid-001" },
            { "contoso_sensortype", "Humidity" },
            { "contoso_value", 60 },
            { "contoso_timestamp", DateTime.UtcNow },
            { "partitionid", "deviceid-001" },
            { "ttlinseconds", 86400 }
        }
    };

    var request = new UpsertRequest
    {
        Target = entity,
        ["SessionToken"] = sessionToken
    };

    var response = (UpsertResponse)service.Execute(request);

    // Capture the session token
    sessionToken = response.Results["x-ms-session-token"].ToString();

    return response.RecordCreated;
}
```

#### [Web API](#tab/webapi)

This example upserts a row in SensorData table with ID = `ff67610c-82ce-412c-85df-0bbc6521bb01` and `partitionid` = `'deviceid-001'`.

> [!NOTE]
> Upsert is identical to update except that the `If-Match: *` request header isn't included.

**Request**

```http
PATCH [Organization URI]/api/data/v9.2/sensordata(ff67610c-82ce-412c-85df-0bbc6521bb01)
Content-Type: application/json
x-ms-session-token: hn76qq#7324
OData-MaxVersion: 4.0  
OData-Version: 4.0
  
{  
  "deviceid", "deviceid-001",
  "sensortype", "Humidity",
  "value", 40,
  "timestamp", "2023-05-01Z05:00:00",
  "partitionid", "deviceid-001",
  "ttlinseconds", 86400
}
```

**Response**

```http
HTTP/1.1 204 No Content  
OData-Version: 4.0
```

---

## Delete a record in an elastic table

When deleting a record that uses a custom `partitionid` value, you must include the `partitionid` value.

#### [SDK for .NET](#tab/sdk)

This example deletes a row in `contoso_SensorData` table with specified ID and `partitionid` = `'deviceid-001'`.

```csharp
/// <summary>
/// Demonstrates a delete operation
/// </summary>
/// <param name="service">Authenticated client implementing the IOrganizationService interface</param>
/// <param name="sensordataid">The unique identifier of the contoso_sensordata table.</param>
/// <param name="sessionToken">The current session token</param>
public static void DeleteExample(
   IOrganizationService service, 
   Guid sensordataid, 
   ref string sessionToken)
{
    var request = new DeleteRequest
    {
        Target = new EntityReference("contoso_sensordata", sensordataid),
        ["partitionId"] = "deviceid-001"
    };

    var response = service.Execute(request);
    // Known issue: Value not currently being returned.
    // sessionToken = response.Results["x-ms-session-token"].ToString();
}
```

#### [Web API](#tab/webapi)

This example deletes a row in `contoso_SensorData` table with `contoso_sensordataid` = `02d82842-f3f4-ed11-8848-000d3a993550` and `partitionid` = `'deviceid-001'` using the alternate key style.

**Request**

```http
DELETE [Organization URI]/api/data/v9.2/contoso_sensordatas(contoso_sensordataid=02d82842-f3f4-ed11-8848-000d3a993550,partitionid='deviceid-001')
Content-Type: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0
```

**Response**

```http
HTTP/1.1 204 No Content  
OData-Version: 4.0
```

You could also use the `partitionId` parameter:

`sensordata(02d82842-f3f4-ed11-8848-000d3a993550)?partitionId=deviceid-001`

---

## Next steps

Learn how to create and query JSON data in JSON columns in elastic tables with code

> [!div class="nextstepaction"]
> [Query JSON columns](query-json-columns-elastic-tables.md)<br/>

### See also

[Elastic tables (preview)](elastic-tables.md)<br />
[Create elastic tables using code](create-elastic-tables.md)<br />
[Bulk operations with elastic tables](bulk-operations-elastic-tables.md)<br />
[Query JSON columns in elastic tables (preview)](query-json-columns-elastic-tables.md)<br />
[Elastic table sample code (preview)](elastic-table-samples.md)
