---
title: "Entity overview in PowerApps | MicrosoftDocs"
description: "Learn how to create and edit entities using PowerApps portal"
ms.custom: ""
ms.date: 07/25/2018
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
ms.assetid: 
caps.latest.revision: 0
ms.author: "matp"
manager: "kvivek"
---

# Entity relationships overview

Entity relationships define the ways that entity records can be associated with records from other entities or the same entity. There are two types of entity relationships.
- **One-to-many relationships**. In a one-to-many entity relationship, many referencing (related) entity records can be associated with a single referenced (primary) entity record. The referenced entity record is sometimes referred to as the ”parent” and records of the referencing entity are referred to as ”children.”  A many-to-one relationship is just the child perspective of a one-to-many relationship.
- **Many-to-many relationships**. In a many-to-many entity relationship many entity records can be associated with many other entity records. Records related using a many-to-many relationship can be considered peers and the relationship is reciprocal. 

## See also
[Create a relationship between entities](data-platform-entity-lookup.md) <br/>
[Create Many-to-many entity relationships in Common Data Service for Apps using PowerApps portal](create-edit-nn-relationships-portal.md)