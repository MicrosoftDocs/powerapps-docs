---
title: "Developers: Understand terminology in Microsoft Dataverse | Microsoft Docs"
description: "Developers: Understand terminology in Dataverse."
suite: powerapps
author: KumarVivek
ms.service: powerapps
ms.date: 03/04/2021
ms.author: kvivek
ms.reviewer: "pehecke"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Developers: Understand terminology in Microsoft Dataverse

[Dataverse](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-intro) is not just a database, but also web services that enable developers to [interact with data](work-with-data.md).

If you are familiar with the [ADO.NET Entity Framework](https://docs.microsoft.com/dotnet/framework/data/adonet/ef/overview), architects and developers of data-oriented applications have struggled with the need to achieve two different objectives.
- They must model the entities, relationships, and logic of the business problems they are solving.
- They must also work with the data services used to store and retrieve the data. 

The Entity Framework enables developers to work with data in the form of domain-specific objects and properties, such as customers and customer addresses, without having to concern themselves with the underlying database tables and columns where this data is stored. 

In Power Apps and Dataverse, while [*tables* and *columns*](https://docs.microsoft.com/powerapps/maker/data-platform/entity-overview) are used in the user interface and refer to the general idea of how data is stored in the Dataverse database, specific terminology (such as *entity* and *attributes*) is used to refer to the underlying data model and interfaces that developers work with depending on the protocol or technology used to interact with data. 

The data structures that developers work with are exposed as entities, and the term is baked in the names of things developers use. For example:

|To...|Using...|Developers will...|
|--|--|--|
|Create a Dataverse table|[Web API](/powerapps/developer/data-platform/webapi/overview)|POST an instance of the [EntityMetadata EntityType](https://docs.microsoft.com/dynamics365/customer-engagement/web-api/entitymetadata?view=dynamics-ce-odata-9) to the `/EntityDefinitions` resource|
|Create a Dataverse table|[.NET SDK](/powerapps/developer/data-platform/org-service/overview)|Create an instance of the [EntityMetadata Class](https://docs.microsoft.com/dotnet/api/microsoft.xrm.sdk.metadata.entitymetadata?view=dynamics-general-ce-9) and use the [CreateEntityRequest Class](https://docs.microsoft.com/dotnet/api/microsoft.xrm.sdk.messages.createentityrequest?view=dynamics-general-ce-9) to send this to the Organization service|
|Create a row or record in a Dataverse table|[Web API](/powerapps/developer/data-platform/webapi/overview)|POST data defined as an a specific EntityType. You can find a list of these EntityTypes here: [Web API EntityType Reference](https://docs.microsoft.com/dynamics365/customer-engagement/web-api/entitytypes?view=dynamics-ce-odata-9)|
|Create a row or record in a Dataverse table|[.NET SDK](/powerapps/developer/data-platform/org-service/overview)|Create an instance of the [Entity Class](https://docs.microsoft.com/dotnet/api/microsoft.xrm.sdk.entity?view=dynamics-general-ce-9) or a class that inherits from it (Account, Contact, etc.) and use the [CreateRequest Class](https://docs.microsoft.com/dotnet/api/microsoft.xrm.sdk.messages.createrequest?view=dynamics-general-ce-9) to send this to the Organization service. A developer can find the information they need to use the Entity class in the [entity reference](https://docs.microsoft.com/powerapps/developer/data-platform/reference/about-entity-reference).|


## Terminology use depending on protocol or technology

The terminology used in the developer documentation depends on the protocol or class library used by developers. 

- When working with the [Web API](/powerapps/developer/data-platform/webapi/overview), we use the terminology defined by the OData protocol. Data structures are defined as *EntityTypes*, which have properties and navigation properties. 

- When working with the [.NET SDK](/powerapps/developer/data-platform/org-service/overview), we use *Entity* because there is an Entity class. The Entity class has an [Attributes](https://docs.microsoft.com/dotnet/api/microsoft.xrm.sdk.entity.attributes?view=dynamics-general-ce-9) property that contains a collection of attributes that are defined by data in an  [AttributeMetadata Class](https://docs.microsoft.com/dotnet/api/microsoft.xrm.sdk.metadata.attributemetadata?view=dynamics-general-ce-9) and many other classes derived from it. 

We use the appropriate terminology to describe the SDK and Web API technology. The developer documentation will *at times* use different terminology than the Power Apps user interface. The table below will help guide you to some of the terminology differences between the developer documentation and rest of the Power Apps documentation. 

| Power Apps UI  | Dataverse SDK       | Dataverse Web API  |
|----------------|---------------------|--------------------|
| Table          | Entity              | EntityType         |
| Column         | Attribute           | Property           |
| Row            | Record              | Record             |
| Choices        | OptionSet/Picklist  | OptionSet          |
| Yes/No         | Boolean             | Boolean            | 
