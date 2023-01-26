---
title: How to run Portal Checker
description: Learn how to run Portal Checker within Power Apps to help you identify common problems within your portal and get suggestions on how to fix them.
author: neerajnandwana-msft

ms.topic: conceptual
ms.custom: 
ms.date: 07/18/2022
ms.subservice: portals
ms.author: nenandw
ms.reviewer: ndoelman
contributors:
    - neerajnandwana-msft
    - nickdoelman
---

# Run Portal Checker

Portal Checker is a self-service diagnostic tool that can be used by portal administrators to identify common issues in their portal. Portal Checker helps to identify issues with a portal by looking at various configuration parameters and provides suggestions on how to fix them.

When you run Portal Checker, the results are displayed in the **Diagnostic Results** section in a grid format. The results grid has the following columns:

- **Issue**: Displays the top-level issue faced by a customer; for example, performance issue.
- **Category**: Displays the top-level area where issues can be categorized; for example, provisioning or solution upgrade.
- **Result**: Displays the status of the issue; for example, error or warning.

By default, information in the grid is sorted by the **Result** column in this order: error, warning, and pass.

> [!div class=mx-imgBorder]
> ![Diagnostic results.](../media/diagnostic-results.png "Diagnostic results")

You can expand an issue to view detailed information and mitigation steps. If the mitigation requires any action, you'll see a button that will perform the action. You can also provide feedback on whether the mitigation was useful.

> [!div class=mx-imgBorder]
> ![Expand an issue in diagnostic results.](../media/diagnostic-results-issue-expand.png "Expand an issue in diagnostic results")

If required, you can rerun the diagnostic checks, which will refresh the results with updated data.

> [!NOTE]
> If portal is turned off or IP address filtering is enabled, certain diagnostic checks will not be run on your portal.

For a list of common issues diagnosed by Portal Checker, see [Common portal issues diagnosed by Portal Checker and their best practices](/dynamics365/customer-engagement/portals/portal-faq).

To run Portal Checker:

1. Open [Power Apps portals admin center](admin-overview.md).

1. Go to **Run Portal Checker**.

    > [!div class=mx-imgBorder]
    > ![Run Portal Checker.](../media/run-diagnostics.png "Run Portal Checker")

1. Select the **Run Portal Checker** button. The diagnostic session will start and gather data about the customer issues. The results are displayed in the **Diagnostic Results** section.

    > [!div class=mx-imgBorder]
    > ![Diagnostic results.](../media/diagnostic-results.png "Diagnostic results")

1. To rerun the diagnostic checks, select **Refresh results**.

    > [!div class=mx-imgBorder]
    > ![Refresh diagnostic results.](../media/diagnostic-results-refresh.png "Refresh diagnostic results")

## Identifying web pages listed in diagnostic results

The portal checker diagnostic results could list web pages that have the same name as other pages in the portal. If there are multiple web pages with the same name, you can identify the specific page affected using the unique guid of the page.

1. Open the [Portal Management app](../configure/configure-portal.md).
1. In the left pane, select **Web Pages**.
1. Open any web page.
1. Replace the ID in the URL with the guid specified in the portal checker diagnostic results.

    :::image type="content" source="media/portal-checker-analysis/webpage-by-id.png" alt-text="Replacing the web page ID the URL.":::

## Next steps

Analyze and resolve Portal Checker diagnostics results:
- [Cache invalidation issues](portal-checker-cache-invalidation.md)
- [Configuration issues](portal-checker-configuration-issues.md)
- [Performance issues](portal-checker-performance.md)
- [Portal start-up issues](portal-checker-startup-issue.md)
- [Provisioning issues](portal-checker-provisioning-issues.md)

