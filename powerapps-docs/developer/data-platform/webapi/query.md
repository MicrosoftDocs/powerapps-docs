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
  - bgribaudo
---
# Query data using the Web API (Microsoft Dataverse)

When you retrieve data with a query, you must make the following choices:

|Query element|Description|
|---------|---------|
|Select Columns|Choose which columns of data to return.|
|Join Tables|Choose which related tables to include in the results.|
|Order rows|Choose the order the results are returned.|
|Filter rows|Choose which rows of data to return.|
|Page results|Choose how many rows of data to return.|
|Aggregate data|Choose how to group and aggregate the data returned. |

This article explains how to apply these choices when constructing a query to retrieve data using the Dataverse Web API.

Every query begins with an EntitySet resource. To find all the EntitySet resources available in your environment, send a `GET` request to the Web API endpoint url:

**Request**

```http
GET [Organization URI]/api/data/v9.2/
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
      ...
```

More information:

- [Web API URL and versions](compose-http-requests-handle-errors.md#web-api-url-and-versions)
- [HTTP headers](compose-http-requests-handle-errors.md#http-headers)

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

- The localized labels for choice columns
- The primary name value for lookup properties
- Currency values with currency symbols
- Formatted date values in the user's time zone

To include formatted values in your results, use the `Prefer: odata.include-annotations="OData.Community.Display.V1.FormattedValue"` request header. This is one of several annotations you can request. More information: [Annotations](#annotations)

The formatted value will be returned with the record with an annotation that follows this convention: `<property name>@OData.Community.Display.V1.FormattedValue`.

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


### Annotations

In addition to properties, you can request different OData annotation data to be returned with the results using the `Prefer: odata.include-annotations` request header. You can choose to return all annotations, or specify specific annotations. The following table describes the annotations Dataverse Web API supports:


|Annotation|Description|
|---------|---------|
|`OData.Community.Display.V1.FormattedValue`|See [Formatted values](#formatted-values)|
|`Microsoft.Dynamics.CRM.associatednavigationproperty`<br />`Microsoft.Dynamics.CRM.lookuplogicalname`|When a [lookup property](web-api-properties.md#lookup-properties) represents a polymorphic relationship, use this data to understand which table row is related.<br />`associatednavigationproperty` is the name of the corresponding single-valued navigation property.<br />`lookuplogicalname` is the logical name of the related table.|
|`Microsoft.Dynamics.CRM.totalrecordcount`<br />`Microsoft.Dynamics.CRM.totalrecordcountlimitexceeded`|When you use the `$count` query option the `@odata.count` annotation tells the number of records, but only 5000 records can be returned at a time. Request the `Microsoft.Dynamics.CRM.totalrecordcountlimitexceeded` to get a boolean value that will tell you if the total number of records matching the query exceeds 5000.  More information: [Retrieve a count of rows](#retrieve-a-count-of-rows) |
|`Microsoft.Dynamics.CRM.globalmetadataversion`|This annotation is returned on the request and you can cache it in your application. This value will change when any schema change occurs. This is an indication that you may need to refresh any schema data that your application has cached. More information: [Cache Schema data](../cache-schema-data.md)|
|`Microsoft.PowerApps.CDS.ErrorDetails.OperationStatus`<br />`Microsoft.PowerApps.CDS.ErrorDetails.SubErrorCode`<br />`Microsoft.PowerApps.CDS.HelpLink`<br />`Microsoft.PowerApps.CDS.TraceText`<br />`Microsoft.PowerApps.CDS.InnerError.Message`|These annotations provide additional details when errors are returned. More information: [Include more details with errors](compose-http-requests-handle-errors.md#include-more-details-with-errors)|

It is common to use the `Prefer: odata.include-annotations="*"` request header to return all annotations.

If you want only specific annotations, you can request them as comma separated values. You can also use the '`*`' character as a wildcard.  For example, `Prefer: odata.include-annotations="OData.Community.Display.V1.FormattedValue,Microsoft.PowerApps.CDS.ErrorDetails*"` will include only the formatted values and any additional error detail annotations.

## Join Tables

## Order rows

## Filter rows

### Retrieve a count of rows

## Page results



## Aggregate data
