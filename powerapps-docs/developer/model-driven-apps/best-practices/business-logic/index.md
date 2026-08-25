---
title: "Client-Side Scripting Best Practices for Model-Driven Apps"
description: Review client-side scripting best practices for model-driven apps to prevent errors, improve performance, and manage solutions effectively.
suite: powerapps
author: sriharibs-msft
ms.author: srihas
ms.date: 08/24/2026
ms.reviewer: jdaly
ms.topic: best-practice
ms.subservice: mda-developer
search.audienceType: 
  - developer
contributors: 
  - JimDaly
  - caburk
---

# Client-side scripting best practices for model-driven apps

Review these client-side scripting best practices for model-driven apps to help prevent errors, improve client performance, and manage solutions effectively.

[!INCLUDE[cc-terminology](../../../data-platform/includes/cc-terminology.md)]

|Best practice  |Description  |
|---------|---------|
|[Avoid using window.top](avoid-window-top.md)|Describes how to avoid script errors and incorrect application behavior associated with using window.top in JavaScript customizations.|
|[Consider disabling NavBar when programmatically opening forms or views](consider-disabling-navbar-programmatically-opening-entity-forms-views.md)|Opening forms or views with a URL can lead to slower client performance on high latency networks when the navigation bar (NavBar) is enabled.|
|[Do not use the OData v2.0 endpoint](do-not-use-odata-v2-endpoint.md)|Describes the requirement to upgrade code to use Web API OData v4.0 endpoint rather than the deprecated OData v2.0 endpoint.|
|[Interact with HTTP and HTTPS resources asynchronously](interact-http-https-resources-asynchronously.md)|You should interact with HTTP and HTTPS resources asynchronously when writing JavaScript client extensions for model-driven apps.|
|[Remove deactivated or disabled customizations](remove-deactivated-disabled-configurations.md)|Remove deactivated or disabled customizations from a solution to improve solution management and to decrease the risk of utilizing or managing an outdated component.|

## See also

[Apply business logic using client scripting](../../client-scripting.md)   
 

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
