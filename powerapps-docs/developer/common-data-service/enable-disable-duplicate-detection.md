---
title: "Enable and disable duplicate detection (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This topic covers information on how to enable duplicate detection for all entities in an organization, for a specific entity and for specific operations and how to disable duplicate detection globally or for an entity type by unpublishing the duplicate detection rules or by deleting the published rules." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "mayadumesh" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Enable and Disable duplicate detection

This topic covers information on how to enable and disable duplicate detection in Dynamics 365.

<a name="bkmk_enable"></a>

## Enable duplicate detection

Before running duplicate detection, enable it for each of the following:  
  
-   Globally (for all entities in the organization).  
  
-   For an entity.  
  
-   For specific operations.  
  
> [!NOTE]
>  You must enable duplicate detection in all three areas to detect duplicates for an entity and for operations on an entity.  
  
### Enable duplicate detection globally  
  
-   Use the <xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> message to set the `Organization.IsDuplicateDetectionEnabled` attribute to `true`.
-   Read [Turn duplicate detection rules on or off for the whole organization](/dynamics365/customer-engagement/admin/turn-duplicate-detection-rules-off-whole-organization) to find out how you can use the user interface to enable duplicate detection for the entire organization.
  
### Enable duplicate detection for an entity  
  
-   Use the <xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> message to set the <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.IsDuplicateDetectionEnabled> property to `true`.  
  
### Enable duplicate detection for specific operations  
  
- Set the following attributes to `true`:  
  
  - `Organization.IsDuplicateDetectionEnabledForOnlineCreateUpdate`. Create and update records in CDS for Apps by using the Web application or Dynamics 365 for Outlook. This attribute enables or disables duplicate detection for records created or updated with the <xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> and <xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> messages. However, it does not affect records created or updated with the <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*> and <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*> methods.  
  
  - `Organization.IsDuplicateDetectionEnabledForOfflineSync`. Synchronize offline records when Dynamics 365 for Outlook goes from offline to online.  
  
  - `Organization.IsDuplicateDetectionEnabledForImport`. Import bulk data.  
  
  > [!NOTE]
  >  You do not have to publish the duplicate detection rules to enable duplicate detection for these operations. However, you must publish the duplicate detection rules before you perform the operations.  

<a name="bkmk_disable"></a>

## Disable duplicate detection

Disable duplicate detection globally or for an entity type by unpublishing the duplicate detection rules or by deleting the published rules.  
  
 **Disable duplicate detection globally**  
  
 To disable duplicate detection globally, use the <xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> message to set the `Organization.IsDuplicateDetectionEnabled` attribute to `false`. This automatically unpublishes all duplicate detection rules for all entity types in the organization.  
  
 **Disable duplicate detection for an entity**  
  
 To disable duplicate detection for an entity type, do one of the following:  
  
-   Use the <xref:Microsoft.Xrm.Sdk.Messages.UpdateEntityRequest> message to set the <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.IsDuplicateDetectionEnabled> property to `false`. This automatically unpublishes all duplicate detection rules for an entity type. This removes duplicate detection support for the entity type and you cannot create a new duplicate detection rule for this entity type.  
  
-   Unpublish all duplicate detection rules for an entity type by using the <xref:Microsoft.Crm.Sdk.Messages.UnpublishDuplicateRuleRequest> message.  
  
**Delete published duplicate detection rules**  
  
Delete all published rules in the system to disable duplicate detection globally, or delete published rules for specific entity types by using the <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*> method.  

## See Also

[Duplicate detection](detect-duplicate-data-with-code.md)  
[Run duplicate detection](run-duplicate-detection.md)   
[Duplicate rule entities](duplicaterule-entities.md) 