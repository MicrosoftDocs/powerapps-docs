---
title: "Search options in Common Data Service| MicrosoftDocs"
ms.custom: ""
author: mduelae
manager: kvivek
ms.service: powerapps
ms.component: pa-user
ms.topic: conceptual
ms.date: 1/27/2020
ms.author: mduelae
ms.custom: ""
ms.reviewer: ""
ms.assetid: 
search.audienceType: 
  - enduser
search.app: 
  - PowerApps
  - D365CE
---

# Compare search options in Common Data Service

There are three ways to search records in Common Data Service:

-   Relevance Search   
  
-   Quick Find (single-entity or multi-entity)  

-   Advanced Find

> [!NOTE]
> Multi-entity Quick Find is also called Categorized Search. 
  
The following table provides a brief comparison of the three options.

|Functionality|[Relevance Search](relevance-search.md)|[Quick Find](quick-find.md)|[Advanced Find](advanced-find.md)|  
|-------------------|---------------------------|----------------|-------------------|  
|Enabled by default?|No. An administrator must manually enable it.|Yes|Yes|  
|Single-entity search scope|Not available in an entity grid. You can filter the search results by an entity on the results page.|Available in an entity grid.|Available in an entity grid.|  
|Multi-entity search scope|There is no maximum limit on the number of entities you can search. **Note:**  While there is no maximum limit on the number of entities you can search, the Record Type filter shows data for only 10 entities.|Searches up to 10 entities, grouped by an entity.|Multi-entity search not available.|  
|Search behavior|Finds matches to any word in the search term in any field in the entity.|Finds matches to all words in the search term in one field in an entity; however, the words can be matched in any order in the field.|Query builder where you can define search criteria for the selected record type. Can also be used to prepare data for export to Office Excel so that you analyze, summarize,or aggregate data, or create PivotTables to view your data from different perspectives.|  
|Searchable fields|Text fields like Single Line of Text, Multiple Lines of Text, Lookups, and Option Sets. Doesn't support searching in fields of Numeric or Date data type.|All searchable fields.|All searchable fields.|  
|Search results|Returns the search results in order of their relevance, in a single list.|For single-entity, returns the search results in an entity grid. For multi-entity, returns the search results grouped by categories, such as accounts, contacts, or leads.|Returns search results of the selected record type with the columns you have specified, in the sort order you have configured.|
|Wildcards (*)|Trailing wildcard supported for word completion.|Leading wildcard supported. Trailing wildcard added by default.|Not supported.|  
