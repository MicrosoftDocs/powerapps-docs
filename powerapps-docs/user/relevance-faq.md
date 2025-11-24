---
title: "FAQ for Dataverse search | MicrosoftDocs"
description: FAQ about Dataverse search
author: shwetamurkute
ms.component: pa-user
ms.topic: faq
ms.date: 11/24/2025
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

## What is Dataverse search?

Dataverse search is the foundation that enables Copilot and in-app search experiences to understand and process business data, helping organizations turn raw information into meaningful insights. Learn more about Dataverse search and its enabled experiences in [What is Dataverse search](relevance-search-benefits.md).

## What is the difference between "On" and "Default" state for Dataverse search?

 The state selected for Dataverse search impacts the ability to use Dataverse data across the enabled experiences for the organization.
 For a better understanding of what each Dataverse search state means, please refer to:
 - [What Dataverse search setting means for global search](relevance-search-benefits.md#what-dataverse-search-setting-means-for-global-search)
 - [What Dataverse search means for generative AI enabled experiences](relevance-search-benefits.md#what-dataverse-search-means-for-generative-ai-enabled-experiences)

## What is the scope of content searched by Dataverse search?

Any file or Dataverse knowledge added to Agents or model-driven apps defines the scope of content that's searched.

![An example of search results on the Contacts tab.](media/search-faq-1.png "An example of search results on the Contacts tab") 

## What are the column types that can be searched in Dataverse search?

The **Find Columns** on a **Quick Find View** define the searchable fields in the Dataverse search index. Text fields such as Single Line of Text and Multiple Lines of Text, Lookups, and Option Sets are searchable. **Find Columns** of all other data types such as Integer, Double are ignored. Learn more in [Select searchable fields and filters for each table](/power-platform/admin/configure-relevance-search-organization#select-searchable-fields-and-filters-for-each-table).

## Why am I not seeing search results from a table that is enabled for Dataverse search?

If a table isn't part of the model-driven app, it is not included in search results. Use the Power Apps app designer to verify that the table is included in that app's components. Make sure that the table has a default Quick Find View created and defined. A default Quick Find View is created with a table, but if it has been removed you need to select the Quick Find View you want and set as the default for your table. Learn more in [Add or edit model-driven app components](../maker/model-driven-apps/add-edit-app-components.md#add-a-component). 

## Can I configure quick actions to show or hide certain commands?
Yes, you can with version 9.2.21034.00126 or later. Quick actions are a subset of a table's grid-level command set. You can configure them by using ribbon rules.
For more information on how to configure quick actions, see [Configure Dataverse search to improve search results and performance](/power-platform/admin/configure-relevance-search-organization#configure-quick-actions).

## Why are results that appear in suggestions sometimes not seen on the results page?

Suggestions are quick results based on a search performed on the primary column of a table. This feature is enabled for Dataverse search in model-driven apps. Learn more in [Inline suggestions](relevance-search.md#inline-suggestions)

When you navigate to the results page, the search terms are treated as the complete search query. The search performs many more types of matching to display a more comprehensive set of results.

## Can I configure the order of tables appearing in the search results page?

The order of tables in the **Top results** tab and in the horizontal list of tabs is based on the ranking and relevance of search results for that search term. You can make results from a particular table appear at the top by including the table name in the search term. For example, searching for **account fabrikam** would, in most cases, rank result records that have the term **fabrikam** of type **account** higher than result records that have the term **fabrikam** of a type other than **account**.

## Can I see search results from SharePoint files and documents through Dataverse search?

Currently, Dataverse search searches your data in Microsoft Dataverse only. It doesn't search SharePoint files and documents, including the names of the files and the content in the files. It also doesn't search objects of **File** data type in Dataverse.

## Why am I unable to view information for party list fields like To, From, and CC in full results?

Party list fields are special fields. Dataverse search doesn't support them, and it doesn't include them in the search results page.

## Why don't returns support HTML formatting for memo data types?

Dataverse search doesn't return HTML formatting for memo types to optimize the UI experience.

## Why aren't columns enabled for Dataverse search after adding them to a quick find view?

Columns are enabled for Dataverse search only if a quick find view is set as the default view. For more information on how to set a default view, see [Specify a default view for a table](../maker/model-driven-apps/specify-default-views.md#specify-a-default-view-for-a-table).

## Why doesn't search on the OwnerID attribute work when I enable search on it?

The search and suggest operations don't have access to data from the Owner column. Learn more in [Types of columns](../maker/data-platform/types-of-fields.md).

## Why doesn't search on the RegardingObjectId attribute work when I enable search on it?

Search doesn't support polymorphic lookup attributes. The RegardingObjectId attribute in activity tables like email and task is a polymorphic lookup attribute.

## How is the Dataverse search API throttled?

When you use the Dataverse search API, throttling limits restrict you to one request per second for each user. Additionally, each organization can make up to 150 requests per minute.

## What attribute types does indexing support?

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

## What attribute types are eligible for facet list fields?

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

Dataverse search strives to maintain functional parity between our commercially available services and those available through our US Government clouds. It's available in US Government Community Cloud (GCC), US GCC High, and Department of Defense (DoD).

## How is Dataverse search reported?

In addition to the database and file storage, Dataverse search includes the indexes that power different experiences. These indexes support search and generative AI across structured or tabular, as well as unstructured data stored in Dataverse, including files.
Dataverse search storage appears at the environment level in the `DataverseSearch` table, previously called `RelevanceSearch`.  
Learn more in [Dataverse capacity-based storage](/power-platform/admin/capacity-storage).

## What actions can admins take to manage Dataverse search?

Depending on the experience that uses Dataverse search and its usage, consumption size might increase more drastically. To learn more about managing Dataverse search, see [What is Dataverse search](relevance-search-benefits.md#what-actions-can-makers-or-admins-take-to-manage-dataverse-search-efficiently).

## What happens if Dataverse search is turned off?

If you set Dataverse search to **Off** for the environment, you can't use the search capability in the Power Apps navigation bar or any generative AI experience that relies on Dataverse, like uploaded files or using OneDrive or SharePoint files in Microsoft Copilot Studio agents, among other experiences. For details about these limitations, see [What is Dataverse search](relevance-search-benefits.md#what-happens-if-dataverse-search-is-turned-off).

### See also

[What is Dataverse search?](relevance-search-benefits.md)<br/>
[Search for tables and rows using Dataverse search](relevance-search.md)<br/>
[Configure facets and filters](facets-and-filters.md)

[!INCLUDE[footer-include](../includes/footer-banner.md)]
