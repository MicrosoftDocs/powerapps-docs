---
title: "Detect duplicate data using code (Common Data Service) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Duplicate detection lets organizations set duplicate detection policies and create duplicate detection rules for business and custom entities" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "mayadumesh" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Detect duplicate data using code

[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

Duplicate detection lets organizations set duplicate detection policies and create duplicate detection rules for business and custom entities. These rules can be applied across different record types in Common Data Service. For example, an organization may define that a lead is a duplicate of a contact, if they have the same name and phone number. Based on the duplicate detection rules set by the administrator, the system alerts the user about potential duplicates when the user tries to create new records or update existing records. To maintain data quality, you can schedule a duplicate detection job to check for duplicates for all records that match a certain criteria. You can clean the data by deleting, deactivating, or merging the duplicates reported by a duplicate detection job.

> [!NOTE]
> For information on how to create rules and run system jobs for detecting duplicate data using the user interface (UI), see [Detect duplicate data so you can fix or remove it](/dynamics365/customer-engagement/admin/detect-duplicate-data).

You can use the Web API or Organization service to detect duplicate data. Topics in this section provide information on how you can detect duplicate data using both web services. 

### See also

[Enable and Disable duplicate detection](enable-disable-duplicate-detection.md)<br/>
[Run duplicate detection](run-duplicate-detection.md)<br/>
[Duplicate detection messages](duplicate-detection-messages.md)<br/>
[Duplicate Rule entities](duplicaterule-entities.md)

