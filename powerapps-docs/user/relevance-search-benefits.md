---
title: "What is relevance search and it's benefits| MicrosoftDocs"
description: What is relevance search and it's benefits.
author: mduelae
manager: kvivek
ms.service: powerapps
ms.component: pa-user
ms.topic: conceptual
ms.date: 2/3/2021
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

# What is relevance search 

Relevance search helps you find what you need to complete your task in model-driven Power Apps. It delivers fast and comprehensive results across multiple tables, in a single list, sorted by relevance. 
  
Relevance search brings the following enhancements and benefits:  

- Improved performance compared to Categorized search.  
  
- Finds matches to any word in the search term in any column in the table, compared to quick find where all words from the search term must be found in one column. 

- Finds matches that include inflectional words like **stream**, **streaming**, or **streamed**.  
  
- Returns results from all searchable tables in a single list sorted by relevance, so the better the match, the higher the result appears in the list. A match has a higher relevancy if more words from the search term are found in close proximity to each other. The smaller the amount of text where the search words are found, the higher the relevancy. For example, if you find the search words in a company name and address, it might be a better match than finding the same words in a long article, far apart from each other.
  
- Highlights matches in the results list. When a search term matches a term in a row, the term appears as bold and italicized text in your search results. 

    > [!NOTE]
    > - Certain words that are very commonly used in a language (like **the** or **a**) are ignored during search, because they don't help uniquely identify rows. Because they're ignored during search, these words are also not highlighted in results.
    > - Highlighted terms are often returned as a portion of the full value in a column because only the matched terms are highlighted.
    > - Highlighted results are shown in context of the sentence that it is a part of. This may result in unexpected behavior, when a column has a period (.) because the period is considered as the end of sentence. Due this behavior, you may get results where part of the matched column is truncated.
    
- Includes search results for text in a document that's stored in Microsoft Dataverse, including text in notes, email attachments, or appointments. The following file formats are supported for search: PDF, Microsoft Office documents, HTML, XML, ZIP, EML, plain text, and JSON. Note, that File data type is not supported
  
- Enables you to search for rows that are shared with you and rows that you own.  
  
  > [!NOTE]
  >  Hierarchical security models aren't supported. Even if you see a row in Dataverse because you have access to it through hierarchical security, you won't see the result in relevance search.  
  
- Lets you also search for choices and lookups. For example, let's say you want to find a retail store account that has **Pharmaceuticals** in the name. When you search for **Pharmaceutical Retail**, you'll find the result because there's a match to the Industry column, which is a searchable option set.

  > [!NOTE]
  > - Relevance search is text-based, and can search only on columns of type Single Line of Text, Multiple Lines of Text, Option Sets, or Lookups. It doesn't support searching in columns of Numeric, Date, or File data type.
  
- Allows you to use syntax in your search term to get the results you want. For example, type **car silver 2-door** to include matches for any word in the search term in the search results. Type **car+silver+2-door** to find only matches that include all three words. Type **car&#124;silver&#124;2-door** to  get results that contain **car** or **silver** or **2-door**, or all three words. For more information about syntax you can use in your search queries, see [Search across table data using relevance search](https://docs.microsoft.com/powerapps/developer/data-platform/webapi/relevance-search).
  
  > [!NOTE]
  > Relevance search is configured to require matches to any (instead of all) of the criteria in a query, which might bring about results that are different from your expectations. This is especially true when Boolean operators are included in the query.
