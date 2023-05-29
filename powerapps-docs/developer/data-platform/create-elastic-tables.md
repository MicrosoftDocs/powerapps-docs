---
title: "Create elastic tables using code (preview) (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn how to create elastic tables with code" # 115-145 characters including spaces. This abstract displays in the search result.
ms.topic: article
ms.date: 05/23/2022
author: pnghub
ms.author: gned
ms.reviewer: jdaly
search.audienceType: 
  - developer
contributors:
 - sumantb-msft
 - JimDaly
---

# Create elastic tables using code (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

You can create elastic tables using [Power Apps](https://make.powerapps.com/) without writing code. More information: [Create and edit tables using Power Apps](../../maker/data-platform/create-edit-entities-portal.md).

But sometimes it is useful to be able to create and update table definitions with code. These examples create a new elastic table with the `SchemaName` `contoso_SensorData` using the Dataverse SDK for .NET and Web API. Use the `EntityMetadata.TableType` property with a value of `Elastic` to create an elastic table with code. When this is not set, the value will default to `Standard` and a standard table will be created.

#### [SDK for .NET](#tab/sdk)

> [!NOTE]
> At the time of this writing the SDK [EntityMetadata](xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata) class doesn't have the `TableType` property to create an elastic table. You will need to use the Web API until this is added.
>
> After the SDK is updated, you will be able to use the [CreateEntityRequest](xref:Microsoft.Xrm.Sdk.Messages.CreateEntityRequest) class as shown below.

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

The [CreateEntityResponse](xref:Microsoft.Xrm.Sdk.Messages.CreateEntityResponse) has these properties:

- [AttributeId](xref:Microsoft.Xrm.Sdk.Messages.CreateEntityResponse.AttributeId): The ID of the `contoso_SensorType` primary name string column.
- [EntityId](xref:Microsoft.Xrm.Sdk.Messages.CreateEntityResponse.EntityId): The ID of the `contoso_SensorData` table.


More information: [Create a custom table using code](org-service/create-custom-entity.md)

#### [Web API](#tab/webapi)

Set the [EntityMetadata](xref:Microsoft.Dynamics.CRM.EntityMetadata) `TableType` property to `Elastic` and include a [StringAttributeMetadata](xref:Microsoft.Dynamics.CRM.StringAttributeMetadata) column with the `IsPrimaryName` property value set to `true`.

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

In this case, `417129e1-207c-e511-80d2-00155d2a68d2` is the ID of the `contoso_SensorData` table. You must make a separate request to get the ID of the `contoso_SensorType` primary name string column.

More information: [Create and update table definitions using the Web API](webapi/create-update-entity-definitions-using-web-api.md)

---

## Adding Columns

You can create columns in elastic tables using [Power Apps](https://make.powerapps.com/) without writing code. More information: [Create and edit tables using Power Apps](../../maker/data-platform/create-edit-entities-portal.md).

Columns can also be created using the SDK or Web API, but there are limits on the types of columns you can add. Currently you cannot add these types of columns:

- Money (`MoneyAttributeMetadata`)
- MultiSelectPicklist (`MultiSelectPicklistAttributeMetadata`)
- State (`StateAttributeMetadata`)
- Status (`StatusAttributeMetadata`)
- File (`FileAttributeMetadata`)
- Image (`ImageAttributeMetadata`)
- Calculated, Rollup, or Formula Columns

Elastic tables support string columns that store JSON data.

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
            SchemaName = "contoso_EnergyConsumption",
            RequiredLevel = new AttributeRequiredLevelManagedProperty(AttributeRequiredLevel.None),
            MaxLength = 1000,
            FormatName = StringFormatName.Json,
            DisplayName = new Label("Energy Consumption", 1033),
            Description = new Label("Contains information about energy consumed by the IoT devices", 1033)
         },
         SolutionUniqueName  = "examplesolution"
   };

   var response = (CreateAttributeResponse)service.Execute(request);

   return response.AttributeId;
}
```

More information: [Add a String column to a table](org-service/create-custom-entity.md#add-a-string-column-to-the-custom-table)


#### [Web API](#tab/webapi)

This request creates a new <xref:Microsoft.Dynamics.CRM.StringAttributeMetadata> column by posting to the Web API `EntityDefinitions` resource referring to the `contoso_SensorData` table.

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
            "Label":"Contains information about energy consumed by the IoT devices",
            "LanguageCode":1033
         }
      ]
   },
   "DisplayName":{
      "@odata.type":"Microsoft.Dynamics.CRM.Label",
      "LocalizedLabels":[
         {
            "@odata.type":"Microsoft.Dynamics.CRM.LocalizedLabel",
            "Label":"Energy Consumption",
            "LanguageCode":1033
         }
      ]
   },
   "RequiredLevel":{
      "Value":"None",
      "CanBeChanged":true,
      "ManagedPropertyLogicalName":"canmodifyrequirementlevelsettings"
   },
   "SchemaName":"contoso_EnergyConsumption",
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

## Alternate keys

You cannot create custom alternate keys for elastic tables.

Each elastic table is created with one alternate key using these values:

- Display Name: **Entity key for NoSql Entity that contains PrimaryKey and PartitionId attributes**
- Name: `KeyForNoSqlEntityWithPKPartitionId`
- LogicalName: `keyfornosqlentitywithpkpartitionid`

This alternate key has the key values: `<table primary key name>` and `partitionid`.

If you need to reference a record that has a `partitionid` value set to a value other than the default value (that is equal to the value of the primary key) you can reference the record using this alternate key.

More information: [Use an alternate key to reference a record](use-alternate-key-reference-record.md)

## Adding Relationships

Dataverse currently does not support creating Many-to-Many relationships with elastic tables.

One-to-Many relationships are supported for elastic tables with following limitations:

- Cascading is not supported. Cascading behavior must be set to `Cascade.None` when creating relationship.
- Formatted values for lookup columns are not returned when the following conditions are true:

   - The table being retrieved is a standard table and the lookup refers to an elastic table.
   - The elastic table `partitionid` value is set to a value other than the default value, the primary key value of the elastic table row. In other words, when you are using a custom `partitionid` value. More information: [Choosing a PartitionId value](elastic-tables.md#choosing-a-partitionid-value)

Elastic tables support One-to-Many relationships and related rows can be retrieved when retrieving a record. Related records can't be included in a query. More information : [Return related rows in a query](use-elastic-tables.md#return-related-rows-in-a-query)


## Next steps

> [!div class="nextstepaction"]
> [Use elastic tables using code](use-elastic-tables.md)<br/>

### See also

[Elastic tables](elastic-tables.md)<br />
[Query JSON columns in elastic tables](query-json-columns-elastic-tables.md)<br />
[Bulk operations with elastic tables](bulk-operations-elastic-tables.md)<br />
