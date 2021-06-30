---
title: "Create many-to-many table relationships in Microsoft Dataverse overview | MicrosoftDocs"
description: "Learn how to create many-to-many table relationships"
ms.custom: ""
ms.date: 04/07/2020
ms.reviewer: ""
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "overview"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
author: "Mattp123"
ms.assetid: 248cecfd-c9e8-430b-b4b0-860669866084
caps.latest.revision: 33
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Create many-to-many table relationships overview

[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

One-to-many (1:N) table relationships establish a hierarchy between rows. With Many-to-many (N:N) relationships there is no explicit hierarchy. There are no lookup columns or behaviors to configure. Rows created using Many-to-many relationships can be considered peers and the relationship is reciprocal.  

One example of a many-to-many relationship is defined between two standard tables included with the Dynamics 365 Sales app. The opportunity table has an N:N relationship with the competitor table. This allows for multiple competitors to be added to the opportunity and multiple opportunities associated with the same competitor. 
  
With Many-to-many relationships a Relationship (or Intersect) table stores the data that associates the tables. This table has a One-to-many table relationship with both of the related tables and only stores the necessary values to define the relationship. You can’t add custom columns to a relationship table and it is never visible in the user interface. 
  
Creating a Many-to-many relationship requires choosing the two tables that you want to participate in the relationship. For model-driven apps you can decide how you want the respective lists to be available within the navigation for each table. These are the same options used for the primary table in 1:N table relationships. More information:  [Navigation Pane Item for Primary table](create-edit-1n-relationships-solution-explorer.md#navigation-pane-item-for-primary-table)
  
Not all tables can be used with Many-to-many relationships. If the table isn't available to be chosen in the designer, you can’t create a new Many-to-many relationship with this table. More information: [Developer documentation: table relationship eligibility](/dynamics365/customer-engagement/developer/entity-relationship-eligibility)

There are two designers you can use to create and edit 1:N (one-to-many) or N:1 (many-to-one) relationships:

|Designer| Description|
|--|--|
|[Power Apps portal](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc)|Provides an easy streamlined experience, but some special settings are not available.<br />More information: [Create Many-to-many table relationships in Microsoft Dataverse using Power Apps portal](create-edit-nn-relationships-portal.md)|
|Solution explorer|Not as easy, but provides for more flexibility for less common requirements.<br />More information: [Create N:N (many-to-many) table relationships in Dataverse using solution explorer](create-edit-nn-relationships-solution-explorer.md) |

> [!NOTE]
> You can also create new Many-to-many (N:N) table relationship in your environment using the following:
> - Import a solution that contains the definition of the relationship. More information: [Import, update, and export solutions](import-update-export-solutions.md)
> - A developer can use [Metadata services](../../developer/data-platform/metadata-services.md) to write a program to create and update table relationships. More information: [Developer documentation: Customize table relationship metadata](/dynamics365/customer-engagement/developer/customize-entity-relationship-metadata)

Information in this topic will help you choose which designer you can use. 

You should use the Power Apps portal to create and edit Many-to-many (N:N) table relationships unless you need to address any of the following requirements:

- Configure navigation pane options for model-driven apps.
- Hide the relationship from Advanced find in model-driven apps.

## See also

[Create and edit relationships between tables](create-edit-entity-relationships.md)<br />
[Create Many-to-many table relationships in Dataverse using Power Apps portal](create-edit-nn-relationships-portal.md)<br />
[Create N:N (many-to-many) table relationships in Dataverse using solution explorer](create-edit-nn-relationships-solution-explorer.md)<br />
[Developer documentation: Customize table relationship metadata](/dynamics365/customer-engagement/developer/customize-entity-relationship-metadata)<br />
[Developer documentation: table relationship eligibility](/dynamics365/customer-engagement/developer/table-relationship-eligibility)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]