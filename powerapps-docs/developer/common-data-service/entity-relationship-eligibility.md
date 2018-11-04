---
title: "Entity relationship eligibility (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "The article lists the messages that you can use to determine whether entities can participate in entity relationships" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "mayadumesh" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Entity relationship eligibility

Before you create an entity relationship you should confirm whether the entity is eligible to participate in the relationship. The following table lists the messages that you can use to determine whether entities can participate in entity relationships.  
  
|Message|Web API Operation|SDK Assembly|  
|-------------|-----------------|----------------|  
|CanBeReferenced</br>Checks whether the specified entity can be the primary entity (one) in a one-to-many relationship.|<xref href="Microsoft.Dynamics.CRM.CanBeReferenced?text=CanBeReferenced Action" />|<xref:Microsoft.Xrm.Sdk.Messages.CanBeReferencedRequest>|  
|CanBeReferencing</br>Checks whether the specified entity can be the referencing entity (many) in a one-to-many relationship.|<xref href="Microsoft.Dynamics.CRM.CanBeReferencing?text=CanBeReferencing Action" />|<xref:Microsoft.Xrm.Sdk.Messages.CanBeReferencingRequest>|  
|CanManyToMany</br>Checks whether the entity can participate in a many-to-many relationship.|<xref href="Microsoft.Dynamics.CRM.CanManyToMany?text=CanManyToMany Action" />|<xref:Microsoft.Xrm.Sdk.Messages.CanManyToManyRequest>|  
|GetValidManyToMany</br>Returns the set of entities that can participate in a many-to-many relationship.|<xref href="Microsoft.Dynamics.CRM.GetValidManyToMany?text=GetValidManyToMany Function" />|<xref:Microsoft.Xrm.Sdk.Messages.GetValidManyToManyRequest>|  
|GetValidReferencedEntities</br>Returns the set of entities that are valid as the primary entity (one) from the specified entity in a one-to-many relationship.|<xref href="Microsoft.Dynamics.CRM.GetValidReferencedEntities?text=GetValidReferencedEntities Function" />|<xref:Microsoft.Xrm.Sdk.Messages.GetValidReferencedEntitiesRequest>|  
|GetValidReferencingEntities</br>Returns the set of entities that are valid as the related entity (many) to the specified entity in a one-to-many relationship.|<xref href="Microsoft.Dynamics.CRM.GetValidReferencingEntities?text=GetValidReferencingEntities Function" />|<xref:Microsoft.Xrm.Sdk.Messages.GetValidReferencingEntitiesRequest>|  
  
### See also  
 [Customize Entity Relationship Metadata](/dynamics365/customer-engagement/developer/customize-entity-relationship-metadata)   
 [Extend the Metadata Model for Dynamics 365](/dynamics365/customer-engagement/developer/org-service/use-organization-service-metadata)   
 [Entity Relationship Metadata](/dynamics365/customer-engagement/developer/customize-entity-relationship-metadata)   
 [Entity Relationship Messages](entity-relationship-metadata-messages.md)   
 [Entity Relationship Behavior](/dynamics365/customer-engagement/developer/entity-relationship-behavior)   
 [Create a 1:N Entity Relationship](/dynamics365/customer-engagement/developer/org-service/create-retrieve-entity-relationships#BKMK_Create1NEntityRelationship)   
 [Create an N:N Entity Relationship](/dynamics365/customer-engagement/developer/org-service/create-retrieve-entity-relationships#BKMK_CreateNNEntityRelationship)
