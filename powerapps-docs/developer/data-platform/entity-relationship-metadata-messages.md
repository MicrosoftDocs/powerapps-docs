---
title: "Table relationship definitions messages (Microsoft Dataverse) | Microsoft Docs" 
description: "The article describes the messages that you can use to create, retrieve, update, and delete relationships using Web API and SDK for .NET." 
ms.custom: ""
ms.date: 03/11/2021
ms.reviewer: "pehecke"

ms.topic: "article"
author: "mayadumesh" 
ms.subservice: dataverse-developer
ms.author: "jdaly"
search.audienceType: 
  - developer
---
# Table relationship definitions messages

Table relationships define how tables are related to each other. This includes information about how relationships are represented in the application. Also, when actions are performed on a record, the relationship indicates what actions to perform on related records.  

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]
  
The following table lists the messages that you can use to create, retrieve, update, and delete relationships.  
  
|Web API|SDK for .NET|Description|  
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
