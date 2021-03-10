---
title: "Quick Find| MicrosoftDocs"
description: Learn how to use quick find to search for records
author: mduelae
manager: kvivek
ms.service: powerapps
ms.component: pa-user
ms.topic: conceptual
ms.date: 3/10/2021
ms.author: mkaur
ms.custom: ""
ms.reviewer: ""
ms.assetid: 
search.audienceType: 
  - enduser
search.app: 
  - PowerApps
  - D365CE
searchScope:
  - D365-App-msdynce_saleshub
  - D365-Entity-activity
  - D365-UI-*
  - Power Platform
  - Power Apps
---

# Using quick find to search for rows

Quickly search across multiple tables at the same time and find the information that you're looking for. When you enter a search term the system finds matches to all words in the search term in one column in a table. The words can be matched in any order in the column.

With categorized search, you can search for rows that begin with a specific word or use a wildcard character.
  
- **Begins with**: Results include rows that begin with a specific word. For example, if you want to search for "Alpine Ski House," type **alp** in the search box; if you type **ski**, the row won't show up.  
  
- **Wildcard**: For example, *ski or *ski\*. 

  > [!NOTE]
  >  Using a wildcard at the beginning of your quick find (single or multiple-table) search query might result in slower performance.

## Single table quick find 

Use single-table quick to find row in a view.

   > [!div class="mx-imgBorder"]
   > ![Single-table Quick Find](media/quick-find-view-only.gif "Single-table quick find search box") 

## Multiple-table quick find (categorized search)

Multiple-table quick find searches up to 10 tables and returns the search results grouped by table.

1.  To start a categorized search, from the top nav bar, select **Search**.  

     > [!div class="mx-imgBorder"]
     > ![Global Search Button](media/global-search-button.png "Global search")
  
2.  Type your search words in the search box, and then select **Search**. The search returns results grouped by table. 

     > [!div class="mx-imgBorder"]
     > ![Categorized Search Results](media/categorized-search-results.png "Categorized search results page") 

 3. Filter results by a row type, choose a row type from the **Filter with** list. To search all row types, choose **None** from the **Filter with** list.  

    > [!div class="mx-imgBorder"]
    > ![Filtering Categorized Search Results](media/filter-categorized-search-results.png "Filtering categorized search results")  

  



[!INCLUDE[footer-include](../includes/footer-banner.md)]
