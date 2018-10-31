---
title: "BusinessUnit entity (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "An organization in Common Data Service (CDS) for Apps, such as a holding company or a corporation, is made up of business units." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "paulliew" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# BusinessUnit entity

An organization in Common Data Service (CDS) for Apps, such as a holding company or a corporation, is made up of business units. A *business unit* is a unit of the top-level organization. Business units can be parents of other business units (child business units). The first business unit created for an organization is called the root business unit. Business units can be deleted, however, the root business unit can’t be deleted.  
  
- A *parent business unit* is any business unit with one or more business units that report to it in the hierarchy.  
  
- A *child business unit* is a business unit that is immediately under another business unit in the business hierarchy of an organization.  
  
 A business unit can own records as defined in the ownership type in the metadata definition for an entity. 
  
 Security roles are associated with a business unit. You can call the <xref:Microsoft.Crm.Sdk.Messages.WhoAmIRequest> message to find out the business unit for the currently logged on or impersonated user.

### See also

[BusinessUnit Entity Reference](reference/entities/businessunit.md)
[Security entities](security-model.md)