---
title: "Frequently asked questions about Relevance Search MicrosoftDocs"
description: Frequently asked questions about Relevance Search
author: mduelae
manager: kvivek
ms.service: powerapps
ms.component: pa-user
ms.topic: conceptual
ms.date: 2/5/2020
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

## What is the scope of content that is searched on by Relevance Search?

The scope of content that is searched on is specified by the administrator who can configure the tables and specific columns in the table to be searched on. The specific columns that are searched on for a table are indicated on the results page under each tab. 

![Example of search results](media/search-faq-1.png)  


## Why are results that appear in suggestions sometimes not seen in the results page? 

Suggestions are quick results based on a search performed on the primary column of a table that is both enabled for Relevance Search and included in the model-driven app. For more information see [Inline suggestions](https://docs.microsoft.com/powerapps/user/relevance-search#inline-suggestions).

When you navigate to the results page, the entered search term is treated as the complete search query and a lot more types of matching are performed to display a more comprehensive set of results. 

## Can I see search results from SharePoint files and documents through Relevance Search? 

Currently, Relevance Search searches on your data in Microsoft Dataverse only. So, SharePoint files and documents (both names of the files and the content in those files) are not searched on. Objects of File data type in Microsoft Dataverse are also not searched on. Please follow our blog for more updates on this. 

## Why am I unable to view information for party list fields like To, From, CC and in full results? 

Party list fields are special fields that are not searchable and viewable in the results page. 

## See also

[What is Relevance Search](relevance-search-benefits.md)<br/>
[Use Relevance Search to search for rows](relevance-search.md)<br/>
[Configure facets and filters](facets-and-filters.md)

