---
title: "Relevance search using the Web API (Common Data Service)| Microsoft Docs"
description: "Read about the various ways to find entity data, including search, suggestions, and autocomplete, and even search across entity types using Common Data Service."
ms.custom: ""
ms.date: 10/12/2020
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

# Search entity data using relevance search

Relevance search delivers fast and comprehensive search results across multiple
entities, in a single list, sorted by relevance. Relevance search must be
enabled in your target environment by an administrator prior to using the
feature.

For more information about relevance search including instructions to enable the
feature, see [Using relevance search to search for records](https://docs.microsoft.com/en-us/powerapps/user/relevance-search).

To begin using relevance search, your application simply issues an HTTP POST
request (presently Web API only) to start a relevance search. When searching
data, specify optional query parameters to set criteria for how the environment
data is to be searched.

There are three relevance search methods that can be used in the Power Apps web
application UI:

- Search – Provides a search results page.

- Suggestions – Provides suggestions as the user types into a form field.

- Autocomplete – Provides autocompletion of input as the user types into a
    form field.

The following sections describe how to access the above mentioned search
capabilities from application code.

## Search

The minimum syntax of a relevance search HTTP request is as shown below.

```http
POST [Organization URI]/api/search/v1.0/query
{  
  “search”: “<search term>”
}
```

The search parameter value contains the term to be searched for and has a
100-character limit.

A successful search response returns an HTTP status of 200 and consists of:

- Value: a list of entities. By default, 50 results are returned. This also
    includes search highlights, which indicate matches to the search parameter
    value contained within the `crmhit` tag.

- Totalrecordcount: The total count of results (of type long). A value of -1
    is returned if returntotalrecordcount set to false (default).

- Facets: The facet results.

In addition, you can add one or more query parameters to customize how the
search is to be done and what results are returned. The supported query
parameters are indicated in the next section.

### Query parameters

A list of supported query parameters for relevance search is listed below.

**entities=[list\<string\>] (optional)**

The default entity list searches across all relevance search-configured entities
and fields. The default list is configured by your administrator when relevance
search is enabled.

**facets=[list\<string\>] (optional)**

Facets support the ability to drill into data results after they have been
retrieved.

```http
POST [Organization URI]/api/search/v1.0/query
{  
“search”: ”maria”,

“facets”: ["\@search.entityname,count:100",  
  "account.primarycontactid,count:100",  
  "ownerid,count:100",  
  "modifiedon,values:2019-04-27T00:00:00|2020-03-27T00:00:00\|2020-04-20T00:00:00|2020-04-27T00:00:00",
  "createdon,values:2019-04-27T00:00:00|2020-03-27T00:00:00\|2020-04-20T00:00:00|2020-04-27T00:00:00"]
}
```

**filter=[string] (optional)**

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

**returntotalrecordcount = true \| false (optional)**

Specify **true** to return the total record count; otherwise **false**. The default
is **false**.

**skip=[int] (optional)**

Specifies the number of search results to skip.

**top=[int] (optional)**

Specifies the number of search results to retrieve. The default is 50.

**orderby=[list\<string\>] (optional)**

A list of comma-separated clauses where each clause consists of an attribute
name followed by ‘asc’ (shorthand for ascending) or ‘desc’ (shorthand for
descending). This list specifies how to order the results in order of
precedence.

**searchmode= any \| all (optional)**

Specifies whether any or all the search terms must be matched to count the
document as a match. The default is 'any'.

> [!NOTE]
> The `searchMode` parameter on a query request controls whether a term with the NOT operator is AND'ed or OR'ed with other terms in the query (assuming there is no + or | operator on the other terms).<p/> Using `searchMode=any` increases the recall of queries by including more results, and by default, will be interpreted as "OR NOT". For example, "wifi -luxury" will match documents that either contain the term "wifi" or those that do not contain the term "luxury".<p/>Using `searchMode=all` increases the precision of queries by including fewer results, and by default, will be interpreted as "AND NOT". For example, "wifi -luxury" will match documents that contain the term "wifi" and do not contain the term "luxury".

**searchtype= simple \| full (optional)**

The search type specifies the syntax of a search query. Using 'simple' selects
simple query syntax and 'full' selects Lucene query syntax. The default is
‘simple’.

The simple query syntax supports the following functionality:

| **Functionality** | **Description** |
|---|---|
| Boolean operators | AND operator; denoted by +<br/>OR operator; denoted by \|<br/>NOT operator; denoted by \- |
| Precedence operators | A search term "hotel+(wifi \| luxury)" will search for results containing the term “hotel” and either “wifi” or “luxury” (or both). |
| Wildcards            | Trailing wildcard are supported. For example, "Alp\*" searches for "alpine". |
| Exact matches        | A query enclosed in quotation marks “ “.|

The Lucene query syntax supports the following functionality:

| **Functionality** | **Description** |
|---|---|
| Boolean operators | Provides an expanded set compared to simple query syntax.<br/>AND operator; denoted by AND, &&, +<br/>OR operator; denoted by OR, \|\|<br/>NOT operator; denoted by NOT, !, – |
| Precedence operators              | The same functionality as simple query syntax. |
| Wildcards                         | In addition to a trailing wildcard, also supports a leading wildcard.<br/>Trailing wildcard – alp\*<br/>Leading wildcard - \*ine |
| Fuzzy search                      | Supports queries misspelled by up to 2 characters.<br/>“Uniersty\~” will return “University”<br/>“Blue\~1” will return “glue”, “blues” |
| Term boosting                     | Weighs specific terms in a query differently.<br/>“Rock\^2 electronic” will return results where the matches of “rock” are more important than matches to “electronic”. |
| Proximity search                  | Returns results where terms are within X words of each other - for more contextual results.<br/>For example, “airport hotel”\~5 returns results where “airport” and “hotel” are within 5 words of each other, thus boosting the chances of finding a hotel located close to an airport. |
| Regular expression (regex) search | For example, /\[mh\]otel/ matches “motel” or “hotel”. |

### Example 1

Below is an example of a basic search request and response.

**Request**

```http
POST [Organization URI]/api/search/v1.0/query
{  
“search”: ”maria”,

“facets”: ["\@search.entityname,count:100",  
  "account.primarycontactid,count:100",  
  "ownerid,count:100",  
  "modifiedon,values:2019-04-27T00:00:00\|2020-03-27T00:00:00\|2020-04-20T00:00:00\|2020-04-27T00:00:00",

  "createdon,values:2019-04-27T00:00:00\|2020-03-27T00:00:00\|2020-04-20T00:00:00\|2020-04-27T00:00:00"]
}
```

**Response**

```json
{
    "value": [

        {

            "\@search.score": 0.4547767,

            "\@search.highlights": {

                "emailaddress1": [

                    "{crmhit}maria{/crmhit}\@contoso.com"

                ],

                "firstname": [

                    "{crmhit}Maria{/crmhit}"

                ],

                "fullname": [

                    "{crmhit}Maria{/crmhit} Sullivan"

                ]

            },

            "\@search.entityname": "contact",

            "\@search.objectid": "16ffc791-d06d-4d8c-84ad-89a8978e14f3",

            "key": "5d3d6f6b-a721-4108-ad95-fe25eebbc277contact2",

            "ownerid": "bb2500d1-5e6d-4953-8389-bfedf57e3857",

            "owneridname": "Corey Gray",

            "\@search.ownerid.logicalname": "systemuser",

            "owningbusinessunit": "e854b0d3-3441-418d-854f-b7d11bb17f1b",

            "owningbusinessunitname": "",

            "\@search.owningbusinessunit.logicalname": "businessunit",

            "sharedtoprincipalid": [],

            "\@search.objecttypecode": 2,

            "fullname": "Maria Sullivan",

            "versionnumber": 1622564,

            "statecode\@stringcollection": [

                "Active"

            ],

            "statecode": 0,

            "statuscode\@stringcollection": [

                "Active"

            ],

            "statuscode": 1,

            "entityimage_url": **null**,

            "lastsyncdate": "/Date(1602289865930)/",

            "createdon": "10/9/2020 5:27 PM",

            "modifiedon": "10/9/2020 5:27 PM",

            "documentbody": **null**,

            "body": **null**,

            "filebody": **null**,

            "emailaddress1": "maria\@contoso.com",

            "address1_city": **“Seattle”**,

            "address1_telephone1": **“206-400-0200”**,

            "parentcustomerid": **null**,

            "parentcustomeridname": **null**,

            "telephone1": **“206-400-0300”**

        }

    ],

    "facets": {

        "account.primarycontactid": [],

        "ownerid": [

            {

                "Type": "Value",

                "Value": "31ca7d4b-701c-4ea9-8714-a89a5172106e",

                "OptionalValue": "Corey Gray",

                "Count": 1

            }

        ],

        "\@search.entityname": [

            {

                "Type": "Value",

                "Value": "contact",

                "Count": 1

            }

        ],

        "modifiedon": [

            {

                "Type": "Range",

                "To": "4/27/2019 12:00 AM",

                "Count": 0

            },

            {

                "Type": "Range",

                "From": "4/27/2019 12:00 AM",

                "To": "3/27/2020 12:00 AM",

                "Count": 0

            },

            {

                "Type": "Range",

                "From": "3/27/2020 12:00 AM",

                "To": "4/20/2020 12:00 AM",

                "Count": 0

            },

            {

                "Type": "Range",

                "From": "4/20/2020 12:00 AM",

                "To": "4/27/2020 12:00 AM",

                "Count": 0

            },

            {

                "Type": "Range",

                "From": "4/27/2020 12:00 AM",

                "Count": 1

            }

        ],

        "createdon": [

            {

                "Type": "Range",

                "To": "4/27/2019 12:00 AM",

                "Count": 0

            },

            {

                "Type": "Range",

                "From": "4/27/2019 12:00 AM",

                "To": "3/27/2020 12:00 AM",

                "Count": 0

            },

            {

                "Type": "Range",

                "From": "3/27/2020 12:00 AM",

                "To": "4/20/2020 12:00 AM",

                "Count": 0

            },

            {

                "Type": "Range",

                "From": "4/20/2020 12:00 AM",

                "To": "4/27/2020 12:00 AM",

                "Count": 0

            },

            {

                "Type": "Range",

                "From": "4/27/2020 12:00 AM",

                "Count": 1

            }

        ]

    },

    "totalrecordcount": -1
}
```

## Suggestions

Suggestions provide a list of matches to the specified search parameter value,
based on an entity record’s primary field. This is different from a Search
request because this only searches through an entity record’s primary field,
while Search requests search through all relevance search-enabled entity fields.

The minimum syntax of a suggestion search HTTP request is as shown below.

```http
POST [Organization URI]/api/search/v1.0/suggest
{
“search”: “\<text-fragment\>”
}
```

The search parameter value provides a text string for the search to match and
has a 3-character minimum length.

A successful search response returns an HTTP status of 200 and contains “value”,
which is a list consisting of text or a document where the text is the
suggestion with highlights, and the document is a dictionary \<string,object\>
of the suggestion result. By default, five results are returned.

In addition, you can add one or more query parameters to customize how the
suggestion search is to be done and what results are returned. The supported
query parameters are indicated in the next section.

### Query parameters

**usefuzzy=true \| false (optional)**

Use fuzzy search to aid with misspellings. The default is false.

**top=[int] (optional)**

Number of suggestions to retrieve. The default is 5.

**orderby=[List\<string\>] (optional)**

List of comma-separated clauses where each clause consists of an attribute name
followed by ‘asc’ (ascending) or ‘desc’ (descending). This list specifies how to
order the results, in order of precedence.

**entities=[list\<string\>] (optional)**

Default is searching across all relevance search configured entities.

**filter=[string] (optional)**

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

### Example 2

Below is an example of a basic suggestion search request.

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

                "\@search.objectid": "52a33850-8f0a-eb11-a813-000d3a8ab142",

                "\@search.entityname": "contact",

                "\@search.objecttypecode": 2,

                "fullname": "Maria Sullivan",

                "entityimage_url": **null**,

                "emailaddress1": "maria\@contoso.com",

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

Provides autocompletion of user input. Autocomplete is based on an entity
record’s primary field.

The minimum syntax of a relevance search HTTP request is as shown below.

```http
POST [Organization URI]/api/search/v1.0/autocomplete
{  
“search”: ”\<text-fragment\>”
}
```

A successful search response returns an HTTP status of 200 and consists of
“value”, which is a string.

In addition, you can add one or more query parameters to customize how the
search is to be done and what results are returned. The supported query
parameters are indicated in the next section.

### Query parameters

**usefuzzy=true \| false (optional)**

Fuzzy search to aid with misspellings. The default is false.

**entities=[list\<string\>] (optional)**

The default scope is searching across all relevance search configured entities
and fields.

**filter=[string] (optional)**

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

### Example 3

Below is an example of a basic autocomplete request.

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

### See Also

[Configure Relevance Search to improve search results and performance](https://docs.microsoft.com/en-us/power-platform/admin/configure-relevance-search-organization)
