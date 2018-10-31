---
title: "Entity relationship metadata messages (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "The article describes the messages that you can use to create, retrieve, update, and delete entity relationships using Web API and Organization service." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "mayadumesh" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Entity relationship metadata messages

Entity relationships define how entities are related to each other. This includes information about how relationships are represented in the application. Also, when actions are performed on a record, the relationship indicates what actions to perform on related records.  
  
The following table lists the messages that you can use to create, retrieve, update, and delete entity relationships.  
  
|Web API|Organization Service|Description|  
|-------------|-------------|-----------------|  
|`POST` request on `RelationshipDefinitions` entity. <br/>More information: [Create a many-to-many relationship](webapi/create-update-entity-relationships-using-web-api.md#create-a-many-to-many-relationship) |<xref:Microsoft.Xrm.Sdk.Messages.CreateManyToManyRequest>|Creates a many-to-many relationship between two entities.|  
|`POST` request on `RelationshipDefinitions` entity. <br/>More information: [Create a one-to-many relationship](webapi/create-update-entity-relationships-using-web-api.md#create-a-one-to-many-relationship)|<xref:Microsoft.Xrm.Sdk.Messages.CreateOneToManyRequest>|Creates a one-to-many relationship between two entities.|  
|`DELETE` request on `RelationshipDefinitions` entity.<br/>More information: [Delete relationships](webapi/create-update-entity-relationships-using-web-api.md#delete-relationships)|<xref:Microsoft.Xrm.Sdk.Messages.DeleteRelationshipRequest>|Deletes an entity relationship.|  
|`GET` request on `RelationshipDefinitions` entity.|<xref:Microsoft.Xrm.Sdk.Messages.RetrieveRelationshipRequest>|Retrieves an entity relationship.|  
|`PUT` request on `RelationshipDefinitions` entity.<br/>More information: [Update relationships](webapi/create-update-entity-relationships-using-web-api.md#update-relationships)|<xref:Microsoft.Xrm.Sdk.Messages.UpdateRelationshipRequest>|Updates an entity relationship.|  
  
### See also  

 [Entity Relationship Eligibility](entity-relationship-eligibility.md)   
 [Configure entity relationship cascading behavior](configure-entity-relationship-cascading-behavior.md)