---
title: "Get started with virtual tables (Common Data Service) | Microsoft Docs"
description: "Virtual tables enable the integration of data residing in external systems by seamlessly representing that data as tables in Common Data Service, without replication of data and often without custom coding."
ms.date: 11/09/2020
ms.service: powerapps
ms.topic: "get-started-article"
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

# Get started with virtual tables

[!INCLUDE[cc-data-platform-banner](../../../includes/cc-data-platform-banner.md)]

Virtual tables enable the integration of data residing in external systems by seamlessly representing that data as tables in Common Data Service, without replication of data and often without custom coding. Virtual tables support create, updates and delete of data in the external system. 

Virtual tables replace previous client-side and server-side approaches to integrating external data, which required customized code and suffered from numerous limitations, including imperfect integration, data duplication, or extensive commitment of development resources.  In addition, for administrators and system customizers, the use of virtual tables greatly simplifies administration and configuration.

> [!NOTE]
> This section discusses the implications of virtual tables for developers. For more information about managing virtual tables from the user interface, see [Create and edit virtual tables that contain data from an external data source](../../../maker/common-data-service/create-edit-virtual-entities.md).

## Virtual tables, data providers and data sources

A virtual table is a definition of a table in the Common Data Service platform metadata without the associated physical tables for table instances created in the Common Data Service database. Instead during runtime, when a table instance is required, its state is dynamically retrieved from the associated external system. Each virtual table type is associated with a *virtual table data provider* and (optionally) some configuration information from an associated *virtual table data source*. 

The following data providers ship with Common Data Service:
- An [OData v4](https://www.odata.org/documentation/) provider is included with the service and is installed by default.
- An [Azure Cosmos DB](https://docs.microsoft.com/azure/cosmos-db) (formerly *Microsoft Document DB*) provider is available from [AppSource](https://appsource.microsoft.com).

If a data provider cannot be found for your external data source, you can develop a *custom virtual table data provider*; for more information, see [Virtual table data providers](custom-ve-data-providers.md).

## Virtual table creation and mapping

Initially, defining a virtual table is the same as defining a custom table: you specify the table, attributes, and relationships for the new virtual table type. However, additionally, you then connect the virtual table to a data provider to manage data retrieval. The custom table type and its fields must be mapped to the corresponding data in the external data source.  For example, a virtual table might be represented as a row in an external relational database, and each of its fields might correspond to a column in that row.  (Note that these external data names are often different than their corresponding virtual table names.) A specific, required mapping occurs for the table ID field: the data provider must be able to provide this GUID and associate it to the external record that represents this table instance. The most direct way to achieve this is to actually use GUIDs as primary keys in the external data source.  

In this example, a corresponding virtual table data source would also be provided to supply user and connection information for the external database.

## Limitations of virtual tables

Following are the limitations in virtual tables that must be considered.

- Only organization-owned tables are supported. The security filtering applied to user-owned tables is not supported. Access to the virtual table data can be turned on or off for individual users based on their security role. Field-level security is not supported.
- It must be possible to model the external data as a Common Data Service table. This means:
    - All tables in the external data source must have an associated GUID primary key.  
    - All table properties must be represented as Common Data Service attributes. You can use simple types representing text, numbers, optionsets, dates, images, and lookups. 
    - You must be able to model any table relationships in Common Data Service.
    - An attribute on a virtual table cannot be calculated or rollup.  Any desired calculations must be done on the external side, possibly within or directed by the data provider.
    - Although you can add virtual table columns as a lookup on a grid or other UI views, you cannot filter or sort based on this virtual table lookup column.
- Auditing and change tracking is not supported.
- Virtual tables cannot be enabled for queues.
- Offline caching of values is not supported for virtual tables.
- A virtual table cannot represent an activity and do not support business process flows.
- Once created, a virtual table cannot be changed to be a standard (non-virtual) table.  The reverse is also true: a standard table cannot be converted into a virtual table.

For more information about how these limitations are reflected in the Common Data Service API, see [API considerations of virtual tables](api-considerations-ve.md). 

### See also

[API considerations of virtual tables](api-considerations-ve.md)<br />
[Custom virtual table data providers](custom-ve-data-providers.md)<br />
[Sample: Generic virtual table data provider plug-in](sample-generic-ve-plugin.md)
