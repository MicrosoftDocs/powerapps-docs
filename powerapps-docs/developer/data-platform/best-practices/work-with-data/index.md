---
title: "Developers: Best practices and guidance for working with data in Microsoft Dataverse"
description: Best practices and guidance around working with data for developers of Microsoft Dataverse.
author: MsSQLGirl
ms.author: jukoesma
ms.reviewer: jdaly
ms.topic: best-practice
ms.date: 03/02/2026
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
---

# Best practices and guidance for working with data in Microsoft Dataverse

The following list contains best practices and guidance for integrating data by using code with Dataverse.

|Best practice  |Description  |
|---------|---------|
|[Service protection API limits (Dataverse)](../../api-limits.md)|Understand the limits for API requests.|
|[Optimize performance for bulk operations](../../optimize-performance-create-update.md)|Choose the best strategy to create and update large numbers of records in the least amount of time.|
|[Manage invalid characters](invalidcharactersinfield.md)| Manage invalid characters |
|[Retrieve specific columns for a table via query APIs](retrieve-specific-columns-entity-via-query-apis.md) |Queries submitted to retrieve data should include specific columns in the ColumnSet instance associated to the query rather than All Columns.|

### See also

[Work with data using code in Dataverse (Power Apps)](../../work-with-data.md)<br />

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
