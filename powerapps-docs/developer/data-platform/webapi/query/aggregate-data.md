---
title: Aggregate data using OData
description: Learn how to use OData to retrieve aggregated data from Microsoft Dataverse Web API.
ms.date: 07/11/2024
ms.topic: how-to
author: MsSQLGirl
ms.author: jukoesma
ms.reviewer: jdaly
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
contributors: 
  - JimDaly
  - JosinaJoy
---
# Aggregate data using OData

Use the `$apply` option to aggregate and group your data.

The aggregate functions are limited to a collection of 50,000 records.  Further information around using aggregate functionality with Dataverse can be found here: [Aggregate data using FetchXml](../../fetchxml/aggregate-data.md).

You can find more information about OData data aggregation here: [OData extension for data aggregation version 4.0](https://docs.oasis-open.org/odata/odata-data-aggregation-ext/v4.0/cs01/odata-data-aggregation-ext-v4.0-cs01.html). Dataverse supports only a subset of these aggregate methods.

> [!NOTE]
> - `groupby` with datetime values is not supported.
> 
> - `$orderby` with aggregate values is not supported. This will return the error: `The query node SingleValueOpenPropertyAccess is not supported`.

## Examples

Following are some examples:

- [List of unique statuses in the query](#list-of-unique-statuses-in-the-query)
- [Count by status values](#count-by-status-values)
- [Aggregate sum of revenue](#aggregate-sum-of-revenue)
- [Average revenue based on status](#average-revenue-based-on-status)
- [Sum of revenue based on status](#sum-of-revenue-based-on-status)
- [Total account revenue by primary contact name](#total-account-revenue-by-primary-contact-name)
- [Primary contact names for accounts in 'WA'](#primary-contact-names-for-accounts-in-wa)
- [Last created record date and time](#last-created-record-date-and-time)
- [First created record date and time](#first-created-record-date-and-time)

These samples don't show the complete request and response for brevity.

### List of unique statuses in the query

```http
GET accounts?$apply=groupby((statuscode))
Prefer: odata.include-annotations="OData.Community.Display.V1.FormattedValue"
```

**Response body**

```json
{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#accounts",
    "value": [
        {
            "statuscode@OData.Community.Display.V1.FormattedValue": "Active",
            "statuscode": 1
        },
        {
            "statuscode@OData.Community.Display.V1.FormattedValue": "Inactive",
            "statuscode": 2
        }
    ]
}
```

### Count by status values

```http
GET accounts?$apply=groupby((statuscode),aggregate($count as count))
Prefer: odata.include-annotations="OData.Community.Display.V1.FormattedValue"
```

**Response body**

```json
{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#accounts",
    "value": [
        {
            "statuscode@OData.Community.Display.V1.FormattedValue": "Active",
            "statuscode": 1,
            "count@OData.Community.Display.V1.FormattedValue": "8",
            "count": 8
        },
        {
            "statuscode@OData.Community.Display.V1.FormattedValue": "Inactive",
            "statuscode": 2,
            "count@OData.Community.Display.V1.FormattedValue": "1",
            "count": 1
        }
    ]
}
```

### Aggregate sum of revenue

```http
GET accounts?$apply=aggregate(revenue with sum as total)
Prefer: odata.include-annotations="OData.Community.Display.V1.FormattedValue"
```

**Response body**

```json
{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#accounts",
    "value": [
        {
            "total@OData.Community.Display.V1.FormattedValue": "$440,000.00",
            "total": 440000.000000000
        }
    ]
}
```

### Average revenue based on status

```http
GET accounts?$apply=groupby((statuscode),aggregate(revenue with average as averagevalue))
Prefer: odata.include-annotations="OData.Community.Display.V1.FormattedValue"
```

**Response body**

```json
{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#accounts",
    "value": [
        {
            "statuscode@OData.Community.Display.V1.FormattedValue": "Active",
            "statuscode": 1,
            "averagevalue@OData.Community.Display.V1.FormattedValue": "$53,750.00",
            "averagevalue": 53750.000000000
        },
        {
            "statuscode@OData.Community.Display.V1.FormattedValue": "Inactive",
            "statuscode": 2,
            "averagevalue@OData.Community.Display.V1.FormattedValue": "$10,000.00",
            "averagevalue": 10000.000000000
        }
    ]
}
```

### Sum of revenue based on status

```http
GET accounts?$apply=groupby((statuscode),aggregate(revenue with sum as total))
Prefer: odata.include-annotations="OData.Community.Display.V1.FormattedValue"
```

**Response body**

```json
{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#accounts",
    "value": [
        {
            "statuscode@OData.Community.Display.V1.FormattedValue": "Active",
            "statuscode": 1,
            "total@OData.Community.Display.V1.FormattedValue": "$430,000.00",
            "total": 430000.000000000
        },
        {
            "statuscode@OData.Community.Display.V1.FormattedValue": "Inactive",
            "statuscode": 2,
            "total@OData.Community.Display.V1.FormattedValue": "$10,000.00",
            "total": 10000.000000000
        }
    ]
}
```

### Total account revenue by primary contact name

```http
GET accounts?$apply=groupby((primarycontactid/fullname),aggregate(revenue with sum as total))
Prefer: odata.include-annotations="OData.Community.Display.V1.FormattedValue"
```

**Response body**

```json
{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#accounts",
    "value": [
        {
            "total@OData.Community.Display.V1.FormattedValue": "$10,000.00",
            "total": 10000.000000000,
            "contact_fullname": "Jim Glynn (sample)"
        },
        {
            "total@OData.Community.Display.V1.FormattedValue": "$80,000.00",
            "total": 80000.000000000,
            "contact_fullname": "Maria Campbell (sample)"
        },
      ... <truncated for brevity>
      
    ]
}
```

### Primary contact names for accounts in 'WA'

```http
GET accounts?$apply=filter(address1_stateorprovince eq 'WA')/groupby((primarycontactid/fullname))
```

**Response body**

```json
{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#accounts",
    "value": [
        {
            "contact_fullname": "Rene Valdes (sample)"
        },
        {
            "contact_fullname": "Robert Lyon (sample)"
        },
        {
            "contact_fullname": "Scott Konersmann (sample)"
        }
    ]
}
```

### Last created record date and time

```http
GET accounts?$apply=aggregate(createdon with max as lastCreate)
Prefer: odata.include-annotations="OData.Community.Display.V1.FormattedValue"
```

**Response body**

```json
{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#accounts",
    "value": [
        {
            "lastCreate@OData.Community.Display.V1.FormattedValue": "3/25/2023 10:42 AM",
            "lastCreate": "2023-03-25T17:42:47Z"
        }
    ]
}
```

### First created record date and time

```http
GET accounts?$apply=aggregate(createdon with min as firstCreate)
Prefer: odata.include-annotations="OData.Community.Display.V1.FormattedValue"
```

**Response body**

```json
{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#accounts",
    "value": [
        {
            "firstCreate@OData.Community.Display.V1.FormattedValue": "3/25/2023 10:42 AM",
            "firstCreate": "2023-03-25T17:42:46Z"
        }
    ]
}
```

## Distinct column values

OData doesn't have a `$distinct` query option to restrict results to unique values. Instead, use the `$apply` system query option with the `groupby` transformation. This returns distinct values for each property.

**Request:**

```http
GET [Organization URI]/api/data/v9.2/accounts?$apply=groupby((statecode,statuscode,accountcategorycode))
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0
Prefer: odata.include-annotations="OData.Community.Display.V1.FormattedValue"
```

**Response:**

```http
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  
Preference-Applied: odata.include-annotations="OData.Community.Display.V1.FormattedValue"

{
   "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#accounts",
   "value": [
      {
         "statuscode": 1,
         "statecode": 0
      },
      {
         "statuscode": 1,
         "statecode": 0,
         "accountcategorycode": 1
      },
      {
         "statuscode": 1,
         "statecode": 0,
         "accountcategorycode": 2
      },
      {
         "statuscode": 2,
         "statecode": 1
      }
   ]
}
```

## OData aggregation limitations

This section describes capabilities that are available using aggregation with FetchXml that are not currently available using OData.

### Get distinct number with CountColumn

You can't get a distinct number of values using [CountColumn](xref:Microsoft.Xrm.Sdk.Query.XrmAggregateType.CountColumn) with OData. [Learn about distinct column values using FetchXml](../../fetchxml/aggregate-data.md#distinct-column-values)


### Time zone when grouping by date

Grouping by parts of a date always uses UTC time and there is no way to specify that the user's time zone should be used instead [available in FetchXml](../../fetchxml/aggregate-data.md#grouping-by-parts-of-a-date)


### Row aggregate

When a table has a [hierarchical relationship defined](../../../../maker/data-platform/query-visualize-hierarchical-data.md), you can't return a row aggregate on the lookup column for the hierarchical relationship. [Learn about row aggregates using FetchXml](../../fetchxml/aggregate-data.md#row-aggregate)

### Per query limit

There is no way to specify a configurable aggregate limit. [Learn about per query limits using FetchXml](../../fetchxml/aggregate-data.md#per-query-limit)


[!INCLUDE [cc-query-aggregation-limitations](../../includes/cc-query-aggregation-limitations.md)]

## Next steps

Learn how to count rows.

> [!div class="nextstepaction"]
> [Count rows](count-rows.md)

[!INCLUDE [footer-banner](../../../../includes/footer-banner.md)]