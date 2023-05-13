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
Elastic tables are Dataverse tables which are powered by Azure Cosmos DB. They are designed to automatically scale horizontally and can handle large amounts of data and high levels of throughput with low latency. Elastic tables are suitable for applications with unpredictable, spiky or rapidly growing workloads.

## When to use elastic tables

Whether you should use an elastic table depends on the specific needs of your data and your application.

Elastic tables are better when:

- Your data is unstructured or semi-structured, or if your data model is constantly changing.
- You need automatic horizontal scaling.
- You need to handle a high volume of read and write requests.

Standard tables are better when:

- Your application requires strong data consistency.
- Your application requires relational modeling and needs transactional capability across tables and during plugin execution stages.
- Your application requires complex joins.

The choice of table should be based on the specific needs of your application. A combination of both types of tables may be appropriate.

## Partitioning and horizontal scaling

Elastic tables use Azure Cosmos DB partitioning to scale individual tables to meet the performance needs of your application. All elastic tables contain a system-defined **Partition Id** string column with the schema name `PartitionId` and logical name `partitionid`.

Azure Cosmos DB ensures that the rows in a table are divided into distinct subsets called [logical partitions](/azure/cosmos-db/partitioning-overview#logical-partitions) which are formed based on the value of `partitionid` column of each row.

### Choosing a PartitionId value

The `partitionid` value you should use depends on the nature of your data.  A logical partition in an elastic table consists of a set of rows that have the same `partitionid`. For example, in a table that contains data about various products, you can use product category as the `partitionid` for the table. Groups of items that have specific values for product category, such as Clothing, Books, Electronic Appliances and Pet supplies, form distinct logical partitions.

Dataverse transparently and automatically manages logical partitions associated with a table. There is no limit on the number of logical partitions you can have in a table. You also don't have to worry about deleting a logical partition when the underlying rows belonging to that partition is deleted.

For all elastic tables, `partitionid` column should:

- Have a value which doesn't change. Once a row is created with a `partitionid` value, you cannot change it later. <!-- TODO: need clarity on whether this is 'can not' or 'should not'. IsValidForUpdate is set to 'true', which suggests it can be updated. -->
- Have a high cardinality value. In other words, the property should have a wide range of possible values. Each logical partition can store 20 GB of data. So, choosing a `partitionid` with a wide range of possible values ensures that the table can scale without reaching limits for any specific logical partition.
- Spread data as evenly as possible between all logical partitions.
- Have values that are no larger than 1024 bytes.

When `partitionid` is not specified for a row, Dataverse uses the primary key as the default `partitionid`. For write-heavy tables of any size or for cases where rows are mostly retrieved using id, the primary key is naturally a great choice for the `partitionid` column.

## Consistency level

Elastic tables support [session consistency](/azure/cosmos-db/consistency-levels#session-consistency). Elastic tables use *session tokens* to achieve session consistency. Session tokens are opaque strings returned by Dataverse when a client performs any write operation (create/update/delete).

When the client performs a subsequent read operation, it includes the session token in the request, allowing Dataverse to return the most up-to-date data for that client.

You will find session token as `x-ms-session-token` header in response of all write operations.

When calling a retrieve API, you can use `MSCRM.SessionToken` header to pass corresponding `x-ms-session-token` to retrieve the most up-to-date row value.

## Transactional behavior

Elastic tables are vastly different from standard tables when it comes to transactional guarantees.

For standard tables, transactions are a fundamental concept and are used to group a set of requests into a single unit of work that must be either fully completed or fully rolled back in case of failure. Standard tables provide **ACID** guarantees for transactions, meaning that each transaction is:

- **A**tomic: All or nothing
- **C**onsistent: Maintains data integrity
- **I**solated: transactions don't interfere with each other
- **D**urable: Committed transactions are permanent

In contrast, elastic tables currently do not support transaction in any form.
For single request execution, write operation happening in synchronous plugin stages are **NOT** transactional.

For example, if you have a synchronous plug-in step registered on the `PostOperation` stage for the `Create` message an elastic table, any error in your plug-in will not roll back the operation.

Multiple write operations within same the plugin execution are also not atomic.

Elastic tables also currently do not support executing two or more organization service requests in a single database transaction using the `ExecuteTransaction` message or in a Web API `$batch` operation `ChangeSet`.

<!-- 
TODO: What is the error thrown if you try? 
Or does it simply succeed without actually having a transaction?
-->

### Scenario

Imagine Contoso operates large number of Internet of Things (IoT) devices deployed by the company all across the world. Contoso needs to store and query large amounts of sensor data being emitted from IoT devices so that they can monitor health of device and gathering other insights.

Contoso can create an elastic table named `contoso_SensorData` to store and query large volume of IoT data. It can choose to use a string column named `contoso_DeviceId` as the partitionid value for each row corresponding to that device. Since `contoso_DeviceId` is unique to each device and Contoso performs queries mostly in context of a given `contoso_DeviceId`, it acts as a good partition strategy for entire dataset.

## Create elastic tables

You can create elastic tables using [Power Apps](https://make.powerapps.com/) without writing code. More information: [Create and edit tables using Power Apps](../../maker/data-platform/create-edit-entities-portal.md). 

These examples create a new elastic table `contoso_SensorData` using the Dataverse SDK for .NET and Web API. Use the `EntityMetadata.TableType` property with a value of `Elastic` to create an elastic table with code.



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

## Adding Columns

You can create columns in elastic tables using [Power Apps](https://make.powerapps.com/) without writing code. More information: [Create and edit tables using Power Apps](../../maker/data-platform/create-edit-entities-portal.md). 

Dataverse automatically creates two system columns for each elastic tables at the time of table creation.
- `PartitionId` : Defines the logical partition a row belongs to.
- `TimeToLiveInSeconds` :  Defines the time in seconds after which row will expire and get deleted from database automatically.

Columns can also be created using standard table APIs.

There are limits on the types of columns you can add. Currently you cannot add these types of columns:

- MoneyType (`MoneyAttributeMetadata`)
- MultiSelectPicklistType (`MultiSelectPicklistAttributeMetadata`)
- StateType (`StateAttributeMetadata`)
- StatusType (`StatusAttributeMetadata`)
- FileType (`FileAttributeMetadata`)
- ImageType (`ImageAttributeMetadata`)
- Calculated or Rollup Columns

Elastic tables support columns that store JSON data. More information: [Create column with Json format](#create-column-with-json-format)

<!-- 

These examples create a new column `contoso_sensortype` in elastic table `contoso_SensorData` using the Dataverse SDK for .NET and Web API.

TODO

I don't think we need this sample b/c it there is nothing special about it for elastic tables.

#### [SDK for .NET](#tab/sdk)

```csharp
public static Guid OrganizationResponse CreateColumn(IOrganizationService service)
{
    var request = new CreateAttributeRequest
    {
        EntityName = "contoso_sensordata",
        Attribute = new StringAttributeMetadata
        {
            SchemaName = "contoso_sensortype",
            RequiredLevel = new AttributeRequiredLevelManagedProperty(AttributeRequiredLevel.None),
            MaxLength = 1000,
            FormatName = StringFormatName.Text,
            DisplayName = new Label("Sensor Type", 1033),
            Description = new Label("Type of sensor. e.g. pressure, Humidity", 1033)
        }
    };

   var response = service.Execute(request);
    return response.AttributeId
}
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
            "Label":"Type of sensor e.g. Pressure, Humidity",
            "LanguageCode":1033
         }
      ]
   },
   "DisplayName":{
      "@odata.type":"Microsoft.Dynamics.CRM.Label",
      "LocalizedLabels":[
         {
            "@odata.type":"Microsoft.Dynamics.CRM.LocalizedLabel",
            "Label":"SensorType",
            "LanguageCode":1033
         }
      ]
   },
   "RequiredLevel":{
      "Value":"None",
      "CanBeChanged":true,
      "ManagedPropertyLogicalName":"canmodifyrequirementlevelsettings"
   },
   "SchemaName":"contoso_sensorvalue",
   "@odata.type":"Microsoft.Dynamics.CRM.StringAttributeMetadata",
   "FormatName":{
      "Value":"Text"
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

-->

## Adding Relationships

Dataverse currently does not support creating Many-to-Many relationships with elastic tables.

One-to-Many relationships are supported for elastic tables with following limitations:

- Cascading is not supported. Cascading behavior must be set to `Cascade.None` when creating relationship.
- When the table on the Many side of relationship is a standard table.

<!-- 
TODO: I'm still not clear here. 
1:N relationship means creating a lookup column.

- I can create a lookup on an elastic table to a standard table.
- I can create a lookup on a standard table to an elastic table.

Where is the limitation?
-->

> [!NOTE]
> You can't add filters to queries for related tables. You can retrieve related data, but you can't limit the data returned based on criteria in the related tables.

<!-- 
Try to simplify with the description above.

> Although elastic table supports having One-to-Many relationships and fetch related rows using fetchXml or OData  `$expand`, adding filters on related tables is not supported. This is because elastic tables cannot perform join operations between two tables. 

TODO: Does an error occur if you try to add a filter? Or is the filter just ignored?

-->

<!-- 

TODO:
Sorry, but I don't think we need these samples about relationship creation here either. 
Unless there is something specific about elastic tables that needs to be demonstrated here.
We need samples like this here: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/entity-relationship-metadata

#### [SDK for .NET](#tab/sdk)

This example creates a One-to-Many relationship between `contact` (standard table) and `contoso_SensorData` (elastic table).

```csharp
public static OrganizationResponse CreateOneToManyRelationship(IOrganizationService service)
{
    CreateOneToManyRequest createOneToManyRelationshipRequest =
        new CreateOneToManyRequest
        {
            OneToManyRelationship =
                new OneToManyRelationshipMetadata
                {
                    ReferencedEntity = "contact",
                    ReferencingEntity = "contoso_sensordata",
                    SchemaName = "contoso_contact_contoso_sensordata",
                    AssociatedMenuConfiguration = new AssociatedMenuConfiguration
                    {
                        Behavior = AssociatedMenuBehavior.UseLabel,
                        Group = AssociatedMenuGroup.Details,
                        Label = new Label("Contact", 1033),
                        Order = 10000
                    },
                    CascadeConfiguration = new CascadeConfiguration
                    {
                        Assign = CascadeType.NoCascade,
                        Delete = CascadeType.NoCascade,
                        Merge = CascadeType.NoCascade,
                        Reparent = CascadeType.NoCascade,
                        Share = CascadeType.NoCascade,
                        Unshare = CascadeType.NoCascade
                    }
                },
            Lookup = new LookupAttributeMetadata
            {
                SchemaName = "contoso_DeviceOwner",
                DisplayName = new Label("Device owner", 1033),
                RequiredLevel = new AttributeRequiredLevelManagedProperty(AttributeRequiredLevel.None),
                Description = new Label("Owner of the IoT device", 1033)
            }
        };

    return service.Execute(createOneToManyRelationshipRequest);
}
```

#### [Web API](#tab/webapi)

This example creates a One-to-Many relationship between `contact` (standard table) and `contoso_SensorData` (elastic table).

**Request**

```http
{  
 "SchemaName": "contoso_contact_contoso_sensordata",  
 "@odata.type": "Microsoft.Dynamics.CRM.OneToManyRelationshipMetadata",  
 "AssociatedMenuConfiguration": {  
  "Behavior": "UseCollectionName",  
  "Group": "Details",  
  "Label": {  
   "@odata.type": "Microsoft.Dynamics.CRM.Label",  
   "LocalizedLabels": [  
    {  
     "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",  
     "Label": "SensorData",  
     "LanguageCode": 1033  
    }  
   ],  
   "UserLocalizedLabel": {  
    "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",  
    "Label": "SensorData",  
    "LanguageCode": 1033  
   }  
  },  
  "Order": 10000  
 },  
 "CascadeConfiguration": {  
  "Assign": "NoCascade",  
  "Delete": "NoCascade",  
  "Merge": "NoCascade",  
  "Reparent": "NoCascade",  
  "Share": "NoCascade",  
  "Unshare": "NoCascade"  
 },  
 "ReferencedAttribute": "contactid",  
 "ReferencedEntity": "contact",  
 "ReferencingEntity": "contoso_sensordata",  
 "Lookup": {  
  "AttributeType": "Lookup",  
  "AttributeTypeName": {  
   "Value": "LookupType"  
  },  
  "Description": {  
   "@odata.type": "Microsoft.Dynamics.CRM.Label",  
   "LocalizedLabels": [  
    {  
     "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",  
     "Label": "Owner of the IoT device",  
     "LanguageCode": 1033  
    }  
   ],  
   "UserLocalizedLabel": {  
    "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",  
    "Label": "Owner of the IoT device",  
    "LanguageCode": 1033  
   }  
  },  
  "DisplayName": {  
   "@odata.type": "Microsoft.Dynamics.CRM.Label",  
   "LocalizedLabels": [  
    {  
     "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",  
     "Label": "Device Owner",  
     "LanguageCode": 1033  
    }  
   ],  
   "UserLocalizedLabel": {  
    "@odata.type": "Microsoft.Dynamics.CRM.LocalizedLabel",  
    "Label": "Device Owner",  
    "LanguageCode": 1033  
   }  
  },  
  "RequiredLevel": {  
   "Value": "ApplicationRequired",  
   "CanBeChanged": true,  
   "ManagedPropertyLogicalName": "canmodifyrequirementlevelsettings"  
  },  
  "SchemaName": "contoso_DeviceOwner",  
  "@odata.type": "Microsoft.Dynamics.CRM.LookupAttributeMetadata"  
 }  
}
```

**Response**

```http
HTTP/1.1 204 No Content
OData-Version: 4.0
x-ms-session-token: hj23ad#1543
OData-EntityId: [Organization URI]/api/data/v9.0/RelationshipDefinitions(125e6d7f-2af1-ed11-8f6d-6045bdd811fa)
```

---
-->

## Elastic table data operations

Following examples show how customer can work with data stored in an elastic table.

- [Create a record](#create-a-record)
- [Update a record](#update-a-record)
- [Retrieve a record](#retrieve-a-record)
- [Query rows in a single logical partition](#query-rows-in-a-single-logical-partition)


### Create a record in an elastic table

This example creates a new row in `contoso_SensorData` table with `partitionid` set to `deviceid`. It also sets `ttlinseconds` column which ensures that row expires after 1 day and deleted from Dataverse automatically.

#### [SDK for .NET](#tab/sdk)

```csharp
public static Guid CreateExample(IOrganizationService service)
{
   var entity = new Entity("contoso_sensordata")
   {
         Attributes = 
         {
            { "contoso_deviceId", "deviceid-001" },
            { "contoso_sensortype", "Humidity" },
            { "contoso_value", 40 },
            { "contoso_timestamp", "2023-05-01Z05:00:00"},
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
  "contoso_deviceid", "deviceid-001",
  "contoso_sensortype", "Humidity",
  "contoso_value", 40,
  "contoso_timestamp", "2023-05-01Z05:00:00",
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

> [!NOTE]
> The `x-ms-session-token` value returned can be used to with the `MSCRM.SessionToken` request header to retrieve the latest version of a record. More information: [Consistency level](#consistency-level)

---

### Update a record in an elastic table

This example updates sensor `value` and `timestamp` of an existing row in `contoso_SensorData` table with using the `sensordataid` primary key and `partitionid` = `'device-001'`. Note that primary key and `partitionid` columns are always required to uniquely identify an existing elastic table row. The `partitionid` of an existing row cannot be updated and is only being used to uniquely identify the row to update.

#### [SDK for .NET](#tab/sdk)

```csharp
public static void UpdateExample(IOrganizationService service, Guid sensordataid)
{
   var entity = new Entity("contoso_sensordata", sensordataid)
   {
         Attributes = {
            { "contoso_value", 60 },
            { "contoso_timestamp", "2023-05-01Z06:00:00" },
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
    "contoso_value": 60,
    "contoso_timestamp", "2023-05-01Z06:00:00",
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

### Retrieve a record in an elastic table

This example retrieves an existing row in SensorData table with SensorDataId = 'ff67610c-82ce-412c-85df-0bbc6521bb01' and `partitionid` = 'device-001'. 
Here the `partitionid` value is passed using `partitionId` as an optional parameter. More information: [Use optional parameters](optional-parameters.md)

Note that unlike standard tables where primary key is enough to uniquely identify a row, Both primary key and `partitionid` columns are required for elastic tables. If a row has been created with non-null `partitionid` value, when retrieving the same row `partitionid` parameter MUST be passed. `404 Not Found` error will be thrown by Dataverse if `partitionid` is not passed but row was created with a non-null `partitionid` value.


#### [SDK for .NET](#tab/sdk)


```csharp
public static Entity RetrieveExample(IOrganizationService service, Guid sensorDataId)
{
   var request = new RetrieveRequest
   {
         ColumnSet = new ColumnSet("new_firstname"),
         Target = new EntityReference("new_customer", sensorDataId),
         ["partitionId"] = "deviceid-001"
   };

   var response = (RetrieveResponse)service.Execute(request);
   return response.Entity;
}
```

#### [Web API](#tab/webapi)

Here the `partitionid` is being passed as query parameter.

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

### Query rows in a single logical partition of an elastic table

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

### Query rows across all logical partitions of an elastic table

This example retrieves all rows in SensorData table across all logical partitions. Not applying any filter on logical partition allows us to get rows from all logical partitions. Note that this query will not be performant and table should be modeled in a way which keeps queries limited to a single logical partition as much as possible.

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

### Upsert a record in an elastic table

An Upsert operation is similar to update. The difference is that if record with given id and `partitionid` doesn't exist it will be created. If it already exists, it will be updated.

#### [SDK for .NET](#tab/sdk)

This example upserts a row in SensorData table with id = 'ff67610c-82ce-412c-85df-0bbc6521bb01' and `partitionid` = 'deviceid-001'.

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

This example upserts a row in SensorData table with id = 'ff67610c-82ce-412c-85df-0bbc6521bb01' and `partitionid` = 'deviceid-001'. Note that unlike standard tables where `primarykey` is sufficient and `partitionid` columns are needed to uniquely identify a row in elastic tables.

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

### Delete a record in an elastic table

#### [SDK for .NET](#tab/sdk)

This example deletes a row in SensorData table with id = 'ff67610c-82ce-412c-85df-0bbc6521bb01' and `partitionid` = 'deviceid-001'.

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

This example deletes a row in SensorData table with id = 'ff67610c-82ce-412c-85df-0bbc6521bb01' and `partitionid` = 'deviceid-001'.

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

## Query JSON columns in an elastic table

Elastic table supports a new JSON format for text columns. This column can be used to store schema less arbitrary json as per application needs. You can use `ExecuteCosmosSQLQuery` message to run any Cosmos SQL query directly against your elastic table and filter rows based on properties inside JSON.

### Create a column with Json format

This example creates a string column `contoso_SensorValue` with Json format in our `contoso_SensorData` elastic table. For cases where large json need to be stored, instead of using `StringAttributeMetadata` type, we can use `MemoAttributeMetadata` type with JSON format.

#### [SDK for .NET](#tab/sdk)

This function creates a new <xref:Microsoft.Xrm.Sdk.Metadata.StringAttributeMetadata> column using the <xref:Microsoft.Xrm.Sdk.Messages.CreateAttributeRequest> class.

```csharp
public static Guid OrganizationResponse CreateJsonAttribute(IOrganizationService service)
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
POST [Organization URI]/api/data/v9.0/EntityDefinitions(LogicalName='contoso_sensordata')/Attributes HTTP/1.1
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

More information: [Create columns](webapi/create-update-entity-definitions-using-web-api.md#create-columns)

---

### Set Json column data

This example creates a row in `contoso_SensorData` elastic table with JSON values in the `contoso_Value` column.

#### [SDK for .NET](#tab/sdk)

When using SDK for .Net, Json column value need to serialized into a string. Dataverse will store it as raw json in the table after parsing.

```csharp
public static void CreateWithJsonData(IOrganizationService service, Guid sensordataid)
{
   var entity = new Entity("contoso_sensordata", sensordataid)
   {
         Attributes = {
            { "contoso_sensorvalue", "{\"type\":\"Humidity\",\"value\": \"40\",\"timestamp\":\"2023-05-01Z05:00:00\"}" },
            { "deviceid", "deviceid-001" }
            { "partitionid", "deviceid-001" }
         }
   };

   service.Update(entity);
}
```

#### [Web API](#tab/webapi)


**Request**

```http
POST [Organization URI]/api/data/v9.0/contoso_sensordata
{
   "contoso_sensorvalue": {
      "type":"Humidity",
      "value": "40",
      "timestamp":"2023-05-01Z05:00:00"
   }
   "contoso_deviceid" : "device-001"
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

This example runs a query on SensorData elastic table with filter on sensorvalue.type json element to be equal to "Humidity". 

All table columns can be queried with a `c.props` prefix to the schema name of the columns where `"c"` is an alias or a shorthand notation for the elastic table being queried. For example, `contoso_deviceid` column in `contoso_sensordata` table can be referenced in the Cosmos SQL query using `c.props.contoso_deviceid`.

#### [SDK for .NET](#tab/sdk)

The SDK for .NET doesn't yet have request and response classes for the  `ExecuteCosmosSqlQuery` message. You can use <xref:Microsoft.Xrm.Sdk.OrganizationRequest> and <xref:Microsoft.Xrm.Sdk.OrganizationResponse> classes. 

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

This request uses the 

**Request**

```http
GET [Organization URI]/api/data/v9.0/ExecuteCosmosSqlQuery(
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

Often applications need to ingest large amount of data into Dataverse in a short amount of time which can be be processed later. Using Bulk APIs with elastic tables provides a great way to achieve high throughput for such large volume ingestions.

Bulk APIs are optimized for performance when executing multiple write operations on the same table by taking a batch of rows as input in a single write operation. Multiple bulk operation can be run in parallel to achieve high throughput. Read more about them here <!--> TODO. Link here. -->

Elastic tables currently supports following messages for Bulk execution:

- `CreateMultiple`
- `UpdateMultiple`
- `DeleteMultiple`

Support for `UpsertMultiple` mesage will be coming soon. Also, Bulk APIs are currently supported only in SDK for .NET

### CreateMultiple


This example uses CreateMultiple message to create mutiple rows in `contoso_SensorData` elastic table.

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

This example uses UpdateMultiple message to update mutiple rows of `contoso_SensorData` elastic table.

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

This example uses DeleteMultiple message to delete mutiple rows from `contoso_SensorData` elastic table.

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