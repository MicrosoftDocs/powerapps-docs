---
title: "Frequently asked questions about Relevance Search MicrosoftDocs"
description: Frequently asked questions about Relevance Search
author: mduelae
manager: kvivek
ms.service: powerapps
ms.component: pa-user
ms.topic: conceptual
ms.date: 2/8/2020
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

# Frequently asked questions about Relevance Search

## What is the scope of content that is searched when a run a search using Relevance Search?

The scope of content that is searched is defined by your administrator. An administrator can configure the tables and specific columns in the table that can be searched. The specific columns that are searched on for a table are indicated on the results page under each tab. 

![Example of search results](media/search-faq-1.png)  


## Why are results that appear in suggestions sometimes not seen in the results page? 

Suggestions are quick results based on a search performed on the primary column of a table. This enabled for Relevance Search in model-driven apps. For more information, see [Inline suggestions](https://docs.microsoft.com/powerapps/user/relevance-search#inline-suggestions).

When you navigate to the results page, the search terms are treated as the complete search query and a lot more types of matching are performed to display a more comprehensive set of results. 

## Can I see search results from SharePoint files and documents through Relevance Search? 

Currently, Relevance Search searches on your data in Microsoft Dataverse only. SharePoint files and documents including the names of the files and the content in the files are not searched. Objects of file data type in Microsoft Dataverse are also not searched on.

## Why am I unable to view information for party list fields like To, From, CC and in full results? 

Party list fields are special fields that are not searchable and viewable in the results page. 

## Can I configure quick actions to show or hide certain commands?

The [quick actions](https://docs.microsoft.com/powerapps/user/relevance-search#quick-actions-preview) are currently a subset of a table's grid level command set. They cannot be configured. However, we are working to enabled this functionality in a future release. 

Thank you,



## See also

[What is Relevance Search](relevance-search-benefits.md)<br/>
[Search for tables and rows using Relevance Search](relevance-search.md)<br/>
[Configure facets and filters](facets-and-filters.md)



[!INCLUDE[footer-include](../includes/footer-banner.md)]