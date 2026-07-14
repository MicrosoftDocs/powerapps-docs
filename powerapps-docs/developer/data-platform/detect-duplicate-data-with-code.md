---
title: "Detect duplicate data using code (Microsoft Dataverse) | Microsoft Docs"
description: "Duplicate detection lets organizations set duplicate detection policies and create duplicate detection rules for business and custom tables." 
ms.custom: ""
ms.date: 03/26/2021
ms.reviewer: "pehecke"

ms.topic: "article"
author: "mayadumesh" # GitHub ID
ms.subservice: dataverse-developer
ms.author: "jdaly" # MSFT alias of Microsoft employees only
search.audienceType: 
  - developer
---
# Detect duplicate data using code

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

Duplicate detection lets organizations set duplicate detection policies and create duplicate detection rules for business and custom tables. These rules can be applied across different record types in Microsoft Dataverse. For example, an organization may define that a lead is a duplicate of a contact, if they have the same name and phone number. Based on the duplicate detection rules set by the administrator, the system alerts the user about potential duplicates when the user tries to create new records or update existing records. To maintain data quality, you can schedule a duplicate detection job to check for duplicates for all records that match a certain criteria. You can clean the data by deleting, deactivating, or merging the duplicates reported by a duplicate detection job.

> [!NOTE]
> For information on how to create rules and run system jobs for detecting duplicate data using the user interface (UI), see [Set up duplicate detection rules to keep your data clean](/power-platform/admin/set-up-duplicate-detection-rules-keep-data-clean).

You can use the Web API or SDK for .NET to detect duplicate data. Topics in this section provide information on how you can detect duplicate data using both web services. 

### See also

[Enable and disable duplicate detection](enable-disable-duplicate-detection.md)<br/>
[Run duplicate detection](run-duplicate-detection.md)<br/>
[Duplicate detection messages](duplicate-detection-messages.md)<br/>
[Duplicate rule tables](duplicaterule-entities.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
