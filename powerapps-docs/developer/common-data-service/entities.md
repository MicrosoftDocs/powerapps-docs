---
title: Common Data Service tables | Microsoft Docs
description: Learn about the tables available in Common Data Service.
services: ''
suite: powerapps
documentationcenter: na
author: "mayadumesh" # GitHub ID
ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 11/08/2020
ms.author: jdaly
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Common Data Service tables

[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

Providing storage for data is the most important function of Common Data Service. Common Data Service includes a base set of tables that provide structure for data used by business applications. 

You can view the base set of tables in the [Common Data Service table reference](reference/about-entity-reference.md).

## Modify tables

You can modify the table metadata using several different methods.

### Use designers

There are several ways to edit table metadata using designers.


|Designer  |Description  |
|---------|---------|
|powerapps.com|The easiest and most common approach to modify the schema is to use the [powerapps.com](https://make.powerapps.com/) site to edit Common Data Service associated with an environment. Changes applied here are performed in the context of an unmanaged Common Data Service Default solution. <!-- TODO: Add link to topic that describes this -->|
|Common Data Service Default solution explorer|There is another designer available from the [powerapps.com](https://make.powerapps.com/) site when editing Common Data Service. In the lower left-hand corner, the **Advanced** button will open the solution explorer to the Common Data Service Default solution. |
|Solution explorer for your solution |If you will distribute a solution you should create any new tables, columns, or relationships in the context of the unmanaged solution that you will use to develop your solution. <br /> More information: [Solution publisher](/power-platform/alm/solution-concepts-alm#solution-publisher)|
|From the form editor|When editing a model-driven app form for a table, you can click the **New Field** button in the **Field Explorer**. If you create a lookup field, you will create a new table relationship to support it.|

### Import a solution

A solution can contain table metadata and other customized components. Importing a managed or unmanaged solution into your Common Data Service tenant will include those tables or extend existing tables with the new table metadata they contain.

### From a data source using Power Query

You can create new tables and fill them with data using Power Query. More information: [Add data to a table in Common Data Service by using Power Query](../../maker/common-data-service/data-platform-cds-newentity-pq.md)

### Use metadata services

The web services exposed in Common Data Service include capabilities to create, read, write, and delete table metadata. These services are most frequently used to read the metadata because that data can inform your code at runtime about how the environment has been customized. More information: [Metadata services](metadata-services.md)

## Table metadata

The data model is defined as metadata that is stored within Common Data Service. This data about the schema is known as *Table Metadata*. 

- The [EntityMetadata Class](/dotnet/api/microsoft.xrm.sdk.metadata.entitymetadata) defines this with the Organization service. 
- The [EntityMetadata EntityType](/dynamics365/customer-engagement/web-api/entitymetadata) defines this for the Web API. 

The table metadata includes the following information:


|Data  |Description  |
|---------|---------|
|Table Properties|Each table has nearly 100 properties that describe how it is identified and what can be done with it.  More information: [Table Metadata](entity-metadata.md)|
|Columns|The table `Attributes` property is a collection of columns. Each columns has around 50 properties to describe how it is identified, the type of data it contains, how it is formatted, and what can be done with it. More information: [Column Metadata](entity-attribute-metadata.md)|
|Relationships|Three of the table properties are collections of relationships between tables. These collections contain different types of relationships: Many-To-Many, Many-To-One, and One-To-Many. More information: [Table Relationships Metadata](entity-relationship-metadata.md)|
|Privileges|One of the table properties is a collection of between 0 and 8 privileges that identity the kinds of data operations that can be performed on that table with a unique identifier associated with each one. These operations include: *Append*, *AppendTo*, *Assign*, *Create*, *Delete*, *Read*, *Share*, and *Write*.|
|Keys|By default, each table has a single GUID (globally unique identifier) attribute and the `Keys` property is an empty collection. You can add alternate keys to a table. More information: [Entity Keys](entity-metadata.md#entity-keys)|

> [!TIP]
> Developing an understanding of the table metadata in the system can help you understand how Common Data Service works. Many of the properties also control what tables in model-driven apps can do. The designers available to edit metadata cannot show all the details found in the metadata. You can install a model-driven app called the Metadata Browser which will allow you to view all the hidden tables and metadata properties that are found in the system. More information: [Browse the metadata for your organization](/powerapps/developer/common-data-service/browse-your-metadata)

## Private tables

Common Data Service contains some tables which are not intended for third-party developers to use. These tables are added by Microsoft to enable feature functionality. Private tables are indicated by the <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata>.<xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.IsPrivate> property. These tables are not included in the Web API [CSDL $metadata document](webapi/web-api-types-operations.md#csdl-metadata-document) for this reason. However, you will find them when querying table metadata.

> [!CAUTION]
> You should not use private tables in your solutions. By marking an table as private, Microsoft is explicitly indicating that we do not support other apps to use the table. Microsoft may remove the table or introduce breaking changes at any time. Use of these tables by anyone other than Microsoft is not supported.


### See also

[Common Data Service Developer Overview](overview.md)


