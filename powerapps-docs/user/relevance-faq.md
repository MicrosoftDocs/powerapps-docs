---
title: "FAQ for Dataverse search | MicrosoftDocs"
description: FAQ about Dataverse search
author: sericks007
ms.component: pa-user
ms.topic: conceptual
ms.date: 08/02/2023
ms.subservice: end-user
ms.author: sericks
ms.custom: ""
ms.reviewer: sericks
ms.assetid: 
search.audienceType: 
  - enduser
contributors:
- mspilde
- manish1604
- prdeka
- AnikaMD 
---

# Frequently asked questions about Dataverse search

## What is the scope of content searched by Dataverse search?

Your administrator defines the scope of content that's searched. An administrator can configure the tables, and specific columns in the tables, that can be searched. The specific columns that were searched for a table are indicated on the results page on each tab.

![An example of search results on the Contacts tab.](media/search-faq-1.png "An example of search results on the Contacts tab") 

## Why am I not seeing search results from a table that is enabled for Dataverse search?

If a table isn't part of the model-driven app, it's not included in search results. Use the Power Apps app designer to verify that the table is included in that app's components. For more information, see [Add or edit model-driven app components](../maker/model-driven-apps/add-edit-app-components.md#add-a-component).


## Can I configure quick actions to show or hide certain commands?
Yes, you can with version 9.2.21034.00126 or later. Quick actions are a subset of a table's grid-level command set. They can be configured using ribbon rules
For more information on how to configure quick actions, see [Configure Dataverse search to improve search results and performance](/power-platform/admin/configure-relevance-search-organization#configure-quick-actions).

## Why are results that appear in suggestions sometimes not seen on the results page?

Suggestions are quick results based on a search performed on the primary column of a table. This is enabled for Dataverse search in model-driven apps. More information: [Inline suggestions](relevance-search.md#inline-suggestions)

When you navigate to the results page, the search terms are treated as the complete search query and a lot more types of matching are performed to display a more comprehensive set of results.

## Can I configure the order of tables appearing in search results page?

The order of tables in the **Top results** tab and in the horizontal list of tabs is based on the ranking and relevance of search results for that search term. You can make results from a particular table appear at the top by including the table name in the search term. For example, searching for **account fabrikam** would, in most cases, rank result records that have the term **fabrikam** of type **account** higher than result records that have the term **fabrikam** of type other than **account**.

## Can I see search results from SharePoint files and documents through Dataverse search?

Currently, Dataverse search searches your data in Microsoft Dataverse only. SharePoint files and documents, including the names of the files and the content in the files, aren't searched. Objects of **File** data type in Dataverse are also not searched on.

## Why am I unable to view information for party list fields like To, From, and CC in full results?

Party list fields are special fields that aren't searchable or viewable in the results page. 

## How come returns don't support HTLM formatting for memo data types?

Dataverse search doesn't return HTML formatting for memo types to optomize the UI experience.

## Why columns aren't enabled for Dataverse search after adding to a quick find view?

Columns are enabled for Dataverse search only if a quick find view is set as the default view. For more information on how to set a default view, see [Specify a default view for a table](../maker/model-driven-apps/specify-default-views.md#specify-a-default-view-for-a-table).

## Why does searching on the OwnerID attribute not work when search is enabled on it?

Data from the Owner column isn't available for search and suggest operations. More information: [Types of columns](../maker/data-platform/types-of-fields.md)

## How is the Dataverse search API throttled?

When using the Dataverse search API, there's a throttling limit of one request per second for each user. Additionally, there's a throttling limit of 150 requests per minute per organization.

## What are the supported attribute types for indexing?

- BigInt
- Boolean
- Customer
- DateTime
- Decimal
- Double
- EntityName
- Integer
- Lookup
- Memo
- Money
- Owner
- Picklist
- State
- Status
- String
- Uniqueidentifier
- Virtual (only for MultiSelectPicklistType and FileType)

## What are the eligible attribute types for facet list fields?

- Lookup 
- DateTime 
- Money
- Picklist
- Integer
- Customer
- Decimal
- MultiSelectPicklist
- State
- Status

### See also

[What is Dataverse search?](relevance-search-benefits.md)<br/>
[Search for tables and rows using Dataverse search](relevance-search.md)<br/>
[Configure facets and filters](facets-and-filters.md)

[!INCLUDE[footer-include](../includes/footer-banner.md)]

