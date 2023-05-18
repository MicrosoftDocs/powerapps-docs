---
title: "Bulk operations with elastic tables (Preview) (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn how to perform bulk data operations on  elastic tables with code" # 115-145 characters including spaces. This abstract displays in the search result.
ms.topic: article
ms.date: 05/18/2022
author: pnghub
ms.author: gned
ms.reviewer: jdaly
search.audienceType: 
  - developer
contributors:
 - sumantb-msft
 - JimDaly
---
# Bulk operations with elastic tables (Preview)

Often applications need to ingest large amount of data into Dataverse in a short amount of time. Dataverse has a group of messages that are designed to achieve high throughput. With elastic tables, the throughput is very high.

Bulk operations are optimized for performance when executing multiple write operations on the same table by taking a batch of rows as input in a single write operation. Multiple bulk operation can be run in parallel to achieve high throughput. More information <!--> TODO. Link here. -->

Elastic tables currently supports following messages for Bulk execution:

- `CreateMultiple`
- `UpdateMultiple`
- `DeleteMultiple`

Support for `UpsertMultiple` mesage will be coming soon. Also, Bulk APIs are currently supported only in SDK for .NET

## Use CreateMultiple with elastic tables


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


## Use UpdateMultiple with elastic tables

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

## Use DeleteMultiple with elastic tables

This example uses `DeleteMultiple` message to delete multiple rows from `contoso_SensorData` elastic table.

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

### See also

[Use elastic tables (Preview)](elastic-tables.md)<br />
[Create elastic tables (Preview)](create-elastic-tables.md)<br />
[Use elastic tables (Preview)](use-elastic-tables.md)<br />
[Query JSON columns in elastic tables (Preview)](query-json-columns-elastic-tables.md)




