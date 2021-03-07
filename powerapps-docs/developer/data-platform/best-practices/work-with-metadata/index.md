---
title: "Developers: Best practices and guidance while working with metadata for the Microsoft Dataverse | Microsoft Docs"
description: Best practices and guidance while working with metadata for developers of the Microsoft Dataverse in Power Apps.
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
ms.date: 12/12/2018
ms.author: jowells
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Best practices and guidance while working with metadata for the Microsoft Dataverse

[!INCLUDE[cc-data-platform-banner](../../../../includes/cc-data-platform-banner.md)]

This list below contains all of the guidance and best practices regarding interacting and working with metadata within the Dataverse.


|Best Practice  |Description  |
|---------|---------|
|[Retrieve published metadata](retrieve-published-metadata.md)     |Retrieving unpublished metadata not only will add overhead to processing the request itself, performing more slowly, it could also return metadata that the requestor does not expect.         |
|[Retrieve specific columns for an entity via query APIs](retrieve-specific-columns-entity-via-query-apis.md)     |Queries submitted to retrieve data should include specific columns in the ColumnSet instance associated to the query rather than All Columns.         |

### See Also
[Work with metadata using code](../../metadata-services.md)<br />


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]