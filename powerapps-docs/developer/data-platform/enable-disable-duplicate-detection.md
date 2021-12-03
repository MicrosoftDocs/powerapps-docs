---
title: "Enable and disable duplicate detection (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Describes how to enable duplicate detection for all data tables in an organization or for a specific table. Also, this article describes how to disable duplicate detection globally or for a specific table type." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 03/26/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "mayadumesh" # GitHub ID
ms.subservice: dataverse-developer
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Enable and disable duplicate detection

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

This topic covers information on how to enable and disable duplicate detection in Dynamics 365 and Microsoft Dataverse.

<a name="bkmk_enable"></a>

## Enable duplicate detection

Before running duplicate detection, enable it for each of the following:  
  
-   Globally (for all tables in the organization).  
  
-   For a table.  
  
-   For specific operations.  
  
> [!NOTE]
>  You must enable duplicate detection in all three above mentioned areas to detect duplicates for a table and for operations on a table.
  
### Enable duplicate detection globally  
  
-   Use the <xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> message to set the `Organization.IsDuplicateDetectionEnabled` column to `true`.
-   Read [Turn duplicate detection rules on or off for the whole organization](/dynamics365/customer-engagement/admin/turn-duplicate-detection-rules-off-whole-organization) to find out how you can use the user interface to enable duplicate detection for the entire organization.
  
### Enable duplicate detection for a table  
  
-   Use the <xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> message to set the <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.IsDuplicateDetectionEnabled> property to `true`.  
  
### Enable duplicate detection for specific operations  
  
- Set the following columns to `true`:  
  
  - `Organization.IsDuplicateDetectionEnabledForOnlineCreateUpdate`. Create and update records in Microsoft Dataverse by using the Web application or Dynamics 365 for Outlook. This column enables or disables duplicate detection for records created or updated with the <xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> and <xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> messages. However, it does not affect records created or updated with the <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Create*> and <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*> methods.  
  
  - `Organization.IsDuplicateDetectionEnabledForOfflineSync`. Synchronize offline records when Dynamics 365 for Outlook goes from offline to online.  
  
  - `Organization.IsDuplicateDetectionEnabledForImport`. Import bulk data.  
  
  > [!NOTE]
  >  You do not have to publish the duplicate detection rules to enable duplicate detection for these operations. However, you must publish the duplicate detection rules before you perform the operations.  

<a name="bkmk_disable"></a>

## Disable duplicate detection

Disable duplicate detection globally or for a table type by un-publishing the duplicate detection rules or by deleting the published rules.  
  
 **Disable duplicate detection globally**  
  
 To disable duplicate detection globally, use the <xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> message to set the `Organization.IsDuplicateDetectionEnabled` column to `false`. This automatically un-publishes all duplicate detection rules for all table types in the organization.  
  
 **Disable duplicate detection for a table**  
  
 To disable duplicate detection for a table type, do one of the following:  
  
-   Use the <xref:Microsoft.Xrm.Sdk.Messages.UpdateEntityRequest> message to set the <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.IsDuplicateDetectionEnabled> property to `false`. This automatically un-publishes all duplicate detection rules for a table type. This removes duplicate detection support for the table type and you cannot create a new duplicate detection rule for this table type.  
  
-   Un-publish all duplicate detection rules for a table type by using the <xref:Microsoft.Crm.Sdk.Messages.UnpublishDuplicateRuleRequest> message.  
  
**Delete published duplicate detection rules**  
  
Delete all published rules in the system to disable duplicate detection globally, or delete published rules for specific table types by using the <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Delete*> method.  

## See Also

[Duplicate detection](detect-duplicate-data-with-code.md)  
[Run duplicate detection](run-duplicate-detection.md)   
[Duplicate rule tables](duplicaterule-entities.md) 

[!INCLUDE[footer-include](../../includes/footer-banner.md)]