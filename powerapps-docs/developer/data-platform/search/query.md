---
title: "Dataverse Search query (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Use Dataverse search query to return search results across multiple tables." # 115-145 characters including spaces. This abstract displays in the search result.
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
# Dataverse Search query

The query operation returns search results based on a search term. In addition to a search term, the results returned can be influenced by passing values for the following parameters:


|Name  |Type  |Description  |
|---------|---------|---------|
|`search`|string|**Required** The text to search with. See [search parameter](#search-parameter)|
|`entities`|string[]|Limits the scope of search to a sub-set of tables. See [entities parameter](#entities-parameter)|
|`facets`|string[]|Facets support the ability to drill down into data results after they've been retrieved. See [facets parameter](#facets-parameter)|
|`filter`|string|Limits the scope of the search results returned. See [filter parameter](#filter-parameter)|
|`returntotalrecordcount`|bool|When using the search endpoint: Whether to return the total record count. Use `count` when using Dataverse Web API or SDK.|
|`count`|bool|When using Dataverse Web API or SDK: Whether to return the total record count. Use `returntotalrecordcount`when using the search endpoint|
|`skip`|int|Specifies the number of search results to skip. See [skip and top parameters](#skip-and-top-parameters)|
|`top`|int|Specifies the number of search results to retrieve. See [skip and top parameters](#skip-and-top-parameters)|
|`orderby`|string[]|Specifies how to order the results in order of precedence. See [orderby parameter](#orderby-parameter)|
|`searchmode`|`any` \| `all`|Specifies whether any or all the search terms must be matched to count the document as a match. See [searchmode parameter](#searchmode-parameter)|
|`searchtype`|`simple` \| `full`|Specifies the syntax of a search query. See [searchtype parameter](#searchtype-parameter)|
|`propertybag`|string|A collection of the additional properties for search request. Eg. appid, correlationid.|
|`options`|string|Options are settings configured to search a search term. Eg. `lucene`, `besteffortsearch`, `groupranking`, `searchmodelall`.|

## search parameter

## entities parameter

## facets parameter

## filter parameter

## returntotalrecordcount or count parameter

## skip and top parameters

## orderby parameter

## searchmode parameter

## searchtype parameter

## propertybag parameter

## options parameter

## Examples

### Example: TODO

This is a template for an example
#### [Search endpoint](#tab/search)

**Request**

```http
POST [Organization URI]/api/search/v1.0/status HTTP/1.1
```

**Response**

```http
HTTP/1.1 200 OK

{}
```

#### [.NET SDK](#tab/sdk)

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
---
### See also

[Search for Dataverse records](overview.md)<br />
[Dataverse Search query](query.md)
[Dataverse Search suggest](suggest.md)<br />
[Dataverse Search autocomplete](autocomplete.md)

[!INCLUDE [footer-banner](../../../includes/footer-banner.md)]