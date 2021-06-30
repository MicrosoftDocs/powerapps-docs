---
title: "BusinessUnit table (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "An organization in Microsoft Dataverse, such as a holding company or a corporation, is made up of business units." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 03/27/2021
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
# BusinessUnit table

An organization in Microsoft Dataverse, such as a holding company or a corporation, is made up of business units. A *business unit* is a unit of the top-level organization. Business units can be parents of other business units (child business units). The first business unit created for an organization is called the root business unit. Business units can be deleted, however, the root business unit can’t be deleted.  
  
- A *parent business unit* is any business unit with one or more business units that report to it in the hierarchy.  
  
- A *child business unit* is a business unit that is immediately under another business unit in the business hierarchy of an organization.  
  
 A business unit can own records as defined in the ownership type in the definition of a table. 
  
 Security roles are associated with a business unit. You can call the <xref:Microsoft.Crm.Sdk.Messages.WhoAmIRequest> message to find out the business unit for the currently logged on or impersonated user.

### See also

[BusinessUnit table reference](reference/entities/businessunit.md)<br/>
[Security and data access](security-model.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
