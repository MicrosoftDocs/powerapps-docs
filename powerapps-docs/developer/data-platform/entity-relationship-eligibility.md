---
title: "Table relationship eligibility (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "The article lists the messages that you can use to determine whether tables can participate in relationships" # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 07/20/2023
ms.reviewer: pehecke
ms.topic: article
author: mayadumesh # GitHub ID
ms.subservice: dataverse-developer
ms.author: mayadu # MSFT alias of Microsoft employees only
search.audienceType: 
  - developer
---
# Table relationship eligibility

Before you create a relationship you should confirm whether the table is eligible to participate in the relationship. The following lists the messages that you can use to determine whether tables can participate in relationships.  

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]
  
|Message<br />Web API operation<br />SDK Request class|Description|
|-------------|-----------------|
|`CanBeReferenced`</br>[CanBeReferenced Action](xref:Microsoft.Dynamics.CRM.CanBeReferenced)<br /><xref:Microsoft.Xrm.Sdk.Messages.CanBeReferencedRequest>|Checks whether the specified table can be the primary table (one) in a one-to-many relationship.|
|`CanBeReferencing`</br>[CanBeReferencing Action](xref:Microsoft.Dynamics.CRM.CanBeReferencing)<br /><xref:Microsoft.Xrm.Sdk.Messages.CanBeReferencingRequest>|Checks whether the specified table can be the referencing table (many) in a one-to-many relationship.|
|`CanManyToMany`</br>[CanManyToMany Action](xref:Microsoft.Dynamics.CRM.CanManyToMany)<br /><xref:Microsoft.Xrm.Sdk.Messages.CanManyToManyRequest>|Checks whether the table can participate in a many-to-many relationship.|
|`GetValidManyToMany`</br>[GetValidManyToMany Function](xref:Microsoft.Dynamics.CRM.GetValidManyToMany)<br /><xref:Microsoft.Xrm.Sdk.Messages.GetValidManyToManyRequest>|Returns the set of tables that can participate in a many-to-many relationship.|
|`GetValidReferencedEntities`</br>[GetValidReferencedEntities Function](xref:Microsoft.Dynamics.CRM.GetValidReferencedEntities)<br /><xref:Microsoft.Xrm.Sdk.Messages.GetValidReferencedEntitiesRequest>|Returns the set of tables that are valid as the primary table (one) from the specified table in a one-to-many relationship.|
|`GetValidReferencingEntities`</br>[GetValidReferencingEntities Function](xref:Microsoft.Dynamics.CRM.GetValidReferencingEntities)<br /><xref:Microsoft.Xrm.Sdk.Messages.GetValidReferencingEntitiesRequest>|Returns the set of tables that are valid as the related table (many) to the specified table in a one-to-many relationship.|
  
### See also

[Table relationship definitions](entity-relationship-metadata.md)   
[Work with table definitions using the Organization service](org-service/work-with-metadata.md)   
[Create and retrieve table row relationships](org-service/metadata-relationshipmetadata.md)   
[Table relationship messages](entity-relationship-metadata-messages.md)   
[Configure table relationship cascading behavior](configure-entity-relationship-cascading-behavior.md)   


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
