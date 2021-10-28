---
title: "Developers: Best practices and guidance of client side scripting for model-driven apps | Microsoft Docs"
description: Best practices and guidance of client side scripting for developers of model-driven apps in Power Apps.
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
ms.subservice: mda-developer
ms.author: jowells
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Best practices and guidance of client side scripting for model-driven apps

This list below contains all of the Best practices and guidance of client side scripting for model-driven apps.

[!INCLUDE[cc-terminology](../../../data-platform/includes/cc-terminology.md)]

|Best Practice  |Description  |
|---------|---------|
|[Avoid using window.top](avoid-window-top.md)     |Describes how to avoid script errors and incorrect application behavior associated with using window.top in JavaScript customizations.         |
|[Consider disabling NavBar when programmatically opening forms or views](consider-disabling-navbar-programmatically-opening-entity-forms-views.md)|Opening up forms or views with a URL, could lead to slower client performance on high latency networks when the navigation bar (NavBar) is enabled.|
|[Do not use the OData v2.0 endpoint](do-not-use-odata-v2-endpoint.md)|Describes the requirement to upgrade code to use Web API OData v4.0 endpoint rather than the deprecated OData v2.0 endpoint.|
|[Best practices: Client scripting in model-driven apps](../../clientapi/client-scripting-best-practices.md)     |Some of the best practice tips you could consider while writing your JavaScript code for model-driven apps.         |
|[Interact with HTTP and HTTPS resources asynchronously](interact-http-https-resources-asynchronously.md)     |You should interact with HTTP and HTTPS resources asynchronously when writing JavaScript client extensions for model driven apps.         |
|[Remove deactivated or disabled customizations](remove-deactivated-disabled-configurations.md)     |Deactivated or disabled customizations should be removed from a solution to improve solution management and to decrease the risk of utilizing or managing an outdated component.         |

### See Also
[Apply business logic using client scripting](../../client-scripting.md) <br />
 

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]