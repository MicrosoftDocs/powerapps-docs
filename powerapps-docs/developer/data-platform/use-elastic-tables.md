---
title: Use elastic tables using code (preview)
description: Learn how to perform data operations on Dataverse elastic tables using code.
ms.topic: how-to
ms.date: 07/21/2023
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

This article describes how to use code to perform data operations on elastic tables.

## Work with the session token

As was mentioned in [Consistency level](elastic-tables.md#consistency-level), you can achieve session-level consistency by passing the current session token with your requests. If you don't include the session token, the data that you retrieve might not include data changes that you've just made.

### Getting the session token

The session token is available in the response of all write operations. Look for the `x-ms-session-token` value.

#### [SDK for .NET](#tab/sdk)

For any [OrganizationResponse](xref:Microsoft.Xrm.Sdk.OrganizationResponse) that performs a write operation, you can capture the `x-ms-session-token` value in the [Results](xref:Microsoft.Xrm.Sdk.OrganizationResponse.Results) collection.

> [!NOTE]
> [DeleteResponse](xref:Microsoft.Xrm.Sdk.Messages.DeleteResponse) doesn't currently return the `x-ms-session-token` value. For more information, go to [Known issue: No x-ms-session-token value is returned for delete operations](elastic-tables.md#no-x-ms-session-token-value-is-returned-for-delete-operations).

```csharp
string sessionToken = response.Results["x-ms-session-token"].ToString();
```

#### [Web API](#tab/webapi)

The session token value is returned as the `x-ms-session-token` response header.

> [!NOTE]
> Delete operations don't currently return the `x-ms-session-token` value. For more information, go to [Known issue: No x-ms-session-token value is returned for delete operations](elastic-tables.md#no-x-ms-session-token-value-is-returned-for-delete-operations).

```http
x-ms-session-token: 240:8#144100870#7=-1
```

---

### Sending the session token

The way that you send the session token in a read operation depends on whether you're using the SDK or Web API.

#### [SDK for .NET](#tab/sdk)

When you perform an operation that retrieves data, set the `SessionToken` optional parameter on [OrganizationRequest](xref:Microsoft.Xrm.Sdk.OrganizationRequest).

```csharp
var request = new RetrieveRequest
{
    Target = new EntityReference("contoso_sensordata", sensordataid),
    ColumnSet = new ColumnSet("contoso_value"),
    ["partitionId"] = deviceId,
    ["SessionToken"] = sessionToken
};
```

[Learn more about using optional parameters](optional-parameters.md).


#### [Web API](#tab/webapi)

When you perform a `GET` operation, use the `MSCRM.SessionToken` request header to pass the corresponding `x-ms-session-token` value to retrieve the most up-to-date row value.

```http
MSCRM.SessionToken: 240:8#144100870#7=-1
```

---

## Specify PartitionId

As was mentioned in [Partitioning and horizontal scaling](elastic-tables.md#partitioning-and-horizontal-scaling), each elastic table has a `partitionid` column that you must use if you choose to apply a partitioning strategy for the table. Otherwise, don't set a value for the `partitionid` column.

After you specify a non-null value for the `partitionid` column when you create a row, you must specify it when you perform any other data operation on that row. You can't change the value later.

If you don't set a `partitionid` value for a record when you create it, the `partitionid` column value remains null, and you can't change it later. In this case, you can identify records by using the primary key, just as you do with standard tables. Specifying a `partitionid` value isn't required.

> [!NOTE]
> The examples in this article assume that you specify a non-null value for the `partitionid` column.

You can set the `partitionid` value in following ways when you perform various data operations.

### Using the alternate key

As was mentioned in [Alternate keys](create-elastic-tables.md#alternate-keys), every elastic table has an alternate key that is named `KeyForNoSqlEntityWithPKPartitionId`. This alternate key combines the primary key of the table with the `partitionid` column.

You can use this alternate key to specify the `partitionid` value when you use `Retrieve`, `Update`, or `Delete` operations.

#### [SDK for .NET](#tab/sdk)

This example shows how you can use the alternate key to specify the `partitionid` value when you use `Retrieve`, `Update`, and `Delete` requests on elastic tables.

```csharp
var keys = new KeyAttributeCollection() {
    { "contoso_sensordataid", sensordataid },
    { "partitionid", deviceId }
};

var entity = new Entity("contoso_sensordata", keys)
```

#### [Web API](#tab/webapi)

This example shows how you can use the special syntax in Web API to refer to records by alternate key when you perform `GET`, `PATCH`, and `DELETE` operations on a single row of an elastic table. [Learn more about using an alternate key to reference a record](use-alternate-key-reference-record.md?tabs=webapi).

`<entity set name>(<primary key name>=<primary key value>,partitionid='<partitionid value>')`

> [!NOTE]
> Because the primary key value is a globally unique identifier (GUID), no single quotation marks are needed around it. However, because the `partitionid` value is a string, single quotation marks are needed.

Here is an example:

```http
/contoso_sensordatas(contoso_sensordataid=e61a662e-68d8-487e-94e7-ae3a22fd4bbd,partitionid='device-001')
```

---
### Using the partitionId parameter

Currently, you can use a `partitionId` parameter to specify the value of the `partitionid` column only for `Retrieve` and `Delete` operations. For more information, go to [Known issue: The partitionId optional parameter isn't available for all messages](elastic-tables.md#the-partitionid-optional-parameter-isnt-available-for-all-messages).

#### [SDK for .NET](#tab/sdk)

> [!NOTE]
> The `partitionId` parameter doesn't work with `Create`, `Update`, or `Upsert` messages, and it is ignored if it's sent.

```csharp
request["partitionId"] = "device-001"
```

#### [Web API](#tab/webapi)

> [!NOTE]
> The `partitionId` parameter doesn't work with `POST` or `PATCH` requests, and it is ignored if it's sent.

Here is an example:

```http
/contoso_sensordatas(<primary key value>)?partitionId='<partitionid value>'
```

---

### Using the partitionid column directly

For `Create`, `Upsert`, or `Update` operations, you can directly specify the value of the `partitionid` column.

#### [SDK for .NET](#tab/sdk)

This example shows how you can directly specify the value of the `partitionid` column in `Entity` when you perform a `Create`, `Upsert`, or `Update` operation.

```csharp
var entity = new Entity("contoso_sensordata", sensordataid)
{
    Attributes = {
        { "partitionid", "device-001" }
    }
};
```

#### [Web API](#tab/webapi)

This example shows how you can directly specify the value of the `partitionid` column in the request body when you make a `POST` or `PATCH` request.

```json
{
    "partitionid": "deviceid-001"
}
```

---

## Create a record in an elastic table

This example creates a row in the `contoso_SensorData` table, where `partitionid` is set to `deviceid`. It also sets the `ttlinseconds` column to ensure that the row expires after one day (86,400 seconds) and is automatically deleted from Dataverse.

This example also captures the `x-ms-session-token` value that you can use when you retrieve the created record.

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

Use the `x-ms-session-token` value that is returned to set the `SessionToken` optional parameter when you retrieve the record that you created. [Learn more about sending the session token](#sending-the-session-token).

#### [Web API](#tab/webapi)

**Request:**

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

**Response:**

```http
HTTP/1.1 204 No Content
OData-Version: 4.0
x-ms-session-token: 240:8#144035050#7=-1
OData-EntityId: [Organization URI]/api/data/v9.2/sensordata(7eb682f1-ca75-e511-80d4-00155d2a68d1)
```

Use the `x-ms-session-token` value that is returned with the `MSCRM.SessionToken` request header to retrieve the latest version of a record. [Learn more about sending the session token](#sending-the-session-token).

---

## Update a record in an elastic table

This example updates the `contoso_value` and `contoso_timestamp` values of an existing row in the `contoso_SensorData` table by using the `contoso_sensordataid` primary key and `partitionid` = `'device-001'`.

If you're using a partitioning strategy, the primary key and `partitionid` columns must uniquely identify an existing elastic table row. The `partitionid` value of an existing row can't be updated and is used only to uniquely identify the row to update.

This example uses the `KeyForNoSqlEntityWithPKPartitionId` alternate key to uniquely identify the record by using both the primary key and `partitionid` values. [Learn more about alternate keys](create-elastic-tables.md#alternate-keys).

#### [SDK for .NET](#tab/sdk)

This example shows how to use the `partitionid` value as an alternate key.

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

[Learn more about using the Entity class to set alternate keys](use-alternate-key-reference-record.md#using-the-entity-class).

#### [Web API](#tab/webapi)

**Request:**

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

**Response:**

```http
HTTP/1.1 204 No Content
OData-Version: 4.0
OData-EntityId: [Organization URI]/api/data/v9.2/contoso_sensordatas(contoso_sensordataid=21d455f2-70f3-ed11-8848-000d3a993550,partitionid='deviceid-001')
x-ms-session-token: 240:8#144035978#7=-1
```

---

## Retrieve a record in an elastic table

If the `partitionid` value was set when an elastic table record was created, you must use it together with the primary key value to uniquely identify a record.

If the `partitionid` wasn't set, you can retrieve the record in the usual way, by using only the primary key value.

#### [SDK for .NET](#tab/sdk)

There are two different ways to compose a request to retrieve a record by using the `partitionid` value.

This example uses the [RetrieveRequest class](xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest). The `Target` property is set to an [EntityReference](xref:Microsoft.Xrm.Sdk.EntityReference) that is created by using the constructor that accepts a [KeyAttributeCollection](xref:Microsoft.Xrm.Sdk.KeyAttributeCollection) to use the `KeyForNoSqlEntityWithPKPartitionId` alternate key. [Learn more about using the EntityReference class with alternate keys](use-alternate-key-reference-record.md#using-the-entityreference-class).


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

This example uses an optional parameter that is named `partitionId` on the [RetrieveRequest class](xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest). [Learn more about using optional parameters](optional-parameters.md).

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

This example uses the `partitionId` query parameter.

**Request:**

```http
GET [Organization URI]/api/data/v9.2/sensordata(<sensordataid value>)?partitionId=deviceid-001&$select=contoso_value,contoso_timestamp
Accept: application/json
Content-Type: application/json
MSCRM.SessionToken : htjy#4567
OData-MaxVersion: 4.0
OData-Version: 4.0
```

**Response:**

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

You can also use the alternate key.

`contoso_sensordatas(contoso_sensordataid=<Guid Value>,partitionId='deviceid-001')`

---

## Query rows of an elastic table

When you query the rows of an elastic table, you get the best performance if you limit your query to a specific partition. Otherwise, your query returns data across all logical partitions, which isn't as fast.

> [!NOTE]
> When you use this approach, the parameter must use the name `partitionId` (with a capital *I*) instead of `partitionid` (in all lowercase letters).
> 
> When you specify a filter this way, you don't have to specify the filter criteria on `partitionid` in your query in the usual manner (that is, by using FetchXML `condition`, [QueryExpression](xref:Microsoft.Xrm.Sdk.Query.QueryExpression) [ConditionExpression](xref:Microsoft.Xrm.Sdk.Query.ConditionExpression), or Web API `$filter`).
> 
> Specifying a filter on the `partitionid` value in the usual manner doesn't have the same performance benefits as specifying it through the `partitionId` parameter as shown in the following examples.

These examples retrieve the first 5,000 rows in the `contoso_SensorData` table that belong to the logical partition where `partitionid` = `'deviceid-001'`.

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

**Request:**

```http
GET [Organization URI]/api/data/v9.2/sensordata?partitionId=deviceid-001
&$select=contoso_sensortype,contoso_value,contoso_timestamp
Accept: application/json
Content-Type: application/json
OData-MaxVersion: 4.0
OData-Version: 4.0
```

**Response:**

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

Elastic tables don't currently support returning related rows when a query is run. If you try to return related rows, Dataverse throws an error with code `0x80048d0b` and the following message:

> `Link entities are not supported`.

However, elastic tables do support returning related rows when a single row is retrieved.

## Upsert a record in an elastic table

> [!IMPORTANT]
> Upsert operations with elastic tables differ from upsert operations with standard tables. Upsert operations are expected to contain the full payload and will overwrite any existing record data. They don't call the `Create` or `Update` messages. [Learn more about elastic table upsert](use-upsert-insert-update-record.md#elastic-table-upsert).

With elastic tables, if a record that has a given ID and `partitionid` doesn't exist, it's created. If it already exists, it's replaced.

#### [SDK for .NET](#tab/sdk)

This example upserts a row in the `contoso_SensorData` table with the specified `id` value and `partitionid` = `deviceid-001`.

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

This example upserts a row in the `SensorData` table with ID = `ff67610c-82ce-412c-85df-0bbc6521bb01` and `partitionid` = `'deviceid-001'`.

> [!NOTE]
> Upsert is identical to update, except the `If-Match: *` request header isn't included.

**Request:**

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

**Response:**

```http
HTTP/1.1 204 No Content
OData-Version: 4.0
```

---

## Delete a record in an elastic table

When you delete a record that uses a custom `partitionid` value, you must include the `partitionid` value.

#### [SDK for .NET](#tab/sdk)

This example deletes a row in the `contoso_SensorData` table with the specified ID and `partitionid` = `'deviceid-001'`.

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

This example uses the alternate key style to delete a row in the `contoso_SensorData` table with `contoso_sensordataid` = `02d82842-f3f4-ed11-8848-000d3a993550` and `partitionid` = `'deviceid-001'`.

**Request:**

```http
DELETE [Organization URI]/api/data/v9.2/contoso_sensordatas(contoso_sensordataid=02d82842-f3f4-ed11-8848-000d3a993550,partitionid='deviceid-001')
Content-Type: application/json
OData-MaxVersion: 4.0
OData-Version: 4.0
```

**Response:**

```http
HTTP/1.1 204 No Content
OData-Version: 4.0
```

You can also use the `partitionId` parameter:

`sensordata(02d82842-f3f4-ed11-8848-000d3a993550)?partitionId=deviceid-001`

---

## Bulk operations with elastic tables

Often, applications must ingest a large amount of data into Dataverse in a short time. Dataverse has a group of messages that are designed to achieve high throughput. With elastic tables, the throughput can be even higher.

Bulk operations are optimized for performance when multiple write operations are performed on the same table by taking a batch of rows as input in a single write operation. [Learn more about bulk Operation messages (preview)](bulk-operations.md).

### Use CreateMultiple with elastic tables

You can use the `CreateMultiple` message with either the SDK for .NET or Web API.

#### [SDK for .NET](#tab/sdk)

This example uses the [CreateMultipleRequest class](xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest) to create multiple rows in the `contoso_SensorData` elastic table.

```csharp
public static Guid CreateMultiple(IOrganizationService service)
{
    string tableLogicalName = "contoso_sensordata";

    List<Microsoft.Xrm.Sdk.Entity> entityList = new List<Microsoft.Xrm.Sdk.Entity>
    {      
        new Microsoft.Xrm.Sdk.Entity(tableLogicalName)
        {
            Attributes =
            {
                { "contoso_deviceId", "deviceid-001" },
                { "contoso_sensortype", "Humidity" },
                { "contoso_value", "40" },
                { "contoso_timestamp", "2023-05-01Z05:00:00"},
                { "partitionid", "deviceid-001" },
                { "ttlinseconds", 86400 }
            }
        },
        new Microsoft.Xrm.Sdk.Entity(tableLogicalName)
        {
            Attributes =
            {
                { "contoso_deviceId", "deviceid-002" },
                { "contoso_sensortype", "Humidity" },
                { "contoso_value", "10" },
                { "contoso_timestamp", "2023-05-01Z09:30:00"},
                { "partitionid", "deviceid-002" },
                { "ttlinseconds", 86400 }
            }
        }
        new Microsoft.Xrm.Sdk.Entity(tableLogicalName)
        {
            Attributes =
            {
                { "contoso_deviceId", "deviceid-002" },
                { "contoso_sensortype", "Pressure" },
                { "contoso_value", "20" },
                { "contoso_timestamp", "2023-05-01Z07:20:00"},
                { "partitionid", "deviceid-002" },
                { "ttlinseconds", 86400 }
            }
        }
    };

    // Create an EntityCollection populated with the list of entities.
    EntityCollection entities = new(entityList)
    {
        EntityName = tableLogicalName
    };

    // Use CreateMultipleRequest
    CreateMultipleRequest createMultipleRequest = new()
    {
        Targets = entities,
    };
    return service.Execute(request);
}
```

#### [Web API](#tab/webapi)

This example shows how to use the [CreateMultiple action](xref:Microsoft.Dynamics.CRM.CreateMultiple) to create multiple rows in the `contoso_SensorData` elastic table. The `partitionid` value is included to uniquely identify the rows. These operations set the `contoso_deviceid`,`contoso_sensortype`, `partitionid`, and `ttlinseconds` properties.

**Request:**

```http
POST [Organization Uri]/api/data/v9.2/contoso_sensordatas/Microsoft.Dynamics.CRM.CreateMultiple
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
Content-Type: application/json; charset=utf-8
Content-Length: 741

{
    "Targets": [
        {
            "@odata.type": "Microsoft.Dynamics.CRM.contoso_sensordata",
            "contoso_deviceid": "Device-ABC-1234",
            "contoso_sensortype": "Humidity",
            "partitionid": "Device-ABC-1234",
            "ttlinseconds": 86400
        },
        {
            "@odata.type": "Microsoft.Dynamics.CRM.contoso_sensordata",
            "contoso_deviceid": "Device-ABC-1234",
            "contoso_sensortype": "Humidity",
            "partitionid": "Device-ABC-1234",
            "ttlinseconds": 86400
        },
        {
            "@odata.type": "Microsoft.Dynamics.CRM.contoso_sensordata",
            "contoso_deviceid": "Device-ABC-1234",
            "contoso_sensortype": "Humidity",
            "partitionid": "Device-ABC-1234",
            "ttlinseconds": 86400
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
        "6114ca58-0928-ee11-9965-6045bd5cd155",
        "6214ca58-0928-ee11-9965-6045bd5cd155",
        "6314ca58-0928-ee11-9965-6045bd5cd155"
    ]
}
```

---

### Use UpdateMultiple with elastic tables

You can use the `UpdateMultiple` message with either the SDK for .NET or Web API.

#### [SDK for .NET](#tab/sdk)

This example uses the [UpdateMultipleRequest class](xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest) to update multiple rows of the `contoso_SensorData` elastic table. These updates set the `contoso_value` column.

```csharp
public static Guid UpdateMultiple(IOrganizationService service)
{
    string tableLogicalName = "contoso_sensordata";

    List<Microsoft.Xrm.Sdk.Entity> entityList = new List<Microsoft.Xrm.Sdk.Entity>
    {
        new Microsoft.Xrm.Sdk.Entity(tableLogicalName)
        {
            Attributes =
            {
                { "contoso_value", "45" },
                { "partitionid", "deviceid-001" }
            }
        },
        new Microsoft.Xrm.Sdk.Entity(tableLogicalName)
        {
            Attributes =
            {
                { "contoso_value", "15" },
                { "partitionid", "deviceid-002" }
            }
        }
        new Microsoft.Xrm.Sdk.Entity(tableLogicalName)
        {
            Attributes =
            {
                { "contoso_value", "25" },
                { "partitionid", "deviceid-002" }
            }
        }
    };

    // Create an EntityCollection populated with the list of entities.
    EntityCollection entities = new(entityList)
    {
        EntityName = tableLogicalName
    };

    // Use UpdateMultipleRequest
    UpdateMultipleRequest updateMultipleRequest = new()
    {
        Targets = entities,
    };
    return service.Execute(request);
}
```

#### [Web API](#tab/webapi)

This example shows how to use the [UpdateMultiple action](xref:Microsoft.Dynamics.CRM.UpdateMultiple) to update multiple rows of the `contoso_SensorData` elastic table. The `partitionid` value is included to uniquely identify the rows. These updates set the `contoso_energyconsumption` property.

**Request:**

```http
POST [Organization Uri]/api/data/v9.2/contoso_sensordatas/Microsoft.Dynamics.CRM.UpdateMultiple
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
Content-Type: application/json; charset=utf-8
Content-Length: 954

{
    "Targets": [
        {
            "@odata.type": "Microsoft.Dynamics.CRM.contoso_sensordata",
            "contoso_sensordataid": "6114ca58-0928-ee11-9965-6045bd5cd155",
            "partitionid": "Device-ABC-1234",
            "contoso_energyconsumption": "{\"power\":2,\"powerUnit\":\"Watts\",\"voltage\":1,\"voltageUnit\":\"Volts\"}"
        },
        {
            "@odata.type": "Microsoft.Dynamics.CRM.contoso_sensordata",
            "contoso_sensordataid": "6214ca58-0928-ee11-9965-6045bd5cd155",
            "partitionid": "Device-ABC-1234",
            "contoso_energyconsumption": "{\"power\":4,\"powerUnit\":\"Watts\",\"voltage\":2,\"voltageUnit\":\"Volts\"}"
        },
        {
            "@odata.type": "Microsoft.Dynamics.CRM.contoso_sensordata",
            "contoso_sensordataid": "6314ca58-0928-ee11-9965-6045bd5cd155",
            "partitionid": "Device-ABC-1234",
            "contoso_energyconsumption": "{\"power\":6,\"powerUnit\":\"Watts\",\"voltage\":3,\"voltageUnit\":\"Volts\"}"
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

### Use DeleteMultiple with elastic tables

You can use the `DeleteMultiple` message with either the SDK for .NET or Web API.

#### [SDK for .NET](#tab/sdk)

> [!NOTE]
> With the SDK, you must use the [OrganizationRequest class](xref:Microsoft.Xrm.Sdk.OrganizationRequest) because the SDK doesn't currently have a `DeleteMultipleRequest` class. [Learn more about using messages with the Organization service](org-service/use-messages.md).

The following `DeleteMultipleExample` static method uses the `DeleteMultiple` message with the [OrganizationRequest class](xref:Microsoft.Xrm.Sdk.OrganizationRequest) to delete multiple rows from the `contoso_SensorData` elastic table. The alternate key is used to include the `partitionid` value to uniquely identify the rows.

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

#### [Web API](#tab/webapi)

This example shows how to use the `DeleteMultiple` action to delete multiple rows from `contoso_SensorData` elastic table. The `partitionid` value is included to uniquely identify the rows.

> [!NOTE]
> Currently, the Web API `DeleteMultiple` action is a private action. You won't find it in the [CSDL $metadata document](webapi/web-api-service-documents.md#csdl-metadata-document) or in the Dataverse <xref:Microsoft.Dynamics.CRM.ActionIndex?displayProperty=fullName>. This action will become public in the coming weeks. You can use it while it's private.

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

## Next steps

Learn how to use code to create and query JavaScript Object Notation (JSON) data in JSON columns in elastic tables.

> [!div class="nextstepaction"]
> [Query JSON columns](query-json-columns-elastic-tables.md)<br/>

### See also

[Elastic tables for developers (preview)](elastic-tables.md)  
[Create elastic tables using code (preview)](create-elastic-tables.md)  
[Query JSON columns in elastic tables (preview)](query-json-columns-elastic-tables.md) 
[Elastic table sample code (preview)](elastic-table-samples.md)  
[Bulk operation messages (preview)](bulk-operations.md)
