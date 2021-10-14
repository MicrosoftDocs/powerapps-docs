---
title: "Use the Web API with table definitions (Microsoft Dataverse) | Microsoft Docs"
description: "The section provides guidance about how to use the Web API with the entity types included in Web API Metadata EntityType Reference, enabling you to read, create, and update table and column definitions."
ms.custom: ""
ms.date: 04/21/2021
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
author: "JimDaly" # GitHub ID
ms.author: pehecke
manager: "shujoshi"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Use the Web API with table definitions

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

You can perform any of the table and column definition (metadata) operations with the Web API that you can perform using the Organization service. This section provides guidance about how to use the Web API with the entity types included in <xref:Microsoft.Dynamics.CRM.MetadataEntityTypeIndex>.  

 There are four entity set paths exposed to perform operations with definition entities as described in the following table.  
  
|Entity Set Path|Description|  
|---------------------|-----------------|  
|*[Organization URI]*/api/data/v9.0/EntityDefinitions|Contains a collection of <xref:Microsoft.Dynamics.CRM.EntityMetadata?text=EntityMetadata EntityType/>.|  
|*[Organization URI]*/api/data/v9.0/RelationshipDefinitions|Contains <xref:Microsoft.Dynamics.CRM.ManyToManyRelationshipMetadata?text=ManyToManyRelationshipMetadata EntityType/> and <xref:Microsoft.Dynamics.CRM.OneToManyRelationshipMetadata?text=OneToManyRelationshipMetadata EntityType/> as both inherit from <xref:Microsoft.Dynamics.CRM.RelationshipMetadataBase?text=RelationshipMetadataBase EntityType/>.|  
|*[Organization URI]*/api/data/v9.0/GlobalOptionSetDefinitions|Contains a collection of globally defined <xref:Microsoft.Dynamics.CRM.BooleanOptionSetMetadata?text=BooleanOptionSetMetadata EntityType/> and <xref:Microsoft.Dynamics.CRM.OptionSetMetadata?text=OptionSetMetadata EntityType/> as both inherit from <xref:Microsoft.Dynamics.CRM.OptionSetMetadata?text=OptionSetMetadata EntityType/>.|  
|*[Organization URI]*/api/data/v9.0/ManagedPropertyDefinitions|  For internal use only|  
  
Each definition entity type uses `MetadataId` as the unique identifier property, which it inherits from the <xref:Microsoft.Dynamics.CRM.MetadataBase?text=MetadataBase EntityType/>. While all definition entities have a `MetadataId`, you can’t query all of them directly. For example, you can query and perform operations on attributes (table columns) only in the context of the `EntityMetadata` entity that contains them.  
  
These definition entities have some substantial differences from the tables that store business and application data, for example:  
  
- The properties for definition entities use many of the complex and enum types defined in <xref:Microsoft.Dynamics.CRM.ComplexTypeIndex> and <xref:Microsoft.Dynamics.CRM.EnumTypeIndex> rather than the primitive data types used for properties in entities that inherit from <xref:Microsoft.Dynamics.CRM.crmbaseentity?text=crmbaseentity EntityType/>.  
  
- Definition entities follow a different naming convention and maintain the Pascal Case naming style used in the assemblies of the Organization service.  
  
- Definition entities make more extensive use of inheritance, which requires that you may need to perform casts to retrieve the data that you want.  
  
## In This Section

[Query table definitions using the Web API](query-metadata-web-api.md)<br />
You can use the Web API to query table or column definitions using a RESTful query style.  

[Retrieve table definitions by name or MetadataId](retrieve-metadata-name-metadataid.md)<br />
Your applications can adapt to configuration changes by querying the table and column definitions. When you know one of the key properties of a definition item, you can retrieve definitions using the Web API.  

[Create and update table definitions using the Web API](create-update-entity-definitions-using-web-api.md)<br />
You can create and update tables and columns using the Web API to achieve the same results you get with the organization service <xref:Microsoft.Xrm.Sdk.Messages.CreateEntityRequest>, <xref:Microsoft.Xrm.Sdk.Messages.UpdateEntityRequest>, <xref:Microsoft.Xrm.Sdk.Messages.CreateAttributeRequest>, and <xref:Microsoft.Xrm.Sdk.Messages.UpdateAttributeRequest>.  

[Create and update table relationships using the Web API](create-update-entity-relationships-using-web-api.md)<br />
You can check whether tables are eligible to participate in a relationship with other tables and then create or update those relationships using the Web API.  

### See also

[Browse the table definitions for your environment](../browse-your-metadata.md)<br />
[Use the Microsoft Dataverse Web API](overview.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]