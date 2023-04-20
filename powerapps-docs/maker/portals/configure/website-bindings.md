---
title: Create and manage website bindings
description: Learn how to create and manage website bindings in portals.
author: sandhangitmsft

ms.topic: conceptual
ms.custom: 
ms.date: 01/11/2023
ms.subservice: portals
ms.author: sandhan
ms.reviewer: ndoelman
contributors:
    - nickdoelman
    - sandhangitmsft
---

# website bindings

[!INCLUDE[cc-pages-ga-banner](../../../includes/cc-pages-ga-banner.md)]

In the [Portal Management app](configure-portal.md), you can view **Website Bindings** metadata records. These records provide the link between the site metadata stored in Microsoft Dataverse and the Power Pages site Azure web application.

> [!WARNING]
> - It is not recommended that you modify the website binding record. Instead, that you use the **Edit** option in the **Site Details** section in the Power Pages hub of the [Power Platform admin center](/power-pages/admin/admin-overview#site-details) and selecting the **Website Record** value.
> - You should be careful while modifying the website binding records as they may cause your site to no longer function.


## Website binding attributes

These are the attributes common to all bindings.

|Name|Description|
|-----|----------|
|Name| A title to identify the website binding when viewing the records.|
|Website|The [website](websites.md) that should be selected by the portal.|

> [!NOTE]
> The **Release Date** and **Expiration Date** attributes are legacy settings and no longer apply to selecting a website record.


### See also
[Create and manage websites](websites.md)


