---
title: "Customize entity and attribute mappings in PowerApps (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn about mapping attributes between entities that have an entity relationship in PowerApps. This lets you set default values for a record that is created in the context of another record." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "mayadumesh" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "kvivek" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Customize entity and attribute mappings

You can map attributes between entities that have an entity relationship. This lets you set default values for a record that is created in the context of another record. Use the customization tools in the application to map attributes; see [Map entity fields](../../maker/common-data-service/map-entity-fields.md).

<a name="bkmk_BehaviorintheApplication"></a>

## Behavior in the application

 Mapping in Common Data Service (CDS) for Apps streamlines data entry when you create new records that are associated with another record. When an entity has an entity relationship with another entity, you can create new related entity records by using the **Create Related** tab in the ribbon. When you create a new record in this manner, mapped data from the primary entity record is copied to the form for the new related entity record. By mapping entity attributes, you control what data is copied by adding new mappings in the relationship between the two entities. If you create a record in any way other than from the associated view of the primary entity, data is not mapped.  

 For example, you might want to set up a mapping between the address fields in accounts and the address fields in contacts. With this mapping, when a user adds a contact associated with a specific account, the address fields for the contact are populated automatically.  

 You can map one attribute to multiple target attributes. For example, you can map address information in an account to both the billing and shipping addresses in an order.  

 Mapping is applied before a new, related record is created. Users can make changes before saving the record. Later changes to the data in the primary record are not applied to the related record.  

<a name="bkmk_UsingEntityandAttributeMappingData"></a>

## Using entity and attribute mapping data

### Using Web API

When working with the Web API, you can use <xref href="Microsoft.Dynamics.CRM.InitializeFrom?text=InitializeFrom Function" /> to create new records in the context of existing records where a mapping exists between the entities. 

The response received from InitializeFrom request consists of values of mapped attributes between the source entity and target entity and the GUID of parent record. The attribute mapping between entities that have an entity relationship is different for different entity sets and is customizable, so the response from InitializeFrom function request may vary for different entities and organizations. When this response is passed in the body of create request of the new record, these attribute values are replicated in the new record. The values of custom mapped attributes also get set in the new record during the process.

> [!NOTE] 
> To determine if two entities can be mapped, use the following Web API request:<br/>`GET [Organization URI]/api/data/v9.0/entitymaps?$select=sourceentityname,targetentityname&$orderby=sourceentityname`

For more information see [Create a new entity from another entity](webapi/create-entity-web-api.md#create-a-new-entity-from-another-entity).

### Using Organization Service

 When creating new records in the context of an existing record where a mapping exists between the entities, you can use the 
 <xref:Microsoft.Crm.Sdk.Messages.InitializeFromRequest> message to define a new record that contains the values specified in the mapping. You can then use the 
<xref:Microsoft.Xrm.Sdk.IOrganizationService>.
 <xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*> method to save the record. In in this manner, any mappings that you define are applied.  

 Valid entity maps are created when an entity relationship is created. Use the `entity_map_attribute_maps` entity relationship to retrieve the attribute maps for the pair of entities specified by the entity map.  
 You can create or update attribute map records. The following requirements must be met for attribute maps:  
- The <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata> type must match.
- The length of the target field cannot be shorter than the source field.
- The format must match.
- The target field must not be used in another mapping.
- The source field must be visible on the entity form.
- The target field must be a field in which a user can enter data.
- Address ID values cannot be mapped.
- PartyList attributes, where <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata>.<xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.AttributeType> is <xref:Microsoft.Xrm.Sdk.Metadata.AttributeTypeCode>.PartyList cannot be mapped.

<a name="bkmk_Automapping"></a>

## Auto-mapping attributes between entities

 You can edit attribute mappings between entities for entity relationships that support mapping. 

 In addition to creating each attribute map manually, you can use the 
 `AutoMapEntity` message(<xref href="Microsoft.Dynamics.CRM.AutoMapEntity?text=AutoMapEntity Action" /> or <xref:Microsoft.Crm.Sdk.Messages.AutoMapEntityRequest> class) to generate a new set of attribute mappings. This message performs the action found under the **Generate Mappings** menu option in the **More Actions** menu on the toolbar (see [Automatically generate field mappings](../../maker/common-data-service/map-entity-fields.md#automatically-generate-field-mappings)). This message maps all the attributes between the two related entities where the attribute names and types are identical. This message is provided as a productivity enhancement so that you do not have to manually add all attribute mappings. Instead, you can generate a set of likely mappings and minimize the amount of manual work to add or remove individual mappings to meet your requirements. 

> [!NOTE]
> Automatically generating mappings in this manner will remove any previously defined attribute mappings and may include mappings that you do not want.  

<a name="BKMK_mapping"></a>

## Retrieve the entity and attribute mappings

 An easy way to see the mappings that have been created is to use the following FetchXML query. For more information on how to run this query, see [Use FetchXML to query data](use-fetchxml-construct-query.md).

```xml

<fetch version='1.0' mapping='logical' distinct='false'>
   <entity name='entitymap'>
      <attribute name='sourceentityname'/>
      <attribute name='targetentityname'/>
      <link-entity name='attributemap' alias='attributemap' to='entitymapid' from='entitymapid' link-type='inner'>
         <attribute name='sourceattributename'/>
         <attribute name='targetattributename'/>
      </link-entity>
   </entity>
 </fetch>
```

### See also

 [Map entity fields](../../maker/common-data-service/map-entity-fields.md)