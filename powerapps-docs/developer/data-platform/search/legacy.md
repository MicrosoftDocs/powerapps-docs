---
title: "Dataverse search (legacy) (Microsoft Dataverse)| Microsoft Docs"
description: "Dataverse legacy search remains available but we recommend you use Dataverse Search 2.0."
ms.date: 10/20/2023
ms.topic: article
author: seanwat-msft
ms.author: seanwat
ms.reviewer: jdaly
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
 - JimDaly
 - jeromeblouinms
---

# Dataverse search (legacy)

> [!IMPORTANT]
> This documentation is for the legacy Dataverse search endpoint. We recommend that you use the latest Dataverse search endpoint. More information: [Search for Dataverse records](overview.md)

To begin using the legacy Dataverse search (version 1.0), your application issues an HTTP POST
request to start a Dataverse search. When searching
data, specify optional properties in the request body to set criteria for how the environment
data is to be searched.

The legacy Dataverse search has three endpoints that can be used in Power Apps ([make.powerapps.com](https://make.powerapps.com)):

- **Search**: `/api/search/v1.0/query` Provides a search results page.

- **Suggestions**: `/api/search/v1.0/suggest` Provides suggestions as the user enters text into a form field.

- **Autocomplete**: `/api/search/v1.0/autocomplete` Provides autocompletion of input as the user enters text into a
    form field.

The following sections describe how to access the previously mentioned search
capabilities from application code.

## Search

The following example shows the minimum syntax of a Dataverse search HTTP request.

```http
POST [Organization URI]/api/search/v1.0/query
{  
  "search": "<search term>"
}
```

The `search` property value contains the term to be searched for and has a
100-character limit.

A successful search response returns an HTTP status of 200 and consists of:

- `value`: a list of tables. By default, 50 results are returned. This property also
    includes search highlights, which indicate matches to the `search` property
    value contained within the `crmhit` tag of the response.

- `totalrecordcount`: The total count of results (of type long). A value of &minus;1
    is returned if `returntotalrecordcount` is set to **false** (default).

- `facets`: The facet results.

In addition, you can add one or more properties to the payload to customize how the
search is to be done and which results are returned. The supported properties are indicated in the following section.

### Query properties

The following properties are supported for Dataverse search using the query endpoint.

#### `entities:[list<string>]` (optional)

The default table list searches across all Dataverse search&ndash;configured tables
and columns. The administrator configures the default list when Dataverse search is enabled.

#### `facets:[list<string>]` (optional)

Facets support the ability to drill down into data results after they've been
retrieved.

```http
POST [Organization URI]/api/search/v1.0/query
{  
  "search": "maria",

  "facets": ["@search.entityname,count:100",  
    "account.primarycontactid,count:100",  
    "ownerid,count:100",  
    "modifiedon,values:2019-04-27T00:00:00|2020-03-27T00:00:00|2020-04-20T00:00:00|2020-04-27T00:00:00",
    "createdon,values:2019-04-27T00:00:00|2020-03-27T00:00:00|2020-04-20T00:00:00|2020-04-27T00:00:00"]
}
```

#### `filter:[string]` (optional)

Filters are applied while searching data and are specified in an OData-style
syntax.

```http
POST [Organization URI]/api/search/v1.0/query
{  
  "search": "maria",

  "filter": "account:modifiedon ge 2020-04-27T00:00:00,
    activities: regardingobjecttypecode eq 'account', annotation:objecttypecode eq 'account',
    incident: (prioritycode eq 1 or prioritycode eq 2)"
}
```

#### `returntotalrecordcount: true | false` (optional)

Specify **true** to return the total record count; otherwise **false**. The default
is **false**.

#### `skip:[int]` (optional)

Specifies the number of search results to skip.

#### `top:[int]` (optional)

Specifies the number of search results to retrieve. The default is 50, and the maximum value is 100.

#### `orderby:[list<string>]` (optional)

A list of comma-separated clauses where each clause consists of a column name followed by 'asc' (ascending, which is the default) or 'desc' (descending). This list specifies how to order the results in order of precedence. By default, results are listed in descending order of relevance score (@search.score). For results with identical scores, the ordering is random.

For a set of results that contain multiple table types, the list of clauses for `orderby` must be globally applicable (for example, modifiedon, createdon, @search.score). Note that specifying the `orderby` property overrides the default. For example, to get results ranked (in order of precedence) by relevance, followed by the most recently modified records listed higher:

`"orderby": ["@search.score desc", "modifiedon desc"]`

If the query request includes a filter for a specific table type, `orderby` can optionally specify table-specific columns.

#### `searchmode:any | all` (optional)

Specifies whether `any` or `all` the search terms must be matched to count the
document as a match. The default is `any`.

> [!NOTE]
> The `searchMode` property on a query request body controls whether a term with the NOT operator is AND'ed or OR'ed with other terms in the query (assuming there is no + or | operator on the other terms).
>
> Using `"searchMode": "any"` increases the recall of queries by including more results, and by default will be interpreted as "OR NOT". For example, "wifi -luxury" will match documents that either contain the term "wifi" or those that don't contain the term "luxury".
>
> Using `"searchMode": "all"` increases the precision of queries by including fewer results, and by default will be interpreted as "AND NOT". For example, "wifi -luxury" will match documents that contain the term "wifi" and don't contain the term "luxury".

#### `searchtype:simple | full` (optional)

The search type specifies the syntax of a search query. Using `simple` selects
simple query syntax and `full` selects Lucene query syntax. The default is
`simple`.

The simple query syntax supports the following functionality:

| **Functionality** | **Description** |
|---|---|
| Boolean operators | AND operator; denoted by +<br/>OR operator; denoted by \|<br/>NOT operator; denoted by \- |
| Precedence operators | A search term "hotel+(wifi \| luxury)" searches for results containing the term "hotel" and either "wifi" or "luxury" (or both). |
| Wildcards            | Trailing wildcard are supported. For example, "Alp\*" searches for "alpine". |
| Exact matches        | A query enclosed in quotation marks " ".|

The Lucene query syntax supports the following functionality:

| **Functionality** | **Description** |
|---|---|
| Boolean operators | Provides an expanded set compared to simple query syntax.<br/>AND operator; denoted by AND, +<br/>OR operator; denoted by OR, \|\|<br/>NOT operator; denoted by NOT, !, – |
| Precedence operators              | The same functionality as simple query syntax. |
| Wildcards                         | In addition to a trailing wildcard, also supports a leading wildcard.<br/>Trailing wildcard – "alp\*"<br/>Leading wildcard - "/.\*pine/" |
| Fuzzy search                      | Supports queries misspelled by up to two characters.<br/>"Uniersty\~" returns "University"<br/>"Blue\~1" returns "glue", "blues" |
| Term boosting                     | Weighs specific terms in a query differently.<br/>"Rock\^2 electronic" returns results where the matches to "rock" are more important than matches to "electronic". |
| Proximity search                  | Returns results where terms are within *x* words of each other, for more contextual results.<br/>For example, "airport hotel"\~5 returns results where "airport" and "hotel" are within five words of each other, thus boosting the chances of finding a hotel located close to an airport. |
| Regular expression (regex) search | For example, /\[mh\]otel/ matches "motel" or "hotel". |

> [!NOTE]
> Wildcards are used only for word completion in Dataverse search. As a rule, querying with a leading wildcard will take significantly longer than not using a wildcard, so we encourage you to explore alternative ways to find what you're looking for and only use leading wildcards sparingly, if at all.

In order to use any of the search operators as part of the search text, escape the character by prefixing it with a single backslash (\\). Special characters that require escaping include the following: `+ - & | ! ( ) { } [ ] ^ " ~ * ? : \ /`

### Example: basic search

The following example is a basic search request and response.

**Request:**

```http
POST [Organization URI]/api/search/v1.0/query
{  
  "search": "maria",

  "facets": ["@search.entityname,count:100",  
    "account.primarycontactid,count:100",  
    "ownerid,count:100",  
    "modifiedon,values:2019-04-27T00:00:00|2020-03-27T00:00:00|2020-04-20T00:00:00|2020-04-27T00:00:00",
    "createdon,values:2019-04-27T00:00:00|2020-03-27T00:00:00|2020-04-20T00:00:00|2020-04-27T00:00:00"]
}
```

**Response:**

```json
{
    "value": [
        {
            "@search.score": 0.4547767,
            "@search.highlights": {
                "emailaddress1": [
                    "{crmhit}maria{/crmhit}@contoso.com"
                ],
                "firstname": [
                    "{crmhit}Maria{/crmhit}"
                ],
                "fullname": [
                    "{crmhit}Maria{/crmhit} Sullivan"
                ]
            },
            "@search.entityname": "contact",
            "@search.objectid": "aaaaaaaa-0000-1111-2222-bbbbbbbbbbbb",
            "ownerid": "bb2500d1-5e6d-4953-8389-bfedf57e3857",
            "owneridname": "Corey Gray",
            "@search.ownerid.logicalname": "systemuser",
            "@search.objecttypecode": 2,
            "fullname": "Maria Sullivan",
            "entityimage_url": **null**,
            "createdon": "10/9/2020 5:27 PM",
            "modifiedon": "10/9/2020 5:27 PM",
            "emailaddress1": "maria@contoso.com",
            "address1_city": **"Seattle"**,
            "address1_telephone1": **"206-400-0200"**,
            "parentcustomerid": **null**,
            "parentcustomeridname": **null**,
            "telephone1": **"206-400-0300"**
        }
    ],
    "facets": {
        "account.primarycontactid": [],
        "ownerid": [
            {
                "Type": "Value",
                "Value": "31ca7d4b-701c-4ea9-8714-a89a5172106e",
                "OptionalValue": "Corey Gray",
                "Count": 1
            }
        ],
        "@search.entityname": [
            {
                "Type": "Value",
                "Value": "contact",
                "Count": 1
            }
        ],
        "modifiedon": [
            {
                "Type": "Range",
                "To": "4/27/2019 12:00 AM",
                "Count": 0
            },
            {
                "Type": "Range",
                "From": "4/27/2019 12:00 AM",
                "To": "3/27/2020 12:00 AM",
                "Count": 0
            },
            {
                "Type": "Range",
                "From": "3/27/2020 12:00 AM",
                "To": "4/20/2020 12:00 AM",
                "Count": 0
            },
            {
                "Type": "Range",
                "From": "4/20/2020 12:00 AM",
                "To": "4/27/2020 12:00 AM",
                "Count": 0
            },
            {
                "Type": "Range",
                "From": "4/27/2020 12:00 AM",
                "Count": 1
            }
        ],
        "createdon": [
            {
                "Type": "Range",
                "To": "4/27/2019 12:00 AM",
                "Count": 0
            },
            {
                "Type": "Range",
                "From": "4/27/2019 12:00 AM",
                "To": "3/27/2020 12:00 AM",
                "Count": 0
            },
            {
                "Type": "Range",
                "From": "3/27/2020 12:00 AM",
                "To": "4/20/2020 12:00 AM",
                "Count": 0
            },
            {
                "Type": "Range",
                "From": "4/20/2020 12:00 AM",
                "To": "4/27/2020 12:00 AM",
                "Count": 0
            },
            {
                "Type": "Range",
                "From": "4/27/2020 12:00 AM",
                "Count": 1
            }
        ]
    },
    "totalrecordcount": -1
}
```

## Suggestions

Suggestions provide a list of matches to the specified search property value,
based on a table record's primary column. This is different from a regular search
request because a suggestion search only searches through a record's primary column,
while search requests search through all Dataverse search&ndash;enabled table columns.

The following example shows the minimum syntax of a suggestion search HTTP request.

```http
POST [Organization URI]/api/search/v1.0/suggest
{
  "search": "<text-fragment>"
}
```

The search property value provides a text string for the search to match and
has a three-character minimum length.

A successful search response returns an HTTP status of 200 and contains "value",
which is a list consisting of text or a document where the text is the
suggestion with highlights, and the document is a dictionary \<string,object\>
of the suggestion result. By default, five results are returned. Suggestion highlights indicate matches to the search property value and are contained within the `crmhit` tag in the response.

In addition, you can add one or more properties to the body of the request to customize how the
suggestion search is to be done and which results are returned. The supported
properties are indicated in the following section.

### Suggest properties

#### `usefuzzy:true | false` (optional)

Use fuzzy search to aid with misspellings. The default is **false**.

#### `top:[int]` (optional)

Number of suggestions to retrieve. The default is 5.

#### `orderby:[List<string>]` (optional)

A list of comma-separated clauses where each clause consists of an column name followed by `asc` (ascending) or `desc` (descending). This list specifies how to order the results in order of precedence. By default, results are listed in descending order of relevance score (@search.score). For results with identical scores, the ordering will be random.

For a set of results that contain multiple table types, the list of clauses for `orderby` must be globally applicable (for example, modifiedon, createdon, @search.score). Note that specifying the `orderby` property overrides the default. For example, to get results ranked (in order of precedence) by relevance, followed by the most recently modified records listed higher:

`"orderby": ["@search.score desc", "modifiedon desc"]`

If the query request includes a filter for a specific table type, `orderby` can optionally specify table-specific columns.

#### `entities:[list<string>]` (optional)

The default is searching across all Dataverse search&ndash;configured tables.

#### `filter:[string]` (optional)

Filters are applied while searching data and are specified in standard OData
syntax.

**Request:**

```http
POST [Organization URI]/api/search/v1.0/suggest
{  
  "search": "mar",

  "filter": "account:modifiedon ge 2020-04-27T00:00:00,
    activities:regardingobjecttypecode eq 'account', annotation:objecttypecode eq 'account'"
}
```

### Example: suggestion search

The following example shows a basic suggestion search request.

**Request:**

```http
POST [Organization URI]/api/search/v1.0/suggest
{  
  "search": "mar"
}
```

**Response:**

```json
{
    "value": [
        {
            "text": "{crmhit}Mar{/crmhit}ia Sullivan",
            "document": {
                "@search.objectid": "bbbbbbbb-1111-2222-3333-cccccccccccc",
                "@search.entityname": "contact",
                "@search.objecttypecode": 2,
                "fullname": "Maria Sullivan",
                "entityimage_url": **null**,
                "emailaddress1": "maria@contoso.com",
                "address1_city": **null**,
                "address1_telephone1": **null**,
                "parentcustomerid": **null**,
                "parentcustomeridname": **null**,
                "telephone1": **null**
            }
        }
    ]
}
```

## Autocomplete

Provides autocompletion of user input. Autocomplete is based on a table
record's primary column.

The minimum syntax of a Dataverse search HTTP request is as follows.

```http
POST [Organization URI]/api/search/v1.0/autocomplete
{  
  "search": "<text-fragment>"
}
```

A successful search response returns an HTTP status of 200 and consists of
"value", which is a string.

In addition, you can add one or more properties to the request body to customize how the
search is to be done and which results are returned. The supported properties are indicated in the following section.

### Autocomplete properties

#### `usefuzzy: true | false` (optional)

Fuzzy search to aid with misspellings. The default is **false**.

#### `entities: [list<string>]` (optional)

The default scope is searching across all Dataverse search&ndash;configured tables
and columns.

#### `filter: [string]` (optional)

Filters are applied while searching data and are specified in standard OData
syntax.

**Request:**

```http
POST [Organization URI]/api/search/v1.0/autocomplete
{  
  "search": "mar",

  "filter": "account:modifiedon ge 2020-04-27T00:00:00,
    activities:regardingobjecttypecode eq 'account', annotation:objecttypecode eq 'account'"
}
```

### Example: autocomplete search

The following example shows a basic autocomplete request.

**Request:**

```http
POST [Organization URI]/api/search/v1.0/autocomplete
{  
  "search": "mar"
}
```

**Response:**

```json
{
  "value": "{crmhit}maria{/crmhit}"
}
```

### See also

[Search for Dataverse records](overview.md)   
[Dataverse Search query](query.md)   
[Dataverse Search suggest](suggest.md)   
[Dataverse Search autocomplete](autocomplete.md)   
[Dataverse Search statistics and status](statistics-status.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
