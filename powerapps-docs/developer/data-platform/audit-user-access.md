---
title: "Audit user access (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Read about the ability to audit user access, including user identification, access time, and client type." # 115-145 characters including spaces. This abstract displays in the search result.
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

# Audit user access

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

Microsoft Dataverse support the ability to audit user access. The information that is recorded includes when the user started accessing Dataverse and if access originated from the Dataverse web application, Dynamics 365 for Outlook, or SDK calls to the web services.  
  
## Enable user access auditing

 Auditing of user access is enabled at the organization level. To enable or disable user access auditing, you must retrieve the target organization’s record, and update the `Organization.IsUserAccessAuditEnabled` column value for the organization. Global auditing on the organization must also be enabled by setting the `Organization.IsAuditEnabled` column to `true` in the organization record. To audit the origin of user access, for example: web application, Dynamics 365 for Outlook or SDK, you must enable auditing on the tables being accessed.  
  
 The frequency of auditing user access can be read or set using the `Organization.UserAccessAuditingInterval` column. The default column value of four (4) indicates user access is audited once every 4 hours.
  
 For more information about enabling auditing for an organization and table, see [Configure tables and columns for auditing](configure-entities-attributes-auditing.md).  
  
## Filter on user access events

 To search for audit records that are related to user access, your code should retrieve `Audit` records of an organization and filter on the value in `Audit.Action`. An enumeration named `AuditAction` is provided to identify supported audit actions. The actions related to user access are shown in the following list.  
  
-   `AuditAction.UserAccessviaWeb`  
  
-   `AuditAction.UserAccessviaWebServices`  
  
-   `AuditAction.UserAccessAuditStarted`  
  
-   `AuditAction.UserAccessAuditStopped`  
  
 `UserAccessviaWeb` indicates access from the Dataverse web application or Dynamics 365 for Outlook. `UserAccessviaWebServices` indicates a web service request from the SDK. The `AuditAction` enumeration is available to your code when you include `OptionSets.cs` in your application’s project.  
  
### See also

 [Audit data changes](./auditing-overview.md)   
 [Configure tables and columns for auditing](./configure-entities-attributes-auditing.md)     
 [Sample: Audit table data changes](./org-service/samples/audit-entity-data-changes.md)   
 [Sample: Audit user access](./org-service/samples/audit-user-access.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]