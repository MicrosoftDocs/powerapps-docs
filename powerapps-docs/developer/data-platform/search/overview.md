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
> - [Configure Dataverse search for your environment](/power-platform/admin/configure-relevance-search-organization)

## How to use

Developers can use the search APIs three different ways:

- The Dataverse SDK for .NET
- The Web API `/api/data/v9.x` endpoint
- The native search `/api/search/v2.0/` endpoint

### SDK for .NET

Search operations are defined as Dataverse messages using [Custom APIs](../custom-api.md). For .NET projects they can also be used with the SDK for .NET.

There are currently no classes included in the SDK to use these operations. For .NET Framework projects you can use the `CrmSvcUtil` command line code generation tool with the `/generateactions` parameter to generate `*Request` and `*Response` classes for these messages just as you would for any custom action.

You can also use the <xref:Microsoft.Xrm.Sdk.OrganizationRequest?text=OrganizationRequest> and <xref:Microsoft.Xrm.Sdk.OrganizationResponse?text=OrganizationResponse> classes.

More information:

- [Generate early-bound classes for the Organization service](../org-service/generate-early-bound-classes.md)
- [Use messages with the Organization service](../org-service/use-messages.md)

### Web API

Search operations exposed with Web API are OData actions or functions described in the [CSDL $metadata document](../webapi/web-api-service-documents.md#csdl-metadata-document). You can use these in the same way you use other Web API operations.

More information:

- [Use Web API actions](../webapi/use-web-api-actions.md)
- [Use Web API functions](../webapi/use-web-api-functions.md)

### Native search 2.0

The native search 2.0 endpoint is not an OData service and has no service document. The native search 2.0 endpoint accepts the same parameters and returns the same responses as the corresponding Web API Actions and functions.

The [Dataverse native search 1.0](search1.0.md) has not been deprecated and continues to be supported.

## Search operations

Search provides three operations to support a user interface that enables searching for data.

|Web API Action<br />Search Endpoint<br />SDK Message Name|Description|
|---------|---------|
|<xref:Microsoft.Dynamics.CRM.searchquery?text=searchquery Action><br />`/api/search/v2.0/query`<br />`searchquery`| Returns a search results page. <br /> See [Dataverse Search query](query.md)|
|<xref:Microsoft.Dynamics.CRM.searchquery?text=searchsuggest Action><br />`/api/search/v2.0/suggest`<br />`searchsuggest`|Provide suggestions as the user enters text into a form field. <br /> See [Dataverse Search suggest](suggest.md)|
|<xref:Microsoft.Dynamics.CRM.searchquery?text=searchautocomplete Action><br />`/api/search/v2.0/autocomplete`<br />`searchautocomplete`| Provide autocompletion of input as the user enters text into a form field.<br /> See [Dataverse Search autocomplete](autocomplete.md)|

There are also two operations you can use to understand whether search is enabled and how it is configured.

|Web API Function<br />Search Endpoint<br />SDK Message Name|Description|
|---------|---------|
|<xref:Microsoft.Dynamics.CRM.searchstatus?text=searchstatus Function><br />`/api/search/v2.0/status`<br />`searchstatus`|Search status of an Organization.<br /> See [Dataverse Search status](status.md)|
|<xref:Microsoft.Dynamics.CRM.searchstatistics?text=searchstatistics Function><br />`/api/search/v2.0/statistics`<br />`searchstatistics`|Provides organization storage size and document count.<br /> See [Dataverse Search statistics](statistics.md)|


## Detect if search is enabled

Dataverse search is enabled by default for production environments, but it is an opt-out feature so it could be turned off even in a production environment. If you are using an environment other than a production environment, an administrator must enable it.

This is the error you will get when search is not enabled when using Web API or the Native search:

```http
HTTP/1.1 400 Bad Request
{"error":{"code":"0x80048d0b","message":"Dataverse Search feature is disabled for this organization."}}
```

TODO: Verify SDK Error is the same


You can detect whether the search service is enabled by checking the settings in the organization table or by using the [Dataverse Search status](status.md) operation.

### Check Organization table

The [Organization table](../reference/entities/organization.md) contains a single row of data that controls how the organization is configured. The [IsExternalSearchIndexEnabled](../reference/entities/organization.md#BKMK_IsExternalSearchIndexEnabled) boolean column tells you whether search is enabled for the organization.


## Enable tables and columns for search

Which tables and columns are enabled for search is driven by data in Dataverse.

### Enable Tables

Only those tables where the <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.CanEnableSyncToExternalSearchIndex?text=EntityMetadata.CanEnableSyncToExternalSearchIndex>.Value property is true can be enabled for Dataverse search.

To enable a table for Dataverse Search, set the <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.SyncToExternalSearchIndex?text=EntityMetadata.SyncToExternalSearchIndex> boolean property to true.

More information:

- [Select tables for Dataverse search](/power-platform/admin/configure-relevance-search-organization#select-tables-for-dataverse-search)
- [Set managed properties for Dataverse search](/power-platform/admin/configure-relevance-search-organization#set-managed-properties-for-dataverse-search)

### Enable Columns

The columns that are searchable for the table are determined by whether they are included in the Quick Find view for each table. You can query the definition of the view in the [View (SavedQuery)  table](../reference/entities/savedquery.md)

More information:

- [Select searchable fields and filters for each table](/power-platform/admin/configure-relevance-search-organization#select-searchable-fields-and-filters-for-each-table)
- [Customize views](../../model-driven-apps/customize-entity-views.md)

## Service Protection Limits

Dataverse search has service protection limits that are different from the Dataverse [Service protection API limits](../api-limits.md) that apply to the Web API and Dataverse SDK for .NET.

Dataverse search allows a user to send 1 request per second. If this is exceeded, a [429 Too Many Requests](https://developer.mozilla.org/docs/Web/HTTP/Status/429) error will be returned. If a `429` error is returned, you should wait until the period defined in the `Retry-After` response header value has passed before sending additional requests. The value represents the number of seconds to wait.


### See also

[Dataverse Search query](query.md)<br />
[Dataverse Search suggest](suggest.md)<br />
[Dataverse Search autocomplete](autocomplete.md)<br />
[Dataverse Search status](status.md)<br />
[Dataverse Search statistics](statistics.md)<br />
[Dataverse Native Search 1.0](search1.0.md)


[!INCLUDE [footer-banner](../../../includes/footer-banner.md)]
