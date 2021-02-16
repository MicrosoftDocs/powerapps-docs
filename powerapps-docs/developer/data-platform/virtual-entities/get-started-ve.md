---
title: "Get started with virtual entities (Microsoft Dataverse) | Microsoft Docs"
description: "Virtual entities enable the integration of data residing in external systems by seamlessly representing that data as entities in Microsoft Dataverse, without replication of data and often without custom coding."
ms.date: 06/24/2020
ms.service: powerapps
ms.topic: "get-started-article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: 14c5fbbc-98db-4e49-b245-2c84c1cd11cd
author: "Sunil-Garg" # GitHub ID
ms.author: "pehecke"
manager: "ryjones"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Get started with virtual entities

[!INCLUDE[cc-data-platform-banner](../../../includes/cc-data-platform-banner.md)]

Virtual entities enable the integration of data residing in external systems by seamlessly representing that data as entities in Microsoft Dataverse, without replication of data and often without custom coding. Virtual entities support create, updates and delete of data in the external system. 

Virtual entities replace previous client-side and server-side approaches to integrating external data, which required customized code and suffered from numerous limitations, including imperfect integration, data duplication, or extensive commitment of development resources.  In addition, for administrators and system customizers, the use of virtual entities greatly simplifies administration and configuration.

> [!NOTE]
> This section discusses the implications of virtual entities for developers. For more information about managing virtual entities from the user interface, see [Create and edit virtual entities that contain data from an external data source](../../../maker/data-platform/create-edit-virtual-entities.md).

## Virtual entities, data providers and data sources

A virtual entity is a definition of an entity in the Dataverse platform metadata without the associated physical tables for entity instances created in the Dataverse database. Instead during runtime, when an entity instance is required, its state is dynamically retrieved from the associated external system. Each virtual entity type is associated with a *virtual entity data provider* and (optionally) some configuration information from an associated *virtual entity data source*. 

<!-- TODO:
A data provider is a particular type of Dataverse plug-in, which is registered against CRUD events that occur in the platform. More information: [Write a plug-in](../write-plugin.md) -->

The following data providers ship with Dataverse:
- An [OData v4](https://www.odata.org/documentation/) provider is included with the service and is installed by default.
- An [Azure Cosmos DB](https://docs.microsoft.com/azure/cosmos-db) (formerly *Microsoft Document DB*) provider is available from [AppSource](https://appsource.microsoft.com).

If a data provider cannot be found for your external data source, you can develop a *custom virtual entity data provider*; for more information, see [Virtual entity data providers](custom-ve-data-providers.md).

## Virtual entity creation and mapping

Initially, defining a virtual entity is the same as defining a custom entity: you specify the entity, attributes, and relationships for the new virtual entity type. However, additionally, you then connect the virtual entity to a data provider to manage data retrieval. The custom entity type and its fields must be mapped to the corresponding data in the external data source.  For example, a virtual entity might be represented as a row in an external relational database, and each of its fields might correspond to a column in that row.  (Note that these external data names are often different than their corresponding virtual entity names.) A specific, required mapping occurs for the entity ID field: the data provider must be able to provide this GUID and associate it to the external record that represents this entity instance. The most direct way to achieve this is to actually use GUIDs as primary keys in the external data source.  

In this example, a corresponding virtual entity data source would also be provided to supply user and connection information for the external database.

## Limitations of Virtual Entities

Following are the limitations in virtual entities that must be considered.

- Only organization-owned entities are supported. The security filtering applied to user-owned entities is not supported. Access to the virtual entity data can be turned on or off for individual users based on their security role. Field-level security is not supported.
- It must be possible to model the external data as a Dataverse entity. This means:
    - All entities in the external data source must have an associated GUID primary key.  
    - All entity properties must be represented as Dataverse attributes. You can use simple types representing text, numbers, optionsets, dates, images, and lookups. 
    - You must be able to model any entity relationships in Dataverse.
    - An attribute on a virtual entity cannot be calculated or rollup.  Any desired calculations must be done on the external side, possibly within or directed by the data provider.
    - Although you can add virtual entity columns as a lookup on a grid or other UI views, you cannot filter or sort based on this virtual entity lookup column.
- Auditing and change tracking is not supported.
- Virtual entities cannot be enabled for queues.
- Offline caching of values is not supported for virtual entities.
- A virtual entity cannot represent an activity and do not support business process flows.
- Once created, a virtual entity cannot be changed to be a standard (non-virtual) entity.  The reverse is also true: a standard entity cannot be converted into a virtual entity.

For more information about how these limitations are reflected in the Dataverse API, see [API considerations of virtual entities](api-considerations-ve.md). 

### See also

[API considerations of virtual entities](api-considerations-ve.md)<br />
[Custom virtual entity data providers](custom-ve-data-providers.md)<br />
[Sample: Generic virtual entity data provider plug-in](sample-generic-ve-plugin.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]