---
title: "Use elastic tables (Preview) (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn how to use elastic tables with code" # 115-145 characters including spaces. This abstract displays in the search result.
ms.topic: article
ms.date: 05/14/2022
author: pnghub
ms.author: gned
ms.reviewer: jdaly
search.audienceType: 
  - developer
contributors:
 - sumantb-msft
 - JimDaly
---

# Use elastic tables (Preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

> [!IMPORTANT]
> This is a preview feature.
> 
> [!INCLUDE [cc-preview-features-definition](../../includes/cc-preview-features-definition.md)]

<!-- 
Maker topics to refer to from https://github.com/MicrosoftDocs/powerapps-docs-pr/pull/8083
These are in the peakerbl-1 branch.

Create and edit elastic tables (preview)
https://review.learn.microsoft.com/en-us/power-apps/maker/data-platform/create-edit-elastic-tables?branch=pr-en-us-8083

Create and edit tables using Power Apps
https://review.learn.microsoft.com/en-us/power-apps/maker/data-platform/create-edit-entities-portal?branch=pr-en-us-8083

Types of tables
https://review.learn.microsoft.com/en-us/power-apps/maker/data-platform/types-of-entities?branch=pr-en-us-8083

-->
Dataverse elastic tables are powered by Azure Cosmos DB. They automatically scale horizontally and can handle large amounts of data and high levels of throughput with low latency. Elastic tables are suitable for applications with unpredictable, spiky or rapidly growing workloads.

## When to use elastic tables

Whether you should use an elastic table depends on the specific needs of your data and your application.

Use elastic tables when:

- Your data is unstructured or semi-structured, or if your data model is constantly changing.
- You need automatic horizontal scaling.
- You need to handle a high volume of read and write requests.

Use standard tables when:

- Your application requires strong data consistency.
- Your application requires relational modeling and needs transactional capability across tables and during plugin execution stages.
- Your application requires complex joins.

The choice of table should be based on the specific needs of your application. A combination of both types of tables may be appropriate.

### Partitioning and horizontal scaling

Elastic tables use Azure Cosmos DB partitioning to scale individual tables to meet the performance needs of your application. All elastic tables contain a system-defined **Partition Id** string column with the schema name `PartitionId` and logical name `partitionid`.

Azure Cosmos DB ensures that the rows in a table are divided into distinct subsets called [logical partitions](/azure/cosmos-db/partitioning-overview#logical-partitions) which are formed based on the value of `partitionid` column of each row.

#### Choosing a PartitionId value

The `partitionid` value you should use depends on the nature of your data.  A logical partition in an elastic table consists of a set of rows that have the same `partitionid`. For example, in a table that contains data about various products, you can use product category as the `partitionid` for the table. Groups of items that have specific values for product category, such as Clothing, Books, Electronic Appliances and Pet supplies, form distinct logical partitions.

Dataverse transparently and automatically manages logical partitions associated with a table. There is no limit on the number of logical partitions you can have in a table. You also don't have to worry about deleting a logical partition when the underlying rows belonging to that partition is deleted.

For all elastic tables, `partitionid` column should:

- Have a value which doesn't change. Once a row is created with a `partitionid` value, you cannot change it.
- Have a high cardinality value. In other words, the property should have a wide range of possible values. Each logical partition can store 20 GB of data. So, choosing a `partitionid` with a wide range of possible values ensures that the table can scale without reaching limits for any specific logical partition.
- Spread data as evenly as possible between all logical partitions.
- Have values that are no larger than 1024 bytes.

When `partitionid` is not specified for a row, Dataverse uses the primary key as the default `partitionid`. For write-heavy tables of any size or for cases where rows are mostly retrieved using id, the primary key is naturally a great choice for the `partitionid` column.

### Consistency level

Elastic table supports strong consistency within a logical session. A logical session here represents a logical connection between client and Dataverse. When a client performs a write operation on an elastic tables, it receives a session token that uniquely identifies this logical session. The session token is then included in subsequent requests to maintain the logical session context.

With session tokens, all the read operations performed within the same logical session will return the most recent write made within that logical session. In other words, reads are guaranteed to honor the read-your-writes, and write-follows-reads guarantees within a logical session. If a different logical session performs a write operation, other logical sessions may not see those changes immediately.

You will find session token as `x-ms-session-token` header in response of all write operations.  

When calling a retrieve API, you can use `MSCRM.SessionToken` header to pass corresponding `x-ms-session-token` to retrieve the most up-to-date row. If you retrieve a record without a session token, the changes applied recently may not be applied, but will eventually be returned.

<!-- Elastic tables support [session consistency](/azure/cosmos-db/consistency-levels#session-consistency). Elastic tables use *session tokens* to achieve session consistency. Session tokens are opaque strings returned by Dataverse when your client performs any write operation (create/update/delete).

When your client performs a subsequent read operation, include the session token in the request, allowing Dataverse to return the most up-to-date data for that client. -->

#### Getting the session token

You will find session token as `x-ms-session-token` header in response of all write operations.

#### [SDK for .NET](#tab/sdk)

For any [OrganizationResponse](xref:Microsoft.Xrm.Sdk.OrganizationResponse) that performs a write operation ([CreateResponse](xref:Microsoft.Xrm.Sdk.Messages.CreateResponse),[UpdateResponse](xref:Microsoft.Xrm.Sdk.Messages.UpdateResponse),[UpsertResponse](xref:Microsoft.Xrm.Sdk.Messages.UpsertResponse),[DeleteResponse](xref:Microsoft.Xrm.Sdk.Messages.DeleteResponse)) you can capture the `x-ms-session-token` in the [Results](xref:Microsoft.Xrm.Sdk.OrganizationResponse.Results) collection.

> [!NOTE]
> [DeleteResponse](xref:Microsoft.Xrm.Sdk.Messages.DeleteResponse) does not currently return the x-ms-session-token. More information: [Known issues: x-ms-session-token value not returned for delete operations](#x-ms-session-token-value-not-returned-for-delete-operations)

```csharp
string sessionToken = response.Results["x-ms-session-token"].ToString();
```

#### [Web API](#tab/webapi)

The session token value will be returned as the `x-ms-session-token` response header.

> [!NOTE]
> DELETE operations do not currently return the x-ms-session-token. More information: [Known issues: x-ms-session-token value not returned for delete operations](#x-ms-session-token-value-not-returned-for-delete-operations)

```http
x-ms-session-token: 240:8#144100870#7=-1
```

---

#### Sending the session token

How you send the session token in a read operation depends on whether you are using the SDK or Web API.
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

#### [Web API](#tab/webapi)

When performing a `GET` operation, use `MSCRM.SessionToken` request header to pass corresponding `x-ms-session-token` to retrieve the most up-to-date row value.

```http
MSCRM.SessionToken: 240:8#144100870#7=-1
```
---

### Transactional behavior

Elastic tables do not support multi-record transactions. This means that for a single request execution, multiple write operation happening in same or different synchronous plugin stages are not transactional with each other.

For example, if you have a synchronous plug-in step registered on the PostOperation stage for Create message on an elastic table, any error in your plug-in will not roll back the created record in Dataverse.

Multiple write operations within same the plugin execution are also not atomic.

Elastic tables also do not support grouping requests in a single database transaction using the SDK [ExecuteTransactionRequest](xref:Microsoft.Xrm.Sdk.Messages.ExecuteTransactionRequest) class or in a Web API `$batch` operation change set.  More information:

- [Execute messages in a single database transaction](org-service/use-executetransaction.md)
- [Change sets](webapi/execute-batch-operations-using-web-api.md#change-sets)
- [Known issue: Error not returned when grouping elastic table data operations in a transaction](#error-not-returned-when-grouping-elastic-table-data-operations-in-a-transaction)


## Scenario

The examples in the rest of this article will use this scenario.

Imagine Contoso operates large number of Internet of Things (IoT) devices deployed by the company all across the world. Contoso needs to store and query large amounts of sensor data being emitted from IoT devices so that they can monitor health of device and gathering other insights.

Contoso can create an elastic table named `contoso_SensorData` to store and query large volume of IoT data. It can choose to use a string column named `contoso_DeviceId` as the partitionid value for each row corresponding to that device. Since `contoso_DeviceId` is unique to each device and Contoso performs queries mostly in context of a given `contoso_DeviceId`, it acts as a good partition strategy for entire dataset.

## Create elastic tables

You can create elastic tables using [Power Apps](https://make.powerapps.com/) without writing code. More information: [Create and edit tables using Power Apps](../../maker/data-platform/create-edit-entities-portal.md). 

These examples create a new elastic table `contoso_SensorData` using the Dataverse SDK for .NET and Web API. Use the `EntityMetadata.TableType` property with a value of `Elastic` to create an elastic table with code.

#### [SDK for .NET](#tab/sdk)

> [!NOTE]
> At the time of this writing the SDK [EntityMetadata](xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata) class doesn't have the `TableType` property to create an elastic table. You will need to use the Web API until this is added.
>
> After the SDK is updated, you will be able to use the [CreateEntityRequest](xref:Microsoft.Xrm.Sdk.Messages.CreateEntityRequest> class as shown below.

```csharp
public static CreateEntityResponse CreateElasticTable(IOrganizationService service)
{
   var request = new CreateEntityRequest
   {
         // Define table properties
         Entity = new EntityMetadata
         {
            SchemaName = "contoso_SensorData",
            DisplayName = new Label("SensorData", 1033),
            DisplayCollectionName = new Label("SensorData", 1033),
            Description = new Label("Stores IoT data emitted from devices", 1033),
            OwnershipType = OwnershipTypes.UserOwned,
            TableType = "Elastic",
            IsActivity = false,
            CanCreateCharts = new Microsoft.Xrm.Sdk.BooleanManagedProperty(false)
         },

         // Define the primary attribute for the entity
         PrimaryAttribute = new StringAttributeMetadata
         {
            SchemaName = "contoso_SensorType",
            RequiredLevel = new AttributeRequiredLevelManagedProperty(AttributeRequiredLevel.None),
            MaxLength = 100,
            FormatName = StringFormatName.Text,
            DisplayName = new Label("Sensor Type", 1033),
            Description = new Label("Type of sensor emitting data", 1033)
         }

   };
   return (CreateEntityResponse)service.Execute(request);
}
``` 

More information: [Create a custom table using code](org-service/create-custom-entity.md)

#### [Web API](#tab/webapi)

Set the [EntityMetadata](xref:Microsoft.Dynamics.CRM.EntityMetadata) `TableType` property to `Elastic`.

**Request**

```http
POST [Organization URI]/api/data/v9.2/EntityDefinitions
Content-Type: application/json
OData-MaxVersion: 4.0
OData-Version: 4.0

{
  "@odata.type": "Microsoft.Dynamics.CRM.EntityMetadata",
  "SchemaName": "contoso_SensorData",
  "TableType": "Elastic",
  "DisplayName": {
    "@odata.type": "Microsoft.Dynamics.CRM.Label",
    "LocalizedLabels": [
      {
        "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
        "Label": "SensorData",
        "LanguageCode": 1033
      }
    ]
  },
  "Description": {
    "@odata.type": "Microsoft.Dynamics.CRM.Label",
    "LocalizedLabels": [
      {
        "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
        "Label": "Stores IoT data emitted from devices",
        "LanguageCode": 1033
      }
    ]
  },
  "DisplayCollectionName": {
    "@odata.type": "Microsoft.Dynamics.CRM.Label",
    "LocalizedLabels": [
      {
        "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
        "Label": "SensorData",
        "LanguageCode": 1033
      }
    ]
  },
  "HasActivities": false,
  "HasNotes": false,
  "IsActivity": false,
  "IsActivityParty": false,
  "OwnershipType": "UserOwned",
  "CanChangeTrackingBeEnabled": {
    "Value": true,
    "CanBeChanged": true
  },
  "ChangeTrackingEnabled": true,
  "CanCreateCharts": {
    "Value": false,
    "CanBeChanged": true
  },
  "Attributes": [
    {
      "SchemaName": "contoso_SensorType",
      "@odata.type": "Microsoft.Dynamics.CRM.StringAttributeMetadata",
      "FormatName": {
        "Value": "Text"
      },
      "AttributeType": "String",
      "AttributeTypeName": {
        "Value": "StringType"
      },
      "Description": {
        "@odata.type": "Microsoft.Dynamics.CRM.Label",
        "LocalizedLabels": [
          {
            "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
            "Label": "Type of sensor reporting data",
            "LanguageCode": 1033
          }
        ]
      },
      "DisplayName": {
        "@odata.type": "Microsoft.Dynamics.CRM.Label",
        "LocalizedLabels": [
          {
            "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",
            "Label": "Sensor Type",
            "LanguageCode": 1033
          }
        ]
      },
      "IsPrimaryName": true,
      "RequiredLevel": {
        "Value": "None",
        "CanBeChanged": true,
        "ManagedPropertyLogicalName": "canmodifyrequirementlevelsettings"
      },
      "MaxLength": 100
    }
  ]
}
```

**Response**

```http
HTTP/1.1 204 No Content  
OData-Version: 4.0  
OData-EntityId: [Organization URI]/api/data/v9.2/EntityDefinitions(417129e1-207c-e511-80d2-00155d2a68d2) 
```

More information: [Create and update table definitions using the Web API](webapi/create-update-entity-definitions-using-web-api.md)

---

## Adding Columns

You can create columns in elastic tables using [Power Apps](https://make.powerapps.com/) without writing code. More information: [Create and edit tables using Power Apps](../../maker/data-platform/create-edit-entities-portal.md). 

Dataverse automatically creates two system columns for each elastic tables at the time of table creation.


|SchemaName<br />LogicalName|Type  |Description|
|---------|---------|---------|
|`PartitionId`<br />`partitiond`|String|Defines the logical partition a row belongs to.|
|`TTLInSeconds`<br />`ttlinseconds` |Integer|Defines the time in seconds after which row will expire and get deleted from database automatically.|


Columns can also be created using the SDK or Web API, but there are limits on the types of columns you can add. Currently you cannot add these types of columns:

- Money (`MoneyAttributeMetadata`)
- MultiSelectPicklist (`MultiSelectPicklistAttributeMetadata`)
- State (`StateAttributeMetadata`)
- Status (`StatusAttributeMetadata`)
- File (`FileAttributeMetadata`)
- Image (`ImageAttributeMetadata`)
- Calculated, Rollup, or Formula Columns

Elastic tables support string columns that store JSON data. More information: [Create a column with Json format](#create-a-column-with-json-format)



## Alternate keys

You cannot create custom alternate keys for elastic tables.

Each elastic table is created with one alternate key using these values:

- Display Name: Entity key for NoSql Entity that contains PrimaryKey and PartitionId attributes
- Name: `KeyForNoSqlEntityWithPKPartitionId`
- LogicalName: `keyfornosqlentitywithpkpartitionid`

This alternate key has the key values: `<table primary key name>` and `partitionid`.

If you need to reference a record that has a `partitionid` value set to a value other than the default value that is equal to the value of the primary key, you can reference the record using this alternate key.

More information: [Use an alternate key to reference a record](use-alternate-key-reference-record.md)

## Adding Relationships

Dataverse currently does not support creating Many-to-Many relationships with elastic tables.

One-to-Many relationships are supported for elastic tables with following limitations:

- Cascading is not supported. Cascading behavior must be set to `Cascade.None` when creating relationship.
- Formatted values for lookup columns are not returned when the following conditions are true:

   - The table being retrieved is a standard table and the lookup refers to an elastic table.
   - The elastic table `partitionid` value is set to a value other than the primary key value of the elastic table row.

Although elastic table supports having One-to-Many relationships and get related rows using fetchXml, there are restrictions when it comes retrieving data using fetchXml from related tables. In FetchXML queries, the `link-type` attribute is used within the `<link-entity>` element to specify the type of join between two tables. Elastic table only supports `outer` link-type. Elastic tables does not support `inner` link-type.

Here's an example that demonstrates the usage of the outer "link-type" attribute for elastic tables

```xml
<fetch>
   <entity name="contoso_sensordata">
      <attribute name="contoso_sensortype"/>
      <attribute name="contoso_value"/>
      <order attribute="contoso_timestamp" descending="false"/>
      <attribute name="toasttype"/>
      <link-entity name="Devices" alias="devices" link-type="inner" from="contoso_deviceid" to="contoso_deviceid">
         <attribute name="contoso_OwnerName" />
         <attribute name="contoso_OwnerEmailAddres" />
         <filter type="and">
            <condition attribute="contoso_location" operator="eq" value="Seattle"/>
         </filter>
      </link-entity>
   </entity>
</fetch>
```

In the above example, the `link-type` attribute is set to `outer` within the `<link-entity>` element. This means that all records from the `contoso_SensorData` entity will be retrieved, regardless of whether they have related records in the `contoso_Devices` entity. If a related record exists, the attributes `contoso_OwnerName` and `contoso_OwnerEmail` from the `contoso_Devices` table will be included in the query results. If no related record is found, null values will be returned for these columns.

If the `link-type` is set to `inner`, Dataverse will throw an error with code `0x80048d0b` and message **Link entities are not supported**.
To perform inner join operation across two tables when working with elastic tables, it is recommended that 
- Either columns from related tables are denormalized into main table so that filter can be applied on a single table without join requirement, or
- Two queries are performed on both table separately with appropriate conditions and do in-memory join on client side.

<!-- 
Try to simplify with the description above.

> Although elastic table supports having One-to-Many relationships and fetch related rows using fetchXml or OData  `$expand`, adding filters on related tables is not supported. This is because elastic tables cannot perform join operations between two tables. 

TODO: Does an error occur if you try to add a filter? Or is the filter just ignored?

-->

## Elastic table data operations

Following examples show how to work with data stored in an elastic table.

- [Create a record in an elastic table](#create-a-record-in-an-elastic-table)
- [Update a record in an elastic table](#update-a-record-in-an-elastic-table)
- [Retrieve a record in an elastic table](#retrieve-a-record-in-an-elastic-table)
- [Query rows of an elastic table](#query-rows-of-an-elastic-table)
- [Upsert a record in an elastic table](#upsert-a-record-in-an-elastic-table)
- [Delete a record in an elastic table](#delete-a-record-in-an-elastic-table)


### Create a record in an elastic table

This example creates a new row in `contoso_SensorData` table with `partitionid` set to `deviceid`. It also sets `ttlinseconds` column which ensures that row expires after 1 day (86400 seconds) and deleted from Dataverse automatically.

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
public static Guid CreateExample(IOrganizationService service, string deviceId, ref string sessionToken )
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

Use the `x-ms-session-token` value returned to set the `SessionToken` optional parameter when retrieving the record. More information: [Sending the session token](#sending-the-session-token)

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

### Update a record in an elastic table

This example updates the `contoso_value` and `contoso_timestamp` values of an existing row in `contoso_SensorData` table with using the `contoso_sensordataid` primary key and `partitionid` = `'device-001'`. Note that primary key and `partitionid` columns are always required to uniquely identify an existing elastic table row. The `partitionid` of an existing row cannot be updated and is only being used to uniquely identify the row to update.

This example uses the `KeyForNoSqlEntityWithPKPartitionId` alternate key to uniquely identify the record using both the primary key and the `partitionid`. More information: [Alternate keys](#alternate-keys)

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
public static void UpdateExample(IOrganizationService service, Guid sensordataid, string deviceId, ref string sessionToken)
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

This example shows using the `partitionId` optional parameter.

```csharp
/// <summary>
/// Demonstrates updating elastic table row with partitionid set as optional Parameter.
/// </summary>
/// <param name="service">Authenticated client implementing the IOrganizationService interface</param>
/// <param name="sensordataid">The unique identifier of the contoso_sensordata table.</param>
/// <param name="deviceId">The value used as partitionid for the contoso_sensordata table. </param>
/// <param name="sessionToken">The current session token</param>
public static void UpdateExampleOptionalParameter(
    IOrganizationService service, 
    Guid sensordataid, 
    string deviceId, 
    ref string sessionToken)
{

    var entity = new Entity("contoso_sensordata", sensordataid)
    {
        Attributes = {
            { "contoso_value", 60 },
            { "contoso_timestamp", DateTime.UtcNow }
        }
    };

    var request = new UpdateRequest { 
        Target = entity,
        ["partitionId"] = deviceId,
        ["SessionToken"] = sessionToken
    };

    var response = (UpdateResponse)service.Execute(request);

    // Capture the session token
    sessionToken = response.Results["x-ms-session-token"].ToString();

}
```

#### [Web API](#tab/webapi)

When applying an update, you need to uniquely identify the record you are going to update.

- You can use the alternate key style:

   `contoso_sensordatas(contoso_sensordataid=<primary key value>,partitionid='<partitionid value>')`

   More information: [Use an alternate key to reference a record](use-alternate-key-reference-record.md?tabs=webapi)

- Or you can use the `partitionId` query parameter.

   `contoso_sensordatas(<primary key value>)?partitionId='<partitionid value>'`

The following example uses the alternate key style.

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

### Retrieve a record in an elastic table

If an elastic table record was created setting the `partitionid`, you must use the `partitionid` value together with the primary key value to uniquely identify a record.

If the `partitionid` was not set, you can retrieve the record normally using only the primary key value.

#### [SDK for .NET](#tab/sdk)

There are two different ways to compose a request to retrieve a record using the `partitionid` value.

This example uses the [RetrieveRequest](xref:Microsoft.Xrm.Sdk.Messages.RetrieveRequest) class with the `Target` property set to an the [EntityReference](xref:Microsoft.Xrm.Sdk.EntityReference) created using the constructor that accepts a [KeyAttributeCollection](xref:Microsoft.Xrm.Sdk.KeyAttributeCollection) to use the `KeyForNoSqlEntityWithPKPartitionId` alternate key. More information: [Using the EntityReference class](use-alternate-key-reference-record.md#using-the-entityreference-class)


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

There are two different ways to compose a URL to retrieve a record using the `partitionid` value.

- You can use the alternate key style:

   `contoso_sensordatas(contoso_sensordataid=<primary key value>,partitionid='<partitionid value>')?$select=contoso_value`

   More information: [Use an alternate key to reference a record](use-alternate-key-reference-record.md?tabs=webapi)

- Or you can use the `partitionId` query parameter.

   `contoso_sensordatas(<primary key value>)?partitionId='<partitionid value>'&$select=contoso_value`

   > [!NOTE]
   > For GET and DELETE operations parameter has a capital `I` for `Id`.

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

---

### Query rows of an elastic table

When you query the rows of an elastic table you will get best performance if you limit your query to a specific partition. If you don't limit your query to a specific partition, your query will return data across all logical partitions, which is not as fast.


> [!NOTE]
> When used this way, the parameter must use the name `partitionId` (capital 'I') rather than `partitionid` (all lower case).
> 
> When specifying a filter this way, you don't need to specify the filter criteria on `partitionid` in your query in the normal manner (using FetchXML, QueryExpression, or Web API `$filter`.)
> 
> A filter on the `partitionid` value in the normal manner will not have the same performance benefits as specifying it with the `partitionId` shown below.

These examples retrieve the first 5000 rows in the `contoso_SensorData` table which belong to logical `partitionid` = 'deviceid-001'.

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

> [!NOTE]
> For the `DELETE` and `GET` operations, the `partitionId` parameter must use a capital `I` for `Id`.

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

<!-- 

I don't think we need this

### Query rows across all logical partitions of an elastic table

This example retrieves all rows in `contoso_SensorData` table across all logical partitions. Not applying any filter on logical partition allows us to get rows from all logical partitions. Note that this query will not be as performant as it would be with a `partitionid` and table should be modeled in a way which keeps queries limited to a single logical partition as much as possible.

#### [SDK for .NET](#tab/sdk)

```csharp
public static EntityCollection RetrieveMultipleExample(IOrganizationService service)
{
   var request = new RetrieveMultipleRequest
   {
         Query = new QueryExpression()
         {
            EntityName = "sensordata",
            ColumnSet = new ColumnSet("value")
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
GET [Organization URI]/api/data/v9.2/sensordata
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
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#contoso_sensordata/$entity",
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

--- -->

### Upsert a record in an elastic table

An upsert operation is similar to update. The difference is that if a record with given id and `partitionid` doesn't exist it will be created. If it already exists, it will be updated.

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

This example upserts a row in SensorData table with id = 'ff67610c-82ce-412c-85df-0bbc6521bb01' and `partitionid` = 'deviceid-001'. Note that unlike standard tables where `primarykey` is sufficient and `partitionid` columns are needed to uniquely identify a row in elastic tables.

> [!NOTE]
> Upsert is identical to update except that the `If-Match: *` request header isn't included.

**Request**

```http
PATCH [Organization URI]/api/data/v9.2/sensordata(ff67610c-82ce-412c-85df-0bbc6521bb01)?partitionid="deviceid-001"
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

### Delete a record in an elastic table

#### [SDK for .NET](#tab/sdk)

This example deletes a row in `contoso_SensorData` table with specified `id` and `partitionid` = 'deviceid-001'.

```csharp
/// <summary>
/// Demonstrates a delete operation
/// </summary>
/// <param name="service">Authenticated client implementing the IOrganizationService interface</param>
/// <param name="sensordataid">The unique identifier of the contoso_sensordata table.</param>
/// <param name="sessionToken">The current session token</param>
public static void DeleteExample(IOrganizationService service, Guid sensordataid, ref string sessionToken)
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

There are two different ways to compose a URL to delete a record using the `partitionid` value.

- You can use the alternate key style:

   `contoso_sensordatas(contoso_sensordataid=<primary key value>,partitionid='<partitionid value>')`

   More information: [Use an alternate key to reference a record](use-alternate-key-reference-record.md?tabs=webapi)

- Or you can use the `partitionId` query parameter.

   `contoso_sensordatas(<primary key value>)?partitionId='<partitionid value>'`

   For example: `contoso_sensordatas(bbae4948-f3f4-ed11-8848-000d3a993550)?partitionId=deviceid-001`

   > [!NOTE]
   > For GET and DELETE operations parameter has a capital `I` for `Id`.

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

---

## Query JSON columns in an elastic table

Elastic table supports a new JSON format for text columns. This column can be used to store schema-less arbitrary json as per application needs. You can use the `ExecuteCosmosSQLQuery` message to run any Cosmos SQL query directly against your elastic table and filter rows based on properties inside JSON.

### Create a column with Json format

This example creates a string column `contoso_SensorValue` with Json format in our `contoso_SensorData` elastic table. For cases where large json need to be stored, instead of using `StringAttributeMetadata` type, we can use `MemoAttributeMetadata` type with JSON format.

#### [SDK for .NET](#tab/sdk)

This function creates a new <xref:Microsoft.Xrm.Sdk.Metadata.StringAttributeMetadata> column using the <xref:Microsoft.Xrm.Sdk.Messages.CreateAttributeRequest> class.

```csharp
public static Guid CreateJsonAttribute(IOrganizationService service)
{
   var request = new CreateAttributeRequest
   {
         EntityName = "contoso_sensordata",
         Attribute = new StringAttributeMetadata
         {
            SchemaName = "contoso_SensorValue",
            RequiredLevel = new AttributeRequiredLevelManagedProperty(AttributeRequiredLevel.None),
            MaxLength = 1000,
            FormatName = StringFormatName.Json,
            DisplayName = new Label("Sensor Value", 1033),
            Description = new Label("Stores unstructured sensor data as reported by device", 1033)
         }
   };

   var response = (CreateAttributeResponse)service.Execute(request);

   return response.AttributeId;
}
```

More information: [Add a String column to a table](org-service/create-custom-entity.md#add-a-string-column-to-the-custom-table)


#### [Web API](#tab/webapi)

This request creates a new <xref:Microsoft.Dynamics.CRM.StringAttributeMetadata> column by posting to the Web API `EntityDefinitions` resource referring to the `contoso_sensordata` table.

**Request**

```http
POST [Organization URI]/api/data/v9.2/EntityDefinitions(LogicalName='contoso_sensordata')/Attributes
MSCRM.SolutionUniqueName: examplesolution
Accept: application/json  
Content-Type: application/json; charset=utf-8  
OData-MaxVersion: 4.0  
OData-Version: 4.0  

{
   "AttributeType":"String",
   "AttributeTypeName":{
      "Value":"StringType"
   },
   "Description":{
      "@odata.type":"Microsoft.Dynamics.CRM.Label",
      "LocalizedLabels":[
         {
            "@odata.type":"Microsoft.Dynamics.CRM.LocalizedLabel",
            "Label":"Contains sensor data reported by IOT devices as JSON values",
            "LanguageCode":1033
         }
      ]
   },
   "DisplayName":{
      "@odata.type":"Microsoft.Dynamics.CRM.Label",
      "LocalizedLabels":[
         {
            "@odata.type":"Microsoft.Dynamics.CRM.LocalizedLabel",
            "Label":"sensorvalue",
            "LanguageCode":1033
         }
      ]
   },
   "RequiredLevel":{
      "Value":"None",
      "CanBeChanged":true,
      "ManagedPropertyLogicalName":"canmodifyrequirementlevelsettings"
   },
   "SchemaName":"sensorvalue",
   "@odata.type":"Microsoft.Dynamics.CRM.StringAttributeMetadata",
   "FormatName":{
      "Value":"Json"
   },
   "MaxLength":3500
}
```

**Response**

```http
HTTP/1.1 204 No Content  
OData-Version: 4.0  
OData-EntityId: [Organization URI]/api/data/v9.2/EntityDefinitions(402fa40f-287c-e511-80d2-00155d2a68d2)/Attributes(f01bef16-287c-e511-80d2-00155d2a68d2)  
```

More information: [Create columns](webapi/create-update-entity-definitions-using-web-api.md#create-columns)

---

### Set Json column data

This example creates a row in `contoso_SensorData` elastic table with JSON values in the `contoso_Value` column.

#### [SDK for .NET](#tab/sdk)

```csharp
public static Guid CreateWithJsonData(IOrganizationService service, string deviceId, ref string sessionToken)
{
   var entity = new Entity("contoso_sensordata")
   {
         Attributes =
         {
            { "contoso_sensorvalue", "{\"type\":\"Humidity\",\"value\": \"40\",\"timestamp\":\"2023-05-01Z05:00:00\"}" },
            { "contoso_deviceid", deviceId },
            { "partitionid", deviceId }
         }
   };

   var request = new CreateRequest
   {
         Target = entity
   };

   var response = (CreateResponse)service.Execute(request);

   // Capture the session token
   sessionToken = response.Results["x-ms-session-token"].ToString();

   return response.id;
}
```

#### [Web API](#tab/webapi)


**Request**

```http
POST [Organization URI]/api/data/v9.2/contoso_sensordatas

{
   "contoso_sensorvalue": "{\"type\":\"Humidity\",\"value\": \"40\",\"timestamp\":\"2023-05-01Z05:00:00\"}",
   "contoso_deviceid" : "device-001",
   "partitionid" : "device-001"
}
```

**Response**

```http
HTTP/1.1 204 No Content
OData-Version: 4.0
x-ms-session-token: hj23ad#1543
OData-EntityId: [Organization URI]/api/data/v9.2/sensordata(7eb682f1-ca75-e511-80d4-00155d2a68d1)
```

---


### Query Json column data

This example runs a query on `contoso_SensorData` elastic table with filter on sensorvalue.type json element to be equal to "Humidity".

All table columns can be queried with a `c.props` prefix to the schema name of the columns where `"c"` is an alias or a shorthand notation for the elastic table being queried. For example, `contoso_deviceid` column in `contoso_sensordata` table can be referenced in the Cosmos SQL query using `c.props.contoso_deviceid`.

#### [SDK for .NET](#tab/sdk)

The SDK for .NET doesn't yet have request and response classes for the  `ExecuteCosmosSqlQuery` message. You can use <xref:Microsoft.Xrm.Sdk.OrganizationRequest> and <xref:Microsoft.Xrm.Sdk.OrganizationResponse> classes. 

<!-- TODO This sample didn't work for me -->

```csharp
public static List<SensorValue> QueryJsonAttribute(IOrganizationService service)
{
    var request = new OrganizationRequest("ExecuteCosmosSqlQuery");
    
    request.Parameters["EntityLogicalName"] = "cr03e_hyperdocument";
    request.Parameters["QueryText"] = "select c.sensorvalue.type, c.sensorvalue.value, c.deviceid * from c where c.props.sensorvalue.type='Humidity'";

    OrganizationResponse response = service.Execute(request);

    // Deserialized query result into a class with expected schema.
    Entity result = (Entity)response.Results["Result"];    
    return JsonConvert.Deserialize<List<SensorValue>>(result["Result"].ToString());
}

public class SensorValue
{
   [JsonProperty("type")]
   public string Type {get;set;}
   [JsonProperty("value")]
   public string Value {get;set;}
   [JsonProperty("deviceid")]
   public string DeviceId {get;set;}
}

```

More information: [Use messages with the Organization service](org-service/use-messages.md)

#### [Web API](#tab/webapi)

This request uses the [ExecuteCosmosSqlQuery Function](xref:Microsoft.Dynamics.CRM.ExecuteCosmosSqlQuery).

**Request**

```http
GET [Organization URI]/api/data/v9.2/ExecuteCosmosSqlQuery(
   QueryText=@p1,
   EntityLogicalName=@p2,
   QueryParameters=@p3)?
   @p1='select c.contoso_sensorvalue.type, c.contoso_sensorvalue.value, c.contoso_deviceid * from c where c.props.sensorvalue.type=@sensortype'
   &@p2='contoso_sensordata'
   &@p3={'Keys':['@sensortype'],'Values':[{'Type':'System.String','Value':'Humidity'}]}
```

**Response**

```http
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  

{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#executecosmossqlquery",
    "Result": [
        {
            "type" : "Humidity",
            "value": "60",
            "deviceid" : "device-001"
        },
        {
            "type" : "Humidity",
            "value": "80",
            "deviceid" : "device-002"
        },
        {
            "type" : "Humidity",
            "value": "15",
            "deviceid" : "device-003"
        }
    ]
}
```

---

## Bulk operations

Often applications need to ingest large amount of data into Dataverse in a short amount of time. Dataverse has a group of messages that are designed to achieve high throughput. With elastic tables, the throughput is very high.

Bulk operations are optimized for performance when executing multiple write operations on the same table by taking a batch of rows as input in a single write operation. Multiple bulk operation can be run in parallel to achieve high throughput. More information <!--> TODO. Link here. -->

Elastic tables currently supports following messages for Bulk execution:

- `CreateMultiple`
- `UpdateMultiple`
- `DeleteMultiple`

Support for `UpsertMultiple` mesage will be coming soon. Also, Bulk APIs are currently supported only in SDK for .NET

### CreateMultiple


This example uses the `CreateMultiple` message to create mutiple rows in `contoso_SensorData` elastic table.

```csharp
public static Guid CreateMultiple(IOrganizationService service)
{
    List<Microsoft.Xrm.Sdk.Entity> entityList = new List<Microsoft.Xrm.Sdk.Entity>
      {
         new Microsoft.Xrm.Sdk.Entity("contoso_sensordata")
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
         new Microsoft.Xrm.Sdk.Entity("contoso_sensordata")
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
         new Microsoft.Xrm.Sdk.Entity("contoso_sensordata")
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

### UpdateMultiple

This example uses `UpdateMultiple` message to update mutiple rows of `contoso_SensorData` elastic table.

```csharp
public static Guid UpdateMultiple(IOrganizationService service)
{
    List<Microsoft.Xrm.Sdk.Entity> entityList = new List<Microsoft.Xrm.Sdk.Entity>
      {
         new Microsoft.Xrm.Sdk.Entity("contoso_sensordata")
         {
            Attributes =
            {
               { "contoso_value", "45" },
               { "partitionid", "deviceid-001" }
            }
         },
         new Microsoft.Xrm.Sdk.Entity("contoso_sensordata")
         {
            Attributes =
            {
               { "contoso_value", "15" },
               { "partitionid", "deviceid-002" }
            }
         }
         new Microsoft.Xrm.Sdk.Entity("contoso_sensordata")
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

    // Use CreateMultipleRequest
    UpdateMultipleRequest updateMultipleRequest = new()
    {
        Targets = entities,
    };
    return service.Execute(request);
}
```

### DeleteMultiple

This example uses `DeleteMultiple` message to delete mutiple rows from `contoso_SensorData` elastic table.

```csharp
public static OrganizationResponse DeleteMultiple(IOrganizationService service)
{
    EntityReference record1 = new EntityReference(
        "contoso_sensordata", 
        new KeyAttributeCollection
        {
            { "contoso_sensordataid", "3f56361a-b210-4a74-8708-3c664038fa41" },
            { "partitionid", "deviceid-001" }
        });

    EntityReference record2 = new EntityReference(
        "contoso_sensordata",
        new KeyAttributeCollection
        {
            { "contoso_sensordataid", "e682715b-1bba-415e-b2bc-de9327308423" },
            { "partitionid", "deviceid-002" }
        });

    EntityReferenceCollection entityReferenceCollection = new EntityReferenceCollection();
    entityReferenceCollection.Add(record1);
    entityReferenceCollection.Add(record2);

    OrganizationRequest deleteMultipleRequest = new OrganizationRequest("DeleteMultiple");
    deleteMultipleRequest.Parameters["Targets"] = entityReferenceCollection;

    return service.Execute(deleteMultipleRequest);
}
```

## Known issues

Following are known issues with elastic tables that should be addressed before this feature is generally available.

### Error not returned when grouping elastic table data operations in a transaction

Dataverse does not return an error when you group data operations using SDK [ExecuteTransactionRequest](xref:Microsoft.Xrm.Sdk.Messages.ExecuteTransactionRequest) class or with Web API `$batch` `ChangeSets`. These data operations will complete, but no transaction is actually applied. No transaction can be applied, so this operation should fail and return an error.

### x-ms-session-token value not returned for delete operations

Dataverse doesn't return the `x-ms-session-token` value for delete operations. More information: [Consistency level](#consistency-level)

## Frequently Asked Questions (FAQ)

<!-- 

FAQ should only be used to refer to content that is ALREADY described in the docs.
They should ALWAYS include a link to the section of the docs where the information was provided in context. 

-->

## Tabbed Template

<!-- Copy the following for in-line samples showing SDK & Web API -->

<!-- Copy Start -->

#### [SDK for .NET](#tab/sdk)

Comments on anything special about the SDK sample

```csharp

```

#### [Web API](#tab/webapi)

Comments on anything special about the Web API sample

**Request**

```http

```

**Response**

```http

```

---

<!-- Copy End -->

### See Also

[Use optional parameters](optional-parameters.md)<br />
[Partitioning and horizontal scaling in Azure Cosmos DB](/azure/cosmos-db/partitioning-overview)