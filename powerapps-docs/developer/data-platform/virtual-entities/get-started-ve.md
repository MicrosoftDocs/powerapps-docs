---
title: "Get started with virtual tables (entities) (Microsoft Dataverse) | Microsoft Docs"
description: "Virtual tables enable integration of data residing in external systems with Microsoft Dataverse."
ms.date: 08/08/2024
author: mkannapiran
ms.author: kamanick
ms.reviewer: pehecke
ms.topic: get-started
ms.collection: get-started
applies_to: 
  - "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - phecke
  - JimDaly
---

# Get started with virtual tables (entities)

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

*Virtual tables*, also known as *virtual entities*, enable the integration of data residing in external systems with Microsoft Dataverse. This integration seamlessly represents that external data as tables in Dataverse, without replication of data and often without custom coding.

Virtual tables replace previous client-side and server-side approaches to integrating external data, which required customized code and suffered from numerous limitations. These limitations include imperfect integration, data duplication, or extensive commitment of development resources. In addition, for administrators and system customizers, the use of virtual tables greatly simplifies administration and configuration.

> [!NOTE]
> This section discusses the implications of virtual tables for developers. For more information about managing virtual tables from the user interface, see [Create and edit virtual tables that contain data from an external data source](../../../maker/data-platform/create-edit-virtual-entities.md).

## Virtual tables, data providers, and data sources

A virtual table includes a definition of a table in Dataverse without the associated physical table for record storage in the Dataverse database. During runtime, when a record is required, its state is dynamically retrieved from the associated external system. Each virtual table type is associated with a *virtual table data provider* and (optionally) some configuration information from an associated *virtual table data source*.

<!-- TODO:
A data provider is a particular type of Dataverse plug-in, which is registered against CRUD events that occur in the platform. More information: [Write a plug-in](../write-plugin.md) -->

The following data providers ship with Dataverse:

- An [OData v4](https://www.odata.org/documentation/) provider is included with the service and is installed by default. This provider supports create, read (retrieve, retrieve multiple), update and delete (CRUD) operations.
- An [Azure Cosmos DB](/azure/cosmos-db) (formerly *Microsoft Document DB*) provider is available from [AppSource](https://appsource.microsoft.com).

If a data provider can't be found for your external data source, you can develop a *custom virtual table data provider*. More information: [Virtual table data providers](custom-ve-data-providers.md)

Full CRUD operation is now supported for custom virtual table data provider. Developers can implement plug-ins, and register them using the Plug-in Registration tool, for each of the CRUD operations supporting the virtual table.

## Virtual table creation and mapping

Initially, defining a virtual table is the same as defining a custom table. You specify the table, columns, and relationships for the new virtual table type. You then connect the virtual table to a data provider to manage data operations.

The custom table type and its columns must be mapped to the corresponding data in the external data source. For example, a virtual table might be represented as a row in an external relational database, and each of its columns might correspond to a column in that row. These external data names are often different than their corresponding virtual table names. A specific and required mapping occurs for the entity ID field - the data provider must be able to provide this GUID and associate it to the external record that represents this record. The most direct way to achieve this result is to actually use GUIDs as primary keys in the external data source.  

In this example, a corresponding virtual table data source would also be provided to supply user and connection information for the external database.

## Limitations of virtual tables

The following are limitations of virtual tables that should be considered.

- Only organization-owned tables are supported. The security filtering applied to user-owned tables isn't supported. Access to the virtual table data can be turned on or off for individual users based on their security role. Field-level security isn't supported.
- It must be possible to model the external data as a Dataverse table. This means:
  - All tables in the external data source must have an associated GUID primary key.  
  - All table properties must be represented as Dataverse table columns. You can use simple types representing text, numbers, choices, dates, images, and lookups.
  - You must be able to model any table relationships in Dataverse.
  - A column on a virtual table can't be calculated or rollup.  Any desired calculations must be done on the external side, possibly within or directed by the data provider.
  - Although you can add virtual table columns as a lookup on a grid or other UI views, you can't filter or sort based on this virtual table lookup column.
- Auditing isn't supported.
- Search functionality isn't supported for virtual tables as they don't persist data.
- Charts and dashboards aren't supported for virtual tables.
- Virtual tables can't be enabled for queues.
- Offline caching of values isn't supported for virtual tables.
- A virtual table can't represent an activity and don't support business process flows.
- Once created, a virtual table can't be changed to be a standard (nonvirtual) table.  The reverse is also true whereas a standard table can't be converted into a virtual table.
- Selecting attributes in Retrieve and RetrieveMultiple queries won't be applied since all attributes are returned

For more information about how these limitations are reflected in the Dataverse API, see [API considerations of virtual tables](api-considerations-ve.md).

### See also

[Virtual table walkthrough using the OData v4 Data Provider](../../../maker/data-platform/virtual-entity-walkthrough-using-odata-provider.md)<br/>
[API considerations of virtual tables](api-considerations-ve.md)<br />
[Custom virtual table data providers](custom-ve-data-providers.md)<br />
[Sample: Generic virtual table data provider plug-in](sample-generic-ve-plugin.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
