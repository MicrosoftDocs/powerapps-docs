---
title: "table relationships in Power Apps | MicrosoftDocs"
description: "Learn about table relationships in Power Apps"
ms.custom: intro-internal
ms.date: 07/25/2018
ms.reviewer: ""
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
author: "Mattp123"
ms.assetid: 
caps.latest.revision: 0
ms.subservice: dataverse-maker
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---

# Table relationships overview

[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

Table relationships define the ways that table rows can be associated with rows from other tables or the same table. There are two types of table relationships.
- **One-to-many relationships**. In a one-to-many table relationship, many referencing (related) table rows can be associated with a single referenced (primary) table row. The referenced table row is sometimes referred to as the ”parent” and rows of the referencing table are referred to as ”children.”  A many-to-one relationship is just the child perspective of a one-to-many relationship.
- **Many-to-many relationships**. In a many-to-many table relationship many table rows can be associated with many other table rows. Rows related using a many-to-many relationship can be considered peers and the relationship is reciprocal. 

## See also
[Create a relationship between tables](data-platform-entity-lookup.md) <br/>
[Create Many-to-many table relationships in Microsoft Dataverse using Power Apps portal](create-edit-nn-relationships-portal.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]