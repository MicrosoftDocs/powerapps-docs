---
title: "Search options in Microsoft Dataverse| MicrosoftDocs"
description: Learn how to to use the different search option
author: mduelae
manager: kvivek
ms.service: powerapps
ms.component: pa-user
ms.topic: conceptual
ms.date: 1/27/2020
ms.subservice: end-user
ms.author: mkaur
ms.custom: ""
ms.reviewer: ""
ms.assetid: 
search.audienceType: 
  - enduser
search.app: 
  - PowerApps
  - D365CE
---

# Compare search options in Microsoft Dataverse

There are three ways to search rows in Dataverse:

-   Dataverse search   
  
-   Quick Find (single-table or multi-table)  

-   Advanced Find

> [!NOTE]
> Multi-table Quick Find is also called Categorized Search. 
  
The following table provides a brief comparison of the three options.

|Functionality|[Dataverse search](relevance-search.md)|[Quick Find](quick-find.md)|[Advanced Find](advanced-find.md)|  
|-------------------|---------------------------|----------------|-------------------|  
|Enabled by default?|No. An administrator must manually enable it.|Yes|Yes|  
|Single-table search scope|Not available in a table grid. You can filter the search results by a table on the results page.|Available in a table grid.|Available in a table grid.|  
|Multi-table search scope|There is no maximum limit on the number of tables you can search. **Note:**  While there is no maximum limit on the number of tables you can search, the Row Type filter shows data for only 10 tables.|Searches up to 10 tables, grouped by a table.|Multi-table search not available.|  
|Search behavior|Finds matches to any word in the search term in any column in the table.|Finds matches to all words in the search term in one column in a table; however, the words can be matched in any order in the column.|Query builder where you can define search criteria for the selected row type. Can also be used to prepare data for export to Office Excel so that you analyze, summarize,or aggregate data, or create PivotTables to view your data from different perspectives.|  
|Searchable columns|Text columns like Single Line of Text, Multiple Lines of Text, Lookups, and Option Sets. Doesn't support searching in columns of Numeric or Date data type.|All searchable columns.|All searchable columns.|  
|Search results|Returns the search results in order of their relevance, in a single list.|For single-table, returns the search results in a table grid. For multi-table, returns the search results grouped by categories, such as accounts, contacts, or leads.|Returns search results of the selected row type with the columns you have specified, in the sort order you have configured.|
|Wildcards (*)|Trailing wildcard supported for word completion.|Leading wildcard supported. Trailing wildcard added by default.|Not supported.|  


[!INCLUDE[footer-include](../includes/footer-banner.md)]