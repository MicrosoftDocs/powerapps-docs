---
title: "Dataverse Search query (Microsoft Dataverse) | Microsoft Docs"
description: "Use Dataverse search query to return search results across multiple tables."
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
# Dataverse Search query

The query operation returns search results based on a search term.

In addition to a search term, the results returned can be influenced by passing values for the following parameters:


|Name  |Type  |Description  |More information|
|---------|---------|---------|---------|
|`search`|string|**Required**. The text to search with. |[search parameter](#search-parameter)|
|`count`|bool|Whether to return the total record count.|[`count` parameter](#count-parameter) |
|`entities`|string|Limits the scope of search to a subset of tables. |[entities parameter](#entities-parameter)|
|`facets`|string|Facets support the ability to drill down into data results after they've been retrieved. | [facets parameter](#facets-parameter)|
|`filter`|string|Limits the scope of the search results returned. |[filter parameter](#filter-parameter)|
|`options`|string|Options are settings configured to search a search term.|[`options` parameter](#options-parameter)|
|`orderby`|string|Specifies how to order the results in order of precedence. |[orderby parameter](#orderby-parameter)|
|`skip`|int|Specifies the number of search results to skip. |[skip and top parameters](#skip-and-top-parameters)|
|`top`|int|Specifies the number of search results to retrieve. |[skip and top parameters](#skip-and-top-parameters)|

## Parameters

This section includes details about the parameters introduced in the table above.

### `search` parameter

**Type**: string<br />
**Optional**: false

The search parameter contains the text to search. It's the only required parameter. Search term must be at least one character long and has a 100 character limit.

#### Simple Search syntax

By default, the search parameter supports simple search syntax as described in the following table:

| **Functionality** | **Description** |
|---|---|
| Boolean operators | AND operator; denoted by `+`<br/>OR operator; denoted by `|`<br/>NOT operator; denoted by `-` |
| Precedence operators | A search term `hotel+(wifi | luxury)` searches for results containing the term `hotel` and either `wifi` or `luxury` (or both). |
| Wildcards            | Trailing wildcard are supported. For example, `Alp*` searches for "alpine". |
| Exact matches        | A query enclosed in quotation marks `" "`.|

> [!NOTE]
> In order to use any search operators as part of the search text, escape the character by prefixing it with a single backslash (`\`). Special characters that require escaping include the following: `+ - & | ! ( ) { } [ ] ^ " ~ * ? : \ /`.

For example, an escaped phone number might look like this: `\+1\(800\)555\-1234`.

Using the [`options` parameter](#options-parameter), you can enable [Lucerne Query Syntax](#lucerne-query-syntax) that enables different operators.

### `count` parameter

**Type**: bool<br />
**Optional**: true

Whether to return the total record count. If you don't set this parameter, the `Count` response property is `-1`.

### `entities` parameter

**Type**: string<br />
**Optional**: true

By default all the tables enabled for search are searched unless you specify a subset using the `entities` parameter. 

When you set an entity, you can also specify which columns you want to return and which columns to search. You can also include filter criteria for the table.

To get a list of tables enabled for the environment, use the [Search Status](statistics-status.md#status) API and look for the tables listed by  `entitylogicalname` within `entitystatusresults`.

### SearchEntity type

Use this type to compose the array of tables to pass to the `entities` parameter.

|Field Name|Type  |Description  |
|---------|---------|---------|
|`name`|string|Required. Logical name of the table. Specifies scope of the query.|
|`selectColumns`|string[]|Optional. List of columns that needs to be projected when table documents are returned in response. If empty, only the table primary name is returned.  |
|`searchColumns`|string[]|Optional. List of columns to scope the query on.  If empty, only the table primary name is searched on.|
|`filter`|string|Optional. Filters applied on the entity. |

#### Example

The following is an example of some JSON data that uses the schema described above.

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

To use this data, you must escape the string and pass it as the value of the `entities` parameter in the body of the request:

```json
{
    "search": "maria",
    "entities":"[{\"name\":\"account\",\"selectColumns\":[\"name\",\"address1_city\"],\"searchColumns\":[\"name\",\"address1_city\"],\"filter\":\"modifiedon ge 2018-01-01T00:00:00Z\"},{\"name\":\"contact\",\"selectColumns\":[\"fullname\",\"address1_city\"],\"searchColumns\":[\"fullname\",\"address1_city\"],\"filter\":\"modifiedon ge 2018-01-01T00:00:00Z\"}]"
}
```


### `facets` parameter

**Type**: string<br />
**Optional**: true

The facet parameter is optional.  The string might contain parameters to customize the faceting, expressed as comma-separated name-value pairs. Use facets to group your search results.


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
|`count`|The maximum number of facet terms. The default is 10. There's no upper limit|
|`sort` |Can be set to `count`, `-count`, `value`, `-value`. Use `count` to sort descending by `count`. Use `-count` to sort ascending by `count`. Use `value` to sort ascending by `value`. Use `-value` to sort descending by `value`.|
|`values`|Set to pipe-delimited numeric or `Edm.DateTimeOffset` values specifying a dynamic set of facet entry values. The values must be listed in sequential, ascending order to get the expected results.|
|`interval`|An integer interval greater than zero for numbers, or minute, hour, day, week, month, quarter, year for date time values.|
|`timeoffset`|Set to (`[+-]hh:mm`, `[+-]hhmm`, or `[+-]hh`). If used, the `timeoffset` parameter must be combined with the interval option, and only when applied to a field of type `Edm.DateTimeOffset`. The value specifies the UTC time offset to account for in setting time boundaries.|


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

Filters limit the scope of the search results returned. Use filters to exclude unwanted results. This is a top level filter that helps filter common columns across multiple entities like `createdon` or `modifiedon` etc.

Apply filters using this syntax: `<attribute logical name> <filter>` where the table logical name specifies the entity the filter should be applied to.

Filters use the following query operators:

|Operator|Description|Example|
|--------|-----------|-------|
|**Comparison Operators**|&nbsp;|&nbsp;|
|`eq`|Equal|`revenue eq 100000`|
|`ne`|Not Equal|`revenue ne 100000`|
|`gt`|Greater than|`revenue gt 100000`|
|`ge`|Greater than or equal|`revenue ge 100000`|
|`lt`|Less than|`revenue lt 100000`|
|`le`|Less than or equal|`revenue le 100000`|
|**Logical Operators**|&nbsp;|&nbsp;|
|`and`|Logical and|`revenue lt 100000 and revenue gt 2000`|
|`or`|Logical or|`name eq 'sample' or name eq 'test'`|
|`not`|Logical negation|`not name eq 'sample'`|
|**Grouping Operators**|&nbsp;|&nbsp;|
|`( )`|Precedence grouping|`(name eq 'sample') or name eq 'test') and revenue gt 5000`|


### `options` parameter

**Type**: string<br />
**Optional**: true

Options are settings configured to search a search term. Set the `options` value to a serialized `Dictionary<string, string>` of these options, such as `"{'querytype': 'lucene', 'searchmode': 'all', 'besteffortsearchenabled': 'true', 'grouprankingenabled': 'true'}"`.

The following table lists the options:

|Option|Description  |
|---------|---------|
|`querytype`| Values can be `simple` or `lucene` [Lucerne Query Syntax](#lucerne-query-syntax)|
|`besteffortsearchenabled`|Enables intelligent query workflow to return probable set of results if no good matches are found for the search request terms.|
|`groupranking`|Enable ranking of results in the response optimized for display in search results pages where results are grouped by table.|
|`searchmode`|When specified as `all` the search terms must be matched in order to consider the document as a match. Setting its value to `any` defaults to matching any word in the search term.|

#### Lucerne Query Syntax

The Lucene query syntax supports the following functionality:

| **Functionality** | **Description** |
|---|---|
| Boolean operators | Provides an expanded set compared to simple query syntax.<br/>AND operator; denoted by `AND`, `&&`, `+`<br/>OR operator; denoted by `OR`, `||`<br/>NOT operator; denoted by `NOT`, `!`, `–` |
| Wildcards| In addition to a trailing wildcard, also supports a leading wildcard.<br/>Trailing wildcard – `alp*`<br/>Leading wildcard - `/.*pine/` |
| Fuzzy search| Supports queries misspelled by up to two characters.<br/>`Uniersty~` returns `University`<br/>`Blue~1` returns `glue`, `blues` |
| Term boosting| Weighs specific terms in a query differently.<br/>`Rock^2 electronic` returns results where the matches to `rock` are more important than matches to `electronic`. |
| Proximity search| Returns results where terms are within *x* words of each other, for more contextual results.<br/>For example, `"airport hotel"~5` returns results where `airport` and `hotel` are within five words of each other, thus boosting the chances of finding a hotel located close to an airport. |
| Regular expression (regex) search | For example, `/[mh]otel/`  matches `motel` or `hotel`. |

### `orderby` parameter

**Type**: string<br />
**Optional**: true

Use the `orderby` parameter to override the default ordering. By default, results are listed in descending order of relevance score (`@search.score`). For results with identical scores, the ordering is random. You can only use this parameter when query type is lucene with wildcard characters in the query string.

Use a list of comma-separated clauses where each clause consists of a column name followed by `asc` (*ascending*, which is the default) or `desc` (descending).

For a set of results that contain multiple table types, the list of clauses for `orderby` must be globally applicable (for example, `modifiedon`, `createdon`, `@search.score`). For example, to get results ranked (in order of precedence) by relevance, followed by the most recently modified records listed higher:

`"orderby": ["@search.score desc", "modifiedon desc"]`

If the query request includes a filter for a specific table type, `orderby` can optionally specify table-specific columns.

### `skip` and `top` parameters

**Type**: int<br />
**Optional**: true

You can use these parameters together with the [count parameter](#count-parameter) to create a paged experience.

By default, up to 50 results are returned at a time. You can use `top` to raise it as high as 100, but more commonly you'll use `top` to specify a smaller result set, such as 10, and then use `skip` to bypass previously returned results when the user moves to the next page.

## Response

The response from the query operation is an escaped string that includes JSON data.

The unescaped response contains JSON using the following properties.


|Name|Type|Description|
|---------|---------|---------|
|`Error`|[ErrorDetail](#errordetail)|Provides error information from Azure Cognitive search.|
|`Value`|[`QueryResult`](#queryresult)`[]`|A collection of matching records.|
|`Facets`|`Dictionary<string,` [FacetResult](#facetresult)`[]>`|If facets were requested in the query, a dictionary of facet values.|
|`QueryContext` |[QueryContext](#querycontext)|This property is used for backend search. It's included for future feature releases and isn't currently used.|
|`Count`|long| If `"Count": true` is included in the body of the request, the count of all documents that match the search, ignoring top and skip|

### Response Types

This section describes the types returned with the response.

#### ErrorDetail

The Azure Cognitive search error returned as part of the response.

|Name|Type|Description|
|---------|---------|---------|
|`code`|string|The error code.|
|`message`|string|The error message.|
|`propertybag`|`Dictionary<string, object>`|More error information.|

#### QueryResult

Each `QueryResult` item returned in the response `Value` property represents a record in Dataverse.

|Name|Type|Description|
|---------|---------|---------|
|`Id`|string|The identifier of the record.|
|`EntityName`|string|The logical name of the table.|
|`ObjectTypeCode`|int|The object type code.|
|`Attributes`|`Dictionary<string, object>`|Record attributes|
|`Highlights`|`Dictionary<string, string[]>`|The highlights.|
|`Score`|double|The document score.|

#### FacetResult

A facet query result that reports the number of documents with a field falling within a particular range or having a particular value or interval.

|Name|Type|Description|
|---------|---------|---------|
|`count`|long?|The count of documents falling within the bucket described by this facet.|
|`from`|object|Value indicating the inclusive lower bound of the facet's range, or null to indicate that there's no lower bound.|
|`to`|object|Value indicating the exclusive upper bound of the facet's range, or null to indicate that there's no upper bound.|
|`type`|`Value` \| `Range`|Type of the facet.|
|`value`|object|Value of the facet, or the inclusive lower bound if it's an interval facet.|
|`optionalvalue`|object|Another or optional value of the facet, populated while faceting on lookups.|


#### QueryContext

The query context returned as part of response. This property is used for backend search. It's included for future feature releases and isn't currently used.

|Name|Type|Description|
|---------|---------|---------|
|`originalquery`|string|The query string as specified in the request.|
|`alteredquery`|string|The query string that Dataverse search used to perform the query. Dataverse search uses the altered query string if the original query string contained spelling mistakes or didn't yield optimal results.|
|`reason`|string[]|The reasons behind query alter decision by Dataverse search.|
|`spellsuggestions`|string[]|The spell suggestion that is the likely words that represent user's intent. Populated only when Dataverse alters the query search due to spell check.|

## Examples

The following examples show how to use the query operation. These examples perform a search operation on the account and contact tables `name` and `fullname` columns respectively, for records created later than August 15, 2022 and orders the top seven results by the `createdon` field, descending.

### [SDK for .NET](#tab/sdk)

This example is from the [SDK for .NET search operations sample](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/CSharp-NETCore/Search) on GitHub. The static `OutputSearchQuery` method accepts a value for the [search parameter](#search-parameter).

```csharp
/// <summary>
/// Demonstrate query API
/// </summary>
/// <param name="service">The authenticated IOrganizationService instance to use.</param>
/// <param name="searchTerm">The term to search for</param>
/// <returns></returns>
static void OutputSearchQuery(IOrganizationService service, string searchTerm)
{
    Console.WriteLine("OutputSearchQuery START\n");

    searchqueryRequest request = new() { 
        search = searchTerm,
        count = true,
        top = 7,
        entities = JsonConvert.SerializeObject(new List<SearchEntity>()
        {
            new SearchEntity()
            {
                Name = "account",
                SelectColumns = new List<string>() { "name", "createdon" },
                SearchColumns = new List<string>() { "name" },
                Filter = "statecode eq 0"
            },
            new SearchEntity()
            {
                Name = "contact",
                SelectColumns = new List<string>() { "fullname", "createdon" },
                SearchColumns = new List<string>() { "fullname" },
                Filter = "statecode eq 0"
            }
        }),
        orderby = JsonConvert.SerializeObject(new List<string>() { "createdon desc" }),
        filter = "createdon gt 2022-08-15"

    };
    
    var searchqueryResponse = (searchqueryResponse)service.Execute(request);

    var queryResults = JsonConvert.DeserializeObject<SearchQueryResults>(searchqueryResponse.response);
  

    Console.WriteLine($"\tCount:{queryResults.Count}");
    Console.WriteLine("\tValue:");
    queryResults.Value.ForEach(result =>
    {

        Console.WriteLine($"\t\tId:{result.Id}");
        Console.WriteLine($"\t\tEntityName:{result.EntityName}");
        Console.WriteLine($"\t\tObjectTypeCode:{result.ObjectTypeCode}");
        Console.WriteLine("\t\tAttributes:");
        foreach (string key in result.Attributes.Keys)
        {
            Console.WriteLine($"\t\t\t{key}:{result.Attributes[key]}");
        }
        Console.WriteLine("\t\tHighlights:");
        foreach (string key in result.Highlights.Keys)
        {
            Console.WriteLine($"\t\t\t{key}:");

            foreach (string value in result.Highlights[key])
            {
                Console.WriteLine($"\t\t\t\t{value}:");
            }
        }
        Console.WriteLine($"\t\tScore:{result.Score}\n");

    });
    Console.WriteLine("OutputSearchQuery END\n");
}
```

#### Output

When you invoke the `OutputSearchQuery` method with an authenticated instance of the [ServiceClient](xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient) class with the `searchTerm` set to "Contoso":

```csharp
OutputSearchQuery(service: serviceClient, searchTerm: "Contoso");
```

The output looks something like the following:

```console
OutputSearchQuery START

        Count:1
        Value:
                Id:8b35eda1-ef69-ee11-9ae7-000d3a88a4a2
                EntityName:account
                ObjectTypeCode:0
                Attributes:
                        @search.objecttypecode:1
                        name:Contoso Pharmaceuticals (sample)
                        createdon:10/13/2023 5:41:21 PM
                        createdon@OData.Community.Display.V1.FormattedValue:10/13/2023 5:41 PM
                Highlights:
                        name:
                                {crmhit}Contoso{/crmhit} Pharmaceuticals (sample):
                Score:4.986711

OutputSearchQuery END
```

#### Supporting classes

The `OutputSearchQuery` method depends on the following supporting classes to send the request and process the result:

##### searchqueryRequest and searchqueryResponse classes

These classes are generated using Power Platform CLI [pac modelbuilder build](/power-platform/developer/cli/reference/modelbuilder#pac-modelbuilder-build) command as described in [Generate early-bound classes for the SDK for .NET](../org-service/generate-early-bound-classes.md).

##### SearchEntity class

Used to compose [SearchEntity type](#searchentity-type) data.

```csharp
public sealed class SearchEntity
{
    /// <summary>
    /// Gets or sets the logical name of the table. Specifies scope of the query.
    /// </summary>
    [DataMember(Name = "name", IsRequired = true)]
    public string Name { get; set; }

    /// <summary>
    /// Gets or sets the list of columns that needs to be projected when table documents are returned in response. 
    /// If empty, only PrimaryName will be returned.
    /// </summary>
    [DataMember(Name = "selectcolumns")]
    public List<string> SelectColumns { get; set; }

    /// <summary>
    /// Gets or sets the list of columns to scope the query on.
    /// If empty, only PrimaryName will be searched on. 
    /// </summary>
    [DataMember(Name = "searchcolumns")]
    public List<string> SearchColumns { get; set; }

    /// <summary>
    /// Gets or sets the filters applied on the entity.
    /// </summary>
    [DataMember(Name = "filter")]
    public string Filter { get; set; }
}
```

##### SearchQueryResults class

Use to deserialize JSON data from the `searchqueryResponse.response` string property.

```csharp
public sealed class SearchQueryResults
{
    /// <summary>
    /// Provides error information from Azure Cognitive search.
    /// </summary>
    public ErrorDetail? Error { get; set; }

    /// <summary>
    /// A collection of matching records.
    /// </summary>
    public List<QueryResult>? Value { get; set; }

    /// <summary>
    /// If facets were requested in the query, a dictionary of facet values.
    /// </summary>
    public Dictionary<string, IList<FacetResult>>? Facets { get; set; }

    /// <summary>
    /// The query context returned as part of response. This property is used for backend search. It is included for future feature releases and is not currently used.
    /// </summary>
    public QueryContext? QueryContext { get; set; }

    /// <summary>
    /// If `"Count": true` is included in the body of the request, the count of all documents that match the search, ignoring top and skip.
    /// </summary>
    public long Count { get; set; }
}
```

##### ErrorDetail class

Used to deserialize the [ErrorDetail](#errordetail) data.

```csharp
public sealed class ErrorDetail
{
    /// <summary>
    /// Gets or sets the error code.
    /// </summary>
    [DataMember(Name = "code")]
    public string Code { get; set; }

    /// <summary>
    /// Gets or sets the error message.
    /// </summary>
    [DataMember(Name = "message")]
    public string Message { get; set; }

    /// <summary>
    /// Gets or sets additional error information.
    /// </summary>
    [DataMember(Name = "propertybag")]
    public Dictionary<string, object> PropertyBag { get; set; }
}
```

##### QueryResult class

Used to deserialize the [QueryResult](#queryresult) data.

```csharp
public sealed class QueryResult
{
    /// <summary>
    /// Gets or sets the identifier of the record
    /// </summary>
    public string Id { get; set; }

    /// <summary>
    /// Gets or sets the logical name of the table
    /// </summary>
    public string EntityName { get; set; }

    /// <summary>
    /// Gets or sets the object type code
    /// </summary>
    public int ObjectTypeCode { get; set; }

    /// <summary>
    /// Gets or sets the record attributes
    /// </summary>
    public Dictionary<string, object> Attributes { get; set; }

    /// <summary>
    /// Gets or sets the highlights
    /// </summary>
    public Dictionary<string, string[]> Highlights { get; set; }

    // Gets or sets the document score
    public double Score { get; set; }
}
```

##### FacetResult class

Used to deserialize the [FacetResult](#facetresult) data.

```csharp
public sealed class FacetResult
{
    /// <summary>
    /// Gets or sets the count of documents falling within the bucket described by this facet.
    /// </summary>
    [DataMember(Name = "count")]
    public long? Count { get; set; }

    /// <summary>
    /// Gets or sets value indicating the inclusive lower bound of the facet's range, or null to indicate that there is no lower bound.
    /// </summary>
    [DataMember(Name = "from")]
    public object From { get; set; }

    /// <summary>
    /// Gets or sets value indicating the exclusive upper bound of the facet's range, or null to indicate that there is no upper bound.
    /// </summary>
    [DataMember(Name = "to")]
    public object To { get; set; }

    /// <summary>
    /// Gets or sets type of the facet - Value or Range.
    /// </summary>
    [DataMember(Name = "type")]
    public FacetType Type { get; set; }

    /// <summary>
    /// Gets or sets value of the facet, or the inclusive lower bound if it's an interval facet.
    /// </summary>
    [DataMember(Name = "value")]
    public object Value { get; set; }

    /// <summary>
    /// Gets or sets additional/ Optional value of the facet, will be populated while faceting on lookups.
    /// </summary>
    [DataMember(Name = "optionalvalue")]
    public object OptionalValue { get; set; }
}
```

##### FacetType class

Specifies the type of a facet query result.

```csharp
public enum FacetType
{
    /// <summary>
    /// The facet counts documents with a particular field value.
    /// </summary>
    [EnumMember(Value = "value")]
    Value = 0,

    /// <summary>
    /// The facet counts documents with a field value in a particular range.
    /// </summary>
    [EnumMember(Value = "range")]
    Range = 1,
}
```

##### QueryContext class

Used to deserialize the [QueryContext](#querycontext) data.

```csharp
public sealed class QueryContext
{
    /// <summary>
    /// Gets or sets the query string as specified in the request.
    /// </summary>
    [DataMember(Name = "originalquery")]
    public string OriginalQuery { get; set; }

    /// <summary>
    /// Gets or sets the query string that Dataverse search used to perform the query. 
    /// Dataverse search uses the altered query string if the original query string contained spelling mistakes or did not yield optimal results.
    /// </summary>
    [DataMember(Name = "alteredquery")]
    public string AlteredQuery { get; set; }

    /// <summary>
    /// Gets or sets the reason behind query alter decision by Dataverse search.
    /// </summary>
    [DataMember(Name = "reason")]
    public List<string> Reason { get; set; }

    /// <summary>
    /// Gets or sets the spell suggestion that are the likely words that represent user's intent. 
    /// This will be populated only when the query was altered by Dataverse search due to spell check.
    /// </summary>
    [DataMember(Name = "spellsuggestions")]
    public List<string> SpellSuggestions { get; set; }
}
```

### [Web API](#tab/webapi)

Use the [searchquery action](xref:Microsoft.Dynamics.CRM.searchquery) to receive a [searchqueryResponse complex type](xref:Microsoft.Dynamics.CRM.searchqueryResponse).

This example is from the [Web API search operations sample](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/webapi/CSharp-NETx/Search) on GitHub.

The formatted JSON passed to the string `entities` parameter looks like this:

```json
[
  {
    "Name": "account",
    "SelectColumns": [
      "name",
      "createdon"
    ],
    "SearchColumns": [
      "name"
    ],
    "Filter": "statecode eq 0"
  },
  {
    "Name": "contact",
    "SelectColumns": [
      "fullname",
      "createdon"
    ],
    "SearchColumns": [
      "fullname"
    ],
    "Filter": "statecode eq 0"
  }
]
```

**Request**

```http
POST [Organization Uri]/api/data/v9.2/searchquery
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
Content-Type: application/json; charset=utf-8
Content-Length: 471

{
  "top": 7,
  "search": "Contoso",
  "skip": 0,
  "entities": "[{\"Name\":\"account\",\"SelectColumns\":[\"name\",\"createdon\"],\"SearchColumns\":[\"name\"],\"Filter\":\"statecode eq 0\"},{\"Name\":\"contact\",\"SelectColumns\":[\"fullname\",\"createdon\"],\"SearchColumns\":[\"fullname\"],\"Filter\":\"statecode eq 0\"}]",
  "orderby": "[\"createdon desc\"]",
  "filter": "createdon gt 2022-08-15",
  "count": true,
  "options": "null",
  "facets": "null"
}
```

**Response**

```http
HTTP/1.1 200 OK
OData-Version: 4.0

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.searchqueryResponse",
  "response": "{\"Error\":null,\"Value\":[{\"Id\":\"8b35eda1-ef69-ee11-9ae7-000d3a88a4a2\",\"EntityName\":\"account\",\"ObjectTypeCode\":0,\"Attributes\":{\"@search.objecttypecode\":1,\"name\":\"Contoso Pharmaceuticals (sample)\",\"createdon\":\"2023-10-13T17:41:21Z\",\"createdon@OData.Community.Display.V1.FormattedValue\":\"10/13/2023 5:41 PM\"},\"Highlights\":{\"name\":[\"{crmhit}Contoso{/crmhit} Pharmaceuticals (sample)\"]},\"Score\":4.95567}],\"Facets\":{},\"QueryContext\":null,\"Count\":1}"
}
```

The formatted JSON value for the string `response` property looks like this:

```json
{
  "Error": null,
  "Value": [
    {
      "Id": "8b35eda1-ef69-ee11-9ae7-000d3a88a4a2",
      "EntityName": "account",
      "ObjectTypeCode": 0,
      "Attributes": {
        "@search.objecttypecode": 1,
        "name": "Contoso Pharmaceuticals (sample)",
        "createdon": "2023-10-13T17:41:21Z",
        "createdon@OData.Community.Display.V1.FormattedValue": "10/13/2023 5:41 PM"
      },
      "Highlights": {
        "name": [
          "{crmhit}Contoso{/crmhit} Pharmaceuticals (sample)"
        ]
      },
      "Score": 4.95567
    }
  ],
  "Facets": {},
  "QueryContext": null,
  "Count": 1
}
```

#### [Search 2.0 endpoint](#tab/search)

The request parameters and the response from the `search/v2.0/query` endpoint is the same as the Web API. Only the URL is different.

**Request URL**

```http
POST [Organization Uri]/api/search/v2.0/query
```

---

### See also

[Search for Dataverse records](overview.md)   
[Dataverse Search suggest](suggest.md)   
[Dataverse Search autocomplete](autocomplete.md)   
[Dataverse Search statistics and status](statistics-status.md)   
[Dataverse legacy search](legacy.md)

[!INCLUDE [footer-banner](../../../includes/footer-banner.md)]
