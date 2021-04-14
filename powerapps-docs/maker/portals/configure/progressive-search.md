---
title: Progressive search
description: Learn how to configure progressive search in portals for accurate record counts.
author: sandhangitmsft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 04/15/2021
ms.author: sandhan
ms.reviewer: tapanm
contributors:
    - sandhangitmsft
    - tapanm-msft
---

# Progressive search

Finding accurate search results when a portal has several [additional tables](search-additional-entities.md) enabled for search can become difficult. A complex permissions structure for individual tables and records adds to this difficulty. Searching for content on such portals may end up with a high number of results while the results count may not match the records count on the results page.

## Overview

By default, portals search processes only one page for permissions and keywords match. When results span across more than one page causing some results being discarded because of permissions or keywords, the pagination gets distorted.

Progressive search eliminates the possibility of having a mismatch between the results count, and the number of records returned in search results.

A portal configured with progressive search processes five pages for permissions and keywords check, with 50 records for a single search attempt. The search count now shows **50+** on the first page instead of the mismatch count between facet and the results.

## Configure progressive search

To configure progressive search for your portal:

1. Open the [Portal Management app](configure-portal.md) app.
1. On the left-pane, select **Site Settings** under **Website**.
1. Select **New**.
1. Enter **Name** as "Search/EnableProgressiveSearchCounts".
1. Select your website record.
1. Enter **Value** as "true".
1. Select Save.

    ![Progressive search site setting of Search/EnableProgressiveSearchCounts set to true](media/progressive-search/site-setting.png "Progressive search site setting of Search/EnableProgressiveSearchCounts set to true")

1. [Rebuild your search index](search-additional-entities.md#step-6-rebuild-the-search-index).

To disable progressive search, set the value of **Search/EnableProgressiveSearchCounts** site setting to **false**.

## Progressive search with sample data

For example, consider a portal in an environment with [Northwind Traders sample data](../../canvas-apps/northwind-install.md), having search enabled for [Order Products](search-additional-entities.md).

In this sample portal, consider a total of 68 products in the *Order Products* table. However, a user has permissions to access only 10 products.

When the user searches for products, only 10 results show up, even though the search faced shows the total number of products as 68, including the configured filters.

![Search result with mismatch of results count and actual results](media/progressive-search/incorrect-results-count.png "Search result with mismatch of results count and actual results")

This behavior is more prevalent when search results span across multiple pages.

After you enable progressive search on this portal, the search results for the same user, permissions, and keyword shows total number of results as 10 instead.

![Search result with matching results count and actual results](media/progressive-search/correct-results-count.png "Search result with matching results count and actual results")

Furthermore, if a user searches for keyword that results in more than 50 results after the permissions check and keyword filter, the count shows as **50+** instead.

![Search result with 50+ results](media/progressive-search/results-count-50plus.png "Search result with 50+ results")

Selecting next pages, such as page 2, shows the count updated to the total number of search results.

![Search result with 50+ results and next page](media/progressive-search/results-count-50plus-subsequent-page.png "Search result with 50+ results and next page")

With progressive search, you can get more accurate search results.

## Considerations

- Enabling progressive search changes the behavior of the search for all enabled facets and filters.
- Progressive search processes a maximum of 50 records at a time, with more than 50 results shown as **50+** on the first result page.
- To optimize search experience while searching, use specific keywords that narrow the search results to a smaller number.
- Selecting a particular facet in filters only shows results for the selected facet, such as tables.
- Since the records are progressively evaluated, the jump to last page button (![Jump to last page button](media/progressive-search/last-page-button.png "Jump to last page button")) is only available if the remaining number of pages in the search result are five or less.

    ![Jump to last page option available when number of pages are five or less](media/progressive-search/jump-last-page.png "Jump to last page option available when number of pages are five or less")

### See also

[Use faceted search](improve-portal-search-faceted-search.md) <br>
[Configure search for additional tables](search-additional-entities.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
