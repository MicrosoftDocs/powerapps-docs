---
title: Work with Dataverse tables using code | Microsoft Docs
description: Learn about the tabled available in Microsoft Dataverse.
services: ''
suite: powerapps
documentationcenter: na
author: "mayadumesh" # GitHub ID
manager: kvivek
editor: ''
tags: ''
ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 10/26/2020
ms.author: jdaly
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Work with Dataverse tables using code

Providing storage for data is the most important function of Dataverse. Dataverse includes a base set of tables that provide structure for data used by business applications. 

You can view the base set of tables in the [Dataverse table/entity reference](reference/about-entity-reference.md).

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

## Modify tables

You can modify the entity metadata using several different methods.

### Use designers

There are several ways to edit entity metadata using designers.


|Designer  |Description  |
|---------|---------|
|powerapps.com|The easiest and most common approach to modify the schema is to use the [powerapps.com](https://make.powerapps.com/) site to edit Dataverse associated with an environment. Changes applied here are performed in the context of an unmanaged Common Data Service Default Solution. |
|Common Data Service Default Solution explorer|There is another designer available from the [powerapps.com](https://make.powerapps.com/) site when editing Dataverse. In the lower left-hand corner, the **Advanced** button will open the solution explorer to the Common Data Service Default Solution. |
|Solution explorer for your solution |If you will distribute a solution you should create any new tables, attributes, or relationships in the context of the unmanaged solution that you will use to develop your solution. <br /> More information: [Solution publisher](/power-platform/alm/solution-concepts-alm#solution-publisher)|
|From the form editor|When editing a model-driven app form for an entity, you can click the **New Field** button in the **Field Explorer**. If you create a lookup field, you will create a new relationship to support it.|

### Import a solution

A solution can contain table and other customized components. Importing a managed or unmanaged solution into your Dataverse tenant will include those tables or extend existing tables with the new table they contain.

### From a data source using Power Query

You can create new tables and fill them with data using Power Query. More information: [Add data to a table in Dataverse by using Power Query](../../maker/data-platform/add-data-power-query.md)

### Use metadata services

The web services exposed in Dataverse include capabilities to create, read, write, and delete entity metadata. These services are most frequently used to read the metadata because that data can inform your code at runtime about how the environment has been customized. More information: [Metadata services](metadata-services.md)

## Metadata

The data model is defined as metadata that is stored within Dataverse. This data about the schema is known as *Entity Metadata*. 

- The [EntityMetadata Class](/dotnet/api/microsoft.xrm.sdk.metadata.entitymetadata) defines this with the Organization service. 
- The [EntityMetadata EntityType](/dynamics365/customer-engagement/web-api/entitymetadata) defines this for the Web API. 

The metadata includes the following information:


|Data  |Description  |
|---------|---------|
|Properties|Each entity has nearly 100 properties that describe how it is identified and what can be done with it.  More information: [Entity Metadata](entity-metadata.md)|
|Attributes|The entity `Attributes` property is a collection of attributes. Each attribute has around 50 properties to describe how it is identified, the type of data it contains, how it is formatted, and what can be done with it. More information: [Attribute Metadata](entity-attribute-metadata.md)|
|Relationships|Three of the entity properties are collections of relationships between tables. These collections contain different types of relationships: Many-To-Many, Many-To-One, and One-To-Many. More information: [Entity Relationships Metadata](entity-relationship-metadata.md)|
|Privileges|One of the entity properties is a collection of between 0 and 8 privileges that identity the kinds of data operations that can be performed on that entity with a unique identifier associated with each one. These operations include: *Append*, *AppendTo*, *Assign*, *Create*, *Delete*, *Read*, *Share*, and *Write*.|
|Keys|By default, each entity has a single GUID (globally unique identifier) attribute and the `Keys` property is an empty collection. You can add alternate keys to an entity. More information: [Entity Keys](entity-metadata.md#entity-keys)|

> [!TIP]
> Developing an understanding of the entity metadata in the system can help you understand how Dataverse works. Many of the properties also control what tables in model-driven apps can do. The designers available to edit metadata cannot show all the details found in the metadata. You can install a model-driven app called the Metadata Browser which will allow you to view all the hidden tables and metadata properties that are found in the system. More information: [Browse the metadata for your organization](/dynamics365/customer-engagement/developer/browse-your-metadata)

## Private tables

Dataverse contains some tables which are not intended for 3rd party developers to use. These tables are added by Microsoft to enable feature functionality. Private tables are indicated by the <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata>.<xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.IsPrivate> property. These tables are not included in the Web API [CSDL $metadata document](webapi/web-api-types-operations.md#csdl-metadata-document) for this reason. However you will find them when querying entity metadata.

> [!CAUTION]
> You should not use private tables in your solutions. By marking an entity as private, Microsoft is explicitly indicating that we do not support other apps to use the entity. Microsoft may remove the entity or introduce breaking changes at any time. Use of these tables by anyone other than Microsoft is not supported.


### See also

[Dataverse Developer Overview](overview.md)




[!INCLUDE[footer-include](../../includes/footer-banner.md)]