---
title: "Use the Web API with table definitions (Microsoft Dataverse) | Microsoft Docs"
description: "The section provides guidance about how to use the Web API with the entity types included in Web API Metadata EntityType Reference, enabling you to read, create, and update table and column definitions."
ms.date: 09/02/2022
author: NHelgren
ms.author: nhelgren
ms.reviewer: jdaly
search.audienceType: 
  - developer
contributors: 
  - JimDaly
---
# Use the Web API with table definitions

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

You can perform any of the table and column definition (metadata) operations with the Web API that you can perform using the Organization service. This section provides guidance about how to use the Web API with the entity types included in <xref:Microsoft.Dynamics.CRM.MetadataEntityTypeIndex>.  

 There are four entity set paths exposed to perform operations with definition entities as described in the following table.  
  
|Entity Set Path|Description|  
|---------------------|-----------------|  
|*[Organization URI]*/api/data/v9.2/EntityDefinitions|Contains a collection of <xref:Microsoft.Dynamics.CRM.EntityMetadata?text=EntityMetadata EntityType>.|  
|*[Organization URI]*/api/data/v9.2/RelationshipDefinitions|Contains <xref:Microsoft.Dynamics.CRM.ManyToManyRelationshipMetadata?text=ManyToManyRelationshipMetadata EntityType> and <xref:Microsoft.Dynamics.CRM.OneToManyRelationshipMetadata?text=OneToManyRelationshipMetadata EntityType> as both inherit from <xref:Microsoft.Dynamics.CRM.RelationshipMetadataBase?text=RelationshipMetadataBase EntityType>.|  
|*[Organization URI]*/api/data/v9.2/GlobalOptionSetDefinitions|Contains a collection of globally defined <xref:Microsoft.Dynamics.CRM.BooleanOptionSetMetadata?text=BooleanOptionSetMetadata EntityType> and <xref:Microsoft.Dynamics.CRM.OptionSetMetadata?text=OptionSetMetadata EntityType> as both inherit from <xref:Microsoft.Dynamics.CRM.OptionSetMetadata?text=OptionSetMetadata EntityType>.|  
|*[Organization URI]*/api/data/v9.2/ManagedPropertyDefinitions|  For internal use only|  
  
Each definition entity type uses `MetadataId` as the unique identifier property, which it inherits from the <xref:Microsoft.Dynamics.CRM.MetadataBase?text=MetadataBase EntityType>. While all definition entities have a `MetadataId`, you can't query all of them directly. For example, you can query and perform operations on attributes (table columns) only in the context of the `EntityMetadata` entity that contains them.  
  
These definition entities have some substantial differences from the tables that store business and application data, for example:  
  
- The properties for definition entities use many of the complex and enum types defined in <xref:Microsoft.Dynamics.CRM.ComplexTypeIndex> and <xref:Microsoft.Dynamics.CRM.EnumTypeIndex> rather than the primitive data types used for properties in entities that inherit from <xref:Microsoft.Dynamics.CRM.crmbaseentity?text=crmbaseentity EntityType>.  
  
- Definition entities follow a different naming convention and maintain the Pascal Case naming style used in the assemblies of the Organization service.  
  
- Definition entities make more extensive use of inheritance, which requires that you may need to perform casts to retrieve the data that you want.  
  
## In This Section

[Query table definitions using the Web API](query-metadata-web-api.md)  
You can use the Web API to query table or column definitions using a RESTful query style.  

[Retrieve table definitions by name or MetadataId](retrieve-metadata-name-metadataid.md)  
Your applications can adapt to configuration changes by querying the table and column definitions. When you know one of the key properties of a definition item, you can retrieve definitions using the Web API.  

[Create and update table definitions using the Web API](create-update-entity-definitions-using-web-api.md)  
You can create and update tables using the Web API to achieve the same results you get with the organization service <xref:Microsoft.Xrm.Sdk.Messages.CreateEntityRequest> and <xref:Microsoft.Xrm.Sdk.Messages.UpdateEntityRequest>.  

[Create and update column definitions using the Web API](create-update-column-definitions-using-web-api.md)  
You can create and update columns using the Web API to achieve the same results you get with the organization service <xref:Microsoft.Xrm.Sdk.Messages.CreateAttributeRequest>, and <xref:Microsoft.Xrm.Sdk.Messages.UpdateAttributeRequest>.  

[Create and update table relationships using the Web API](create-update-entity-relationships-using-web-api.md)  
You can check whether tables are eligible to participate in a relationship with other tables and then create or update those relationships using the Web API.

[Multi-table lookups](multitable-lookup.md)  
Multi-table lookup type columns allow a user to use a specific table that has multiple one-to-many (1:N) relationships to other tables in the environment. A single lookup type column can refer to multiple other tables. A lookup value submitted to the multi-table type column will be matched to a record in any of the related tables. Multi-table lookups can be created with both local tables and virtual tables as referenced tables.

[Create and update choices (option sets) using the Web API](create-update-optionsets.md)  
Explains how to work with global and local choice columns. How to retrieve option values, add, update, delete, and re-order options.

### See also

[Browse the table definitions for your environment](../browse-your-metadata.md)<br />
[Use the Microsoft Dataverse Web API](overview.md)
[Web API Metadata Operations Sample](web-api-metadata-operations-sample.md)  
[Web API Metadata Operations Sample (C#)](samples/webapiservice-metadata-operations.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
