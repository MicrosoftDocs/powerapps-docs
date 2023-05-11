---
title: List OData feeds
description: Learn how to enable a list render as an OData formatted data feed on a portal.
author: sandhangitmsft

ms.topic: conceptual
ms.custom: 
ms.date: 05/27/2022
ms.subservice: portals
ms.author: sandhan
ms.reviewer: ndoelman
contributors:
    - nickdoelman
    - sandhangitmsft
    - ProfessorKendrick
---

# List OData feeds


[!INCLUDE[cc-pages-banner](../../../includes/cc-pages-banner.md)]

> [!NOTE]
> This feature has been deprecated. Alternatively, use the [portals Web API](../web-api-overview.md) to interact with the data.

On the **OData Feed** tab, you can enable the list to render as an OData formatted data feed.

When enabled, a table can be published to an OData feed. The OData protocol is an application-level protocol for interacting with data via RESTful web services. Data from this feed can be viewed in a web browser, consumed by a client-side web application, or imported into [!INCLUDE[pn-excel-short](../../../includes/pn-excel-short.md)].

> [!NOTE]
> Lists that have OData feeds enabled require appropriate [table permissions](entity-permissions-studio.md) setup for the feed on these lists to work. Hence, you must enable table permissions on a list that has OData feeds enabled.
> - Latest portal solutions will show the following error, and won't allow you to save the list without enabling table permissions:
> <br> "Table permissions must be enabled from the General tab because the OData feed is enabled."
> - Older portal solutions don't show the above message. However, for the lists with OData feeds enabled, table permissions are always considered enabled even if you save the list without selecting **Enable Table Permissions** setting explicitly.

### See also

- [Work with lists](entity-lists.md)
- [Configure a portal](configure-portal.md)  
- [Redirect to a new URL on a portal](add-redirect-url.md)
