---
title: "Developers: Understand terminology in Microsoft Dataverse | Microsoft Docs"
description: "Developers: Understand terminology in Dataverse."
suite: powerapps
author: phecke
ms.author: pehecke
ms.reviewer: pehecke
ms.date: 08/28/2026
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
---

# Developers: Understand terminology in Microsoft Dataverse

[Dataverse](/powerapps/maker/data-platform/data-platform-intro) isn't just a database. It also provides web services that enable developers to [interact with data](work-with-data.md).

If you're familiar with the [ADO.NET Entity Framework](/dotnet/framework/data/adonet/ef/overview), you know that architects and developers of data-oriented applications often struggle to achieve two different objectives.

- They must model the entities, relationships, and logic of the business problems they're solving.
- They must also work with the data services that store and retrieve the data.

The Entity Framework enables developers to work with data as domain-specific objects and properties, such as customers and customer addresses. They don't need to worry about the underlying database tables and columns where this data is stored.

In Power Apps and Dataverse, you use [*tables* and *columns*](/powerapps/maker/data-platform/entity-overview) in the user interface. These terms refer to the general idea of how data is stored in the Dataverse database. However, specific terminology such as *entity* and *attributes* refers to the underlying data model and interfaces. Developers use this terminology depending on the protocol or technology used to interact with data.

The data structures that developers work with are exposed as entities. The term is baked into the names of things developers use. For example:

|To...|Using...|Developers will...|
|--|--|--|
|Create a Dataverse table|[Web API](/powerapps/developer/data-platform/webapi/overview)|POST an instance of the [EntityMetadata EntityType](/dynamics365/customer-engagement/web-api/entitymetadata) to the `/EntityDefinitions` resource|
|Create a Dataverse table|[.NET SDK](/powerapps/developer/data-platform/org-service/overview)|Create an instance of the [EntityMetadata Class](/dotnet/api/microsoft.xrm.sdk.metadata.entitymetadata) and use the [CreateEntityRequest Class](/dotnet/api/microsoft.xrm.sdk.messages.createentityrequest) when using the SDK for .NET.|
|Create a row or record in a Dataverse table|[Web API](/powerapps/developer/data-platform/webapi/overview)|POST data defined as a specific EntityType. You can find a list of these EntityTypes here: [Web API EntityType Reference](/dynamics365/customer-engagement/web-api/entitytypes)|
|Create a row or record in a Dataverse table|[.NET SDK](/powerapps/developer/data-platform/org-service/overview)|Create an instance of the [Entity Class](/dotnet/api/microsoft.xrm.sdk.entity) or a class that inherits from it (Account, Contact, etc.) and use the [CreateRequest Class](/dotnet/api/microsoft.xrm.sdk.messages.createrequest) when using the SDK for .NET. A developer can find the information they need to use the Entity class in the [entity reference](/powerapps/developer/data-platform/reference/about-entity-reference).|

## Terminology use depending on protocol or technology

The developer documentation uses terminology that depends on the protocol or class library that developers use.

- When you work with the [Web API](/powerapps/developer/data-platform/webapi/overview), you use the terminology defined by the OData protocol. Data structures called *EntityTypes* have properties and navigation properties.

- When you work with the [.NET SDK](/powerapps/developer/data-platform/org-service/overview), you use *Entity* because there's an Entity class. The Entity class has an [Attributes](/dotnet/api/microsoft.xrm.sdk.entity.attributes) property that contains a collection of attributes defined by data in an [AttributeMetadata Class](/dotnet/api/microsoft.xrm.sdk.metadata.attributemetadata) and many other classes derived from it.

Use the appropriate terminology to describe the SDK and Web API technology. The developer documentation sometimes uses different terminology than the Power Apps user interface. The following table helps guide you to some of the terminology differences between the developer documentation and the rest of the Power Apps documentation.

| Power Apps UI  | Dataverse SDK       | Dataverse Web API  |
|----------------|---------------------|--------------------|
| Table          | Entity              | EntityType         |
| Column         | Attribute           | Property           |
| Row            | Record              | Record             |
| Choices        | OptionSet/Picklist  | OptionSet          |
| Yes/No         | Boolean             | Boolean            |
