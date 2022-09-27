---
title: "Dataverse Search suggest (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Use Dataverse search suggest to provide suggestions as the user enters text into a form field." # 115-145 characters including spaces. This abstract displays in the search result.
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
# Dataverse Search suggest

Use this API to support a richer search box experience. For example, as the user enters each character of their search term, call this API and populate the dropdown list of the search field with the suggested query results.

In addition to a search term, the results returned can be influenced by passing values for the following parameters:


|Name  |Type  |Description  |More information|
|---------|---------|---------|---------|
|`search`|string|**Required** The text to search with. |[search parameter](#search-parameter)|
|`entities`|string|The default is searching across all search–configured entities.|[`entities` parameter](#entities-parameter)|
|`filter`|string|Filter criteria to reduce results returned.|[`filter` parameter](#filter-parameter)|
|`fuzzy`|bool|Use fuzzy search to aid with misspellings. The default is false.|[`fuzzy` parameter](#fuzzy-parameter)|
|`options`|string|Options are settings configured to search a search term. Eg. `lucene`, `besteffortsearch`, `groupranking`, `searchmodelall`.|[`options` parameter](#options-parameter)|
|`orderby`|string|   List of comma-separated clauses where each clause is an attribute name followed by `asc` or `desc`.|[`orderby` parameter](#orderby-parameter)|
|`propertybag`|string|A collection of additional properties for search request. Eg. appid, correlationid.|[`propertybag` parameter](#propertybag-parameter)|
|`top`|int|Number of suggestions to retrieve. The default is 5.|[`top` parameter](#top-parameter)|

## Parameters

Details for the parameters in the table above can be found below.


### `search` parameter

**Type**: string<br />
**Optional**: false

Search term.

### `entities` parameter

**Type**: string<br />
**Optional**: false

The default is searching across all search–configured entities.

### `filter` parameter

**Type**: string<br />
**Optional**: false

Filter criteria to reduce results returned.

### `fuzzy` parameter

**Type**: bool<br />
**Optional**: false

Use fuzzy search to aid with misspellings. The default is false.

### `options` parameter

**Type**: string<br />
**Optional**: false

Options are settings configured to search a search term. Eg. `lucene`, `besteffortsearch`, `groupranking`, `searchmodelall`.

TODO: Internal docs say `advanced` is the only option for suggest, and the reason to choose it is:

> Use 'advanced' if your suggest request needs to route through advanced suggest algorithm.

What does this mean?

- Are the other options mentioned valid here?

### `orderby` parameter

**Type**: string<br />
**Optional**: false

List of comma-separated clauses where each clause is an attribute name followed by `asc` or `desc`.

### `propertybag` parameter

**Type**: string<br />
**Optional**: false

A collection of additional properties for search request. Eg. appid, correlationid.

### `top` parameter

**Type**: int<br />
**Optional**: false

Number of suggestions to retrieve. The default is 5.

## Response

The response from the suggest operation is an escaped string that includes JSON data.

The unescaped response contains JSON using the following properties.


|Name|Type|Description|
|---------|---------|---------|
|`Error`|[ErrorDetail](#errordetail)|Provides error information from Azure Cognitive search.|
|`Value`|[`SuggestResult`](#queryresult)`[]`|A collection of matching records.|
|`QueryContext` |[QueryContext](#querycontext)|TODO: find out. It is always null. Why is it included?|

### Types

The following types are returned by the Query Response.

#### ErrorDetail

TODO: Why is this included? Why doesn't the service just return an error?
GUESS: This will be a Cognitive Search error

|Name|Type|Description|
|---------|---------|---------|
|`Code`|string|The error code.|
|`Message`|string|The error message.|
|`PropertyBag`|`Dictionary<string, object>`|Additional error information.|

#### SuggestResult

Provides the suggested text.

|Name|Type|Description|
|---------|---------|---------|
|`Text`|string|Provides the suggested text.|
|`Document`|`Dictionary<string, object>`|The document.|

TODO: Explain what to do with the document.

#### QueryContext

|Name|Type|Description|
|---------|---------|---------|
|`OriginalQuery`|string|The query string as specified in the request.|
|`AlteredQuery`|string|The query string that Dataverse search used to perform the query. Dataverse search uses the altered query string if the original query string contained spelling mistakes or did not yield optimal results.|
|`Reason`|string[]|The reason behind query alter decision by Dataverse search.|
|`SpellSuggestions`|string[]|The spell suggestion that are the likely words that represent user's intent. This will be populated only when the query was altered by Dataverse search due to spell check.|

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
GET [Organization URI]/api/data/v9.2/searchquery HTTP/1.1
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
POST [Organization URI]/api/search/v1.0/status HTTP/1.1
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
[Dataverse Search autocomplete](autocomplete.md)<br />
[Dataverse Search status](status.md)<br />
[Dataverse Search statistics](statistics.md)<br />
[Dataverse Native Search 1.0](search1.0.md)

[!INCLUDE [footer-banner](../../../includes/footer-banner.md)]
