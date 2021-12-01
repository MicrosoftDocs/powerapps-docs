---
title: "Search across table data using Dataverse search (Microsoft Dataverse)| Microsoft Docs"
description: "Read about the various ways to find table data, including search, suggestions, and autocomplete, and even search across table types using Microsoft Dataverse."
ms.custom: ""
ms.date: 10/13/2020
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: fc3ade34-9c4e-4c33-88a4-aa3842c5eee1
caps.latest.revision: 78
author: "MitiJ"
ms.author: "mijosh"
ms.reviewer: "pehecke"
manager: "mayadumesh"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Search across table data using Dataverse search

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

Dataverse search delivers fast and comprehensive search results across multiple
tables, in a single list, sorted by relevance. Dataverse search must be
enabled in your target environment by an administrator before you can use the
feature. More information: [Using Dataverse search to search for records](../../../user/relevance-search.md)

To begin using Dataverse search, your application simply issues an HTTP POST
request (presently Web API only) to start a Dataverse search. When searching
data, specify optional query parameters to set criteria for how the environment
data is to be searched.

There are three Dataverse search methods that can be used in the Power Apps web
application UI:

- **Search**: Provides a search results page.

- **Suggestions**: Provides suggestions as the user enters text into a form field.

- **Autocomplete**: Provides autocompletion of input as the user enters text into a
    form field.

The following sections describe how to access the above mentioned search
capabilities from application code.

## Search

The minimum syntax of a Dataverse search HTTP request is as shown below.

```http
POST [Organization URI]/api/search/v1.0/query
{  
  “search”: “<search term>”
}
```

The `search` parameter value contains the term to be searched for and has a
100-character limit.

A successful search response returns an HTTP status of 200 and consists of:

- value: a list of tables. By default, 50 results are returned. This also
    includes search highlights, which indicate matches to the search parameter
    value contained within the `crmhit` tag of the response.

- totalrecordcount: The total count of results (of type long). A value of &minus;1
    is returned if `returntotalrecordcount` is set to **false** (default).

- facets: The facet results.

In addition, you can add one or more query parameters to customize how the
search is to be done and which results are returned. The supported query
parameters are indicated in the following section.

### Query parameters

The following query parameters are supported for Dataverse search.

#### `entities=[list<string>] (optional)`

The default table list searches across all Dataverse search&ndash;configured tables
and columns. The default list is configured by your administrator when Dataverse
search is enabled.

#### `facets=[list<string>] (optional)`

Facets support the ability to drill down into data results after they've been
retrieved.

```http
POST [Organization URI]/api/search/v1.0/query
{  
  “search”: ”maria”,

  “facets”: ["@search.entityname,count:100",  
    "account.primarycontactid,count:100",  
    "ownerid,count:100",  
    "modifiedon,values:2019-04-27T00:00:00|2020-03-27T00:00:00|2020-04-20T00:00:00|2020-04-27T00:00:00",
    "createdon,values:2019-04-27T00:00:00|2020-03-27T00:00:00|2020-04-20T00:00:00|2020-04-27T00:00:00"]
}
```

#### `filter=[string] (optional)`

Filters are applied while searching data and are specified in standard OData
syntax.

```http
POST [Organization URI]/api/search/v1.0/query
{  
  “search”: ”maria”,

  “filter”: "account:modifiedon ge 2020-04-27T00:00:00,
    activities: regardingobjecttypecode eq 'account', annotation:objecttypecode eq 'account',
    incident: (prioritycode eq 1 or prioritycode eq 2)"
}
```

#### `returntotalrecordcount = true | false (optional)`

Specify **true** to return the total record count; otherwise **false**. The default
is **false**.

#### `skip=[int] (optional)`

Specifies the number of search results to skip.

#### `top=[int] (optional)`

Specifies the number of search results to retrieve. The default is 50, and the maximum value is 100.

#### `orderby=[list<string>] (optional)`

A list of comma-separated clauses where each clause consists of a column name followed by 'asc' (ascending, which is the default) or 'desc' (descending). This list specifies how to order the results in order of precedence. By default, results are listed in descending order of relevance score (@search.score). For results with identical scores, the ordering will be random.

For a set of results that contain multiple table types, the list of clauses for `orderby` must be globally applicable (for example, modifiedon, createdon, @search.score). Note that specifying the `orderby` parameter overrides the default. For example, to get results ranked (in order of precedence) by relevance, followed by the most recently modified records listed higher:

`“orderby”: [“@search.score desc", "modifiedon desc”]`

If the query request includes a filter for a specific table type, `orderby` can optionally specify table-specific columns.

#### `searchmode= any | all (optional)`

Specifies whether any or all the search terms must be matched to count the
document as a match. The default is 'any'.

> [!NOTE]
> The `searchMode` parameter on a query request controls whether a term with the NOT operator is AND'ed or OR'ed with other terms in the query (assuming there is no + or | operator on the other terms).<p/> Using `searchMode=any` increases the recall of queries by including more results, and by default will be interpreted as "OR NOT". For example, "wifi -luxury" will match documents that either contain the term "wifi" or those that don't contain the term "luxury".<p/>Using `searchMode=all` increases the precision of queries by including fewer results, and by default will be interpreted as "AND NOT". For example, "wifi -luxury" will match documents that contain the term "wifi" and don't contain the term "luxury".

#### `searchtype= simple | full (optional)`

The search type specifies the syntax of a search query. Using 'simple' selects
simple query syntax and 'full' selects Lucene query syntax. The default is
'simple'.

The simple query syntax supports the following functionality:

| **Functionality** | **Description** |
|---|---|
| Boolean operators | AND operator; denoted by +<br/>OR operator; denoted by \|<br/>NOT operator; denoted by \- |
| Precedence operators | A search term "hotel+(wifi \| luxury)" will search for results containing the term "hotel" and either "wifi" or "luxury" (or both). |
| Wildcards            | Trailing wildcard are supported. For example, "Alp\*" searches for "alpine". |
| Exact matches        | A query enclosed in quotation marks " ".|

The Lucene query syntax supports the following functionality:

| **Functionality** | **Description** |
|---|---|
| Boolean operators | Provides an expanded set compared to simple query syntax.<br/>AND operator; denoted by AND, &&, +<br/>OR operator; denoted by OR, \|\|<br/>NOT operator; denoted by NOT, !, – |
| Precedence operators              | The same functionality as simple query syntax. |
| Wildcards                         | In addition to a trailing wildcard, also supports a leading wildcard.<br/>Trailing wildcard – "alp\*"<br/>Leading wildcard - “/.\*pine/” |
| Fuzzy search                      | Supports queries misspelled by up to two characters.<br/>"Uniersty\~" will return "University"<br/>"Blue\~1" will return "glue", "blues" |
| Term boosting                     | Weighs specific terms in a query differently.<br/>"Rock\^2 electronic" will return results where the matches to "rock" are more important than matches to "electronic". |
| Proximity search                  | Returns results where terms are within *x* words of each other, for more contextual results.<br/>For example, "airport hotel"\~5 returns results where "airport" and "hotel" are within five words of each other, thus boosting the chances of finding a hotel located close to an airport. |
| Regular expression (regex) search | For example, /\[mh\]otel/ matches "motel" or "hotel". |

> [!NOTE]
> Wildcards are used only for word completion in Dataverse search. As a rule, querying with a leading wildcard will take significantly longer than not using a wildcard, so we encourage you to explore alternative ways to find what you're looking for and only use leading wildcards sparingly, if at all.

In order to use any of the search operators as part of the search text, escape the character by prefixing it with a single backslash (\\). Special characters that require escaping include the following: + - & | ! ( ) { } [ ] ^ " ~ * ? : \ /

### Example: basic search

Below is an example of a basic search request and response.

**Request**

```http
POST [Organization URI]/api/search/v1.0/query
{  
  “search”: ”maria”,

  “facets”: ["@search.entityname,count:100",  
    "account.primarycontactid,count:100",  
    "ownerid,count:100",  
    "modifiedon,values:2019-04-27T00:00:00|2020-03-27T00:00:00|2020-04-20T00:00:00|2020-04-27T00:00:00",
    "createdon,values:2019-04-27T00:00:00|2020-03-27T00:00:00|2020-04-20T00:00:00|2020-04-27T00:00:00"]
}
```

**Response**

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
            "@search.objectid": "16ffc791-d06d-4d8c-84ad-89a8978e14f3",
            "ownerid": "bb2500d1-5e6d-4953-8389-bfedf57e3857",
            "owneridname": "Corey Gray",
            "@search.ownerid.logicalname": "systemuser",
            "@search.objecttypecode": 2,
            "fullname": "Maria Sullivan",
            "entityimage_url": **null**,
            "createdon": "10/9/2020 5:27 PM",
            "modifiedon": "10/9/2020 5:27 PM",
            "emailaddress1": "maria@contoso.com",
            "address1_city": **“Seattle”**,
            "address1_telephone1": **“206-400-0200”**,
            "parentcustomerid": **null**,
            "parentcustomeridname": **null**,
            "telephone1": **“206-400-0300”**
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

Suggestions provide a list of matches to the specified search parameter value,
based on a table record's primary column. This is different from a regular search
request because a suggestion search only searches through a record's primary column,
while search requests search through all Dataverse search&ndash;enabled table columns.

The minimum syntax of a suggestion search HTTP request is as shown below.

```http
POST [Organization URI]/api/search/v1.0/suggest
{
  “search”: “<text-fragment>”
}
```

The search parameter value provides a text string for the search to match and
has a three-character minimum length.

A successful search response returns an HTTP status of 200 and contains "value",
which is a list consisting of text or a document where the text is the
suggestion with highlights, and the document is a dictionary \<string,object\>
of the suggestion result. By default, five results are returned. Suggestion highlights indicate matches to the search parameter value and are contained within the `crmhit` tag in the response.

In addition, you can add one or more query parameters to customize how the
suggestion search is to be done and which results are returned. The supported
query parameters are indicated in the following section.

### Query parameters

#### `usefuzzy=true | false (optional)`

Use fuzzy search to aid with misspellings. The default is **false**.

#### `top=[int] (optional)`

Number of suggestions to retrieve. The default is 5.

#### `orderby=[List<string>] (optional)`

A list of comma-separated clauses where each clause consists of an column name followed by 'asc' (ascending) or 'desc' (descending). This list specifies how to order the results in order of precedence. By default, results are listed in descending order of relevance score (@search.score). For results with identical scores, the ordering will be random.

For a set of results that contain multiple table types, the list of clauses for `orderby` must be globally applicable (for example, modifiedon, createdon, @search.score). Note that specifying the `orderby` parameter overrides the default. For example, to get results ranked (in order of precedence) by relevance, followed by the most recently modified records listed higher:

`“orderby”: [“@search.score desc", "modifiedon desc”]`

If the query request includes a filter for a specific table type, `orderby` can optionally specify table-specific columns.

#### `entities=[list<string>] (optional)`

The default is searching across all Dataverse search&ndash;configured tables.

#### `filter=[string] (optional)`

Filters are applied while searching data and are specified in standard OData
syntax.

**Request**

```http
POST [Organization URI]/api/search/v1.0/suggest
{  
  “search”: ”mar”,

  “filter”: "account:modifiedon ge 2020-04-27T00:00:00,
    activities:regardingobjecttypecode eq 'account', annotation:objecttypecode eq 'account'"
}
```

### Example: suggestion search

The following is an example of a basic suggestion search request.

**Request**

```http
POST [Organization URI]/api/search/v1.0/suggest
{  
  “search”: ”mar”
}
```

**Response**

```json
{
    "value": [
        {
            "text": "{crmhit}Mar{/crmhit}ia Sullivan",
            "document": {
                "@search.objectid": "52a33850-8f0a-eb11-a813-000d3a8ab142",
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
  “search”: ”<text-fragment>”
}
```

A successful search response returns an HTTP status of 200 and consists of
"value", which is a string.

In addition, you can add one or more query parameters to customize how the
search is to be done and which results are returned. The supported query
parameters are indicated in the following section.

### Query parameters

#### `usefuzzy=true | false (optional)`

Fuzzy search to aid with misspellings. The default is **false**.

#### `entities=[list<string>] (optional)`

The default scope is searching across all Dataverse search&ndash;configured tables
and columns.

#### `filter=[string] (optional)`

Filters are applied while searching data and are specified in standard OData
syntax.

**Request**

```http
POST [Organization URI]/api/search/v1.0/autocomplete
{  
  “search”: ”mar”,

  “filter”: "account:modifiedon ge 2020-04-27T00:00:00,
    activities:regardingobjecttypecode eq 'account', annotation:objecttypecode eq 'account'"
}
```

### Example: autocomplete search

The following is an example of a basic autocomplete request.

**Request**

```http
POST [Organization URI]/api/search/v1.0/autocomplete
{  
  “search”: ”mar”
}
```

**Response**

```json
{
  "value": "{crmhit}maria{/crmhit}"
}
```

### See also

[Configure Dataverse search to improve search results and performance](/power-platform/admin/configure-relevance-search-organization)  
[Compare search options in Microsoft Dataverse](../../../user/search.md)  
[Retrieve related table records with a query](retrieve-related-entities-query.md)  
[Query Data using the Web API](query-data-web-api.md)  
[Connect with your Dataverse environment](setup-postman-environment.md#connect-with-your-dataverse-environment)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
