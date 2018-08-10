---
title: "Enable document management for entities (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Document management can be enabled for customizable entities in Dynamics 365. To enable document management for an entity, set the EntityMetadata.IsDocumentManagementEnabled attribute value to true" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "JimDaly" #TODO: NoOwner
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Enable document management for entities

Document management can be enabled for those entities in Common Data Service for Apps that can be customized. By default, document management is enabled only for the following entities in a new installation of CDS for Apps:  
  
- `Account`  
  
- `KbArticle`  
  
- `Lead`  
  
- `Opportunity`  
  
- `Product`  
  
- `Quote`  
  
- `SalesLiterature`  
  
  To enable document management for an entity, set the <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata>.<xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.IsDocumentManagementEnabled> attribute value to **true**. To disable document management for an entity, set the value to **false**.  
  
> [!NOTE]
>  You must have the System Administrator or System Customizer role to enable or disable document management for an entity.  
  
### See also  
 [SharePoint Extensions for Dynamics 365](integrate-sharepoint.md)   
 [Actions on SharePoint Location Records](actions-on-sharepoint-location-records.md)   
 [Sample: Enable SharePoint Integration](sample-enable-document-management-entities.md)
