---
title: "Audit user access (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Support for the ability to audit user access, including user identification, access time, and client type." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "paulliew" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Audit user access

Common Data Service for Apps support the ability to audit user access. The information that is recorded includes when the user started accessing CDS for Apps and if access originated from the CDS for Apps web application, Dynamics 365 for Outlook, or SDK calls to the web services.  
  
## Enable user access auditing  
 Auditing of user access is enabled at the organization level. To enable or disable user access auditing, you must retrieve the target organization’s record, and update the `Organization.IsUserAccessAuditEnabled` attribute value for the organization. Global auditing on the organization must also be enabled by setting the `Organization.IsAuditEnabled` attribute to `true` in the organization record. To audit the origin of user access, for example: web application, Dynamics 365 for Outlook or SDK, you must enable auditing on the entities being accessed.  
  
 The frequency of auditing user access can be read or set using the `Organization.UserAccessAuditingInterval` attribute. The default attribute value of 4 indicates user access is audited once every 4 hours.  
  
 For more information about enabling auditing for an organization and entity, see [Configure Entities and Attributes for Auditing](configure-entities-attributes-auditing.md).  
  
## Filter on user access events  
 To search for audit records that are related to user access, your code should retrieve `Audit` records of an organization and filter on the value in `Audit.Action`. An enumeration named `AuditAction` is provided to identify supported audit actions. The actions related to user access are shown in the following list.  
  
-   `AuditAction.UserAccessviaWeb`  
  
-   `AuditAction.UserAccessviaWebServices`  
  
-   `AuditAction.UserAccessAuditStarted`  
  
-   `AuditAction.UserAccessAuditStopped`  
  
 `UserAccessviaWeb` indicates access from the CDS for Apps web application or Dynamics 365 for Outlook. `UserAccessviaWebServices` indicates a web service request from the SDK. The `AuditAction` enumeration is available to your code when you include `OptionSets.cs` or `OptionSets.vb` in your application’s project.  
  
### See also  
 [Audit Entity Data Changes in Dynamics 365](/dynamics365/customer-engagement/developer/audit-entity-data-changes)   
 [Configure Entities and Attributes for Auditing](/dynamics365/customer-engagement/developer/configure-entities-attributes-auditing)     
 [Sample: Audit Entity Data Changes](/dynamics365/customer-engagement/developer/sample-audit-entity-data-changes)   
 [Sample: Audit User Access](/dynamics365/customer-engagement/developer/sample-audit-user-access)
