---
title: "Table relationship eligibility (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "The article lists the messages that you can use to determine whether tables can participate in relationships" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 03/11/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "mayadumesh" # GitHub ID
ms.subservice: dataverse-developer
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Table relationship eligibility

Before you create a relationship you should confirm whether the table is eligible to participate in the relationship. The following lists the messages that you can use to determine whether tables can participate in relationships.  

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]
  
|Message|Web API Operation|SDK Assembly|  
|-------------|-----------------|----------------|  
|CanBeReferenced</br>Checks whether the specified enttableity can be the primary table (one) in a one-to-many relationship.|<xref href="Microsoft.Dynamics.CRM.CanBeReferenced?text=CanBeReferenced Action" />|<xref:Microsoft.Xrm.Sdk.Messages.CanBeReferencedRequest>|  
|CanBeReferencing</br>Checks whether the specified table can be the referencing table (many) in a one-to-many relationship.|<xref href="Microsoft.Dynamics.CRM.CanBeReferencing?text=CanBeReferencing Action" />|<xref:Microsoft.Xrm.Sdk.Messages.CanBeReferencingRequest>|  
|CanManyToMany</br>Checks whether the table can participate in a many-to-many relationship.|<xref href="Microsoft.Dynamics.CRM.CanManyToMany?text=CanManyToMany Action" />|<xref:Microsoft.Xrm.Sdk.Messages.CanManyToManyRequest>|  
|GetValidManyToMany</br>Returns the set of tables that can participate in a many-to-many relationship.|<xref href="Microsoft.Dynamics.CRM.GetValidManyToMany?text=GetValidManyToMany Function" />|<xref:Microsoft.Xrm.Sdk.Messages.GetValidManyToManyRequest>|  
|GetValidReferencedEntities</br>Returns the set of tables that are valid as the primary table (one) from the specified table in a one-to-many relationship.|<xref href="Microsoft.Dynamics.CRM.GetValidReferencedEntities?text=GetValidReferencedEntities Function" />|<xref:Microsoft.Xrm.Sdk.Messages.GetValidReferencedEntitiesRequest>|  
|GetValidReferencingEntities</br>Returns the set of tables that are valid as the related table (many) to the specified table in a one-to-many relationship.|<xref href="Microsoft.Dynamics.CRM.GetValidReferencingEntities?text=GetValidReferencingEntities Function" />|<xref:Microsoft.Xrm.Sdk.Messages.GetValidReferencingEntitiesRequest>|  
  
### See also  
 [Customize table relationship definitions](/dynamics365/customer-engagement/developer/customize-entity-relationship-metadata)   
 [Extend the table definitions model for Dynamics 365](/dynamics365/customer-engagement/developer/org-service/use-organization-service-metadata)   
 [Table relationship definitions](/dynamics365/customer-engagement/developer/customize-entity-relationship-metadata)   
 [Table relationship messages](entity-relationship-metadata-messages.md)   
 [Table relationship behavior](/dynamics365/customer-engagement/developer/entity-relationship-behavior)   
 [Create a 1:N relationship](/dynamics365/customer-engagement/developer/org-service/create-retrieve-entity-relationships#BKMK_Create1NEntityRelationship)   
 [Create an N:N relationship](/dynamics365/customer-engagement/developer/org-service/create-retrieve-entity-relationships#BKMK_CreateNNEntityRelationship)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]