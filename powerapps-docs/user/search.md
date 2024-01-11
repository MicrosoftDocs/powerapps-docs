---
title: Compare search options in Microsoft Dataverse
description: Learn how to to use the different search option
author: sericks

ms.component: pa-user
ms.topic: conceptual
ms.date: 05/10/2023
ms.subservice: end-user
ms.author: sericks
ms.custom: ""
ms.reviewer: sericks
ms.assetid: 
search.audienceType: 
  - enduser
---

# Compare search options in Microsoft Dataverse

There are three ways to search rows in Dataverse:

-   Dataverse search   
  
-   Quick Find (single-table or multi-table)  

-   Advanced Find

> [!NOTE]
> Multi-table Quick Find is also called Categorized Search.
> For a given query, the search results from the three options below might be different due to the searchs cope and search behavior.
  
The following table provides a brief comparison of the three options.

|Functionality|[Dataverse search](relevance-search.md)|[Quick Find](quick-find.md)|[Advanced Find](advanced-find.md)|  
|-------------------|---------------------------|----------------|-------------------|  
|Enabled by default?|Yes. </br> **Note:** For non-production environments an administrator must manually enable it.|Yes, for the table grid. </br> No, for multiple-table quick find (categorized search). An administrator must first disable Dataverse search before multiple-table grid find can be enabled.|Yes|  
|Single-table search scope|Not available in a table grid. You can filter the search results by a table on the results page.|Available in a table grid.|Available in a table grid.|  
|Multi-table search scope|There is no maximum limit on the number of tables you can search.|Searches up to 10 tables, grouped by a table.|Multi-table search not available.|  
|Search behavior|Finds matches to any word in the search term in any column in the table.|Finds matches to all words in the search term in one column in a table; however, the words can be matched in any order in the column.|Query builder where you can define search criteria for the selected row type. Can also be used to prepare data for export to Office Excel so that you analyze, summarize,or aggregate data, or create PivotTables to view your data from different perspectives.|  
|Searchable columns|Text columns like Single Line of Text, Multiple Lines of Text, Lookups, and Option Sets. Doesn't support searching in columns of Numeric or Date data type.|All searchable columns.|All searchable columns.|  
|Search results|Returns the search results in order of their relevance, in a single list.|For single-table, returns the search results in a table grid. For multi-table, returns the search results grouped by categories, such as accounts, contacts, or leads.|Returns search results of the selected row type with the columns you have specified, in the sort order you have configured.|
|Wildcards (*)|Trailing wildcard supported for word completion.|Leading wildcard supported. Trailing wildcard added by default.|Leading wildcard supported.|  


[!INCLUDE[footer-include](../includes/footer-banner.md)]
