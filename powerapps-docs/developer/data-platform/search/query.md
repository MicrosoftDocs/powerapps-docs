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

The search parameter contains the text to search. It is the only required parameter. It has a 100 character limit.

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

## entities parameter

By default all the tables enabled for search will be searched unless you specify a sub-set using the `entities` parameter. Set this parameter with an array of table logical names.

To get a list of entities enabled for the environment use the [Search Status](overview.md#search-status) API and look for the entities listed by  `entitylogicalname` within `entitystatusresults`.

## facets parameter

Facets support the ability to drill down into data results after they've been retrieved. By default, no facets are returned with search results.

TODO: Establish exactly what developers will do with the facets data and how to set them. This is a mystery:

```
  "facets": ["@search.entityname,count:100",  
    "account.primarycontactid,count:100",  
    "ownerid,count:100",  
    "modifiedon,values:2019-04-27T00:00:00|2020-03-27T00:00:00|2020-04-20T00:00:00|2020-04-27T00:00:00",
    "createdon,values:2019-04-27T00:00:00|2020-03-27T00:00:00|2020-04-20T00:00:00|2020-04-27T00:00:00"]
```


## filter parameter

Filters limit the scope of the search results returned. Use filters to exclude unwanted results.

Apply filters using this syntax: `<table logical name>: <filter>` where the table logical name specifies the entity the filter should be applied to.

Filters use the following query operators:

|Operator|Description|Example|  
|--------------|-----------------|-------------|  
|**Comparison Operators**|||  
|`eq`|Equal|`account:revenue eq 100000`|  
|`ne`|Not Equal|`account:revenue ne 100000`|  
|`gt`|Greater than|`account:revenue gt 100000`|  
|`ge`|Greater than or equal|`account:revenue ge 100000`|  
|`lt`|Less than|`account:revenue lt 100000`|  
|`le`|Less than or equal|`account:revenue le 100000`|  
|**Logical Operators**|||  
|`and`|Logical and|`account:revenue lt 100000 and revenue gt 2000`|  
|`or`|Logical or|`account:name eq 'sample' or name eq 'test'|  
|`not`|Logical negation|`account:not name eq 'sample'`|  
|**Grouping Operators**|||  
|`( )`|Precedence grouping|`account:(name eq 'sample') or name eq 'test') and revenue gt 5000`|  


## returntotalrecordcount or count parameter

Whether to return the total record count. When using the search endpoint use `returntotalrecordcount`. Use `count` when using Dataverse Web API or SDK.


## skip and top parameters

You can use these parameters together with the [returntotalrecordcount or count parameter](#returntotalrecordcount-or-count-parameter) to create a paged experience.
By default, as many as 50 results will be returned at a time. You can use `top` to raise it as high as 100, but more commonly you will use top to specify a smaller result set, such as 10, and then use `skip` to bypass previously returned results when the user moves to the next page.

## orderby parameter

Use the `orderby` parameter to override the default ordering. By default, results are listed in descending order of relevance score (@search.score). For results with identical scores, the ordering will be random.

Use a list of comma-separated clauses where each clause consists of a column name followed by `asc` (*ascending*, which is the default) or `desc` (descending).

For a set of results that contain multiple table types, the list of clauses for `orderby` must be globally applicable (for example, `modifiedon`, `createdon`, `@search.score`).  For example, to get results ranked (in order of precedence) by relevance, followed by the most recently modified records listed higher:

`"orderby": ["@search.score desc", "modifiedon desc"]`

If the query request includes a filter for a specific table type, `orderby` can optionally specify table-specific columns.

## searchmode parameter

Specifies whether `any` or `all` the search terms must be matched to count the
document as a match. The default is `any`.

The `searchMode` parameter on a query request controls whether a term with the NOT operator is AND'ed or OR'ed with other terms in the query (assuming there is no + or | operator on the other terms).

Using `searchMode=any` increases the recall of queries by including more results, and by default will be interpreted as `OR NOT`. For example, `wifi -luxury` will match documents that either contain the term `wifi` or those that don't contain the term `luxury`.

Using `searchMode=all` increases the precision of queries by including fewer results, and by default will be interpreted as `AND NOT`. For example, `wifi -luxury` will match documents that contain the term `wifi` and don't contain the term `luxury`.

## searchtype parameter

When you use `"searchtype": "full"`, you specify that Lucerne Query syntax be used.

### Lucerne Query Syntax

The Lucene query syntax supports the following functionality:

| **Functionality** | **Description** |
|---|---|
| Boolean operators | Provides an expanded set compared to simple query syntax.<br/>AND operator; denoted by AND, &&, +<br/>OR operator; denoted by OR, \|\|<br/>NOT operator; denoted by NOT, !, – |
| Wildcards| In addition to a trailing wildcard, also supports a leading wildcard.<br/>Trailing wildcard – "alp\*"<br/>Leading wildcard - "/.\*pine/" |
| Fuzzy search| Supports queries misspelled by up to two characters.<br/>"Uniersty\~" will return "University"<br/>"Blue\~1" will return "glue", "blues" |
| Term boosting| Weighs specific terms in a query differently.<br/>"Rock\^2 electronic" will return results where the matches to "rock" are more important than matches to "electronic". |
| Proximity search| Returns results where terms are within *x* words of each other, for more contextual results.<br/>For example, "airport hotel"\~5 returns results where "airport" and "hotel" are within five words of each other, thus boosting the chances of finding a hotel located close to an airport. |
| Regular expression (regex) search | For example, /\[mh\]otel/ matches "motel" or "hotel". |


## propertybag parameter

A collection of the additional properties for search request. Eg. appid, correlationid.

TODO: Only find this in <xref:Microsoft.Dynamics.CRM.searchquery>

## options parameter

Options are settings configured to search a search term. Eg. lucene, besteffortsearch, groupranking, searchmodelall.

TODO: Only find this in <xref:Microsoft.Dynamics.CRM.searchquery>

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