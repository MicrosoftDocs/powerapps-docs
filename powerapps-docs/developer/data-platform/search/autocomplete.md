---
title: "Dataverse Search autocomplete (Microsoft Dataverse) | Microsoft Docs"
description: "Use Dataverse search autocomplete to provide autocompletion of input as the user enters text into a form field."
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

## Parameters

This section contains details about the parameters in the table above.

### `search` parameter

**Type**: string<br />
**Optional**: false

Search term must be at least one character long and has a 100 character limit.

### `entities` parameter

**Type**: string<br />
**Optional**: True

The default scope is searching across all search–configured entities and fields. This parameter uses the same [Query SearchEntity type](query.md#searchentity-type) used by the query API.

### `filter` parameter

**Type**: string<br />
**Optional**: True

Filter criteria to reduce results returned. This parameter uses the same string values as [Query filter parameter](query.md#filter-parameter).

### `fuzzy` parameter

**Type**: bool<br />
**Optional**: True

Fuzzy search to aid with misspellings. The default is false.

When set to true, this API finds suggestions even if there's a substituted or missing character in the search text. The edit distance is 1 per query string. If the query string is multiple terms, there can only be one missing, extra, substituted, or transposed character in the entire string. Enabling fuzzy match can be a better experience in some scenarios, it does come at a performance cost, as fuzzy suggestion searches are slower and consume more resources.

## Response

The response from the suggest operation is an escaped string that includes JSON data.

The unescaped response contains JSON using the following properties.


|Name|Type|Description|
|---------|---------|---------|
|`Error`|[ErrorDetail](#errordetail)|Provides error information from Azure Cognitive search.|
|`Value`|string|The text.|
|`QueryContext` |[QueryContext](#querycontext)|This property is used for backend search. It's included for future feature releases and is currently not used.

### Response types

The response returns the following types:

#### ErrorDetail

This type is the same [ErrorDetail](query.md#errordetail) returned by the query API.

#### QueryContext

This type is the same [QueryContext](query.md#querycontext) returned by the query API.

## Examples

The following examples show how to use the autocomplete operation. These examples return autocomplete results for the account table `name` field.

#### [SDK for .NET](#tab/sdk)

This example is from the [SDK for .NET search operations sample](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/CSharp-NETCore/Search) on GitHub. The static `OutputAutoComplete` method accepts a value for the [search parameter](#search-parameter).

```csharp
/// <summary>
/// Demonstrate autocomplete API
/// </summary>
/// <param name="service">The authenticated IOrganizationService instance to use.</param>
/// <param name="searchTerm">The term to use</param>
/// <returns></returns>
static void OutputAutoComplete(IOrganizationService service, string searchTerm)
{
    Console.WriteLine("OutputAutoComplete START\n");

    searchautocompleteRequest request = new()
    {
        search = searchTerm,
        filter = null,
        fuzzy = true,
        entities = JsonConvert.SerializeObject(new List<SearchEntity>()
            {
                new SearchEntity()
                {
                    Name = "account",
                    SelectColumns = new List<string>() { "name", "createdon" },
                    SearchColumns = new List<string>() { "name" },
                }
            }
        )
    };

    var searchautocompleteResponse = (searchautocompleteResponse)service.Execute(request);

    SearchAutoCompleteResults results = JsonConvert.DeserializeObject<SearchAutoCompleteResults>(searchautocompleteResponse.response);

    Console.WriteLine($"\tSearch: {request.search}");
    Console.WriteLine($"\tValue: {results.Value}");

    Console.WriteLine("\nOutputAutoComplete END\n");
}
```

#### Output

When you invoke the `OutputAutoComplete` method with an authenticated instance of the [ServiceClient](xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient) class with the `searchTerm` set to "Con":

```csharp
OutputAutoComplete(service: serviceClient, searchTerm: "Con");
```

The output looks something like the following:

```
OutputAutoComplete START

        Search: Con
        Value: {crmhit}contoso{/crmhit}

OutputAutoComplete END
```

#### Supporting classes

The `OutputAutoComplete` method depends on the following supporting classes to send the request and process the result:

##### searchautocompleteRequest and searchautocompleteResponse classes

These classes are generated using Power Platform CLI [pac modelbuilder build](/power-platform/developer/cli/reference/modelbuilder#pac-modelbuilder-build) command as described in [Generate early-bound classes for the SDK for .NET](../org-service/generate-early-bound-classes.md).

##### SearchEntity class

This class is the same `SearchEntity` class used for the [query example](query.md#searchentity-class). In this case, you use it to set the `searchautocompleteRequest.entities` property.

##### SearchAutoCompleteResults class

Use to deserialize JSON data from the `searchautocompleteResponse.response` string property.

```csharp
class SearchAutoCompleteResults
{
   /// <summary>
   /// The Azure Cognitive error detail returned as part of response.
   /// </summary>
   public ErrorDetail? Error {  get; set; }

   /// <summary>
   /// The text
   /// </summary>
   public string? Value { get; set; }

   /// <summary>
   /// This request is used for backend search, this is included for future feature releases, it is not currently used.
   /// </summary>
   public QueryContext? QueryContext { get; set; }
}
```

##### ErrorDetail class

This class is the same `ErrorDetail` class used for the [query example](query.md#errordetail-class).

##### QueryContext class

This class is the same `QueryContext` class used for the [query example](query.md#querycontext-class).


#### [Web API](#tab/webapi)

Use the [searchautocomplete action](xref:Microsoft.Dynamics.CRM.searchautocomplete) to receive a [searchautocompleteResponse complex type](xref:Microsoft.Dynamics.CRM.searchautocompleteResponse).

This example is from the [Web API search operations sample](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/webapi/CSharp-NETx/Search) on GitHub.

The unescaped, formatted JSON passed to the string `entities` parameter looks like this:

```json
[
  {
    "Name": "account",
    "SelectColumns": ["name", "createdon"],
    "SearchColumns": ["name"],
    "Filter": null
  }
]
```

**Request**

```http
POST [Organization Uri]/api/data/v9.2/searchautocomplete
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
Content-Type: application/json; charset=utf-8
Content-Length: 191

{
  "entities": "[{\"Name\":\"account\",\"SelectColumns\":[\"name\",\"createdon\"],\"SearchColumns\":[\"name\"],\"Filter\":null}]",
  "search": "Con",
  "fuzzy": true,
  "filter": null
}
```

**Response**

```http
HTTP/1.1 200 OK
CRM.ServiceId: framework
OData-Version: 4.0

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.searchautocompleteResponse",
  "response": "{\"Error\":null,\"Value\":\"{crmhit}contoso{/crmhit}\",\"QueryContext\":null}"
}
```

The unescaped, formatted JSON `response` property value looks like this:

```json
{
  "Error": null,
  "Value": "{crmhit}contoso{/crmhit}",
  "QueryContext": null
}
```

#### [Search 2.0 endpoint](#tab/search)

The request parameters and the response from the `search/v2.0/autocomplete` endpoint is the same as the Web API. Only the URL is different.

**Request URL**

```http
POST [Organization Uri]/api/search/v2.0/autocomplete
```

---

### See also

[Search for Dataverse records](overview.md)   
[Dataverse Search query](query.md)   
[Dataverse Search suggest](suggest.md)   
[Dataverse Search statistics and status](statistics-status.md)   
[Dataverse legacy search](legacy.md)

[!INCLUDE [footer-banner](../../../includes/footer-banner.md)]
