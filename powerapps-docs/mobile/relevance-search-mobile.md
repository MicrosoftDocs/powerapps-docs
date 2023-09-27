---
title: Use Dataverse search for model-driven apps in the Power Apps mobile app 
description: How to use Dataverse search for model-driven apps using your mobile app.
author: trdehove

ms.component: pa-user
ms.topic: quickstart
ms.date: 08/10/2021
ms.subservice: mobile
ms.author: trdehove
ms.custom: ""
ms.reviewer: sericks
ms.assetid: 
search.audienceType: 
  - enduser
searchScope:
  - "Power Apps"
---

# Use Dataverse search for model-driven apps in the Power Apps mobile app 


You can quickly find the information that you're looking for by using Dataverse search. The Dataverse search experience delivers fast and comprehensive results across multiple tables, in a single list, sorted by relevance.

Dataverse search is already available when you're using a model-driven app in a web browser. The functionality is the same in Power Apps Mobile, but it works a little differently. More information: [Search for tables and rows by using Dataverse search](../user/relevance-search.md)

Before you begin using Dataverse search, the new experience needs to be enabled by the administrator for your organization. More information: [Enable Dataverse search](/power-platform/admin/configure-relevance-search-organization#enable-relevance-search)

When Dataverse search is turned on, it becomes your default and only global search experience for all of your model-driven apps. You won't be able to switch to [quick find search also known as categorized search](../user/quick-find.md).

  > [!div class="mx-imgBorder"]
  > ![Demonstration of how Dataverse search works in a model-driven app running on Power Apps Mobile.](media/powerapps-mobile-rel-search.gif "Demonstration of how Dataverse search works in a model-driven app running on Power Apps Mobile")

 

## Run a search

View suggested search results inline as you type, minimizing keystrokes and simplifying page navigation.

1. Select the search button. 

   > [!div class="mx-imgBorder"]
   > ![Select the search button.](media/search-on-mobile-1.png "Select the search button") 
  
2. Enter the words you want to search for in the search box.  

   > [!div class="mx-imgBorder"]
   > ![Enter search text.](media/search-on-mobile-2.png "Enter search text") 
  
3. As you enter search text, rows that match your text begin to appear.

   > [!div class="mx-imgBorder"]
   > ![See suggested results as you type.](media/suggested-results.png "See suggested results as you type")



## Early access: Use the barcode scanner

 [!INCLUDE [cc-beta-prerelease-disclaimer](../includes/cc-beta-prerelease-disclaimer.md)]
 
 If you're on [early access](/power-platform/admin/opt-in-early-access-updates), you can use the barcode scanner to look up rows. The scanner automatically detects a barcode, a QR code, or a data-matrix code.
 
 You also enter text in the search box such as **contoso** and then use the barcode scanner to scan a barcode, such as **12345**. In this case, the system will search for **contoso12345**.
 
 1. To use the barcode scanner, select the search button.
 2. Select the barcode scanner button and then scan your item.

    > [!div class="mx-imgBorder"]
    > ![Select the barcode scanner.](media/bar-code-scanner.png "Barcode scanner")
 

## View search results

Search results are ranked and grouped by table.

![Search results page.](media/search-results-page.png "Search results page") 
  
  Legend
  
  1. **Search box**: Enter the words you want to search for.
  2. **Top results**: This tab shows the rows that best match the search query. 
  3. **Table-specific tab**: To narrow your search results to a specific table, select the table tab.
  4. **Filter**: Refine the search results by using filters. When you select filters, the number of tables that have been filtered on appears next to the filter option.
  5. **See all**: Up to three rows will appear; if there are more, select **See all**.
  
## Filter search results
  
Use filters to drill into and explore the results of your current search without having to repeatedly refine your search terms. Immediately after you perform a search, you can filter by **Owner**, **Created On**, or **Modified On**.

![Filter results page.](media/filter-results-page.png "Filter results page") 
  
  Legend
  
  1. **Back**: Go back to the search results screen.
  2. **Filter**: Select a filter type to filter the search results.
  3. **Clear all**: Clear all filters and return to the search results screen.


[!INCLUDE[footer-include](../includes/footer-banner.md)]
