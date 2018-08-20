---
title: "Get started with Virtual entities (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "mayadumesh" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Virtual Entities

In Common Data Service for Apps, virtual entities enable the integration of data residing in external systems by seamlessly representing that data as entities in Dynamics 365, without replication of data and often without custom coding. The initial implementation of this feature provides just read-only support for such entities, and has a number of other limitations described in the section [Limitations of Virtual Entities](#limitations-of-virtual-entities) below. Besides these limitations, virtual entities behave the same as other custom entities. 

Virtual entities replace previous client-side and server-side approaches to integrating external data, which required customized code and suffered from numerous limitations, including imperfect integration, data duplication, or extensive commitment of development resources.  In addition, for administrators and system customizers, the use of virtual entities greatly simplifies administration and configuration.

This section discusses the implications of virtual entities for developers. For more information about managing virtual entities from the user interface, see [Create and edit virtual entities](/dynamics365/customer-engagement/customize/create-edit-virtual-entities). 

## Virtual entities, data providers and data sources
A virtual entity is a definition of an entity in the CDS for Apps platform metadata without the associated physical tables for entity instances created in the CDS for Apps database. Instead during runtime, when an entity instance is required, its state is dynamically retrieved from the associated external system. Each virtual entity type is associated with a *virtual entity data provider* and (optionally) some configuration information from an associated *virtual entity data source*. 

A data provider is a particular type of CDS for Apps [plugin](../plugin-development.md), which is registered against CRUD events that occur in the platform. This initial release only supports READ operations. 

The following data providers ship with CDS for Apps:
- An [OData v4](http://www.odata.org/documentation/) provider is included with the service and is installed by default.
- An [Azure Cosmos DB](https://docs.microsoft.com/azure/cosmos-db) (formerly _Microsoft Document DB_) provider is available from [AppSource](https://appsource.microsoft.com).

Additional providers will be made available by Microsoft, its partners, or other third parties. If a data provider cannot be found for your external data source, you can develop a _custom virtual entity data provider_; for more information, see [Virtual entity data providers](custom-ve-data-providers.md).

## Virtual entity creation and mapping
Initially, defining a virtual entity is the same as defining a custom entity: you specify the entity, attributes, and relationships for the new virtual entity type. However, additionally, you then connect the virtual entity to a data provider to manage data retrieval. The custom entity type and its fields must be mapped to the corresponding data in the external data source.  For example, a virtual entity might be represented as a row in an external relational database, and each of its fields might correspond to a column in that row.  (Note that these external data names are often different than their corresponding virtual entity names.) A specific, required mapping occurs for the entity ID field: the data provider must be able to provide this GUID and associate it to the external record that represents this entity instance. The most direct way to achieve this is to actually use GUIDs as primary keys in the external data source.  

In this example, a corresponding virtual entity data source would also be provided to supply user and connection information for the external database.

## Limitations of Virtual Entities
In this release, there are some limitations to virtual entities that you need to be aware of when evaluating whether you can use virtual entities with your external data.
- Data is read-only. The virtual entity feature doesn’t support pushing changes made in CDS for Apps back to the external system.
- Only organization-owned entities are supported. The security filtering applied to user-owned entities is not supported. Access to the virtual entity data can be turned on or off for individual users based on their security role. Field-level security is not supported.
- It must be possible to model the external data as a CDS for Apps entity. This means:
  - All entities in the external data source must have an associated GUID primary key.  
  - All entity properties must be represented as CDS for Apps attributes. You can use simple types representing text, numbers, optionsets, dates, images, and lookups. 
  - You must be able to model any entity relationships in CDS for Apps.
  - An attribute on a virtual entity cannot be calculated or rollup.  Any desired calculations must be done on the external side, possibly within or directed by the data provider.

- Auditing and change tracking is not supported.  These may be implemented within the external data store.
- Virtual entities cannot be enabled for queues.
- Offline caching of values is not supported for virtual entities.
- A virtual entity cannot represent an activity and do not support business process flows.
- Once created, a virtual entity cannot be changed to be a standard (non-virtual) entity.  The reverse is also true: a standard entity cannot be converted into a virtual entity.

<!-- TODO: Make bulleted list into table.  Make more complete by reviewing API modification tables. -->

For more information about how these limitations are reflected in the CDS for Apps API, see [API considerations of virtual entities](api-considerations-ve.md). 