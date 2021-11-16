---
title: "Get started with virtual tables (entities) (Microsoft Dataverse) | Microsoft Docs"
description: "Virtual tables enable the integration of data residing in external systems by seamlessly representing that data as tables in Microsoft Dataverse, without replication of data and often without custom coding."
ms.date: 04/08/2021
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

# Get started with virtual tables (entities)

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

*Virtual tables* (also known as *virtual entities*) enable the integration of data residing in external systems by seamlessly representing that data as tables in Microsoft Dataverse, without replication of data and often without custom coding.

Virtual tables replace previous client-side and server-side approaches to integrating external data, which required customized code and suffered from numerous limitations, including imperfect integration, data duplication, or extensive commitment of development resources.  In addition, for administrators and system customizers, the use of virtual tables greatly simplifies administration and configuration.

> [!NOTE]
> This section discusses the implications of virtual tables for developers. For more information about managing virtual tables from the user interface, see [Create and edit virtual tables that contain data from an external data source](../../../maker/data-platform/create-edit-virtual-entities.md).

## Virtual tables, data providers and data sources

A virtual table is a definition of a table in the Dataverse platform without the associated physical tables for table instances created in the Dataverse database. Instead during runtime, when a table instance is required, its state is dynamically retrieved from the associated external system. Each virtual table type is associated with a *virtual table data provider* and (optionally) some configuration information from an associated *virtual table data source*.

<!-- TODO:
A data provider is a particular type of Dataverse plug-in, which is registered against CRUD events that occur in the platform. More information: [Write a plug-in](../write-plugin.md) -->

The following data providers ship with Dataverse:

- An [OData v4](https://www.odata.org/documentation/) provider is included with the service and is installed by default. This provider supports create, read (retrieve, retrieve multiple), update and delete operations.
- An [Azure Cosmos DB](https://docs.microsoft.com/azure/cosmos-db) (formerly *Microsoft Document DB*) provider is available from [AppSource](https://appsource.microsoft.com).


If a data provider cannot be found for your external data source, you can develop a *custom virtual table data provider*; for more information, see [Virtual table data providers](custom-ve-data-providers.md). Full CRUD operation is now supported for custom virtual table data provider. Developers can implement plug-ins and register them using the Plug-in Registration tool for each of the CRUD operation supporting the virtual table.

## Virtual table creation and mapping

Initially, defining a virtual table is the same as defining a custom table: you specify the table, columns, and relationships for the new virtual table type. However, additionally, you then connect the virtual table to a data provider to manage data operations. The custom table type and its columns must be mapped to the corresponding data in the external data source.  For example, a virtual table might be represented as a row in an external relational database, and each of its columns might correspond to a column in that row.  (Note that these external data names are often different than their corresponding virtual table names.) A specific, required mapping occurs for the entity ID field: the data provider must be able to provide this GUID and associate it to the external record that represents this table instance. The most direct way to achieve this is to actually use GUIDs as primary keys in the external data source.  

In this example, a corresponding virtual table data source would also be provided to supply user and connection information for the external database.

## Limitations of virtual tables

Following are the limitations in virtual tables that must be considered.

- Only organization-owned tables are supported. The security filtering applied to user-owned tables is not supported. Access to the virtual table data can be turned on or off for individual users based on their security role. Field-level security is not supported.
- It must be possible to model the external data as a Dataverse table. This means:
    - All tables in the external data source must have an associated GUID primary key.  
    - All table properties must be represented as Dataverse table columns. You can use simple types representing text, numbers, choices, dates, images, and lookups.
    - You must be able to model any table relationships in Dataverse.
    - A column on a virtual table cannot be calculated or rollup.  Any desired calculations must be done on the external side, possibly within or directed by the data provider.
    - Although you can add virtual table columns as a lookup on a grid or other UI views, you cannot filter or sort based on this virtual table lookup column.
- Auditing is not supported.
- Search functionality is not support for virtual tables as they do not persist data.
- Charts and dashboards are not supported for virtual tables.
- Virtual tables cannot be enabled for queues.
- Offline caching of values is not supported for virtual tables.
- A virtual table cannot represent an activity and do not support business process flows.
- Once created, a virtual table cannot be changed to be a standard (non-virtual) table.  The reverse is also true: a standard table cannot be converted into a virtual table.

For more information about how these limitations are reflected in the Dataverse API, see [API considerations of virtual tables](api-considerations-ve.md).

### See also
[Virtual table walkthrough using the OData v4 Data Provider](../../../maker/data-platform/virtual-entity-walkthrough-using-odata-provider.md)<br/>
[API considerations of virtual tables](api-considerations-ve.md)<br />
[Custom virtual table data providers](custom-ve-data-providers.md)<br />
[Sample: Generic virtual table data provider plug-in](sample-generic-ve-plugin.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
