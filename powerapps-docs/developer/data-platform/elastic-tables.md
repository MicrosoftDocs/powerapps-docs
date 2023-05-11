---
title: "Use elastic tables (Preview) (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn how to use elastic tables with code" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: intro-internal
ms.topic: "article"
ms.date: 05/09/2022
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
**///////////////////////////////////**

TODO: Sumant to add content about why Elastic tables are great for developers

**///////////////////////////////////**

## Partitioning and horizontal scaling

Elastic tables leverage Azure Cosmos DB partitioning to scale individual tables to meet the performance needs of your application. All elastic tables contain a system-defined **Partition Id** string column with the schema name `PartitionId` and logical name `partitionid`.

Azure Cosmos DB ensures that the rows in a table are divided into distinct subsets called logical partitions which are formed based on the value of `partitionid` column of each row.

### Choosing a PartitionId value

The `partitionid` value you should use depends on the nature of your data.  A logical partition in an elastic table consists of a set of rows that have the same `partitionid`. For example, in a table that contains data about various products, you can use product category as the `partitionid` for the table. Groups of items that have specific values for product category, such as Clothing, Books, Electronic Appliances and Pet supplies, form distinct logical partitions.

Dataverse transparently and automatically manages logical partitions associated with a table. There is no limit on the number of logical partitions you can have in a table. You also don't have to worry about deleting a logical partition when the underlying rows belonging to that partition is deleted.

For all elastic tables, `partitionid` column should:

- Have a value which doesn't change. Once a row is created with a `partitionid` value, you cannot change it later.
- Have a high cardinality value. In other words, the property should have a wide range of possible values. Each logical partition can store 20 GB of data. So, choosing a partitionId with a wide range of possible values ensures that the table can scale without reaching limits for any specific logical partition.
- Spread data as evenly as possible between all logical partitions.
- Have values that are no larger than 1024 bytes.

When `partitionid` is not specified for a row, Dataverse uses the primary key as the default `partitionid`. For write-heavy tables of any size or for cases where rows are mostly retrieved using id, the primary key is naturally a great choice for the `partitionid` column.

### Scenario

Imagine Contoso operates large number of IoT devices deployed by the company all across the world. Contoso needs to store and query large amounts of sensor data being emitted from IoT devices so that they can monitor health of device and gathering other insights.

Contoso can create an elastic table named  `contoso_SensorData` to store and query large volume of Internet of Things (IoT) data. It can choose to use `contoso_DeviceId` as the partitionid for each row corresponding to that device. Since `contoso_DeviceId` is unique to each device and contoso performs queries mostly in context of a given `contoso_DeviceId`, it acts as a good partition strategy for entire dataset.

## Create elastic tables

You can create elastic tables using [Power Apps](https://make.powerapps.com/) without writing code. More information: [Create and edit tables using Power Apps](../../maker/data-platform/create-edit-entities-portal.md). 

These examples create a new elastic table `contoso_SensorData` using the Dataverse SDK for .NET and Web API. Use the `EntityMetadata.TableType` property with a value of `Elastic` to create an elastic table with code.

Dataverse automatically creates two system columns for each elastic tables at the time of table creation.

- `PartitionId` : Defines the logical partition a row belongs to.
- `TimeToLiveInSeconds` :  Defines the time in seconds after which row will expire and get deleted from database automatically.

#### [SDK for .NET](#tab/sdk)

```csharp
public static Guid CreateElasticTable(IOrganizationService service)
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
            TableType = "Elastic"
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
    return service.Execute(request);
}
```

#### [Web API](#tab/webapi)


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

---

### Adding Columns

**///////////////////////////////////**

I think there are limits on the types of columns that can be created

**///////////////////////////////////**


### Adding Relationships

**///////////////////////////////////**

I know that there are limits on relationships that can be added.

Verify whether the Table relationship eligibilty APIs work for this:

https://learn.microsoft.com/en-us/power-apps/developer/data-platform/entity-relationship-eligibility

**///////////////////////////////////**


## Data operations

Following examples show how customer can work with data stored in an elastic table.

- [Create a record](#create-a-record)
- [Update a record](#update-a-record)
- [Retrieve a record](#retrieve-a-record)
- [Query rows in a single logical partition](#query-rows-in-a-single-logical-partition)


### Create a record

This example creates a new row in `contoso_SensorData` table with `partitionid` set to `deviceid`. It also sets `ttlinseconds` column which ensures that row expires after 1 day and deleted from dataverse automatically.


**///////////////////////////////////**

**TODO: Sumant:**
These examples seem to be setting the `sensordataid` primary key value for create. 
For create we recommend people let Dataverse set the primary key value. Is this different for elastic tables?

Also, I expect that the column names must be `contoso_deviceId`, `contoso_sensortype`, `contoso_value` etc.

**///////////////////////////////////**

#### [SDK for .NET](#tab/sdk)

```csharp
public static Guid CreateExample(IOrganizationService service)
{
   var entity = new Entity("contoso_sensordata")
   {
         Attributes = {
            { "sensordataid", "ff67610c-82ce-412c-85df-0bbc6521bb01" },
            { "deviceId", "deviceid-001" },
            { "sensortype", "Humidity" },
            { "value", 40 },
            { "timestamp", "2023-05-01Z05:00:00"},
            { "partitionid", "deviceid-001" },
            { "ttlinseconds", 86400 }
         }
   };

   return service.Create(entity);
}
```

#### [Web API](#tab/webapi)

**Request**

```http
POST [Organization URI]/api/data/v9.1/sensordata
Content-Type: application/json
OData-MaxVersion: 4.0
OData-Version: 4.0
Accept: application/json
{
  "sensordataid", "ff67610c-82ce-412c-85df-0bbc6521bb01",
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
x-ms-session-token: hj23ad#1543
OData-EntityId: [Organization URI]/api/data/v9.0/sensordata(7eb682f1-ca75-e511-80d4-00155d2a68d1)
```

**///////////////////////////////////**
We have never called out the `x-ms-session-token` response header as something developers need to know about.
I'll read further to see if you explain why this is important.
**///////////////////////////////////**

---

### Update a record

This example updates sensor `value` and `timestamp` of an existing row in `contoso_SensorData` table with using the sensordataid primary key and `partitionid` = `'device-001'`. Note that primary key and `partitionid` columns are always required to uniquely identify an existing elastic table row. The `partitionid` of an existing row cannot be updated and is only being used to uniquely identify the row to update.

#### [SDK for .NET](#tab/sdk)



```csharp
public static void UpdateExample(IOrganizationService service, Guid sensordataid)
{
   var entity = new Entity("contoso_sensordata", sensordataid)
   {
         Attributes = {
            { "value", 60 },
            { "timestamp", "2023-05-01Z06:00:00" },
            { "partitionid", "deviceid-001" }
         }
   };

   service.Update(entity);
}
```

#### [Web API](#tab/webapi)



**Request**

```http
PATCH [Organization URI]/api/data/v9.0/contoso_sensordata(<sensordataid value>)
Content-Type: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0
If-Match: *  

{  
    "value": 60,
    "timestamp", "2023-05-01Z06:00:00",
    "partitionid", "deviceid-001"
}
```

**Response**

```http
HTTP/1.1 204 No Content  
OData-Version: 4.0
x-ms-session-token: hn76qq#7324
```

---

### Retrieve a record

#### [SDK for .NET](#tab/sdk)

This example retrieves an existing row in SensorData table with SensorDataId = 'ff67610c-82ce-412c-85df-0bbc6521bb01' and partitionid = 'device-001'. Both primary key and partitionid columns are required to uniquely identify an existing elastic table row.

```csharp
public static Entity RetrieveExample(IOrganizationService service)
{
   var request = new RetrieveRequest
   {
         ColumnSet = new ColumnSet("new_firstname"),
         Target = new EntityReference("new_customer", new Guid("ff67610c-82ce-412c-85df-0bbc6521bb01")),
         ["partitionId"] = "deviceid-001"
   };

   var response = (RetrieveResponse)service.Execute(request);
   return response.Entity;
}
```

#### [Web API](#tab/webapi)

This example retrieves an existing row in SensorData table with SensorDataId = 'ff67610c-82ce-412c-85df-0bbc6521bb01' and partitionid = 'device-001'. Both primary key and partitionid columns are required to uniquely identify an existing elastic table row. Here partitionid is being passed as query parameter.

**Request**

```http
GET [Organization URI]/api/data/v9.2/sensordata(ff67610c-82ce-412c-85df-0bbc6521bb01)?partitionid="deviceid-001"&$select=value,timestamp
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
"@odata.context": "[Organization URI]/api/data/v9.2/$metadata#sensordata/$entity",  
"@odata.etag": "W/\"502186\"",  
"value": 60
"timestamp" : "2023-05-01Z06:00:00"
}
```

---

### Query rows in a single logical partition

These examples retrieve the first 5000 rows in the `contoso_SensorData` table which belong to logical `partitionid` = 'deviceid-001'. 

> [!NOTE]
> When used this way, the value must use `partitionId` (capital 'I') rather than `partitionid` (all lower case).

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

This example retrieves all rows in SensorData table which belong to logical partitionid = 'deviceid-001'.

**Request**

```http
GET [Organization URI]/api/data/v9.2/sensordata?partitionId="deviceid-001"
&$select=new_firstname
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
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#new_customers(new_firstname)",
    "value": [
        {
            "@odata.etag": "W/\"81052965\"",
            "sensortype" : "Humidity",
            "value": "60",
            "timestamp" : "2023-05-01Z06:00:00"
        },
        {
            "@odata.etag": "W/\"81052965\"",
            "sensortype" : "Temperature",
            "value": "110",
            "timestamp" : "2023-05-02Z06:10:00"
        },
        {
            "@odata.etag": "W/\"81052965\"",
            "sensortype" : "Pressure",
            "value": "230",
            "timestamp" : "2023-05-01Z16:30:00"
        }
    ]
}
```
---

### Query rows across all logical partitions

#### [SDK for .NET](#tab/sdk)

This example retrieves all rows in SensorData table across all logical partitions. Not applying any filter on logical partition allows us to get rows from all logical partitions. Note that this query will not performant and data modelling of the table should be done in a way to keep queries limited to a single logical partition as much as possible.

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

This example retrieves all rows in SensorData table across all logical partitions. Not applying any filter on logical partition allows us to get rows from all logical partitions. Note that this query will not performant and data modelling of the table should be done in a way to keep queries limited to a single logical partition as much as possible.

**Request**

```http
GET [Organization URI]/api/data/v9.2/sensordata
&$select=new_firstname
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
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#new_customers(new_firstname)",
    "value": [
        {
            "@odata.etag": "W/\"81052965\"",
            "sensortype" : "Humidity",
            "value": "60",
            "timestamp" : "2023-05-01Z06:00:00"
        },
        {
            "@odata.etag": "W/\"81052965\"",
            "sensortype" : "Temperature",
            "value": "110",
            "timestamp" : "2023-05-02Z06:10:00"
        },
        {
            "@odata.etag": "W/\"81052965\"",
            "sensortype" : "Pressure",
            "value": "230",
            "timestamp" : "2023-05-01Z16:30:00"
        }
    ]
}
```

---

### Upsert a record

An Upsert oepration is similar to update. The difference is that if record with given id and partitionid doesn't exist it will be created. If it already exists, it will be updated.

#### [SDK for .NET](#tab/sdk)

This example upserts a row in SensorData table with id = 'ff67610c-82ce-412c-85df-0bbc6521bb01' and partitionid = 'deviceid-001'.

```csharp
public static void UpsertExample(IOrganizationService service, Guid id)
{
   var entity = new Entity("SensorData")
   {
         Attributes = {
            { "sensordataid", "ff67610c-82ce-412c-85df-0bbc6521bb01" },
            { "deviceId", "deviceid-001" },
            { "sensortype", "Humidity" },
            { "value", 60 },
            { "timestamp", "2023-05-01Z12:30:00"},
            { "partitionid", "deviceid-001" },
            { "ttlinseconds", 86400 }
         }
   };

   service.Execute(request);
}
```

#### [Web API](#tab/webapi)

This example upserts a row in SensorData table with id = 'ff67610c-82ce-412c-85df-0bbc6521bb01' and partitionid = 'deviceid-001'.

> [!NOTE]
> Upsert is identical to update except that the `If-Match: *` request header isn't included.

**Request**

```http
PATCH [Organization URI]/api/data/v9.0/sensordata(ff67610c-82ce-412c-85df-0bbc6521bb01)?partitionid="deviceid-001"
Content-Type: application/json
x-ms-session-token: hn76qq#7324
OData-MaxVersion: 4.0  
OData-Version: 4.0
  
{  
  "sensordataid", "ff67610c-82ce-412c-85df-0bbc6521bb01",
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

### Delete a record

#### [SDK for .NET](#tab/sdk)

This example deletes a row in SensorData table with id = 'ff67610c-82ce-412c-85df-0bbc6521bb01' and partitionid = 'deviceid-001'.

```csharp
public static void DeleteExample(IOrganizationService service, Guid id)
{
   var request = new DeleteRequest
   {
         Target = new EntityReference("sensordataid", new Guid("ff67610c-82ce-412c-85df-0bbc6521bb01")),
         ["partitionId"] = "deviceid-001"
   };

   service.Execute(request);
}
```

#### [Web API](#tab/webapi)

This example upserts a row in SensorData table with id = 'ff67610c-82ce-412c-85df-0bbc6521bb01' and partitionid = 'deviceid-001'.

**Request**

```http
DELETE [Organization URI]/api/data/v9.0/sensordata(ff67610c-82ce-412c-85df-0bbc6521bb01)?partitionId="deviceid-001"
Content-Type: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0
```

**Response**

```http
HTTP/1.1 204 No Content  
OData-Version: 4.0
x-ms-session-token: hn76qq#7324
```

---
## Query JSON columns

Elastic table supports a new JSON format for text columns. This column can be used to store schema less arbitrary json as per application needs. You can use ExecuteCosmosSQLQuery API to run any Cosmos SQL query directly against your elastic table and filter rows based on properties inside JSON.

### Create Json format columns

This example creates a string column SensorValue with Json format in our SensorData elastic table. For cases where large json need to be stored, instead of using String attribute type, we can use Memo attribute type with JSON format.
#### [SDK for .NET](#tab/sdk)

**///////////////////////////////////**

We need to keep the SDK tab for all samples.
If this can't be done with the SDK, we will say that this is only possible using Web API

**///////////////////////////////////**

```csharp

```

#### [Web API](#tab/webapi)


**Request**

```http
POST [Organization URI]/api/data/v9.0/EntityDefinitions(402fa40f-287c-e511-80d2-00155d2a68d2)/Attributes HTTP/1.1
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
OData-EntityId: [Organization URI]/api/data/v9.0/EntityDefinitions(402fa40f-287c-e511-80d2-00155d2a68d2)/Attributes(f01bef16-287c-e511-80d2-00155d2a68d2)  
```

---

### Set Json column data

This example creates a row in SensorData elastic table with JSON values in the sensorvalue column.
#### [SDK for .NET](#tab/sdk)

**///////////////////////////////////**

We need to keep the SDK tab for all samples.
If this can't be done with the SDK, we will say that this is only possible using Web API

**///////////////////////////////////**

```csharp

```

#### [Web API](#tab/webapi)


**Request**

```http
POST [Organization URI]/api/data/v9.0/sensordata
{
   "sensordataid" : "id",
   "sensorvalue": {
      "type":"Humidity",
      "value": "40",
      "timestamp":"2023-05-01Z05:00:00"
   }
   "deviceid" : "device-001"
   "partitionid" : "device-001"
}
```

**Response**

```http
HTTP/1.1 204 No Content
OData-Version: 4.0
x-ms-session-token: hj23ad#1543
OData-EntityId: [Organization URI]/api/data/v9.0/sensordata(7eb682f1-ca75-e511-80d4-00155d2a68d1)
```

---


### Query Json column data

This example runs a query on SensorData elastic table with filter on sensorvalue.type json element to be equal to "Humidity"

#### [SDK for .NET](#tab/sdk)


**///////////////////////////////////**

We need to keep the SDK tab for all samples.
If this can't be done with the SDK, we will say that this is only possible using Web API

**///////////////////////////////////**

```csharp

```

#### [Web API](#tab/webapi)



**Request**

```http
GET [Organization URI]/api/data/v9.0/ExecuteCosmosSqlQuery(
   QueryText=@p1,
   EntityLogicalName=@p2,
   QueryParameters=@p3)?
   @p1='select c.sensorvalue.type, c.sensorvalue.value, c.deviceid * from c where c.props.sensorvalue.type=@sensortype'
   &@p2='sensordata'
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




## Consistency level

Elastic tables support session consistency. Session consistency in Elastic tables is achieved through the use of session tokens, which are opaque strings returned by dataverse when a client performs any write operation (create/update/upsert/delete). When the client performs a subsequent read operation, it includes the session token in the request, allowing dataverse to return the most up-to-date data for that client.

You will find session token as x-ms-session-token header in response of all write operations. (Create/Update/Upsert/Delete)

When calling a retrieve API, you can use MSCRM.SessionToken header to pass corresponding session-token to retrieve the most up-to-date row value.

## Transactional behavior

Elastic tables are vastly different from standard tables when it comes to transactional guarantees. For standard tables, transactions are a fundamental concept and are used to group a set of requests into a single unit of work that must be either fully completed or fully rolled back in case of failure. Standard tables provide ACID guarantees for transactions, meaning that each transaction is atomic (all or nothing), consistent (maintains data integrity), isolated (transactions don't interfere with each other), and durable (committed transactions are permanent).

In contrast, Elastic table currently do not support transaction in any form. 
For single request execution, write operation happening in various plugin stages are **NOT** transactional. For example, if you have a post plugin registered on Create message for SensorData table at stage 40, and if an error ocurrs during post plugin execution, the database write operation will not be rolled back.
Multiple write operations within even within same plugin execution are also not atomic.

Elastic tables also currently do not support executing two or more organization service requests in a single database transaction using the ExecuteTransactionRequest message.


## Frequently Asked Questions (FAQ)

<!-- 

FAQ should only be used to refer to content that is ALREADY described in the docs.
They should ALWAYS include a link to the section of the docs where the information was provided in context. 

-->

## Tabbed Template

<!-- Copy the following whenever you want to have a sample that is for SDK AND Web API -->

#### [SDK for .NET](#tab/sdk)

Introduce what the SDK sample does

```csharp

```

#### [Web API](#tab/webapi)

Introduce what the Web API sample does

**Request**

```http

```

**Response**

```http

```

---

### See Also

[Use optional parameters](optional-parameters.md)<br />
[Partitioning and horizontal scaling in Azure Cosmos DB](/azure/cosmos-db/partitioning-overview)