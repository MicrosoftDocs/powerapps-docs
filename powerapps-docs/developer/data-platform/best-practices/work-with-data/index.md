---
title: "Developers: Best practices and guidance around working with data for the Microsoft Dataverse | Microsoft Docs"
description: Best practices and guidance around working with data for developers of Microsoft Dataverse.
author: JimDaly
ms.topic: article
ms.date: 03/26/2021
ms.subservice: dataverse-developer
ms.author: jdaly
search.audienceType: 
  - developer
---

# Best practices and guidance around working with data for the Microsoft Dataverse

This list below contains all of the best practices and guidance around integrating data using code with the Dataverse.

|Best Practice  |Description  |
|---------|---------|
|[Service protection API limits (Dataverse)](../../api-limits.md)|Understand the limits for API requests.|
|[Optimize performance for Create and Update operations](../../optimize-performance-create-update.md)|Choose the best strategy to create and update large numbers of records in the least amount of time.|
|[Manage invalid characters](invalidcharactersinfield.md)| Manage invalid characters |
|[Retrieve specific columns for a table via query APIs](retrieve-specific-columns-entity-via-query-apis.md) |Queries submitted to retrieve data should include specific columns in the ColumnSet instance associated to the query rather than All Columns.         |

### See Also

[Work with data using code in Dataverse (Power Apps)](../../work-with-data.md)<br />

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
