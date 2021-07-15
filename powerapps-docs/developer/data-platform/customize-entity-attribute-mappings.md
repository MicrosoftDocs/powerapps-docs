---
title: "Customize table and column mappings in Power Apps (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn about mapping columns between tables that have a relationship in Power Apps. This lets you set default values for a record that is created in the context of another record." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 03/11/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "mayadumesh" # GitHub ID
ms.subservice: dataverse-developer
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "kvivek" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Customize table and column mappings

You can map columns between tables that have a relationship. This lets you set default values for a record that is created in the context of another record. Use the customization tools in the application to map tables; see [Map columns](../../maker/data-platform/map-entity-fields.md).

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

## Behavior in the application

 Mapping in Microsoft Dataverse streamlines data entry when you create new records that are associated with another record. When a table has a relationship with another table, you can create new related records by using the **Create Related** tab in the ribbon. When you create a new record in this manner, mapped data from the primary  record is copied to the form for the new related record. By mapping table columns, you control what data is copied by adding new mappings in the relationship between the two tables. If you create a record in any way other than from the associated view of the primary table, data is not mapped.  

 For example, you might want to set up a mapping between the address columns in accounts and the address columns in contacts. With this mapping, when a user adds a contact associated with a specific account, the address columns for the contact are populated automatically.  

 You can map one column to multiple target columns. For example, you can map address information in an account to both the billing and shipping addresses in an order.  

 Mapping is applied before a new, related record is created. Users can make changes before saving the record. Later changes to the data in the primary record are not applied to the related record.  

## Using table and column mapping data

### Using Web API

When working with the Web API, you can use <xref href="Microsoft.Dynamics.CRM.InitializeFrom?text=InitializeFrom Function" /> to create new records in the context of existing records where a mapping exists between the tables. 

The response received from InitializeFrom request consists of values of mapped columns between the source table and target table and the GUID of parent record. The column mapping between tables that have a relationship is different for different table sets and is customizable, so the response from InitializeFrom function request may vary for different tables and organizations. When this response is passed in the body of create request of the new record, these column values are replicated in the new record. The values of custom mapped columns also get set in the new record during the process.

> [!NOTE] 
> To determine if two tables can be mapped, use the following Web API request:<br/>`GET [Organization URI]/api/data/v9.0/entitymaps?$select=sourceentityname,targetentityname&$orderby=sourceentityname`

For more information see [Create a new row from another table](webapi/create-entity-web-api.md#create-a-new-table-row-from-another-table).

### Using Organization Service

 When creating new records in the context of an existing record where a mapping exists between the tables, you can use the 
 <xref:Microsoft.Crm.Sdk.Messages.InitializeFromRequest> message to define a new record that contains the values specified in the mapping. You can then use the 
<xref:Microsoft.Xrm.Sdk.IOrganizationService>.
 <xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*> method to save the record. In in this manner, any mappings that you define are applied.  

 Valid table maps are created when a relationship is created. Use the `entity_map_attribute_maps` relationship to retrieve the column maps for the pair of tables specified by the table map.  
 You can create or update column map records. The following requirements must be met for column maps:  
- The <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata> type must match.
- The length of the target column cannot be shorter than the source column.
- The format must match.
- The target column must not be used in another mapping.
- The source column must be visible on the form.
- The target column must be a field in which a user can enter data.
- Address ID values cannot be mapped.
- PartyList columns, where <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata>.<xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.AttributeType> is <xref:Microsoft.Xrm.Sdk.Metadata.AttributeTypeCode>.PartyList cannot be mapped.

<a name="bkmk_Automapping"></a>

## Auto-mapping columns between tables

 You can edit column mappings between table for relationships that support mapping. 

 In addition to creating each column map manually, you can use the 
 `AutoMapEntity` message(<xref href="Microsoft.Dynamics.CRM.AutoMapEntity?text=AutoMapEntity Action" /> or <xref:Microsoft.Crm.Sdk.Messages.AutoMapEntityRequest> class) to generate a new set of column mappings. This message performs the action found under the **Generate Mappings** menu option in the **More Actions** menu on the toolbar (see [Automatically generate column mappings](../../maker/data-platform/map-entity-fields.md#automatically-generate-column-mappings)). This message maps all the columns between the two related tables where the column names and types are identical. This message is provided as a productivity enhancement so that you do not have to manually add all column mappings. Instead, you can generate a set of likely mappings and minimize the amount of manual work to add or remove individual mappings to meet your requirements.

> [!NOTE]
> Automatically generating mappings in this manner will remove any previously defined column mappings and may include mappings that you do not want.  

<a name="BKMK_mapping"></a>

## Retrieve the table and column mappings

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

 [Map columns](../../maker/data-platform/map-entity-fields.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]