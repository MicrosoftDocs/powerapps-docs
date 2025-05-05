---
title: "FAQ for Dataverse search | MicrosoftDocs"
description: FAQ about Dataverse search
author: shwetamurkute
ms.component: pa-user
ms.topic: conceptual
ms.date: 03/13/2025
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

## What makes Dataverse search?

Dataverse search consists of two separate indexes that power different experiences.

- **Dataverse search structured index**: This is the index powering experiences across structured or tabular data stored in Dataverse. Examples of this index include search indexes over tables Dataverse like Accounts, Contact, custom tables, Dataverse relevance search, and others.
- **Dataverse search unstructured index**: This is the index powering experiences across unstructured data stored in Dataverse. Examples of this index include search indexes over files uploaded in Microsoft Copilot Studio custom agents, customer service agents, and others.

## Experiences enabled by Dataverse search
Multiple features within the Power Platform are enabled via Dataverse search, namely the Copilot indexes. These experiences include:

### Microsoft Copilot Studio Agents
1.	[Add Files as a knowledge source](/microsoft-copilot-studio/knowledge-add-file-upload)
2.	[Add Dataverse as a knowledge source](/microsoft-copilot-studio/knowledge-add-dataverse)
3.	[Virtual Agents](/microsoft-copilot-studio/guidance/cux-types#virtual-agents)

### Dynamics 365 Copilots

4. [Sales Copilot](/dynamics365/sales/copilot-overview)
5. [Customer Service Copilot](/dynamics365/customer-service/administer/copilot-enable-summary)
6. [Contact Center Copilot](/dynamics365/contact-center/administer/configure-copilot-features)
7. [Field Service Copilot](/dynamics365/field-service/copilot-side-pane)

### Power Apps – Model-Driven Apps

8. [Copilot Chat](/power-apps/maker/model-driven-apps/add-ai-copilot)
9. [Dataverse search](/power-platform/admin/configure-relevance-search-organization)

### Experiences across the Power Platform

10. [AI Prompts in Power Apps / Power Automate](/microsoft-copilot-studio/nlu-prompt-node)
11. [AI Prompts in Microsoft Copilot Studio](/microsoft-copilot-studio/nlu-prompt-node)
12. [Power Apps / Power Automate - Custom AI Prompts](/ai-builder/create-a-custom-prompt)

## How can I find out how much storage is consumed by Dataverse search?
Storage used by Dataverse search is already reported and charged at the Environment level as a table called “RelevanceSearch” and it's charged by its GB capacity. We're enhancing the capabilities and adjusting the billing of the existing Dataverse search with improved semantic Copilot indexing, where generative AI features like Copilot will become dependent on, to promote consistency across the Dataverse search and its enhanced experiences.

> [!Note]
> Dataverse search will be turned **On** if you happen to use any of the above features in the existing environment (and for any new production environment) and **Default** by default for any other scenario or new environment.
It's recommended to have Dataverse search turned on so users can enjoy a superior search experience in model-driven apps and leverage the benefits of generative AI capabilities. Environment admins have the option to opt out of this feature for the purpose of managing their environments by selecting the option **Off**.

To learn more about how Dataverse search is reported and managed, see: [Configure Dataverse Search](/power-platform/admin/configure-relevance-search-organization)


## Where can I see how much storage is consumed by Dataverse search?

Storage consumed by Dataverse search was already reported at the Environment level as a table called “RelevanceSearch”. Now, this table is been available for both Database and File storage consumption and renamed to match accordingly:
- **DataverseSearch-StructuredIndex** for Database storage indexing 
-	**DataverseSearch-UnstructuredIndex** for Files storage indexing.

#Respectively, Dataverse search is reported as part of database and files storage consumption in the **Summary** tab. Dataverse search can also be viewed in the **Environment** report in Power Platform admin center or **Capacity** report:

-	New admin center: **Licensing > Capacity add-ons > Dataverse** tab (Select **Chart** icon)
-	Classic admin center: **Resources > Capacity > Dataverse** tab 
-	New admin center: **Licensing > Dataverse > Environments** tab (Table view in main page) 
-	Classic admin center: **Billing > Licenses > Dataverse > Environment** tab 

### What entitlements are consumed by Dataverse search?

Dataverse search consumes against the [Dataverse entitlements available within your tenant](/power-platform/admin/whats-new-storage).
- Dataverse search-structured index consumption counts towards Dataverse database capacity
-	Dataverse search unstructured index consumption counts towards Dataverse file capacity

## How much will Dataverse search cost?

Dataverse search is charged at the same rate as Database Capacity and File Capacity, respectively, based on the content storage consumption. Content storage consumption doesn't include the storage for the Dataverse indexed data.
- Dataverse search = Database capacity + Files Capacity (Measured in GBs)

### When does Dataverse search start getting consumed against my storage entitlements?

Starting April 7, 2025, Dataverse search starts drawing from Dataverse storage entitlements as detailed above.

> [! mportant]
> Dataverse search counts towards the different storage entitlements you have in the tenant. It's recommended to manage your storage space. Add storage to your environment.
## What actions can Admins take?

To ensure optimal operations for the organization, Admins with the proper permissions can either: increase capacity storage or reduce Dataverse search by performing all the below
1.	Go to the Power Platform Admin Center and turn off Copilot experiences in model-driven apps 
2.	Disable Copilot experiences in Microsoft Copilot Studio
3.	Removing knowledge in Microsoft Copilot Studio
4.	Disable Copilot in Dynamics 365 applications
5.	Disable AI Prompts
6.	Go to the Power Platform Admin Center and turn Dataverse search “Off”: FAQ for Dataverse search - Power Apps | Microsoft Learn. It's recommended not to perform this as it would directly impact all dependent generative AI experiences in your different applications, and all users using them.

## Turning off Dataverse search

If this feature is turned off, all indexed Dataverse data will be deleted, and the experiences that depend on it are limited or unusable for all users of those experiences, which include search and AI conversational capabilities. 

Environment admins have 12 hours to turn the feature back on with no implications:

### During 12 hours:
-	All Dataverse indexed data is stored.
-	Dataverse search consumption is reported.

### After 12 hours:
-	All Dataverse indexed data is deleted.
-	No Dataverse search consumption is reported.
-	Dependent experiences, such as published agents and published model-driven applications, are limited.

## Re-enabling Dataverse search

### Selecting “On”
Once Dataverse search is turned back on after being turned off, all indexes are immediately re-triggered across all enabled experiences for them to work accordingly, and Dataverse search consumption will be reported.

### Selecting “Default”
Once Dataverse search is turned to “Default” after being turned off, only when the indexes are triggered Dataverse search consumption will be reported.


## Impact of turning off Dataverse search across dependent experiences

|Feature   |Maker experience  |End-User experience  |
|----------|------------------|---------------------|
|Microsoft Copilot Studio Agent – Add Knowledge     |•	Can't upload files •	Can't select Dataverse tables •	Agent won't provide results until Dataverse is enabled for the environment (Warning banner with call to action for environment’s Admin to enable it)       |•	Agent won't provide results until Dataverse is enabled for the environment (default to Fallback answer)        |
|Microsoft Copilot Studio Agent – Using Copilot Chat  | •	Agent won't provide results until Dataverse is enabled for the environment (Warning banner with call to action to connect with environment’s Admin to enable it)  |•	Agent won't provide results until Dataverse is enabled for the environment (default to Fallback answer)  |
|Model Driven Applications – Dataverse search  | •	Search bar won't be visible in model-driven applications  |•	Same as Maker experience |
|Model Driven Applications – Copilot Chat  |•	Can use Model Driven App for record management (add, edit, delete, and so on) •	Agent won't provide results until Dataverse is enabled for the environment (Warning banner with call to action to connect with environment’s Admin to enable it)  |•	Same as Maker experience|
|Prompt actions with AI Builder / Custom AI Prompts •	Microsoft Copilot Studio •	Power Apps •	Power Automate  |•	If enabled in the settings, prompts won't be grounded with Dataverse knowledge|•	N/A|


## What actions can Makers take if Dataverse search is turned "Off"?

The best option for a Maker is to request their environment or tenant Admin to turn Dataverse search “On” or “Default”, as its disablement leads to poor quality answers and overall generative AI experiences.

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

## Can I configure the order of tables appearing in search results page?

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

## Why does searching on the RegardingObjectId attribute not work when search is enabled on it?

Search is not supported on polymorphic lookup attributes. RegardingObjectId attribute in activity table like email, task etc. is a polymorphic lookup attribute.

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
