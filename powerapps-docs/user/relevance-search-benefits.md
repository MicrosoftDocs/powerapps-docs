---
title: What is Dataverse search?
description: Dataverse search for model-driven apps helps you quickly find what you're looking for. 
author: shwetamurkute
ms.component: pa-user
ms.topic: conceptual
ms.date: 11/01/2023
ms.subservice: end-user
ms.author: smurkute
ms.custom: 
ms.reviewer: smurkute
ms.assetid: 
search.audienceType: 
  - enduser
ms.contributors:
- mspilde
- JimDaly
---

# What is Dataverse search?

Dataverse search helps users of model-driven apps quickly find what they're looking for. As part of its search capabilities, its indexed data is also leveraged across generative AI experiences such as Copilot experiences to fetch records and use them as answers. Dataverse search enables rich search and AI-powered experiences across different products that use Dataverse as one of the data sources, subject to Copilot feature availability.

Dataverse search delivers the following benefits:

- **Fast and accurate search**: Provides a precise and quick search experience for model-driven apps, and performance that's superior to [categorized search](quick-find.md#multiple-table-quick-find-categorized-search). 

- **Suggested results as you type**: Finds what you're looking for and shows you the top results, as you type.

- **Better matching**: Finds matches to any word in the search term for columns in a table. Provides a better user experience compared to [quick find](quick-find.md) search, where all words in the search term must be found in one column. 

- **Smart**: Finds matches that include inflectional words such as **stream**, **streaming**, or **streamed**. 

- **Search activities**: Search includes notes and attachments in activities. 

- **Understanding of underlying data**: Understands data types like **Choice** and **Lookup**, so it can effectively interpret a search query that includes multiple search terms.

- **Operators for advanced search**: Lets you use simple Boolean operators in your search term and craft the query to get the results you want. 

- **Intelligence**: Applies AI technology to interpret natural language such as misspellings, common abbreviations, and synonyms to deliver quality results.

- **Search across documents in Microsoft Dataverse**: Includes search results for text in documents that are stored in Dataverse such as PDF, Microsoft Office documents, HTML, XML, ZIP, EML, plain text, and JSON file formats. It also searches text in notes and attachments.

- **Enables gen. AI experiences**: Provides a superior knowledge experience for search and agents for data in Dataverse tables and files uploaded in Microsoft Copilot Studio.


For more information about Dataverse search, see [Search for tables and rows by using Dataverse search](/powerapps/user/relevance-search).


## What makes Dataverse search
Dataverse search consists of two separate indexes that power different experiences.

- **Dataverse search structured index**: This is the index powering experiences across structured or tabular data stored in Dataverse. Examples of this index include search indexes over tables Dataverse like Accounts, Contact, custom tables, Dataverse relevance search, and others.
- **Dataverse search unstructured index**: This is the index powering experiences across unstructured data stored in Dataverse. Examples of this index include search indexes over files uploaded in Microsoft Copilot Studio custom agents, customer service agents, and others.

## Experiences enabled by Dataverse search
Multiple features within the Power Platform are enabled via Dataverse search, namely the Copilot indexes. These experiences include

### Microsoft Copilot Studio agents
1.	[Add Files as a knowledge source](/microsoft-copilot-studio/knowledge-add-file-upload)
2.	[Add Dataverse as a knowledge source](/microsoft-copilot-studio/knowledge-add-dataverse)
3.	[Virtual Agents](/microsoft-copilot-studio/guidance/cux-types#virtual-agents)

### Dynamics 365 copilots

4. [Sales Copilot](/dynamics365/sales/copilot-overview)
5. [Customer Service Copilot](/dynamics365/customer-service/administer/copilot-enable-summary)
6. [Contact Center Copilot](/dynamics365/contact-center/administer/configure-copilot-features)
7. [Field Service Copilot](/dynamics365/field-service/copilot-side-pane)

### Power Apps – model-driven apps

8. [Copilot Chat](../maker/model-driven-apps/add-ai-copilot.md)
9. [Dataverse search](/power-platform/admin/configure-relevance-search-organization)

### Experiences across the Power Platform

10. [AI Prompts in Power Apps / Power Automate](/microsoft-copilot-studio/nlu-prompt-node)
11. [AI Prompts in Microsoft Copilot Studio](/microsoft-copilot-studio/nlu-prompt-node)
12. [Power Apps / Power Automate - Custom AI Prompts](/ai-builder/create-a-custom-prompt)

## Managing Dataverse search

Storage used by Dataverse search is reported and charged at the environment level as a table called “RelevanceSearch” and is charged by its GB capacity. We're enhancing the capabilities and adjusting the billing of the existing Dataverse search with improved semantic Copilot indexing, where generative AI features like Copilot will become dependent on, to promote consistency across the Dataverse search and its enhanced experiences.

> [!Note]
> Dataverse search will be turned **On** if you happen to use any of the above features in the existing environment (and for any new production environment) and **Default** by default for any other scenario or new environment.
We recommend turning on Dataverse search so users can enjoy a superior search experience in model-driven apps and leverage the benefits of generative AI capabilities. Environment admins can opt out of this feature for managing their environments by selecting the option **Off**.

To learn more about how Dataverse search is reported and managed, see: [Configure Dataverse Search](/power-platform/admin/configure-relevance-search-organization)

## What actions can Makers take?

Currently, the best option for a Maker is to request their environment or tenant Admin to turn Dataverse search “On” or “Default”, as its disablement leads to poor quality answers and overall gen/ Ai experiences.

## Turning off Dataverse search

If this feature is turned off, all indexed Dataverse data will be deleted, and the experiences that depend on it are limited or unusable for all users of those experiences, which include search and AI conversational capabilities. 

Environment admins have 12 hours to turn the feature back on with no implications after turning it off.

### During 12 hours:
-	All Dataverse indexed data is stored.
-	Dataverse search consumption is reported.
-	Makers and End Users can use the experiences normally

### After 12 hours:
-	All Dataverse indexed data is deleted.
-	No Dataverse search consumption is reported.
-	Dependent experiences, such as published agents and published model-driven applications, are limited for Makers and End users.

Dataverse search can be turned back "On" or to the "Default" state anytime after being turned off.

### Selecting “On”
Once Dataverse search is turned back on after being turned off, all indexes are immediately re-triggered across all enabled experiences for them to work accordingly, and Dataverse search consumption will be reported.

### Selecting “Default”
Once Dataverse search is turned to “Default” after being turned off, only when the indexes are triggered Dataverse search consumption will be reported.

## What happens if Dataverse search is off across dependent experiences

|Feature   |Maker experience  |End-User experience  |
|----------|------------------|---------------------|
|Microsoft Copilot Studio Agent – Add Knowledge     |•	Can't upload files •	Can't select Dataverse tables •	Agent won't provide results until Dataverse is enabled for the environment (Warning banner with call to action for environment’s Admin to enable it)       |•	Agent won't provide results until Dataverse is enabled for the environment (default to Fallback answer)        |
|Microsoft Copilot Studio Agent – Using Copilot Chat  | •	Agent won't provide results until Dataverse is enabled for the environment (Warning banner with call to action to connect with environment’s Admin to enable it)  |•	Agent won't provide results until Dataverse is enabled for the environment (default to Fallback answer)  |
|Model Driven Applications – Dataverse search  | •	Search bar won't be visible in model-driven applications  |•	Same as Maker experience |
|Model Driven Applications – Copilot Chat  |•	Can use Model Driven App for record management (add, edit, delete, and so on) •	Agent won't provide results until Dataverse is enabled for the environment (Warning banner with call to action to connect with environment’s Admin to enable it)  |•	Same as Maker experience|
|Prompt actions with AI Builder / Custom AI Prompts •	Microsoft Copilot Studio •	Power Apps •	Power Automate  |•	If enabled in the settings, prompts won't be grounded with Dataverse knowledge|•	N/A|

### See also

[Search for tables and rows by using Dataverse search](relevance-search.md)<br/>
[Configure facets and filters](facets-and-filters.md)<br/>
[Frequently asked questions about Dataverse search](relevance-faq.md)<br />
[Developer's guide: Search for Dataverse records using the API](../developer/data-platform/search/overview.md)<br/>   
[Compare search options in Microsoft Dataverse](search.md)

[!INCLUDE[footer-include](../includes/footer-banner.md)]
