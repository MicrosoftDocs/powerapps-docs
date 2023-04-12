---
title: "Query data using the Web API (Microsoft Dataverse)"
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
# Query data using the Web API (Microsoft Dataverse)

When you retrieve data with a query, you must make the following choices:

|Query element|Description|
|---------|---------|
|[Select Columns](#select-columns)|Choose which columns of data to return.|
|[Join Tables](#join-tables)|Choose which related tables to include in the results.|
|[Order rows](#order-rows)|Choose the order the results are returned.|
|[Filter rows](#filter-rows)|Choose which rows of data to return.|
|[Page results](#page-results)|Choose how many rows of data to return.|
|[Aggregate data](#aggregate-data)|Choose how to group and aggregate the data returned. |

This article explains how to apply these choices when constructing a query to retrieve data using the Dataverse Web API.

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

If you want to retrieve data from the [account](xref:Microsoft.Dynamics.CRM.account), where a specific user is the [OwningUser](../reference/entities/account.md#BKMK_OwningUser), you can use the `user_accounts` collection-valued navigation property from specified [systemuser](xref:Microsoft.Dynamics.CRM.systemuser) record.

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
|`$count`|Use this to request a count of the matching resources included with the resources in the response. |[Retrieve a count of rows](#retrieve-a-count-of-rows)|
|`$apply`|Use this to aggregate and group your data. |[Aggregate data](#aggregate-data)|

You can apply multiple options to a query. All query options must be separated from the resource path using '`?`'. After the first option, each option must be separated by '`&`'. The names of all options are case sensitive.

The following OData  query options are not supported by Dataverse Web API: `$skip`,`$search`,`$format`.

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

The following example shows two different account records. The first is owned by a team, the second by a user:

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
    "@odata.context": "https://crmue.api.crm.dynamics.com/api/data/v9.2/$metadata#accounts(name,_ownerid_value)",
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
|`Microsoft.Dynamics.CRM.totalrecordcount`<br />`Microsoft.Dynamics.CRM.totalrecordcountlimitexceeded`|When you use the `$count` query option the `@odata.count` annotation tells the number of records, but only 5000 records can be returned at a time. Request the `Microsoft.Dynamics.CRM.totalrecordcountlimitexceeded` to get a boolean value that will tell you if the total number of records matching the query exceeds 5000.  More information: [Retrieve a count of rows](#retrieve-a-count-of-rows) |
|`Microsoft.Dynamics.CRM.globalmetadataversion`|This annotation is returned on the request and you can cache it in your application. This value will change when any schema change occurs. This is an indication that you may need to refresh any schema data that your application has cached. More information: [Cache Schema data](../cache-schema-data.md)|
|`Microsoft.PowerApps.CDS.ErrorDetails.OperationStatus`<br />`Microsoft.PowerApps.CDS.ErrorDetails.SubErrorCode`<br />`Microsoft.PowerApps.CDS.HelpLink`<br />`Microsoft.PowerApps.CDS.TraceText`<br />`Microsoft.PowerApps.CDS.InnerError.Message`|These annotations provide additional details when errors are returned. More information: [Include more details with errors](compose-http-requests-handle-errors.md#include-more-details-with-errors)|

> [!TIP]
> It is common to use the `Prefer: odata.include-annotations="*"` request header to return all annotations.

If you want only specific annotations, you can request them as comma separated values. You can also use the '`*`' character as a wildcard.  For example, `Prefer: odata.include-annotations="OData.Community.Display.V1.FormattedValue,Microsoft.PowerApps.CDS.ErrorDetails*"` will include only the formatted values and any additional error detail annotations.

## Join Tables

Use the `$expand `system query option specify the related resources to be included in line with retrieved resources.

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
|**Dates** |<xref:Microsoft.Dynamics.CRM.InFiscalPeriod>,<xref:Microsoft.Dynamics.CRM.InFiscalPeriodAndYear>,<xref:Microsoft.Dynamics.CRM.InFiscalYear>,<xref:Microsoft.Dynamics.CRM.InOrAfterFiscalPeriodAndYear>,<xref:Microsoft.Dynamics.CRM.InOrBeforeFiscalPeriodAndYear>,<xref:Microsoft.Dynamics.CRM.Last7Days>,<br /><xref:Microsoft.Dynamics.CRM.LastFiscalPeriod>,<xref:Microsoft.Dynamics.CRM.LastFiscalYear>,<xref:Microsoft.Dynamics.CRM.LastMonth>,<xref:Microsoft.Dynamics.CRM.LastWeek>,<xref:Microsoft.Dynamics.CRM.LastXDays>,<xref:Microsoft.Dynamics.CRM.LastXFiscalPeriods>,<xref:Microsoft.Dynamics.CRM.LastXFiscalYears>,<xref:Microsoft.Dynamics.CRM.LastXHours>,<xref:Microsoft.Dynamics.CRM.LastXMonths>,<br /><xref:Microsoft.Dynamics.CRM.LastXWeeks>,<xref:Microsoft.Dynamics.CRM.LastXYears>,<xref:Microsoft.Dynamics.CRM.LastYear>,<xref:Microsoft.Dynamics.CRM.Next7Days>,<xref:Microsoft.Dynamics.CRM.NextFiscalPeriod>,<xref:Microsoft.Dynamics.CRM.NextFiscalYear>,<xref:Microsoft.Dynamics.CRM.NextMonth>,<xref:Microsoft.Dynamics.CRM.NextWeek>,<xref:Microsoft.Dynamics.CRM.NextXDays>,<br /><xref:Microsoft.Dynamics.CRM.NextXFiscalPeriods>,<xref:Microsoft.Dynamics.CRM.NextXFiscalYears>,<xref:Microsoft.Dynamics.CRM.NextXHours>,<xref:Microsoft.Dynamics.CRM.NextXMonths>,<xref:Microsoft.Dynamics.CRM.NextXWeeks>,<xref:Microsoft.Dynamics.CRM.NextXYears>,<xref:Microsoft.Dynamics.CRM.NextYear>,<xref:Microsoft.Dynamics.CRM.OlderThanXDays>,<br /><xref:Microsoft.Dynamics.CRM.OlderThanXHours>,<xref:Microsoft.Dynamics.CRM.OlderThanXMinutes>,<xref:Microsoft.Dynamics.CRM.OlderThanXMonths>,<xref:Microsoft.Dynamics.CRM.OlderThanXWeeks>,<xref:Microsoft.Dynamics.CRM.OlderThanXYears>,<xref:Microsoft.Dynamics.CRM.On>,<xref:Microsoft.Dynamics.CRM.OnOrAfter>,<xref:Microsoft.Dynamics.CRM.OnOrBefore>,<xref:Microsoft.Dynamics.CRM.ThisFiscalPeriod>,<xref:Microsoft.Dynamics.CRM.ThisFiscalYear>,<xref:Microsoft.Dynamics.CRM.ThisMonth>,<xref:Microsoft.Dynamics.CRM.ThisWeek>,<xref:Microsoft.Dynamics.CRM.ThisYear>,<xref:Microsoft.Dynamics.CRM.Today>,<xref:Microsoft.Dynamics.CRM.Tomorrow>,<xref:Microsoft.Dynamics.CRM.Yesterday>|
|**Id Values**|<xref:Microsoft.Dynamics.CRM.EqualBusinessId>,<xref:Microsoft.Dynamics.CRM.EqualUserId>,<xref:Microsoft.Dynamics.CRM.NotEqualBusinessId>,<xref:Microsoft.Dynamics.CRM.NotEqualUserId>|
|**Hierarchy**|<xref:Microsoft.Dynamics.CRM.Above>,<xref:Microsoft.Dynamics.CRM.AboveOrEqual>,<xref:Microsoft.Dynamics.CRM.EqualUserOrUserHierarchy>,<xref:Microsoft.Dynamics.CRM.EqualUserOrUserHierarchyAndTeams>,<xref:Microsoft.Dynamics.CRM.EqualUserOrUserTeams>,<br /><xref:Microsoft.Dynamics.CRM.EqualUserTeams>,<xref:Microsoft.Dynamics.CRM.NotUnder>,<xref:Microsoft.Dynamics.CRM.Under>,<xref:Microsoft.Dynamics.CRM.UnderOrEqual><br />More information: [Query hierarchical data](../query-hierarchical-data.md)|
|**Choices columns**|<xref:Microsoft.Dynamics.CRM.ContainValues>,<xref:Microsoft.Dynamics.CRM.DoesNotContainValues><br />More information: [Query data from choices](../multi-select-picklist.md#query-data-from-choices)|
|**Between**|<xref:Microsoft.Dynamics.CRM.Between>,<xref:Microsoft.Dynamics.CRM.NotBetween>|
|**In**|<xref:Microsoft.Dynamics.CRM.In>,<xref:Microsoft.Dynamics.CRM.NotIn>|
|**Language**|<xref:Microsoft.Dynamics.CRM.EqualUserLanguage>|

See <xref:Microsoft.Dynamics.CRM.QueryFunctionIndex?displayProperty=fullName> for the complete list. Each article provides a syntax example you can copy.

You must use the *fully qualified name* of these functions. This means you must append the [Service namespace](web-api-service-documents.md#service-namespace) (`Microsoft.Dynamics.CRM`) to the name of the function.

Each function has a `PropertyName` parameter that specifies which property to be evaluated. The function may have additional parameters such as `PropertyValue`, `PropertyValues`, or `PropertyValue1` and `PropertyValue2` when you must supply a value to compare to the `PropertyName` parameter.

The following is an example of the <xref:Microsoft.Dynamics.CRM.Between?text=Between Function> searching for accounts with a number of employees between 5 and 2000.  
  
```http 
GET [Organization URI]/api/data/v9.2/accounts?$select=name,numberofemployees
&$filter=Microsoft.Dynamics.CRM.Between(PropertyName='numberofemployees',PropertyValues=["5","2000"])  
```  

### Lambda Expressions

### Filter using string values

#### Use wildcard characters

#### Use OData query functions



#### Manage single quotes

### Filter based on related data values

#### Filter using lookup column property values

#### Filter using values of related collections


<!-- Where does this belong? -->
### Retrieve a count of rows

## Page results

### $top

## Aggregate data
