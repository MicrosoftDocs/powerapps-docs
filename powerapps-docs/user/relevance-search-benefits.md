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

- **Enables generative AI experiences**: Provides advanced knowledge experience for search and agents with data in Dataverse tables and files uploaded in Microsoft Copilot Studio.
 
For more information about Dataverse search, see [Search for tables and rows by using Dataverse search](/powerapps/user/relevance-search).

## What makes Dataverse search?

In addition to the database and file storage, Dataverse search includes the indexes that power different experiences. These indexes support search and generative AI across structured or tabular, as well as unstructured data stored in Dataverse.

## Experiences enabled by Dataverse search

Dataverse search lets you use multiple features in Power Platform, including Copilot indexes. These experiences include:

**Microsoft Copilot Studio Agents**

- [Add Files as a knowledge source](/microsoft-copilot-studio/knowledge-add-file-upload)
- [Add Dataverse as a knowledge source](/microsoft-copilot-studio/knowledge-add-dataverse)
- [Add Sharepoint as a knowledge source](/microsoft-copilot-studio/knowledge-add-sharepoint)
- [Add OneDrive as a knowledge source](/microsoft-copilot-studio/knowledge-add-unstructured-data)
- [Agent Copilot](/microsoft-copilot-studio/guidance/generative-ai-math-data-queries)

**Dynamics 365 Copilots**

- [Sales Copilot](/dynamics365/sales/copilot-overview)
- [Customer Service Copilot](/dynamics365/contact-center/use/use-copilot-features)
- [Contact Center Copilot](/dynamics365/contact-center/administer/configure-copilot-features)
- [Field Service Copilot](/dynamics365/field-service/copilot-side-pane)

**Power Apps – Model-Driven Apps**

- [Copilot for app users in model-driven apps](/power-apps/maker/model-driven-apps/add-ai-copilot)
- [Dataverse search](/power-platform/admin/configure-relevance-search-organization)

**Experiences across the Power Platform**

- [In Power Apps / Power Automate](/ai-builder/prompt-library)
- [In Microsoft Copilot Studio](/microsoft-copilot-studio/nlu-prompt-node)
- [Power Apps / Power Automate - Custom AI Prompts](/ai-builder/create-a-custom-prompt)

## What actions can makers take if Dataverse search is turned off for their environment?

Currently, the best option for a maker is to request their environment or tenant admin to set Dataverse search to **On** or **Default**. If Dataverse search is off, you get lower quality answers and a poor generative AI experience.

## What happens if Dataverse search is turned off?

| Feature |	Maker experience | End User Experience|
|---------|------------------|--------------------|
| Microsoft Copilot Studio Agent – Add Knowledge  | You can't upload files. You can't select Dataverse tables. The agent doesn't provide results that rely on this indexed data until Dataverse search is enabled for the environment. Ask the environment's admin to enable Dataverse search.  | The agent doesn't provide results that rely on this indexed data until Dataverse search is enabled for the environment. The agent uses the fallback answer by default.  |
| Microsoft Copilot Studio Agent – Using Copilot Chat	|	The agent doesn't provide results that rely on this indexed data until Dataverse search is enabled for the environment. Ask your environment admin to enable Dataverse search.  | The agent doesn't provide results that rely on this indexed data until Dataverse search is enabled for the environment. By default, the agent uses a fallback answer. |
| Model Driven Applications – Dataverse search  |	The search bar isn't visible in model-driven apps. | Search bar isn't visible in model-driven apps |

### See also

[Search for tables and rows by using Dataverse search](relevance-search.md)<br/>
[Configure facets and filters](facets-and-filters.md)<br/>
[Frequently asked questions about Dataverse search](relevance-faq.md)<br />
[Developer's guide: Search for Dataverse records using the API](../developer/data-platform/search/overview.md)<br/>
[Compare search options in Microsoft Dataverse](search.md)

[!INCLUDE[footer-include](../includes/footer-banner.md)]
