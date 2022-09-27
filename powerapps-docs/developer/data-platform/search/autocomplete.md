---
title: "Dataverse Search autocomplete (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Use Dataverse search autocomplete to provide autocompletion of input as the user enters text into a form field." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 09/27/2022
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
|`search`|string|**Required**. Search Term|[`search` parameter](#search-parameter)|
|`entities`|string|The default scope is searching across all search–configured entities and fields.|[`entities` parameter](#entities-parameter)|
|`filter`|string|Filter criteria to reduce results returned.|[`filter` parameter](#filter-parameter)|
|`fuzzy`|bool|Fuzzy search to aid with misspellings. The default is false.|[`fuzzy` parameter](#fuzzy-parameter)|
|`options`|string|Options are settings configured to search a search term. Eg. `lucene`, `besteffortsearch`, `groupranking`, `searchmodelall`. TODO: I think `advanced` maybe the only valid parameter here, and it may be a no-op.|[`options` parameter](#options-parameter)|
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

When set to true, this API finds suggestions even if there is a substituted or missing character in the search text. The edit distance is 1 per query string. If the query string is multiple terms, there can only be one missing, extra, substituted, or transposed character in the entire string. Enabling fuzzy match can be a better experience in some scenarios, it does come at a performance cost, as fuzzy suggestion searches are slower and consume more resources.

### `options` parameter

**Type**: string<br />
**Optional**: True

Options are settings configured to search a search term. Eg. `lucene`, `besteffortsearch`, `groupranking`, `searchmodelall`.

TODO: Same as with suggest. Internal docs say `advanced` is the only option for suggest, and the reason to choose it is:

> Use 'advanced' if your autocomplete request needs to route through advanced algorithm. This is a no-op at this point of time.

What does this mean? Mark as **Internal use only**?

- Are the other options mentioned valid here?


### `propertybag` parameter

**Type**: string<br />
**Optional**: True

A collection of the additional properties for search request. Eg. appid, correlationid.

## Response

The response from the suggest operation is an escaped string that includes JSON data.

The unescaped response contains JSON using the following properties.


|Name|Type|Description|
|---------|---------|---------|
|`Error`|[ErrorDetail](#errordetail)|Provides error information from Azure Cognitive search.|
|`Value`|string|The text|
|`QueryContext` |[QueryContext](#querycontext)|TODO: find out. It is always null. Why is it included?|

### Types

The following types are returned by the Query Response.

#### ErrorDetail

TODO: Why is this included? Why doesn't the service just return an error?
GUESS: This will be a Cognitive Search error

TODO: Use include if this is the same for all types

|Name|Type|Description|
|---------|---------|---------|
|`Code`|string|The error code.|
|`Message`|string|The error message.|
|`PropertyBag`|`Dictionary<string, object>`|Additional error information.|

#### QueryContext

|Name|Type|Description|
|---------|---------|---------|
|`OriginalQuery`|string|The query string as specified in the request.|
|`AlteredQuery`|string|The query string that Dataverse search used to perform the query. Dataverse search uses the altered query string if the original query string contained spelling mistakes or did not yield optimal results.|
|`Reason`|string[]|The reason behind query alter decision by Dataverse search.|
|`SpellSuggestions`|string[]|The spell suggestion that are the likely words that represent user's intent. This will be populated only when the query was altered by Dataverse search due to spell check.|

## Examples

The following examples show how to use the autocomplete operation.

### Example: TODO specific scenario

This is a template for an example about how to achieve a specific scenario.


#### [SDK for .NET](#tab/sdk)

```csharp
static void SDKExampleMethod(IOrganizationService service){
    OrganizationRequest autocompleteRequest = new OrganizationRequest("searchautocomplete")
   {
      Parameters = new ParameterCollection
      {
         { "search", "TODO" },
         { "entities", "TODO" },
         { "filter","TODO" },
         { "fuzzy", true },
         { "options","TODO" },
         { "propertybag","TODO" }
      }
   };

   OrganizationResponse searchAutoCompleteResponse = service.Execute(autocompleteRequest);
   string responseString = searchAutoCompleteResponse.Results["response"];
   
   //TODO: Parse the string to get the objects.
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

{
 "search": "TODO",
 "entities": "TODO",
 "filter": "TODO",
 "fuzzy": true,
 "options": "TODO",
 "propertybag": "TODO"
}
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

{
 "search": "TODO",
 "entities": "TODO",
 "filter": "TODO",
 "fuzzy": true,
 "options": "TODO",
 "propertybag": "TODO"
}
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
