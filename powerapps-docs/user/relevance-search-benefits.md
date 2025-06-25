---
title: What is Dataverse search?
description: Dataverse search for model-driven apps helps you quickly find what you're looking for. 
author: shwetamurkute
ms.component: pa-user
ms.topic: article
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

In addition to helping users of model-driven apps quickly find what they're looking for, Dataverse search is how Microsoft enables rich search and AI-powered experiences across different products that use Dataverse as one of the data sources. 

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

- **Enables generative AI experiences**: Provides superior knowledge experience for search and agents for data in Dataverse tables and Files uploaded in Microsoft Copilot Studio.
 
For more information about Dataverse search, see [Search for tables and rows by using Dataverse search](/powerapps/user/relevance-search).

## What makes Dataverse search?
In addition to the Database and File storage, Dataverse search includes the indexes that power different experiences. These indexes support search and generative AI across structured or tabular, as well as unstructured data stored in Dataverse.

## Experiences enabled by Dataverse search
Multiple features within the Power Platform are enabled via Dataverse search, namely the Copilot indexes. These experiences include:

**Microsoft Copilot Studio Agents**

1.	[Add Files as a knowledge source]([url](microsoft-copilot-studio/knowledge-add-file-upload))
2.	[Add Dataverse as a knowledge source]([url](microsoft-copilot-studio/knowledge-add-dataverse))
3.	[Add Sharepoint as a knowledge source]([url](microsoft-copilot-studio/knowledge-add-sharepoint))
4.	[Add OneDrive as a knowledge source]([url](microsoft-copilot-studio/knowledge-add-unstructured-data))
5.	[Agent Copilot]([url](microsoft-copilot-studio/guidance/generative-ai-math-data-queries))

**Dynamics 365 Copilots**

6.	[Sales Copilot]([url](dynamics365/sales/copilot-overview))
7.	[Customer Service Copilot]([url](dynamics365/contact-center/use/use-copilot-features))
8.	[Contact Center Copilot]([url](dynamics365/contact-center/administer/configure-copilot-features))
9.	[Field Service Copilot]([url](dynamics365/field-service/copilot-side-pane))

**Power Apps – Model-Driven Apps**

10.	[Copilot for app users in model-driven apps]([url](power-apps/maker/model-driven-apps/add-ai-copilot))
11.	[Dataverse search]([url](configure-relevance-search-organization?tabs=new))

**Experiences across the Power Platform**

12.	[In Power Apps / Power Automate]([url](ai-builder/prompt-library))
13.	[In Microsoft Copilot Studio]([url](microsoft-copilot-studio/nlu-prompt-node))
14.	[Power Apps / Power Automate - Custom AI Prompts]([url](ai-builder/create-a-custom-prompt))

# What actions can Makers take if Dataverse search is turned off for their environment?

Currently, the best option for a Maker is to request their environment or tenant Admin to turn Dataverse search “On” or “Default”, as its disablement leads to poor quality answers and overall generative AI experiences.

## What happens if Dataverse search is turned off?

| Feature |	Maker experience | End User Experience|
|---------|------------------|--------------------|
| Microsoft Copilot Studio Agent – Add Knowledge  | - Cannot upload files - Cannot select Dataverse tables - Agent will not provide results that rely on this indexed data until Dataverse search is enabled for the environment (call to action for environment’s Admin to enable it)  | Agent will not provide results that rely on this indexed data until Dataverse search is enabled for the environment (default to Fallback answer)  |
| Microsoft Copilot Studio Agent – Using Copilot Chat	|	Agent will not provide results that rely on this indexed data until Dataverse search is enabled for the environment (call to action for environment’s Admin to enable it)  | Agent will not provide results that rely on this indexed data until Dataverse search is enabled for the environment (default to Fallback answer) 
| Model Driven Applications – Dataverse search  |	Search bar will not be visible in model-driven applications  | Search bar will not be visible in model-driven applications |

### See also

[Search for tables and rows by using Dataverse search](relevance-search.md)<br/>
[Configure facets and filters](facets-and-filters.md)<br/>
[Frequently asked questions about Dataverse search](relevance-faq.md)<br />
[Developer's guide: Search for Dataverse records using the API](../developer/data-platform/search/overview.md)<br/>   
[Compare search options in Microsoft Dataverse](search.md)

[!INCLUDE[footer-include](../includes/footer-banner.md)]
