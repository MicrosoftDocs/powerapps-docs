---
title: "Detect duplicate data using code (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "<Description>" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "mayadumesh" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Detect duplicate data using code

Duplicate detection lets organizations set duplicate detection policies and create duplicate detection rules for business and custom entities. These rules can be applied across different record types in Common Data Service (CDS) for Apps. For example, an organization may define that a lead is a duplicate of a contact, if they have the same name and phone number. Based on the duplicate detection rules set by the administrator, the system alerts the user about potential duplicates when the user tries to create new records or update existing records. To maintain data quality, you can schedule a duplicate detection job to check for duplicates for all records that match a certain criteria. You can clean the data by deleting, deactivating, or merging the duplicates reported by a duplicate detection job.

> [!NOTE]
> For information on how to create rules and run system jobs for detecting duplicate data using the user interface (UI), see [Detect duplicate data so you can fix or remove it](/dynamics365/customer-engagement/admin/detect-duplicate-data).  
  
 To detect duplicates in the system, create a *duplicate detection rule* for a specific entity type. A duplicate detection rule is represented by the duplicate rule [DuplicateRule entity](entities/duplicaterule.md). You can create multiple detection rules for the same entity type. However, you can publish a maximum of five duplicate detection rules per entity type at one time.  
  
 A rule can have one or more *duplicate detection rule conditions* that are represented by the duplicate rule condition [DuplicateRuleCondition entity](entities/duplicaterulecondition.md). The conditions are combined by the system as in logical `AND` operation. A duplicate detection rule specifies a base entity type and a matching entity type. A duplicate rule condition specifies the name of a base attribute and the name of a matching attribute. For example, specify an account as a base entity and a contact as a matching entity to compare last names and addresses. The matching criteria consist of operators such as exactly match, first n-number of characters, or last n-number of characters.  

 Duplicate detection works by comparing generated match codes of existing records with each new record being created. These match codes are created as each new record is created. Therefore, there is potential for one or more duplicate records to be created if they are processed at the exact same moment. In addition to detecting duplicates as they are created, you should schedule duplicate detection jobs to check for other potential duplicate records.
 
 The duplicate detection rules are system-wide. You must publish them before running a duplicate detection job to detect duplicates for bulk data or retrieve duplicates for a particular entity record. To publish a duplicate detection rule, use the `PublishDuplicateRule` message(<xref href="Microsoft.Dynamics.CRM.PublishDuplicateRule?text=PublishDuplicateRule Action" /> or <xref:Microsoft.Crm.Sdk.Messages.PublishDuplicateRuleRequest>). Duplicate rule publishing is an asynchronous operation that runs in the background.

## Use Web API for duplicate detection 

More information:  [Manage duplicate detection for create and update operations using the Web API](webapi/manage-duplicate-detection-create-update.md)


## Use Organization service for duplicate detection 

More information:  [Detect duplicate data using the Organization service](org-service/detect-duplicate-data.md)
  

<!-- 
Was Mike Carter

https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/detect-duplicate-data-for-developers 

Tells the high level story
powerapps-docs/developer/common-data-service/detect-duplicate-data-for-developers.md 
Tells the org service story
powerapps-docs/developer/common-data-service/org-service/detect-duplicate-data.md
Tells the Web API Story
powerapps-docs/developer/common-data-service/webapi/detect-duplicate-data.md

