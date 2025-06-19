---
title: "Dataverse Search suggest (Microsoft Dataverse) | Microsoft Docs"
description: "Use Dataverse search suggest to provide suggestions as users enter text into a form field."
ms.date: 10/20/2023
ms.reviewer: jdaly
ms.topic: article
author: seanwat-msft
ms.author: seanwat
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
 - JimDaly
 - jeromeblouinms
---
# Dataverse Search suggest

Use this API to support a richer search box experience. For example, as the user enters each character of their search term, call this API and populate the dropdown list of the search field with the suggested query results.

In addition to a search term, the results returned can be influenced by passing values for the following parameters:


|Name  |Type  |Description  |More information|
|---------|---------|---------|---------|
|`search`|string|**Required**. The text to search with. |[search parameter](#search-parameter)|
|`entities`|string|The default is searching across all search–configured entities.|[`entities` parameter](#entities-parameter)|
|`filter`|string|Filter criteria to reduce results returned.|[`filter` parameter](#filter-parameter)|
|`fuzzy`|bool|Use fuzzy search to aid with misspellings. The default is false.|[`fuzzy` parameter](#fuzzy-parameter)|
|`options`|string|Options are settings configured to search a search term. For example `"{ 'advancedsuggestenabled': 'true' }"`.|[`options` parameter](#options-parameter)|
|`orderby`|string|   List of comma-separated clauses where each clause is an attribute name followed by `asc` or `desc`.|[`orderby` parameter](#orderby-parameter)|
|`top`|int|Number of suggestions to retrieve. The default is 5.|[`top` parameter](#top-parameter)|

## Parameters

This section contains details about the parameters introduced by the table above.


### `search` parameter

**Type**: string<br />
**Optional**: false

The text to search with. Search term must be at least three characters long and has a 100 character limit.

### `entities` parameter

**Type**: string<br />
**Optional**: true

The default is searching across all search–configured entities. Use this property to narrow the results.

### `filter` parameter

**Type**: string<br />
**Optional**: true

Filter criteria to reduce results returned based on records that match the filter criteria.

### `fuzzy` parameter

**Type**: bool<br />
**Optional**: true

Use fuzzy search to aid with misspellings. The default is false.

### `options` parameter

**Type**: string<br />
**Optional**: true

Options are settings configured to search a search term. Valid options for suggest query is:

`"{ 'advancedsuggestenabled': 'true' }"`.

### `orderby` parameter

**Type**: string<br />
**Optional**: true

List of comma-separated clauses where each clause is an attribute name followed by `asc` or `desc`.

### `top` parameter

**Type**: int<br />
**Optional**: true

Number of suggestions to retrieve. The default is 5.

## Response

The response from the suggest operation is an escaped string that includes JSON data.

The unescaped response contains JSON using the following properties.


|Name|Type|Description|
|---------|---------|---------|
|`Error`|[ErrorDetail](#errordetail)|Provides error information from Azure Cognitive search.|
|`Value`|[`SuggestResult`](#suggestresult)`[]`|A collection of matching records.|
|`QueryContext` |[QueryContext](#querycontext)|The query context returned as part of response. This property is used for backend search. It's included for future feature releases and isn't currently used.|

### Response Types

The response returns the following types:

#### ErrorDetail

This is the same [ErrorDetail](query.md#errordetail) returned by the query API.

#### SuggestResult

Provides the suggested text.

|Name|Type|Description|
|---------|---------|---------|
|`Text`|string|Provides the suggested text.|
|`Document`|`Dictionary<string, object>`|The document.|

#### QueryContext

This is the same [QueryContext](query.md#querycontext) returned by the query API.

## Examples

The following examples show how to use the suggest operation. Each of these examples pass the value "Cont" as the [search parameter](#search-parameter) and request the top three suggestions.

### [SDK for .NET](#tab/sdk)

This example is from the [SDK for .NET search operations sample](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/CSharp-NETCore/Search) on GitHub. The static `OutputSearchSuggest` method returns the top three suggestions for any search term.

```csharp
/// <summary>
/// Demonstrate suggest API
/// </summary>
/// <param name="service">The authenticated IOrganizationService instance to use.</param>
/// <param name="searchTerm">The term to use</param>
/// <returns></returns>
static void OutputSearchSuggest(IOrganizationService service, string searchTerm)
{
    Console.WriteLine("OutputSearchSuggest START\n");

    searchsuggestRequest request = new()
    {
        search = searchTerm,
        top = 3
    };

    var searchsuggestResponse = (searchsuggestResponse)service.Execute(request);

    SearchSuggestResults results = JsonConvert.DeserializeObject<SearchSuggestResults>(searchsuggestResponse.response);

    results.Value?.ForEach(suggestion =>
    {
        Console.WriteLine($"\tText:{suggestion.Text}");
        Console.WriteLine("\tDocument: ");
        foreach (string key in suggestion.Document.Keys)
        {
            Console.WriteLine($"\t\t{key}: {suggestion.Document[key]}");
        }
        Console.WriteLine();
    });

    Console.WriteLine("OutputSearchSuggest END\n");
}
```

#### Output

When you invoke the `OutputSearchSuggest` method with an authenticated instance of the [ServiceClient](xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient) class with the `searchTerm` set to "Cont":

```csharp
OutputSearchSuggest(service: serviceClient, searchTerm: "Cont");
```

The output looks something like the following:

```
OutputSearchSuggest START

        Text:{crmhit}cont{/crmhit}act
        Document:
                @search.objectid: aaaaaaaa-0000-1111-2222-bbbbbbbbbbbb
                @search.entityname: contact
                @search.objecttypecode: 2
                fullname: Yvonne McKay (sample)

        Text:{crmhit}cont{/crmhit}act
        Document:
                @search.objectid: bbbbbbbb-1111-2222-3333-cccccccccccc
                @search.entityname: contact
                @search.objecttypecode: 2
                fullname: Susanna Stubberod (sample)

        Text:{crmhit}cont{/crmhit}act
        Document:
                @search.objectid: cccccccc-2222-3333-4444-dddddddddddd
                @search.entityname: contact
                @search.objecttypecode: 2
                fullname: Nancy Anderson (sample)

OutputSearchSuggest END
```
#### Supporting classes

The `OutputSearchSuggest` method depends on the following supporting classes to send the request and process the result.

##### searchsuggestRequest and searchsuggestResponse classes

These classes are generated using Power Platform CLI [pac modelbuilder build](/power-platform/developer/cli/reference/modelbuilder#pac-modelbuilder-build) command as described in [Generate early-bound classes for the SDK for .NET](../org-service/generate-early-bound-classes.md).

##### ErrorDetail class

This class is the same `ErrorDetail` class used for the [query example](query.md#errordetail-class).

##### SuggestResults class

Used to deserialize the data from the `searchsuggestResponse.response` property

```csharp
class SearchSuggestResults
{
   /// <summary>
   /// Provides error information from Azure Cognitive search.
   /// </summary>
   [JsonProperty(PropertyName = "Error")]
   public ErrorDetail? Error { get; set; }

   /// <summary>
   /// A collection of matching records.
   /// </summary>
   public List<SuggestResult>? Value { get; set; }

   /// <summary>
   /// The query context returned as part of response. This property is used for backend search, this is included for future feature releases, it is not currently used.
   /// </summary>
   public QueryContext? QueryContext { get; set; }
}
```

##### SuggestResult class

Result object for suggest results.

```csharp
public sealed class SuggestResult
{
   /// <summary>
   /// Gets or sets the text.
   /// </summary>
   [JsonProperty(PropertyName = "text")]
   public string Text { get; set; }

   /// <summary>
   /// Gets or sets document.
   /// </summary>
   [JsonProperty(PropertyName = "document")]
   public Dictionary<string, object> Document { get; set; }
}
```


##### QueryContext class

This class is the same `QueryContext` class used for the [query example](query.md#querycontext-class).


### [Web API](#tab/webapi)

Use the [searchsuggest action](xref:Microsoft.Dynamics.CRM.searchsuggest) to receive a [searchsuggestResponse complex type](xref:Microsoft.Dynamics.CRM.searchsuggestResponse).

This example is from the [Web API search operations sample](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/webapi/CSharp-NETx/Search) on GitHub.

**Request**

```http
POST [Organization Uri]/api/data/v9.2/searchsuggest
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
Content-Type: application/json; charset=utf-8
Content-Length: 142

{
  "orderby": "null",
  "options": "null",
  "fuzzy": false,
  "search": "Cont",
  "filter": null,
  "entities": "null",
  "top": 3
}
```

**Response**

```http
HTTP/1.1 200 OK
CRM.ServiceId: framework
OData-Version: 4.0

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.searchsuggestResponse",
  "response": "{\"Error\":null,\"Value\":[{\"Text\":\"{crmhit}cont{/crmhit}act\",\"Document\":{\"@search.objectid\":\"aaaaaaaa-0000-1111-2222-bbbbbbbbbbbb\",\"@search.entityname\":\"contact\",\"@search.objecttypecode\":2,\"fullname\":\"Yvonne McKay (sample)\"}},{\"Text\":\"{crmhit}cont{/crmhit}act\",\"Document\":{\"@search.objectid\":\"bbbbbbbb-1111-2222-3333-cccccccccccc\",\"@search.entityname\":\"contact\",\"@search.objecttypecode\":2,\"fullname\":\"Susanna Stubberod (sample)\"}},{\"Text\":\"{crmhit}cont{/crmhit}act\",\"Document\":{\"@search.objectid\":\"cccccccc-2222-3333-4444-dddddddddddd\",\"@search.entityname\":\"contact\",\"@search.objecttypecode\":2,\"fullname\":\"Nancy Anderson (sample)\"}}],\"QueryContext\":null}"
}
```

The unescaped JSON data in the response property looks like this:

```json
{
  "Error": null,
  "Value": [
    {
      "Text": "{crmhit}cont{/crmhit}act",
      "Document": {
        "@search.objectid": "aaaaaaaa-0000-1111-2222-bbbbbbbbbbbb",
        "@search.entityname": "contact",
        "@search.objecttypecode": 2,
        "fullname": "Yvonne McKay (sample)"
      }
    },
    {
      "Text": "{crmhit}cont{/crmhit}act",
      "Document": {
        "@search.objectid": "bbbbbbbb-1111-2222-3333-cccccccccccc",
        "@search.entityname": "contact",
        "@search.objecttypecode": 2,
        "fullname": "Susanna Stubberod (sample)"
      }
    },
    {
      "Text": "{crmhit}cont{/crmhit}act",
      "Document": {
        "@search.objectid": "cccccccc-2222-3333-4444-dddddddddddd",
        "@search.entityname": "contact",
        "@search.objecttypecode": 2,
        "fullname": "Nancy Anderson (sample)"
      }
    }
  ],
  "QueryContext": null
}
```

### [Search 2.0 endpoint](#tab/search)

The parameters and response value using the search 2.0 endpoint are identical to the Web API, only the URL is different.

**Request**

```http
POST [Organization Uri]/api/search/v2.0/suggest
```

---

### See also

[Search for Dataverse records](overview.md)   
[Dataverse Search query](query.md)   
[Dataverse Search autocomplete](autocomplete.md)   
[Dataverse Search statistics and status](statistics-status.md)   
[Dataverse legacy search](legacy.md)

[!INCLUDE [footer-banner](../../../includes/footer-banner.md)]
