---
title: "Developers: Best practices and guidance while working with table definitions in Microsoft Dataverse | Microsoft Docs"
description: Best practices and guidance while working with table definitions for developers of the Microsoft Dataverse in Power Apps.
services: ''
suite: powerapps
documentationcenter: na
author: jowells
manager: austinj
editor: ''
tags: ''
ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 03/24/2021
ms.author: jowells
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Best practices and guidance while working with table definitions in Dataverse

This list below contains all of the guidance and best practices regarding interacting and working with table definitions in Dataverse.

[!INCLUDE[cc-terminology](../../includes/cc-terminology.md)]


|Best Practice  |Description  |
|---------|---------|
|[Retrieve published definitions](retrieve-published-metadata.md)     |Retrieving unpublished definitions not only will add overhead to processing the request itself, performing more slowly, it could also return definitions that the requestor does not expect.         |
|[Retrieve specific columns for a= table via query APIs](retrieve-specific-columns-entity-via-query-apis.md)     |Queries submitted to retrieve data should include specific columns in the ColumnSet instance associated to the query rather than All Columns.         |

### See Also
[Work with definitions using code](../../metadata-services.md)<br />


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
