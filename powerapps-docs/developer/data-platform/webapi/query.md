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
GET [Organization URI]/api/data/v9.2/accounts
```

### Filtered collections

You can query any collection of entities represented by a collection-valued navigation property of a specified record.

If you want to retrieve data from the [account table](../reference/entities/account.md), where a specific user is the [OwningUser](../reference/entities/account.md#BKMK_OwningUser), you can use the `user_accounts` collection-valued navigation property.

```http
GET [Organization URI]/api/data/v9.2/systemusers(4026be43-6b69-e111-8f65-78e7d1620f5e)/user_accounts
```

To locate the name of the collection-valued navigation property

- For any Dataverse tables and relationships, you can check the <xref:Microsoft.Dynamics.CRM.EntityTypeIndex?displayProperty=fullName>
- For any custom tables or relationships, look for the [Collection-valued navigation properties](web-api-navigation-properties.md#collection-valued-navigation-properties) within the [$metadata service document](web-api-service-documents.md#csdl-metadata-document)


## System Query options

Dataverse Web API supports the following system query options:


|Option|Description|
|---------|---------|
|`$select`|Use this to request a specific set of properties for each entity or complex type.|
|`$top`|Use this to specify the number of items in the queried collection to be included in the result. |
|`$expand`|Use this to specify the related resources to be included in line with retrieved resources.|
|`$filter `|Use this to filter a collection of resources that are addressed by a request URL. The expression specified with $filter is evaluated for each resource in the collection, and only items where the expression evaluates to true are included in the response. Resources for which the expression evaluates to false or to null, or which reference properties that are unavailable due to permissions, are omitted from the response.|
|`$orderby`|Use this to request resources in a particular order.|
|`$count`|Use this to request a count of the matching resources included with the resources in the response.|

You can apply multiple options to a query. All query options must be separated from the resource path using '`?`'. After the first option, each option must be separated by '`&`'. The names of all options are case sensitive.

The following OData system query options are not supported by Dataverse Web API: `$skip`,`$search`,`$format`.

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

The following annotations are returned with the record with an annotation that follows this convention: `<lookup property name>@OData.Community.Display.V1.FormattedValue` as shown in the following example.

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

- `<lookup property name>@Microsoft.Dynamics.CRM.associatednavigationproperty` is the name of the corresponding single-valued navigation property.
- `<lookup property name>@Microsoft.Dynamics.CRM.lookuplogicalname` is the logical name of the related table.

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


## Order rows

## Filter rows

### Retrieve a count of rows

## Page results



## Aggregate data
