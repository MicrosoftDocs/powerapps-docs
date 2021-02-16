---
title: "Quick Find| MicrosoftDocs"
description: Learn how to use quick find to search for records
author: mduelae
manager: kvivek
ms.service: powerapps
ms.component: pa-user
ms.topic: conceptual
ms.date: 1/28/2020
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

## Single-table quick find

Single-table quick find is used to find rows of only one type. This search option is available from within a view. 

   > [!div class="mx-imgBorder"]
   > ![Single-table Quick Find](media/single-quick-find-search-box.png "Single-table quick find search box") 

## Multiple-table quick find (categorized search)

Multiple-table quick find is also known as categorized search. 

1.  To start a categorized search, from the top nav bar, select **Search**.  

     > [!div class="mx-imgBorder"]
     > ![Global Search Button](media/global-search-button.png "Global search")
  
2.  Type your search words in the search box, and then select **Search**. Categorized search returns results grouped by table types, such as accounts or contacts.

     > [!div class="mx-imgBorder"]
     > ![Categorized Search Results](media/categorized-search-results.png "Categorized search results page") 

With categorized search, you can search for rows that begin with a specific word or use a wildcard character.
  
- **Begins with**: Results include rows that begin with a specific word. For example, if you want to search for "Alpine Ski House," type **alp** in the search box; if you type **ski**, the row won't show up.  
  
- **Wildcard**: For example, *ski or *ski\*. 

  > [!NOTE]
  >  Using a wildcard at the beginning of your quick find (single or multiple-table) search query might result in slower performance.
  
## Filter categorized search results 
  
-   To filter results by a row type, choose a row type from the **Filter with** list. 

    > [!div class="mx-imgBorder"]
    > ![Filtering Categorized Search Results](media/filter-categorized-search-results.png "Filtering categorized search results")  

  
-   To search all row types, choose **None** from the **Filter with** list.  


[!INCLUDE[footer-include](../includes/footer-banner.md)]