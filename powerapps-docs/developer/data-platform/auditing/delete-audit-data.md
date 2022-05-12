---
title: "Delete audit data (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Explains how to configure programatically delete audit data." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 05/10/2022
ms.reviewer: jdaly
ms.topic: overview
author: Bluebear7 # GitHub ID
ms.subservice: dataverse-developer
ms.author: munzinge # MSFT alias of Microsoft employees only
manager: mayadu # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
 - JimDaly
 - phecke
---

# Delete audit data

You may need to delete audit data because:
- You need to comply with a request from a customer to delete their history.
- You want to use less log capacity space.

Dataverse provides the following messages to delete audit history data:

|Message|Description|
|---------|---------|
|`DeleteRecordChangeHistory`|Deletes all the audit change history records for a particular record|
|`DeleteAuditData `|Deletes all audit data records up until a specified end date.|
|`BulkDelete`|Asynchronously deletes records identified by a query. This message can be used to delete large numbers of audit records without blocking other activities|

> [!NOTE]
> You cannot directly delete records in the [Auditing (Audit) table](reference/entities/audit.md)