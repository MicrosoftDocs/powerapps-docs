---
title: "Create many-to-many entity relationships in Common Data Service for Apps overview | MicrosoftDocs"
description: "Learn how to create many-to-many entity relationships"
ms.custom: ""
ms.date: 05/29/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
author: "Mattp123"
ms.assetid: 248cecfd-c9e8-430b-b4b0-860669866084
caps.latest.revision: 33
ms.author: "matp"
manager: "kvivek"
---
# Create many-to-many entity relationships overview

One-to-many (1:N) entity relationships establish a hierarchy between records. With Many-to-many (N:N) relationships there is no explicit hierarchy. There are no lookup fields or behaviors to configure. Records created using Many-to-many relationships can be considered peers and the relationship is reciprocal.  
  
With Many-to-many relationships a Relationship (or Intersect) entity stores the data that assoicates the entities. This entity has a One-to-many entity relationship with both of the related entities and only stores the necessary values to define the relationship. You can’t add custom fields to a relationship entity and it is never visible in the user interface. 
  
Creating a Many-to-many relationship requires choosing the two entities that you want to participate in the relationship. For model-driven apps you can decide how you want the respective lists to be available within the navigation for each entity. These are the same options used for the primary entity in 1:N entity relationships. More information:  [Navigation Pane Item for Primary Entity](create-edit-1n-relationships-solution-explorer.md#navigation-pane-item-for-primary-entity)
  
Not all entities can be used with Many-to-many relationships. If the entity isn't available to be chosen in the designer, you can’t create a new Many-to-many relationship with this entity. More information: [Developer documentation: Entity relationship eligibility](https://docs.microsoft.com/dynamics365/customer-engagement/developer/entity-relationship-eligibility)

There are two designers you can use to create and edit 1:N (one-to-many) or N:1 (many-to-one) relationships:

|Designer| Description|
|--|--|
|[PowerApps portal](https://web.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc)|Provides an easy streamlined experience, but some special settings are not available.<br />More information: [Create Many-to-many entity relationships in Common Data Service for Apps using PowerApps portal](create-edit-nn-relationships-portal.md)|
|Solution explorer|Not as easy, but provides for more flexibility for less common requirements.<br />More information: [Create N:N (many-to-many) entity relationships in Common Data Service for Apps using solution explorer](create-edit-nn-relationships-solution-explorer.md) |

> [!NOTE]
> You can also create new Many-to-many (N:N) entity relationship in your environment using the following:
> - Import a solution that contains the definition of the relationship. More information: [Import, update, and export solutions](import-update-export-solutions.md)
> - A developer can use [Metadata services](../../developer/common-data-service/use-web-services.md#metadata-services) to write a program to create and update entity relationships. More information: [Developer documentation: Customize entity relationship metadata](https://docs.microsoft.com/dynamics365/customer-engagement/developer/customize-entity-relationship-metadata)

Information in this topic will help you choose which designer you can use. 

You should use the PowerApps portal to create and edit Many-to-many (N:N) entity relationships unless you need to address any of the following requirements:

- Configure navigation pane options for model-driven apps.
- Hide the relationship from Advanced find in model-driven apps.

## See also

[Create and edit relationships between entities](create-edit-entity-relationships.md)<br />
[Create Many-to-many entity relationships in Common Data Service for Apps using PowerApps portal](create-edit-nn-relationships-portal.md)<br />
[Create N:N (many-to-many) entity relationships in Common Data Service for Apps using solution explorer](create-edit-nn-relationships-solution-explorer.md)<br />
[Developer documentation: Customize entity relationship metadata](https://docs.microsoft.com/dynamics365/customer-engagement/developer/customize-entity-relationship-metadata)<br />
[Developer documentation: Entity relationship eligibility](https://docs.microsoft.com/dynamics365/customer-engagement/developer/entity-relationship-eligibility)