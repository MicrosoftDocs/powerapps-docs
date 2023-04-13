---
title: "Query data using the Web API"
description: "Learn how to query Microsoft Dataverse table data using the Web API and the options that can be applied in these queries."
ms.date: 03/27/2023
author: divkamath
ms.author: dikamath
ms.reviewer: jdaly
search.audienceType: 
  - developer
contributors: 
  - JimDaly
---
# Query data using the Web API

When you retrieve data with a query, you must make the following choices:

|Choice|Description|
|---------|---------|
|[Select Columns](#select-columns)|Which columns of data to return.|
|[Join Tables](#join-tables)|Which related tables to include in the results.|
|[Order rows](#order-rows)|What order to return the results.|
|[Filter rows](#filter-rows)|Which rows of data to return.|
|[Page results](#page-results)|How many rows of data to return.|
|[Aggregate data](#aggregate-data)|How to group and aggregate the data returned.|
|[Count number of rows](#count-number-of-rows)|How to count the number of rows.|

This article explains how to apply these choices when constructing a query to retrieve data using the Dataverse Web API.

> [!NOTE]
> This article is about querying data found in tables. You can also query data about table definitions. The structure of the data is different, so many of the capabilities described here do not apply. More information: [Query table definitions using the Web API](query-metadata-web-api.md) and [Query schema definitions](../query-schema-definitions.md)

## Entity Collections

Every query begins with a collection of entities. Entity collections can be either:

- [EntitySet resources](#entityset-resources): One of the Web API EntitySet collections.
- [Filtered collections](#filtered-collections): A set of entities returned by a collection-valued navigation property for a specific record.

### EntitySet resources

To find all the EntitySet resources available in your environment, send a `GET` request to the Web API [Service document](web-api-service-documents.md#service-document):

**Request**

```http
GET [Organization URI]/api/data/v9.2/
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0
If-None-Match: null
```

**Response**

```http
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  

{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata",
    "value": [
        {
            "name": "aadusers",
            "kind": "EntitySet",
            "url": "aadusers"
        },
        {
            "name": "accountleadscollection",
            "kind": "EntitySet",
            "url": "accountleadscollection"
        },
        {
            "name": "accounts",
            "kind": "EntitySet",
            "url": "accounts"
        }
      ... <Truncated for brevity>
```

> [!TIP]
> These values are usually plural name of the table. But they can be different. Use this query to make sure you are using the correct EntitySet resource name.

If you want to retrieve data from the [account table](../reference/entities/account.md), you start with the `accounts` EntitySet resource.

```http
GET [Organization URI]/api/data/v9.2/accounts?$select=name
```

### Filtered collections

You can query any collection of entities represented by a collection-valued navigation property of a specified record.

If you want to retrieve data from the [account EntityType](xref:Microsoft.Dynamics.CRM.account), where a specific user is the [OwningUser](../reference/entities/account.md#BKMK_OwningUser), you can use the `user_accounts` collection-valued navigation property from specified [systemuser](xref:Microsoft.Dynamics.CRM.systemuser) record.

```http
GET [Organization URI]/api/data/v9.2/systemusers(<systemuserid value>)/user_accounts?$select=name
```

To locate the name of the collection-valued navigation property

- For any Dataverse tables and relationships, you can check the <xref:Microsoft.Dynamics.CRM.EntityTypeIndex?displayProperty=fullName>
- For any custom tables or relationships, look for the [Collection-valued navigation properties](web-api-navigation-properties.md#collection-valued-navigation-properties) within the [$metadata service document](web-api-service-documents.md#csdl-metadata-document)


## OData query options

Dataverse Web API supports the following OData query options:


|Option|Description|More information|
|---------|---------|---------|
|`$select`|Use this to request a specific set of properties for each entity or complex type.|[Select Columns](#select-columns)|
|`$top`|Use this to specify the number of items in the queried collection to be included in the result. Don't use this when you retrieving pages of data. |[Page results](#page-results) |
|`$expand`|Use this to specify the related resources to be included in line with retrieved resources. |[Join Tables](#join-tables)|
|`$filter `|Use this to filter a collection of resources that are addressed by a request URL. |[Filter rows](#filter-rows)|
|`$orderby`|Use this to request resources in a particular order. |[Order rows](#order-rows)|
|`$apply`|Use this to aggregate and group your data. |[Aggregate data](#aggregate-data)|
|`$count`|Use this to request a count of the matching resources included with the resources in the response. |[Count number of rows](#count-number-of-rows)|

You can apply multiple options to a query. All query options must be separated from the resource path using '`?`'. After the first option, each option must be separated by '`&`'. The names of all options are case sensitive.

The following OData query options are not supported by Dataverse Web API: `$skip`,`$search`,`$format`.

## Select Columns

> [!IMPORTANT]
> When you query data, it is important to limit the amount of data returned to optimize performance. Only select the columns with data that you need.

Use the OData `$select` query option to choose which columns to return with your query. If you don't include a `$select` query option, all properties will be returned. In OData, every column is represented as a *property*. More information: [Web API Properties](web-api-properties.md)

**Request**

```http
GET [Organization URI]/api/data/v9.2/accounts?$select=name,revenue&$top=1
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
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#accounts(name,revenue)",
    "value": [
        {
            "@odata.etag": "W/\"81052965\"",
            "name": "Litware, Inc. (sample)",
            "revenue": 20000.0000,
            "_transactioncurrencyid_value": "228f42f8-e646-e111-8eb7-78e7d162ced1",
            "accountid": "4624eff7-53d3-ed11-a7c7-000d3a993550"
        }
    ]
}
```

The primary key property is always returned so you don't need to include it in your `$select`. In this example, `accountid` is the primary key.

Other property values may also be included. In this case, the `_transactioncurrencyid_value` [lookup property](web-api-properties.md#lookup-properties) for the related [Currency (TransactionCurrency)  table/entity reference](../reference/entities/transactioncurrency.md) is included because revenue is a currency property.

### Which properties are available?

All the available properties for an entity are found in the [$metadata service document](web-api-service-documents.md#csdl-metadata-document). More information: [Web API Properties](web-api-properties.md)

For the entity types included with Dataverse, see <xref:Microsoft.Dynamics.CRM.EntityTypeIndex>.

> [!TIP]
> The easiest way to quickly discover which properties are available is to send a request using the `$top` system query option with a value of `1` without using `$select`.

### Formatted values

Formatted values are string values generated on the server that you can use in your application. Formatted values include:

- The localized labels for choice, choices, yes/no, status, and status reason columns
- The primary name value for lookup and owner properties
- Currency values with currency symbols.
- Formatted date values in the user's time zone

To include formatted values in your results, use the `Prefer: odata.include-annotations="OData.Community.Display.V1.FormattedValue"` request header. This is one of several annotations you can request. Use `Prefer: odata.include-annotations="*"` to include all annotations. More information: [Request annotations](#request-annotations)

The formatted value is returned with the record with an annotation that follows this convention: `<property name>@OData.Community.Display.V1.FormattedValue` as shown in the following example.

**Request**

```http
GET [Organization URI]/api/data/v9.2/accounts?$select=name,revenue,_primarycontactid_value,customertypecode,modifiedon&$top=1
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
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#accounts(name,revenue)",
    "value": [
{
            "@odata.etag": "W/\"81359849\"",
            "name": "Litware, Inc. (sample)",
            "revenue@OData.Community.Display.V1.FormattedValue": "$20,000.00",
            "revenue": 20000.0000,
            "_primarycontactid_value@OData.Community.Display.V1.FormattedValue": "Susanna Stubberod (sample)",
            "_primarycontactid_value": "70bf4d48-34cb-ed11-b596-0022481d68cd",
            "customertypecode@OData.Community.Display.V1.FormattedValue": "Competitor",
            "customertypecode": 1,
            "modifiedon@OData.Community.Display.V1.FormattedValue": "4/7/2023 2:59 PM",
            "modifiedon": "2023-04-07T21:59:01Z",
            "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
            "_transactioncurrencyid_value": "228f42f8-e646-e111-8eb7-78e7d162ced1",
            "accountid": "78914942-34cb-ed11-b596-0022481d68cd"
        }
    ]
}
```

### Lookup property data

When a [lookup property](web-api-properties.md#lookup-properties) represents a multi-table (polymorphic) relationship, you need to request specific annotations to determine which table contains the related data.

For example, many tables have records that can be owned by users or teams. This data is stored in a lookup column named `ownerid`. This column is represented by a single-valued navigation property in OData. You can't use `$select` to get this value, but you can use the corresponding `_ownerid_value` lookup property with `$select`.

When you include the `_ownerid_value` lookup property with your `$select`, it will return a Guid value, but it will not tell you whether the owner of the record is a user or a team. You need to request annotations to get this data.

To include these annotations in your results, use the `Prefer: odata.include-annotations="Microsoft.Dynamics.CRM.associatednavigationproperty,Microsoft.Dynamics.CRM.lookuplogicalname"` request header. This is one of several annotations you can request. Or you can uses `Prefer: odata.include-annotations="*"` to include all annotations. More information: [Request annotations](#request-annotations)

The following example shows two different account records. The first is owned by a `team`, the second by a `systemuser`:

**Request**

```http
GET [Organization URI]/api/data/v9.2/accounts?$select=name,_ownerid_value&$top=2
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0
Prefer: odata.include-annotations="Microsoft.Dynamics.CRM.associatednavigationproperty,Microsoft.Dynamics.CRM.lookuplogicalname"
```

**Response**

```http
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0
Preference-Applied: odata.include-annotations="Microsoft.Dynamics.CRM.associatednavigationproperty,Microsoft.Dynamics.CRM.lookuplogicalname"

{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#accounts(name,_ownerid_value)",
    "value": [
        {
            "@odata.etag": "W/\"81550512\"",
            "name": "Adventure Works (sample)",
            "_ownerid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "ownerid",
            "_ownerid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "team",
            "_ownerid_value": "39e0dbe4-131b-e111-ba7e-78e7d1620f5e",
            "accountid": "1adef0b8-54d3-ed11-a7c7-000d3a993550"
        },
        {
            "@odata.etag": "W/\"81359849\"",
            "name": "Litware, Inc. (sample)",
            "_ownerid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "ownerid",
            "_ownerid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "systemuser",
            "_ownerid_value": "4026be43-6b69-e111-8f65-78e7d1620f5e",
            "accountid": "78914942-34cb-ed11-b596-0022481d68cd"
        }
    ]
}
```

- `<lookup property name>@Microsoft.Dynamics.CRM.lookuplogicalname` is the logical name of the related table.
- `<lookup property name>@Microsoft.Dynamics.CRM.associatednavigationproperty` is the name of the corresponding single-valued navigation property.


### Request annotations

In addition to properties, you can request different OData annotation data to be returned with the results using the `Prefer: odata.include-annotations` request header. You can choose to return all annotations, or specify specific annotations. The following table describes the annotations Dataverse Web API supports:


|Annotation|Description|
|---------|---------|
|`OData.Community.Display.V1.FormattedValue`|See [Formatted values](#formatted-values)|
|`Microsoft.Dynamics.CRM.associatednavigationproperty`<br />`Microsoft.Dynamics.CRM.lookuplogicalname`|See [Lookup property data](#lookup-property-data)|
|`Microsoft.Dynamics.CRM.totalrecordcount`<br />`Microsoft.Dynamics.CRM.totalrecordcountlimitexceeded`|When you use the `$count` query option the `@odata.count` annotation tells the number of records, but only 5000 records can be returned at a time. Request the `Microsoft.Dynamics.CRM.totalrecordcountlimitexceeded` to get a boolean value that will tell you if the total number of records matching the query exceeds 5000.  More information: [Count number of rows](#count-number-of-rows) |
|`Microsoft.Dynamics.CRM.globalmetadataversion`|This annotation is returned on the request and you can cache it in your application. This value will change when any schema change occurs. This is an indication that you may need to refresh any schema data that your application has cached. More information: [Cache Schema data](../cache-schema-data.md)|
|`Microsoft.PowerApps.CDS.ErrorDetails.OperationStatus`<br />`Microsoft.PowerApps.CDS.ErrorDetails.SubErrorCode`<br />`Microsoft.PowerApps.CDS.HelpLink`<br />`Microsoft.PowerApps.CDS.TraceText`<br />`Microsoft.PowerApps.CDS.InnerError.Message`|These annotations provide additional details when errors are returned. More information: [Include more details with errors](compose-http-requests-handle-errors.md#include-more-details-with-errors)|

> [!TIP]
> It is common to use the `Prefer: odata.include-annotations="*"` request header to return all annotations.

If you want only specific annotations, you can request them as comma separated values. You can also use the '`*`' character as a wildcard.  For example, the following `Prefer` request header only includes the formatted values and any additional error detail annotations:

> `Prefer: odata.include-annotations="OData.Community.Display.V1.FormattedValue,Microsoft.PowerApps.CDS.ErrorDetails*"`

## Join Tables

Use the `$expand` system query option specify the related resources to be included in line with retrieved resources.

<!-- 

This should mostly correspond to the existing retrieve-related-entities-query topic, recently re-written
Look at other sections to see how much is necessary to explain.
 -->

## Order rows

Specify the order in which items are returned using the `$orderby` system query option. Use the `asc` or `desc` suffix to specify ascending or descending order respectively. The default is ascending if the suffix isn't applied. The following example shows retrieving the `name` and `revenue` properties of accounts ordered by ascending `revenue` and by descending `name`.

```http
GET [Organization URI]/api/data/v9.2/accounts?$select=name,revenue
&$orderby=revenue asc,name desc
&$filter=revenue ne null
```

<!-- Not really much to say here -->

## Filter rows

Use the `$filter` system query option to filter a collection of resources that are addressed by a request URL.

Dataverse evaluates each resource in the collection using the expression set for `$filter`. Only records where the expression evaluates to `true` are returned in the response. Records are not returned if the expression evaluates to `false` or `null`, or if the user doesn't have read access to the record.

To compose `$filter` expressions you can apply the following:


| |Description| More information|
|---------|---------|---------|
|**Comparison operators**|Use the `eq`,`ne`,`gt`,`ge`,`lt`, and `le` operators to compare a property and a value.|[ Comparison operators](#comparison-operators)|
|**Logical operators**|Use `and`, `or`, and `not` to create more complex expressions. |[Logical operators](#logical-operators)|
|**Grouping operators**|Use parentheses: `(` & `)`, to specify the precedence to evaluate a complex expression. |[Grouping operators](#grouping-operators)|
|**OData query functions**|Evaluate string values using `contains`, `endswith`, and `startswith` functions. |[Use OData query functions](#use-odata-query-functions)|
|**Dataverse query functions**|Use more than 60 specialized functions designed for business applications. |[Dataverse query functions](#dataverse-query-functions)|
|**Lambda Expressions**|Create expressions based on values of related collections. |[Filter using values of related collections](#filter-using-values-of-related-collections)|

> [!TIP]
> Remember that you can also use [Filtered collections](#filtered-collections).
>
> If you are using a [lookup property](web-api-properties.md#lookup-properties) in a `$filter`, you could also use a filtered collection with the corresponding collection-valued navigation property.
>
> For example, these two queries return the same results:
>
> `accounts?$filter=_owninguser_value eq '<systemuserid value>'&$select=name`
>
> `systemusers(<systemuserid value>)/user_accounts?$select=name`


### Comparison operators

Use the following comparison operators to compare a property and a value.

|Operator|Description|Example|  
|--------------|-----------------|-------------|
|`eq`|Equal|`$filter=revenue eq 100000`|  
|`ne`|Not Equal|`$filter=revenue ne 100000`|  
|`gt`|Greater than|`$filter=revenue gt 100000`|  
|`ge`|Greater than or equal|`$filter=revenue ge 100000`|  
|`lt`|Less than|`$filter=revenue lt 100000`|  
|`le`|Less than or equal|`$filter=revenue le 100000`|  

#### Column comparison

You can use comparison operators to compare property values in the same row. For example, the following query will return any contacts where the `firstname` equals `lastname`.

```http
GET [Organization URI]/api/data/v9.2/contacts?$select=fullname&$filter=firstname eq lastname
```

> [!NOTE]
> - Only comparison operators can be used to compare values in the same row.
> - The types of columns must match.

More information: [Use column comparison in queries](../column-comparison.md)

### Logical operators

Use the following logical operators to create more complex expressions:

|Operator|Description|Example|  
|--------------|-----------------|-------------|
|`and`|Logical and|`$filter=revenue lt 100000 and revenue gt 2000`|  
|`or`|Logical or|`$filter=contains(name,'(sample)') or contains(name,'test')`|  
|`not`|Logical negation|`$filter=not contains(name,'sample')`|  

### Grouping operators

Use parentheses `(` & `)`, with logical operators to specify the precedence to evaluate a complex expression. For example:<br />
`$filter=(contains(name,'sample') or contains(name,'test')) and revenue gt 5000`

### Dataverse query functions

Use more than 60 specialized functions designed for business applications. These functions provide special capabilities as described in the following table:

|Group|Functions|
|---------|---------|
|**Dates** |<xref:Microsoft.Dynamics.CRM.InFiscalPeriod>, <xref:Microsoft.Dynamics.CRM.InFiscalPeriodAndYear>, <xref:Microsoft.Dynamics.CRM.InFiscalYear>, <xref:Microsoft.Dynamics.CRM.InOrAfterFiscalPeriodAndYear>, <xref:Microsoft.Dynamics.CRM.InOrBeforeFiscalPeriodAndYear>,<br /><xref:Microsoft.Dynamics.CRM.Last7Days>, <xref:Microsoft.Dynamics.CRM.LastFiscalPeriod>, <xref:Microsoft.Dynamics.CRM.LastFiscalYear>, <xref:Microsoft.Dynamics.CRM.LastMonth>, <xref:Microsoft.Dynamics.CRM.LastWeek>, <xref:Microsoft.Dynamics.CRM.LastXDays>, <xref:Microsoft.Dynamics.CRM.LastXFiscalPeriods>, <xref:Microsoft.Dynamics.CRM.LastXFiscalYears>,<br /><xref:Microsoft.Dynamics.CRM.LastXHours>, <xref:Microsoft.Dynamics.CRM.LastXMonths>, <xref:Microsoft.Dynamics.CRM.LastXWeeks>, <xref:Microsoft.Dynamics.CRM.LastXYears>, <xref:Microsoft.Dynamics.CRM.LastYear>, <xref:Microsoft.Dynamics.CRM.Next7Days>, <xref:Microsoft.Dynamics.CRM.NextFiscalPeriod>, <xref:Microsoft.Dynamics.CRM.NextFiscalYear>,<br /><xref:Microsoft.Dynamics.CRM.NextMonth>, <xref:Microsoft.Dynamics.CRM.NextWeek>, <xref:Microsoft.Dynamics.CRM.NextXDays>, <xref:Microsoft.Dynamics.CRM.NextXFiscalPeriods>, <xref:Microsoft.Dynamics.CRM.NextXFiscalYears>, <xref:Microsoft.Dynamics.CRM.NextXHours>, <xref:Microsoft.Dynamics.CRM.NextXMonths>,<br /><xref:Microsoft.Dynamics.CRM.NextXWeeks>, <xref:Microsoft.Dynamics.CRM.NextXYears>, <xref:Microsoft.Dynamics.CRM.NextYear>, <xref:Microsoft.Dynamics.CRM.OlderThanXDays>, <xref:Microsoft.Dynamics.CRM.OlderThanXHours>, <xref:Microsoft.Dynamics.CRM.OlderThanXMinutes>, <xref:Microsoft.Dynamics.CRM.OlderThanXMonths>,<br /><xref:Microsoft.Dynamics.CRM.OlderThanXWeeks>, <xref:Microsoft.Dynamics.CRM.OlderThanXYears>, <xref:Microsoft.Dynamics.CRM.On>, <xref:Microsoft.Dynamics.CRM.OnOrAfter>, <xref:Microsoft.Dynamics.CRM.OnOrBefore>, <xref:Microsoft.Dynamics.CRM.ThisFiscalPeriod>, <xref:Microsoft.Dynamics.CRM.ThisFiscalYear>, <xref:Microsoft.Dynamics.CRM.ThisMonth>, <xref:Microsoft.Dynamics.CRM.ThisWeek>, <xref:Microsoft.Dynamics.CRM.ThisYear>, <xref:Microsoft.Dynamics.CRM.Today>, <xref:Microsoft.Dynamics.CRM.Tomorrow>, <xref:Microsoft.Dynamics.CRM.Yesterday>|
|**Id Values**|<xref:Microsoft.Dynamics.CRM.EqualBusinessId>, <xref:Microsoft.Dynamics.CRM.EqualUserId>, <xref:Microsoft.Dynamics.CRM.NotEqualBusinessId>, <xref:Microsoft.Dynamics.CRM.NotEqualUserId>|
|**Hierarchy**|<xref:Microsoft.Dynamics.CRM.Above>, <xref:Microsoft.Dynamics.CRM.AboveOrEqual>, <xref:Microsoft.Dynamics.CRM.EqualUserOrUserHierarchy>, <xref:Microsoft.Dynamics.CRM.EqualUserOrUserHierarchyAndTeams>, <xref:Microsoft.Dynamics.CRM.EqualUserOrUserTeams>, <br /><xref:Microsoft.Dynamics.CRM.EqualUserTeams>, <xref:Microsoft.Dynamics.CRM.NotUnder>, <xref:Microsoft.Dynamics.CRM.Under>, <xref:Microsoft.Dynamics.CRM.UnderOrEqual><br />More information: [Query hierarchical data](../query-hierarchical-data.md)|
|**Choices columns**|<xref:Microsoft.Dynamics.CRM.ContainValues>, <xref:Microsoft.Dynamics.CRM.DoesNotContainValues><br />More information: [Query data from choices](../multi-select-picklist.md#query-data-from-choices)|
|**Between**|<xref:Microsoft.Dynamics.CRM.Between>, <xref:Microsoft.Dynamics.CRM.NotBetween>|
|**In**|<xref:Microsoft.Dynamics.CRM.In>, <xref:Microsoft.Dynamics.CRM.NotIn>|
|**Language**|<xref:Microsoft.Dynamics.CRM.EqualUserLanguage>|

> [!NOTE]
> The [Contains Function](xref:Microsoft.Dynamics.CRM.Contains) is for use with columns that have full-text indexing. Only the Dynamics 365 KBArticle (article) table has columns that have full-text indexing. Use the OData `contains` function instead.

See <xref:Microsoft.Dynamics.CRM.QueryFunctionIndex?displayProperty=fullName> for the complete list. Each article provides a syntax example you can copy.

You must use the *fully qualified name* of these functions. This means you must append the [Service namespace](web-api-service-documents.md#service-namespace) (`Microsoft.Dynamics.CRM`) to the name of the function.

Each function has a `PropertyName` parameter that specifies which property to be evaluated. The function may have additional parameters such as `PropertyValue`, `PropertyValues`, or `PropertyValue1` and `PropertyValue2`. When these parameters exist, you must supply a value, or values, to compare to the `PropertyName` parameter.

The following is an example of the [Between Function](xref:Microsoft.Dynamics.CRM.Between) searching for accounts with a number of employees between 5 and 2000.  
  
```http 
GET [Organization URI]/api/data/v9.2/accounts?$select=name,numberofemployees
&$filter=Microsoft.Dynamics.CRM.Between(PropertyName='numberofemployees',PropertyValues=["5","2000"])  
```  

### Filter using string values

Keep the following in mind while filtering on string values:

- All filters using string values are case insensitive.
- You may use wildcard characters, but avoid trailing wildcards. More information: [Use wildcard characters](#use-wildcard-characters)
- You can use OData query functions: `contains`, `startswith`, `endswith`. More information: [Use OData query functions](#use-odata-query-functions)
- You must manage single quotes when using filters that accept an array of string values. More information: [Manage single quotes](#manage-single-quotes)

#### Use wildcard characters

When composing filters using strings, you can apply the following wildcard characters:

|Characters  |Description  |T-SQL Documentation and examples  |
|---------|---------|---------|
|`% ` |Matches any string of zero or more characters. This wildcard character can be used as either a prefix or a suffix.|[Percent character (Wildcard - Character(s) to Match) (Transact-SQL)](/sql/t-sql/language-elements/percent-character-wildcard-character-s-to-match-transact-sql)|
|`_`  |Use the underscore character to match any single character in a string comparison operation that involves pattern matching.|[_ (Wildcard - Match One Character) (Transact-SQL)](/sql/t-sql/language-elements/wildcard-match-one-character-transact-sql)|
|`[]` |Matches any single character within the specified range or set that is specified between brackets.|[[ ] (Wildcard - Character(s) to Match) (Transact-SQL)](/sql/t-sql/language-elements/wildcard-character-s-to-match-transact-sql)|
|`[^]`|Matches any single character that is not within the range or set specified between the square brackets.|[[^] (Wildcard - Character(s) Not to Match) (Transact-SQL)](/sql/t-sql/language-elements/wildcard-character-s-not-to-match-transact-sql)|

More information: [Use wildcard characters in conditions for string values](../wildcard-characters.md)

##### Trailing wildcards not supported

When using wildcard characters, it is important not to use trailing wild cards. They are not supported. Queries using these anti-patterns introduce performance problems because the queries cannot be optimized. Some examples of trailing wildcards:

```
startswith(name,'%value')
endswith(name,'value%')
```

#### Use OData query functions

OData provides the following query functions:

|Function|Example|  
|--------------|-------------|  
|`contains`|`$filter=contains(name,'(sample)')`|  
|`endswith`|`$filter=endswith(name,'Inc.')`|  
|`startswith`|`$filter=startswith(name,'a')`|

You can use these functions together with the logical operator `not` to negate the result.

#### Manage single quotes

When specifying values for comparison in filters that accept an array of string values, such as the [In Query Function](xref:Microsoft.Dynamics.CRM.In), which contain single quote "`'`" (apostrophe) characters, such as `O'Brian` or `Men's clothes` you must use double quotes around the values. For example: 

```http
GET [Organization URI]/api/data/v9.2/contacts?$select=fullname
&$filter=Microsoft.Dynamics.CRM.In(PropertyName=@p1,PropertyValues=@p2)
&@p1='lastname'
&@p2=["OBrian","OBryan","O'Brian","O'Bryan"]
```

Otherwise you will get the following error: `Invalid JSON. A comma character ',' was expected in scope 'Array'. Every two elements in an array and properties of an object must be separated by commas.`

If the filter is for a single value, replace the single quote character with two consecutive single quote characters. For example:

```http
GET [Organization URI]/api/data/v9.2/contacts?$select=fullname
&$filter=lastname eq 'O''Bryan'
```

Otherwise you will get an error like the following: `There is an unterminated literal at position 21 in 'lastname eq 'O'Bryan''.`

### Filter based on related data values

You can filter rows returned based on values in related tables. How you do this depends on the type of relationship.

#### Filter using lookup column property values

You can filter based on values in single-valued navigation properties that represent lookup columns. Use this pattern:

`<single-valued navigation property>/<property name>`

The following example returns account records based on the value of the `primarycontactid/fullname` column.

**Request**

```http
GET [Organization URI]/api/data/v9.2/accounts?$filter=primarycontactid/fullname eq 'Susanna Stubberod (sample)'
&$select=name,_primarycontactid_value
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
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#accounts(name,_primarycontactid_value)",
    "value": [
        {
            "@odata.etag": "W/\"81359849\"",
            "name": "Litware, Inc. (sample)",
            "_primarycontactid_value@OData.Community.Display.V1.FormattedValue": "Susanna Stubberod (sample)",
            "_primarycontactid_value": "70bf4d48-34cb-ed11-b596-0022481d68cd",
            "accountid": "78914942-34cb-ed11-b596-0022481d68cd"
        }
    ]
}
```

You can also compare values of further up the hierarchy of single-valued navigation properties.

This example will return the first account where the contact record representing the `primarycontactid` was created by 'System Administrator', using `primarycontactid/createdby/fullname` in the `$filter`.

**Request**

```http
GET [Organization URI]/api/data/v9.2/accounts?$filter=primarycontactid/createdby/fullname eq 'System Administrator'
&$select=name,_primarycontactid_value
&$expand=primarycontactid(
$select=fullname,_createdby_value;
$expand=createdby($select=fullname))
&$top=1
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
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#accounts(name,_primarycontactid_value,primarycontactid(fullname,_createdby_value,createdby(fullname)))",
    "value": [
        {
            "@odata.etag": "W/\"81359849\"",
            "name": "Litware, Inc. (sample)",
            "_primarycontactid_value@OData.Community.Display.V1.FormattedValue": "Susanna Stubberod (sample)",
            "_primarycontactid_value": "70bf4d48-34cb-ed11-b596-0022481d68cd",
            "accountid": "78914942-34cb-ed11-b596-0022481d68cd",
            "primarycontactid": {
                "fullname": "Susanna Stubberod (sample)",
                "_createdby_value@OData.Community.Display.V1.FormattedValue": "System Administrator",
                "_createdby_value": "4026be43-6b69-e111-8f65-78e7d1620f5e",
                "contactid": "70bf4d48-34cb-ed11-b596-0022481d68cd",
                "createdby": {
                    "fullname": "System Administrator",
                    "systemuserid": "4026be43-6b69-e111-8f65-78e7d1620f5e",
                    "ownerid": "4026be43-6b69-e111-8f65-78e7d1620f5e"
                }
            }
        }
    ]
}
```

#### Filter using values of related collections

Use *Lambda operators* (`any` & `all` ) to get evaluate values in a collection to filter the results.


|Operator|Description|
|---------|---------|
|`any`|Returns `true` if the expression applied is true for any member of the collection, otherwise it returns false. The `any` operator without an argument returns `true` if the collection is not empty.|
|`all`|Returns true if the expression applied is true for all members of the collection, otherwise it returns false.|

The syntax looks like this:

`<collection>/[any | all](o:<expression to evaluate>)`

In this case `o` is the variable that represents items in the collection. The convention is to use the first letter of the type.
Within the expression, use `o/<property or collection name>` to refer to property or collection of a given item.

You can include conditions on multiple collection-valued navigation properties and nested collections.

More information: [Lambda Operators at odata.org](https://www.odata.org/getting-started/basic-tutorial/#lambda)

##### Lambda operator examples

The example given below shows how you can retrieve all account entity records that have at least one email with `sometext` in the subject.

```http
GET [Organization URI]/api/data/v9.2/accounts?$select=name
&$filter=Account_Emails/any(e:contains(e/subject,'sometext'))
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0
```

The example given below shows how you can retrieve all account entity records that have all associated tasks closed.

```http
GET [Organization URI]/api/data/v9.2/accounts?$select=name
&$filter=Account_Tasks/all(t:t/statecode eq 1)
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0
```

The example given below shows how you can retrieve all account entity records that have at least one email with "sometext" in the subject and whose statecode is active.

```http
GET [Organization URI]/api/data/v9.2/accounts?$select=name
&$filter=Account_Emails/any(e:contains(e/subject,'sometext') and 
e/statecode eq 0)
Accept: application/json
OData-MaxVersion: 4.0
OData-Version: 4.0
```

The example given below shows how you can also create a nested query using `any` and `all` operators.

```http
GET [Organization URI]/api/data/v9.2/accounts?$select=name
&$filter=(contact_customer_accounts/any(c:c/jobtitle eq 'jobtitle' and 
c/opportunity_customer_contacts/any(o:o/description ne 'N/A'))) and 
endswith(name,'Inc.')
Accept: application/json
OData-MaxVersion: 4.0
OData-Version: 4.0
```

## Page results

You can control the number of records returned using the `Prefer: odata.maxpagesize` request header. If you don't specify the number records to return, up to 5000 records may be returned for each request. You can't request a page size larger than 5000.

> [!NOTE]
> Dataverse doesn't support the `$skip` query option, so the combination of `$top` and `$skip` can't be used for paging. More information: [Use $top query option](#use-top-query-option)

The following example returns just the first two contact records:

**Request**

```http
GET [Organization URI]/api/data/v9.2/contacts?$select=fullname
Accept: application/json
OData-MaxVersion: 4.0
OData-Version: 4.0
Prefer: odata.maxpagesize=2
```

**Response**

```http
HTTP/1.1 200 OK
OData-Version: 4.0
Preference-Applied: odata.maxpagesize=2

{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#contacts(fullname)",
    "value": [
        {
            "@odata.etag": "W/\"72201545\"",
            "fullname": "Yvonne McKay (sample)",
            "contactid": "49b0be2e-d01c-ed11-b83e-000d3a572421"
        },
        {
            "@odata.etag": "W/\"80648695\"",
            "fullname": "Susanna Stubberod (sample)",
            "contactid": "70bf4d48-34cb-ed11-b596-0022481d68cd"
        }
    ],
    "@odata.nextLink": "[Organization URI]/api/data/v9.2/contacts?$select=fullname&$skiptoken=%3Ccookie%20pagenumber=%222%22%20pagingcookie=%22%253ccookie%2520page%253d%25221%2522%253e%253ccontactid%2520last%253d%2522%257bD5026A4D-D01C-ED11-B83E-000D3A572421%257d%2522%2520first%253d%2522%257b49B0BE2E-D01C-ED11-B83E-000D3A572421%257d%2522%2520%252f%253e%253c%252fcookie%253e%22%20istracking=%22False%22%20/%3E"
}
```

When there are more records than requested, the `@odata.nextLink` annotation provides a URL you can use with `GET` to return the next page of data.

**Request**

```http
GET [Organization URI]/api/data/v9.2/contacts?$select=fullname&$skiptoken=%3Ccookie%20pagenumber=%222%22%20pagingcookie=%22%253ccookie%2520page%253d%25221%2522%253e%253ccontactid%2520last%253d%2522%257bD5026A4D-D01C-ED11-B83E-000D3A572421%257d%2522%2520first%253d%2522%257b49B0BE2E-D01C-ED11-B83E-000D3A572421%257d%2522%2520%252f%253e%253c%252fcookie%253e%22%20istracking=%22False%22%20/%3E
Accept: application/json
OData-MaxVersion: 4.0
OData-Version: 4.0
Prefer: odata.maxpagesize=2
```

**Response**

```http
HTTP/1.1 200 OK
OData-Version: 4.0
Preference-Applied: odata.maxpagesize=2

{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#contacts(fullname)",
    "value": [
        {
            "@odata.etag": "W/\"80648710\"",
            "fullname": "Nancy Anderson (sample)",
            "contactid": "72bf4d48-34cb-ed11-b596-0022481d68cd"
        },
        {
            "@odata.etag": "W/\"80648724\"",
            "fullname": "Maria Campbell (sample)",
            "contactid": "74bf4d48-34cb-ed11-b596-0022481d68cd"
        }
    ],
    "@odata.nextLink": "[Organization URI]/api/data/v9.2/contacts?$select=fullname&$skiptoken=%3Ccookie%20pagenumber=%223%22%20pagingcookie=%22%253ccookie%2520page%253d%25222%2522%253e%253ccontactid%2520last%253d%2522%257bF2318099-171F-ED11-B83E-000D3A572421%257d%2522%2520first%253d%2522%257bBB55F942-161F-ED11-B83E-000D3A572421%257d%2522%2520%252f%253e%253c%252fcookie%253e%22%20istracking=%22False%22%20/%3E"
}
```

You should cache the results returned or the `@odata.nextLink` URL value and use it to return to previous pages.

Don't change or append any additional system query options to the `@odata.nextLink` URL value. For every subsequent request for additional pages, you should use the same `odata.maxpagesize` preference value used in the original request. You can continue paging through the data until no `@odata.nextLink` is included in the results.

In the examples above you can see that there is encoded information set as the value of the `$skiptoken` parameter within the `@odata.nextLink` URL value. This is set by the server to control paging. You should not modify the encoded information or encode it further, just use the URL value provided to retrieve the next page.

### Use $top query option

You can limit the number of results returned by using the `$top` system query option. The following example will return just the first three account rows.

```http
GET [Organization URI]/api/data/v9.2/accounts?$select=name,revenue&$top=3
```

You should not use `$top` together with the `Prefer: odata.maxpagesize` request header. If you include both, `$top `will be ignored.

We also recommend you avoid using `$top` with `$count`. More information: [Count number of rows](#count-number-of-rows)

## Aggregate data



## Count number of rows
