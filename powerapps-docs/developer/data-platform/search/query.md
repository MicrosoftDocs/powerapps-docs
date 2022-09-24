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

The query operation returns search results based on a search term.

In addition to a search term, the results returned can be influenced by passing values for the following parameters:


|Name  |Type  |Description  |More information|
|---------|---------|---------|---------|
|`search`|string|**Required** The text to search with. |[search parameter](#search-parameter)|
|`count`|bool|Whether to return the total record count.|[`count` parameter](#count-parameter) |
|`entities`|string|Limits the scope of search to a sub-set of tables. |[entities parameter](#entities-parameter)|
|`facets`|string|Facets support the ability to drill down into data results after they've been retrieved. | [facets parameter](#facets-parameter)|
|`filter`|string|Limits the scope of the search results returned. |[filter parameter](#filter-parameter)|
|`options`|string|Options are settings configured to search a search term. Eg. `lucene`, `besteffortsearch`, `groupranking`, `searchmodelall`.|[`options` parameter](#options-parameter)|
|`orderby`|string|Specifies how to order the results in order of precedence. |[orderby parameter](#orderby-parameter)|
|`propertybag`|string|A collection of the additional properties for search request. Eg. appid, correlationid.|[`propertybag` parameter](#propertybag-parameter)|
|`skip`|int|Specifies the number of search results to skip. |[skip and top parameters](#skip-and-top-parameters)|
|`top`|int|Specifies the number of search results to retrieve. |[skip and top parameters](#skip-and-top-parameters)|

## Parameters

Details for the parameters in the table above can be found below.


### `search` parameter

**Type**: string<br />
**Optional**: false

The search parameter contains the text to search. It is the only required parameter. Search term must be at least three characters long and has a 100 character limit.

#### Simple Search syntax

By default, the search parameter supports simple search syntax as described in the table below:

| **Functionality** | **Description** |
|---|---|
| Boolean operators | AND operator; denoted by `+`<br/>OR operator; denoted by `|`<br/>NOT operator; denoted by `-` |
| Precedence operators | A search term `hotel+(wifi | luxury) `will search for results containing the term `hotel` and either `wifi` or `luxury` (or both). |
| Wildcards            | Trailing wildcard are supported. For example, `Alp*` searches for "alpine". |
| Exact matches        | A query enclosed in quotation marks `" "`.|

> [!NOTE]
> In order to use any search operators as part of the search text, escape the character by prefixing it with a single backslash (`\`). Special characters that require escaping include the following: `+ - & | ! ( ) { } [ ] ^ " ~ * ? : \ /`.

For example, and escaped phone number might look like this: `\+1\(800\)555\-1234`.

Using the [`options` parameter](#options-parameter), you can enable [Lucerne Query Syntax](#lucerne-query-syntax) which enables different operators..

### `count` parameter

**Type**: bool<br />
**Optional**: true

Whether to return the total record count. If this is not set the `Count` response property will be `-1`.

### `entities` parameter

**Type**: string<br />
**Optional**: true

By default all the tables enabled for search will be searched unless you specify a sub-set using the `entities` parameter. 

When you set an entity, you can also specify which columns you want to return and which columns to search. You can also include filter criteria for the table.

To get a list of tables enabled for the environment use the [Search status](status.md) API and look for the tables listed by  `entitylogicalname` within `entitystatusresults`.

The following table shows the schema of an entity:

|Field Name|Type  |Description  |
|---------|---------|---------|
|`name`|string|Required. Logical name of the table. Specifies scope of the query.|
|`selectColumns`|string[]|Optional. List of columns that needs to be projected when table documents are returned in response. If empty, only the table primary name will be returned.  |
|`searchColumns`|string[]|Optional. List of columns to scope the query on.  If empty, only the table primary name will be searched on.|
|`filter`|string|Optional. Filters applied on the entity. |

#### Example

This is an example of some JSON data that uses the schema described above.

```json
[
   {
      "name":"account",
      "selectColumns":["name","address1_city"],
      "searchColumns":["name","address1_city"],
      "filter":"modifiedon ge 2018-01-01T00:00:00Z"
   },
   {
      "name":"contact",
      "selectColumns":["fullname","address1_city"],
      "searchColumns":["fullname","address1_city"],
      "filter":"modifiedon ge 2018-01-01T00:00:00Z"
   }
]
```

To use this data you must escape the string and pass it as the value of the `entities` parameter in the body of the request:

```json
{
    "search": "maria",
    "entities":"[{\"name\":\"account\",\"selectColumns\":[\"name\",\"address1_city\"],\"searchColumns\":[\"name\",\"address1_city\"],\"filter\":\"modifiedon ge 2018-01-01T00:00:00Z\"},{\"name\":\"contact\",\"selectColumns\":[\"fullname\",\"address1_city\"],\"searchColumns\":[\"fullname\",\"address1_city\"],\"filter\":\"modifiedon ge 2018-01-01T00:00:00Z\"}]"
}
```


### `facets` parameter

**Type**: string<br />
**Optional**: true

Facets support the ability to drill down into data results after they've been retrieved. By default, no facets are returned with search results.

#### Facet definition

Facets are defined as an array of strings, for example:

```
[
"entityname,count:100",
"account:primarycontactid,count:100",
"ownerid,count:100",
"modifiedon,values:2019-04-27T00:00:00|2020-03-27T00:00:00|2020-04-20T00:00:00|2020-04-27T00:00:00",
"createdon,values:2019-04-27T00:00:00|2020-03-27T00:00:00|2020-04-20T00:00:00|2020-04-27T00:00:00"
]
```

Each item in the array represents a different way to group the data returned by the query. For each property returned, you can specify appropriate faceting using the values in the following table:


|Facet Type|Description|
|---------|---------|
|`count`|The maximum number of facet terms. The default is 10. There is no upper limit|
|`sort` |Can be set to `count`, `-count`, `value`, `-value`. Use `count` to sort descending by `count`. Use `-count` to sort ascending by `count`. Use `value` to sort ascending by `value`. Use `-value` to sort descending by `value`.|
|`values`|Set to pipe-delimited numeric or Edm.DateTimeOffset values specifying a dynamic set of facet entry values.The values must be listed in sequential, ascending order to get the expected results.|
|`interval`|An integer interval greater than 0 for numbers, or minute, hour, day, week, month, quarter, year for date time values.|
|`timeoffset`|Set to (`[+-]hh:mm`, `[+-]hhmm`, or `[+-]hh`). If used, the timeoffset parameter must be combined with the interval option, and only when applied to a field of type `Edm.DateTimeOffset`. The value specifies the UTC time offset to account for in setting time boundaries.|


> [!NOTE]
> `count` and `sort` can be combined in the same facet specification, but they cannot be combined with `interval` or `values`, and `interval` and `values` cannot be combined together.

Set the `facets` value with an escaped string containing the definition of the facets.

```json
{
    "search": "maria",
    "facets": "[\"entityname,count:100\",\"account:primarycontactid,count:100\",\"ownerid,count:100\",\"modifiedon,values:2019-04-27T00:00:00|2020-03-27T00:00:00|2020-04-20T00:00:00|2020-04-27T00:00:00\",\"createdon,values:2019-04-27T00:00:00|2020-03-27T00:00:00|2020-04-20T00:00:00|2020-04-27T00:00:00\"]"    
}
```

More information:

- [Azure Cognitive Search: Add faceted navigation to a search app](/azure/search/search-faceted-navigation)
- [Azure Cognitive Search REST API > Search Documents > Query Parameters](/rest/api/searchservice/search-documents#query-parameters)

### `filter` parameter

**Type**: string<br />
**Optional**: true

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



### `options` parameter

**Type**: string<br />
**Optional**: true

Options are settings configured to search a search term. Set the `options` value to a serialized array of these options, such as `["lucene","besteffortsearch","groupranking","searchmodelall"]`.

These are the options:

|Option|Description  |
|---------|---------|
|`lucene`|Enables [Lucerne Query Syntax](#lucerne-query-syntax)|
|`besteffortsearch`|Enables intelligent query workflow to return probable set of results if no good matches are found for the search request terms.|
|`groupranking`|Enable ranking of results in the response optimized for display in search results pages where results are grouped by table.|
|`searchmodelall`|Specifiy whether all the search terms must be matched in order to consider the document as a match. Not specifying this flag will default to matching any word in the search term.|

#### Lucerne Query Syntax

The Lucene query syntax supports the following functionality:

| **Functionality** | **Description** |
|---|---|
| Boolean operators | Provides an expanded set compared to simple query syntax.<br/>AND operator; denoted by `AND`, `&&`, `+`<br/>OR operator; denoted by `OR`, `||`<br/>NOT operator; denoted by `NOT`, `!`, `–` |
| Wildcards| In addition to a trailing wildcard, also supports a leading wildcard.<br/>Trailing wildcard – `alp*`<br/>Leading wildcard - `/.*pine/` |
| Fuzzy search| Supports queries misspelled by up to two characters.<br/>`Uniersty~` will return `University`<br/>`Blue~1` will return `glue`, `blues` |
| Term boosting| Weighs specific terms in a query differently.<br/>`Rock^2 electronic` will return results where the matches to `rock` are more important than matches to `electronic`. |
| Proximity search| Returns results where terms are within *x* words of each other, for more contextual results.<br/>For example, `"airport hotel"~5` returns results where `airport` and `hotel` are within five words of each other, thus boosting the chances of finding a hotel located close to an airport. |
| Regular expression (regex) search | For example, `/[mh]otel/`  matches `motel` or `hotel`. |

### `orderby` parameter

**Type**: string<br />
**Optional**: true

Use the `orderby` parameter to override the default ordering. By default, results are listed in descending order of relevance score (@search.score). For results with identical scores, the ordering will be random.

Use a list of comma-separated clauses where each clause consists of a column name followed by `asc` (*ascending*, which is the default) or `desc` (descending).

For a set of results that contain multiple table types, the list of clauses for `orderby` must be globally applicable (for example, `modifiedon`, `createdon`, `@search.score`).  For example, to get results ranked (in order of precedence) by relevance, followed by the most recently modified records listed higher:

`"orderby": ["@search.score desc", "modifiedon desc"]`

If the query request includes a filter for a specific table type, `orderby` can optionally specify table-specific columns.

### `propertybag` parameter

**Type**: string<br />
**Optional**: true

A collection of the additional properties for search request. Eg. `appid`, `correlationid`.

### `skip` and `top` parameters

**Type**: int<br />
**Optional**: true

You can use these parameters together with the [count parameter](#count-parameter) to create a paged experience.

By default, up to 50 results will be returned at a time. You can use `top` to raise it as high as 100, but more commonly you will use `top` to specify a smaller result set, such as 10, and then use `skip` to bypass previously returned results when the user moves to the next page.

## Response

The response from the query operation is an escaped string that includes JSON data.

The unescaped response contains JSON using the following properties.


|Name|Type|Description|
|---------|---------|---------|
|`Error`|[ErrorDetail](#errordetail)|Provides error information from Azure Cognitive search.|
|`Value`|[`QueryResult`](#queryresult)`[]`|A collection of matching records.|
|`Facets`|`Dictionary<string,` [FacetResult](#facetresult)`[]>`|If facets were requested in the query, a dictionary of facet values.|
|`QueryContext` |[QueryContext](#querycontext)|TODO: find out. It is always null. Why is it included?|
|`Count`|long| If `"Count": true` is included in the body of the request, the count of all documents that match the search, ignoring top and skip|

## Types

The following types are returned by the Query Response.

### ErrorDetail

TODO: Why is this included? Why doesn't the service just return an error?
GUESS: This will be a Cognitive Search error

|Name|Type|Description|
|---------|---------|---------|
|`Code`|string|The error code.|
|`Message`|string|The error message.|
|`PropertyBag`|`Dictionary<string, object>`|Additional error information.|

### QueryResult

Each `QueryResult` item returned in the response `Value` property represents a record in Dataverse.

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
TODO: The Console Writeline output of the SDK Sample
```
#### [Web API](#tab/webapi)

**Request**

```http
POST [Organization URI]/api/data/v9.2/searchquery HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json

{
    
}
```

**Response**

```http
HTTP/1.1 200 OK

{}
```
#### [Search 2.0 endpoint](#tab/search)

The parameters and response value using the search 2.0 endpoint are identical to the Web API.

**Request**

```http
POST [Organization URI]/api/search/v2.0/query HTTP/1.1
```

**Response**

```http
HTTP/1.1 200 OK

{}
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