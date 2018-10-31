---
title: "Use the Web API with metadata (Common Data Service for Apps) | Microsoft Docs"
description: "The section provides guidance about how to use the Web API with the entity types included in Web API Metadata EntityType Reference."
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: a0edc029-c6db-48ac-9538-b0270fe94440
caps.latest.revision: 10
author: "brandonsimons" # GitHub ID
ms.author: "jdaly"
manager: "amyla"
---
# Use the Web API with metadata

You can perform any of the metadata operations with the Web API that you can perform using the organization service. This section provides guidance about how to use the Web API with the entity types included in <xref:Microsoft.Dynamics.CRM.MetadataEntityTypeIndex>.  
  
 There are four entity set paths exposed to perform operations with metadata entities as described in the following table.  
  
|Entity Set Path|Description|  
|---------------------|-----------------|  
|*[Organization URI]*/api/data/v9.0/EntityDefinitions|Contains <xref href="Microsoft.Dynamics.CRM.EntityMetadata?text=EntityMetadata EntityType" /> entities.|  
|*[Organization URI]*/api/data/v9.0/RelationshipDefinitions|Contains <xref href="Microsoft.Dynamics.CRM.ManyToManyRelationshipMetadata?text=ManyToManyRelationshipMetadata EntityType" /> and <xref href="Microsoft.Dynamics.CRM.OneToManyRelationshipMetadata?text=OneToManyRelationshipMetadata EntityType" /> as both inherit from <xref href="Microsoft.Dynamics.CRM.RelationshipMetadataBase?text=RelationshipMetadataBase EntityType" />.|  
|*[Organization URI]*/api/data/v9.0/GlobalOptionSetDefinitions|Contains globally defined <xref href="Microsoft.Dynamics.CRM.BooleanOptionSetMetadata?text=BooleanOptionSetMetadata EntityType" /> and <xref href="Microsoft.Dynamics.CRM.OptionSetMetadata?text=OptionSetMetadata EntityType" /> entities as both inherit from <xref href="Microsoft.Dynamics.CRM.OptionSetMetadata?text=OptionSetMetadata EntityType" />.|  
|*[Organization URI]*/api/data/v9.0/ManagedPropertyDefinitions|For internal use only|  
  
Each metadata entity type uses `MetadataId` as the unique identifier property, which it inherits from the <xref href="Microsoft.Dynamics.CRM.MetadataBase?text=MetadataBase EntityType" />. While all metadata entities have a `MetadataId`, you can’t query all of them directly. For example, you can query and perform operations on attributes only in the context of the `EntityMetadata` entity that contains them.  
  
These entities have some substantial differences from the entities that store business and application data, for example:  
  
- The properties for metadata entities use many of the complex and enum types defined in <xref:Microsoft.Dynamics.CRM.ComplexTypeIndex> and <xref:Microsoft.Dynamics.CRM.EnumTypeIndex> rather than the primitive data types used for properties in entities that inherit from <xref href="Microsoft.Dynamics.CRM.crmbaseentity?text=crmbaseentity EntityType" />.  
  
- Metadata entities follow a different naming convention and maintain the Pascal Case naming style used in the assemblies of the organization service.  
  
- Metadata entities make more extensive use of inheritance, which requires that you may need to perform casts to retrieve the data that you want.  
  
## In This Section 

[Query Metadata using the Web API](query-metadata-web-api.md)  
 You can use the Web API to query metadata in a manner similar to what can be done using the <xref:Microsoft.Xrm.Sdk.Messages.RetrieveMetadataChangesRequest> and the objects in the <xref:Microsoft.Xrm.Sdk.Metadata.Query> namespace using the organization service.  
  
[Retrieve metadata by name or MetadataId](retrieve-metadata-name-metadataid.md)  
 Your applications can adapt to configuration changes by querying the metadata. When you know one of the key properties of a metadata item, you can retrieve metadata definitions using the Web API.  
  
[Create and update model entities using the Web API](create-update-entity-definitions-using-web-api.md)  
 You can create and update entities and attributes using the Web API to achieve the same results you get with the organization service <xref:Microsoft.Xrm.Sdk.Messages.CreateEntityRequest>, <xref:Microsoft.Xrm.Sdk.Messages.UpdateEntityRequest>, <xref:Microsoft.Xrm.Sdk.Messages.CreateAttributeRequest>, and <xref:Microsoft.Xrm.Sdk.Messages.UpdateAttributeRequest>.  
  
[Create and update entity relationships using the Web API](create-update-entity-relationships-using-web-api.md)  
 You can check whether entities are eligible to participate in a relationship with other entities and then create or update those relationships using the Web API.  
  
### See also

<!-- TODO:
[Metadata and data models](../metadata-data-models.md)<br />
[Browse the Metadata for Your Organization](../browse-your-metadata.md)<br />
[Use the Organization service with Common Data Service for Apps metadata](../org-service/use-organization-service-metadata.md)<br />
[Use the Common Data Service for Apps Web API](overview.md) -->
