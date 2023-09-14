---
title: Create elastic tables using code (preview)
description: Learn how to create Dataverse elastic tables with code.
ms.topic: article
ms.date: 07/18/2023
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

By using [Power Apps](https://make.powerapps.com/), you can [create and edit elastic tables without writing code](../../maker/data-platform/create-edit-entities-portal.md).

However, it's sometimes useful to use code to create and update table definitions. The following examples show how to use the Dataverse SDK for .NET and Web API to create a new elastic table that has the schema name `contoso_SensorData`. To create an elastic table through code, use the `EntityMetadata.TableType` property with a value of `Elastic`. If you don't set `TableType`, the default value `Standard` is used, and a standard table is created.

#### [SDK for .NET](#tab/sdk)

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

[CreateEntityResponse](xref:Microsoft.Xrm.Sdk.Messages.CreateEntityResponse) has these properties:

- [AttributeId](xref:Microsoft.Xrm.Sdk.Messages.CreateEntityResponse.AttributeId): The ID of the `contoso_SensorType` primary name string column.
- [EntityId](xref:Microsoft.Xrm.Sdk.Messages.CreateEntityResponse.EntityId): The ID of the `contoso_SensorData` table.

[Learn more about creating custom tables using the SDK for .NET](org-service/create-custom-entity.md).

#### [Web API](#tab/webapi)

Set the [EntityMetadata](xref:Microsoft.Dynamics.CRM.EntityMetadata) `TableType` property to `Elastic`, and include a [StringAttributeMetadata](xref:Microsoft.Dynamics.CRM.StringAttributeMetadata) column where the value of the `IsPrimaryName` property is set to `true`.

**Request:**

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

**Response:**

```http
HTTP/1.1 204 No Content
OData-Version: 4.0
OData-EntityId: [Organization URI]/api/data/v9.2/EntityDefinitions(417129e1-207c-e511-80d2-00155d2a68d2) 
```

In this case, `417129e1-207c-e511-80d2-00155d2a68d2` is the ID of the `contoso_SensorData` table. You must make a separate request to get the ID of the `contoso_SensorType` primary name string column.

[Learn more about creating and updating table definitions using the Web API](webapi/create-update-entity-definitions-using-web-api.md).

---

## Adding columns

By using [Power Apps](https://make.powerapps.com/), you can [create columns in elastic tables without writing code](../../maker/data-platform/create-edit-entities-portal.md).

You can also create columns by using the SDK or Web API. However, there are limits on the types of columns that you can add. Currently, you can't add the following types of columns:

- Money (`MoneyAttributeMetadata`)
- MultiSelectPicklist (`MultiSelectPicklistAttributeMetadata`)
- State (`StateAttributeMetadata`)
- Status (`StatusAttributeMetadata`)
- File (`FileAttributeMetadata`)
- Image (`ImageAttributeMetadata`)
- Calculated, Rollup, or Formula Columns

Elastic tables support string columns that store JavaScript Object Notation (JSON) data.

### Create a column with JSON format

This example creates a `contoso_SensorValue` string column with JSON format in the `contoso_SensorData` elastic table. For cases where a large amount of JSON data must be stored, you can use the `MemoAttributeMetadata` column type with JSON format instead of using the `StringAttributeMetadata` column type.

#### [SDK for .NET](#tab/sdk)

This function creates a [StringAttributeMetadata](xref:Microsoft.Xrm.Sdk.Metadata.StringAttributeMetadata) column by using the [CreateAttributeRequest class](xref:Microsoft.Xrm.Sdk.Messages.CreateAttributeRequest).

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

For more information, go to [Add a String column to the custom table](org-service/create-custom-entity.md#add-a-string-column-to-the-custom-table).

#### [Web API](#tab/webapi)

This request creates a [StringAttributeMetadata](xref:Microsoft.Dynamics.CRM.StringAttributeMetadata) column by posting to the Web API `EntityDefinitions` resource that refers to the `contoso_SensorData` table.

**Request:**

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

**Response:**

```http
HTTP/1.1 204 No Content
OData-Version: 4.0
OData-EntityId: [Organization URI]/api/data/v9.2/EntityDefinitions(402fa40f-287c-e511-80d2-00155d2a68d2)/Attributes(f01bef16-287c-e511-80d2-00155d2a68d2)
```

[Learn more about creating columns using the Web API](webapi/create-update-column-definitions-using-web-api.md#create-columns).

---

## Alternate keys

You can't create custom alternate keys for elastic tables.

Each elastic table is created with one alternate key that uses these values:

- Display Name: **Entity key for NoSql Entity that contains PrimaryKey and PartitionId attributes**
- Name: `KeyForNoSqlEntityWithPKPartitionId`
- LogicalName: `keyfornosqlentitywithpkpartitionid`

This alternate key has the key values `<table primary key name>` and `partitionid`.

If you must reference a record where a `partitionid` value is set, you can reference it by using this alternate key.

[Learn how to use an alternate key to reference a record](use-alternate-key-reference-record.md).

## Adding relationships

Dataverse currently doesn't support creating many-to-many relationships with elastic tables.

One-to-many relationships are supported for elastic tables with the following limitations:

- Cascading isn't supported. Cascading behavior must be set to `Cascade.None` when the relationship is created.
- Formatted values for lookup columns aren't returned when the following conditions are true:

    - The table that is retrieved is a standard table, and the lookup refers to an elastic table.
    - You're using a custom elastic table `partitionid` value. In other words, the `partitionid` value is set to something other than the default value (the primary key value of the elastic table row). [Learn how to choose a partitionid value](elastic-tables.md#choosing-a-partitionid-value).

Elastic tables support one-to-many relationships, and related rows can be retrieved when a record is retrieved. Related records can't be included in a query. [Learn how to return related rows in a query](use-elastic-tables.md#return-related-rows-in-a-query).

## Next steps

> [!div class="nextstepaction"]
> [Use elastic tables using code](use-elastic-tables.md)<br/>

### See also

[Elastic tables for developers (preview)](elastic-tables.md)   
[Query JSON columns in elastic tables (preview)](query-json-columns-elastic-tables.md)   
[Use bulk operation messages (preview)](bulk-operations.md)   
[Elastic table sample code (preview)](elastic-table-samples.md)
