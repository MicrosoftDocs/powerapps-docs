---
title: "Table relationship eligibility (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "The article lists the messages that you can use to determine whether tables can participate in relationships" # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 03/11/2021
ms.reviewer: pehecke
ms.topic: "article"
author: mayadumesh # GitHub ID
ms.subservice: dataverse-developer
ms.author: mayadu # MSFT alias of Microsoft employees only
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
|CanBeReferenced</br>Checks whether the specified table can be the primary table (one) in a one-to-many relationship.|<xref:Microsoft.Dynamics.CRM.CanBeReferenced?text=CanBeReferenced Action>|<xref:Microsoft.Xrm.Sdk.Messages.CanBeReferencedRequest>|  
|CanBeReferencing</br>Checks whether the specified table can be the referencing table (many) in a one-to-many relationship.|<xref:Microsoft.Dynamics.CRM.CanBeReferencing?text=CanBeReferencing Action>|<xref:Microsoft.Xrm.Sdk.Messages.CanBeReferencingRequest>|  
|CanManyToMany</br>Checks whether the table can participate in a many-to-many relationship.|<xref:Microsoft.Dynamics.CRM.CanManyToMany?text=CanManyToMany Action>|<xref:Microsoft.Xrm.Sdk.Messages.CanManyToManyRequest>|  
|GetValidManyToMany</br>Returns the set of tables that can participate in a many-to-many relationship.|<xref:Microsoft.Dynamics.CRM.GetValidManyToMany?text=GetValidManyToMany Function>|<xref:Microsoft.Xrm.Sdk.Messages.GetValidManyToManyRequest>|  
|GetValidReferencedEntities</br>Returns the set of tables that are valid as the primary table (one) from the specified table in a one-to-many relationship.|<xref:Microsoft.Dynamics.CRM.GetValidReferencedEntities?text=GetValidReferencedEntities Function>|<xref:Microsoft.Xrm.Sdk.Messages.GetValidReferencedEntitiesRequest>|  
|GetValidReferencingEntities</br>Returns the set of tables that are valid as the related table (many) to the specified table in a one-to-many relationship.|<xref:Microsoft.Dynamics.CRM.GetValidReferencingEntities?text=GetValidReferencingEntities Function>|<xref:Microsoft.Xrm.Sdk.Messages.GetValidReferencingEntitiesRequest>|  
  
### See also

[Table relationship definitions](entity-relationship-metadata.md)<br />
[Work with table definitions using the Organization service](org-service/work-with-metadata.md)<br />
[Create and retrieve table row relationships](org-service/metadata-relationshipmetadata.md)<br />
[Table relationship messages](entity-relationship-metadata-messages.md)<br />
[Configure table relationship cascading behavior](configure-entity-relationship-cascading-behavior.md)<br />


[!INCLUDE[footer-include](../../includes/footer-banner.md)]