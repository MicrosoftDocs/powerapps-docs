---
title: "Bulk operations with elastic tables (preview) (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn how to perform bulk data operations on  elastic tables with code" # 115-145 characters including spaces. This abstract displays in the search result.
ms.topic: article
ms.date: 05/27/2023
author: pnghub
ms.author: gned
ms.reviewer: jdaly
contributors:
 - sumantb-msft
 - JimDaly
---
# Bulk operations with elastic tables (Preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

Often applications need to ingest large amount of data into Dataverse in a short amount of time. Dataverse has a group of messages that are designed to achieve high throughput. With elastic tables, the throughput can be much higher.

Bulk operations are optimized for performance when executing multiple write operations on the same table by taking a batch of rows as input in a single write operation. For elastic tables, we recommend sending 100 items in a batch. Multiple bulk operation can be run in parallel to achieve high throughput. More information [Send parallel requests](send-parallel-requests.md)

Elastic tables currently supports following messages for bulk operations:

- `CreateMultiple`
- `UpdateMultiple`
- `DeleteMultiple`

Support for `UpsertMultiple` message will be coming soon. Also, these messages are currently supported only using the SDK for .NET.

## Use CreateMultiple with elastic tables


This example uses the `CreateMultiple` message to create multiple rows in `contoso_SensorData` elastic table.

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


## Use UpdateMultiple with elastic tables

This example uses `UpdateMultiple` message to update multiple rows of `contoso_SensorData` elastic table.

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

    // Use CreateMultipleRequest
    UpdateMultipleRequest updateMultipleRequest = new()
    {
        Targets = entities,
    };
    return service.Execute(request);
}
```

## Use DeleteMultiple with elastic tables

This example uses `DeleteMultiple` message to delete multiple rows from `contoso_SensorData` elastic table.

```csharp
public static OrganizationResponse DeleteMultiple(IOrganizationService service)
{
   string tableLogicalName = "contoso_sensordata";

    EntityReference record1 = new EntityReference(
        tableLogicalName, 
        new KeyAttributeCollection
        {
            { "contoso_sensordataid", "3f56361a-b210-4a74-8708-3c664038fa41" },
            { "partitionid", "deviceid-001" }
        });

    EntityReference record2 = new EntityReference(
        tableLogicalName,
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

### See also

[Use elastic tables](elastic-tables.md)<br />
[Create elastic tables using code](create-elastic-tables.md)<br />
[Use elastic tables](use-elastic-tables.md)<br />
[Query JSON columns in elastic tables](query-json-columns-elastic-tables.md)<br />
[Elastic table sample code (preview)](elastic-table-samples.md)
