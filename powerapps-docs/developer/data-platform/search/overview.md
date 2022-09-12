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

## How to use

Developers can use the search APIs three different ways:

- The native Search `/api/search/v1.0/` endpoint
- The Dataverse SDK for .NET
- The Web API `/api/data/` endpoint


### Use the native search endpoint

The search endpoint is the native endpoint for Dataverse Search. This is the endpoint used for the search experience in model-driven apps. You can use this endpoint without authentication from within model-driven application experiences such as PCF controls or form scripts.

You can also authenticate to this endpoint from external applications just as you would when using Web API, but you will use the `/api/search/` path rather than `/api/data/`.

### Use the Dataverse SDK for .NET

For .NET projects using the Dataverse SDK for .NET, you can use the `CrmSvcUtil` command line code generation tool to generate `*Request` and `*Response` classes for these messages just as you would for any custom action. Or, you can use the <xref:Microsoft.Xrm.Sdk.OrganizationRequest?text=OrganizationRequest> and <xref:Microsoft.Xrm.Sdk.OrganizationResponse?text=OrganizationResponse> classes.

> [!NOTE]
> To use Dataverse search from a plug-in, you must use the SDK.

More information:

- [Generate early-bound classes for the Organization service](../org-service/generate-early-bound-classes.md)
- [Use messages with the Organization service](../org-service/use-messages.md)

### Use the Web API

In the Web API, the `searchquery`, `searchsuggest`, and `searchautocomplete` messages are exposed as OData actions. More information: [Use Web API actions](../webapi/use-web-api-actions.md)

## Search operations

Search provides three operations to support a user interface that enables searching for data and two operations that you can use to retrieve information about how the organization is configured to support search.

|Search Endpoint<br />Web API Action<br />SDK message|Description|
|---------|---------|
|`/api/search/v1.0/query`<br /><xref:Microsoft.Dynamics.CRM.searchquery?text=searchquery Action><br />`searchquery`| Returns a search results page.|
|`/api/search/v1.0/suggest`<br /><xref:Microsoft.Dynamics.CRM.searchquery?text=searchsuggest Action><br />`searchsuggest`|Provide suggestions as the user enters text into a form field. |
|`/api/search/v1.0/autocomplete`<br /><xref:Microsoft.Dynamics.CRM.searchquery?text=searchautocomplete Action><br />`searchautocomplete`| Provide autocompletion of input as the user enters text into a form field.|
|`/api/search/v1.0/status`<br /><xref:Microsoft.Dynamics.CRM.status?text=status Function><br />`status`|Search status of an Organization.|
|`/api/search/v1.0/searchstatistics`<br /><xref:Microsoft.Dynamics.CRM.searchstatistics?text=searchstatistics Function><br />`searchstatistics`|Provides organization storage size and document count.|

The Web API and Dataverse SDK for .NET expose the native Search verbs Web API Actions or as organization service `messages`. These actions and messages use the native search endpoint on the server and return the results.

## Search Status and Statistics


## Service Protection Limits

The search endpoint has service protection limits that are different from the Dataverse [Service protection API limits](../api-limits.md) that apply to the Web API and Dataverse SDK for .NET. The search endpoint returns a 429 error when # requests are received within a specific time frame. If a 429 error is returned, you should wait until the Retry-After period returned in the response header has passed before sending additional requests.

### See also

[Dataverse Search query](query.md)<br />
[Dataverse Search suggest](suggest.md)<br />
[Dataverse Search autocomplete](autocomplete.md)


[!INCLUDE [footer-banner](../../../includes/footer-banner.md)]
