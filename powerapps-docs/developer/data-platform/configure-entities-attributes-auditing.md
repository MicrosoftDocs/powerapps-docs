---
title: "Configure tables and columns for auditing (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Explains configuration requirements to enable and disable auditing of tables and their columns." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 03/26/2021
ms.reviewer: "pehecke"
ms.service: powerapps
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

# Configure tables and columns for auditing

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

There are three levels where auditing can be configured: organization, table, and column. The organization level is the highest level, followed by the table level, and finally the column level. For column auditing to take place, auditing must be enabled at the column, table, and organization levels. For table auditing to take place, auditing must be enabled at the table and organization levels.  
  
 There is a slight difference in how auditing is enabled or disable for an organization compared to a table or column. You enable or disable auditing at the organization level by setting a particular column value of the organization record. However, for tables and columns, you set a property value of the table or column definition.  
  
 A user must be assigned the System Administrator or System Customizer role to enable or disable auditing.  
  
## Enabling auditing  

 By setting the <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.IsAuditEnabled> property of a table’s definition and the <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.IsAuditEnabled> property of each desired column’s definition to `true`, data changes to records of those tables can be logged by the platform. However, when enabling auditing on a table, all of the table’s columns are enabled for auditing by default. Of course you can explicitly disable auditing on any or all of the columns as needed. The <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.IsAuditEnabled> property can be set when the table or column definition is created or updated through the following requests: <xref:Microsoft.Xrm.Sdk.Messages.CreateEntityRequest>, <xref:Microsoft.Xrm.Sdk.Messages.UpdateEntityRequest>, <xref:Microsoft.Xrm.Sdk.Messages.CreateAttributeRequest>, <xref:Microsoft.Xrm.Sdk.Messages.UpdateAttributeRequest>.  
  
 After changing the table column definition, you must publish the table by using <xref:Microsoft.Crm.Sdk.Messages.PublishXmlRequest>. Changing the <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.IsAuditEnabled> property at the table level does not require publishing. Typically, customization and publishing is performed by the same user. However, if these tasks are performed by different users, auditing will record the publish action, the user that initiated the publish operation, and not the update action.  
  
 In addition, auditing is enabled at the organization level by setting the <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.IsAuditEnabled> column value of the target organization record to `true`.  
  
## Disabling auditing

 To disable auditing, just set <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.IsAuditEnabled>, as described previously, to `false`. Publish the table customizations if you have disabled auditing on any columns. You can disable auditing for a whole organization by setting the <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.IsAuditEnabled> column to `false` in the target organization’s record.  
  
## Entities that can be audited

 All custom and most customizable tables can be audited. For a list of customizable tables, see [Which tables are customizable?](/dynamics365/customer-engagement/developer/which-entities-are-customizable).  
  
 The following table lists the non-customizable tables that cannot be audited. This table was obtained by testing for a `CanModifyAuditSettings` column value of `false` on each table’s definition.  
  
|Non-customizable tables|  
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

 [Data management in Dynamics 365](/dynamics365/customer-engagement/developer/manage-data)   
 [Audit table data changes](/dynamics365/customer-engagement/developer/audit-entity-data-changes)   
 [Retrieve and delete the history of audited data changes](retrieve-and-delete-the-history-of-audited-data-changes.md)   
 [Sample: Audit table data changes](/dynamics365/customerengagement/on-premises/developer/sample-audit-entity-data-changes)   
 [Auditing data changes in Dynamics 365](/dynamics365/customer-engagement/developer/audit-entity-data-changes)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
