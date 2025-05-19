---
title: "FAQ for Dataverse search | MicrosoftDocs"
description: FAQ about Dataverse search
author: shwetamurkute
ms.component: pa-user
ms.topic: faq
ms.date: 05/06/2025
ms.subservice: end-user
ms.author: smurkute
ms.custom: ""
ms.reviewer: smurkute
ms.assetid: 
search.audienceType: 
  - enduser
contributors:
- mspilde
- manish1604
- prdeka
- AnikaMD
- JimDaly
---

# Frequently asked questions about Dataverse search

## What is the scope of content searched by Dataverse search?

Any file or Dataverse knowledge added to Agents or model-driven apps defines the scope of content that's searched.

![An example of search results on the Contacts tab.](media/search-faq-1.png "An example of search results on the Contacts tab") 

## What are the Column Types that can be searched in Dataverse Search?

The **Find Columns** on a **Quick Find View** define the searchable fields in the Dataverse search index. Text fields such as Single Line of Text and Multiple Lines of Text, Lookups, and Option Sets are searchable. **Find Columns** of all other data types such as Integer, Double are ignored. For more information, see [Select searchable fields and filters for each table](/power-platform/admin/configure-relevance-search-organization#select-searchable-fields-and-filters-for-each-table).

## Why am I not seeing search results from a table that is enabled for Dataverse search?

If a table isn't part of the model-driven app, it's not included in search results. Use the Power Apps app designer to verify that the table is included in that app's components. Make sure that the table has a default Quick Find View created and defined. A default Quick Find View is created with a table, but if it has been removed you need to select the Quick Find View you want and set as the default for your table. For more information, see [Add or edit model-driven app components](../maker/model-driven-apps/add-edit-app-components.md#add-a-component). 

## Can I configure quick actions to show or hide certain commands?
Yes, you can with version 9.2.21034.00126 or later. Quick actions are a subset of a table's grid-level command set. They can be configured using ribbon rules
For more information on how to configure quick actions, see [Configure Dataverse search to improve search results and performance](/power-platform/admin/configure-relevance-search-organization#configure-quick-actions).

## Why are results that appear in suggestions sometimes not seen on the results page?

Suggestions are quick results based on a search performed on the primary column of a table. This is enabled for Dataverse search in model-driven apps. More information: [Inline suggestions](relevance-search.md#inline-suggestions)

When you navigate to the results page, the search terms are treated as the complete search query and a lot more types of matching are performed to display a more comprehensive set of results.

## Can I configure the order of tables appearing in the search results page?

The order of tables in the **Top results** tab and in the horizontal list of tabs is based on the ranking and relevance of search results for that search term. You can make results from a particular table appear at the top by including the table name in the search term. For example, searching for **account fabrikam** would, in most cases, rank result records that have the term **fabrikam** of type **account** higher than result records that have the term **fabrikam** of type other than **account**.

## Can I see search results from SharePoint files and documents through Dataverse search?

Currently, Dataverse search searches your data in Microsoft Dataverse only. SharePoint files and documents, including the names of the files and the content in the files, aren't searched. Objects of **File** data type in Dataverse are also not searched on.

## Why am I unable to view information for party list fields like To, From, and CC in full results?

Party list fields are special fields. They're not supported in Dataverse search, nor are they included in the search results page.

## How come returns don't support HTML formatting for memo data types?

Dataverse search doesn't return HTML formatting for memo types to optimize the UI experience.

## Why columns aren't enabled for Dataverse search after adding to a quick find view?

Columns are enabled for Dataverse search only if a quick find view is set as the default view. For more information on how to set a default view, see [Specify a default view for a table](../maker/model-driven-apps/specify-default-views.md#specify-a-default-view-for-a-table).

## Why does searching on the OwnerID attribute not work when search is enabled on it?

Data from the Owner column isn't available for search and suggest operations. More information: [Types of columns](../maker/data-platform/types-of-fields.md)

## Why doesn't search on the RegardingObjectId attribute work when search is enabled on it?

Search isn't supported on polymorphic lookup attributes. The RegardingObjectId attribute in activity tables like email and task is a polymorphic lookup attribute.

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

## How can I use the search API?

[Developer's guide: Search for Dataverse records using the API](../developer/data-platform/search/overview.md)

## Does Dataverse search support US Government clouds?
Dataverse search strives to maintain functional parity between our commercially available services and those available through our US Government clouds. It's available in US Government Community Cloud (GCC), US GCC High and Department of Defense (DoD).

### See also

[What is Dataverse search?](relevance-search-benefits.md)<br/>
[Search for tables and rows using Dataverse search](relevance-search.md)<br/>
[Configure facets and filters](facets-and-filters.md)

[!INCLUDE[footer-include](../includes/footer-banner.md)]
