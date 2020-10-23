---
title: "Auditing Overview (Common Data Service) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Read how the auditing capability of Common Data Service can be used to record attribute and entity data changes over time for use in analysis and reporting purposes." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "Bluebear73" # GitHub ID
ms.author: "munzinge" # MSFT alias of Microsoft employees only
manager: "mayadu" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Auditing overview

[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

Organizations often need to be in compliance with various regulations to ensure availability of customer interaction history, audit logs, access reports, and security incident tracking reports. Organizations may want to track changes in Common Data Service data for security and analytical purpose.  
  
 Common Data Service supports an auditing capability where entity and attribute data changes within an organization can be recorded over time for use in analysis and reporting purposes. Auditing is supported on all custom and most customizable entities and attributes. Auditing is not supported on metadata changes, retrieve operations, export operations, or during authentication. For information on how to configure auditing, see [Configure Entities and Attributes for Auditing](configure-entities-attributes-auditing.md).  
  
## Supported for auditing  
 The following lists auditing capabilities for Common Data Service:  
<!-- TODO: Jim, I don't think this is online only. Please correct the tokens here. -->
  
* Audit of customizable entities
* Audit of custom entities
* Configure entities for audit
* Configure attributes for audit
* Privilege-based audit trail viewing
* Privilege-based audit summary viewing
* Audit log deletion for a partitioned SQL database  
* Audit log deletion for a non-partitioned SQL database 
* Audit of record create, update, and delete operations
* Audit of relationships (1:N, N:N) 
* Audit of audit events
* Audit of user access
* Adherence to regulatory standards
* Auditing APIs for developers
  
## Not supported for auditing  
 The following lists what cannot be audited for Common Data Service:  
  
* Audit of read operations
* Audit of metadata changes 
  
## Key concepts  
 The following bullets identify some key auditing concepts:  
  
-   You can enable or disable auditing at the organization, entity, and attribute levels. If auditing is not enabled at the organization level, auditing of entities and attributes, even if it is enabled, does not occur. By default, auditing is enabled on all auditable entity attributes, but is disabled at the entity and organization level.  
  
-   The ability to retrieve and display the audit history is restricted to users who have certain security privileges: View Audit History, and View Audit Summary. There are also privileges specific to partitions: View Audit Partitions, and Delete Audit Partitions. See the specific message request documentation for information about the required privileges for each message.  
  
-   Audited data changes are stored in records of the **audit** entity.  
  
## Data that can be audited  
 The following list identifies the data and operations that can be audited:  
  
-   Create, update, and delete operations on records.  
  
-   Changes to the shared privileges of a record.  
  
-   N:N association or disassociation of records.  
  
-   Changes to security roles.  
  
-   Audit changes at the entity, attribute, and organization level. For example, enabling audit on an entity.  
  
-   Deletion of audit logs.  
  
-   When (date/time) a user accesses Common Data Service data, for how long, and from what client.  
  
 Enabling or disabling of field level security by setting the <xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.IsSecured> attribute cannot be audited.  
  
### See also
   
 [Configure entities and attributes for auditing](configure-entities-attributes-auditing.md) 
