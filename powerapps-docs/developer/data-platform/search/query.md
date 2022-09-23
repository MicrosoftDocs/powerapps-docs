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


|Name  |Type  |Description  |More information|
|---------|---------|---------|---------|
|`search`|string|**Required** The text to search with. |[search parameter](#search-parameter)|
|`entities`|string[]|Limits the scope of search to a sub-set of tables. |[entities parameter](#entities-parameter)|
|`facets`|string[]|Facets support the ability to drill down into data results after they've been retrieved. See [facets parameter](#facets-parameter)|
|`filter`|string|Limits the scope of the search results returned. |[filter parameter](#filter-parameter)|
|`count`|bool|Whether to return the total record count.|[`count` parameter](#count-parameter) |
|`skip`|int|Specifies the number of search results to skip. |[skip and top parameters](#skip-and-top-parameters)|
|`top`|int|Specifies the number of search results to retrieve. |[skip and top parameters](#skip-and-top-parameters)|
|`orderby`|string[]|Specifies how to order the results in order of precedence. |[orderby parameter](#orderby-parameter)|
|`propertybag`|string|A collection of the additional properties for search request. Eg. appid, correlationid.|[`propertybag` parameter](#propertybag-parameter)|
|`options`|string|Options are settings configured to search a search term. Eg. `lucene`, `besteffortsearch`, `groupranking`, `searchmodelall`.|[`options` parameter](#options-parameter)|

## Parameters

Details for the parameters in the table above can be found below.

### `search` parameter

The search parameter contains the text to search. It is the only required parameter. Search term must be at least three characters long and has a 100 character limit.

By default, the search parameter supports simple search syntax as described in the table below:

| **Functionality** | **Description** |
|---|---|
| Boolean operators | AND operator; denoted by +<br/>OR operator; denoted by \|<br/>NOT operator; denoted by \- |
| Precedence operators | A search term "hotel+(wifi \| luxury)" will search for results containing the term "hotel" and either "wifi" or "luxury" (or both). |
| Wildcards            | Trailing wildcard are supported. For example, "Alp\*" searches for "alpine". |
| Exact matches        | A query enclosed in quotation marks " ".|

> [!NOTE]
> In order to use any search operators as part of the search text, escape the character by prefixing it with a single backslash (`\`). Special characters that require escaping include the following: `+ - & | ! ( ) { } [ ] ^ " ~ * ? : \ /`.

Using the [searchtype parameter](#searchtype-parameter), you can enable [Lucerne Query Syntax](#lucerne-query-syntax).

### `entities` parameter

By default all the tables enabled for search will be searched unless you specify a sub-set using the `entities` parameter. Set this parameter with an array of table logical names.

To get a list of entities enabled for the environment use the [Search Status](overview.md#search-status) API and look for the entities listed by  `entitylogicalname` within `entitystatusresults`.

### `facets` parameter

Facets support the ability to drill down into data results after they've been retrieved. By default, no facets are returned with search results.

TODO: Establish exactly what developers will do with the facets data and how to set them. This is a mystery:

```
  "facets": ["@search.entityname,count:100",  
    "account.primarycontactid,count:100",  
    "ownerid,count:100",  
    "modifiedon,values:2019-04-27T00:00:00|2020-03-27T00:00:00|2020-04-20T00:00:00|2020-04-27T00:00:00",
    "createdon,values:2019-04-27T00:00:00|2020-03-27T00:00:00|2020-04-20T00:00:00|2020-04-27T00:00:00"]
```
### `filter` parameter

Filters limit the scope of the search results returned. Use filters to exclude unwanted results.

Apply filters using this syntax: `<table logical name>: <filter>` where the table logical name specifies the entity the filter should be applied to.

Filters use the following query operators:


|Operator|Description|Example|
|--------|-----------|-------|
|**Comparison Operators**|&nbsp;|&nbsp;|
|`eq`|Equal|`account:revenue eq 100000`|
|`ne`|Not Equal|`account:revenue ne 100000`|
|`gt`|Greater than|`account:revenue gt 100000`|
|`ge`|Greater than or equal|`account:revenue ge 100000`|
|`lt`|Less than|`account:revenue lt 100000`|
|`le`|Less than or equal|`account:revenue le 100000`|
|**Logical Operators**|&nbsp;|&nbsp;|
|`and`|Logical and|`account:revenue lt 100000 and revenue gt 2000`|
|`or`|Logical or|`account:name eq 'sample' or name eq 'test'`|
|`not`|Logical negation|`account:not name eq 'sample'`|
|**Grouping Operators**|&nbsp;|&nbsp;|
|`( )`|Precedence grouping|`account:(name eq 'sample') or name eq 'test') and revenue gt 5000`|


### `count` parameter

Whether to return the total record count.


### `skip` and `top` parameters

You can use these parameters together with the [count parameter](#count-parameter) to create a paged experience.
By default, as many as 50 results will be returned at a time. You can use `top` to raise it as high as 100, but more commonly you will use top to specify a smaller result set, such as 10, and then use `skip` to bypass previously returned results when the user moves to the next page.

### `orderby` parameter

Use the `orderby` parameter to override the default ordering. By default, results are listed in descending order of relevance score (@search.score). For results with identical scores, the ordering will be random.

Use a list of comma-separated clauses where each clause consists of a column name followed by `asc` (*ascending*, which is the default) or `desc` (descending).

For a set of results that contain multiple table types, the list of clauses for `orderby` must be globally applicable (for example, `modifiedon`, `createdon`, `@search.score`).  For example, to get results ranked (in order of precedence) by relevance, followed by the most recently modified records listed higher:

`"orderby": ["@search.score desc", "modifiedon desc"]`

If the query request includes a filter for a specific table type, `orderby` can optionally specify table-specific columns.

### `propertybag` parameter

A collection of the additional properties for search request. Eg. `appid`, `correlationid`.

### `options` parameter

Options are settings configured to search a search term. Eg. `lucene`, `besteffortsearch`, `groupranking`, `searchmodelall`.

#### Lucerne Query Syntax

The Lucene query syntax supports the following functionality:

| **Functionality** | **Description** |
|---|---|
| Boolean operators | Provides an expanded set compared to simple query syntax.<br/>AND operator; denoted by AND, &&, +<br/>OR operator; denoted by OR, \|\|<br/>NOT operator; denoted by NOT, !, – |
| Wildcards| In addition to a trailing wildcard, also supports a leading wildcard.<br/>Trailing wildcard – "alp\*"<br/>Leading wildcard - "/.\*pine/" |
| Fuzzy search| Supports queries misspelled by up to two characters.<br/>"Uniersty\~" will return "University"<br/>"Blue\~1" will return "glue", "blues" |
| Term boosting| Weighs specific terms in a query differently.<br/>"Rock\^2 electronic" will return results where the matches to "rock" are more important than matches to "electronic". |
| Proximity search| Returns results where terms are within *x* words of each other, for more contextual results.<br/>For example, "airport hotel"\~5 returns results where "airport" and "hotel" are within five words of each other, thus boosting the chances of finding a hotel located close to an airport. |
| Regular expression (regex) search | For example, /\[mh\]otel/ matches "motel" or "hotel". |

## Response

The following is an example of the response from a query.

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
#### [Search endpoint](#tab/search)

**Request**

```http

```
---

The unescaped response contains JSON using the following properties.


|Name|Type|Description|
|---------|---------|---------|
|`Error`|[ErrorDetail](#errordetail)|TODO: find out. Why is this included?|
|`Value`|[`QueryResult`](#queryresult)`[]`|A collection of matching records.|
|`Facets`|`Dictionary<string,` [FacetResult](#facetresult)`[]>`|If facets were requested in the query, a dictionary of facet values.|
|`QueryContext` |[QueryContext](#querycontext)|TODO: find out. It is always null. Why is it included?|
|`Count`|long| If `"Count": true` is included in the body of the request, the count of all documents that match the search, ignoring top and skip|

## Types

The following types are returned by the Query Response.

### ErrorDetail

|Name|Type|Description|
|---------|---------|---------|
|`Code`|string|The error code.|
|`Message`|string|The error message.|
|`PropertyBag`|`Dictionary<string, object>`|Additional error information.|

### QueryResult

|Name|Type|Description|
|---------|---------|---------|
|`Id`|string|The identifier of the record.|
|`EntityName`|string|The logical name of the table.|
|`ObjectTypeCode`|int|The object type code.|
|`Attributes`|`Dictionary<string, object>`|Record attributes|
|`Highlights`|`Dictionary<string, string[]>`|The highlights.|
|`Score`|double|The document score.|

### FacetResult

|Name|Type|Description|
|---------|---------|---------|
|`Count`|long?|The count of documents falling within the bucket described by this facet.|
|`From`|object|Value indicating the inclusive lower bound of the facet's range, or null to indicate that there is no lower bound.|
|`To`|object|Value indicating the exclusive upper bound of the facet's range, or null to indicate that there is no upper bound.|
|`Type`|`Value` \| `Range`|Type of the facet.|
|`Value`|object|Value of the facet, or the inclusive lower bound if it's an interval facet.|
|`OptionalValue`|object|Additional or optional value of the facet, will be populated while faceting on lookups.|


### QueryContext

|Name|Type|Description|
|---------|---------|---------|
|`OriginalQuery`|string|The query string as specified in the request.|
|`AlteredQuery`|string|The query string that Dataverse search used to perform the query. Dataverse search uses the altered query string if the original query string contained spelling mistakes or did not yield optimal results.|
|`Reason`|string[]|The reason behind query alter decision by Dataverse search.|
|`SpellSuggestions`|string[]|The spell suggestion that are the likely words that represent user's intent. This will be populated only when the query was altered by Dataverse search due to spell check.|

## Examples

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
#### [Search endpoint](#tab/search)

**Request**

```http
POST [Organization URI]/api/search/v2.0/query HTTP/1.1
```

---
### See also

[Search for Dataverse records](overview.md)<br />
[Dataverse Search suggest](suggest.md)<br />
[Dataverse Search autocomplete](autocomplete.md)<br />
[Dataverse Search status](status.md)<br />
[Dataverse Search statistics](statistics.md)<br />
[Dataverse Native Search 1.0](search1.0.md)

[!INCLUDE [footer-banner](../../../includes/footer-banner.md)]