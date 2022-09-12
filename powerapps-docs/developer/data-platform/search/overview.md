---
title: "Search for Dataverse records (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Use Dataverse search to return search results across multiple tables and provide suggestions and autocompletion experiences in apps." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 09/12/2022
ms.reviewer: jdaly
ms.topic: article
author: mspilde # GitHub ID
ms.author: mspilde # MSFT alias of Microsoft employees only
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
 - JimDaly
---
# Search for Dataverse records

Dataverse search delivers fast and comprehensive search results across multiple tables, in a single list, sorted by relevance. It also provides capabilities to support suggestions and autocompletion experiences in apps.

> [!NOTE]
> This documentation for developers will describe how to programmatically interact with the Dataverse Search APIs.
> 
> See the following topics for information about the user experience and how to configure Dataverse Search for your environment:
> 
> - [What is Dataverse search?](../../../user/relevance-search-benefits.md)
> - [Search for records by using Dataverse search](../../../user/relevance-search.md).
> - [Configure facets and filters](../../../user/facets-and-filters.md)
> - [Frequently asked questions about Dataverse search](../../../user/relevance-faq.md)
> - [Configure Dataverse search for your environment](/power-platform/admin/configure-relevance-search-organization)

Developers can use the search APIs to search for records using three methods:

- The Search `/api/search/v1.0/` endpoint
- The Web API `/api/data/` endpoint
- The Dataverse SDK for .NET

> [!NOTE]
> The Search endpoint is the native endpoint for Dataverse Search. This is the endpoint used for the search experience in model-driven apps.

## Search operations

Search provides three operations to support a user interface that enables searching for data.

|Search Endpoint<br />Web API Action<br />SDK for .NET message|Description|
|---------|---------|
|`/api/search/v1.0/query`<br /><xref:Microsoft.Dynamics.CRM.searchquery?text=searchquery Action><br />`searchquery`| Returns a search results page.|
|`/api/search/v1.0/suggest`<br /><xref:Microsoft.Dynamics.CRM.searchquery?text=searchsuggest Action><br />`searchsuggest`|Provide suggestions as the user enters text into a form field. |
|`/api/search/v1.0/autocomplete`<br /><xref:Microsoft.Dynamics.CRM.searchquery?text=searchautocomplete Action><br />`searchautocomplete`| Provide autocompletion of input as the user enters text into a form field.|

The Web API and Dataverse SDK for .NET expose the native Search verbs Web API Actions or as organization service `messages`. These actions and messages use the native search endpoint on the server and return the results.

## Authentication

The search endpoint uses the same authentication as the Web API. You must use OAuth except when your code runs as part of a model-driven app, such as a PCF control or form script. In those cases authentication is not required.

## Service Protection Limits

The search endpoint has service protection limits that are different from the Dataverse [Service protection API limits](../api-limits.md) that apply to the Web API and Dataverse SDK for .NET. The search endpoint returns a 429 error when # requests are received within a specific time frame. If a 429 error is returned, you should wait until the Retry-After period returned in the response header has passed before sending additional requests.

### See also

[Dataverse Search query](query.md)<br />
[Dataverse Search suggest](suggest.md)<br />
[Dataverse Search autocomplete](autocomplete.md)


[!INCLUDE [footer-banner](../../../includes/footer-banner.md)]
