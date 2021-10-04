---
title: "Query data using the Web API (Microsoft Dataverse)| Microsoft Docs"
description: "Read about the various ways to query Microsoft Dataverse table data using the Web API and the various system query options that can be applied in these queries."
ms.custom: ""
ms.date: 04/29/2021
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: fc3ade34-9c4e-4c33-88a4-aa3842c5eee1
caps.latest.revision: 78
author: "JimDaly"
ms.author: "jdaly"
ms.reviewer: "pehecke"
manager: "annbe"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Query data using the Web API

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

If you want to retrieve data for an entity set, use a `GET` request. When retrieving data, you can apply query options to set criteria for the entity (table) data you want and the entity properties (columns) that should be returned.  
    
<a name="bkmk_basicQuery"></a>

## Basic query example

 This example queries the accounts entity set and uses the `$select` and `$top` system query options to return the name property for the first three accounts:  
  
 **Request**

```http 
GET [Organization URI]/api/data/v9.1/accounts?$select=name
&$top=3 HTTP/1.1  
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
  
```  
  
**Response**

```http 
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  
  
{  
   "@odata.context":"[Organization URI]/api/data/v9.1/$metadata#accounts(name)",
   "value":[  
      {  
         "@odata.etag":"W/\"501097\"",
         "name":"Fourth Coffee (sample)",
         "accountid":"89390c24-9c72-e511-80d4-00155d2a68d1"
      },
      {  
         "@odata.etag":"W/\"501098\"",
         "name":"Litware, Inc. (sample)",
         "accountid":"8b390c24-9c72-e511-80d4-00155d2a68d1"
      },
      {  
         "@odata.etag":"W/\"501099\"",
         "name":"Adventure Works (sample)",
         "accountid":"8d390c24-9c72-e511-80d4-00155d2a68d1"
      }
   ]
}
 
```  
  
<a name="bkmk_limits"></a>

## Limits on number of table rows (entities) returned

 Unless you specify a smaller page size, a maximum of 5000 rows will be returned for each request. If there are more rows that match the query filter criteria, a `@odata.nextLink` property will be returned with the results. Use the value of the `@odata.nextLink` property with a new `GET` request to return the next page of rows.  
  
> [!NOTE]
>  Queries on entity (table) definitions aren’t limited or paged. More information:[Query table definitions using the Web API](query-metadata-web-api.md)  

<a name="bkmk_limitResults"></a>

### Use `$top` query option

You can limit the number of results returned by using the `$top` system query option. The following example will return just the first three account rows.  
  
```http 
GET [Organization URI]/api/data/v9.1/accounts?$select=name,revenue&$top=3  
```  
  
> [!NOTE]
>  Limiting results using `$top` will prevent `odata.maxpagesize` preference from being applied. You can use `odata.maxpagesize` preference or `$top`, but not both at the same time. For more information about `odata.maxpagesize`, see [Specify the number of rows to return in a page](query-data-web-api.md#bkmk_specifyNumber).  
>   
>  You should also not use `$top` with `$count`.  

<a name="bkmk_specifyNumber"></a>

### Specify the number of rows to return in a page

Use the `odata.maxpagesize` preference value to request the number of rows returned in the response.  
  
> [!NOTE]
>  You can’t use an `odata.maxpagesize` preference value greater than 5000.  
  
 The following example queries the accounts entity set and returns the `name` property for the first three accounts.  
  
 **Request**

```http 
GET [Organization URI]/api/data/v9.1/accounts?$select=name HTTP/1.1  
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
Prefer: odata.maxpagesize=3  
```  
  
 **Response**  

```http 
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  
Content-Length: 402  
Preference-Applied: odata.maxpagesize=3  
  
{  
   "@odata.context":"[Organization URI]/api/data/v9.1/$metadata#accounts(name)",
   "value":[  
      {  
         "@odata.etag":"W/\"437194\"",
         "name":"Fourth Coffee (sample)",
         "accountid":"7d51925c-cde2-e411-80db-00155d2a68cb"
      },
      {  
         "@odata.etag":"W/\"437195\"",
         "name":"Litware, Inc. (sample)",
         "accountid":"7f51925c-cde2-e411-80db-00155d2a68cb"
      },
      {  
         "@odata.etag":"W/\"468026\"",
         "name":"Adventure Works (sample)",
         "accountid":"8151925c-cde2-e411-80db-00155d2a68cb"
      }
   ],
   "@odata.nextLink":"[Organization URI]/api/data/v9.1/accounts?$select=name&$skiptoken=%3Ccookie%20pagenumber=%222%22%20pagingcookie=%22%253ccookie%2520page%253d%25221%2522%253e%253caccountid%2520last%253d%2522%257b8151925C-CDE2-E411-80DB-00155D2A68CB%257d%2522%2520first%253d%2522%257b7D51925C-CDE2-E411-80DB-00155D2A68CB%257d%2522%2520%252f%253e%253c%252fcookie%253e%22%20/%3E"
}
  
```  
  
 Use the value of the `@odata.nextLink` property to request the next set of records. Don’t change or append any additional system query options to the value. For every subsequent request for additional pages, you should use the same odata.maxpagesize preference value used in the original request. Also, cache the results returned or the value of the `@odata.nextLink` property so that previously retrieved pages can be returned to.  
  
> [!NOTE]
>  The value of the `@odata.nextLink` property is URI encoded. If you URI encode the value before you send it, the XML cookie information in the URL will cause an error.  
  
<a name="bkmk_applyqueryOptions"></a>

## Apply system query options

 Each of the system query options you append to the URL for the entity set is added using the syntax for query strings. The first is appended after [?] and subsequent query options are separated using [&]. All query options are case-sensitive as shown in the following example.  
  
```http 
GET [Organization URI]/api/data/v9.1/accounts?$select=name,revenue
&$top=3
&$filter=revenue gt 100000  
```  
  
<a name="bkmk_requestProperties"></a>
 
## Request specific properties

 Use the `$select` system query option to limit the properties returned as shown in the following example.  
  
```http 
GET [Organization URI]/api/data/v9.1/accounts?$select=name,revenue  
```  
  
> [!IMPORTANT]
>  This is a performance best practice. If properties aren’t specified using `$select`, all properties will be returned.  
  
 When you request certain types of properties you can expect additional read-only properties to be returned automatically.  
  
 If you request a money value, the `_transactioncurrencyid_value` lookup property will be returned. This property contains only the GUID value of the transaction currency so you could use this value to retrieve information about the currency using the <xref:Microsoft.Dynamics.CRM.transactioncurrency?text=transactioncurrency EntityType />. Alternatively, by requesting annotations you can also get additional data in the same request. More information: [Retrieve data about lookup properties](#bkmk_lookupProperty)  
  
 If you request a property that is part of a composite attribute for an address, you will get the composite property as well. For example, if your query requests the `address1_line1` property for a contact, the `address1_composite` property will be returned as well. 
  
<a name="bkmk_filter"></a>

## Filter results

 Use the `$filter` system query option to set criteria for which rows will be returned.  
  
<a name="bkmk_buildInFilterOperators"></a>

### Standard filter operators

 The Web API supports the standard OData filter operators listed in the following table.  
  
|Operator|Description|Example|  
|--------------|-----------------|-------------|  
|**Comparison Operators**|||  
|`eq`|Equal|`$filter=revenue eq 100000`|  
|`ne`|Not Equal|`$filter=revenue ne 100000`|  
|`gt`|Greater than|`$filter=revenue gt 100000`|  
|`ge`|Greater than or equal|`$filter=revenue ge 100000`|  
|`lt`|Less than|`$filter=revenue lt 100000`|  
|`le`|Less than or equal|`$filter=revenue le 100000`|  
|**Logical Operators**|||  
|`and`|Logical and|`$filter=revenue lt 100000 and revenue gt 2000`|  
|`or`|Logical or|`$filter=contains(name,'(sample)') or contains(name,'test')`|  
|`not`|Logical negation|`$filter=not contains(name,'sample')`|  
|**Grouping Operators**|||  
|`( )`|Precedence grouping|`(contains(name,'sample') or contains(name,'test')) and revenue gt 5000`|  
  
> [!NOTE]
>  This is a sub-set of the [11.2.5.1.1 Built-in Filter Operations](https://docs.oasis-open.org/odata/odata/v4.0/errata02/os/complete/part1-protocol/odata-v4.0-errata02-os-part1-protocol-complete.html). Arithmetic operators and the comparison has operator are not supported in the Web API.
>
> All filter conditions for string values are case insensitive.  
  
<a name="bkmk_buildInQueryFunctions"></a>

### Standard query functions  
 
The Web API supports these standard OData string query functions:
 
|Function|Example|  
|--------------|-------------|  
|`contains`|`$filter=contains(name,'(sample)')`|  
|`endswith`|`$filter=endswith(name,'Inc.')`|  
|`startswith`|`$filter=startswith(name,'a')`|  
  
> [!NOTE]
>  This is a sub-set of the [11.2.5.1.2 Built-in Query Functions](https://docs.oasis-open.org/odata/odata/v4.0/errata02/os/complete/part1-protocol/odata-v4.0-errata02-os-part1-protocol-complete.html). `Date`, `Math`, `Type`, `Geo` and other string functions aren’t supported in the web API.  
  
### Microsoft Dataverse Web API query functions

Dataverse provides a number of special functions that accept parameters, return Boolean values, and can be used as filter criteria in a query. See <xref:Microsoft.Dynamics.CRM.QueryFunctionIndex?displayProperty=nameWithType> for a list of these functions. The following is an example of the <xref:Microsoft.Dynamics.CRM.Between?text=Between Function /> searching for accounts with a number of employees between 5 and 2000.  
  
```http 
GET [Organization URI]/api/data/v9.1/accounts?$select=name,numberofemployees
&$filter=Microsoft.Dynamics.CRM.Between(PropertyName='numberofemployees',PropertyValues=["5","2000"])  
```  
  
More information: [Compose a query with functions](use-web-api-functions.md#bkmk_composeQueryWithFunctions). 

<a name="bkmk_LambdaOperators"></a>

### Use Lambda operators

The Web API allows you to use two lambda operators, which are `any` and `all` to evaluate a Boolean expression on a collection.

<a name ="bkmk_anyoperator"></a>

### `any` operator

The `any` operator returns `true` if the Boolean expression applied is `true` for any member of the collection, otherwise it returns `false`. The `any` operator without an argument returns `true` if the collection is not empty.

**Example**

The example given below shows how you can retrieve all account entity records that have at least one email with "sometext" in the subject.

```http
GET [Organization URI]/api/data/v9.1/accounts?$select=name
&$filter=Account_Emails/any(o:contains(o/subject,'sometext')) HTTP/1.1
Prefer: odata.include-annotations="*"
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0 
```

<a name ="bkmk_alloperator"></a>

### `all` operator

The `all` operator returns `true` if the Boolean expression applied is `true` for all members of the collection, otherwise it returns `false`.

**Example**

The example given below shows how you can retrieve all account entity records that have all associated tasks closed.

```http
GET [Organization URI]/api/data/v9.1/accounts?$select=name
&$filter=Account_Tasks/all(o:o/statecode eq 1) HTTP/1.1
Prefer: odata.include-annotations="*"
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0 
```

The example given below shows how you can retrieve all account entity records that have at least one email with "sometext" in the subject and whose statecode is active.

```http
GET [Organization URI]/api/data/v9.1/accounts?$select=name
&$filter=Account_Emails/any(o:contains(o/subject,'sometext') and 
o/statecode eq 0) HTTP/1.1
Prefer: odata.include-annotations="*"
Accept: application/json
OData-MaxVersion: 4.0
OData-Version: 4.0
```

The example given below shows how you can also create a nested query using `any` and `all` operators.

```http
GET [Organization URI]/api/data/v9.1/accounts?$select=name
&$filter=(contact_customer_accounts/any(c:c/jobtitle eq 'jobtitle' and 
c/opportunity_customer_contacts/any(o:o/description ne 'N/A'))) and 
endswith(name,'{0}') HTTP/1.1
Prefer: odata.include-annotations="*"
Accept: application/json
OData-MaxVersion: 4.0
OData-Version: 4.0
```

### Filter parent rows (records) based on values of child records

The example given below shows how you can use the [/any operator](#bkmk_anyoperator) to retrieve all the account records that have:

- any of their linked opportunity records' budget greater than or equal to 300, and
- the opportunity records' have no description, or
- the opportunity records' description contains the term "*bad*".

**Request**

```http
GET [Organization URI]/api/data/v9.1/accounts?$select=name
&$filter=not opportunity_customer_accounts/any(o:o/description eq null and 
o/budgetamount le 300 or 
contains(o/description, 'bad')) and 
opportunity_customer_accounts/any() and 
endswith(name,'{0}') HTTP/1.1
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0 
```

<a name="BKMK_FilterNavProperties"></a>

### Filter rows (records) based on single-valued navigation property

Navigation properties let you access data related to the current entity. *Single-valued* navigation properties correspond to Lookup attributes that support many-to-one relationships and allow setting a reference to another entity. More information: [Navigation properties](web-api-types-operations.md#bkmk_navprops).  
  
You can filter your entity set records based on single-valued navigation property values. For example, you can retrieve child accounts for the specified account.  
  
For example:  
  
-   **Retrieve all the matching accounts for a specified Contact ID**  
  
**Request** 
 
```http 
GET [Organization URI]/api/data/v9.1/accounts?$select=name
&$filter=primarycontactid/contactid eq a0dbf27c-8efb-e511-80d2-00155db07c77 HTTP/1.1  
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
```  
  
**Response**  

```http 
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  
  
{  
"@odata.context":"[Organization URI]/api/data/v9.1/$metadata#accounts(name)",
"value":[  
        {  
            "@odata.etag":"W/\"513479\"",
            "name":"Adventure Works (sample)",
            "accountid":"3adbf27c-8efb-e511-80d2-00155db07c77"
        },
        {  
            "@odata.etag":"W/\"514057\"",
            "name":"Blue Yonder Airlines (sample)",
            "accountid":"3edbf27c-8efb-e511-80d2-00155db07c77"
        }
    ]
}  
```  

-   **Retrieve child accounts for the specified Account ID**  
  
**Request**  

```http 
GET [Organization URI]/api/data/v9.1/accounts?$select=name
&$filter=parentaccountid/accountid eq 3adbf27c-8efb-e511-80d2-00155db07c77  
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
```  
  
**Response**  

```http 
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  
  
{  
"@odata.context":"[Organization URI]/api/data/v9.1/$metadata#accounts(name)",
"value":[  
        {  
            "@odata.etag":"W/\"514058\"",
            "name":"Sample Child Account 1",
            "accountid":"915e89f5-29fc-e511-80d2-00155db07c77"
        },
        {  
            "@odata.etag":"W/\"514061\"",
            "name":"Sample Child Account 2",
            "accountid":"03312500-2afc-e511-80d2-00155db07c77"
        }
    ]
}   
```

### Filter results based on values of collection-valued navigation properties

> [!NOTE]
> It is possible to use `$filter` within `$expand` to filter results for related records in a Retrieve operation. You can use a semi-colon separated list of system query options enclosed in parentheses after the name of the collection-valued navigation property. The query options that are supported within `$expand` are `$select`, `$filter`, `$top` and `$orderby`. More information: [Options to apply to expanded tables](retrieve-entity-using-web-api.md#options-to-apply-to-expanded-tables).

The two options for filtering results based on values of collection-valued navigation properties are:

1. **Construct a query using Lambda operators**

Lambda operators allow you to apply filter on values of collection properties for a link-entity. The below example retrieves the records of `systemuser` entity type that are linked with `team` and `teammembership` entity types, that means it retrieves `systemuser` records who are also administrators of a team whose name is "CITTEST".

```http
GET [Organization URI]/api/data/v9.1/systemusers?$filter=(teammembership_association/any(t:t/name eq 'CITTEST'))
&$select=fullname,businessunitid,title,address1_telephone1,systemuserid
&$orderby=fullname
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
```
More information: [Use Lambda operators](#bkmk_LambdaOperators).

2. **Iterate over results filtering individual entities based on values in the collection using multiple operations**

To get the same results as the example above, you can retrieve records of two entity types and then iteratively match the values in the collection of one entity to the value in the other entity, thereby filtering entities based on the values in the collection.

Follow the steps in the below example to understand how we can filter results using the iteration method:

1. Get a distinct list of <xref:Microsoft.Dynamics.CRM.team?displayProperty=nameWithType>._administratorid_value values.
      - `GET [OrganizationURI]/api/data/v9.1/teams?$select=_administratorid_value&$filter=_administrator_value ne null`
      - Then loop through the returned values to remove duplicates and get a distinct list. i.e. Create a new array, loop through the query results, for each check to see if they are already in the new array, if not, add them. This should give you a list of distinct `systemuserid` values
      - The way you would do this in JavaScript vs C# would be different, but essentially you should be able to get the same results.
2. Query <xref:Microsoft.Dynamics.CRM.systemuser?displayProperty=nameWithType> using <xref:Microsoft.Dynamics.CRM.ContainValues?text=ContainValues Query Function /> to compare the `systemuserid` values with the list collected in Step 1.

<a name="bkmk_order"></a>

## Order results

 Specify the order in which items are returned using the `$orderby` system query option. Use the `asc` or `desc` suffix to specify ascending or descending order respectively. The default is ascending if the suffix isn’t applied. The following example shows retrieving the name and revenue properties of accounts ordered by ascending revenue and by descending name.  
  
```http 
GET [Organization URI]/api/data/v9.1/accounts?$select=name,revenue
&$orderby=revenue asc,name desc
&$filter=revenue ne null  
```  
<a name="bkmk_AggregateGroup"></a>

## Aggregate and grouping results

By using `$apply` you can aggregate and group your data dynamically.  Possible use cases with `$apply`:

|Use Case|Example|
|--------------|-------------| 
|List of unique statuses in the query|`accounts?$apply=groupby((statuscode))`|
|Aggregate sum of the estimated value|`opportunities?$apply=aggregate(estimatedvalue with sum as total)`|
|Average size of the deal based on estimated value and status|`opportunities?$apply=groupby((statuscode),aggregate(estimatedvalue with average as averagevalue)`|
|Sum of estimated value based on status|`opportunities?$apply=groupby((statuscode),aggregate(estimatedvalue with sum as total))`|
|Total opportunity revenue by account name|`opportunities?$apply=groupby((parentaccountid/name),aggregate(estimatedvalue with sum as total))`|
|Primary contact names for accounts in 'WA'|`accounts?$apply=filter(address1_stateorprovince eq 'WA')/groupby((primarycontactid/fullname))`|
|Last created record date and time|`accounts?$apply=aggregate(createdon with max as lastCreate)`|
|First created record date and time|`accounts?$apply=aggregate(createdon with min as firstCreate)`|

The aggregate functions are limited to a collection of 50,000 records.  Further information around using aggregate functionality with Dataverse can be found here: [Use FetchXML to construct a query](../use-fetchxml-construct-query.md).

Additional details on OData data aggregation can be found here: [OData extension for data aggregation version 4.0](https://docs.oasis-open.org/odata/odata-data-aggregation-ext/v4.0/cs01/odata-data-aggregation-ext-v4.0-cs01.html).  Note that Dataverse supports only a sub-set of these aggregate methods.


<a name="bkmk_useParameterAliases"></a>
  
## Use parameter aliases with system query options

 You can use parameter aliases for `$filter` and `$orderby` system query options. Parameter aliases allow for the same value to be used multiple times in a request. If the alias isn’t assigned a value it is assumed to be null.  
  
 Without parameter aliases:

```http  
GET [Organization URI]/api/data/v9.1/accounts?$select=name,revenue
&$orderby=revenue asc,name desc
&$filter=revenue ne null  
```  
  
 With parameter aliases:

```http  
GET [Organization URI]/api/data/v9.1/accounts?$select=name,revenue
&$orderby=@p1 asc,@p2 desc
&$filter=@p1 ne @p3&@p1=revenue&@p2=name  
```  
  
 You can also use parameter aliases when using functions. More information: [Use Web API functions](use-web-api-functions.md)  
    
<a name="bkmk_retrieveCount"></a>
 
## Retrieve a count of rows

 Use the `$count` system query option with a value of `true` to include a count of entities that match the filter criteria up to 5000.  
  
> [!NOTE]
> The count value does not represent the total number of rows in the system. It is limited by the maximum number of rows that can be returned. More information: [Limits on number of rows returned](#bkmk_limits)
>
> If you want to retrieve the total number of rows for a table beyond 5000, use the <xref:Microsoft.Dynamics.CRM.RetrieveTotalRecordCount?text=RetrieveTotalRecordCount  Function />.
  
 The response `@odata.count` property will contain the number of rows that match the filter criteria irrespective of an `odata.maxpagesize` preference limitation.  
  
> [!NOTE]
>  You should not use `$top` with `$count`.  
  
 The following example shows that there are ten accounts that match the criteria where the name contains “sample”, but only the first three accounts are returned.  
  
 **Request**

```http 
GET [Organization URI]/api/data/v9.1/accounts?$select=name
&$filter=contains(name,'sample')
&$count=true HTTP/1.1  
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
Prefer: odata.maxpagesize=3  
```  
  
 **Response** 
 
```http 
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  
Preference-Applied: odata.maxpagesize=3  
  
{  
   "@odata.context":"[Organization URI]/api/data/v9.1/$metadata#accounts(name)",
   "@odata.count":10,
   "value":[  
      {  
         "@odata.etag":"W/\"502482\"",
         "name":"Fourth Coffee (sample)",
         "accountid":"655eaf89-f083-e511-80d3-00155d2a68d3"
      },
      {  
         "@odata.etag":"W/\"502483\"",
         "name":"Litware, Inc. (sample)",
         "accountid":"675eaf89-f083-e511-80d3-00155d2a68d3"
      },
      {  
         "@odata.etag":"W/\"502484\"",
         "name":"Adventure Works (sample)",
         "accountid":"695eaf89-f083-e511-80d3-00155d2a68d3"
      }
   ],
   "@odata.nextLink":"[Organization URI]/api/data/v9.1/accounts?$select=name&$filter=contains(name,'sample')&$skiptoken=%3Ccookie%20pagenumber=%222%22%20pagingcookie=%22%253ccookie%2520page%253d%25221%2522%253e%253caccountid%2520last%253d%2522%257b695EAF89-F083-E511-80D3-00155D2A68D3%257d%2522%2520first%253d%2522%257b655EAF89-F083-E511-80D3-00155D2A68D3%257d%2522%2520%252f%253e%253c%252fcookie%253e%22%20istracking=%22False%22%20/%3E"
}

  
```  
  
 If you don’t want to return any data except for the count, you can apply `$count` to any collection to get just the value.  
  
 **Request**  

```http 
GET [Organization URI]/api/data/v9.1/accounts/$count HTTP/1.1  
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
```  
  
 **Response**  
```http 
HTTP/1.1 200 OK  
Content-Type: text/plain  
OData-Version: 4.0  
  
10  
```  
  
<a name="bkmk_includeFormattedValues"></a>

## Include formatted values

 When you want to receive formatted values for properties with the results, use the `odata.include-annotations` preference with the value of `OData.Community.Display.V1.FormattedValue`. The response will include these values with properties that match the following naming convention:  
  
```  
<propertyname>@OData.Community.Display.V1.FormattedValue  
```  
 The following example queries the accounts entity set and returns the first record, including properties that support formatted values.  
  
 **Request**

```http 
GET [Organization URI]/api/data/v9.1/accounts?$select=name,donotpostalmail,accountratingcode,numberofemployees,revenue
&$top=1 HTTP/1.1  
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
Prefer: odata.include-annotations="OData.Community.Display.V1.FormattedValue"  
```  
  
 **Response**  
```http 
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  
Preference-Applied: odata.include-annotations="OData.Community.Display.V1.FormattedValue"  
  
{  
   "@odata.context":"[Organization URI]/api/data/v9.1/$metadata#accounts(name,donotpostalmail,accountratingcode,numberofemployees,revenue)",
   "value":[  
      {  
         "@odata.etag":"W/\"502170\"",
         "name":"Fourth Coffee (sample)",
         "donotpostalmail@OData.Community.Display.V1.FormattedValue":"Allow",
         "donotpostalmail":false,
         "accountratingcode@OData.Community.Display.V1.FormattedValue":"Default Value",
         "accountratingcode":1,
         "numberofemployees@OData.Community.Display.V1.FormattedValue":"9,500",
         "numberofemployees":9500,
         "revenue@OData.Community.Display.V1.FormattedValue":"$100,000.00",
         "revenue":100000,
         "accountid":"89390c24-9c72-e511-80d4-00155d2a68d1",
         "transactioncurrencyid_value":"50b6dd7b-f16d-e511-80d0-00155db07cb1"
      }
   ]
}
```  

<a name="bkmk_retrieverelatedentities"></a>

## Retrieve related tables with query

Use the `$expand` system query option in the navigation properties to control what data from related entities is returned. More information: [Retrieve related tables with query](retrieve-related-entities-query.md).

<a name="bkmk_lookupProperty"></a>

## Retrieve data about lookup properties

 If your query includes lookup properties you can request annotations that will provide additional information about the data in these properties. Most of the time, the same data is can be derived with knowledge of the single-valued navigation properties and the data included in the related entities. However, in cases where the property represents a lookup attribute that can refer to more than one type of entity, this information can tell you what type of entity is referenced by the lookup property. More information: [Lookup properties](web-api-types-operations.md#bkmk_lookupProperties)  
  
 There are two additional types of annotations available for these properties,  
  
|Annotation|Description|  
|----------------|-----------------|  
|Microsoft.Dynamics.CRM.associatednavigationproperty|The name of the single-valued navigation property that includes the reference to the entity.|  
|Microsoft.Dynamics.CRM.lookuplogicalname|The logical name of the entity referenced by the lookup.|  
  
 These properties also can include formatted values as described in [Include formatted values](query-data-web-api.md#bkmk_includeFormattedValues). Just like formatted values, you can return the other annotations using the `odata.include-annotations` preference set to the specific type of annotation you want, or you can set the value to `"*"` and return all three. The following sample shows the request and response to retrieve information about the incident entity `_customerid_value` lookup property with annotations included.  
  
 **Request**  

```http 
GET [Organization URI]/api/data/v9.1/incidents(39dd0b31-ed8b-e511-80d2-00155d2a68d4)?$select=title,_customerid_value
&$expand=customerid_contact($select=fullname) HTTP/1.1  
Accept: application/json  
Content-Type: application/json; charset=utf-8  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
Prefer: odata.include-annotations="*"  
```  
  
 **Response**  

```http 
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  
Preference-Applied: odata.include-annotations="*"  
  
{  
    "@odata.context":"[Organization URI]/api/data/v9.1/$metadata#incidents(title,_customerid_value,customerid_contact(fullname))/$entity",
    "@odata.etag":"W/\"504696\"",
    "_customerid_value@Microsoft.Dynamics.CRM.associatednavigationproperty":"customerid_contact",
    "_customerid_value@Microsoft.Dynamics.CRM.lookuplogicalname":"contact",
    "_customerid_value@OData.Community.Display.V1.FormattedValue":"Susanna Stubberod (sample)",
    "_customerid_value":"7ddd0b31-ed8b-e511-80d2-00155d2a68d4",
    "incidentid":"39dd0b31-ed8b-e511-80d2-00155d2a68d4",
    "customerid_contact":{  
        "@odata.etag":"W/\"503587\"",
        "fullname":"Susanna Stubberod (sample)",
        "contactid":"7ddd0b31-ed8b-e511-80d2-00155d2a68d4"
    }
} 
```  
  
<a name="bkmk_expandRelated"></a>

## Retrieve related tables by expanding navigation properties
 
<a bkmk="bkmk_retrieverelatedentityexpandcollectionnavprop"></a>

### Retrieve related tables by expanding collection-valued navigation properties

If you expand on collection-valued navigation parameters to retrieve related entities for entity sets, an `@odata.nextLink` property will be returned for the related entities. You should use the value of the `@odata.nextLink` property with a new `GET` request to return the required data.  

The following example retrieves the tasks assigned to the top 5 account records.  
  
**Request**

```http 
GET [Organization URI]/api/data/v9.1/accounts?$top=5
&$select=name
&$expand=Account_Tasks($select=subject,scheduledstart) HTTP/1.1  
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
```  
  
**Response** 
 
```http 
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  
  
{  
   "@odata.context":"[Organization URI]/api/data/v9.1/$metadata#accounts(name,Account_Tasks,Account_Tasks(subject,scheduledstart))",
   "value":[  
      {  
         "@odata.etag":"W/\"513475\"",
         "name":"Fourth Coffee (sample)",
         "accountid":"36dbf27c-8efb-e511-80d2-00155db07c77",
         "Account_Tasks":[  

         ],
         "Account_Tasks@odata.nextLink":"[Organization URI]/api/data/v9.1/accounts(36dbf27c-8efb-e511-80d2-00155db07c77)/Account_Tasks?$select=subject,scheduledstart"
      },
      {  
         "@odata.etag":"W/\"513477\"",
         "name":"Litware, Inc. (sample)",
         "accountid":"38dbf27c-8efb-e511-80d2-00155db07c77",
         "Account_Tasks":[  

         ],
         "Account_Tasks@odata.nextLink":"[Organization URI]/api/data/v9.1/accounts(38dbf27c-8efb-e511-80d2-00155db07c77)/Account_Tasks?$select=subject,scheduledstart"
      },
      {  
         "@odata.etag":"W/\"514074\"",
         "name":"Adventure Works (sample)",
         "accountid":"3adbf27c-8efb-e511-80d2-00155db07c77",
         "Account_Tasks":[  

         ],
         "Account_Tasks@odata.nextLink":"[Organization URI]/api/data/v9.1/accounts(3adbf27c-8efb-e511-80d2-00155db07c77)/Account_Tasks?$select=subject,scheduledstart"
      },
      {  
         "@odata.etag":"W/\"513481\"",
         "name":"Fabrikam, Inc. (sample)",
         "accountid":"3cdbf27c-8efb-e511-80d2-00155db07c77",
         "Account_Tasks":[  

         ],
         "Account_Tasks@odata.nextLink":"[Organization URI]/api/data/v9.1/accounts(3cdbf27c-8efb-e511-80d2-00155db07c77)/Account_Tasks?$select=subject,scheduledstart"
      },
      {  
         "@odata.etag":"W/\"514057\"",
         "name":"Blue Yonder Airlines (sample)",
         "accountid":"3edbf27c-8efb-e511-80d2-00155db07c77",
         "Account_Tasks":[  

         ],
         "Account_Tasks@odata.nextLink":"[Organization URI]/api/data/v9.1/accounts(3edbf27c-8efb-e511-80d2-00155db07c77)/Account_Tasks?$select=subject,scheduledstart"
          }
       ]
    }
 
```  

<a bkmk="bkmk_retrieverelatedentitysingleandcollectionnavprop"></a>
  
### Retrieve related rows (records) by expanding both single-valued and collection-valued navigation properties

The following example demonstrates how you can expand related rows (records) for entity sets using both single and collection-valued navigation properties. As explained earlier, expanding on collection-valued navigation properties to retrieve related entities for entity sets returns an `@odata.nextLink` property for the related entities. You should use the value of the `@odata.nextLink` property with a new `GET` request to return the required data.  
  
In this example, we are retrieving the contact and tasks assigned to the top 3 accounts.  
  
**Request**

```http 
GET [Organization URI]/api/data/v9.1/accounts?$top=3
&$select=name
&$expand=primarycontactid($select=contactid,fullname),Account_Tasks($select=subject,scheduledstart)  HTTP/1.1  
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
```  
  
**Response**  

```http 
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  
  
{  
   "@odata.context":"[Organization URI]/api/data/v9.1/$metadata#accounts(name,primarycontactid,Account_Tasks,primarycontactid(contactid,fullname),Account_Tasks(subject,scheduledstart))",
   "value":[  
      {  
         "@odata.etag":"W/\"550614\"",
         "name":"Fourth Coffee (sample)",
         "accountid":"5b9648c3-68f7-e511-80d3-00155db53318",
         "primarycontactid":{  
            "contactid":"c19648c3-68f7-e511-80d3-00155db53318",
            "fullname":"Yvonne McKay (sample)"
         },
         "Account_Tasks":[  

         ],
         "Account_Tasks@odata.nextLink":"[Organization URI]/api/data/v9.1/accounts(5b9648c3-68f7-e511-80d3-00155db53318)/Account_Tasks?$select=subject,scheduledstart"
      },
      {  
         "@odata.etag":"W/\"550615\"",
         "name":"Litware, Inc. (sample)",
         "accountid":"5d9648c3-68f7-e511-80d3-00155db53318",
         "primarycontactid":{  
            "contactid":"c39648c3-68f7-e511-80d3-00155db53318",
            "fullname":"Susanna Stubberod (sample)"
         },
         "Account_Tasks":[  

         ],
         "Account_Tasks@odata.nextLink":"[Organization URI]/api/data/v9.1/accounts(5d9648c3-68f7-e511-80d3-00155db53318)/Account_Tasks?$select=subject,scheduledstart"
      },
      {  
         "@odata.etag":"W/\"550616\"",
         "name":"Adventure Works (sample)",
         "accountid":"5f9648c3-68f7-e511-80d3-00155db53318",
         "primarycontactid":{  
            "contactid":"c59648c3-68f7-e511-80d3-00155db53318",
            "fullname":"Nancy Anderson (sample)"
         },
         "Account_Tasks":[  

         ],
         "Account_Tasks@odata.nextLink":"[Organization URI]/api/data/v9.1/accounts(5f9648c3-68f7-e511-80d3-00155db53318)/Account_Tasks?$select=subject,scheduledstart"
      }
   ]
}
  
```  
<a name="BKMK_changetracking"></a>

## Use change tracking to synchronize data with external systems

The change tracking feature allows you to keep the data synchronized in an efficient manner by detecting what data has changed since the data was initially extracted or last synchronized. Changes made in entities can be tracked using Web API requests by adding `odata.track-changes` as a preference header. Preference header `odata.track-changes` requests that a delta link be returned which can subsequently be used to retrieve entity changes.

More information: [Use change tracking to synchronize data with external systems](../use-change-tracking-synchronize-data-external-systems.md).

## Column comparison using the Web API

The following example shows how to compare columns using the Web API:

```http
https://<environment-root>/contacts?$select=firstname&$filter=firstname eq lastname
```

More information: [Use column comparison in queries](../column-comparison.md)

### See also

[Search across table data using Dataverse search](relevance-search.md)  
[Work with Quick Find’s search item limit](../quick-find-limit.md)  
[Web API Query Data Sample (C#)](samples/cdswebapiservice-query-data.md)<br />
[Web API Query Data Sample (Client-side JavaScript)](samples/query-data-client-side-javascript.md)<br />
[Perform operations using the Web API](perform-operations-web-api.md)<br />
[Compose Http requests and handle errors](compose-http-requests-handle-errors.md)<br />
[Create a table using the Web API](create-entity-web-api.md)<br />
[Retrieve a table using the Web API](retrieve-entity-using-web-api.md)<br />
[Update and delete tables using the Web API](update-delete-entities-using-web-api.md)<br />
[Associate and disassociate tables using the Web API](associate-disassociate-entities-using-web-api.md)<br />
[Use Web API functions](use-web-api-functions.md)<br />
[Use Web API actions](use-web-api-actions.md)<br />
[Execute batch operations using the Web API](execute-batch-operations-using-web-api.md)<br />
[Impersonate another user using the Web API](impersonate-another-user-web-api.md)<br />
[Perform conditional operations using the Web API](perform-conditional-operations-using-web-api.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
