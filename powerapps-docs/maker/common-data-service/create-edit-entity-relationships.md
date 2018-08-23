---
title: "Entity relationships overview for Common Data Service for Apps | MicrosoftDocs"
ms.custom: ""
ms.date: 05/26/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "PowerApps"
ms.assetid: c765b6d9-4d87-4c2d-aae2-5b1c3b664a71
caps.latest.revision: 28
ms.author: "matp"
manager: "brycho"
search.audienceType: 
  - maker
search.app: 
  - "PowerApps"
  - D365CE
---
# Entity relationships overview

Entity relationships define how records can be related to each other in the database. At the simplest level, adding a lookup field to an entity creates a new 1:N (one-to-many) relationship between the two entities and lets you put that lookup field in a form. With the lookup field, users can associate multiple *child* records of that entity to a single *parent* entity record.  
  
Beyond simply defining how records can be related to other records, 1:N entity relationships also provide data to address the following questions:  
  
- When I delete a record should any records related to that record also be deleted?  
- When I assign a record, do I also need to assign all records related to that record to the new owner?  
- How can I streamline the data entry process when I create a new related record in the context of an existing record?  
- How should people viewing a record be able to view the associated records?  
  
 Entities can also participate in a N:N (many-to-many) relationship where any number of records for two entities can be associated with each other.  

<a name="BKMK_Connections"></a>

## Decide whether to use entity relationships or connections 
 
Entity relationships are metadata that make changes to the database. These relationships allow for queries to retrieve related data very efficiently. Use entity relationships to define formal relationships that define the entity or that most records can use. For example, an opportunity without a potential customer wouldn’t be very useful. The Opportunity entity also has a N:N relationship with the Competitor entity. This allows for multiple competitors to be added to the opportunity. You may want to capture this data and create a report that shows the competitors.  
  
There are other less formal kinds of relationships between records that are called *connections*. For example, it may be useful to know if two contacts are married, or perhaps they are friends outside of work, or perhaps a contact used to work for another account. Most businesses won’t generate reports using this kind of information or require that it is entered, so it’s probably not worthwhile to create entity relationships. More information: [Configure connection roles](configure-connection-roles.md)

  
<a name="BKMK_TypesOfRelationships"></a>
 
## Types of entity relationships

When you look at the solution explorer you might think that there are three types of entity relationships. Actually there are only two, as shown in the following table.  
  
|Relationship Type|Description|  
|-----------------------|-----------------|  
|**1:N (One-to-Many)**|An entity relationship where one entity record for the **Primary Entity** can be associated to many other **Related Entity** records because of a lookup field on the related entity.<br /><br /> When viewing a primary entity record you can see a list of the related entity records that are associated with it.|  
|**N:N (Many-to-Many)**|An entity relationship that depends on a special **Relationship Entity**, sometimes called an Intersect entity, so that many records of one entity can be related to many records of another entity.<br /><br /> When viewing records of either entity in a N:N relationship you can see a list of any records of the other entity that are related to it.|  
  
The **N:1 (many-to-one)** relationship type exists in the user interface because the designer shows you a view grouped by entities. 1:N relationships actually exist *between* entities and refer to each entity as either a **Primary Entity** or **Related Entity**. The related entity, sometimes called the *child* entity, has a lookup field that allows storing a reference to a record from the primary entity, sometimes called the *parent* entity. A N:1 relationship is just a 1:N relationship viewed from the related entity.  
 
## See also

[Entities and metadata overview](create-edit-metadata.md)<br />
[Create and edit 1:N (one-to-many) or N:1 (many-to-one) relationships](create-edit-1n-relationships.md)<br />
[Create Many-to-many (N:N) entity relationships](create-edit-nn-relationships.md)

