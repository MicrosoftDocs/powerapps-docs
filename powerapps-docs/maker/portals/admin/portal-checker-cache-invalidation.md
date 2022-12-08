---
title: Cache invalidation
description: Learn about Portal Checker diagnostics results for cache invalidation issues.
author: neerajnandwana-msft

ms.topic: conceptual
ms.custom: 
ms.date: 07/19/2022
ms.subservice: portals
ms.author: nenandw
ms.reviewer: ndoelman
contributors:
    - neerajnandwana-msft
    - nickdoelman
    - dileepsinghmicrosoft
    - ProfessorKendrick
---

# Cache invalidation

In this article, you'll learn about Portal Checker diagnostics results for cache invalidation issues.

## Portal isn't displaying updated data from Microsoft Dataverse environment

Any data displayed on the portal is rendered from the portal cache. This cache gets updated whenever data in the Dataverse environment is updated. However, this process can take up to 15 minutes. If changes are made in the metadata table of the portal (for example, webpages, web files, content snippet, or site setting), it's recommended to clear the cache manually or restart the portal from the Power Apps portals admin center. For information on how to clear cache, see [Server-side cache in portals](clear-server-side-cache.md). 

However, if you're seeing stale data for a long period of time in non-portal metadata tables, it could be because of one of the following issues.

### Tables not enabled for cache invalidation

If you're seeing stale data only for certain tables and not everything, this can be because the change tracking metadata isn't enabled on that specific table.

If you run the Portal Checker (self-service diagnostic) tool, it will list the Object Type Code of all the tables that are referenced on the portal that aren't enabled for change tracking. You can browse your metadata by following the steps outlined at [Browse the metadata for your organization](/dynamics365/customerengagement/on-premises/developer/browse-your-metadata).

If you're experiencing stale data issues in any of these tables, you can enable change tracking by using the Power Apps portals admin center UI or Dynamics 365 API. For more information, see [Enable change tracking for a table](/dynamics365/customerengagement/on-premises/developer/use-change-tracking-synchronize-data-external-systems#enable-change-tracking-for-an-entity).

### Organization not enabled for change tracking

Apart from each table being enabled for change tracking, organizations on the whole have to be enabled for change tracking as well. An organization is enabled for change tracking when a portal provisioning request is submitted. However, this can break if an organization is restored from an old database or reset. To fix this issue:

1. Open [Power Apps portals admin center](admin-overview.md).
2. In the **Portal Details** tab, select **Off** from the **Portal State** list.
3. Select **Update**.
4. Select **On** from the **Portal State** list.
5. Select **Update**.

### I'm getting a "Page Not Found" error and the page content is different from the default Page Not Found site marker or web page

You may see a *Page Not Found* error message that appears different from the default error page content on the **Page Not Found** site marker and webpage.

![Page Not Found.](media/page-not-found.png "Page Not Found")

This *Page Not Found* error appears if: 

- The default **Page Not Found** site marker is configured incorrectly.
- The default **Page Not Found** site marker is deleted.
- The default **Page Not Found** webpage is deleted.

To resolve this error, ensure that you have the default site marker named **Page Not Found** present and configured correctly. If the site marker is present and correctly configured, check if the **Page Not Found** webpage is selected for the site marker or whether the **Page Not Found** webpage is present or not.

For steps to create a site marker for **Page Not Found**, go to [An active Page Not Found site marker isn't available for this portal](portal-checker-configuration-issues.md#an-active-page-not-found-site-marker-isnt-available-for-this-portal).

For steps to check site marker configuration and ensure it points to the correct webpage, go to [The Page Not Found site marker isn't pointing to any webpage](portal-checker-configuration-issues.md#the-page-not-found-site-marker-isnt-pointing-to-any-webpage).

For steps to change the site marker to point to the correct **Page Not Found** webpage, go to [The Page Not Found site marker is pointing to a deactivated webpage](portal-checker-configuration-issues.md#the-page-not-found-site-marker-is-pointing-to-a-deactivated-webpage).

### See also

[Run Portal Checker](portal-checker.md)
