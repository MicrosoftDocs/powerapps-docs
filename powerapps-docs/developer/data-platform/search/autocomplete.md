---
title: "Dataverse Search autocomplete (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Use Dataverse search autocomplete to provide autocompletion of input as the user enters text into a form field." # 115-145 characters including spaces. This abstract displays in the search result.
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
# Dataverse Search autocomplete

Autocomplete API lets consumers send a partial search query term to Dataverse search and get back the search term that is potential user intent.

Use this API to support a richer search box experience. As the user enters each character of their search term, call autocomplete and populate the search box's query with the autocomplete result to provide type-ahead word completion. For example: typing in `set` autocompletes to `settings`:

:::image type="content" source="../media/autocomplete-settings-example.png" alt-text="Example showing auto-complete with the word 'settings'":::

In addition to a search term, the results returned can be influenced by passing values for the following parameters:

|Name  |Type  |Description  |More information|
|---------|---------|---------|---------|
|`search`|string|**Required** Search Term|[`search` parameter](#search-parameter)|
|`entities`|string|The default scope is searching across all search–configured entities and fields.|[`entities` parameter](#entities-parameter)|
|`filter`|string|Filter criteria to reduce results returned.|[`filter` parameter](#filter-parameter)|
|`fuzzy`|bool|Fuzzy search to aid with misspellings. The default is false.|[`fuzzy` parameter](#fuzzy-parameter)|
|`options`|string|Options are settings configured to search a search term. Eg. `lucene`, `besteffortsearch`, `groupranking`, `searchmodelall`.|[`options` parameter](#options-parameter)|
|`propertybag`|string|A collection of the additional properties for search request. Eg. appid, correlationid.|[`propertybag` parameter](#propertybag-parameter)|

## Parameters

Details for the parameters in the table above can be found below.

### `search` parameter

**Type**: string<br />
**Optional**: false

Search Term

### `entities` parameter

**Type**: string<br />
**Optional**: True

The default scope is searching across all search–configured entities and fields.

### `filter` parameter

**Type**: string<br />
**Optional**: True

Filter criteria to reduce results returned.

### `fuzzy` parameter

**Type**: bool<br />
**Optional**: True

Fuzzy search to aid with misspellings. The default is false.

### `options` parameter

**Type**: string<br />
**Optional**: True

Options are settings configured to search a search term. Eg. `lucene`, `besteffortsearch`, `groupranking`, `searchmodelall`.

### `propertybag` parameter

**Type**: string<br />
**Optional**: True

A collection of the additional properties for search request. Eg. appid, correlationid.

## Examples

### Example: TODO

This is a template for an example


#### [SDK for .NET](#tab/sdk)

```csharp
static void SDKExampleMethod(IOrganizationService service){
 TODO
}
```
**Output**

```
TODO: The output of the SDK Sample
```

#### [Web API](#tab/webapi)

**Request**

```http
POST [Organization URI]/api/data/v9.2/searchautocomplete HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response**

```http
HTTP/1.1 200 OK

{}
```

#### [Search 2.0 endpoint](#tab/search)

**Request**

```http
POST [Organization URI]/api/search/v2.0/autocomplete HTTP/1.1
```

**Response**

```http
HTTP/1.1 200 OK

{}
```
---

### See also

[Search for Dataverse records](overview.md)<br />
[Dataverse Search query](query.md)<br />
[Dataverse Search suggest](suggest.md)<br />
[Dataverse Search status](status.md)<br />
[Dataverse Search statistics](statistics.md)<br />
[Dataverse Native Search 1.0](search1.0.md)

[!INCLUDE [footer-banner](../../../includes/footer-banner.md)]