---
title: Published state configuration
description: Learn about Portal Checker diagnostics results - published state configuration.
author: neerajnandwana-msft

ms.topic: conceptual
ms.custom: 
ms.date: 3/28/2022
ms.subservice: portals
ms.author: nenandw
ms.reviewer: ndoelman
contributors:
    - neerajnandwana-msft
    - nickdoelman
    - dileepsinghmicrosoft
    - Professor Kendrick
---

# Published state configuration

## Web page without a publishing state

This issue occurs when a [web page](../configure/web-page.md) record does not have a corresponding [publishing state](../configure/publishing-states.md). To fix this issue:

1. Open the [Portal Management app](../configure/configure-portal.md).
1. In the left pane, select **Web Pages**.
1. Select the web pages [listed](#identifying-web-pages-listed-in-diagnostic-results) in the portal checker diagnostic results.
1. Update the **Publishing State** field to point to an publishing state record. 

## Web page having a publishing state belong to different web site

This issue occurs when a [publishing state](../configure/publishing-states.md) is associated with a different [website](../configure/websites.md). To fix this issue:

1. Open the [Portal Management app](../configure/configure-portal.md).
1. In the left pane, select **Web Pages**.
1. Select the web pages [listed](#identifying-web-pages-listed-in-diagnostic-results) in the portal checker diagnostic results.
1. Update the **Publishing State** field to point to an publishing state record in the same website. 

## Published state isn't available for this website

To fix this issue, ensure that the publishing state **Published** is available and active.

## Published state isn't visible

To fix this issue, ensure that the publishing state **Published** has the **isVisible** checkbox is selected.

### See also

[Run Portal Checker](portal-checker.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
