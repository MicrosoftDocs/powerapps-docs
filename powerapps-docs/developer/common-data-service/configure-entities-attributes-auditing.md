---
title: "Configure entities and attributes for auditing (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Explains configuration requirements to enable and disable auditing of entities and their attributes." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "paulliew" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Configure entities and attributes for auditing

There are three levels where auditing can be configured: organization, entity, and attribute. The organization level is the highest level, followed by the entity level, and finally the attribute level. For attribute auditing to take place, auditing must be enabled at the attribute, entity, and organization levels. For entity auditing to take place, auditing must be enabled at the entity and organization levels.  
  
 There is a slight difference in how auditing is enabled or disable for an organization compared to an entity or attribute. You enable or disable auditing at the organization level by setting a particular attribute value of the organization record. However, for entities and attributes, you set a property value of the entity or attribute metadata.  
  
 A user must be assigned the System Administrator or System Customizer role to enable or disable auditing.  
  
## Enabling auditing  

 By setting the <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.IsAuditEnabled> property of an entity’s metadata and the <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.IsAuditEnabled> property of each desired attribute’s metadata to `true`, data changes to records of those entities can be logged by the platform. However, when enabling auditing on an entity, all of the entity’s attributes are enabled for auditing by default. Of course you can explicitly disable auditing on any or all of the attributes as needed. The <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.IsAuditEnabled> property can be set when entity or attribute metadata is created or updated through the following requests: <xref:Microsoft.Xrm.Sdk.Messages.CreateEntityRequest>, <xref:Microsoft.Xrm.Sdk.Messages.UpdateEntityRequest>, <xref:Microsoft.Xrm.Sdk.Messages.CreateAttributeRequest>, <xref:Microsoft.Xrm.Sdk.Messages.UpdateAttributeRequest>.  
  
 After changing the entity attribute metadata, you must publish the entity by using <xref:Microsoft.Crm.Sdk.Messages.PublishXmlRequest>. Changing the <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.IsAuditEnabled> property at the entity level does not require publishing. Typically, customization and publishing is performed by the same user. However, if these tasks are performed by different users, auditing will record the publish action, the user that initiated the publish operation, and not the update action.  
  
 In addition, auditing is enabled at the organization level by setting the <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.IsAuditEnabled> attribute value of the target organization record to `true`.  
  
## Disabling auditing  
 To disable auditing, just set <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.IsAuditEnabled>, as described previously, to `false`. Publish the entity customizations if you have disabled auditing on any attributes. You can disable auditing for a whole organization by setting the <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.IsAuditEnabled> attribute to `false` in the target organization’s record.  
  
## Entities that can be audited  
 All custom and most customizable entities can be audited. For a list of customizable entities, see [Which Entities are Customizable?](/dynamics365/customer-engagement/developer/which-entities-are-customizable).  
  
 The following table lists the non-customizable entities that cannot be audited. This table was obtained by testing for a `CanModifyAuditSettings` attribute value of `false` on each entity’s metadata.  
  
||  
|-|  
|ActivityPointer|  
|Annotation|  
|BulkOperation|  
|Calendar|  
|CalendarRule|  
|CustomerOpportunityRole|  
|Discount|  
|DiscountType|  
|IncidentResolution|  
|KbArticle|  
|KbArticleComment|  
|KbArticleTemplate|  
|Notification|  
|OpportunityClose|  
|OrderClose|  
|ProductPriceLevel|  
|QuoteClose|  
|RecurrenceRule|  
|Resource|  
|ResourceGroup|  
|ResourceGroupExpansion|  
|ResourceSpec|  
|SalesLiteratureItem|  
|SalesProcessInstance|  
|Service|  
|Subject|  
|Template|  
|UoM|  
|UoMSchedule|  
|Workflow|  
|WorkflowLog|  
  
### See also  
 [Data Management in Dynamics 365](/dynamics365/customer-engagement/developer/manage-data)   
 [Audit entity data changes](/dynamics365/customer-engagement/developer/audit-entity-data-changes)   
 [Retrieve and delete the history of audited data changes](retrieve-and-delete-the-history-of-audited-data-changes.md)   
 [Sample: Audit Entity Data Changes](/dynamics365/customer-engagement/developer/sample-audit-entity-data-changes)   
 [Auditing Data Changes in Dynamics 365](/dynamics365/customer-engagement/developer/audit-entity-data-changes)