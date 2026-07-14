---
title: "Create many-to-many table relationships in Microsoft Dataverse overview | MicrosoftDocs"
description: "Learn how to create many-to-many table relationships"
ms.custom: ""
ms.date: 09/16/2024
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: overview
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
author: "Mattp123"
ms.assetid: 248cecfd-c9e8-430b-b4b0-860669866084
caps.latest.revision: 33
ms.subservice: dataverse-maker
ms.author: "matp"
search.audienceType: 
  - maker
---
# Create many-to-many table relationships overview

One-to-many (1:N) table relationships establish a hierarchy between rows. With many-to-many (N:N) relationships, there's no explicit hierarchy. There are no lookup columns or behaviors to configure. Rows created using many-to-many relationships can be considered peers and the relationship is reciprocal.  

One example of a many-to-many relationship is defined between two standard tables included with the Dynamics 365 for Sales app. The opportunity table has an N:N relationship with the competitor table. This relationship allows for multiple competitors to be added to the opportunity and multiple opportunities associated with the same competitor.
  
With many-to-many relationships, a relationship (or intersect) table stores the data that associates the tables. This table has a one-to-many table relationship with both of the related tables and only stores the necessary values to define the relationship. You can't add custom columns to a relationship table and it's never visible in the user interface.
  
Creating a many-to-many relationship requires choosing the two tables that you want to participate in the relationship. For model-driven apps you can decide how you want the respective lists to be available within the navigation for each table. These are the same options used for the primary table in 1:N table relationships.
  
Not all tables can be used with many-to-many relationships. If the table isn't available to be chosen in the designer, you can't create a new many-to-many relationship with this table. More information: [Developer documentation: table relationship eligibility](/power-apps/developer/data-platform/entity-relationship-eligibility)

> [!NOTE]
> You can also create new many-to-many (N:N) table relationship in your environment using the following:
> - Import a solution that contains the definition of the relationship. More information: [Import, update, and export solutions](import-update-export-solutions.md)
> - A developer can use [Metadata services](../../developer/data-platform/metadata-services.md) to write a program to create and update table relationships. More information: [Developer documentation: Table relationship definitions](../../developer/data-platform/entity-relationship-metadata.md)

## Next steps

[Create many-to-many table relationships](create-edit-nn-relationships-portal.md)<br />

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
