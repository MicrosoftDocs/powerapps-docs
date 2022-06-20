---
title: Portal checker configuration issues
description: Learn about Portal Checker diagnostics results for configuration issues.
author: neerajnandwana-msft

ms.topic: conceptual
ms.custom: 
ms.date: 06/20/2022
ms.subservice: portals
ms.author: nenandw
ms.reviewer: ndoelman
contributors:
    - neerajnandwana-msft
    - nickdoelman
    - dileepsinghmicrosoft
    - ProfessorKendrick
---

# Analyze and resolve Portal Checker diagnostics results

In this article, you'll learn about Portal Checker diagnostics results related to configuration issues, and how to resolve any issues or problems found.

## Web page has a publishing state that belongs to a different web site

This issue occurs when a [publishing state](../configure/publishing-states.md) is associated with a different [website](../configure/websites.md). To fix this issue:

1. Open the [Portal Management app](../configure/configure-portal.md).
1. In the left pane, select **Web Pages**.
1. Select the web pages [listed](#identifying-web-pages-listed-in-diagnostic-results) in the portal checker diagnostic results.
1. Update the **Publishing State** field to point to a publishing state record in the same website. 

## Web page doesn't have a publishing state

This issue occurs when a [web page](../configure/web-page.md) record doesn't have a corresponding [publishing state](../configure/publishing-states.md). To fix this issue:

1. Open the [Portal Management app](../configure/configure-portal.md).
1. In the left pane, select **Web Pages**.
1. Select the web pages [listed](#identifying-web-pages-listed-in-diagnostic-results) in the portal checker diagnostic results.
1. Update the **Publishing State** field to point to a publishing state record. 

## Web page is trying to use an inactive page template

This issue occurs when the [page template](../configure/page-templates.md) record is inactive. To fix this issue:

1. Open the [Portal Management app](../configure/configure-portal.md).
1. In the left pane, select **Web Pages**.
1. Select the web pages [listed](#identifying-web-pages-listed-in-diagnostic-results) in the portal checker diagnostic results.
1. Select the **Page Template** record to navigate to the record.
1. Select **Activate** from the command bar.
1. Alternatively, update the **Page Template** to point to an active page template in the web page.

## Web Page has a page template that belongs to a different web site

This issue occurs when a [page template](../configure/page-templates.md) is associated with a different [website](../configure/websites.md). To fix this issue:

1. Open the [Portal Management app](../configure/configure-portal.md).
1. In the left pane, select **Web Pages**.
1. Select the web pages [listed](#identifying-web-pages-listed-in-diagnostic-results) in the portal checker diagnostic results.
1. Update the **Web site** field to point the appropriate website.
1. Alternatively, update the **Page Template** to point to a page template in the same website.

## Parent page of an active web page is inactive

This issue occurs when a parent [web page](../configure/web-page.md) record is inactive. To fix this issue:

1. Open the [Portal Management app](../configure/configure-portal.md).
1. In the left pane, select **Web Pages**.
1. Select the web page [listed](#identifying-web-pages-listed-in-diagnostic-results) in the portal checker diagnostic results.
1. Select the **Parent Page** record to navigate to the record.
1. Select **Activate** from the command bar.

## Web page needs at least one active localized language content page

This issue occurs when the [web page](../configure/web-page.md) doesn't have at least one [language content page](../configure/enable-multiple-language-support.md#create-content-in-multiple-languages). To fix this issue:

1. Open the [Portal Management app](../configure/configure-portal.md).
1. In the left pane, select **Web Pages**.
1. Select the web pages [listed](#identifying-web-pages-listed-in-diagnostic-results) in the portal checker diagnostic results.
1. Scroll down to the **Localized Content** section.
1. Select **+ New Web Page** to create a new language content page.

    > [!Note]
    > The configuration fields on the home page of a content page is not inherited to the existing content pages. They are used only in creation of new content pages. You must update the content page configurations individually.

## Web page associated a localized content page as a parent web page  

This issue occurs when a [web page](../configure/web-page.md) record has it's **Parent Web Page** associated to a [language content page](../configure/enable-multiple-language-support.md#create-content-in-multiple-languages). To fix this issue:

1. Open the [Portal Management app](../configure/configure-portal.md).
1. In the left pane, select **Web Pages**.
1. Select the web pages [listed](#identifying-web-pages-listed-in-diagnostic-results) in the portal checker diagnostic results.
1. Update the **Parent Page** field to point to a valid web page record that isn't a content page.

## Web page without a page template

This issue occurs when a [web page](../configure/web-page.md) record doesn't have a corresponding [page template](../configure/page-templates.md). To fix this issue:

1. Open the [Portal Management app](../configure/configure-portal.md).
1. In the left pane, select **Web Pages**.
1. Select the web page [listed](#identifying-web-pages-listed-in-diagnostic-results) in the portal checker diagnostic results.
1. Update the **Page Template** field to point to an active page template record.
 
### See also

[Run Portal Checker](portal-checker.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
