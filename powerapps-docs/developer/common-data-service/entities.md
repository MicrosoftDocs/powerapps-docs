---
title: Common Data Service for Apps entities | Microsoft Docs
description: Learn about the entities available in Common Data Service for Apps.
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
ms.date: 03/19/2018
ms.author: jdaly
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
<!-- 
Was Mike Carter
This topic was not migrated it was written for PowerApps 

Overlap with content in https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/introduction-entities

-->

# Common Data Service for Apps entities

Providing storage for data is the most important function of Common Data Service for Apps. Common Data Service includes a base set of entities that provide structure for data used by business applications. 

You can view the base set of entities in the [Common Data Service for Apps entity reference](reference/about-entity-reference.md).

## Modify entities

You can modify the entity metadata using several different methods.

### Use designers

There are several ways to edit entity metadata using designers.


|Designer  |Description  |
|---------|---------|
|powerapps.com|The easiest and most common approach to modify the schema is to use the [powerapps.com](https://web.powerapps.com/) site to edit Common Data Service associated with an environment. Changes applied here are performed in the context of an unmanaged Common Data Service Default solution. <!-- TODO: Add link to topic that describes this -->|
|Common Data Service Default solution explorer|There is another designer available from the [powerapps.com](https://web.powerapps.com/) site when editing Common Data Service. In the lower left-hand corner, the **Advanced** button will open the solution explorer to the Common Data Service Default solution. |
|Solution explorer for your solution |If you will distribute a solution you should create any new entities, attributes, or relationships in the context of the unmanaged solution that you will use to develop your solution. <br /> More information: [Create a solution publisher and solution](introduction-solutions.md#create-a-solution-publisher-and-solution)|
|From the form editor|When editing a model-driven app form for an entity, you can click the **New Field** button in the **Field Explorer**. If you create a lookup field, you will create a new entity relationship to support it.|

### Import a solution

A solution can contain entity metadata and other customized components. Importing a managed or unmanaged solution into your Common Data Service for Apps tenant will include those entities or extend existing entities with the new entity metadata they contain.

### From a data source using Power Query

You can create new entities and fill them with data using Power Query. More information: [Add data to an entity in Common Data Service by using Power Query](../../maker/common-data-service/data-platform-cds-newentity-pq.md)

### Use metadata services

The web services exposed in Common Data Service include capabilities to create, read, write, and delete entity metadata. These services are most frequently used to read the metadata because that data can inform your code at runtime about how the environment has been customized. More information: [Metadata services](metadata-services.md)

## Entity metadata

The data model is defined as metadata that is stored within Common Data Service. This data about the schema is known as *Entity Metadata*. 

- The [EntityMetadata Class](/dotnet/api/microsoft.xrm.sdk.metadata.entitymetadata) defines this with the Organization service. 
- The [EntityMetadata EntityType](/dynamics365/customer-engagement/web-api/entitymetadata) defines this for the Web API. 

The Entity metadata includes the following information:


|Data  |Description  |
|---------|---------|
|Entity Properties|Each entity has nearly 100 properties that describe how it is identified and what can be done with it.  More information: [Entity Metadata](entity-metadata.md)|
|Attributes|The entity `Attributes` property is a collection of attributes. Each attribute has around 50 properties to describe how it is identified, the type of data it contains, how it is formatted, and what can be done with it. More information: [Attribute Metadata](entity-attribute-metadata.md)|
|Relationships|Three of the entity properties are collections of relationships between entities. These collections contain different types of relationships: Many-To-Many, Many-To-One, and One-To-Many. More information: [Entity Relationships Metadata](entity-relationship-metadata.md)|
|Privileges|One of the entity properties is a collection of between 0 and 8 privileges that identity the kinds of data operations that can be performed on that entity with a unique identifier associated with each one. These operations include: *Append*, *AppendTo*, *Assign*, *Create*, *Delete*, *Read*, *Share*, and *Write*.|
|Keys|By default, each entity has a single GUID (globally unique identifier) attribute and the `Keys` property is an empty collection. You can add alternate keys to an entity. More information: [Entity Keys](entity-metadata.md#entity-keys)|

> [!TIP]
> Developing an understanding of the entity metadata in the system can help you understand how Common Data Service works. Many of the properties also control what entities in model-driven apps can do. The designers available to edit metadata cannot show all the details found in the metadata. You can install a model-driven app called the Metadata Browser which will allow you to view all the hidden entities and metadata properties that are found in the system. More information: [Browse the metadata for your organization](/dynamics365/customer-engagement/developer/browse-your-metadata)

### See also

[Common Data Service for Apps Developer Overview](overview.md)


