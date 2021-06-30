---
title: "Table relationship definitions messages (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "The article describes the messages that you can use to create, retrieve, update, and delete relationships using Web API and Organization service." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 03/11/2021
ms.reviewer: "pehecke"
ms.service: powerapps
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
# Table relationship definitions messages

Table relationships define how tables are related to each other. This includes information about how relationships are represented in the application. Also, when actions are performed on a record, the relationship indicates what actions to perform on related records.  

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]
  
The following table lists the messages that you can use to create, retrieve, update, and delete relationships.  
  
|Web API|Organization Service|Description|  
|-------------|-------------|-----------------|  
|`POST` request on `RelationshipDefinitions` table. <br/>More information: [Create a many-to-many relationship](webapi/create-update-entity-relationships-using-web-api.md#create-a-many-to-many-relationship) |<xref:Microsoft.Xrm.Sdk.Messages.CreateManyToManyRequest>|Creates a many-to-many relationship between two tables.|  
|`POST` request on `RelationshipDefinitions` table. <br/>More information: [Create a one-to-many relationship](webapi/create-update-entity-relationships-using-web-api.md#create-a-one-to-many-relationship)|<xref:Microsoft.Xrm.Sdk.Messages.CreateOneToManyRequest>|Creates a one-to-many relationship between two tables.|  
|`DELETE` request on `RelationshipDefinitions` table.<br/>More information: [Delete relationships](webapi/create-update-entity-relationships-using-web-api.md#delete-relationships)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRelationshipRequest>|Deletes a relationship.|  
|`GET` request on `RelationshipDefinitions` table.|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRelationshipRequest>|Retrieves a relationship.|  
|`PUT` request on `RelationshipDefinitions` table.<br/>More information: [Update relationships](webapi/create-update-entity-relationships-using-web-api.md#update-relationships)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRelationshipRequest>|Updates a relationship.|  
  
### See also  

 [Relationship eligibility](entity-relationship-eligibility.md)   
 [Configure relationship cascading behavior](configure-entity-relationship-cascading-behavior.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]